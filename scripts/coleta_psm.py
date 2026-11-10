#!/usr/bin/env python3
"""
Script de coleta e calculo dos indicadores PSM/CID do projeto.

Coleta issues, milestones, pull requests e commits pela API do GitHub e gera,
em dados/gestao/, planilhas CSV, graficos PNG e os blocos descritivos no
modelo "Measurement Construct" das tres categorias exigidas:
1. Recursos e Custos (Resources and Cost)
2. Calendario e Progresso (Schedule and Progress)
3. Desempenho dos Processos (Process Performance)
"""

import argparse
import csv
import json
import math
import os
import re
import shutil
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path


def carregar_config(caminho_config: Path) -> dict:
    """Carrega o arquivo JSON de configuracao com valor-hora, fonte e equipe."""
    with open(caminho_config, "r", encoding="utf-8") as f:
        return json.load(f)


def requisitar_github(url: str, token: str | None = None) -> list | dict:
    """Realiza uma chamada GET na API do GitHub retornando o JSON."""
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "PSM-CID-Collector-UnB"
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def requisitar_github_paginado(url: str, token: str | None = None) -> list:
    """Realiza chamadas GET paginadas na API do GitHub retornando a lista completa de resultados."""
    resultados = []
    pagina = 1
    separador = "&" if "?" in url else "?"
    while True:
        url_pag = f"{url}{separador}page={pagina}"
        resp_data = requisitar_github(url_pag, token)
        if isinstance(resp_data, list):
            if not resp_data:
                break
            resultados.extend(resp_data)
            if len(resp_data) < 100:
                break
            pagina += 1
        else:
            return resp_data
    return resultados


def coletar_dados_github(repo: str, token: str | None, arquivo_raw: Path, usar_offline: bool) -> dict:
    """
    Extrai issues (abertas e fechadas), milestones e commits da API do GitHub
    ou carrega a partir do cache local para garantir rastreabilidade (Premissa 5).
    """
    if usar_offline and arquivo_raw.exists():
        print(f"[INFO] Carregando dados brutos locais de {arquivo_raw}...")
        with open(arquivo_raw, "r", encoding="utf-8") as f:
            return json.load(f)

    print(f"[INFO] Coletando dados do repositorio {repo} via API do GitHub...")
    base_url = f"https://api.github.com/repos/{repo}"

    issues_e_prs = requisitar_github_paginado(f"{base_url}/issues?state=all&per_page=100", token)
    milestones = requisitar_github_paginado(f"{base_url}/milestones?state=all&per_page=100", token)
    commits = requisitar_github_paginado(f"{base_url}/commits?per_page=100", token)

    revisoes_prs = {}
    for item in issues_e_prs:
        if "pull_request" not in item:
            continue
        revisoes = requisitar_github_paginado(f"{base_url}/pulls/{item['number']}/reviews?per_page=100", token)
        revisoes_prs[str(item["number"])] = [
            {
                "revisor": (r.get("user") or {}).get("login"),
                "estado": r.get("state"),
                "enviada_em": r.get("submitted_at")
            }
            for r in revisoes
        ]

    dados_brutos = {
        "coletado_em": datetime.now(timezone.utc).isoformat(),
        "repositorio": repo,
        "issues_e_prs": issues_e_prs,
        "milestones": milestones,
        "commits": commits,
        "revisoes_prs": revisoes_prs
    }

    arquivo_raw.parent.mkdir(parents=True, exist_ok=True)
    with open(arquivo_raw, "w", encoding="utf-8") as f:
        json.dump(dados_brutos, f, ensure_ascii=False, indent=2)

    print(f"[INFO] Snapshot bruto salvo em {arquivo_raw}")
    return dados_brutos


def extrair_secao_markdown(corpo: str, titulo_secao: str) -> str:
    """Extrai o texto logo abaixo de um cabecalho '### <titulo_secao>' no corpo da issue."""
    if not corpo:
        return ""
    padrao = rf"###\s+{re.escape(titulo_secao)}\s*\n+(.*?)(?=\n+###\s+|\Z)"
    match = re.search(padrao, corpo, flags=re.DOTALL | re.IGNORECASE)
    if not match:
        return ""
    valor = match.group(1).strip()
    if valor.lower() in ("_no response_", "_a preencher pelo responsável_", "_a preencher pelo responsavel_", "nenhuma"):
        return ""
    return valor


def registrar_aviso(avisos: list | None, numero: int | None, tipo: str, mensagem: str) -> None:
    """Guarda um aviso da coleta para imprimir no fim e salvar em CSV."""
    if avisos is not None:
        avisos.append({"issue": numero if numero is not None else "", "tipo": tipo, "mensagem": mensagem})


def extrair_numero_float(texto: str, avisos: list | None = None, numero: int | None = None) -> float:
    """
    Extrai valor em horas de uma string, suportando formatos como:
    - '1h30m' ou '2h30' -> 1.5, 2.5
    - '20m' ou '30 min' -> 0.33, 0.5
    - '2.5' ou '2,5' ou '4' -> 2.5, 4.0
    Um valor como '2h5' e lido como 2 horas e 5 minutos e gera aviso, porque
    pode ter sido escrito querendo dizer 2,5 horas.
    """
    if not texto:
        return 0.0
    texto_limpo = texto.strip().lower().replace(",", ".")
    match_hm = re.search(r"(\d+)\s*h(?:oras?)?\s*(\d+)", texto_limpo)
    if match_hm:
        horas = int(match_hm.group(1))
        minutos = int(match_hm.group(2))
        if len(match_hm.group(2)) == 1:
            registrar_aviso(
                avisos, numero, "formato ambiguo",
                f"'{texto.strip()}' lido como {horas}h{minutos:02d}min, confira se nao era {horas}.{minutos}h"
            )
        return round(horas + (minutos / 60.0), 2)
    match_m = re.search(r"(\d+)\s*(?:m|min|minutos)\b", texto_limpo)
    if match_m:
        minutos = int(match_m.group(1))
        return round(minutos / 60.0, 2)
    match = re.search(r"(\d+(?:\.\d+)?)", texto_limpo)
    return float(match.group(1)) if match else 0.0


def extrair_horas_reais(
    texto: str,
    assignees: list[str],
    avisos: list | None = None,
    numero: int | None = None,
    equipe: dict | None = None
) -> tuple[float, dict[str, float]]:
    """
    Interpreta o campo 'Horas reais (h)' suportando os formatos:
    - '5 (@usuario1: 3, @usuario2: 2)'
    - '@usuario1: 3, @usuario2: 2' ou '@usuario1 3, @usuario2 2' (dois-pontos opcionais)
    - '4' (divide igualmente entre os assignees da issue)
    Retorna (total_horas, dicionario_por_login). Horas que nao puderem ser
    lidas ou atribuidas a alguem geram aviso com o numero da issue.
    """
    if not texto:
        return 0.0, {}

    pares_usuarios = re.findall(r"@([A-Za-z0-9_-]+)\s*:?\s*(\d[^,;)\n@]*)", texto)

    por_usuario: dict[str, float] = {}
    if pares_usuarios:
        for login, horas_str in pares_usuarios:
            horas = extrair_numero_float(horas_str, avisos, numero)
            if horas <= 0:
                registrar_aviso(avisos, numero, "horas nao lidas", f"valor de @{login} ilegivel: '{horas_str.strip()}'")
            if equipe and login not in equipe:
                registrar_aviso(avisos, numero, "horas nao atribuidas", f"@{login} nao esta em scripts/config.json")
            por_usuario[login] = por_usuario.get(login, 0.0) + horas
        total = round(sum(por_usuario.values()), 2)
        logins_citados = set(re.findall(r"@([A-Za-z0-9_-]+)", texto))
        sem_horas = logins_citados - set(por_usuario)
        if sem_horas:
            registrar_aviso(
                avisos, numero, "horas nao lidas",
                "logins sem horas lidas: " + ", ".join(f"@{l}" for l in sorted(sem_horas))
            )
        prefixo = texto.split("@", 1)[0].split("(", 1)[0]
        total_declarado = extrair_numero_float(prefixo)
        if total_declarado > 0 and abs(total_declarado - total) > 0.01:
            registrar_aviso(
                avisos, numero, "horas divergentes",
                f"total declarado {total_declarado}h difere da soma por integrante {total}h"
            )
        return total, por_usuario

    tem_login = "@" in texto
    if tem_login:
        registrar_aviso(avisos, numero, "horas nao lidas", f"nao foi possivel ler horas por integrante em '{texto.strip()}'")

    total = extrair_numero_float(texto, avisos, numero)
    if total <= 0:
        if not tem_login:
            registrar_aviso(avisos, numero, "horas nao lidas", f"valor ilegivel: '{texto.strip()}'")
    elif not assignees:
        registrar_aviso(avisos, numero, "horas nao atribuidas", f"{total}h sem responsavel na issue nem @login no campo")
    else:
        parcela = round(total / len(assignees), 2)
        for login in assignees:
            por_usuario[login] = parcela
    return total, por_usuario


MAX_FAIXA_DEPENDENCIAS = 100


def extrair_dependencias(texto: str, avisos: list | None = None, numero: int | None = None) -> list[int]:
    """
    Le os numeros de issue do campo 'Depende de', incluindo faixas como '#73 a #78'.
    Faixas invertidas ou com mais de MAX_FAIXA_DEPENDENCIAS issues sao ignoradas com aviso.
    """
    if not texto:
        return []
    numeros: set[int] = set()
    for ini, fim in re.findall(r"#(\d+)\s*(?:a|até|ate|-)\s*#(\d+)", texto):
        ini, fim = int(ini), int(fim)
        if fim < ini or fim - ini >= MAX_FAIXA_DEPENDENCIAS:
            registrar_aviso(avisos, numero, "dependencia ignorada", f"faixa #{ini} a #{fim} invalida ou longa demais")
            continue
        numeros.update(range(ini, fim + 1))
    numeros.update(int(n) for n in re.findall(r"#(\d+)", texto))
    return sorted(numeros)


def para_datetime(valor: str | None) -> datetime | None:
    """Converte um timestamp ISO da API do GitHub em datetime com fuso."""
    if not valor:
        return None
    return datetime.fromisoformat(valor.replace("Z", "+00:00"))


def janelas_das_fases(milestones: list, inicio_projeto: datetime) -> dict[str, tuple[datetime, datetime]]:
    """
    Define o inicio e o fim de cada fase. O fim e o fim do dia do due_on da
    milestone no horario de Brasilia. O inicio e o fim da fase anterior ou,
    na primeira fase, a data inicio_fase_1 do config.json.
    """
    fuso_brt = timezone(timedelta(hours=-3))
    fases = sorted(
        [m for m in milestones if m.get("due_on")],
        key=lambda m: m["due_on"]
    )
    janelas: dict[str, tuple[datetime, datetime]] = {}
    fim_anterior = None
    for m in fases:
        dia = para_datetime(m["due_on"]).date()
        fim = datetime(dia.year, dia.month, dia.day, 23, 59, 59, tzinfo=fuso_brt)
        inicio = fim_anterior or inicio_projeto
        janelas[m["title"]] = (inicio, fim)
        fim_anterior = fim
    return janelas


def fase_da_data(data: datetime, janelas: dict[str, tuple[datetime, datetime]]) -> str:
    """Fase cuja janela contem a data. Datas apos a ultima fase ficam na ultima."""
    for fase, (_, fim) in janelas.items():
        if data <= fim:
            return fase
    return list(janelas)[-1] if janelas else "Sem Fase"


ORDINAIS_FASE = {"primeira": 1, "segunda": 2, "terceira": 3, "quarta": 4}


def fases_citadas(texto: str) -> set[int]:
    """Fases citadas em um texto: F3, Fase 3, Fase3, Fase 03, fase-03 ou Terceira Fase."""
    if not texto:
        return set()
    citadas = {int(n) for n in re.findall(r"\bf(?:ase)?[\s_-]*0?([1-4])(?!\d)", texto, flags=re.IGNORECASE)}
    for ordinal, n in ORDINAIS_FASE.items():
        if re.search(rf"\b{ordinal}\s+fase\b", texto, flags=re.IGNORECASE):
            citadas.add(n)
    return citadas


def fase_do_pr(item: dict, fase_por_issue: dict[int, str], janelas: dict) -> tuple[str, str]:
    """
    Fase de um PR e a origem dela, na ordem: milestone da issue ligada (prefixo
    [X-N] no titulo ou Closes/Fixes/Resolves #N no corpo), fase citada uma unica
    vez no titulo ou no corpo, e por fim a data de abertura.
    """
    titulo = item.get("title") or ""
    corpo = item.get("body") or ""
    ligadas = [int(n) for n in re.findall(r"^\s*\[[A-Za-z0-9]+-(\d+)[\]}]", titulo)]
    ligadas += [int(n) for n in re.findall(
        r"\b(?:close[sd]?|fix(?:e[sd])?|resolve[sd]?)\b\s*:?\s*#(\d+)", corpo, flags=re.IGNORECASE
    )]
    for n in ligadas:
        if fase_por_issue.get(n) in janelas:
            return fase_por_issue[n], f"issue #{n}"

    for origem, texto in (("titulo", titulo), ("corpo", corpo)):
        citadas = fases_citadas(texto)
        if len(citadas) == 1 and f"Fase {next(iter(citadas))}" in janelas:
            return f"Fase {next(iter(citadas))}", origem
        if len(citadas) > 1:
            break

    return fase_da_data(para_datetime(item["created_at"]), janelas), "data"


def interpretar_prazo(prazo_str: str, ano_ref: int) -> datetime | None:
    """Converte uma string 'DD/MM' ou 'DD/MM/AAAA' para objeto datetime (final do dia UTC)."""
    if not prazo_str:
        return None
    match = re.search(r"(\d{1,2})/(\d{1,2})(?:/(\d{2,4}))?", prazo_str)
    if not match:
        return None
    dia, mes = int(match.group(1)), int(match.group(2))
    ano = int(match.group(3)) if match.group(3) else ano_ref
    if ano < 100:
        ano += 2000
    try:
        return datetime(ano, mes, dia, 23, 59, 59, tzinfo=timezone.utc)
    except ValueError:
        return None


def acuracia_pct(issues: list) -> float:
    """Horas reais / horas estimadas das issues que tem os dois valores preenchidos."""
    avaliadas = [i for i in issues if i["estimativa_h"] > 0 and i["horas_reais_h"] > 0]
    soma_e = sum(i["estimativa_h"] for i in avaliadas)
    soma_r = sum(i["horas_reais_h"] for i in avaliadas)
    return round(soma_r / soma_e * 100.0, 1) if soma_e > 0 else 0.0


def classificar_estimativa(estimativa_h: float, horas_reais_h: float) -> tuple[float | None, str]:
    """Desvio da estimativa (%) e classificacao na faixa de -20% a +20% do Construct 2."""
    if estimativa_h <= 0 or horas_reais_h <= 0:
        return None, ""
    desvio = round((horas_reais_h - estimativa_h) / estimativa_h * 100.0, 1)
    if desvio > 20.0:
        return desvio, "subestimada"
    if desvio < -20.0:
        return desvio, "superestimada"
    return desvio, "na faixa"


def processar_dados(dados_brutos: dict, config: dict, avisos: list | None = None) -> dict:
    """
    Transforma os dados brutos da API nas estruturas das tres categorias PSM/CID:
    1. Recursos e Custos
    2. Calendario e Progresso
    3. Desempenho dos Processos
    """
    ano_ref = config.get("ano_referencia", 2026)
    valor_hora = float(config.get("valor_hora", 45.0))
    mapa_equipe = config.get("integrantes", {})

    issues_processadas = []
    prs_processados = []

    for item in dados_brutos.get("issues_e_prs", []):
        if "pull_request" in item:
            prs_processados.append(item)
            continue

        numero = item["number"]
        titulo = item["title"]
        estado = item["state"]
        fase = item.get("milestone", {}).get("title") if item.get("milestone") else "Sem Fase"
        assignees = [a["login"] for a in item.get("assignees", [])]
        labels = [l["name"] for l in item.get("labels", [])]
        corpo = item.get("body") or ""

        estimativa_str = extrair_secao_markdown(corpo, "Estimativa (h)")
        horas_reais_str = extrair_secao_markdown(corpo, "Horas reais (h)")
        prazo_str = extrair_secao_markdown(corpo, "Prazo")
        dependencias = extrair_dependencias(extrair_secao_markdown(corpo, "Depende de"), avisos, numero)

        estimativa_h = extrair_numero_float(estimativa_str, avisos, numero)
        horas_reais_h, horas_por_pessoa = extrair_horas_reais(
            horas_reais_str, assignees, avisos, numero, mapa_equipe
        )
        if estado == "closed" and horas_reais_h <= 0 and item.get("state_reason") != "not_planned":
            registrar_aviso(avisos, numero, "fechada sem horas reais", f"'{titulo}' fechada sem horas reais registradas")

        dt_criacao = datetime.fromisoformat(item["created_at"].replace("Z", "+00:00"))
        dt_fechamento = (
            datetime.fromisoformat(item["closed_at"].replace("Z", "+00:00"))
            if item.get("closed_at") else None
        )
        dt_prazo = interpretar_prazo(prazo_str, ano_ref)

        agora = datetime.now(timezone.utc)
        if estado == "closed":
            if dt_prazo and dt_fechamento and dt_fechamento > dt_prazo:
                status_prazo = "Concluida em atraso"
            else:
                status_prazo = "Concluida no prazo"
        else:
            if dt_prazo and agora > dt_prazo:
                status_prazo = "Aberta em atraso"
            else:
                status_prazo = "Em andamento (no prazo)"

        desvio_estimativa, classe_estimativa = classificar_estimativa(estimativa_h, horas_reais_h)

        lead_time_dias = (
            round((dt_fechamento - dt_criacao).total_seconds() / 86400.0, 2)
            if dt_fechamento else None
        )

        issues_processadas.append({
            "numero": numero,
            "titulo": titulo,
            "fase": fase,
            "estado": estado,
            "assignees": assignees,
            "labels": labels,
            "estimativa_h": estimativa_h,
            "estimativa_preenchida": estimativa_h > 0,
            "horas_reais_h": horas_reais_h,
            "horas_por_pessoa": horas_por_pessoa,
            "custo_estimado": round(estimativa_h * valor_hora, 2),
            "custo_real": round(horas_reais_h * valor_hora, 2),
            "prazo_str": prazo_str or "N/A",
            "data_fechamento": dt_fechamento.strftime("%d/%m/%Y") if dt_fechamento else "-",
            "status_prazo": status_prazo,
            "lead_time_dias": lead_time_dias,
            "desvio_estimativa_pct": desvio_estimativa,
            "classificacao_estimativa": classe_estimativa,
            "dt_criacao": dt_criacao,
            "dt_fechamento": dt_fechamento,
            "dt_prazo": dt_prazo,
            "dependencias": dependencias
        })

    fases_ordem = ["Fase 1", "Fase 2", "Fase 3", "Fase 4"]
    fases_encontradas = sorted(
        list({i["fase"] for i in issues_processadas}),
        key=lambda x: fases_ordem.index(x) if x in fases_ordem else 99
    )

    resumo_fases = []
    for fase in fases_encontradas:
        lista = [i for i in issues_processadas if i["fase"] == fase]
        total_issues = len(lista)
        concluidas = sum(1 for i in lista if i["estado"] == "closed")
        abertas = total_issues - concluidas

        no_prazo = sum(1 for i in lista if i["status_prazo"] in ("Concluida no prazo", "Em andamento (no prazo)"))
        em_atraso = total_issues - no_prazo

        h_est = round(sum(i["estimativa_h"] for i in lista), 2)
        h_real = round(sum(i["horas_reais_h"] for i in lista), 2)
        custo_est = round(h_est * valor_hora, 2)
        custo_real = round(h_real * valor_hora, 2)

        acuracia_fase = acuracia_pct(lista)
        com_estimativa = sum(1 for i in lista if i["estimativa_preenchida"])
        taxa_governanca_pct = round((com_estimativa / total_issues) * 100.0, 1) if total_issues > 0 else 0.0

        tempos = [i["lead_time_dias"] for i in lista if i["lead_time_dias"] is not None]
        lead_time_medio = round(sum(tempos) / len(tempos), 2) if tempos else 0.0

        resumo_fases.append({
            "fase": fase,
            "total_issues": total_issues,
            "issues_concluidas": concluidas,
            "issues_abertas": abertas,
            "progresso_pct": round((concluidas / total_issues) * 100.0, 1) if total_issues > 0 else 0.0,
            "issues_no_prazo": no_prazo,
            "issues_em_atraso": em_atraso,
            "aderencia_prazo_pct": round((no_prazo / total_issues) * 100.0, 1) if total_issues > 0 else 0.0,
            "horas_estimadas": h_est,
            "horas_reais": h_real,
            "custo_estimado_brl": custo_est,
            "custo_real_brl": custo_real,
            "acuracia_estimativa_pct": acuracia_fase,
            "taxa_preenchimento_estimativa_pct": taxa_governanca_pct,
            "lead_time_medio_dias": lead_time_medio
        })

    commits_por_login: dict[str, int] = {login: 0 for login in mapa_equipe}
    email_para_login = {
        "wanjo.christopher@gmail.com": "wChrstphr",
        "105730846+wChrstphr@users.noreply.github.com": "wChrstphr",
        "zafirosafira@gmail.com": "DaviPierre",
        "73446334+DaviPierre@users.noreply.github.com": "DaviPierre",
        "gabrielmonteiro1203@gmail.com": "GabrielSMonteiro",
        "100171830+GabrielSMonteiro@users.noreply.github.com": "GabrielSMonteiro",
        "leticia.cs1948@gmail.com": "LeticiaSantosss",
        "luizhenriquesoares18@hotmail.com": "luizh-gsoares",
        "duda.red35@gmail.com": "eduarda-ogomes",
        "162516978+eduarda-ogomes@users.noreply.github.com": "eduarda-ogomes"
    }

    for c in dados_brutos.get("commits", []):
        autor_gh = (c.get("author") or {}).get("login")
        if autor_gh in commits_por_login:
            commits_por_login[autor_gh] += 1
        else:
            commit_info = c.get("commit", {}).get("author", {})
            email = commit_info.get("email")
            nome = commit_info.get("name")
            login_resolvido = email_para_login.get(email)
            if not login_resolvido and nome:
                for log, n in mapa_equipe.items():
                    if n.lower() in nome.lower() or nome.lower() in n.lower():
                        login_resolvido = log
                        break
            if login_resolvido in commits_por_login:
                commits_por_login[login_resolvido] += 1

    prs_por_login: dict[str, int] = {login: 0 for login in mapa_equipe}
    for pr in prs_processados:
        autor_pr = (pr.get("user") or {}).get("login")
        if autor_pr in prs_por_login:
            prs_por_login[autor_pr] += 1

    contribuicao = []
    for login, nome in mapa_equipe.items():
        issues_atribuidas = [i for i in issues_processadas if login in i["assignees"]]
        qtd_issues = len(issues_atribuidas)

        h_est_pessoa = 0.0
        h_real_pessoa = 0.0
        for i in issues_processadas:
            if login in i["assignees"] and len(i["assignees"]) > 0:
                h_est_pessoa += i["estimativa_h"] / len(i["assignees"])
            if login in i["horas_por_pessoa"]:
                h_real_pessoa += i["horas_por_pessoa"][login]

        h_est_pessoa = round(h_est_pessoa, 2)
        h_real_pessoa = round(h_real_pessoa, 2)

        contribuicao.append({
            "login": login,
            "integrante": nome,
            "issues_atribuidas": qtd_issues,
            "horas_estimadas": h_est_pessoa,
            "horas_reais": h_real_pessoa,
            "custo_real_brl": round(h_real_pessoa * valor_hora, 2),
            "commits": commits_por_login.get(login, 0),
            "prs_abertos": prs_por_login.get(login, 0)
        })

    soma_horas_reais = sum(c["horas_reais"] for c in contribuicao)
    soma_issues = sum(c["issues_atribuidas"] for c in contribuicao)

    for c in contribuicao:
        if soma_horas_reais > 0:
            c["percentual_esforco"] = round((c["horas_reais"] / soma_horas_reais) * 100.0, 2)
            c["base_calculo_pct"] = "Horas Reais"
        elif soma_issues > 0:
            c["percentual_esforco"] = round((c["issues_atribuidas"] / soma_issues) * 100.0, 2)
            c["base_calculo_pct"] = "Issues Atribuidas (Linha de Base)"
        else:
            c["percentual_esforco"] = round(100.0 / len(contribuicao), 2)
            c["base_calculo_pct"] = "Distribuicao Igualitaria"

    # Contribuicao individual separada por fase (base: horas reais registradas nas issues da fase)
    contribuicao_por_fase = []
    for fase in fases_encontradas:
        linhas_fase = []
        for login, nome in mapa_equipe.items():
            qtd = 0
            h_est_p = 0.0
            h_real_p = 0.0
            for i in issues_processadas:
                if i["fase"] != fase:
                    continue
                if login in i["assignees"]:
                    qtd += 1
                    h_est_p += i["estimativa_h"] / len(i["assignees"])
                if login in i["horas_por_pessoa"]:
                    h_real_p += i["horas_por_pessoa"][login]
            linhas_fase.append({
                "fase": fase,
                "login": login,
                "integrante": nome,
                "issues_atribuidas": qtd,
                "horas_estimadas": round(h_est_p, 2),
                "horas_reais": round(h_real_p, 2),
                "custo_real_brl": round(h_real_p * valor_hora, 2),
            })
        soma_fase = sum(l["horas_reais"] for l in linhas_fase)
        for l in linhas_fase:
            l["percentual_esforco"] = round((l["horas_reais"] / soma_fase) * 100.0, 2) if soma_fase > 0 else 0.0
        contribuicao_por_fase.extend(linhas_fase)

    # Consolidado por Entrega: Entrega 1 (F1 + F2) e Entrega 2 (F3 + F4)
    mapa_entregas = [
        ("Entrega 1", ["Fase 1", "Fase 2"]),
        ("Entrega 2", ["Fase 3", "Fase 4"]),
    ]
    resumo_entregas = []
    for nome_entrega, fases_ent in mapa_entregas:
        lista_ent = [i for i in issues_processadas if i["fase"] in fases_ent]
        tot = len(lista_ent)
        conc = sum(1 for i in lista_ent if i["estado"] == "closed")
        abert = tot - conc
        nprazo = sum(1 for i in lista_ent if i["status_prazo"] in ("Concluida no prazo", "Em andamento (no prazo)"))
        atraso = tot - nprazo
        h_est = round(sum(i["estimativa_h"] for i in lista_ent), 2)
        h_real = round(sum(i["horas_reais_h"] for i in lista_ent), 2)
        c_est = round(h_est * valor_hora, 2)
        c_real = round(h_real * valor_hora, 2)
        acuracia = acuracia_pct(lista_ent)
        com_est = sum(1 for i in lista_ent if i["estimativa_preenchida"])
        tx_gov = round((com_est / tot) * 100.0, 1) if tot > 0 else 0.0
        tempos = [i["lead_time_dias"] for i in lista_ent if i["lead_time_dias"] is not None]
        lt_medio = round(sum(tempos) / len(tempos), 2) if tempos else 0.0

        resumo_entregas.append({
            "entrega": nome_entrega,
            "fases": " + ".join(fases_ent),
            "total_issues": tot,
            "issues_concluidas": conc,
            "issues_abertas": abert,
            "progresso_pct": round((conc / tot) * 100.0, 1) if tot > 0 else 0.0,
            "issues_no_prazo": nprazo,
            "issues_em_atraso": atraso,
            "aderencia_prazo_pct": round((nprazo / tot) * 100.0, 1) if tot > 0 else 0.0,
            "horas_estimadas": h_est,
            "horas_reais": h_real,
            "custo_estimado_brl": c_est,
            "custo_real_brl": c_real,
            "acuracia_estimativa_pct": acuracia,
            "taxa_preenchimento_estimativa_pct": tx_gov,
            "lead_time_medio_dias": lt_medio
        })

    # Contribuicao individual por entrega
    contribuicao_por_entrega = []
    for nome_entrega, (fase_a, fase_b) in [("Entrega 1", ("Fase 1", "Fase 2")), ("Entrega 2", ("Fase 3", "Fase 4"))]:
        linhas_ent = []
        for login, nome in mapa_equipe.items():
            issues_fa = [i for i in issues_processadas if i["fase"] == fase_a and login in i["assignees"]]
            issues_fb = [i for i in issues_processadas if i["fase"] == fase_b and login in i["assignees"]]

            h_est_fa = sum(i["estimativa_h"] / len(i["assignees"]) for i in issues_fa)
            h_est_fb = sum(i["estimativa_h"] / len(i["assignees"]) for i in issues_fb)

            h_real_fa = sum(i["horas_por_pessoa"].get(login, 0.0) for i in issues_processadas if i["fase"] == fase_a)
            h_real_fb = sum(i["horas_por_pessoa"].get(login, 0.0) for i in issues_processadas if i["fase"] == fase_b)

            h_est_tot = round(h_est_fa + h_est_fb, 2)
            h_real_tot = round(h_real_fa + h_real_fb, 2)

            linhas_ent.append({
                "entrega": nome_entrega,
                "integrante": nome,
                "login": login,
                "issues_fase_a": len(issues_fa),
                "issues_fase_b": len(issues_fb),
                "issues_atribuidas": len(issues_fa) + len(issues_fb),
                "horas_estimadas": h_est_tot,
                "horas_reais_fase_a": round(h_real_fa, 2),
                "horas_reais_fase_b": round(h_real_fb, 2),
                "horas_reais": h_real_tot,
                "custo_real_brl": round(h_real_tot * valor_hora, 2)
            })
        soma_ent = sum(l["horas_reais"] for l in linhas_ent)
        for l in linhas_ent:
            l["percentual_esforco"] = round((l["horas_reais"] / soma_ent) * 100.0, 2) if soma_ent > 0 else 0.0
        contribuicao_por_entrega.extend(linhas_ent)

    return {
        "issues": sorted(issues_processadas, key=lambda x: x["numero"]),
        "resumo_fases": resumo_fases,
        "resumo_entregas": resumo_entregas,
        "contribuicao": contribuicao,
        "contribuicao_por_fase": contribuicao_por_fase,
        "contribuicao_por_entrega": contribuicao_por_entrega,
        "total_prs": len(prs_processados),
        "total_commits": len(dados_brutos.get("commits", []))
    }


def _pct(parte: float, total: float) -> float:
    return round(parte / total * 100.0, 1) if total > 0 else 0.0


def _media(valores: list[float]) -> float | None:
    return round(sum(valores) / len(valores), 2) if valores else None


def _mediana(valores: list[float]) -> float | None:
    if not valores:
        return None
    ordenados = sorted(valores)
    meio = len(ordenados) // 2
    if len(ordenados) % 2:
        return round(ordenados[meio], 2)
    return round((ordenados[meio - 1] + ordenados[meio]) / 2, 2)


def _data_br(data: datetime | None) -> str:
    return data.astimezone(timezone(timedelta(hours=-3))).strftime("%d/%m/%Y %H:%M") if data else "-"


def calcular_ritmo_fechamento(issues: list, janelas: dict, agora: datetime) -> list[dict]:
    """
    Construct 1 (Calendario e Progresso): distribuicao do fechamento das issues
    ao longo da fase, fechamento na primeira metade e issues bloqueadas por
    dependencias ainda abertas.
    """
    abertas = {i["numero"] for i in issues if i["estado"] == "open"}
    linhas = []
    for fase, (inicio, fim) in janelas.items():
        lista = [i for i in issues if i["fase"] == fase]
        if not lista:
            continue
        meio = inicio + (fim - inicio) / 2
        fechadas = [i for i in lista if i["dt_fechamento"]]
        ate_metade = [i for i in fechadas if i["dt_fechamento"] <= meio]
        ultimos_2_dias = [i for i in fechadas if fim - timedelta(days=2) < i["dt_fechamento"] <= fim]
        apos_fim = [i for i in fechadas if i["dt_fechamento"] > fim]
        no_prazo = [i for i in fechadas if i["dt_prazo"] and i["dt_fechamento"] <= i["dt_prazo"]]
        bloqueadas = [
            i["numero"] for i in lista
            if i["estado"] == "open" and any(d in abertas for d in i["dependencias"] if d != i["numero"])
        ]
        taxa_metade = _pct(len(ate_metade), len(lista))
        linhas.append({
            "fase": fase,
            "inicio": _data_br(inicio),
            "data_media": _data_br(meio),
            "fim": _data_br(fim),
            "total_issues": len(lista),
            "issues_fechadas": len(fechadas),
            "progresso_pct": _pct(len(fechadas), len(lista)),
            "fechadas_ate_data_media": len(ate_metade),
            "taxa_fechamento_1a_metade_pct": taxa_metade,
            "fechadas_ultimos_2_dias": len(ultimos_2_dias),
            "fechadas_apos_fim": len(apos_fim),
            "fechadas_no_prazo_pct": _pct(len(no_prazo), len(lista)),
            "issues_bloqueadas": len(bloqueadas),
            "issues_bloqueadas_lista": " ".join(f"#{n}" for n in bloqueadas),
            "alerta_ritmo": "sim" if agora >= meio and taxa_metade < 50.0 else "nao"
        })
    return linhas


def calcular_acerto_estimativas(issues: list) -> list[dict]:
    """
    Construct 2 (Recursos e Custos): quantas issues de cada fase ficaram na
    faixa de -20% a +20% de desvio, sobre as issues com estimativa e horas reais.
    O desvio e a classificacao de cada issue ficam em 05_detalhamento_issues.csv.
    """
    avaliadas = [i for i in issues if i["classificacao_estimativa"]]
    por_fase = []
    for fase in sorted({i["fase"] for i in avaliadas}):
        lista = [i for i in avaliadas if i["fase"] == fase]
        acuracia = acuracia_pct(lista)
        na_faixa = sum(1 for i in lista if i["classificacao_estimativa"] == "na faixa")
        por_fase.append({
            "fase": fase,
            "issues_avaliadas": len(lista),
            "desvio_fase_pct": round(acuracia - 100.0, 1),
            "issues_na_faixa": na_faixa,
            "issues_na_faixa_pct": _pct(na_faixa, len(lista)),
            "issues_subestimadas": sum(1 for i in lista if i["classificacao_estimativa"] == "subestimada"),
            "issues_superestimadas": sum(1 for i in lista if i["classificacao_estimativa"] == "superestimada"),
            "desvio_mediano_pct": _mediana([i["desvio_estimativa_pct"] for i in lista])
        })
    return por_fase


def _percentil(valores: list[float], p: float) -> float | None:
    """Percentil pelo metodo do posto mais proximo."""
    if not valores:
        return None
    ordenados = sorted(valores)
    return round(ordenados[max(math.ceil(p / 100.0 * len(ordenados)) - 1, 0)], 2)


def calcular_revisao_prs(dados_brutos: dict, issues: list, janelas: dict, agora: datetime, avisos: list | None) -> dict:
    """
    Construct 3 (Desempenho dos Processos): tempo de espera de cada PR ate a
    primeira revisao de outro integrante, aprovacao formal e quem revisou.
    """
    revisoes_prs = dados_brutos.get("revisoes_prs")
    if revisoes_prs is None:
        registrar_aviso(avisos, None, "sem revisoes", "snapshot sem revisoes de PR, rode a coleta online")
        return {"prs": [], "fases": [], "revisores": [], "matriz": []}

    fase_por_issue = {i["numero"]: i["fase"] for i in issues}
    prs = []
    for item in dados_brutos.get("issues_e_prs", []):
        if "pull_request" not in item:
            continue
        autor = (item.get("user") or {}).get("login")
        if autor and autor.endswith("[bot]"):
            continue
        criado = para_datetime(item["created_at"])
        merged = para_datetime((item.get("pull_request") or {}).get("merged_at"))
        revisoes = [
            r for r in revisoes_prs.get(str(item["number"]), [])
            if r["revisor"] and r["revisor"] != autor and not r["revisor"].endswith("[bot]")
            and r["estado"] != "PENDING" and r["enviada_em"]
        ]
        primeira = min((para_datetime(r["enviada_em"]) for r in revisoes), default=None)
        aprovacao = min((para_datetime(r["enviada_em"]) for r in revisoes if r["estado"] == "APPROVED"), default=None)
        revisores = sorted({r["revisor"] for r in revisoes})
        if merged:
            situacao = "integrado"
        elif item["state"] == "open":
            situacao = "aberto"
        else:
            situacao = "fechado sem merge"

        espera_h = round((primeira - criado).total_seconds() / 3600.0, 2) if primeira else None
        if situacao == "aberto" and not primeira:
            parado_h = (agora - criado).total_seconds() / 3600.0
            if parado_h > 24:
                registrar_aviso(
                    avisos, item["number"], "PR travado",
                    f"PR aberto ha {parado_h:.0f}h sem revisao (limite do plano: 24h)"
                )

        fase, origem_fase = fase_do_pr(item, fase_por_issue, janelas)
        prs.append({
            "numero": item["number"],
            "titulo": item["title"],
            "fase": fase,
            "origem_fase": origem_fase,
            "autor": autor,
            "situacao": situacao,
            "criado_em": _data_br(criado),
            "primeira_revisao_em": _data_br(primeira),
            "aprovado_em": _data_br(aprovacao),
            "integrado_em": _data_br(merged),
            "espera_revisao_h": espera_h,
            "aprovado_formalmente": "sim" if aprovacao else "nao",
            "revisores": ", ".join(revisores),
            "_revisores": revisores
        })

    fases, revisores_fase, matriz = [], [], []
    for fase in list(janelas) + ["Total"]:
        lista = [p for p in prs if fase == "Total" or p["fase"] == fase]
        if not lista:
            continue
        integrados = [p for p in lista if p["situacao"] == "integrado"]
        aprovados = [p for p in integrados if p["aprovado_formalmente"] == "sim"]
        esperas = [p["espera_revisao_h"] for p in lista if p["espera_revisao_h"] is not None]
        media_h = _media(esperas)
        fases.append({
            "fase": fase,
            "prs": len(lista),
            "prs_integrados": len(integrados),
            "prs_integrados_com_aprovacao": len(aprovados),
            "taxa_revisao_formal_pct": _pct(len(aprovados), len(integrados)),
            "prs_com_revisao": len(esperas),
            "prs_sem_revisao": len(lista) - len(esperas),
            "espera_media_h": media_h,
            "espera_media_dias": round(media_h / 24.0, 2) if media_h is not None else None,
            "espera_mediana_h": _mediana(esperas),
            "espera_p80_h": _percentil(esperas, 80),
            "espera_p90_h": _percentil(esperas, 90),
            "prs_espera_acima_24h": sum(1 for e in esperas if e > 24)
        })

        contagem: dict[str, int] = {}
        pares: dict[tuple[str, str], int] = {}
        for p in lista:
            for r in p["_revisores"]:
                contagem[r] = contagem.get(r, 0) + 1
                pares[(p["autor"], r)] = pares.get((p["autor"], r), 0) + 1
        total_rev = sum(contagem.values())
        for r, n in sorted(contagem.items(), key=lambda x: -x[1]):
            revisores_fase.append({"fase": fase, "revisor": r, "prs_revisados": n, "percentual": _pct(n, total_rev)})
        for (a, r), n in sorted(pares.items()):
            matriz.append({"fase": fase, "autor": a, "revisor": r, "prs": n})

    return {"prs": prs, "fases": fases, "revisores": revisores_fase, "matriz": matriz}


def calcular_medidas_plano(resultado: dict, dados_brutos: dict, config: dict, avisos: list | None) -> dict:
    """Calcula as tres medidas do plano de medicao (docs/gestao/plano-medicao-psm.md)."""
    agora = datetime.now(timezone.utc)
    if config.get("inicio_fase_1"):
        inicio_projeto = datetime.fromisoformat(config["inicio_fase_1"]).replace(tzinfo=timezone(timedelta(hours=-3)))
    else:
        inicio_projeto = min(para_datetime(i["created_at"]) for i in dados_brutos.get("issues_e_prs", []))
    janelas = janelas_das_fases(dados_brutos.get("milestones", []), inicio_projeto)
    return {
        "ritmo_fechamento": calcular_ritmo_fechamento(resultado["issues"], janelas, agora),
        "acerto_fases": calcular_acerto_estimativas(resultado["issues"]),
        "revisao": calcular_revisao_prs(dados_brutos, resultado["issues"], janelas, agora, avisos)
    }


def salvar_csv(caminho: Path, colunas: list[str], linhas: list[dict]) -> None:
    """Salva uma lista de dicionarios em arquivo CSV UTF-8."""
    caminho.parent.mkdir(parents=True, exist_ok=True)
    with open(caminho, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=colunas, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(linhas)
    print(f"[CSV] Gerado: {caminho}")


def _desenhar_grafico_barras_agrupadas_pil(
    caminho: Path,
    titulo: str,
    subtitulo: str,
    eixo_y_label: str,
    categorias: list[str],
    serie1: list[float],
    label1: str,
    cor1: str,
    serie2: list[float],
    label2: str,
    cor2: str
) -> None:
    """
    Renderiza um grafico de barras agrupadas em alta resolucao (supersampling 2x)
    com cabecalho, subtitulo e barra de legenda separada sem sobreposicao.
    """
    from PIL import Image, ImageDraw, ImageFont

    escala = 2
    largura_img, altura_img = 1000 * escala, 600 * escala
    img = Image.new("RGB", (largura_img, altura_img), "#ffffff")
    draw = ImageDraw.Draw(img)

    try:
        f_titulo = ImageFont.truetype("/usr/share/fonts/truetype/inter-zorin-os/Inter-Bold.ttf", 20 * escala)
        f_sub = ImageFont.truetype("/usr/share/fonts/truetype/inter-zorin-os/Inter-Medium.ttf", 13 * escala)
        f_legenda = ImageFont.truetype("/usr/share/fonts/truetype/inter-zorin-os/Inter-Bold.ttf", 13 * escala)
        f_eixo = ImageFont.truetype("/usr/share/fonts/truetype/inter-zorin-os/Inter-Medium.ttf", 13 * escala)
        f_val = ImageFont.truetype("/usr/share/fonts/truetype/inter-zorin-os/Inter-Bold.ttf", 13 * escala)
    except Exception:
        try:
            f_titulo = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20 * escala)
            f_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 13 * escala)
            f_legenda = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 13 * escala)
            f_eixo = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 13 * escala)
            f_val = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 13 * escala)
        except Exception:
            f_titulo = f_sub = f_legenda = f_eixo = f_val = ImageFont.load_default()

    # Moldura externa sutil no padrao de card do Pages (borda #e5e7eb, raio 6px * escala)
    draw.rounded_rectangle(
        [10 * escala, 10 * escala, largura_img - 10 * escala, altura_img - 10 * escala],
        radius=6 * escala,
        outline="#e5e7eb",
        width=2 * escala
    )

    # 1. Cabecalho (Titulo e Subtitulo no padrao tipografico Inter do Pages)
    draw.text((60 * escala, 28 * escala), titulo, fill="#111827", font=f_titulo)
    draw.text((60 * escala, 58 * escala), f"{subtitulo}  |  Unidade: {eixo_y_label}", fill="#4b5563", font=f_sub)

    # 2. Faixa de Legenda abaixo do subtitulo
    ly = 90 * escala
    lx1 = 60 * escala
    draw.rounded_rectangle([lx1, ly, lx1 + 18 * escala, ly + 18 * escala], radius=4 * escala, fill=cor1)
    draw.text((lx1 + 26 * escala, ly + 1 * escala), label1, fill="#111827", font=f_legenda)

    bbox1 = draw.textbbox((0, 0), label1, font=f_legenda)
    largura_lbl1 = bbox1[2] - bbox1[0]
    lx2 = lx1 + 26 * escala + largura_lbl1 + 40 * escala
    draw.rounded_rectangle([lx2, ly, lx2 + 18 * escala, ly + 18 * escala], radius=4 * escala, fill=cor2)
    draw.text((lx2 + 26 * escala, ly + 1 * escala), label2, fill="#111827", font=f_legenda)

    # 3. Area de plotagem
    x0, y0 = 95 * escala, 140 * escala
    x1, y1 = largura_img - 55 * escala, altura_img - 75 * escala

    max_bruto = max(max(serie1, default=0), max(serie2, default=0))
    if max_bruto >= 4:
        import math
        max_val = float(math.ceil((max_bruto * 1.2) / 5.0) * 5)
    else:
        max_val = 4.0

    # Grade horizontal e rotulos Y no padrao do Pages
    num_linhas = 5
    for idx in range(num_linhas + 1):
        val_linha = (max_val / num_linhas) * idx
        py = y1 - ((y1 - y0) * (val_linha / max_val))
        cor_linha = "#e5e7eb" if idx == 0 else "#f3f4f6"
        esp_linha = 2 * escala if idx == 0 else 1 * escala
        draw.line([(x0, py), (x1, py)], fill=cor_linha, width=esp_linha)

        txt_g = f"{val_linha:.0f}" if max_val >= 8 else f"{val_linha:.1f}"
        bbox_g = draw.textbbox((0, 0), txt_g, font=f_eixo)
        w_g = bbox_g[2] - bbox_g[0]
        draw.text((x0 - w_g - 14 * escala, py - 8 * escala), txt_g, fill="#4b5563", font=f_eixo)

    # 4. Barras por categoria
    n_cat = max(len(categorias), 1)
    largura_bloco = (x1 - x0) / n_cat
    largura_barra = min(largura_bloco * 0.28, 68 * escala)
    gap = 5 * escala

    for i, cat in enumerate(categorias):
        centro_x = x0 + (i + 0.5) * largura_bloco

        # Barra 1
        v1 = serie1[i]
        h1 = ((y1 - y0) * (v1 / max_val)) if max_val > 0 else 0
        bx1_ini = centro_x - largura_barra - gap
        bx1_fim = centro_x - gap
        by1_ini = y1 - max(h1, 3 * escala)
        draw.rounded_rectangle([bx1_ini, by1_ini, bx1_fim, y1], radius=4 * escala, fill=cor1)
        txt1 = f"{v1:.0f}" if float(v1).is_integer() else f"{v1:.1f}"
        bbox_v1 = draw.textbbox((0, 0), txt1, font=f_val)
        w_v1 = bbox_v1[2] - bbox_v1[0]
        draw.text(((bx1_ini + bx1_fim - w_v1) / 2, by1_ini - 22 * escala), txt1, fill="#111827", font=f_val)

        # Barra 2
        v2 = serie2[i]
        h2 = ((y1 - y0) * (v2 / max_val)) if max_val > 0 else 0
        bx2_ini = centro_x + gap
        bx2_fim = centro_x + largura_barra + gap
        by2_ini = y1 - max(h2, 3 * escala)
        draw.rounded_rectangle([bx2_ini, by2_ini, bx2_fim, y1], radius=4 * escala, fill=cor2)
        txt2 = f"{v2:.0f}" if float(v2).is_integer() else f"{v2:.1f}"
        bbox_v2 = draw.textbbox((0, 0), txt2, font=f_val)
        w_v2 = bbox_v2[2] - bbox_v2[0]
        draw.text(((bx2_ini + bx2_fim - w_v2) / 2, by2_ini - 22 * escala), txt2, fill="#111827", font=f_val)

        # Rotulo centralizado no eixo X
        bbox_cat = draw.textbbox((0, 0), cat, font=f_eixo)
        w_cat = bbox_cat[2] - bbox_cat[0]
        draw.text((centro_x - w_cat / 2, y1 + 16 * escala), cat, fill="#111827", font=f_eixo)

    # Reduz com filtro LANCZOS para anti-aliasing nitido
    img_final = img.resize((1000, 600), Image.Resampling.LANCZOS)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    img_final.save(caminho, format="PNG", dpi=(300, 300))
    print(f"[PNG] Gerado: {caminho}")


def _fontes_pages(escala: int):
    """Carrega a tipografia Inter/DejaVu/Liberation com fallback seguro para default."""
    from PIL import ImageFont
    candidatos_bold = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
        "/usr/share/fonts/truetype/inter-zorin-os/Inter-Bold.ttf",
    ]
    candidatos_regular = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/usr/share/fonts/truetype/inter-zorin-os/Inter-Medium.ttf",
        "/usr/share/fonts/truetype/inter-zorin-os/Inter-Regular.ttf",
    ]
    f_bold_path = next((p for p in candidatos_bold if Path(p).is_file()), None)
    f_reg_path = next((p for p in candidatos_regular if Path(p).is_file()), None)
    if f_bold_path and f_reg_path:
        try:
            return (
                ImageFont.truetype(f_bold_path, 20 * escala),
                ImageFont.truetype(f_reg_path, 13 * escala),
                ImageFont.truetype(f_bold_path, 13 * escala),
            )
        except Exception:
            pass
    f = ImageFont.load_default()
    return f, f, f


def _desenhar_barras_horizontais_pil(
    caminho: Path,
    titulo: str,
    subtitulo: str,
    categorias: list[str],
    valores: list[float],
    rotulos: list[str],
    cor: str,
    legenda: str
) -> None:
    """Grafico de barras horizontais (participacao por integrante) no padrao visual do Pages."""
    from PIL import Image, ImageDraw

    escala = 2
    w, h = 1000 * escala, 600 * escala
    img = Image.new("RGB", (w, h), "#ffffff")
    draw = ImageDraw.Draw(img)
    f_titulo, f_txt, f_bold = _fontes_pages(escala)

    draw.rounded_rectangle([10 * escala, 10 * escala, w - 10 * escala, h - 10 * escala],
                           radius=6 * escala, outline="#e5e7eb", width=2 * escala)
    draw.text((60 * escala, 28 * escala), titulo, fill="#111827", font=f_titulo)
    draw.text((60 * escala, 58 * escala), subtitulo, fill="#4b5563", font=f_txt)
    draw.rounded_rectangle([60 * escala, 90 * escala, 78 * escala, 108 * escala], radius=4 * escala, fill=cor)
    draw.text((86 * escala, 91 * escala), legenda, fill="#111827", font=f_bold)

    x_lbl = 60 * escala
    x0 = 215 * escala
    x1 = w - 175 * escala
    topo = 140 * escala
    base_y = h - 50 * escala
    n = max(len(categorias), 1)
    passo = (base_y - topo) / n
    altura_barra = min(passo * 0.55, 40 * escala)

    max_val = max(max(valores, default=0.0), 1.0)
    max_val = float(((int(max_val * 1.15) // 20) + 1) * 20)

    # Grade vertical com escala percentual
    for k in range(0, 5):
        gx = x0 + (x1 - x0) * k / 4
        draw.line([(gx, topo - 6 * escala), (gx, base_y)], fill="#e5e7eb" if k == 0 else "#f3f4f6", width=escala)
        txt = f"{max_val * k / 4:.0f}%"
        bb = draw.textbbox((0, 0), txt, font=f_txt)
        draw.text((gx - (bb[2] - bb[0]) / 2, base_y + 8 * escala), txt, fill="#4b5563", font=f_txt)

    for i, cat in enumerate(categorias):
        cy = topo + passo * (i + 0.5)
        draw.text((x_lbl, cy - 9 * escala), cat, fill="#111827", font=f_txt)
        largura = (x1 - x0) * (valores[i] / max_val)
        largura = max(largura, 3 * escala)
        draw.rounded_rectangle([x0, cy - altura_barra / 2, x0 + largura, cy + altura_barra / 2],
                               radius=4 * escala, fill=cor)
        draw.text((x0 + largura + 10 * escala, cy - 9 * escala), rotulos[i], fill="#111827", font=f_bold)

    img_final = img.resize((1000, 600), Image.Resampling.LANCZOS)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    img_final.save(caminho, format="PNG", dpi=(300, 300))
    print(f"[PNG] Gerado: {caminho}")


def _desenhar_grafico_acuracia_pil(caminho: Path, titulo: str, subtitulo: str,
                                   fases: list[str], valores: list[float]) -> None:
    """Acuracia de estimativa por fase, com a faixa ideal (80% a 120%) destacada."""
    from PIL import Image, ImageDraw

    escala = 2
    w, h = 1000 * escala, 600 * escala
    img = Image.new("RGB", (w, h), "#ffffff")
    draw = ImageDraw.Draw(img)
    f_titulo, f_txt, f_bold = _fontes_pages(escala)

    draw.rounded_rectangle([10 * escala, 10 * escala, w - 10 * escala, h - 10 * escala],
                           radius=6 * escala, outline="#e5e7eb", width=2 * escala)
    draw.text((60 * escala, 28 * escala), titulo, fill="#111827", font=f_titulo)
    draw.text((60 * escala, 58 * escala), subtitulo, fill="#4b5563", font=f_txt)

    draw.rounded_rectangle([60 * escala, 90 * escala, 78 * escala, 108 * escala], radius=4 * escala, fill="#4f46e5")
    draw.text((86 * escala, 91 * escala), "Acurácia (horas reais / horas estimadas)", fill="#111827", font=f_bold)
    lx = 420 * escala
    draw.rounded_rectangle([lx, 90 * escala, lx + 18 * escala, 108 * escala], radius=4 * escala,
                           fill="#e0e7ff", outline="#818cf8", width=escala)
    draw.text((lx + 26 * escala, 91 * escala), "Faixa ideal (80% a 120%)", fill="#111827", font=f_bold)

    lx2 = 680 * escala
    draw.line([(lx2, 99 * escala), (lx2 + 24 * escala, 99 * escala)], fill="#818cf8", width=2 * escala)
    draw.text((lx2 + 32 * escala, 91 * escala), "100% = planejado", fill="#4338ca", font=f_bold)

    x0, y0 = 95 * escala, 140 * escala
    x1, y1 = w - 55 * escala, h - 75 * escala
    max_val = max(160.0, float(((int(max(valores, default=0) * 1.15) // 20) + 1) * 20))

    def py(v: float) -> float:
        return y1 - (y1 - y0) * (v / max_val)

    draw.rectangle([x0, py(120), x1, py(80)], fill="#e0e7ff")
    for k in range(0, int(max_val // 20) + 1):
        v = k * 20
        draw.line([(x0, py(v)), (x1, py(v))], fill="#e5e7eb" if v == 0 else "#f3f4f6",
                  width=(2 if v == 0 else 1) * escala)
        txt = f"{v}%"
        bb = draw.textbbox((0, 0), txt, font=f_txt)
        draw.text((x0 - (bb[2] - bb[0]) - 14 * escala, py(v) - 8 * escala), txt, fill="#4b5563", font=f_txt)
    draw.line([(x0, py(100)), (x1, py(100))], fill="#818cf8", width=2 * escala)
    if len(fases) == 1:
        draw.text((x1 - 150 * escala, py(100) - 22 * escala), "100% = planejado", fill="#4338ca", font=f_txt)

    n = max(len(fases), 1)
    bloco = (x1 - x0) / n
    larg = min(bloco * 0.3, 90 * escala)
    for i, fase in enumerate(fases):
        cx = x0 + (i + 0.5) * bloco
        topo = py(valores[i])
        draw.rounded_rectangle([cx - larg / 2, topo, cx + larg / 2, y1], radius=4 * escala, fill="#4f46e5")
        txt = f"{valores[i]:.1f}%"
        bb = draw.textbbox((0, 0), txt, font=f_bold)
        draw.text((cx - (bb[2] - bb[0]) / 2, topo - 24 * escala), txt, fill="#111827", font=f_bold)
        bb = draw.textbbox((0, 0), fase, font=f_txt)
        draw.text((cx - (bb[2] - bb[0]) / 2, y1 + 16 * escala), fase, fill="#111827", font=f_txt)

    img_final = img.resize((1000, 600), Image.Resampling.LANCZOS)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    img_final.save(caminho, format="PNG", dpi=(300, 300))
    print(f"[PNG] Gerado: {caminho}")


def gerar_graficos_por_fase(resultado: dict, dir_graficos: Path) -> None:
    """Graficos separados por fase (horas por integrante, participacao) e acuracia de estimativa."""
    por_fase = resultado.get("contribuicao_por_fase", [])
    fases = [r["fase"] for r in resultado["resumo_fases"]]

    for fase in fases:
        if fase not in ("Fase 1", "Fase 2", "Fase 3", "Fase 4"):
            continue
        num = fase.split()[-1]
        linhas = [l for l in por_fase if l["fase"] == fase]
        if not linhas:
            continue
        nomes = [l["integrante"].split()[0] for l in linhas]
        _desenhar_grafico_barras_agrupadas_pil(
            caminho=dir_graficos / f"04_horas_integrante_fase_{num}.png",
            titulo=f"PSM/CID — {fase}: Horas Estimadas vs. Reais por Integrante",
            subtitulo=f"Esforço de cada integrante nas issues da {fase} (horas rateadas quando compartilhadas)",
            eixo_y_label="Horas (h)",
            categorias=nomes,
            serie1=[l["horas_estimadas"] for l in linhas],
            label1="Horas Estimadas",
            cor1="#818cf8",
            serie2=[l["horas_reais"] for l in linhas],
            label2="Horas Reais",
            cor2="#4f46e5"
        )
        _desenhar_barras_horizontais_pil(
            caminho=dir_graficos / f"05_esforco_integrante_fase_{num}.png",
            titulo=f"PSM/CID — {fase}: Participação no Esforço Real",
            subtitulo=f"Percentual das horas reais da {fase} por integrante (soma = 100%)",
            categorias=[l["integrante"] for l in linhas],
            valores=[l["percentual_esforco"] for l in linhas],
            rotulos=[f"{l['percentual_esforco']:.1f}%  ({l['horas_reais']:.1f} h)" for l in linhas],
            cor="#4f46e5",
            legenda=f"% das horas reais da {fase}"
        )

        # Situacao das issues da fase (conclusao e prazo)
        issues_fase = [i for i in resultado["issues"] if i["fase"] == fase]
        total = max(len(issues_fase), 1)
        categorias_status = [
            ("Concluídas no prazo", "Concluida no prazo"),
            ("Concluídas com atraso", "Concluida em atraso"),
            ("Abertas no prazo", "Em andamento (no prazo)"),
            ("Abertas em atraso", "Aberta em atraso"),
        ]
        contagens = [sum(1 for i in issues_fase if i["status_prazo"] == chave) for _, chave in categorias_status]
        _desenhar_barras_horizontais_pil(
            caminho=dir_graficos / f"07_status_issues_fase_{num}.png",
            titulo=f"PSM/CID — {fase}: Situação e Prazo das Issues",
            subtitulo=f"Distribuição das {len(issues_fase)} issues da {fase} por conclusão e cumprimento do prazo",
            categorias=[nome_cat for nome_cat, _ in categorias_status],
            valores=[c / total * 100.0 for c in contagens],
            rotulos=[f"{c} issue(s)  ({c / total * 100.0:.1f}%)" for c in contagens],
            cor="#4f46e5",
            legenda=f"% das issues da {fase}"
        )

        resumo = next((r for r in resultado["resumo_fases"] if r["fase"] == fase), None)
        if resumo:
            _desenhar_grafico_acuracia_pil(
                caminho=dir_graficos / f"06_acuracia_estimativa_fase_{num}.png",
                titulo=f"PSM/CID — {fase}: Acurácia da Estimativa",
                subtitulo="Horas reais em relação às estimadas; 100% significa que o planejado foi exatamente cumprido",
                fases=[fase],
                valores=[resumo["acuracia_estimativa_pct"]]
            )

    _desenhar_grafico_acuracia_pil(
        caminho=dir_graficos / "06_acuracia_estimativa_fases.png",
        titulo="PSM/CID — Desempenho dos Processos: Acurácia da Estimativa",
        subtitulo="Horas reais em relação às estimadas por fase; 100% significa que o planejado foi exatamente cumprido",
        fases=fases,
        valores=[r["acuracia_estimativa_pct"] for r in resultado["resumo_fases"]]
    )


def gerar_grafico_entrega_1(resultado: dict, dir_graficos: Path) -> None:
    """Gera o grafico de barras horizontais de participacao no esforco real da Entrega 1."""
    linhas_e1 = [l for l in resultado.get("contribuicao_por_entrega", []) if l["entrega"] == "Entrega 1"]
    if not linhas_e1:
        return
    _desenhar_barras_horizontais_pil(
        caminho=dir_graficos / "05_esforco_integrante_entrega_1.png",
        titulo="PSM/CID: Participação no Esforço Real da Entrega 1",
        subtitulo="Percentual do esforço consolidado (Fase 1 + Fase 2) por integrante (soma = 100%)",
        categorias=[l["integrante"] for l in linhas_e1],
        valores=[l["percentual_esforco"] for l in linhas_e1],
        rotulos=[f"{l['percentual_esforco']:.1f}%  ({l['horas_reais']:.1f} h)" for l in linhas_e1],
        cor="#4f46e5",
        legenda="% das horas reais da Entrega 1"
    )


def gerar_graficos(resultado: dict, dir_graficos: Path) -> None:
    """
    Gera os 3 graficos PNG das categorias PSM/CID em dados/gestao/graficos/
    utilizando a paleta de cores padrao do Pages (--ifm-color-primary: #4f46e5 e #818cf8).
    """
    dir_graficos.mkdir(parents=True, exist_ok=True)
    fases = [r["fase"] for r in resultado["resumo_fases"]]
    h_est = [r["horas_estimadas"] for r in resultado["resumo_fases"]]
    h_real = [r["horas_reais"] for r in resultado["resumo_fases"]]
    concluidas = [r["issues_concluidas"] for r in resultado["resumo_fases"]]
    abertas = [r["issues_abertas"] for r in resultado["resumo_fases"]]

    nomes = [c["integrante"].split()[0] for c in resultado["contribuicao"]]
    issues_atrib = [c["issues_atribuidas"] for c in resultado["contribuicao"]]
    commits_ind = [c["commits"] for c in resultado["contribuicao"]]

    # Paleta oficial do Pages (src/css/custom.css):
    # Indigo principal: #4f46e5 (--ifm-color-primary)
    # Indigo destaque claro: #818cf8 (--ifm-color-primary-lighter)
    _desenhar_grafico_barras_agrupadas_pil(
        caminho=dir_graficos / "01_recursos_e_custos_fases.png",
        titulo="PSM/CID — Recursos e Custos: Esforço Planejado vs. Real",
        subtitulo="Comparativo de horas estimadas na abertura e horas reais registradas por fase",
        eixo_y_label="Horas (h)",
        categorias=fases,
        serie1=h_est,
        label1="Horas Estimadas (Planejado)",
        cor1="#818cf8",
        serie2=h_real,
        label2="Horas Reais (Executado)",
        cor2="#4f46e5"
    )

    _desenhar_grafico_barras_agrupadas_pil(
        caminho=dir_graficos / "02_calendario_e_progresso_fases.png",
        titulo="PSM/CID — Calendário e Progresso: Status das Issues por Fase",
        subtitulo="Acompanhamento de tarefas concluídas (closed) e em andamento (open) nas milestones",
        eixo_y_label="Quantidade de Issues",
        categorias=fases,
        serie1=concluidas,
        label1="Issues Concluídas",
        cor1="#4f46e5",
        serie2=abertas,
        label2="Issues em Andamento",
        cor2="#818cf8"
    )

    _desenhar_grafico_barras_agrupadas_pil(
        caminho=dir_graficos / "03_contribuicao_individual.png",
        titulo="PSM/CID — Distribuição de Tarefas e Commits por Integrante",
        subtitulo="Volume de issues atribuídas (incluindo compartilhadas) e commits registrados no repositório",
        eixo_y_label="Quantidade",
        categorias=nomes,
        serie1=issues_atrib,
        label1="Issues Atribuídas",
        cor1="#4f46e5",
        serie2=commits_ind,
        label2="Commits Registrados",
        cor2="#818cf8"
    )


def _tabela_md(colunas: list[tuple[str, str]], linhas: list[dict]) -> list[str]:
    saida = [
        "| " + " | ".join(titulo for titulo, _ in colunas) + " |",
        "| :--- |" + " :---: |" * (len(colunas) - 1)
    ]
    for l in linhas:
        valores = ["-" if l.get(chave) in (None, "") else str(l.get(chave)) for _, chave in colunas]
        saida.append("| " + " | ".join(valores) + " |")
    return saida


def secao_medidas_plano(medidas: dict) -> list[str]:
    """Tabelas Markdown das tres medidas do plano de medicao e avisos da coleta."""
    linhas = ["", "---", "", "## 4. Medidas do Plano de Medicao", "", "### Ritmo de fechamento das issues", ""]
    linhas += _tabela_md([
        ("Fase", "fase"), ("Inicio", "inicio"), ("Data media", "data_media"), ("Fim", "fim"),
        ("Fechadas / Total", "_fechadas"), ("Fechadas ate a data media (%)", "taxa_fechamento_1a_metade_pct"),
        ("Fechadas nos 2 ultimos dias", "fechadas_ultimos_2_dias"), ("Fechadas apos o fim", "fechadas_apos_fim"),
        ("Fechadas no prazo (%)", "fechadas_no_prazo_pct"), ("Bloqueadas", "issues_bloqueadas_lista"),
        ("Alerta de ritmo", "alerta_ritmo")
    ], [dict(r, _fechadas=f"{r['issues_fechadas']} / {r['total_issues']}") for r in medidas["ritmo_fechamento"]])

    linhas += ["", "### Acerto das estimativas por issue", "",
               "Desvio = (horas reais - horas estimadas) / horas estimadas. Na faixa = desvio entre -20% e +20%. "
               "O desvio de cada issue esta em `05_detalhamento_issues.csv`.", ""]
    linhas += _tabela_md([
        ("Fase", "fase"), ("Issues avaliadas", "issues_avaliadas"), ("Desvio da fase (%)", "desvio_fase_pct"),
        ("Desvio mediano (%)", "desvio_mediano_pct"), ("Na faixa (%)", "issues_na_faixa_pct"),
        ("Subestimadas", "issues_subestimadas"), ("Superestimadas", "issues_superestimadas")
    ], medidas["acerto_fases"])

    revisao = medidas["revisao"]
    linhas += ["", "### Tempo de espera dos PRs por revisao", "",
               "Horas corridas entre a abertura do PR e a primeira revisao de outra pessoa.", ""]
    linhas += _tabela_md([
        ("Fase", "fase"), ("PRs", "prs"), ("Integrados", "prs_integrados"),
        ("Integrados com aprovacao", "prs_integrados_com_aprovacao"), ("Revisao formal (%)", "taxa_revisao_formal_pct"),
        ("Sem revisao", "prs_sem_revisao"), ("Media (h)", "espera_media_h"), ("Mediana (h)", "espera_mediana_h"),
        ("P80 (h)", "espera_p80_h"), ("P90 (h)", "espera_p90_h"), ("Acima de 24h", "prs_espera_acima_24h")
    ], revisao["fases"])
    linhas += ["", "### Quem revisou", ""]
    linhas += _tabela_md([("Fase", "fase"), ("Revisor", "revisor"), ("PRs revisados", "prs_revisados"),
                          ("Participacao (%)", "percentual")], revisao["revisores"])
    linhas += ["", "### Autor por revisor", ""]
    linhas += _tabela_md([("Fase", "fase"), ("Autor", "autor"), ("Revisor", "revisor"), ("PRs", "prs")],
                         revisao["matriz"])
    linhas += ["", "### PRs", ""]
    linhas += _tabela_md([
        ("PR", "_pr"), ("Fase", "fase"), ("Origem da fase", "origem_fase"), ("Autor", "autor"),
        ("Situacao", "situacao"), ("Aberto em", "criado_em"), ("Primeira revisao", "primeira_revisao_em"),
        ("Espera (h)", "espera_revisao_h"), ("Aprovado", "aprovado_formalmente"), ("Revisores", "revisores")
    ], [dict(p, _pr=f"#{p['numero']}") for p in revisao["prs"]])

    linhas += ["", "### Avisos da coleta", ""]
    if medidas.get("avisos"):
        linhas += _tabela_md([("Tipo", "tipo"), ("Issue/PR", "_ref"), ("Mensagem", "mensagem")],
                             [dict(a, _ref=f"#{a['issue']}" if a["issue"] != "" else "") for a in medidas["avisos"]])
    else:
        linhas.append("Nenhum aviso.")
    linhas.append("")
    return linhas


def gerar_relatorio_constructs(resultado: dict, config: dict, caminho_md: Path, medidas: dict | None = None) -> None:
    """
    Gera um arquivo Markdown com os 3 Measurement Constructs estruturados,
    tabelas Markdown prontas para o GitPage (#20 e #31) e a tabela LaTeX
    de contribuicao individual para o artigo SBC (#27).
    """
    valor_hora = config["valor_hora"]
    fonte = config["fonte_valor_hora"]

    linhas = [
        "# Indicadores PSM/CID e Measurement Constructs",
        "",
        f"- **Valor-hora de referencia:** R$ {valor_hora:.2f}",
        f"- **Fonte do valor-hora:** {fonte}",
        "",
        "---",
        "",
        "## 1. Measurement Constructs (Padrao PSM/CID)",
        "",
        "### Construct 1 — Recursos e Custos: Esforco e Custo do Projeto",
        "",
        "| Elemento do Construct | Especificacao |",
        "| :--- | :--- |",
        "| **Categoria de Informacao** | Recursos e Custos (*Resources and Cost*) |",
        "| **Necessidade de Informacao** | Avaliar se o esforco empregado pela equipe e o custo financeiro estimado permanecem dentro do planejado e se a carga de trabalho esta equilibrada entre os integrantes. |",
        "| **Conceito Mensuravel** | Esforco de desenvolvimento, custo financeiro equivalente e distribuicao individual de trabalho. |",
        "| **Medidas Base** | 1. `Horas Estimadas (h)`: valor registrado na abertura de cada issue.<br>2. `Horas Reais (h)`: valor apurado no fechamento da issue por integrante.<br>3. `Valor-Hora (R$)`: taxa horaria de referencia configurada em `scripts/config.json`. |",
        "| **Medidas Derivadas** | • $\\text{Custo Planejado (R\\$)} = \\sum \\text{Horas Estimadas} \\times \\text{Valor-Hora}$<br>• $\\text{Custo Real (R\\$)} = \\sum \\text{Horas Reais} \\times \\text{Valor-Hora}$<br>• $\\text{Contribuicao Individual (\\%)} = (\\text{Esforco do Integrante} / \\text{Esforco Total da Equipe}) \\times 100$ |",
        "| **Indicador e Criterio de Decisao** | Comparacao entre horas planejadas e reais por fase e percentual individual. Desvios superiores a 25% entre planejado e realizado ou desequilibrio acentuado entre membros exigem redistribuicao de tarefas na fase seguinte. |",
        "",
        "### Construct 2 — Calendario e Progresso: Taxa de Conclusao e Aderencia a Prazos",
        "",
        "| Elemento do Construct | Especificacao |",
        "| :--- | :--- |",
        "| **Categoria de Informacao** | Calendario e Progresso (*Schedule and Progress*) |",
        "| **Necessidade de Informacao** | Monitorar o ritmo de entrega dos artefatos de cada fase (milestone) e identificar atrasos em relacao aos prazos internos antes da submissao oficial. |",
        "| **Conceito Mensuravel** | Progresso de conclusao de marcos (*Milestone Completion*) e pontualidade das entregas. |",
        "| **Medidas Base** | 1. `Total de Issues da Fase`: contagem de tarefas vinculadas a milestone.<br>2. `Issues Concluidas`: contagem de tarefas com estado `closed`.<br>3. `Data Limite (Prazo)` vs. `Data de Fechamento (closed_at)`. |",
        "| **Medidas Derivadas** | • $\\text{Progresso da Fase (\\%)} = (\\text{Issues Concluidas} / \\text{Total de Issues}) \\times 100$<br>• $\\text{Aderencia ao Prazo (\\%)} = (\\text{Issues no Prazo} / \\text{Total de Issues}) \\times 100$ |",
        "| **Indicador e Criterio de Decisao** | Percentual de conclusao e entregas no prazo. Caso a aderencia ao prazo fique abaixo de 80%, a equipe deve antecipar revisoes de PR e desmembrar tarefas complexas. |",
        "",
        "### Construct 3 — Desempenho dos Processos: Acuracia de Estimativa e Tempo de Ciclo",
        "",
        "| Elemento do Construct | Especificacao |",
        "| :--- | :--- |",
        "| **Categoria de Informacao** | Desempenho dos Processos (*Process Performance*) |",
        "| **Necessidade de Informacao** | Verificar a maturidade do processo de planejamento da equipe (qualidade das estimativas) e a agilidade do fluxo de revisao e fechamento de tarefas. |",
        "| **Conceito Mensuravel** | Acuracia de estimativa (*Estimation Accuracy*), governanca de preenchimento e *Lead Time* de resolucao. |",
        "| **Medidas Base** | 1. `Data de Criacao (created_at)` e `Data de Fechamento (closed_at)` das issues.<br>2. `Horas Estimadas` e `Horas Reais` por tarefa. |",
        "| **Medidas Derivadas** | • $\\text{Acuracia de Estimativa (\\%)} = (\\text{Horas Reais} / \\text{Horas Estimadas}) \\times 100$<br>• $\\text{Lead Time Medio (dias)} = \\frac{1}{N} \\sum (\\text{closed\\_at} - \\text{created\\_at})$<br>• $\\text{Taxa de Governanca (\\%)} = (\\text{Issues com Estimativa Preenchida} / \\text{Total de Issues}) \\times 100$ |",
        "| **Indicador e Criterio de Decisao** | Acuracia ideal entre 80% e 120%. Valores fora dessa faixa indicam subestimacao ou superestimacao sistematica, orientando o ajuste das estimativas nas fases posteriores. |",
        "",
        "---",
        "",
        "## 2. Resumo Consolidado por Fase (Tabelas para #20 e #31)",
        "",
        "| Fase | Issues (Total / Concluidas) | Progresso (%) | Aderencia ao Prazo (%) | Horas Estimadas (h) | Horas Reais (h) | Custo Estimado (R$) | Custo Real (R$) | Acuracia Estimativa (%) | Lead Time Medio (dias) |",
        "| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |"
    ]

    for r in resultado["resumo_fases"]:
        linhas.append(
            f"| {r['fase']} | {r['total_issues']} / {r['issues_concluidas']} | "
            f"{r['progresso_pct']:.1f}% | {r['aderencia_prazo_pct']:.1f}% | "
            f"{r['horas_estimadas']:.1f} | {r['horas_reais']:.1f} | "
            f"R$ {r['custo_estimado_brl']:.2f} | R$ {r['custo_real_brl']:.2f} | "
            f"{r['acuracia_estimativa_pct']:.1f}% | {r['lead_time_medio_dias']:.2f} |"
        )

    linhas.extend([
        "",
        "---",
        "",
        "## 3. Tabela de Contribuicao Individual (Markdown e LaTeX para #27)",
        "",
        "| Integrante | GitHub | Issues Atribuidas | Horas Estimadas (h) | Horas Reais (h) | Custo Equivalente (R$) | Commits | PRs | Contribuicao (%) |",
        "| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |"
    ])

    for c in resultado["contribuicao"]:
        linhas.append(
            f"| {c['integrante']} | `@{c['login']}` | {c['issues_atribuidas']} | "
            f"{c['horas_estimadas']:.1f} | {c['horas_reais']:.1f} | "
            f"R$ {c['custo_real_brl']:.2f} | {c['commits']} | {c['prs_abertos']} | "
            f"**{c['percentual_esforco']:.2f}%** |"
        )

    linhas.extend([
        "",
        "### Codigo LaTeX para o Apendice do Artigo (#27)",
        "",
        "```latex",
        "\\begin{table}[ht]",
        "\\centering",
        "\\caption{Tabela de contribuicao individual da equipe (Entrega 1)}",
        "\\label{tab:contribuicao}",
        "\\begin{tabular}{lccccr}",
        "\\hline",
        "\\textbf{Integrante} & \\textbf{Issues} & \\textbf{Horas Est.} & \\textbf{Horas Reais} & \\textbf{Commits/PRs} & \\textbf{Esfor\\c{c}o (\\%)} \\\\",
        "\\hline"
    ])

    for c in resultado["contribuicao"]:
        linhas.append(
            f"{c['integrante']} & {c['issues_atribuidas']} & "
            f"{c['horas_estimadas']:.1f}h & {c['horas_reais']:.1f}h & "
            f"{c['commits']}/{c['prs_abertos']} & {c['percentual_esforco']:.2f}\\% \\\\"
        )

    linhas.extend([
        "\\hline",
        "\\textbf{Total} & "
        f"\\textbf{{{sum(c['issues_atribuidas'] for c in resultado['contribuicao'])}}} & "
        f"\\textbf{{{sum(c['horas_estimadas'] for c in resultado['contribuicao']):.1f}h}} & "
        f"\\textbf{{{sum(c['horas_reais'] for c in resultado['contribuicao']):.1f}h}} & "
        f"\\textbf{{{sum(c['commits'] for c in resultado['contribuicao'])}/{sum(c['prs_abertos'] for c in resultado['contribuicao'])}}} & "
        "\\textbf{100.00\\%} \\\\",
        "\\hline",
        "\\end{tabular}",
        "\\end{table}",
        "```",
        ""
    ])
    if medidas:
        linhas.extend(secao_medidas_plano(medidas))

    caminho_md.parent.mkdir(parents=True, exist_ok=True)
    with open(caminho_md, "w", encoding="utf-8") as f:
        f.write("\n".join(linhas))
    print(f"[MD]  Gerado: {caminho_md}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Coleta e calcula os indicadores PSM/CID do repositorio.")
    parser.add_argument(
        "--config",
        default="scripts/config.json",
        help="Caminho para o arquivo de configuracao JSON (padrao: scripts/config.json)"
    )
    parser.add_argument(
        "--token",
        default=os.environ.get("GITHUB_TOKEN"),
        help="Token do GitHub opcional (ou defina a variavel de ambiente GITHUB_TOKEN)"
    )
    parser.add_argument(
        "--offline",
        action="store_true",
        help="Usa o snapshot local em dados/gestao/raw_github_data.json sem consultar a rede"
    )
    args = parser.parse_args()

    raiz = Path(__file__).resolve().parent.parent
    caminho_config = raiz / args.config
    config = carregar_config(caminho_config)

    dir_saida = raiz / config.get("diretorio_saida", "dados/gestao")
    arquivo_raw = dir_saida / "raw_github_data.json"

    dados_brutos = coletar_dados_github(
        repo=config["repositorio"],
        token=args.token,
        arquivo_raw=arquivo_raw,
        usar_offline=args.offline
    )

    avisos: list[dict] = []
    resultado = processar_dados(dados_brutos, config, avisos)
    medidas = calcular_medidas_plano(resultado, dados_brutos, config, avisos)

    # 1. Salvar CSVs das 3 categorias + contribuicao individual + detalhamento
    salvar_csv(
        dir_saida / "01_recursos_e_custos_fases.csv",
        ["fase", "horas_estimadas", "horas_reais", "custo_estimado_brl", "custo_real_brl"],
        resultado["resumo_fases"]
    )
    salvar_csv(
        dir_saida / "02_calendario_e_progresso_fases.csv",
        ["fase", "total_issues", "issues_concluidas", "issues_abertas", "progresso_pct", "issues_no_prazo", "issues_em_atraso", "aderencia_prazo_pct"],
        resultado["resumo_fases"]
    )
    salvar_csv(
        dir_saida / "03_desempenho_processos_fases.csv",
        ["fase", "acuracia_estimativa_pct", "taxa_preenchimento_estimativa_pct", "lead_time_medio_dias"],
        resultado["resumo_fases"]
    )
    salvar_csv(
        dir_saida / "04_contribuicao_individual.csv",
        ["integrante", "login", "issues_atribuidas", "horas_estimadas", "horas_reais", "custo_real_brl", "commits", "prs_abertos", "percentual_esforco", "base_calculo_pct"],
        resultado["contribuicao"]
    )

    salvar_csv(
        dir_saida / "06_contribuicao_por_fase.csv",
        ["fase", "integrante", "login", "issues_atribuidas", "horas_estimadas", "horas_reais", "custo_real_brl", "percentual_esforco"],
        resultado["contribuicao_por_fase"]
    )

    salvar_csv(
        dir_saida / "07_resumo_entregas.csv",
        ["entrega", "fases", "total_issues", "issues_concluidas", "issues_abertas", "progresso_pct", "issues_no_prazo", "issues_em_atraso", "aderencia_prazo_pct", "horas_estimadas", "horas_reais", "custo_estimado_brl", "custo_real_brl", "acuracia_estimativa_pct", "taxa_preenchimento_estimativa_pct", "lead_time_medio_dias"],
        resultado["resumo_entregas"]
    )

    salvar_csv(
        dir_saida / "08_contribuicao_por_entrega.csv",
        ["entrega", "integrante", "login", "issues_fase_a", "issues_fase_b", "issues_atribuidas", "horas_estimadas", "horas_reais_fase_a", "horas_reais_fase_b", "horas_reais", "custo_real_brl", "percentual_esforco"],
        resultado["contribuicao_por_entrega"]
    )

    issues_csv = []
    for i in resultado["issues"]:
        copia = dict(i)
        copia["assignees"] = ", ".join(i["assignees"])
        copia["labels"] = ", ".join(i["labels"])
        issues_csv.append(copia)

    salvar_csv(
        dir_saida / "05_detalhamento_issues.csv",
        ["numero", "fase", "titulo", "estado", "assignees", "estimativa_h", "horas_reais_h", "desvio_estimativa_pct", "classificacao_estimativa", "custo_estimado", "custo_real", "prazo_str", "data_fechamento", "status_prazo", "lead_time_dias"],
        issues_csv
    )

    avisos.sort(key=lambda a: (a["tipo"], a["issue"] if isinstance(a["issue"], int) else 0))
    medidas["avisos"] = avisos

    # 2. Gerar graficos PNG
    gerar_graficos(resultado, dir_saida / "graficos")
    gerar_graficos_por_fase(resultado, dir_saida / "graficos")
    gerar_grafico_entrega_1(resultado, dir_saida / "graficos")

    # Gerar Curva S de desempenho de execucao (esforco planejado vs. realizado)
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from gerar_grafico_desempenho import gerar_grafico_desempenho
        gerar_grafico_desempenho(
            dir_saida / "05_detalhamento_issues.csv",
            [dir_saida / "graficos" / "08_desempenho_execucao_curva_s.png"]
        )
    except Exception as e:
        print(f"[AVISO] Nao foi possivel gerar a Curva S automaticamente: {e}")

    # Sincronizar PNGs gerados com static/img/gestao/
    dir_static = raiz / "static" / "img" / "gestao"
    if dir_static.exists():
        for png in (dir_saida / "graficos").glob("*.png"):
            shutil.copy2(png, dir_static / png.name)
        print(f"[SYNC] Graficos sincronizados com: {dir_static}")

    # 3. Gerar documento com Measurement Constructs e tabelas Markdown/LaTeX
    gerar_relatorio_constructs(resultado, config, dir_saida / "constructs_e_tabelas.md", medidas)

    if avisos:
        print(f"\n[AVISO] {len(avisos)} aviso(s) na leitura das issues e PRs:")
        for a in avisos:
            ref = f"#{a['issue']}" if a["issue"] != "" else "-"
            print(f"  [{a['tipo']}] {ref}: {a['mensagem']}")

    print("\n[SUCESSO] Coleta e processamento PSM/CID finalizados!")


if __name__ == "__main__":
    main()
