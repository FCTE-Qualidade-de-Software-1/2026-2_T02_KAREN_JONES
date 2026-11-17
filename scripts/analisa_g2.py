"""Consolida as metricas de Confiabilidade (G2) a partir dos dados brutos
em dados/fase-04/brutos/Q2.* e gera os CSVs em dados/fase-04/consolidados/
e os graficos em static/img/fase-04/.

Uso na raiz do repositorio:
    python scripts/analisa_g2.py
"""

from __future__ import annotations

import csv
import math
import statistics
from pathlib import Path

import matplotlib.pyplot as plt

BRUTOS = Path("dados/fase-04/brutos")
CONSOLIDADOS = Path("dados/fase-04/consolidados")
IMG_DIR = Path("static/img/fase-04")

NIVEL_LABEL = {5: "Excelente (++)", 4: "Bom (+)", 3: "Regular (o)", 2: "Ruim (-)", 1: "Muito ruim (--)"}
NIVEL_SIMBOLO = {5: "++", 4: "+", 3: "o", 2: "-", 1: "--"}
ESCALA_PCT = {5: 100.0, 4: 75.0, 3: 50.0, 2: 25.0, 1: 0.0}


def ler_csv(caminho: Path) -> list[dict[str, str]]:
    with caminho.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def arredondar_meio_para_baixo(valor: float) -> int:
    frac = valor - math.floor(valor)
    if abs(frac - 0.5) < 1e-9:
        return math.floor(valor)
    return round(valor)


def pontuar_proporcao_desejavel(pct: float) -> int:
    if pct >= 95.0:
        return 5
    if pct >= 80.0:
        return 4
    if pct >= 60.0:
        return 3
    if pct >= 20.0:
        return 2
    return 1


def pontuar_m211(pct: float) -> int:
    if pct <= 20.0:
        return 5
    if pct <= 40.0:
        return 4
    if pct <= 60.0:
        return 3
    if pct <= 80.0:
        return 2
    return 1


def pontuar_m212(mediana_dias: float) -> int:
    if mediana_dias <= 7.0:
        return 5
    if mediana_dias <= 14.0:
        return 4
    if mediana_dias <= 30.0:
        return 3
    if mediana_dias <= 90.0:
        return 2
    return 1


def pontuar_lista_de_10(aprovados: int) -> int:
    """Faixas de M2.2.1 e M2.4.3 na Tabela 6: 10, 8 ou 9, 6 ou 7, 2 a 5, 0 ou 1."""
    if aprovados == 10:
        return 5
    if aprovados >= 8:
        return 4
    if aprovados >= 6:
        return 3
    if aprovados >= 2:
        return 2
    return 1


def pontuar_m222(total_externos: int, indispensaveis: int) -> int:
    if indispensaveis >= 2:
        return 1
    if indispensaveis == 1:
        return 2
    if total_externos == 0:
        return 5
    if total_externos <= 3:
        return 4
    return 3


def calcular_metricas() -> list[dict[str, object]]:
    # M2.1.1
    prs = [r for r in ler_csv(BRUTOS / "Q2.1-ausencia-de-falhas/M2.1.1_prs.csv") if r.get("elegivel") == "sim"]
    fixes = [r for r in prs if r.get("eh_fix") == "sim"]
    m211_val = round(len(fixes) / len(prs) * 100.0, 2)
    m211_pts = pontuar_m211(m211_val)

    # M2.1.2
    pares = [r for r in ler_csv(BRUTOS / "Q2.1-ausencia-de-falhas/M2.1.2_pares.csv") if r.get("dias")]
    m212_val = round(statistics.median(float(r["dias"]) for r in pares), 6)
    m212_pts = pontuar_m212(m212_val)

    # M2.1.3
    revs = ler_csv(BRUTOS / "Q2.1-ausencia-de-falhas/M2.1.3_revisoes.csv")
    revs_ok = [r for r in revs if r.get("aprovacao_valida") == "sim"]
    m213_val = round(len(revs_ok) / len(revs) * 100.0, 2)
    m213_pts = pontuar_proporcao_desejavel(m213_val)

    # M2.2.1
    funcoes = ler_csv(BRUTOS / "Q2.2-disponibilidade/M2.2.1_funcoes.csv")
    funcoes_ok = [r for r in funcoes if r.get("resultado") == "aprovado"]
    m221_val = round(len(funcoes_ok) / len(funcoes) * 100.0, 1)
    m221_pts = pontuar_lista_de_10(len(funcoes_ok))

    # M2.2.2
    dominios = ler_csv(BRUTOS / "Q2.2-disponibilidade/M2.2.2_dominios.csv")
    indispensaveis = sum(1 for r in dominios if r.get("indispensavel") == "sim")
    m222_pts = pontuar_m222(len(dominios), indispensaveis)

    # M2.3.1
    casos = ler_csv(BRUTOS / "Q2.3-tolerancia-a-falhas/M2.3.1_casos.csv")
    casos_ok = [r for r in casos if r.get("tratado_consolidado") == "sim"]
    m231_val = round(len(casos_ok) / len(casos) * 100.0, 2)
    m231_pts = {9: 5, 8: 4, 7: 3, 6: 3}.get(len(casos_ok), 2 if len(casos_ok) >= 2 else 1)

    # M2.3.2
    verifs = ler_csv(BRUTOS / "Q2.3-tolerancia-a-falhas/M2.3.2_verificacoes.csv")
    por_verif: dict[str, list[str]] = {}
    for r in verifs:
        por_verif.setdefault(r["verificacao"], []).append(r["resultado"])
    v_ok = sum(1 for resps in por_verif.values() if all(x == "aprovado" for x in resps))
    m232_val = round(v_ok / 5 * 100.0, 1)
    m232_pts = {5: 5, 4: 4, 3: 3, 2: 2, 1: 2, 0: 1}[v_ok]
    h232_ok = all(all(x == "aprovado" for x in por_verif[v]) for v in ("V1", "V2", "V3", "V4"))

    # M2.4.1
    cenarios = ler_csv(BRUTOS / "Q2.4-recuperabilidade/M2.4.1_cenarios.csv")
    cen_ok = [r for r in cenarios if r.get("resultado") == "aprovado"]
    m241_val = round(len(cen_ok) / len(cenarios) * 100.0, 1)
    m241_pts = {4: 5, 3: 3, 2: 2, 1: 2, 0: 1}[len(cen_ok)]

    # M2.4.2
    arquivos = ler_csv(BRUTOS / "Q2.4-recuperabilidade/M2.4.2_arquivos.csv")
    arq_ok = [r for r in arquivos if r.get("resultado") == "aprovado"]
    m242_val = round(len(arq_ok) / len(arquivos) * 100.0, 1)
    m242_pts = {7: 5, 6: 4, 5: 3}.get(len(arq_ok), 2 if len(arq_ok) >= 2 else 1)

    # M2.4.3
    acoes = ler_csv(BRUTOS / "Q2.4-recuperabilidade/M2.4.3_acoes.csv")
    acoes_ok = [r for r in acoes if r.get("resultado") == "aprovado"]
    m243_val = round(len(acoes_ok) / len(acoes) * 100.0, 1)
    m243_pts = pontuar_lista_de_10(len(acoes_ok))

    return [
        {
            "metrica_id": "M2.1.1",
            "nome_metrica": "Proporção de correções entre as contribuições integradas",
            "questao_id": "Q2.1",
            "valor_medido": m211_val,
            "unidade": "%",
            "escala_1_a_5": m211_pts,
            "hipotese_definida": "H2.1.1 >= 20%",
            "status_hipotese": "Confirmada" if m211_val >= 20.0 else "Refutada",
            "arquivo_bruto": "dados/fase-04/brutos/Q2.1-ausencia-de-falhas/M2.1.1_coleta.csv",
            "label_grafico": f"M2.1.1 ({m211_val:.2f}%)".replace(".", ","),
        },
        {
            "metrica_id": "M2.1.2",
            "nome_metrica": "Mediana do tempo entre o relato e a correção",
            "questao_id": "Q2.1",
            "valor_medido": m212_val,
            "unidade": "dias",
            "escala_1_a_5": m212_pts,
            "hipotese_definida": "H2.1.2 <= 30 dias",
            "status_hipotese": "Confirmada" if m212_val <= 30.0 else "Refutada",
            "arquivo_bruto": "dados/fase-04/brutos/Q2.1-ausencia-de-falhas/M2.1.2_coleta.csv",
            "label_grafico": f"M2.1.2 ({m212_val:.2f} d)".replace(".", ","),
        },
        {
            "metrica_id": "M2.1.3",
            "nome_metrica": "Proporção de contribuições revisadas antes da integração",
            "questao_id": "Q2.1",
            "valor_medido": m213_val,
            "unidade": "%",
            "escala_1_a_5": m213_pts,
            "hipotese_definida": "H2.1.3 >= 95%",
            "status_hipotese": "Confirmada" if m213_val >= 95.0 else "Refutada",
            "arquivo_bruto": "dados/fase-04/brutos/Q2.1-ausencia-de-falhas/M2.1.3_coleta.csv",
            "label_grafico": f"M2.1.3 ({m213_val:.2f}%)".replace(".", ","),
        },
        {
            "metrica_id": "M2.2.1",
            "nome_metrica": "Proporção de funções essenciais disponíveis sem conexão",
            "questao_id": "Q2.2",
            "valor_medido": m221_val,
            "unidade": "%",
            "escala_1_a_5": m221_pts,
            "hipotese_definida": "H2.2.1 = 10 de 10",
            "status_hipotese": "Confirmada" if len(funcoes_ok) == 10 else "Refutada",
            "arquivo_bruto": "dados/fase-04/brutos/Q2.2-disponibilidade/M2.2.1_coleta.csv",
            "label_grafico": f"M2.2.1 ({len(funcoes_ok)}/10)",
        },
        {
            "metrica_id": "M2.2.2",
            "nome_metrica": "Origens externas necessárias para o editor local",
            "questao_id": "Q2.2",
            "valor_medido": f"{len(dominios)} externos / {indispensaveis} indispensáveis",
            "unidade": "domínios",
            "escala_1_a_5": m222_pts,
            "hipotese_definida": "H2.2.2 = 0 indispensáveis",
            "status_hipotese": "Confirmada" if indispensaveis == 0 else "Refutada",
            "arquivo_bruto": "dados/fase-04/brutos/Q2.2-disponibilidade/M2.2.2_coleta.csv",
            "label_grafico": f"M2.2.2 ({len(dominios)} ext / {indispensaveis} ind)",
        },
        {
            "metrica_id": "M2.3.1",
            "nome_metrica": "Proporção de arquivos inválidos tratados com mensagem",
            "questao_id": "Q2.3",
            "valor_medido": m231_val,
            "unidade": "%",
            "escala_1_a_5": m231_pts,
            "hipotese_definida": "H2.3.1 = 9 de 9",
            "status_hipotese": "Confirmada" if len(casos_ok) == 9 else "Refutada",
            "arquivo_bruto": "dados/fase-04/brutos/Q2.3-tolerancia-a-falhas/M2.3.1_coleta.csv",
            "label_grafico": f"M2.3.1 ({len(casos_ok)}/9)",
        },
        {
            "metrica_id": "M2.3.2",
            "nome_metrica": "Continuidade do editor após falha da colaboração",
            "questao_id": "Q2.3",
            "valor_medido": m232_val,
            "unidade": "%",
            "escala_1_a_5": m232_pts,
            "hipotese_definida": "H2.3.2 V1 a V4 aprovadas",
            "status_hipotese": "Confirmada" if h232_ok else "Refutada",
            "arquivo_bruto": "dados/fase-04/brutos/Q2.3-tolerancia-a-falhas/M2.3.2_coleta.csv",
            "label_grafico": f"M2.3.2 ({v_ok}/5)",
        },
        {
            "metrica_id": "M2.4.1",
            "nome_metrica": "Proporção de cenários de fechamento com restauração do desenho",
            "questao_id": "Q2.4",
            "valor_medido": m241_val,
            "unidade": "%",
            "escala_1_a_5": m241_pts,
            "hipotese_definida": "H2.4.1 = 4 de 4",
            "status_hipotese": "Confirmada" if len(cen_ok) == 4 else "Refutada",
            "arquivo_bruto": "dados/fase-04/brutos/Q2.4-recuperabilidade/M2.4.1_coleta.csv",
            "label_grafico": f"M2.4.1 ({len(cen_ok)}/4)",
        },
        {
            "metrica_id": "M2.4.2",
            "nome_metrica": "Proporção de arquivos reabertos sem perda",
            "questao_id": "Q2.4",
            "valor_medido": m242_val,
            "unidade": "%",
            "escala_1_a_5": m242_pts,
            "hipotese_definida": "H2.4.2 = 7 de 7",
            "status_hipotese": "Confirmada" if len(arq_ok) == 7 else "Refutada",
            "arquivo_bruto": "dados/fase-04/brutos/Q2.4-recuperabilidade/M2.4.2_coleta.csv",
            "label_grafico": f"M2.4.2 ({len(arq_ok)}/7)",
        },
        {
            "metrica_id": "M2.4.3",
            "nome_metrica": "Cobertura de desfazer e refazer",
            "questao_id": "Q2.4",
            "valor_medido": m243_val,
            "unidade": "%",
            "escala_1_a_5": m243_pts,
            "hipotese_definida": "H2.4.3 = 10 de 10",
            "status_hipotese": "Confirmada" if len(acoes_ok) == 10 else "Refutada",
            "arquivo_bruto": "dados/fase-04/brutos/Q2.4-recuperabilidade/M2.4.3_coleta.csv",
            "label_grafico": f"M2.4.3 ({len(acoes_ok)}/10)",
        },
    ]


def gerar_consolidados_e_graficos() -> None:
    CONSOLIDADOS.mkdir(parents=True, exist_ok=True)
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    metricas = calcular_metricas()

    with (CONSOLIDADOS / "G2_metricas_consolidadas.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "metrica_id", "nome_metrica", "questao_id", "valor_medido", "unidade",
            "nivel_qualitativo", "pontos", "escala_1_a_5", "hipotese_definida",
            "status_hipotese", "arquivo_bruto",
        ])
        for m in metricas:
            pts = int(m["escala_1_a_5"])
            writer.writerow([
                m["metrica_id"], m["nome_metrica"], m["questao_id"], m["valor_medido"],
                m["unidade"], NIVEL_LABEL[pts], ESCALA_PCT[pts], pts,
                m["hipotese_definida"], m["status_hipotese"], m["arquivo_bruto"],
            ])

    questoes_meta = [
        ("Q2.1", "Ausência de falhas", "O projeto evita que falhas cheguem ao usuário e trata de forma organizada os defeitos que chegam?"),
        ("Q2.2", "Disponibilidade", "O editor continua disponível para o usuário sem conexão e sem depender de serviços externos?"),
        ("Q2.3", "Tolerância a falhas", "O editor continua funcionando quando recebe dados inválidos ou quando a conexão com a colaboração falha?"),
        ("Q2.4", "Recuperabilidade", "O usuário recupera seu trabalho depois de fechar a aplicação, de reabrir arquivos antigos ou de cometer um erro de edição?"),
    ]

    q_medias: list[float] = []
    q_niveis: list[int] = []
    with (CONSOLIDADOS / "G2_questoes_pontuacao.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "questao_id", "caracteristica_qualidade", "pergunta_gqm", "metricas_associadas",
            "pontos_percentuais_metricas", "escala_1_a_5_metricas", "media_percentual",
            "media_escala_1_a_5", "nivel_qualitativo_questao", "julgamento",
        ])
        q_pcts: list[float] = []
        for qid, nome, pergunta in questoes_meta:
            ms = [m for m in metricas if m["questao_id"] == qid]
            escala = [int(m["escala_1_a_5"]) for m in ms]
            pcts = [ESCALA_PCT[x] for x in escala]
            media_e = sum(escala) / len(escala)
            media_p = sum(pcts) / len(pcts)
            nivel = arredondar_meio_para_baixo(media_e)
            q_medias.append(media_e)
            q_pcts.append(media_p)
            q_niveis.append(nivel)
            writer.writerow([
                qid, nome, pergunta,
                ", ".join(str(m["metrica_id"]) for m in ms),
                ", ".join(f"{p:.1f}" for p in pcts),
                ", ".join(str(e) for e in escala),
                f"{media_p:.2f}", f"{media_e:.2f}",
                NIVEL_LABEL[nivel], "Atende" if nivel >= 3 else "Não atende",
            ])

        g2_media = sum(q_medias) / len(q_medias)
        g2_pct = sum(q_pcts) / len(q_pcts)
        g2_nivel = arredondar_meio_para_baixo(g2_media)
        julgamento = "Atende" if (g2_nivel >= 3 and all(n > 1 for n in q_niveis)) else "Não atende"
        writer.writerow([
            "OBJETIVO_G2", "Confiabilidade",
            "Avaliar a confiabilidade do editor, da aplicação web e dos mecanismos de colaboração e salvamento do Excalidraw",
            "Q2.1, Q2.2, Q2.3, Q2.4",
            ", ".join(f"{p:.2f}" for p in q_pcts),
            ", ".join(f"{m:.2f}" for m in q_medias),
            f"{g2_pct:.2f}", f"{g2_media:.2f}", NIVEL_LABEL[g2_nivel], julgamento,
        ])

    # Grafico 1: 10 metricas
    cores = {5: "#1b7f3a", 4: "#4caf50", 3: "#f59e0b", 2: "#ef4444", 1: "#991b1b"}
    fig, ax = plt.subplots(figsize=(9, 4.8), dpi=150)
    labels = [str(m["label_grafico"]) for m in reversed(metricas)]
    vals = [int(m["escala_1_a_5"]) for m in reversed(metricas)]
    bars = ax.barh(labels, vals, color=[cores[v] for v in vals], height=0.62, edgecolor="#1f2937", linewidth=0.5)
    ax.set_xlim(0, 5.7)
    ax.set_xticks([1, 2, 3, 4, 5])
    ax.set_xticklabels(["1 (--)", "2 (-)", "3 (o)", "4 (+)", "5 (++)"])
    ax.axvline(3, color="#6b7280", linestyle="--", linewidth=1, label="Limiar Regular (3,0)")
    for bar, v in zip(bars, vals):
        ax.text(v + 0.1, bar.get_y() + bar.get_height() / 2, f"{v} ({NIVEL_SIMBOLO[v]})", va="center", fontsize=9, fontweight="bold")
    ax.set_title("Pontuação das Métricas de Confiabilidade (G2)", fontsize=12, fontweight="bold", pad=10)
    ax.set_xlabel("Escala Heitlager, Kuipers e Visser (1 a 5)")
    ax.grid(axis="x", linestyle=":", alpha=0.5)
    ax.legend(loc="lower right", frameon=True)
    plt.tight_layout()
    plt.savefig(IMG_DIR / "g2-pontuacao-metricas.png")
    plt.close()

    # Grafico 2: Agregacao por questao e G2
    q_labels = [
        "Q2.1\nAusência de falhas",
        "Q2.2\nDisponibilidade",
        "Q2.3\nTolerância a falhas",
        "Q2.4\nRecuperabilidade",
        "G2\nConfiabilidade (Geral)",
    ]
    q_vals = [*q_medias, g2_media]
    q_lvls = [
        f"{m:.1f} ({NIVEL_SIMBOLO[n]})".replace(".", ",")
        for m, n in zip(q_vals, [*q_niveis, g2_nivel])
    ]
    q_colors = [*[cores[n] for n in q_niveis], "#2563eb"]
    fig, ax = plt.subplots(figsize=(8.2, 4.2), dpi=150)
    bars = ax.bar(q_labels, q_vals, color=q_colors, width=0.52, edgecolor="#1f2937", linewidth=0.6)
    ax.set_ylim(0, 5.6)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["1 (--)", "2 (-)", "3 (o)", "4 (+)", "5 (++)"])
    ax.axhline(3.0, color="#6b7280", linestyle="--", linewidth=1, label="Limiar 'Atende' (3,0)")
    for bar, v, lbl in zip(bars, q_vals, q_lvls):
        ax.text(bar.get_x() + bar.get_width() / 2, v + 0.12, lbl, ha="center", va="bottom", fontsize=9.5, fontweight="bold")
    ax.set_title("Agregação por Subcaracterística e Objetivo G2 (Confiabilidade)", fontsize=12, fontweight="bold", pad=10)
    ax.set_ylabel("Média na escala (1 a 5)")
    ax.grid(axis="y", linestyle=":", alpha=0.5)
    ax.legend(loc="upper right", frameon=True)
    plt.tight_layout()
    plt.savefig(IMG_DIR / "g2-agregacao-questoes.png")
    plt.close()
    print(f"G2 consolidada: media={g2_media:.3f}, nivel={NIVEL_LABEL[g2_nivel]}, julgamento={julgamento}")


if __name__ == "__main__":
    gerar_consolidados_e_graficos()
