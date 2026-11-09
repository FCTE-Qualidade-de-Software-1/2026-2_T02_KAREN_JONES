#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Compara os elementos da cena de referência do Excalidraw com as cenas
reimportadas (a partir de .excalidraw, PNG com metadados ou SVG com metadados)
para a métrica M3.4.2 (Proporção de elementos preservados na exportação e reimportação).

Uso:
  python scripts/compara_elementos.py \\
    --original dados/fase-03/massa-de-dados/cena_referencia.excalidraw \\
    --reimportados \\
      dados/fase-04/brutos/reimport_excalidraw.excalidraw \\
      dados/fase-04/brutos/reimport_png.excalidraw \\
      dados/fase-04/brutos/reimport_svg.excalidraw
"""

import argparse
import csv
import json
import os
import sys


def carregar_elementos(caminho_arquivo: str) -> list:
    """Carrega a lista de elementos ativos de um arquivo .excalidraw."""
    if not os.path.exists(caminho_arquivo):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_arquivo}")

    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        dados = json.load(f)

    elementos = dados.get("elements", [])
    # Filtra apenas elementos não excluídos
    return [e for e in elementos if not e.get("isDeleted", False)]


def elementos_iguais(elem_orig: dict, elem_reimp: dict, tolerancia: float = 0.01) -> tuple:
    """
    Verifica se um elemento reimportado preservou as propriedades essenciais
    conforme o critério de M3.4.2:
    - tipo (type)
    - dimensões e posição (x, y, width, height)
    - estilo visual (strokeColor, backgroundColor, fillStyle, strokeWidth)
    - texto (text, se aplicável)
    """
    divergencias = []

    # 1. Tipo
    if elem_orig.get("type") != elem_reimp.get("type"):
        divergencias.append(f"tipo diferente ({elem_orig.get('type')} vs {elem_reimp.get('type')})")

    # 2. Coordenadas e dimensões
    for campo in ["x", "y", "width", "height"]:
        val_orig = elem_orig.get(campo, 0)
        val_reimp = elem_reimp.get(campo, 0)
        if abs(val_orig - val_reimp) > tolerancia:
            divergencias.append(f"{campo} divergente ({val_orig} vs {val_reimp})")

    # 3. Estilo visual
    for campo in ["strokeColor", "backgroundColor", "fillStyle", "strokeWidth"]:
        if elem_orig.get(campo) != elem_reimp.get(campo):
            divergencias.append(f"{campo} divergente ({elem_orig.get(campo)} vs {elem_reimp.get(campo)})")

    # 4. Texto (se for do tipo text)
    if elem_orig.get("type") == "text":
        if elem_orig.get("text") != elem_reimp.get("text"):
            divergencias.append("texto divergente")

    preservado = len(divergencias) == 0
    return preservado, divergencias


def comparar_cenas(elementos_orig: list, elementos_reimp: list) -> dict:
    """Compara os elementos da cena original contra a cena reimportada."""
    total_orig = len(elementos_orig)
    if total_orig == 0:
        return {
            "total_original": 0,
            "preservados": 0,
            "proporcao_preservacao": 0.0,
            "detalhes": [],
        }

    # Indexa elementos reimportados por id
    mapa_reimp = {e.get("id"): e for e in elementos_reimp if "id" in e}

    preservados = 0
    detalhes = []

    for elem_orig in elementos_orig:
        elem_id = elem_orig.get("id")
        elem_tipo = elem_orig.get("type")

        # Tenta buscar por ID
        elem_candidato = mapa_reimp.get(elem_id)

        # Se não achar por ID, tenta achar por tipo e posição aproximada
        if elem_candidato is None:
            for cand in elementos_reimp:
                if cand.get("type") == elem_tipo:
                    if abs(cand.get("x", 0) - elem_orig.get("x", 0)) < 1.0 and abs(
                        cand.get("y", 0) - elem_orig.get("y", 0)
                    ) < 1.0:
                        elem_candidato = cand
                        break

        if elem_candidato is None:
            detalhes.append({
                "id": elem_id,
                "tipo": elem_tipo,
                "preservado": False,
                "motivo": "Elemento não encontrado na cena reimportada",
            })
            continue

        preservado, divergencias = elementos_iguais(elem_orig, elem_candidato)
        if preservado:
            preservados += 1
            detalhes.append({"id": elem_id, "tipo": elem_tipo, "preservado": True, "motivo": "OK"})
        else:
            detalhes.append({
                "id": elem_id,
                "tipo": elem_tipo,
                "preservado": False,
                "motivo": "; ".join(divergencias),
            })

    proporcao = (preservados / total_orig) * 100.0
    return {
        "total_original": total_orig,
        "preservados": preservados,
        "proporcao_preservacao": round(proporcao, 2),
        "detalhes": detalhes,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Compara a preservação de elementos entre a cena de referência e reimportações (M3.4.2)"
    )
    parser.add_argument("--original", required=True, help="Caminho do arquivo da cena original (.excalidraw)")
    parser.add_argument(
        "--reimportados",
        nargs="+",
        required=True,
        help="Lista de arquivos reimportados (.excalidraw) para comparação",
    )
    parser.add_argument(
        "--output-json",
        default="dados/fase-04/brutos/M3.4.2_relatorio_preservacao.json",
        help="Caminho do relatório JSON detalhado de saída",
    )
    parser.add_argument(
        "--output-csv",
        default="dados/fase-04/brutos/M3.4.2_preservacao_formatos.csv",
        help="Caminho do resumo CSV de saída",
    )

    args = parser.parse_args()

    try:
        elementos_orig = carregar_elementos(args.original)
    except Exception as e:
        print(f"Erro ao carregar arquivo original ({args.original}): {e}", file=sys.stderr)
        sys.exit(1)

    print(f"Cena original carregada: {args.original} ({len(elementos_orig)} elementos ativos)")
    print("-" * 75)

    resultados = {}
    linhas_csv = []

    for arq_reimp in args.reimportados:
        nome_base = os.path.basename(arq_reimp)
        if not os.path.exists(arq_reimp):
            print(f"Aviso: arquivo reimportado não encontrado: {arq_reimp}")
            resultados[nome_base] = {"erro": "arquivo_nao_encontrado"}
            linhas_csv.append({
                "Arquivo": nome_base,
                "Elementos_Originais": len(elementos_orig),
                "Elementos_Preservados": 0,
                "Proporcao_Preservacao_Pct": 0.0,
                "Status": "Nao encontrado",
            })
            continue

        try:
            elementos_reimp = carregar_elementos(arq_reimp)
            res = comparar_cenas(elementos_orig, elementos_reimp)
            resultados[nome_base] = res

            pct = res["proporcao_preservacao"]
            print(f"Arquivo: {nome_base:<35} Preservados: {res['preservados']}/{res['total_original']} ({pct:.2f}%)")

            linhas_csv.append({
                "Arquivo": nome_base,
                "Elementos_Originais": res["total_original"],
                "Elementos_Preservados": res["preservados"],
                "Proporcao_Preservacao_Pct": pct,
                "Status": "Sucesso" if pct >= 95.0 else "Abaixo da meta",
            })
        except Exception as e:
            print(f"Erro ao processar {arq_reimp}: {e}", file=sys.stderr)
            resultados[nome_base] = {"erro": str(e)}

    # Salva relatório JSON se diretório puder ser criado
    dir_json = os.path.dirname(args.output_json)
    if dir_json:
        os.makedirs(dir_json, exist_ok=True)
    with open(args.output_json, "w", encoding="utf-8") as f:
        json.dump(resultados, f, indent=2, ensure_ascii=False)
    print(f"\nRelatório JSON salvo em: {args.output_json}")

    # Salva relatório CSV
    dir_csv = os.path.dirname(args.output_csv)
    if dir_csv:
        os.makedirs(dir_csv, exist_ok=True)
    with open(args.output_csv, "w", encoding="utf-8", newline="") as f:
        colunas = ["Arquivo", "Elementos_Originais", "Elementos_Preservados", "Proporcao_Preservacao_Pct", "Status"]
        writer = csv.DictWriter(f, fieldnames=colunas)
        writer.writeheader()
        writer.writerows(linhas_csv)
    print(f"Resumo CSV salvo em: {args.output_csv}")


if __name__ == "__main__":
    main()

