#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Constrói e serve versões antigas do Excalidraw para o conjunto de
reabertura da M2.4.2 (casos c2 a c5).

Para cada versão, clona a tag fora do repositório, constrói a imagem com o
Dockerfile da própria tag e sobe o contêiner numa porta própria. Se a tag
não tiver Dockerfile ou a construção falhar, usa um Dockerfile alternativo
com a imagem node:<major> declarada em VERSOES. Com a versão no ar, o
Playwright (Firefox) abre cena_referencia.excalidraw pelo menu Abrir e salva
a cena pelo comando Salvar em arquivo. O download é gravado sem alteração em
reabertura/<caso>_<versao>.excalidraw. O método de construção, a versão do
Node.js e o resultado do salvamento ficam em <work-dir>/registro.json, e as
capturas de tela em <work-dir>/capturas/.

Ao final, compara cada arquivo salvo com a cena de referência por
scripts/compara_elementos.py (relatórios em <work-dir>/comparacoes/) e gera
reabertura/manifesto.csv com os 7 casos da M2.4.2.

Uso:
  python scripts/gerar_massa_versoes_antigas.py [--versao v0.18.0] [--work-dir DIR]
  python scripts/gerar_massa_versoes_antigas.py --versao v0.18.0 --so-servir
  python scripts/gerar_massa_versoes_antigas.py --so-manifesto

Requer Docker, git e Playwright (pip install playwright e
python -m playwright install firefox).
"""

import argparse
import contextlib
import csv
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request

from gerar_massa_dados import COMMIT_AVALIADO, PNGS_REABERTURA, sha256_arquivo

URL_REPOSITORIO = "https://github.com/excalidraw/excalidraw.git"

# Versão, caso da M2.4.2, porta no host e imagem Node.js da construção alternativa.
# A alternativa usa um major aceito pelo campo engines do package.json da tag
# (>=14 na v0.15.0, >=18 na v0.16.4 e na v0.17.6, 18 a 22 na v0.18.0).
VERSOES = {
    "v0.15.0": {"caso": "c2", "porta": 3011, "node_alternativo": "16"},
    "v0.16.4": {"caso": "c3", "porta": 3012, "node_alternativo": "18"},
    "v0.17.6": {"caso": "c4", "porta": 3013, "node_alternativo": "18"},
    "v0.18.0": {"caso": "c5", "porta": 3014, "node_alternativo": "20"},
}

RAIZ_REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MASSA_DADOS = os.path.join(RAIZ_REPO, "dados", "fase-03", "massa-de-dados")
CENA_REFERENCIA = os.path.join(MASSA_DADOS, "cena_referencia.excalidraw")
DIR_REABERTURA = os.path.join(MASSA_DADOS, "reabertura")
MANIFESTO = os.path.join(DIR_REABERTURA, "manifesto.csv")
COMPARADOR = os.path.join(RAIZ_REPO, "scripts", "compara_elementos.py")

COLUNAS_MANIFESTO = [
    "caso",
    "arquivo",
    "origem",
    "versao",
    "node",
    "sha256",
    "elementos_referencia",
    "elementos_salvos",
    "ids_ausentes",
    "observacao",
]

WORK_DIR_PADRAO = os.path.join(os.path.expanduser("~"), ".cache", "karen-jones", "excalidraw-versoes")

# A pasta da build muda entre as tags (build/ até a v0.17.6, excalidraw-app/build/ na v0.18.0).
DOCKERFILE_ALTERNATIVO = """\
FROM node:{node} AS build
WORKDIR /opt/node_app
COPY . .
RUN yarn --network-timeout 600000
ARG NODE_ENV=production
RUN yarn build:app:docker
RUN mkdir -p /saida && if [ -d excalidraw-app/build ]; then cp -r excalidraw-app/build/. /saida/; \\
    else cp -r build/. /saida/; fi

FROM nginx:1.27-alpine
COPY --from=build /saida /usr/share/nginx/html
"""


# Algumas tags trazem um .dockerignore desatualizado que exclui index.html e
# vite.config.ts. A alternativa usa este ignore próprio (<Dockerfile>.dockerignore,
# lido pelo BuildKit no lugar do .dockerignore da tag).
DOCKERIGNORE_ALTERNATIVO = """\
.git
node_modules
build
excalidraw-app/build
"""


def executar(comando: list, **kwargs) -> subprocess.CompletedProcess:
    """Executa um comando mostrando-o antes e falha se ele terminar com erro."""
    print("$ " + " ".join(comando), flush=True)
    return subprocess.run(comando, check=True, **kwargs)


def preparar_clone(versao: str, work_dir: str) -> str:
    """Clona a tag no work-dir, reaproveitando um clone já existente da mesma tag."""
    destino = os.path.join(work_dir, f"excalidraw-{versao}")
    if os.path.isdir(os.path.join(destino, ".git")):
        tag = subprocess.run(
            ["git", "-C", destino, "describe", "--tags", "--exact-match"],
            capture_output=True,
            text=True,
        ).stdout.strip()
        if tag == versao:
            print(f"Clone de {versao} reaproveitado em {destino}")
            return destino
        print(f"[ERRO] {destino} existe mas não está na tag {versao}. Remova a pasta e rode de novo.")
        sys.exit(1)
    os.makedirs(work_dir, exist_ok=True)
    executar(["git", "clone", "--depth", "1", "--branch", versao, URL_REPOSITORIO, destino])
    return destino


def node_da_construcao(imagem_build: str) -> str:
    """Lê a versão do Node.js dentro da imagem do estágio de construção."""
    saida = subprocess.run(
        ["docker", "run", "--rm", imagem_build, "node", "--version"],
        capture_output=True,
        text=True,
        check=True,
    )
    return saida.stdout.strip()


def construir_imagem(versao: str, clone: str, work_dir: str) -> dict:
    """Constrói a imagem da versão e devolve imagem, método e Node.js usados."""
    imagem = f"excalidraw-{versao}"
    imagem_build = f"{imagem}-build"
    dockerfile_tag = os.path.join(clone, "Dockerfile")

    if os.path.isfile(dockerfile_tag):
        try:
            executar(["docker", "build", "-t", imagem, "."], cwd=clone)
            # O estágio "build" já está em cache, então esta etapa só marca a imagem.
            executar(["docker", "build", "--target", "build", "-t", imagem_build, "."], cwd=clone)
            return {
                "imagem": imagem,
                "metodo": "Dockerfile da tag",
                "node": node_da_construcao(imagem_build),
            }
        except subprocess.CalledProcessError as erro:
            print(f"[AVISO] Construção com o Dockerfile de {versao} falhou ({erro}). Usando a alternativa.")
    else:
        print(f"[AVISO] A tag {versao} não tem Dockerfile. Usando a alternativa.")

    node = VERSOES[versao]["node_alternativo"]
    dockerfile_alt = os.path.join(work_dir, f"Dockerfile.alternativo-{versao}")
    with open(dockerfile_alt, "w", encoding="utf-8") as f:
        f.write(DOCKERFILE_ALTERNATIVO.format(node=node))
    with open(dockerfile_alt + ".dockerignore", "w", encoding="utf-8") as f:
        f.write(DOCKERIGNORE_ALTERNATIVO)
    executar(["docker", "build", "-f", dockerfile_alt, "-t", imagem, "."], cwd=clone)
    executar(["docker", "build", "-f", dockerfile_alt, "--target", "build", "-t", imagem_build, "."], cwd=clone)
    return {
        "imagem": imagem,
        "metodo": f"Dockerfile alternativo com node:{node}",
        "node": node_da_construcao(imagem_build),
    }


def esperar_http_200(url: str, limite_s: int = 120) -> None:
    """Espera a página responder HTTP 200 ou falha ao fim do limite."""
    fim = time.time() + limite_s
    while time.time() < fim:
        try:
            with urllib.request.urlopen(url, timeout=5) as resposta:
                if resposta.status == 200:
                    print(f"{url} respondeu HTTP 200")
                    return
        except (urllib.error.URLError, ConnectionError, TimeoutError):
            pass
        time.sleep(1)
    raise TimeoutError(f"{url} não respondeu HTTP 200 em {limite_s} s")


@contextlib.contextmanager
def servir(versao: str, imagem: str, manter: bool = False):
    """Sobe o contêiner na porta da versão e o remove ao sair, mesmo com erro."""
    porta = VERSOES[versao]["porta"]
    nome = f"karen-jones-excalidraw-{versao}"
    subprocess.run(["docker", "rm", "-f", nome], capture_output=True)
    executar(["docker", "run", "-d", "--name", nome, "-p", f"127.0.0.1:{porta}:80", imagem], capture_output=True)
    url = f"http://127.0.0.1:{porta}"
    try:
        esperar_http_200(url)
        yield url
    finally:
        if manter:
            print(f"Contêiner {nome} mantido em {url}. Para remover: docker rm -f {nome}")
        else:
            subprocess.run(["docker", "rm", "-f", nome], capture_output=True)
            print(f"Contêiner {nome} removido")


def registrar(work_dir: str, versao: str, dados: dict, mesclar: bool = False) -> None:
    """Grava a construção e o salvamento da versão em registro.json.

    Com mesclar, preserva o resultado de salvamento já registrado.
    """
    caminho = os.path.join(work_dir, "registro.json")
    registro = {}
    if os.path.isfile(caminho):
        with open(caminho, "r", encoding="utf-8") as f:
            registro = json.load(f)
    registro[versao] = {**registro.get(versao, {}), **dados} if mesclar else dados
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(registro, f, indent=2, ensure_ascii=False)
        f.write("\n")


# O botão do menu principal se chama dropdown-menu-button na v0.15.0 e
# main-menu-trigger nas versões seguintes.
GATILHO_MENU = '[data-testid="main-menu-trigger"], [data-testid="dropdown-menu-button"]'


def abrir_menu(pagina, item: str) -> None:
    """Garante o menu principal aberto e clica no item pelo data-testid."""
    alvo = pagina.locator(f'[data-testid="{item}"]')
    if not alvo.is_visible():
        pagina.locator(GATILHO_MENU).first.click()
    alvo.click()


def elementos_ativos(caminho: str) -> int:
    """Conta os elementos não excluídos de um arquivo .excalidraw."""
    with open(caminho, "r", encoding="utf-8") as f:
        cena = json.load(f)
    if cena.get("type") != "excalidraw":
        raise ValueError(f'campo "type" é {cena.get("type")!r}, esperado "excalidraw"')
    return sum(1 for e in cena.get("elements", []) if not e.get("isDeleted"))


def salvar_pela_interface(versao: str, url: str, work_dir: str) -> dict:
    """Abre a cena de referência na versão servida e salva pela própria interface.

    O arquivo só é gravado em reabertura/ se a aplicação devolver um JSON
    válido com ao menos um elemento ativo. Em caso de falha, nada é gravado e
    o erro volta no resultado.
    """
    from playwright.sync_api import Error as ErroPlaywright
    from playwright.sync_api import sync_playwright

    caso = VERSOES[versao]["caso"]
    destino = os.path.join(DIR_REABERTURA, f"{caso}_{versao}.excalidraw")
    capturas = os.path.join(work_dir, "capturas")
    os.makedirs(capturas, exist_ok=True)

    try:
        with sync_playwright() as p, tempfile.TemporaryDirectory() as temp:
            navegador = p.firefox.launch()
            try:
                pagina = navegador.new_page(accept_downloads=True, viewport={"width": 1280, "height": 800})
                pagina.goto(url)
                pagina.locator(GATILHO_MENU).first.wait_for(timeout=60000)

                with pagina.expect_file_chooser() as escolha:
                    abrir_menu(pagina, "load-button")
                escolha.value.set_files(CENA_REFERENCIA)
                pagina.wait_for_timeout(3000)
                pagina.screenshot(path=os.path.join(capturas, f"{versao}-aberta.png"))
                if pagina.locator(".ErrorDialog").count():
                    raise RuntimeError("a aplicação mostrou um erro ao abrir a cena")

                abrir_menu(pagina, "json-export-button")
                with pagina.expect_download() as baixado:
                    pagina.get_by_role("button", name="Save to file").click()
                pagina.screenshot(path=os.path.join(capturas, f"{versao}-salva.png"))
                temporario = os.path.join(temp, "salvo.excalidraw")
                baixado.value.save_as(temporario)
            finally:
                navegador.close()

            ativos = elementos_ativos(temporario)
            if ativos == 0:
                raise RuntimeError("a cena salva está vazia")
            os.makedirs(DIR_REABERTURA, exist_ok=True)
            shutil.copyfile(temporario, destino)
    except (ErroPlaywright, RuntimeError, ValueError, json.JSONDecodeError) as erro:
        print(f"[ERRO] {versao} não salvou a cena: {erro}. Nenhum arquivo gravado.")
        return {"salvamento": "falha", "erro": str(erro)}

    arquivo = os.path.relpath(destino, MASSA_DADOS)
    print(f"Cena salva pela {versao} em {arquivo} ({ativos} elementos ativos)")
    return {"salvamento": "ok", "arquivo": arquivo, "elementos_salvos": ativos}


def comparar_com_referencia(caso: str, arquivo: str, work_dir: str) -> dict:
    """Roda compara_elementos.py contra a cena de referência e lê o relatório.

    Os relatórios JSON e CSV ficam em <work-dir>/comparacoes/, fora do repositório.
    """
    pasta = os.path.join(work_dir, "comparacoes")
    os.makedirs(pasta, exist_ok=True)
    relatorio_json = os.path.join(pasta, f"{caso}.json")
    executar(
        [
            sys.executable,
            COMPARADOR,
            "--original",
            CENA_REFERENCIA,
            "--reimportados",
            arquivo,
            "--output-json",
            relatorio_json,
            "--output-csv",
            os.path.join(pasta, f"{caso}.csv"),
        ],
        capture_output=True,
    )
    with open(relatorio_json, "r", encoding="utf-8") as f:
        return json.load(f)[os.path.basename(arquivo)]


def linha_versao_antiga(versao: str, registro: dict, work_dir: str) -> dict:
    """Monta a linha do manifesto de um caso salvo por versão antiga (c2 a c5)."""
    caso = VERSOES[versao]["caso"]
    dados = registro.get(versao, {})
    referencia = elementos_ativos(CENA_REFERENCIA)
    linha = {
        "caso": caso,
        "arquivo": "",
        "origem": f"Salvo pela interface da {versao} ({dados.get('metodo', 'construção não registrada')})",
        "versao": versao,
        "node": dados.get("node", ""),
        "sha256": "",
        "elementos_referencia": referencia,
        "elementos_salvos": "",
        "ids_ausentes": "",
        "observacao": "",
    }
    arquivo = os.path.join(DIR_REABERTURA, f"{caso}_{versao}.excalidraw")
    if dados.get("salvamento") != "ok" or not os.path.isfile(arquivo):
        erro = dados.get("erro", "versão não processada")
        linha["observacao"] = f"Pendência: a versão não salvou a cena ({erro})."
        return linha

    resultado = comparar_com_referencia(caso, arquivo, work_dir)
    with open(CENA_REFERENCIA, "r", encoding="utf-8") as f:
        tipos = {e["id"]: e["type"] for e in json.load(f)["elements"]}
    ausentes = [d for d in resultado["detalhes"] if d["motivo"].startswith("Elemento não encontrado")]
    divergentes = [d for d in resultado["detalhes"] if not d["preservado"] and d not in ausentes]

    observacoes = []
    if ausentes:
        lista = ", ".join(f"{d['id']} ({tipos.get(d['id'], d['tipo'])})" for d in ausentes)
        observacoes.append(f"Elementos ausentes no arquivo salvo: {lista}.")
    if divergentes:
        lista = ", ".join(
            f"{d['id']} ({', '.join(m.split(' ')[0] for m in d['motivo'].split('; '))})" for d in divergentes
        )
        observacoes.append(f"Propriedades alteradas ao salvar: {lista}.")
    if not observacoes:
        observacoes.append("Todos os elementos da referência preservados ao salvar.")

    linha.update(
        {
            "arquivo": os.path.basename(arquivo),
            "sha256": sha256_arquivo(arquivo),
            "elementos_salvos": elementos_ativos(arquivo),
            "ids_ausentes": " ".join(d["id"] for d in ausentes),
            "observacao": " ".join(observacoes),
        }
    )
    return linha


def gerar_manifesto(work_dir: str) -> str:
    """Gera reabertura/manifesto.csv com os 7 casos do conjunto de reabertura."""
    registro = {}
    caminho_registro = os.path.join(work_dir, "registro.json")
    if os.path.isfile(caminho_registro):
        with open(caminho_registro, "r", encoding="utf-8") as f:
            registro = json.load(f)

    referencia = elementos_ativos(CENA_REFERENCIA)
    linhas = [
        {
            "caso": "c1",
            "arquivo": "../cena_referencia.excalidraw",
            "origem": "Gerado por scripts/gerar_massa_dados.py",
            "versao": COMMIT_AVALIADO[:8],
            "node": "",
            "sha256": sha256_arquivo(CENA_REFERENCIA),
            "elementos_referencia": referencia,
            "elementos_salvos": referencia,
            "ids_ausentes": "",
            "observacao": "Cena de referência do conjunto, importada pelas versões antigas em c2 a c5.",
        }
    ]
    linhas += [linha_versao_antiga(versao, registro, work_dir) for versao in VERSOES]

    for caso, nome_origem, nome_png in PNGS_REABERTURA:
        png = os.path.join(DIR_REABERTURA, nome_png)
        cena = os.path.join(DIR_REABERTURA, f"{caso}_referencia.excalidraw")
        existe = os.path.isfile(png) and os.path.isfile(cena)
        ativos = elementos_ativos(cena) if existe else ""
        linhas.append(
            {
                "caso": caso,
                "arquivo": nome_png,
                "origem": f"Fixture {nome_origem} do commit avaliado",
                "versao": COMMIT_AVALIADO[:8],
                "node": "",
                "sha256": sha256_arquivo(png) if os.path.isfile(png) else "",
                "elementos_referencia": ativos,
                "elementos_salvos": ativos,
                "ids_ausentes": "",
                "observacao": (
                    f"Referência é a cena incorporada no PNG, extraída em {caso}_referencia.excalidraw."
                    if existe
                    else "Pendência: rode scripts/gerar_massa_dados.py --so-reabertura-png."
                ),
            }
        )

    with open(MANIFESTO, "w", encoding="utf-8", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=COLUNAS_MANIFESTO)
        escritor.writeheader()
        escritor.writerows(linhas)
    print(f"\nManifesto com {len(linhas)} casos salvo em {os.path.relpath(MANIFESTO, RAIZ_REPO)}")
    return MANIFESTO


def processar_versao(versao: str, work_dir: str, so_servir: bool) -> bool:
    """Clona, constrói e serve uma versão e salva a cena por ela.

    Devolve False se o salvamento falhar. Com so_servir, só deixa a versão no ar.
    """
    print(f"\n== {versao} ({VERSOES[versao]['caso']}) ==")
    clone = preparar_clone(versao, work_dir)
    construcao = construir_imagem(versao, clone, work_dir)
    print(f"Construção: {construcao['metodo']}, Node.js {construcao['node']}")
    dados = {"caso": VERSOES[versao]["caso"], **construcao}
    with servir(versao, construcao["imagem"], manter=so_servir) as url:
        if so_servir:
            registrar(work_dir, versao, dados, mesclar=True)
            return True
        dados.update(salvar_pela_interface(versao, url, work_dir))
    registrar(work_dir, versao, dados)
    return dados["salvamento"] == "ok"


def main():
    parser = argparse.ArgumentParser(
        description="Constrói e serve versões antigas do Excalidraw para o conjunto de reabertura da M2.4.2"
    )
    parser.add_argument(
        "--versao",
        choices=list(VERSOES),
        help="Versão a processar (padrão: todas)",
    )
    parser.add_argument(
        "--work-dir",
        default=WORK_DIR_PADRAO,
        help=f"Pasta dos clones e do registro, fora do repositório (padrão: {WORK_DIR_PADRAO})",
    )
    parser.add_argument(
        "--so-servir",
        action="store_true",
        help="Mantém o contêiner no ar para inspeção manual",
    )
    parser.add_argument(
        "--so-manifesto",
        action="store_true",
        help="Só regenera reabertura/manifesto.csv a partir do registro e dos arquivos já salvos",
    )
    args = parser.parse_args()

    work_dir = os.path.abspath(os.path.expanduser(args.work_dir))
    if os.path.commonpath([work_dir, RAIZ_REPO]) == RAIZ_REPO:
        print(f"[ERRO] --work-dir {work_dir} está dentro do repositório. Use uma pasta fora dele.")
        sys.exit(1)

    if args.so_manifesto:
        gerar_manifesto(work_dir)
        return

    versoes = [args.versao] if args.versao else list(VERSOES)
    falhas = []
    for versao in versoes:
        try:
            if not processar_versao(versao, work_dir, args.so_servir):
                falhas.append(versao)
        except (subprocess.CalledProcessError, TimeoutError) as erro:
            print(f"[ERRO] {versao}: {erro}")
            falhas.append(versao)

    if not args.so_servir:
        gerar_manifesto(work_dir)

    if falhas:
        print(f"\nVersões com falha: {', '.join(falhas)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
