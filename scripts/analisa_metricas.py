#!/usr/bin/env python3
"""Análise das métricas de G1 (Manutenibilidade).

Lê as linhas de G1 de dados/fase-04/consolidados/metricas.csv e aplica as
regras de docs/fase-02/pontuacao-julgamento.md: faixas da tabela 4 e da
tabela 5 (M1.3.1), valor no limite no nível melhor, sem arredondamento,
média por questão e por característica, com média terminada em 0,5
arredondada para baixo, e julgamento da tabela 9.

Grava em dados/fase-04/consolidados/, mantendo as linhas de outros objetivos:
  niveis.csv           valor pontuado, faixa, nível e pontos de cada métrica
  questoes.csv         média e nível de cada questão
  caracteristicas.csv  média, nível e julgamento da característica

Gera os gráficos do plano de análise (seção 4) em docs/fase-04/img/.

Uso, a partir da raiz do repositório:
  python3 scripts/analisa_metricas.py
"""

import csv
import math
from fractions import Fraction
from pathlib import Path

from calcula_metricas import gravar

RAIZ = Path(__file__).resolve().parent.parent
CONSOLIDADOS = RAIZ / "dados" / "fase-04" / "consolidados"
IMG = RAIZ / "docs" / "fase-04" / "img"

SIMBOLOS = {5: "++", 4: "+", 3: "o", 2: "-", 1: "--"}

# Limites superiores de ++, +, o e - (o valor no limite fica no nível melhor).
INDESEJAVEL = (3, 5, 10, 20)
# Limites inferiores de ++, +, o e -.
DESEJAVEL = (95, 80, 60, 20)
# Tabela 5: máximos de moderado, alto e muito alto para ++, +, o e -.
PERFIL_RISCO = ((25, 0, 0), (30, 5, 0), (40, 10, 0), (50, 15, 5))

QUESTOES = {
    "Q1.1": "Modularidade",
    "Q1.2": "Reusabilidade",
    "Q1.3": "Analisabilidade",
    "Q1.4": "Modificabilidade",
    "Q1.5": "Testabilidade",
}


def ate(valor, limites, unidade):
    """Faixas em que menor é melhor: limites superiores de ++ a -."""
    for pontos, limite in zip((5, 4, 3, 2), limites):
        if valor <= limite:
            anterior = ([0] + list(limites))[5 - pontos]
            faixa = f"até {fmt(limite)}" if pontos == 5 else f"acima de {fmt(anterior)} até {fmt(limite)}"
            return pontos, f"{faixa} {unidade}".strip()
    return 1, f"acima de {fmt(limites[-1])} {unidade}".strip()


def a_partir(valor, limites):
    """Faixas de proporção desejável: limites inferiores de ++ a -."""
    for pontos, limite in zip((5, 4, 3, 2), limites):
        if valor >= limite:
            return pontos, f"{limite}% ou mais" if pontos == 5 else f"{limite} a {limites[4 - pontos]}%"
    return 1, f"abaixo de {limites[-1]}%"


def lista(valor, niveis):
    """Listas fixas: niveis mapeia cada valor possível aos pontos."""
    return niveis[int(valor)], f"{int(valor)} de {max(niveis)}"


def perfil(moderado, alto, muito_alto):
    for pontos, limites in zip((5, 4, 3, 2), PERFIL_RISCO):
        if moderado <= limites[0] and alto <= limites[1] and muito_alto <= limites[2]:
            return pontos, "máximos {}%, {}% e {}%".format(*limites)
    return 1, "acima de algum máximo do nível -"


def fmt(x):
    return f"{x:g}"


def pontuar(metrica, linhas):
    """Devolve (valor pontuado, unidade, faixa, pontos) de uma métrica."""
    v = {l["item"]: float(l["valor"]) for l in linhas}
    unidade = linhas[0]["unidade"]
    valor = v.get("")
    if metrica == "M1.1.1":
        pares = round(valor * 28 / 100)
        p, faixa = ate(pares, (0, 1, 2, 5), "pares")
        return str(pares), "pares", faixa, p
    if metrica == "M1.3.1":
        p, faixa = perfil(v["moderado"], v["alto"], v["muito_alto"])
        texto = "/".join(fmt(v[k]) for k in ("moderado", "alto", "muito_alto"))
        return texto, "% moderado/alto/muito alto", faixa, p
    if metrica == "M1.3.2":
        p, faixa = lista(valor, {4: 5, 3: 3, 2: 2, 1: 2, 0: 1})
    elif metrica in ("M1.3.3", "M1.5.2"):
        p, faixa = lista(valor, {3: 5, 2: 3, 1: 2, 0: 1})
    elif metrica == "M1.4.1":
        # Faixas lidas como contínuas: a mediana de um número par de
        # contribuições pode cair entre dois inteiros.
        p, faixa = ate(valor, (2, 4, 8, 16), "arquivos")
    elif metrica in ("M1.2.2", "M1.5.1", "M1.5.3"):
        p, faixa = a_partir(valor, DESEJAVEL)
    else:
        p, faixa = ate(valor, INDESEJAVEL, "%")
    return fmt(valor), unidade, faixa, p


def nivel_da_media(media):
    """Inteiro mais próximo, com 0,5 arredondado para baixo."""
    return math.ceil(media - Fraction(1, 2))


def um_decimal(media):
    return f"{float(media):.1f}"


def ler_metricas():
    with open(CONSOLIDADOS / "metricas.csv", encoding="utf-8-sig", newline="") as f:
        return [l for l in csv.DictReader(f) if l["metrica"].startswith("M1.")]


def analisar():
    por_metrica = {}
    for l in ler_metricas():
        por_metrica.setdefault(l["metrica"], []).append(l)

    niveis = []
    pontos_questao = {q: [] for q in QUESTOES}
    nao_coletadas = 0
    for metrica in sorted(por_metrica, key=lambda m: [int(x) for x in m[1:].split(".")]):
        linhas = por_metrica[metrica]
        questao = "Q" + ".".join(metrica[1:].split(".")[:2])
        if any(l["status"] != "coletada" for l in linhas):
            nao_coletadas += 1
            niveis.append({"metrica": metrica, "questao": questao, "valor_pontuado": "",
                           "unidade": linhas[0]["unidade"], "faixa": "", "nivel": "nao_coletada", "pontos": ""})
            continue
        valor, unidade, faixa, p = pontuar(metrica, linhas)
        pontos_questao[questao].append(p)
        niveis.append({"metrica": metrica, "questao": questao, "valor_pontuado": valor,
                       "unidade": unidade, "faixa": faixa, "nivel": SIMBOLOS[p], "pontos": p})

    questoes, medias = [], []
    for q, nome in QUESTOES.items():
        pts = pontos_questao[q]
        if not pts:
            questoes.append({"questao": q, "subcaracteristica": nome, "media": "", "nivel": "nao_avaliada",
                             "pontos": "", "metricas_coletadas": 0})
            continue
        media = Fraction(sum(pts), len(pts))
        medias.append(media)
        n = nivel_da_media(media)
        questoes.append({"questao": q, "subcaracteristica": nome, "media": um_decimal(media),
                         "nivel": SIMBOLOS[n], "pontos": n, "metricas_coletadas": len(pts)})

    total = len(por_metrica)
    if nao_coletadas * 2 > total or not medias:
        caracteristica = {"caracteristica": "G1", "nome": "Manutenibilidade", "media": "", "nivel": "",
                          "pontos": "", "julgamento": "inconclusiva", "motivo": "mais da metade das métricas não coletada"}
    else:
        media = sum(medias) / len(medias)
        n = nivel_da_media(media)
        em_muito_ruim = [q["questao"] for q in questoes if q["pontos"] == 1]
        if n >= 3 and not em_muito_ruim:
            julgamento, motivo = "atende", f"nível {SIMBOLOS[n]} e nenhuma questão em --"
        elif em_muito_ruim:
            julgamento, motivo = "não atende", "questão em --: " + ", ".join(em_muito_ruim)
        else:
            julgamento, motivo = "não atende", f"nível {SIMBOLOS[n]}"
        caracteristica = {"caracteristica": "G1", "nome": "Manutenibilidade", "media": um_decimal(media),
                          "nivel": SIMBOLOS[n], "pontos": n, "julgamento": julgamento, "motivo": motivo}

    return niveis, questoes, caracteristica, por_metrica


def graficos(questoes, por_metrica):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    plt.rcParams.update({"font.size": 11, "svg.hashsalt": "g1", "pdf.compression": 0})
    IMG.mkdir(parents=True, exist_ok=True)
    metadados = {"Software": None}

    # Barras horizontais por questão, eixo de 1 a 5, linha no nível o.
    avaliadas = [q for q in questoes if q["media"]]
    rotulos = [f"{q['questao']} {q['subcaracteristica']}" for q in avaliadas][::-1]
    medias = [float(q["media"]) for q in avaliadas][::-1]
    fig, ax = plt.subplots(figsize=(8, 3.6))
    barras = ax.barh(rotulos, [m - 1 for m in medias], left=1, color="#4C72B0", height=0.6)
    for barra, q in zip(barras, avaliadas[::-1]):
        ax.text(barra.get_x() + barra.get_width() + 0.05, barra.get_y() + barra.get_height() / 2,
                f"{q['media'].replace('.', ',')} ({q['nivel']})", va="center")
    ax.axvline(3, color="#C44E52", linestyle="--", linewidth=1.5)
    ax.text(3.03, len(rotulos) - 0.45, "mínimo para atender (o)", color="#C44E52", fontsize=9)
    ax.set_xlim(1, 5.6)
    ax.set_xticks([1, 2, 3, 4, 5], ["1 (--)", "2 (-)", "3 (o)", "4 (+)", "5 (++)"])
    ax.set_xlabel("Média dos pontos das métricas da questão")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(IMG / "G1_questoes.png", dpi=150, metadata=metadados)
    plt.close(fig)

    # Barra empilhada do perfil de risco de M1.3.1.
    v = {l["item"]: float(l["valor"]) for l in por_metrica["M1.3.1"]}
    partes = [("baixo (1 a 10)", 100 - v["moderado"] - v["alto"] - v["muito_alto"], "#DDDDDD", ""),
              ("moderado (11 a 20)", v["moderado"], "#8DA0CB", "//"),
              ("alto (21 a 50)", v["alto"], "#FC8D62", ".."),
              ("muito alto (acima de 50)", v["muito_alto"], "#C44E52", "xx")]
    fig, ax = plt.subplots(figsize=(8, 1.8))
    inicio = 0
    for nome, valor, cor, hachura in partes:
        ax.barh([0], [valor], left=inicio, color=cor, hatch=hachura, edgecolor="#333333",
                label=f"{nome}: {valor:.2f}%".replace(".", ","))
        ax.text(inicio + valor / 2, 0, f"{valor:.1f}%".replace(".", ","), ha="center", va="center",
                fontsize=9, bbox={"facecolor": "white", "edgecolor": "none", "pad": 1})
        inicio += valor
    ax.set_xlim(0, 100)
    ax.set_yticks([])
    ax.set_xlabel("Linhas de código em funções, por faixa de risco de complexidade (%)")
    p, _ = perfil(v["moderado"], v["alto"], v["muito_alto"])
    if p > 1:
        titulo = f"Nível {SIMBOLOS[p]}: os três máximos do nível são respeitados"
    else:
        nomes = ("moderado", "alto", "muito_alto")
        acima = [f"{n.replace('_', ' ')} {fmt(v[n])}% > {fmt(m)}%"
                 for n, m in zip(nomes, PERFIL_RISCO[-1]) if v[n] > m]
        titulo = "Nível --: acima do máximo do nível - em " + ", ".join(acima)
    ax.set_title(titulo.replace(".", ","), fontsize=10, loc="left")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.45), ncol=2, frameon=False, fontsize=9)
    ax.spines[["top", "right", "left"]].set_visible(False)
    fig.savefig(IMG / "G1_M1.3.1_perfil-risco.png", dpi=150, metadata=metadados, bbox_inches="tight")
    plt.close(fig)


def main():
    niveis, questoes, caracteristica, por_metrica = analisar()
    gravar(CONSOLIDADOS / "niveis.csv",
           ["metrica", "questao", "valor_pontuado", "unidade", "faixa", "nivel", "pontos"],
           niveis, manter=lambda l: l["metrica"].startswith("M1."))
    gravar(CONSOLIDADOS / "questoes.csv",
           ["questao", "subcaracteristica", "media", "nivel", "pontos", "metricas_coletadas"],
           questoes, manter=lambda l: l["questao"].startswith("Q1."))
    gravar(CONSOLIDADOS / "caracteristicas.csv",
           ["caracteristica", "nome", "media", "nivel", "pontos", "julgamento", "motivo"],
           [caracteristica], manter=lambda l: l["caracteristica"] == "G1")
    graficos(questoes, por_metrica)
    for l in niveis:
        print(f"{l['metrica']:7} {l['valor_pontuado']:>18} {l['nivel']:>3}  {l['faixa']}")
    for q in questoes:
        print(f"{q['questao']:7} média {q['media']:>4} {q['nivel']:>3}")
    c = caracteristica
    print(f"G1      média {c['media']:>4} {c['nivel']:>3}  {c['julgamento']} ({c['motivo']})")


if __name__ == "__main__":
    main()
