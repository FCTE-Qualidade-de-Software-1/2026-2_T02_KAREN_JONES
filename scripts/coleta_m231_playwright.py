"""Coleta automatizada da métrica M2.3.1 com Playwright no Firefox.

Abre cada arquivo inválido de dados/fase-03/massa-de-dados/invalidos/ pelo menu
e arrastando para o editor, registra se o editor mostra uma mensagem e se ainda
permite criar um retângulo e um texto sem recarregar a página, e salva uma captura de tela
de cada tentativa. O critério é o da ficha de M2.3.1 em
docs/fase-02/gqm-confiabilidade.md.

Uso:
    python scripts/coleta_m231_playwright.py --url http://localhost:3000 \
        --saida dados/fase-04/brutos/acao-melhoria/M2.3.1/antes \
        --commit <sha da base>

O editor precisa estar rodando em modo de desenvolvimento (yarn start), que
expõe window.h com os elementos da cena.
"""

import argparse
import base64
import csv
import datetime
import importlib.metadata
import mimetypes
from pathlib import Path

from playwright.sync_api import sync_playwright

RAIZ = Path(__file__).resolve().parent.parent
PASTA_INVALIDOS = RAIZ / "dados" / "fase-03" / "massa-de-dados" / "invalidos"
ESPERA_MENSAGEM_MS = 5000

SOLTAR_ARQUIVO = """
async ({nome, tipo, conteudo}) => {
  const bytes = Uint8Array.from(atob(conteudo), (c) => c.charCodeAt(0));
  const arquivo = new File([bytes], nome, {type: tipo});
  const transferencia = new DataTransfer();
  transferencia.items.add(arquivo);
  const alvo = document.querySelector("canvas.interactive");
  for (const tipoEvento of ["dragenter", "dragover", "drop"]) {
    alvo.dispatchEvent(new DragEvent(tipoEvento, {
      bubbles: true, cancelable: true, dataTransfer: transferencia,
    }));
  }
}
"""

# No Firefox controlado pelo Playwright, interceptar a janela de escolha de
# arquivo dispara o evento "cancel" no <input type="file">, e a biblioteca
# browser-fs-access trata isso como desistência do usuário. O script bloqueia
# esse evento para simular quem escolhe um arquivo na janela.
IGNORAR_CANCELAMENTO = """
window.addEventListener("cancel", (evento) => {
  if (evento.target instanceof HTMLInputElement && evento.target.type === "file") {
    evento.stopPropagation();
  }
}, true);
"""

CONTAR_RETANGULOS = """
() => (window.h && window.h.elements ? window.h.elements : [])
  .filter((e) => e.type === "rectangle" && !e.isDeleted).length
"""


def abrir_editor(pagina, url):
    pagina.goto(url)
    pagina.wait_for_selector("canvas.interactive", timeout=30000)
    pagina.wait_for_timeout(500)


def abrir_pelo_menu(pagina, arquivo):
    pagina.click('[data-testid="main-menu-trigger"]')
    with pagina.expect_file_chooser() as escolha:
        pagina.click('[data-testid="load-button"]')
    escolha.value.set_files(str(arquivo))


def abrir_arrastando(pagina, arquivo):
    tipo = mimetypes.guess_type(arquivo.name)[0] or "application/json"
    conteudo = base64.b64encode(arquivo.read_bytes()).decode()
    pagina.evaluate(
        SOLTAR_ARQUIVO, {"nome": arquivo.name, "tipo": tipo, "conteudo": conteudo}
    )


def ler_mensagem(pagina):
    dialogo = pagina.locator(".Modal.Dialog")
    try:
        dialogo.first.wait_for(state="visible", timeout=ESPERA_MENSAGEM_MS)
    except Exception:
        return ""
    return " ".join(dialogo.first.inner_text().split())


def fechar_dialogo(pagina):
    fundo = pagina.locator(".Modal__background")
    if fundo.count() > 0:
        fundo.first.click(position={"x": 5, "y": 5}, force=True)
        pagina.wait_for_timeout(300)


def editor_vivo(pagina):
    return pagina.locator("canvas.interactive").count() > 0


def criar_formas(pagina):
    """Desenha um retângulo e insere um texto, como na coleta manual."""
    try:
        antes = pagina.evaluate(CONTAR_RETANGULOS)
        caixa = pagina.locator("canvas.interactive").bounding_box()
        x = caixa["x"] + caixa["width"] / 2
        y = caixa["y"] + caixa["height"] / 2
        pagina.keyboard.press("r")
        pagina.mouse.move(x, y)
        pagina.mouse.down()
        pagina.mouse.move(x + 120, y + 80, steps=5)
        pagina.mouse.up()
        pagina.wait_for_timeout(500)
        if not editor_vivo(pagina):
            return False, "editor sumiu da tela ao desenhar o retângulo"
        if pagina.evaluate(CONTAR_RETANGULOS) <= antes:
            return False, "nenhum retângulo novo na cena"
        pagina.keyboard.press("Escape")
        pagina.keyboard.press("t")
        pagina.mouse.click(x - 200, y - 150)
        pagina.keyboard.type("teste")
        pagina.keyboard.press("Escape")
        pagina.wait_for_timeout(700)
        if not editor_vivo(pagina):
            return False, "editor sumiu da tela ao inserir texto"
        return True, ""
    except Exception as erro:  # o editor pode cair ao desenhar
        return False, f"erro ao desenhar: {str(erro).splitlines()[0]}"


def tentar(navegador, url, arquivo, via, pasta_prints):
    contexto = navegador.new_context(viewport={"width": 1280, "height": 800})
    contexto.add_init_script(IGNORAR_CANCELAMENTO)
    pagina = contexto.new_page()
    erros = []
    pagina.on("pageerror", lambda erro: erros.append(str(erro).splitlines()[0]))
    abrir_editor(pagina, url)
    if via == "menu":
        abrir_pelo_menu(pagina, arquivo)
    else:
        abrir_arrastando(pagina, arquivo)
    mensagem = ler_mensagem(pagina)
    pagina.screenshot(path=str(pasta_prints / f"{arquivo.stem}_{via}_mensagem.png"))
    fechar_dialogo(pagina)
    criado, motivo = criar_formas(pagina)
    pagina.screenshot(path=str(pasta_prints / f"{arquivo.stem}_{via}_retangulo.png"))
    contexto.close()
    observacao = "; ".join(filter(None, [motivo] + [f"pageerror: {e}" for e in erros]))
    return {
        "arquivo": arquivo.name,
        "via": via,
        "mensagem_exibida": "sim" if mensagem else "nao",
        "texto_mensagem": mensagem,
        "retangulo_criado": "sim" if criado else "nao",
        "caso_tratado": "sim" if mensagem and criado else "nao",
        "observacao": observacao,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--url", default="http://localhost:3000")
    parser.add_argument("--saida", required=True, type=Path)
    parser.add_argument("--commit", required=True)
    args = parser.parse_args()

    pasta_prints = args.saida / "prints"
    pasta_prints.mkdir(parents=True, exist_ok=True)
    arquivos = sorted(PASTA_INVALIDOS.iterdir())
    inicio = datetime.datetime.now().astimezone().isoformat(timespec="seconds")

    with sync_playwright() as p:
        navegador = p.firefox.launch()
        versao_firefox = navegador.version
        tentativas = [
            tentar(navegador, args.url, arquivo, via, pasta_prints)
            for arquivo in arquivos
            for via in ("menu", "arrastar")
        ]
        navegador.close()

    campos = list(tentativas[0])
    with open(args.saida / "M2.3.1_tentativas.csv", "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(tentativas)

    casos = []
    for arquivo in arquivos:
        por_via = {t["via"]: t["caso_tratado"] for t in tentativas if t["arquivo"] == arquivo.name}
        tratado = "sim" if all(v == "sim" for v in por_via.values()) else "nao"
        casos.append({
            "arquivo": arquivo.name,
            "tratado_menu": por_via["menu"],
            "tratado_arrastar": por_via["arrastar"],
            "tratado_consolidado": tratado,
        })
    with open(args.saida / "M2.3.1_casos.csv", "w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=list(casos[0]))
        escritor.writeheader()
        escritor.writerows(casos)

    tratados = sum(c["tratado_consolidado"] == "sim" for c in casos)
    fim = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    with open(args.saida / "M2.3.1_coleta.txt", "w", encoding="utf-8") as f:
        f.write(
            f"commit: {args.commit}\nurl: {args.url}\ninicio: {inicio}\nfim: {fim}\n"
            f"navegador: Firefox {versao_firefox} (Playwright "
            f"{importlib.metadata.version('playwright')}, headless)\n"
            f"resultado: {tratados} de {len(casos)} casos tratados "
            f"({100 * tratados / len(casos):.2f}%)\n"
        )
    print(f"{tratados} de {len(casos)} casos tratados")


if __name__ == "__main__":
    main()
