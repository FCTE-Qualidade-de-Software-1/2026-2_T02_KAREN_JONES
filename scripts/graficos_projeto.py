"""
Graficos PSM/CID do projeto inteiro (Fases 1 a 4), numerados de 09 a 17.

Chamado por coleta_psm.py. Cada grafico tem uma funcao de calculo, que devolve
as linhas do CSV, e uma funcao de desenho em matplotlib, que le essas linhas.
"""

import csv
from datetime import datetime, timedelta, timezone
from pathlib import Path

FUSO_BRT = timezone(timedelta(hours=-3))
LABELS_IGNORADAS = ("retroativa",)
PREFIXO_SUBGRUPO = "subgrupo-"

# Estilo comum. Uma cor fixa por fase em todos os graficos.
CORES_FASE = {"Fase 1": "#2a78d6", "Fase 2": "#eb6834", "Fase 3": "#1baf7a", "Fase 4": "#eda100"}
COR_SERIE = "#6250d6"
COR_SERIE_2 = "#e87ba4"
COR_NO_PRAZO = "#0ca30c"
COR_EM_ATRASO = "#d03b3b"
COR_NEUTRA = "#c3c2b7"
COR_FUNDO = "#ffffff"
COR_TEXTO = "#111827"
COR_TEXTO_2 = "#4b5563"
COR_GRADE = "#e5e7eb"
NOTA_LABELS = "Issue com mais de um tipo de trabalho conta em cada um."


# ---------------------------------------------------------------- calculo

def labels_de_tipo(labels: list[str]) -> list[str]:
    """Labels que indicam tipo de trabalho. Subgrupos e marcadores ficam de fora."""
    return [l for l in labels if not l.startswith(PREFIXO_SUBGRUPO) and l not in LABELS_IGNORADAS]


def mediana(valores: list[float]) -> float | None:
    if not valores:
        return None
    ordenados = sorted(valores)
    meio = len(ordenados) // 2
    if len(ordenados) % 2:
        return round(ordenados[meio], 2)
    return round((ordenados[meio - 1] + ordenados[meio]) / 2, 2)


def _pct(parte: float, total: float) -> float:
    return round(parte / total * 100.0, 1) if total > 0 else 0.0


def _fases(itens: list[dict]) -> list[str]:
    return sorted({i["fase"] for i in itens})


def _agrupar_por_label(itens: list[dict], chave_labels: str = "labels") -> dict[str, list[dict]]:
    """Agrupa por tipo de trabalho, na ordem em que cada label aparece."""
    grupos: dict[str, list[dict]] = {}
    for item in itens:
        for label in labels_de_tipo(item[chave_labels]):
            grupos.setdefault(label, []).append(item)
    return grupos


def calcular_burnup(issues: list[dict], agora: datetime) -> list[dict]:
    """Issues criadas e fechadas, acumuladas por dia no horario de Brasilia."""
    if not issues:
        return []
    criadas = [i["dt_criacao"].astimezone(FUSO_BRT).date() for i in issues]
    fechadas = [i["dt_fechamento"].astimezone(FUSO_BRT).date() for i in issues if i["dt_fechamento"]]
    dia, fim = min(criadas), agora.astimezone(FUSO_BRT).date()
    linhas = []
    while dia <= fim:
        linhas.append({
            "data": dia.isoformat(),
            "criadas_acumuladas": sum(1 for d in criadas if d <= dia),
            "fechadas_acumuladas": sum(1 for d in fechadas if d <= dia),
        })
        dia += timedelta(days=1)
    return linhas


def calcular_aderencia(resumo_fases: list[dict]) -> list[dict]:
    """Aderencia ao prazo por fase, com os numeros que o resumo das fases ja traz."""
    colunas = ("fase", "total_issues", "issues_no_prazo", "issues_em_atraso", "aderencia_prazo_pct")
    return [{c: fase[c] for c in colunas} for fase in resumo_fases]


def calcular_bloqueio(issues: list[dict], agora: datetime) -> list[dict]:
    """
    Issues com dependencia, por fase, divididas em travadas e nao travadas.
    Travada: alguma dependencia fechou depois do prazo da issue, ou continua
    aberta depois desse prazo.
    """
    por_numero = {i["numero"]: i for i in issues}
    linhas = []
    for fase in _fases(issues):
        com_dependencia, travadas = 0, []
        for issue in issues:
            if issue["fase"] != fase:
                continue
            deps = [por_numero[d] for d in issue["dependencias"] if d in por_numero and d != issue["numero"]]
            if not deps:
                continue
            com_dependencia += 1
            prazo = issue["dt_prazo"]
            if prazo and any((d["dt_fechamento"] or agora) > prazo for d in deps):
                travadas.append(issue["numero"])
        if com_dependencia:
            linhas.append({
                "fase": fase,
                "issues_com_dependencia": com_dependencia,
                "travadas": len(travadas),
                "nao_travadas": com_dependencia - len(travadas),
                "travadas_pct": _pct(len(travadas), com_dependencia),
                "travadas_lista": " ".join(f"#{n}" for n in travadas),
            })
    return linhas


def calcular_acuracia_labels(issues: list[dict]) -> list[dict]:
    """Horas reais sobre horas estimadas por tipo de trabalho, nas issues com os dois valores."""
    avaliadas = [i for i in issues if i["estimativa_h"] > 0 and i["horas_reais_h"] > 0]
    linhas = []
    for label, lista in _agrupar_por_label(avaliadas).items():
        estimadas = sum(i["estimativa_h"] for i in lista)
        reais = sum(i["horas_reais_h"] for i in lista)
        linhas.append({
            "label": label,
            "issues_avaliadas": len(lista),
            "horas_estimadas": round(estimadas, 2),
            "horas_reais": round(reais, 2),
            "acuracia_pct": _pct(reais, estimadas),
        })
    return sorted(linhas, key=lambda l: -l["issues_avaliadas"])


def calcular_horas(issues: list[dict], mapa_equipe: dict[str, str]) -> list[dict]:
    """Horas reais por integrante e por tipo de trabalho."""
    por_pessoa: dict[str, float] = {}
    for issue in issues:
        for login, horas in issue["horas_por_pessoa"].items():
            por_pessoa[login] = por_pessoa.get(login, 0.0) + horas
    por_label = {
        label: sum(i["horas_reais_h"] for i in lista)
        for label, lista in _agrupar_por_label(issues).items()
    }
    linhas = [
        {"recorte": "integrante", "grupo": mapa_equipe.get(login, login), "horas_reais": round(h, 2)}
        for login, h in sorted(por_pessoa.items(), key=lambda x: -x[1]) if h > 0
    ]
    linhas += [
        {"recorte": "label", "grupo": label, "horas_reais": round(h, 2)}
        for label, h in sorted(por_label.items(), key=lambda x: -x[1]) if h > 0
    ]
    return linhas


def calcular_lead_time(issues: list[dict]) -> list[dict]:
    """Mediana do lead time (criacao ate fechamento, em dias) por fase e por tipo de trabalho."""
    fechadas = [i for i in issues if i["lead_time_dias"] is not None]

    def linha(recorte: str, grupo: str, lista: list[dict]) -> dict:
        return {
            "recorte": recorte,
            "grupo": grupo,
            "issues_fechadas": len(lista),
            "lead_time_mediano_dias": mediana([i["lead_time_dias"] for i in lista]),
        }

    linhas = [linha("fase", f, [i for i in fechadas if i["fase"] == f]) for f in _fases(fechadas)]
    por_label = [linha("label", label, lista) for label, lista in _agrupar_por_label(fechadas).items()]
    return linhas + sorted(por_label, key=lambda l: -l["issues_fechadas"])


def calcular_tempo_revisao(prs: list[dict]) -> list[dict]:
    """
    Mediana, em horas, da espera ate a primeira revisao e do intervalo entre
    abertura e merge dos PRs, por fase e por tipo de trabalho.
    """
    def linha(recorte: str, grupo: str, lista: list[dict]) -> dict | None:
        esperas = [p["espera_revisao_h"] for p in lista if p["espera_revisao_h"] is not None]
        merges = [p["abertura_merge_h"] for p in lista if p["abertura_merge_h"] is not None]
        if not esperas and not merges:
            return None
        return {
            "recorte": recorte,
            "grupo": grupo,
            "prs_com_revisao": len(esperas),
            "espera_revisao_mediana_h": mediana(esperas),
            "prs_integrados": len(merges),
            "abertura_merge_mediana_h": mediana(merges),
        }

    por_fase = [linha("fase", f, [p for p in prs if p["fase"] == f]) for f in _fases(prs)]
    por_label = [linha("label", label, lista) for label, lista in _agrupar_por_label(prs, "_labels").items()]
    por_label = sorted([l for l in por_label if l], key=lambda l: -l["prs_integrados"])
    return [l for l in por_fase if l] + por_label


def calcular_distribuicao_revisoes(revisores: list[dict], mapa_equipe: dict[str, str]) -> list[dict]:
    """PRs revisados por integrante no projeto inteiro. Quem nao revisou aparece com zero."""
    linhas = [
        {
            "revisor": mapa_equipe.get(r["revisor"], r["revisor"]),
            "login": r["revisor"],
            "prs_revisados": r["prs_revisados"],
            "percentual": r["percentual"],
        }
        for r in revisores if r["fase"] == "Total"
    ]
    presentes = {l["login"] for l in linhas}
    linhas += [
        {"revisor": nome, "login": login, "prs_revisados": 0, "percentual": 0.0}
        for login, nome in mapa_equipe.items() if login not in presentes
    ]
    return linhas


def calcular_issues_label_fase(issues: list[dict], fases: list[str]) -> list[dict]:
    """Quantidade de issues por tipo de trabalho, aberta por fase."""
    linhas = []
    for label, lista in _agrupar_por_label(issues).items():
        linha = {"label": label}
        for fase in fases:
            linha[fase] = sum(1 for i in lista if i["fase"] == fase)
        linha["total"] = len(lista)
        linhas.append(linha)
    return sorted(linhas, key=lambda l: -l["total"])


# ---------------------------------------------------------------- desenho

def _num(valor: float, casas: int = 1) -> str:
    """Numero no formato brasileiro, sem casas decimais quando e inteiro."""
    arredondado = round(float(valor), casas)
    if arredondado.is_integer():
        return f"{int(arredondado)}"
    return f"{arredondado:.{casas}f}".replace(".", ",")


def _nova_figura(plt, titulo: str, subtitulo: str, rodape: str, paineis: int = 1):
    fig, eixos = plt.subplots(1, paineis, figsize=(19.2, 10.8), dpi=100, squeeze=False)
    fig.patch.set_facecolor(COR_FUNDO)
    fig.subplots_adjust(left=0.08, right=0.96, top=0.80 if paineis == 1 else 0.76, bottom=0.17, wspace=0.42)
    fig.text(0.04, 0.945, titulo, fontsize=32, fontweight="bold", color=COR_TEXTO, va="top")
    fig.text(0.04, 0.885, subtitulo, fontsize=21, color=COR_TEXTO_2, va="top")
    fig.text(0.04, 0.035, rodape, fontsize=16, color=COR_TEXTO_2, va="bottom")
    for eixo in eixos[0]:
        eixo.set_facecolor(COR_FUNDO)
        for lado in ("top", "right", "left"):
            eixo.spines[lado].set_visible(False)
        eixo.spines["bottom"].set_color(COR_NEUTRA)
        eixo.tick_params(colors=COR_TEXTO_2, labelsize=19, length=0, pad=8)
        eixo.set_axisbelow(True)
    return fig, list(eixos[0])


def _grade(eixo, direcao: str) -> None:
    eixo.grid(axis=direcao, color=COR_GRADE, linewidth=1)


def _salvar(plt, fig, caminho: Path) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(caminho, dpi=100, facecolor=COR_FUNDO)
    plt.close(fig)
    print(f"[PNG] Gerado: {caminho}")


def _barras_h(eixo, nomes: list[str], valores: list[float], rotulos: list[str], cor: str, titulo: str,
              unidade: str) -> None:
    """Barras horizontais de uma serie so, com o valor escrito na ponta."""
    posicoes = list(range(len(nomes)))[::-1]
    eixo.barh(posicoes, valores, height=0.58, color=cor, zorder=2)
    eixo.set_yticks(posicoes, nomes)
    teto = max(valores) if valores and max(valores) > 0 else 1
    for pos, valor, rotulo in zip(posicoes, valores, rotulos):
        eixo.text(valor + teto * 0.015, pos, rotulo, va="center", ha="left", fontsize=18, color=COR_TEXTO)
    eixo.set_xlim(0, teto * 1.28)
    eixo.set_xlabel(unidade, fontsize=19, color=COR_TEXTO_2, labelpad=10)
    eixo.set_title(titulo, fontsize=22, color=COR_TEXTO, loc="left", pad=16)
    _grade(eixo, "x")


def _barras_v(eixo, nomes: list[str], valores: list[float], rotulos: list[str], cores: list[str], titulo: str,
              unidade: str) -> None:
    """Barras verticais de uma serie so, com o valor escrito acima."""
    posicoes = list(range(len(nomes)))
    eixo.bar(posicoes, valores, width=0.55, color=cores)
    eixo.set_xticks(posicoes, nomes)
    teto = max(valores) if valores and max(valores) > 0 else 1
    for pos, valor, rotulo in zip(posicoes, valores, rotulos):
        eixo.text(pos, valor + teto * 0.02, rotulo, ha="center", va="bottom", fontsize=18, color=COR_TEXTO)
    eixo.set_ylim(0, teto * 1.22)
    eixo.set_ylabel(unidade, fontsize=19, color=COR_TEXTO_2, labelpad=10)
    eixo.set_title(titulo, fontsize=22, color=COR_TEXTO, loc="left", pad=16)
    _grade(eixo, "y")


def _legenda(eixo, **opcoes) -> None:
    eixo.legend(frameon=False, fontsize=19, labelcolor=COR_TEXTO, **opcoes)


def desenhar_burnup(plt, linhas: list[dict], marcos: list[tuple[str, datetime]], rodape: str, caminho: Path) -> None:
    datas = [datetime.fromisoformat(l["data"]) for l in linhas]
    criadas = [l["criadas_acumuladas"] for l in linhas]
    fechadas = [l["fechadas_acumuladas"] for l in linhas]
    fig, (eixo,) = _nova_figura(
        plt, "Burn-up do projeto: issues criadas e fechadas",
        "Quantidade acumulada de issues, com o fim de cada fase marcado", rodape)
    eixo.step(datas, criadas, where="post", color=COR_TEXTO_2, linewidth=3, label="Issues criadas (escopo)")
    eixo.step(datas, fechadas, where="post", color=COR_SERIE, linewidth=3, label="Issues fechadas")
    eixo.fill_between(datas, fechadas, step="post", color=COR_SERIE, alpha=0.10)
    teto = max(criadas) * 1.18
    for fase, data in marcos:
        if datas[0] <= data <= datas[-1] + timedelta(days=3):
            eixo.axvline(data, color=COR_NEUTRA, linewidth=1.5)
            eixo.text(data, teto * 0.985, f" {fase}\n {data:%d/%m}", ha="left", va="top", fontsize=17,
                      color=COR_TEXTO_2)
    for serie, cor in ((criadas, COR_TEXTO_2), (fechadas, COR_SERIE)):
        eixo.plot(datas[-1], serie[-1], "o", markersize=11, color=cor, markeredgecolor=COR_FUNDO,
                  markeredgewidth=2)
    deslocamento = 14 if criadas[-1] - fechadas[-1] < teto * 0.05 else 0
    eixo.annotate(_num(criadas[-1]), (datas[-1], criadas[-1]), xytext=(12, deslocamento),
                  textcoords="offset points", fontsize=20, fontweight="bold", color=COR_TEXTO, va="center")
    eixo.annotate(_num(fechadas[-1]), (datas[-1], fechadas[-1]), xytext=(12, -deslocamento),
                  textcoords="offset points", fontsize=20, fontweight="bold", color=COR_TEXTO, va="center")
    eixo.set_ylim(0, teto)
    eixo.set_xlim(datas[0], max(datas[-1], max(d for _, d in marcos)) + timedelta(days=5))
    eixo.set_ylabel("Issues (acumulado)", fontsize=19, color=COR_TEXTO_2, labelpad=10)
    import matplotlib.dates as mdates
    eixo.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO))
    eixo.xaxis.set_major_formatter(mdates.DateFormatter("%d/%m"))
    _grade(eixo, "y")
    _legenda(eixo, loc="upper left", bbox_to_anchor=(0.0, 0.86))
    _salvar(plt, fig, caminho)


def _empilhadas(plt, linhas, chave_base, chave_topo, rotulo_base, rotulo_topo, cor_base, cor_topo,
                rotulo_acima, titulo, subtitulo, rodape, caminho) -> None:
    fig, (eixo,) = _nova_figura(plt, titulo, subtitulo, rodape)
    fases = [l["fase"] for l in linhas]
    base = [l[chave_base] for l in linhas]
    topo = [l[chave_topo] for l in linhas]
    posicoes = list(range(len(fases)))
    eixo.bar(posicoes, base, width=0.5, color=cor_base, label=rotulo_base, edgecolor=COR_FUNDO, linewidth=2)
    eixo.bar(posicoes, topo, width=0.5, bottom=base, color=cor_topo, label=rotulo_topo, edgecolor=COR_FUNDO,
             linewidth=2)
    teto = max(b + t for b, t in zip(base, topo))
    for pos, b, t, linha in zip(posicoes, base, topo, linhas):
        if b >= teto * 0.06:
            eixo.text(pos, b / 2, _num(b), ha="center", va="center", fontsize=19, color="#ffffff",
                      fontweight="bold")
        if t >= teto * 0.06:
            eixo.text(pos, b + t / 2, _num(t), ha="center", va="center", fontsize=19,
                      color=COR_TEXTO if cor_topo == COR_NEUTRA else "#ffffff", fontweight="bold")
        eixo.text(pos, b + t + teto * 0.025, rotulo_acima(linha), ha="center", va="bottom", fontsize=19,
                  color=COR_TEXTO)
    eixo.set_xticks(posicoes, fases)
    eixo.set_ylim(0, teto * 1.25)
    eixo.set_ylabel("Issues", fontsize=19, color=COR_TEXTO_2, labelpad=10)
    _grade(eixo, "y")
    _legenda(eixo, loc="upper left", ncols=2)
    _salvar(plt, fig, caminho)


def desenhar_aderencia(plt, linhas: list[dict], rodape: str, caminho: Path) -> None:
    _empilhadas(
        plt, linhas, "issues_no_prazo", "issues_em_atraso", "No prazo", "Em atraso", COR_NO_PRAZO, COR_EM_ATRASO,
        lambda l: f"{_num(l['aderencia_prazo_pct'])}% no prazo",
        "Aderência ao prazo por fase", "Issues de cada fase concluídas ou em andamento dentro do Prazo, e em atraso",
        rodape, caminho)


def desenhar_bloqueio(plt, linhas: list[dict], rodape: str, caminho: Path) -> None:
    _empilhadas(
        plt, linhas, "travadas", "nao_travadas", "Travadas por dependência", "Não travadas", COR_EM_ATRASO,
        COR_NEUTRA, lambda l: f"{_num(l['travadas_pct'])}% travadas",
        "Issues travadas por dependência, por fase",
        "Issues com dependência declarada. Travada: a dependência fechou, ou segue aberta, depois do Prazo da issue",
        rodape, caminho)


def desenhar_acuracia_labels(plt, linhas: list[dict], rodape: str, caminho: Path) -> None:
    fig, (eixo,) = _nova_figura(
        plt, "Acurácia da estimativa por tipo de trabalho",
        "Horas reais sobre horas estimadas. Faixa ideal: 80% a 120%", rodape)
    fig.subplots_adjust(left=0.22)
    nomes = [f"{l['label']} (n={l['issues_avaliadas']})" for l in linhas]
    valores = [l["acuracia_pct"] for l in linhas]
    eixo.axvspan(80, 120, color=COR_NO_PRAZO, alpha=0.12, label="Faixa ideal (80% a 120%)")
    eixo.axvline(100, color=COR_NEUTRA, linewidth=1.5, zorder=1)
    _barras_h(eixo, nomes, valores, [f"{_num(v)}%" for v in valores], COR_SERIE, "", "Horas reais / horas estimadas (%)")
    eixo.set_xlim(0, max(max(valores) * 1.2, 140))
    _legenda(eixo, loc="lower right")
    _salvar(plt, fig, caminho)


def _dois_recortes(linhas: list[dict], primeiro: str) -> tuple[list[dict], list[dict]]:
    return [l for l in linhas if l["recorte"] == primeiro], [l for l in linhas if l["recorte"] == "label"]


def desenhar_horas(plt, linhas: list[dict], rodape: str, caminho: Path) -> None:
    pessoas, labels = _dois_recortes(linhas, "integrante")
    fig, (esq, dir_) = _nova_figura(
        plt, "Horas reais por integrante e por tipo de trabalho",
        "Horas reais registradas nas issues do projeto inteiro", rodape, paineis=2)
    fig.subplots_adjust(left=0.17)
    for eixo, lista, titulo in ((esq, pessoas, "Por integrante"), (dir_, labels, "Por tipo de trabalho")):
        valores = [l["horas_reais"] for l in lista]
        _barras_h(eixo, [l["grupo"] for l in lista], valores, [f"{_num(v)} h" for v in valores], COR_SERIE,
                  titulo, "Horas reais")
    _salvar(plt, fig, caminho)


def desenhar_lead_time(plt, linhas: list[dict], rodape: str, caminho: Path) -> None:
    fases, labels = _dois_recortes(linhas, "fase")
    fig, (esq, dir_) = _nova_figura(
        plt, "Lead time das issues: da criação ao fechamento",
        "Mediana em dias das issues fechadas, com a quantidade de issues (n)", rodape, paineis=2)
    valores = [l["lead_time_mediano_dias"] for l in fases]
    _barras_v(esq, [l["grupo"] for l in fases], valores,
              [f"{_num(v)} d\nn={l['issues_fechadas']}" for v, l in zip(valores, fases)],
              [CORES_FASE.get(l["grupo"], COR_SERIE) for l in fases], "Por fase", "Dias (mediana)")
    esq.set_ylim(0, max(valores) * 1.3)
    valores = [l["lead_time_mediano_dias"] for l in labels]
    _barras_h(dir_, [l["grupo"] for l in labels], valores,
              [f"{_num(v)} d (n={l['issues_fechadas']})" for v, l in zip(valores, labels)], COR_SERIE,
              "Por tipo de trabalho", "Dias (mediana)")
    dir_.set_xlim(0, max(valores) * 1.45)
    _salvar(plt, fig, caminho)


def desenhar_tempo_revisao(plt, linhas: list[dict], rodape: str, caminho: Path) -> None:
    fases, labels = _dois_recortes(linhas, "fase")
    fig, (esq, dir_) = _nova_figura(
        plt, "Tempo de revisão dos pull requests",
        "Mediana em horas: espera até a primeira revisão e intervalo entre abertura e merge", rodape, paineis=2)
    series = (
        ("espera_revisao_mediana_h", "Espera até a 1ª revisão", COR_SERIE),
        ("abertura_merge_mediana_h", "Abertura até o merge", COR_SERIE_2),
    )
    largura = 0.36
    teto = max((l[c] or 0) for l in fases + labels for c, _, _ in series) or 1

    posicoes = list(range(len(fases)))
    for k, (chave, rotulo, cor) in enumerate(series):
        xs = [p + (k - 0.5) * (largura + 0.03) for p in posicoes]
        valores = [l[chave] or 0 for l in fases]
        esq.bar(xs, valores, width=largura, color=cor, label=rotulo)
        for x, v, l in zip(xs, valores, fases):
            if l[chave] is not None:
                esq.text(x, v + teto * 0.015, _num(v), ha="center", va="bottom", fontsize=17, color=COR_TEXTO)
    esq.set_xticks(posicoes, [f"{l['grupo']}\nn={l['prs_integrados']}" for l in fases])
    esq.set_ylim(0, max((l[c] or 0) for l in fases for c, _, _ in series) * 1.3 or 1)
    esq.set_ylabel("Horas (mediana)", fontsize=19, color=COR_TEXTO_2, labelpad=10)
    esq.set_title("Por fase", fontsize=22, color=COR_TEXTO, loc="left", pad=16)
    _grade(esq, "y")
    _legenda(esq, loc="upper left")

    posicoes = list(range(len(labels)))[::-1]
    for k, (chave, rotulo, cor) in enumerate(series):
        ys = [p - (k - 0.5) * (largura + 0.03) for p in posicoes]
        valores = [l[chave] or 0 for l in labels]
        dir_.barh(ys, valores, height=largura, color=cor)
        for y, v, l in zip(ys, valores, labels):
            if l[chave] is not None:
                dir_.text(v + teto * 0.012, y, _num(v), ha="left", va="center", fontsize=16, color=COR_TEXTO)
    dir_.set_yticks(posicoes, [f"{l['grupo']} (n={l['prs_integrados']})" for l in labels])
    dir_.set_xlim(0, max((l[c] or 0) for l in labels for c, _, _ in series) * 1.25 or 1)
    dir_.set_xlabel("Horas (mediana)", fontsize=19, color=COR_TEXTO_2, labelpad=10)
    dir_.set_title("Por tipo de trabalho", fontsize=22, color=COR_TEXTO, loc="left", pad=16)
    _grade(dir_, "x")
    _salvar(plt, fig, caminho)


def desenhar_distribuicao_revisoes(plt, linhas: list[dict], rodape: str, caminho: Path) -> None:
    fig, (eixo,) = _nova_figura(
        plt, "Distribuição das revisões de pull requests",
        "Quantidade de PRs revisados por integrante no projeto inteiro", rodape)
    fig.subplots_adjust(left=0.22)
    valores = [l["prs_revisados"] for l in linhas]
    _barras_h(eixo, [l["revisor"] for l in linhas], valores,
              [f"{v} ({_num(l['percentual'])}%)" for v, l in zip(valores, linhas)], COR_SERIE, "", "PRs revisados")
    _salvar(plt, fig, caminho)


def desenhar_issues_label_fase(plt, linhas: list[dict], fases: list[str], rodape: str, caminho: Path) -> None:
    fig, (eixo,) = _nova_figura(
        plt, "Issues por tipo de trabalho e por fase",
        "Quantidade de issues de cada tipo, dividida pela fase em que foram planejadas", rodape)
    fig.subplots_adjust(left=0.17)
    posicoes = list(range(len(linhas)))[::-1]
    acumulado = [0] * len(linhas)
    teto = max(l["total"] for l in linhas)
    for fase in fases:
        valores = [l[fase] for l in linhas]
        eixo.barh(posicoes, valores, left=acumulado, height=0.6, color=CORES_FASE.get(fase, COR_SERIE),
                  label=fase, edgecolor=COR_FUNDO, linewidth=2)
        for pos, valor, inicio in zip(posicoes, valores, acumulado):
            if valor >= teto * 0.04:
                eixo.text(inicio + valor / 2, pos, _num(valor), ha="center", va="center", fontsize=17,
                          color=COR_TEXTO if fase == "Fase 4" else "#ffffff", fontweight="bold")
        acumulado = [a + v for a, v in zip(acumulado, valores)]
    for pos, linha in zip(posicoes, linhas):
        eixo.text(linha["total"] + teto * 0.012, pos, _num(linha["total"]), va="center", fontsize=19,
                  color=COR_TEXTO, fontweight="bold")
    eixo.set_yticks(posicoes, [l["label"] for l in linhas])
    eixo.set_xlim(0, teto * 1.1)
    eixo.set_xlabel("Issues", fontsize=19, color=COR_TEXTO_2, labelpad=10)
    _grade(eixo, "x")
    _legenda(eixo, loc="lower right")
    _salvar(plt, fig, caminho)


# ---------------------------------------------------------------- orquestracao

def _salvar_csv(caminho: Path, linhas: list[dict], colunas: list[str] | None = None) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    colunas = colunas or (list(linhas[0]) if linhas else [])
    with open(caminho, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=colunas, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(linhas)
    print(f"[CSV] Gerado: {caminho}")


def gerar_graficos_projeto(resultado: dict, medidas: dict, dados_brutos: dict, config: dict, dir_saida: Path) -> None:
    """Calcula, grava os CSVs 09 a 17 em dir_saida e desenha os PNGs em dir_saida/graficos."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams["font.family"] = "DejaVu Sans"

    issues = resultado["issues"]
    mapa_equipe = config.get("integrantes", {})
    coletado = datetime.fromisoformat(dados_brutos["coletado_em"])
    fases = _fases(issues)
    marcos = [
        (m["title"], datetime.fromisoformat(m["due_on"].replace("Z", "+00:00")).replace(tzinfo=None))
        for m in sorted(dados_brutos.get("milestones", []), key=lambda m: m.get("due_on") or "")
        if m.get("due_on")
    ]
    fonte = f"Fonte: GitHub, coleta de {coletado.astimezone(FUSO_BRT):%d/%m/%Y}."
    fonte_labels = f"{fonte} {NOTA_LABELS}"
    graficos = dir_saida / "graficos"

    def saida(nome: str, linhas: list[dict], colunas: list[str] | None = None) -> Path:
        _salvar_csv(dir_saida / f"{nome}.csv", linhas, colunas)
        return graficos / f"{nome}.png"

    linhas = calcular_burnup(issues, coletado)
    desenhar_burnup(plt, linhas, marcos, fonte, saida("09_burnup_projeto", linhas))

    linhas = calcular_aderencia(resultado["resumo_fases"])
    desenhar_aderencia(plt, linhas, fonte, saida("10_aderencia_prazo_fases", linhas))

    linhas = calcular_bloqueio(issues, coletado)
    desenhar_bloqueio(plt, linhas, fonte, saida("11_bloqueio_dependencias_fases", linhas))

    linhas = calcular_acuracia_labels(issues)
    desenhar_acuracia_labels(plt, linhas, fonte_labels, saida("12_acuracia_estimativa_labels", linhas))

    linhas = calcular_horas(issues, mapa_equipe)
    desenhar_horas(plt, linhas, fonte_labels, saida("13_horas_reais_integrante_label", linhas))

    linhas = calcular_lead_time(issues)
    desenhar_lead_time(plt, linhas, fonte_labels, saida("14_lead_time_issues", linhas))

    linhas = calcular_tempo_revisao(medidas["revisao"]["prs"])
    desenhar_tempo_revisao(
        plt, linhas, f"{fonte} n: PRs integrados. PR com mais de um tipo de trabalho conta em cada um.",
        saida("15_tempo_revisao_prs", linhas))

    linhas = calcular_distribuicao_revisoes(medidas["revisao"]["revisores"], mapa_equipe)
    desenhar_distribuicao_revisoes(plt, linhas, fonte, saida("16_distribuicao_revisoes", linhas))

    linhas = calcular_issues_label_fase(issues, fases)
    desenhar_issues_label_fase(
        plt, linhas, fases, fonte_labels, saida("17_issues_label_fase", linhas, ["label", *fases, "total"]))
