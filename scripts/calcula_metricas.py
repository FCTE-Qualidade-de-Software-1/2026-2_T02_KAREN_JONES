#!/usr/bin/env python3
"""
Calcula as métricas de G1 (Manutenibilidade) a partir dos dados brutos.

Lê dados/fase-04/brutos/, aplica o procedimento de cada ficha e grava:

- dados/fase-04/consolidados/metricas.csv: uma linha por valor pontuado, no
  formato da seção 3 do plano de análise. As linhas de outros grupos (G2, G3)
  que já estiverem no arquivo são mantidas.
- dados/fase-04/consolidados/G1_detalhes.csv: os valores das fichas que não
  são pontuados diretamente (por pacote, por faixa, por nível etc.).
- dados/fase-04/consolidados/G1_verificacao.csv: a lista de verificação de
  cada métrica (dado bruto, fatores e recálculo).

M1.3.1 precisa do código-fonte no commit avaliado para contar as linhas de
cada função. Informe o clone em EXC ou em --exc.

Uso, a partir da raiz do repositório:
    EXC=/caminho/do/clone python3 scripts/calcula_metricas.py
"""

import argparse
import csv
import glob
import json
import os
import re
import statistics
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
BRUTOS = RAIZ / "dados" / "fase-04" / "brutos"
CONSOLIDADOS = RAIZ / "dados" / "fase-04" / "consolidados"
BRUTOS_REL = "dados/fase-04/brutos"

COMMIT = "e1b7aacb356a492aa1e0fc6eb57b8896124027f0"
DATA_COLETA = "2026-11-11"
AVALIADOR = "wChrstphr"

PACOTES = ["common", "element", "excalidraw", "fractional-indexing",
           "laser-pointer", "math", "utils", "excalidraw-app"]
BASE = {"common", "element", "fractional-indexing", "laser-pointer", "math", "utils"}
PARES_POSSIVEIS = len(PACOTES) * (len(PACOTES) - 1) // 2  # 28

COLUNAS = ["metrica", "item", "valor", "unidade", "status", "motivo",
           "arquivo_bruto", "data", "avaliador"]


# ---------------------------------------------------------------- utilitários

def bruto(nome):
    return BRUTOS / nome


def ler_json(nome):
    with open(bruto(nome), encoding="utf-8") as f:
        return json.load(f)


def ler_csv(nome):
    with open(bruto(nome), encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def pacote(caminho):
    """Pacote de um caminho relativo à raiz do Excalidraw, ou None."""
    if caminho.startswith("excalidraw-app/"):
        return "excalidraw-app"
    m = re.match(r"packages/([^/]+)/", caminho)
    if m and m.group(1) in PACOTES:
        return m.group(1)
    return None


def eh_producao(caminho):
    """Convenção de código de produção de G1, aplicada ao nome do arquivo."""
    if pacote(caminho) is None:
        return False
    if not re.search(r"\.tsx?$", caminho):
        return False
    if re.search(r"\.test\.tsx?$|\.d\.ts$", caminho):
        return False
    partes = caminho.split("/")
    return not ({"node_modules", "tests", "__snapshots__", "examples"} & set(partes))


def producao():
    with open(bruto("M1.1.1_arquivos-producao.txt"), encoding="utf-8") as f:
        return [l.strip() for l in f if l.strip()]


def relativo(caminho_abs):
    """Corta o prefixo do clone de um caminho absoluto."""
    m = re.search(r"(?:^|/)((?:packages|excalidraw-app)/.*)$", caminho_abs)
    return m.group(1) if m else caminho_abs


def pct(parte, total):
    return round(parte / total * 100, 2) if total else None


class Saida:
    def __init__(self):
        self.metricas = []
        self.detalhes = []

    def valor(self, metrica, valor, unidade, arquivo, item="", motivo=""):
        self.metricas.append({
            "metrica": metrica, "item": item,
            "valor": "" if valor is None else valor, "unidade": unidade,
            "status": "coletada" if valor is not None else "nao_coletada",
            "motivo": motivo, "arquivo_bruto": f"{BRUTOS_REL}/{arquivo}",
            "data": DATA_COLETA, "avaliador": AVALIADOR,
        })

    def detalhe(self, metrica, item, medida, valor, unidade):
        self.detalhes.append({"metrica": metrica, "item": item, "medida": medida,
                              "valor": valor, "unidade": unidade})


# ------------------------------------------------------------ Q1.1 e Q1.2

def grafo_producao():
    """Arestas arquivo → arquivo entre arquivos de produção."""
    prod = set(producao())
    grafo = ler_json("M1.1.1_grafo-madge.json")
    return {a: [b for b in destinos if b in prod]
            for a, destinos in grafo.items() if a in prod}


def arestas_pacotes(grafo):
    arestas = set()
    for a, destinos in grafo.items():
        for b in destinos:
            pa, pb = pacote(a), pacote(b)
            if pa != pb:
                arestas.add((pa, pb))
    return arestas


def alcance(arestas):
    adj = defaultdict(set)
    for a, b in arestas:
        adj[a].add(b)
    resultado = {}
    for p in PACOTES:
        vistos, pilha = set(), [p]
        while pilha:
            for v in adj[pilha.pop()]:
                if v not in vistos:
                    vistos.add(v)
                    pilha.append(v)
        resultado[p] = vistos
    return resultado


def m111(s, grafo):
    arestas = arestas_pacotes(grafo)
    alc = alcance(arestas)
    pares = sorted({tuple(sorted((a, b))) for a in PACOTES for b in alc[a]
                    if a != b and a in alc[b]})
    for a, b in pares:
        s.detalhe("M1.1.1", f"{a} e {b}", "par em ciclo", 1, "par")
    s.detalhe("M1.1.1", "", "pares em ciclo", len(pares), "pares")
    s.valor("M1.1.1", pct(len(pares), PARES_POSSIVEIS), "%", "M1.1.1_grafo-madge.json")


def m112(s, grafo):
    entre = violacoes = 0
    for a, destinos in grafo.items():
        for b in destinos:
            pa, pb = pacote(a), pacote(b)
            if pa == pb:
                continue
            entre += 1
            if (pa in BASE and pb == "excalidraw") or pb == "excalidraw-app":
                violacoes += 1
                s.detalhe("M1.1.2", f"{a} -> {b}", "importação que viola a direção", 1, "importação")
    s.detalhe("M1.1.2", "", "importações que violam a direção", violacoes, "importações")
    s.detalhe("M1.1.2", "", "importações de valor entre pacotes diferentes", entre, "importações")
    s.valor("M1.1.2", pct(violacoes, entre), "%", "M1.1.1_grafo-madge.json")


def m113(s, grafo):
    arestas = arestas_pacotes(grafo)
    inst = {}
    for p in PACOTES:
        ca = len({a for a, b in arestas if b == p})
        ce = len({b for a, b in arestas if a == p})
        i = round(ce / (ca + ce), 4) if ca + ce else None
        inst[p] = i
        s.detalhe("M1.1.3", p, "Ca", ca, "pacotes")
        s.detalhe("M1.1.3", p, "Ce", ce, "pacotes")
        s.detalhe("M1.1.3", p, "I", "não aplicável" if i is None else i, "adimensional")
    contrarias = [(a, b) for a, b in sorted(arestas)
                  if inst[a] is not None and inst[b] is not None and inst[a] < inst[b]]
    for a, b in contrarias:
        s.detalhe("M1.1.3", f"{a} -> {b}", "dependência que contraria o princípio", 1, "dependência")
    s.detalhe("M1.1.3", "", "dependências entre pacotes", len(arestas), "dependências")
    s.valor("M1.1.3", pct(len(contrarias), len(arestas)), "%", "M1.1.1_grafo-madge.json")


def m121(s, grafo):
    marcados = {l["arquivo"] for l in ler_csv("M1.2.1_arquivos-diretos.csv")
                if l["valida"].strip().lower() == "sim"}
    # Arquivos que alcançam algum marcado pelo grafo (dependência transitiva).
    reverso = defaultdict(set)
    for a, destinos in grafo.items():
        for b in destinos:
            reverso[b].add(a)
    alcancam, pilha = set(), list(marcados)
    while pilha:
        for a in reverso[pilha.pop()]:
            if a not in alcancam:
                alcancam.add(a)
                pilha.append(a)
    prod = producao()
    tot_dep = tot_arq = 0
    for p in sorted(BASE):
        arquivos = [f for f in prod if pacote(f) == p]
        diretos = [f for f in arquivos if f in marcados]
        transitivos = [f for f in arquivos if f not in marcados and f in alcancam]
        tot_dep += len(diretos) + len(transitivos)
        tot_arq += len(arquivos)
        s.detalhe("M1.2.1", p, "arquivos com dependência direta", len(diretos), "arquivos")
        s.detalhe("M1.2.1", p, "arquivos só com dependência transitiva", len(transitivos), "arquivos")
        s.detalhe("M1.2.1", p, "arquivos de produção", len(arquivos), "arquivos")
        s.detalhe("M1.2.1", p, "proporção", pct(len(diretos) + len(transitivos), len(arquivos)), "%")
    s.valor("M1.2.1", pct(tot_dep, tot_arq), "%", "M1.2.1_arquivos-diretos.csv")


def m122(s):
    linhas = ler_csv("M1.2.2_propriedades.csv")
    doc = sum(1 for l in linhas if l["documentada"].strip().lower() == "sim")
    s.detalhe("M1.2.2", "", "propriedades documentadas", doc, "propriedades")
    s.detalhe("M1.2.2", "", "propriedades", len(linhas), "propriedades")
    s.valor("M1.2.2", pct(doc, len(linhas)), "%", "M1.2.2_propriedades.csv")


# ------------------------------------------------------------------- Q1.3

FAIXAS_CC = [("baixo", 1, 10), ("moderado", 11, 20), ("alto", 21, 50), ("muito_alto", 51, 10**9)]


def linhas_de_codigo(texto):
    """Conjunto dos números de linha (1-based) que não são branco nem comentário."""
    codigo, em_bloco = set(), False
    for n, linha in enumerate(texto.splitlines(), start=1):
        t = linha.strip()
        resto = ""
        while t:
            if em_bloco:
                fim = t.find("*/")
                if fim < 0:
                    t = ""
                else:
                    em_bloco, t = False, t[fim + 2:].strip()
                continue
            if t.startswith("//"):
                break
            if t.startswith("/*"):
                em_bloco, t = True, t[2:]
                continue
            resto = t
            break
        if resto:
            codigo.add(n)
    return codigo


def m131(s, exc):
    prod = set(producao())
    funcoes = defaultdict(list)  # arquivo -> [(linha, fim, complexidade)]
    for arq in ler_json("M1.3.1_eslint.json"):
        rel = relativo(arq["filePath"])
        if rel not in prod:
            continue
        for m in arq["messages"]:
            if m.get("ruleId") != "complexity" or m["message"].startswith("Class field initializer"):
                continue
            cc = int(re.search(r"complexity of (\d+)", m["message"]).group(1))
            funcoes[rel].append((m["line"], m["endLine"], cc))

    linhas_faixa = defaultdict(lambda: defaultdict(int))  # pacote -> faixa -> linhas
    funcoes_faixa = defaultdict(int)
    arquivos_alto = defaultdict(int)
    for rel, fs in funcoes.items():
        codigo = linhas_de_codigo((Path(exc) / rel).read_text(encoding="utf-8"))
        for i, (ini, fim, cc) in enumerate(fs):
            proprias = {n for n in codigo if ini <= n <= fim}
            for j, (ini2, fim2, _) in enumerate(fs):
                # Funções declaradas dentro desta (intervalo contido e diferente).
                if j != i and ini <= ini2 and fim2 <= fim and (ini2, fim2) != (ini, fim):
                    proprias -= set(range(ini2, fim2 + 1))
            faixa = next(n for n, a, b in FAIXAS_CC if a <= cc <= b)
            linhas_faixa[pacote(rel)][faixa] += len(proprias)
            linhas_faixa["total"][faixa] += len(proprias)
            funcoes_faixa[faixa] += 1
            if faixa in ("alto", "muito_alto"):
                arquivos_alto[rel] += len(proprias)

    for p in PACOTES + ["total"]:
        tot = sum(linhas_faixa[p].values())
        for faixa, _, _ in FAIXAS_CC:
            s.detalhe("M1.3.1", p, f"linhas em risco {faixa}", pct(linhas_faixa[p][faixa], tot), "%")
    nfun = sum(funcoes_faixa.values())
    for faixa, _, _ in FAIXAS_CC:
        s.detalhe("M1.3.1", "total", f"funções em risco {faixa}", pct(funcoes_faixa[faixa], nfun), "%")
    s.detalhe("M1.3.1", "total", "funções analisadas", nfun, "funções")
    for rel, n in sorted(arquivos_alto.items(), key=lambda x: -x[1])[:10]:
        s.detalhe("M1.3.1", rel, "linhas em risco alto ou muito alto", n, "linhas")
    tot = sum(linhas_faixa["total"].values())
    for faixa in ("moderado", "alto", "muito_alto"):
        s.valor("M1.3.1", pct(linhas_faixa["total"][faixa], tot), "%", "M1.3.1_eslint.json", item=faixa)


def m132(s):
    linhas = ler_csv("M1.3.2_lista-verificacao.csv")
    for l in linhas:
        s.detalhe("M1.3.2", l["topico"], "presente", l["presente"], "")
    s.valor("M1.3.2", sum(l["presente"].strip().lower() == "sim" for l in linhas),
            "tópicos", "M1.3.2_lista-verificacao.csv")


def m133(s):
    linhas = ler_csv("M1.3.3_verificacoes.csv")
    for l in linhas:
        s.detalhe("M1.3.3", l["verificacao"], "presente", l["presente"], "")
    s.valor("M1.3.3", sum(l["presente"].strip().lower() == "sim" for l in linhas),
            "verificações", "M1.3.3_verificacoes.csv")


# ------------------------------------------------------------------- Q1.4

def prs_incluidos():
    prs = ler_json("M1.4.1_prs.json")
    excluidos = {int(l["numero"]) for l in ler_csv("M1.4.1_exclusoes.csv")}
    return [p for p in prs if p["number"] not in excluidos], len(excluidos)


def arquivos_pr(numero):
    paginas = ler_json(f"M1.4.1_pr-{numero}-arquivos.json")
    return [f for pagina in paginas for f in pagina]


def m141(s):
    prs, nexc = prs_incluidos()
    contagens = [sum(1 for f in arquivos_pr(p["number"]) if eh_producao(f["filename"]))
                 for p in prs]
    s.detalhe("M1.4.1", "", "pull requests incluídos", len(prs), "pull requests")
    s.detalhe("M1.4.1", "", "pull requests excluídos", nexc, "pull requests")
    s.detalhe("M1.4.1", "", "média de arquivos de produção", round(statistics.mean(contagens), 2), "arquivos")
    s.detalhe("M1.4.1", "", "máximo de arquivos de produção", max(contagens), "arquivos")
    s.valor("M1.4.1", statistics.median(contagens), "arquivos", "M1.4.1_prs.json")


def extensos():
    cloc = ler_json("M1.4.2_cloc.json")
    return {relativo(k): v["code"] for k, v in cloc.items()
            if k not in ("header", "SUM") and v["code"] > 1000}


def m142(s):
    prod = producao()
    ext = extensos()
    for p in PACOTES:
        n = sum(1 for f in ext if pacote(f) == p)
        s.detalhe("M1.4.2", p, "arquivos extensos", n, "arquivos")
    for f, code in sorted(ext.items(), key=lambda x: -x[1]):
        s.detalhe("M1.4.2", f, "linhas de código", code, "linhas")
    s.detalhe("M1.4.2", "total", "arquivos de produção", len(prod), "arquivos")
    s.valor("M1.4.2", pct(len(ext), len(prod)), "%", "M1.4.2_cloc.json")


def m143(s):
    prs, _ = prs_incluidos()
    todos = ler_json("M1.4.1_prs.json")
    renomes = {}
    for p in todos:
        for f in arquivos_pr(p["number"]):
            if f.get("status") == "renamed" and f.get("previous_filename"):
                renomes[f["previous_filename"]] = f["filename"]

    def atual(nome):
        vistos = set()
        while nome in renomes and nome not in vistos:
            vistos.add(nome)
            nome = renomes[nome]
        return nome

    ext = set(extensos())
    alteram = [p["number"] for p in prs
               if any(atual(f["filename"]) in ext for f in arquivos_pr(p["number"]))]
    s.detalhe("M1.4.3", "", "pull requests que alteram arquivo extenso", len(alteram), "pull requests")
    s.detalhe("M1.4.3", "", "pull requests incluídos", len(prs), "pull requests")
    s.valor("M1.4.3", pct(len(alteram), len(prs)), "%", "M1.4.1_prs.json")


# ------------------------------------------------------------------- Q1.5

def m151(s):
    cov = ler_json("M1.5.1_coverage-summary.json")
    prod = set(producao())
    soma = defaultdict(lambda: [0, 0])
    for k, v in cov.items():
        rel = relativo(k)
        if k == "total" or rel not in prod:
            continue
        for chave in (pacote(rel), "total"):
            soma[chave][0] += v["lines"]["covered"]
            soma[chave][1] += v["lines"]["total"]
    for p in PACOTES:
        if p in soma:
            s.detalhe("M1.5.1", p, "cobertura de linhas", pct(*soma[p]), "%")
    s.valor("M1.5.1", pct(*soma["total"]), "%", "M1.5.1_coverage-summary.json")


def m152(s):
    linhas = ler_csv("M1.5.2_classificacao.csv")
    niveis = defaultdict(int)
    for l in linhas:
        niveis[l["nivel"].strip()] += 1
    for n in ("unitário", "integração", "ponta a ponta"):
        s.detalhe("M1.5.2", n, "suítes", niveis[n], "suítes")
        s.detalhe("M1.5.2", n, "proporção", pct(niveis[n], len(linhas)), "%")
    s.valor("M1.5.2", sum(1 for n in ("unitário", "integração", "ponta a ponta") if niveis[n]),
            "níveis", "M1.5.2_classificacao.csv")


def m153(s):
    prs, _ = prs_incluidos()
    verificados = sem_evidencia = 0
    for p in prs:
        runs = ler_json(f"M1.5.3_pr-{p['number']}-execucoes.json")["workflow_runs"]
        todos_passos, passos = [], []
        for r in runs:
            caminho = bruto(f"M1.5.3_execucao-{r['id']}-jobs.json")
            if caminho.exists():
                for job in ler_json(caminho.name)["jobs"]:
                    todos_passos += job.get("steps") or []
        passos = [st for st in todos_passos if st["name"] == "Test Coverage"]
        # Sem execução ou sem nenhum passo disponível: sem evidência. Passos
        # disponíveis sem "Test Coverage" contam como não verificado.
        if not runs or not todos_passos:
            sem_evidencia += 1
            continue
        if any(st["conclusion"] in ("success", "failure") and st.get("completed_at")
               and st["completed_at"] < p["mergedAt"] for st in passos):
            verificados += 1
    com_evidencia = len(prs) - sem_evidencia
    s.detalhe("M1.5.3", "", "pull requests verificados", verificados, "pull requests")
    s.detalhe("M1.5.3", "", "pull requests com evidência", com_evidencia, "pull requests")
    s.detalhe("M1.5.3", "", "pull requests sem evidência", sem_evidencia, "pull requests")
    s.valor("M1.5.3", pct(verificados, com_evidencia), "%", "M1.4.1_prs.json")


# --------------------------------------------------------------- verificação

BRUTOS_ESPERADOS = {
    "M1.1.1": ["M1.1.1_arquivos-producao.txt", "M1.1.1_grafo-madge.json", "M1.1.1_madge-avisos.log"],
    "M1.1.2": ["M1.1.1_grafo-madge.json", "M1.1.2_eslintrc-base.json"],
    "M1.1.3": ["M1.1.1_grafo-madge.json"],
    "M1.2.1": ["M1.2.1_ocorrencias-grep.txt", "M1.2.1_arquivos-diretos.csv", "M1.1.1_grafo-madge.json"],
    "M1.2.2": ["M1.2.2_excalidraw-props.ts", "M1.2.2_propriedades.csv"],
    "M1.3.1": ["M1.3.1_eslint.json", "M1.3.1_eslint-erros.log"],
    "M1.3.2": ["M1.3.2_lista-verificacao.csv"],
    "M1.3.3": ["M1.3.3_fluxos-pull-request.txt", "M1.3.3_package.json", "M1.3.3_verificacoes.csv"],
    "M1.4.1": ["M1.4.1_prs.json", "M1.4.1_exclusoes.csv", "M1.4.1_pr-<N>-arquivos.json"],
    "M1.4.2": ["M1.4.2_cloc.json"],
    "M1.4.3": ["M1.4.1_prs.json", "M1.4.1_pr-<N>-arquivos.json", "M1.4.2_cloc.json"],
    "M1.5.1": ["M1.5.1_coverage-summary.json", "M1.5.1_testes.log"],
    "M1.5.2": ["M1.5.2_suites.txt", "M1.5.2_ocorrencias-grep.txt", "M1.5.2_ferramentas-e2e.txt", "M1.5.2_classificacao.csv"],
    "M1.5.3": ["M1.4.1_prs.json", "M1.5.3_pr-<N>-execucoes.json", "M1.5.3_execucao-<id>-jobs.json"],
}


def existe(nome):
    if "<" in nome:
        padrao = re.sub(r"<[^>]+>", "*", nome)
        return len(glob.glob(str(BRUTOS / padrao))) > 0
    return bruto(nome).exists()


def verificacao(metricas):
    prs = [p["number"] for p in ler_json("M1.4.1_prs.json")]
    linhas = []
    for cod, arquivos in BRUTOS_ESPERADOS.items():
        faltam = [a for a in arquivos if not existe(a)]
        if cod in ("M1.4.1", "M1.4.3"):
            faltam += [f"M1.4.1_pr-{n}-arquivos.json" for n in prs
                       if not bruto(f"M1.4.1_pr-{n}-arquivos.json").exists()]
        if cod == "M1.5.3":
            faltam += [f"M1.5.3_pr-{n}-execucoes.json" for n in prs
                       if not bruto(f"M1.5.3_pr-{n}-execucoes.json").exists()]
        fatores = bruto(f"{cod}_fatores.md").exists()
        valores = [m for m in metricas if m["metrica"] == cod and m["status"] == "coletada"]
        linhas.append({
            "metrica": cod,
            "dado_bruto_presente": "sim" if not faltam else "não",
            "arquivos_ausentes": " ".join(faltam),
            "fatores_registrados": "sim" if fatores else "não",
            "valor_recalculado": "sim" if valores else "não",
            "conferido_por": "",
        })
    return linhas


# ---------------------------------------------------------------------- main

def gravar(caminho, colunas, linhas, manter=None):
    existentes = []
    if manter and caminho.exists():
        with open(caminho, encoding="utf-8-sig", newline="") as f:
            existentes = [l for l in csv.DictReader(f) if not manter(l)]
    caminho.parent.mkdir(parents=True, exist_ok=True)
    with open(caminho, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=colunas, lineterminator="\n")
        w.writeheader()
        w.writerows(existentes + linhas)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--exc", default=os.environ.get("EXC", str(Path.home() / "excalidraw-avaliado")),
                    help="clone do Excalidraw no commit avaliado (usado em M1.3.1)")
    args = ap.parse_args()

    head = subprocess.run(["git", "-C", args.exc, "rev-parse", "HEAD"],
                          capture_output=True, text=True).stdout.strip()
    if head != COMMIT:
        sys.exit(f"O clone {args.exc} está em {head or '?'}, e não em {COMMIT}.")

    s = Saida()
    grafo = grafo_producao()
    m111(s, grafo)
    m112(s, grafo)
    m113(s, grafo)
    m121(s, grafo)
    m122(s)
    m131(s, args.exc)
    m132(s)
    m133(s)
    m141(s)
    m142(s)
    m143(s)
    m151(s)
    m152(s)
    m153(s)

    eh_g1 = lambda l: l["metrica"].startswith("M1.")
    gravar(CONSOLIDADOS / "metricas.csv", COLUNAS, s.metricas, manter=eh_g1)
    gravar(CONSOLIDADOS / "G1_detalhes.csv", ["metrica", "item", "medida", "valor", "unidade"], s.detalhes)
    gravar(CONSOLIDADOS / "G1_verificacao.csv",
           ["metrica", "dado_bruto_presente", "arquivos_ausentes", "fatores_registrados",
            "valor_recalculado", "conferido_por"], verificacao(s.metricas))

    for m in s.metricas:
        print(f"{m['metrica']:7} {m['item']:11} {m['valor']} {m['unidade']}")


if __name__ == "__main__":
    main()
