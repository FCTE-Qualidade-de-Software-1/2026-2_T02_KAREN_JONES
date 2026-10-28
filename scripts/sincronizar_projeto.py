#!/usr/bin/env python3
"""
Script para sincronizar estimativas e horas reais das issues com o GitHub Projects (v2).
Lê os campos Markdown gerados pelo template tarefa.yml e atualiza os campos numéricos
no quadro do GitHub Projects via API GraphQL.
"""

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request
from typing import Any, Optional


def executar_graphql(query: str, variables: dict[str, Any], token: str) -> dict[str, Any]:
    """Executa uma query ou mutation GraphQL na API do GitHub."""
    url = "https://api.github.com/graphql"
    payload = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": "GitHub-Project-Sync-QS1",
    }
    req = urllib.request.Request(url, data=payload, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if "errors" in data:
                print(f"[ERRO GraphQL] {data['errors']}", file=sys.stderr)
                return data
            return data
    except urllib.error.HTTPError as e:
        corpo = e.read().decode("utf-8")
        print(f"[ERRO HTTP {e.code}] {corpo}", file=sys.stderr)
        raise


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


def extrair_numero_float(texto: str) -> Optional[float]:
    """
    Extrai valor em horas de uma string, suportando formatos como:
    - '1h30m' ou '2h30' -> 1.5, 2.5
    - '20m' ou '30 min' -> 0.33, 0.5
    - '2.5' ou '2,5' ou '4' -> 2.5, 4.0
    """
    if not texto:
        return None
    texto_limpo = texto.strip().lower().replace(",", ".")
    match_hm = re.search(r"(\d+)\s*h(?:oras?)?\s*(\d+)", texto_limpo)
    if match_hm:
        horas = int(match_hm.group(1))
        minutos = int(match_hm.group(2))
        return round(horas + (minutos / 60.0), 2)
    match_m = re.search(r"(\d+)\s*(?:m|min|minutos)\b", texto_limpo)
    if match_m:
        minutos = int(match_m.group(1))
        return round(minutos / 60.0, 2)
    match = re.search(r"(\d+(?:\.\d+)?)", texto_limpo)
    return float(match.group(1)) if match else None


def extrair_horas_reais(texto: str) -> Optional[float]:
    """
    Extrai o total de horas reais de strings como:
    - '5 (@usuario1: 3, @usuario2: 2)' -> 5.0
    - '@usuario1: 3, @usuario2: 2' -> 5.0
    - '4' -> 4.0
    - '2h30' -> 2.5
    """
    if not texto:
        return None
    pares = re.findall(r"@([A-Za-z0-9_-]+)\s*:\s*([^,)\n]+)", texto)
    if pares:
        total = 0.0
        for _, h_str in pares:
            val = extrair_numero_float(h_str)
            if val is not None:
                total += val
        return round(total, 2)
    return extrair_numero_float(texto)


def buscar_dados_projeto(org: str, project_number: int, token: str) -> tuple[str, dict[str, dict[str, Any]]]:
    """Obtem o ID do projeto e o mapeamento de campos (nome normalizado -> dados do campo)."""
    query = """
    query($org: String!, $number: Int!) {
      organization(login: $org) {
        projectV2(number: $number) {
          id
          title
          fields(first: 50) {
            nodes {
              ... on ProjectV2Field {
                id
                name
                dataType
              }
              ... on ProjectV2SingleSelectField {
                id
                name
                dataType
              }
              ... on ProjectV2IterationField {
                id
                name
                dataType
              }
            }
          }
        }
      }
    }
    """
    resp = executar_graphql(query, {"org": org, "number": project_number}, token)
    proj = resp.get("data", {}).get("organization", {}).get("projectV2")
    if not proj:
        raise ValueError(f"Projeto #{project_number} nao encontrado na organizacao '{org}'. Verifique o token e o numero do projeto.")

    proj_id = proj["id"]
    campos: dict[str, dict[str, Any]] = {}
    for node in proj.get("fields", {}).get("nodes", []):
        if "name" in node:
            nome = node["name"].strip().lower()
            campos[nome] = node

    return proj_id, campos


def encontrar_campo_por_palavras_chave(campos: dict[str, dict[str, Any]], *palavras_chave: str) -> Optional[dict[str, Any]]:
    """Localiza um campo cujas palavras-chave estejam presentes em seu nome."""
    for nome, dados in campos.items():
        if all(kw.lower() in nome for kw in palavras_chave):
            return dados
    return None


def adicionar_ou_obter_item(project_id: str, content_id: str, token: str) -> Optional[str]:
    """Adiciona a issue ao projeto ou retorna o ID do item existente."""
    mutation = """
    mutation($projectId: ID!, $contentId: ID!) {
      addProjectV2ItemById(input: { projectId: $projectId, contentId: $contentId }) {
        item {
          id
        }
      }
    }
    """
    resp = executar_graphql(mutation, {"projectId": project_id, "contentId": content_id}, token)
    item = resp.get("data", {}).get("addProjectV2ItemById", {}).get("item")
    return item["id"] if item else None


def atualizar_campo_numero(project_id: str, item_id: str, field_id: str, valor: float, token: str) -> None:
    """Atualiza o valor de um campo do tipo Number no GitHub Projects."""
    mutation = """
    mutation($projectId: ID!, $itemId: ID!, $fieldId: ID!, $number: Float!) {
      updateProjectV2ItemFieldValue(input: {
        projectId: $projectId,
        itemId: $itemId,
        fieldId: $fieldId,
        value: { number: $number }
      }) {
        projectV2Item { id }
      }
    }
    """
    executar_graphql(mutation, {
        "projectId": project_id,
        "itemId": item_id,
        "fieldId": field_id,
        "number": valor
    }, token)


def atualizar_campo_texto(project_id: str, item_id: str, field_id: str, valor: str, token: str) -> None:
    """Atualiza o valor de um campo do tipo Text no GitHub Projects."""
    mutation = """
    mutation($projectId: ID!, $itemId: ID!, $fieldId: ID!, $text: String!) {
      updateProjectV2ItemFieldValue(input: {
        projectId: $projectId,
        itemId: $itemId,
        fieldId: $fieldId,
        value: { text: $text }
      }) {
        projectV2Item { id }
      }
    }
    """
    executar_graphql(mutation, {
        "projectId": project_id,
        "itemId": item_id,
        "fieldId": field_id,
        "text": valor
    }, token)


def processar_issue(
    issue_numero: int,
    issue_node_id: str,
    corpo: str,
    project_id: str,
    campo_estimativa: Optional[dict[str, Any]],
    campo_horas_reais: Optional[dict[str, Any]],
    campo_revisor: Optional[dict[str, Any]],
    token: str
) -> None:
    """Extrai os dados de uma issue e atualiza os campos correspondentes no projeto."""
    est_texto = extrair_secao_markdown(corpo, "Estimativa (h)")
    reais_texto = extrair_secao_markdown(corpo, "Horas reais (h)") or extrair_secao_markdown(corpo, "Horas reais")
    revisor_texto = extrair_secao_markdown(corpo, "Revisor")

    estimativa = extrair_numero_float(est_texto)
    horas_reais = extrair_horas_reais(reais_texto)

    print(f"\n[Issue #{issue_numero}]")
    print(f"  Estimativa: {estimativa} (extraido de: '{est_texto}')")
    print(f"  Horas Reais: {horas_reais} (extraido de: '{reais_texto}')")
    if revisor_texto:
        print(f"  Revisor: {revisor_texto}")

    item_id = adicionar_ou_obter_item(project_id, issue_node_id, token)
    if not item_id:
        print(f"  [AVISO] Nao foi possivel obter o item_id no projeto para a issue #{issue_numero}.")
        return

    if campo_estimativa and estimativa is not None:
        atualizar_campo_numero(project_id, item_id, campo_estimativa["id"], estimativa, token)
        print(f"  ✓ Campo '{campo_estimativa['name']}' atualizado para {estimativa}")

    if campo_horas_reais and horas_reais is not None:
        atualizar_campo_numero(project_id, item_id, campo_horas_reais["id"], horas_reais, token)
        print(f"  ✓ Campo '{campo_horas_reais['name']}' atualizado para {horas_reais}")

    if campo_revisor and revisor_texto:
        atualizar_campo_texto(project_id, item_id, campo_revisor["id"], revisor_texto, token)
        print(f"  ✓ Campo '{campo_revisor['name']}' atualizado para '{revisor_texto}'")


def listar_todas_issues_repo(org: str, repo: str, token: str) -> list[dict[str, Any]]:
    """Busca todas as issues (abertas e fechadas) do repositorio via REST API paginada."""
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "User-Agent": "GitHub-Project-Sync-QS1"
    }
    issues = []
    pagina = 1
    while True:
        url = f"https://api.github.com/repos/{org}/{repo}/issues?state=all&per_page=100&page={pagina}"
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            lote = json.loads(resp.read().decode("utf-8"))
            if not lote:
                break
            for item in lote:
                if "pull_request" not in item:
                    issues.append(item)
            if len(lote) < 100:
                break
            pagina += 1
    return issues


def main() -> None:
    parser = argparse.ArgumentParser(description="Sincroniza metricas de issues com o GitHub Projects.")
    parser.add_argument("--org", default="FCTE-Qualidade-de-Software-1", help="Nome da organizacao no GitHub")
    parser.add_argument("--repo", default="2026-2_T02_KAREN_JONES", help="Nome do repositorio")
    parser.add_argument("--project", type=int, default=36, help="Numero do projeto no GitHub Projects")
    parser.add_argument("--issue-node-id", help="Node ID da issue a sincronizar (GraphQL ID)")
    parser.add_argument("--issue-number", type=int, help="Numero da issue")
    parser.add_argument("--issue-body", help="Corpo da issue em Markdown")
    parser.add_argument("--all", action="store_true", help="Sincronizar todas as issues do repositorio (retroativo/backfill)")
    args = parser.parse_args()

    token = os.environ.get("PROJECT_TOKEN") or os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not token:
        print("[ERRO] Token do GitHub nao informado. Defina a variavel PROJECT_TOKEN.", file=sys.stderr)
        sys.exit(1)

    print(f"[INFO] Conectando ao GitHub Project #{args.project} da organizacao '{args.org}'...")
    project_id, campos = buscar_dados_projeto(args.org, args.project, token)
    print(f"[INFO] Projeto localizado com sucesso (ID: {project_id}).")
    print(f"[INFO] Campos disponiveis: {list(campos.keys())}")

    campo_estimativa = encontrar_campo_por_palavras_chave(campos, "estimativa")
    campo_horas_reais = encontrar_campo_por_palavras_chave(campos, "horas", "reais") or encontrar_campo_por_palavras_chave(campos, "horas")
    campo_revisor = encontrar_campo_por_palavras_chave(campos, "revisor")

    if campo_estimativa:
        print(f"[INFO] Mapeado campo de Estimativa: '{campo_estimativa['name']}' ({campo_estimativa['id']})")
    else:
        print("[AVISO] Campo de estimativa nao encontrado no projeto.")

    if campo_horas_reais:
        print(f"[INFO] Mapeado campo de Horas Reais: '{campo_horas_reais['name']}' ({campo_horas_reais['id']})")
    else:
        print("[AVISO] Campo de horas reais nao encontrado no projeto.")

    if args.all:
        print(f"\n[INFO] Modo retroativo ativado: coletando todas as issues de {args.org}/{args.repo}...")
        issues = listar_todas_issues_repo(args.org, args.repo, token)
        print(f"[INFO] Total de issues encontradas: {len(issues)}")
        for iss in issues:
            processar_issue(
                issue_numero=iss["number"],
                issue_node_id=iss["node_id"],
                corpo=iss.get("body", ""),
                project_id=project_id,
                campo_estimativa=campo_estimativa,
                campo_horas_reais=campo_horas_reais,
                campo_revisor=campo_revisor,
                token=token
            )
        print("\n[SUCESSO] Sincronizacao retroativa concluida!")
    elif args.issue_node_id:
        processar_issue(
            issue_numero=args.issue_number or 0,
            issue_node_id=args.issue_node_id,
            corpo=args.issue_body or "",
            project_id=project_id,
            campo_estimativa=campo_estimativa,
            campo_horas_reais=campo_horas_reais,
            campo_revisor=campo_revisor,
            token=token
        )
        print("\n[SUCESSO] Issue sincronizada com sucesso!")
    else:
        print("[ERRO] Informe --issue-node-id ou utilize --all para sincronizar todas.", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
