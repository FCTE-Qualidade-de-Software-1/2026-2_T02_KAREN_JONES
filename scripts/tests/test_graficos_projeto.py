"""Testes das funcoes de calculo de scripts/graficos_projeto.py."""

import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import graficos_projeto as gp  # noqa: E402

BRT = timezone(timedelta(hours=-3))


def dia(d: int, mes: int = 10, hora: int = 12) -> datetime:
    return datetime(2026, mes, d, hora, 0, tzinfo=BRT)


def issue(numero: int, **campos) -> dict:
    base = {
        "numero": numero,
        "fase": "Fase 1",
        "estado": "closed",
        "labels": ["gestao"],
        "assignees": ["ana"],
        "estimativa_h": 0.0,
        "horas_reais_h": 0.0,
        "horas_por_pessoa": {},
        "dt_criacao": dia(1),
        "dt_fechamento": dia(5),
        "dt_prazo": None,
        "dependencias": [],
        "lead_time_dias": 4.0,
    }
    base.update(campos)
    return base


def test_labels_de_tipo_ignora_subgrupos_e_retroativa():
    labels = ["subgrupo-F1F3", "gestao", "retroativa", "artigo", "subgrupo-F2F4"]
    assert gp.labels_de_tipo(labels) == ["gestao", "artigo"]


def test_mediana_par_impar_e_vazia():
    assert gp.mediana([3, 1, 2]) == 2
    assert gp.mediana([4, 1, 2, 3]) == 2.5
    assert gp.mediana([]) is None


def test_burnup_acumula_criadas_e_fechadas_por_dia():
    issues = [
        issue(1, dt_criacao=dia(1), dt_fechamento=dia(3)),
        issue(2, dt_criacao=dia(1), dt_fechamento=None, estado="open"),
        issue(3, dt_criacao=dia(2), dt_fechamento=dia(3)),
    ]
    linhas = gp.calcular_burnup(issues, agora=dia(4))
    assert [l["data"] for l in linhas] == ["2026-10-01", "2026-10-02", "2026-10-03", "2026-10-04"]
    assert [l["criadas_acumuladas"] for l in linhas] == [2, 3, 3, 3]
    assert [l["fechadas_acumuladas"] for l in linhas] == [0, 0, 2, 2]


def test_burnup_usa_o_dia_no_horario_de_brasilia():
    # 02/10 01:00 UTC ainda e 01/10 as 22:00 em Brasilia.
    criada = datetime(2026, 10, 2, 1, 0, tzinfo=timezone.utc)
    linhas = gp.calcular_burnup([issue(1, dt_criacao=criada, dt_fechamento=None)], agora=dia(2))
    assert linhas[0] == {"data": "2026-10-01", "criadas_acumuladas": 1, "fechadas_acumuladas": 0}


def test_aderencia_reaproveita_o_resumo_das_fases():
    resumo = [{"fase": "Fase 1", "total_issues": 18, "issues_no_prazo": 6, "issues_em_atraso": 12,
               "aderencia_prazo_pct": 33.3, "horas_reais": 10}]
    assert gp.calcular_aderencia(resumo) == [
        {"fase": "Fase 1", "total_issues": 18, "issues_no_prazo": 6, "issues_em_atraso": 12,
         "aderencia_prazo_pct": 33.3}
    ]


def test_bloqueio_dependencia_fechada_depois_do_prazo_trava():
    issues = [
        issue(1, dt_fechamento=dia(12)),
        issue(2, dependencias=[1], dt_prazo=dia(10)),
    ]
    linhas = gp.calcular_bloqueio(issues, agora=dia(30))
    assert linhas == [{"fase": "Fase 1", "issues_com_dependencia": 1, "travadas": 1,
                       "nao_travadas": 0, "travadas_pct": 100.0, "travadas_lista": "#2"}]


def test_bloqueio_dependencia_fechada_antes_do_prazo_nao_trava():
    issues = [
        issue(1, dt_fechamento=dia(8)),
        issue(2, dependencias=[1], dt_prazo=dia(10)),
    ]
    linha = gp.calcular_bloqueio(issues, agora=dia(30))[0]
    assert (linha["travadas"], linha["nao_travadas"], linha["travadas_lista"]) == (0, 1, "")


def test_bloqueio_dependencia_aberta_so_trava_depois_do_prazo():
    issues = [
        issue(1, estado="open", dt_fechamento=None),
        issue(2, dependencias=[1], dt_prazo=dia(10), estado="open", dt_fechamento=None),
    ]
    assert gp.calcular_bloqueio(issues, agora=dia(9))[0]["travadas"] == 0
    assert gp.calcular_bloqueio(issues, agora=dia(11))[0]["travadas"] == 1


def test_bloqueio_ignora_issue_sem_dependencia_auto_referencia_e_numero_desconhecido():
    issues = [
        issue(1),
        issue(2, dependencias=[2, 999], dt_prazo=dia(10)),
    ]
    assert gp.calcular_bloqueio(issues, agora=dia(30)) == []


def test_bloqueio_sem_prazo_conta_como_nao_travada():
    issues = [issue(1, dt_fechamento=dia(20)), issue(2, dependencias=[1], dt_prazo=None)]
    linha = gp.calcular_bloqueio(issues, agora=dia(30))[0]
    assert (linha["issues_com_dependencia"], linha["travadas"]) == (1, 0)


def test_acuracia_por_label_usa_so_issues_com_estimativa_e_horas():
    issues = [
        issue(1, labels=["gestao", "subgrupo-F1F3"], estimativa_h=10, horas_reais_h=12),
        issue(2, labels=["gestao"], estimativa_h=10, horas_reais_h=0),
        issue(3, labels=["artigo", "gestao"], estimativa_h=5, horas_reais_h=3),
    ]
    linhas = gp.calcular_acuracia_labels(issues)
    assert linhas == [
        {"label": "gestao", "issues_avaliadas": 2, "horas_estimadas": 15.0, "horas_reais": 15.0,
         "acuracia_pct": 100.0},
        {"label": "artigo", "issues_avaliadas": 1, "horas_estimadas": 5.0, "horas_reais": 3.0,
         "acuracia_pct": 60.0},
    ]


def test_horas_reais_por_integrante_e_por_label():
    issues = [
        issue(1, labels=["gestao"], horas_reais_h=6, horas_por_pessoa={"ana": 4, "bia": 2}),
        issue(2, labels=["artigo", "gestao"], horas_reais_h=3, horas_por_pessoa={"bia": 3}),
    ]
    linhas = gp.calcular_horas(issues, {"ana": "Ana", "bia": "Bia"})
    assert linhas == [
        {"recorte": "integrante", "grupo": "Bia", "horas_reais": 5.0},
        {"recorte": "integrante", "grupo": "Ana", "horas_reais": 4.0},
        {"recorte": "label", "grupo": "gestao", "horas_reais": 9.0},
        {"recorte": "label", "grupo": "artigo", "horas_reais": 3.0},
    ]


def test_lead_time_mediana_por_fase_e_por_label_so_de_fechadas():
    issues = [
        issue(1, fase="Fase 1", labels=["gestao"], lead_time_dias=2.0),
        issue(2, fase="Fase 1", labels=["gestao"], lead_time_dias=10.0),
        issue(3, fase="Fase 1", labels=["artigo"], lead_time_dias=4.0),
        issue(4, fase="Fase 2", labels=["artigo"], lead_time_dias=None, estado="open", dt_fechamento=None),
    ]
    linhas = gp.calcular_lead_time(issues)
    assert linhas == [
        {"recorte": "fase", "grupo": "Fase 1", "issues_fechadas": 3, "lead_time_mediano_dias": 4.0},
        {"recorte": "label", "grupo": "gestao", "issues_fechadas": 2, "lead_time_mediano_dias": 6.0},
        {"recorte": "label", "grupo": "artigo", "issues_fechadas": 1, "lead_time_mediano_dias": 4.0},
    ]


def test_tempo_revisao_medianas_por_fase_e_por_label():
    prs = [
        {"fase": "Fase 1", "_labels": ["gestao", "subgrupo-F1F3"], "espera_revisao_h": 2.0, "abertura_merge_h": 10.0},
        {"fase": "Fase 1", "_labels": ["gestao"], "espera_revisao_h": 6.0, "abertura_merge_h": 30.0},
        {"fase": "Fase 1", "_labels": [], "espera_revisao_h": None, "abertura_merge_h": 20.0},
        {"fase": "Fase 2", "_labels": ["artigo"], "espera_revisao_h": None, "abertura_merge_h": None},
    ]
    linhas = gp.calcular_tempo_revisao(prs)
    assert linhas == [
        {"recorte": "fase", "grupo": "Fase 1", "prs_com_revisao": 2, "espera_revisao_mediana_h": 4.0,
         "prs_integrados": 3, "abertura_merge_mediana_h": 20.0},
        {"recorte": "label", "grupo": "gestao", "prs_com_revisao": 2, "espera_revisao_mediana_h": 4.0,
         "prs_integrados": 2, "abertura_merge_mediana_h": 20.0},
    ]


def test_distribuicao_revisoes_usa_o_total_o_nome_e_inclui_quem_nao_revisou():
    revisores = [
        {"fase": "Fase 1", "revisor": "ana", "prs_revisados": 1, "percentual": 100.0},
        {"fase": "Total", "revisor": "ana", "prs_revisados": 3, "percentual": 75.0},
        {"fase": "Total", "revisor": "zed", "prs_revisados": 1, "percentual": 25.0},
    ]
    assert gp.calcular_distribuicao_revisoes(revisores, {"ana": "Ana", "bia": "Bia"}) == [
        {"revisor": "Ana", "login": "ana", "prs_revisados": 3, "percentual": 75.0},
        {"revisor": "zed", "login": "zed", "prs_revisados": 1, "percentual": 25.0},
        {"revisor": "Bia", "login": "bia", "prs_revisados": 0, "percentual": 0.0},
    ]


def test_issues_por_label_e_fase():
    issues = [
        issue(1, fase="Fase 1", labels=["gestao"]),
        issue(2, fase="Fase 2", labels=["gestao", "artigo"]),
        issue(3, fase="Fase 2", labels=["subgrupo-F1F3"]),
    ]
    linhas = gp.calcular_issues_label_fase(issues, ["Fase 1", "Fase 2"])
    assert linhas == [
        {"label": "gestao", "Fase 1": 1, "Fase 2": 1, "total": 2},
        {"label": "artigo", "Fase 1": 0, "Fase 2": 1, "total": 1},
    ]
