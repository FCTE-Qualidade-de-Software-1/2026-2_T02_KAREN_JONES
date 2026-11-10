#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera a massa de dados para a avaliação do Excalidraw (Fase 03):
- Cena de referência com os 10 tipos de elemento da Fase 02
- Cenas de escala com 100, 1.000, 5.000 e 10.000 elementos (40/20/20/20)
- 9 arquivos inválidos para o teste de tolerância a falhas (M2.3.1)

Uso:
  python scripts/gerar_massa_dados.py [--output-dir DIR] [--verificar]
"""

import argparse
import json
import os
import struct
import sys
import zlib


def criar_png_minimo(caminho_arquivo: str) -> None:
    """Gera um arquivo PNG válido mínimo (1x1 pixel branco) sem metadados Excalidraw."""
    assinatura = b"\x89PNG\r\n\x1a\n"
    # Chunk IHDR: 1x1, 8 bits/canal, Truecolor RGB (tipo 2)
    ihdr_dados = struct.pack(">IIBBBBB", 1, 1, 8, 2, 0, 0, 0)
    ihdr_crc = struct.pack(">I", zlib.crc32(b"IHDR" + ihdr_dados))
    ihdr = struct.pack(">I", len(ihdr_dados)) + b"IHDR" + ihdr_dados + ihdr_crc

    # Chunk IDAT: 1 linha com byte de filtro 0 seguido por R=255, G=255, B=255
    raw_pixels = b"\x00\xff\xff\xff"
    idat_dados = zlib.compress(raw_pixels)
    idat_crc = struct.pack(">I", zlib.crc32(b"IDAT" + idat_dados))
    idat = struct.pack(">I", len(idat_dados)) + b"IDAT" + idat_dados + idat_crc

    # Chunk IEND
    iend_crc = struct.pack(">I", zlib.crc32(b"IEND"))
    iend = struct.pack(">I", 0) + b"IEND" + iend_crc

    with open(caminho_arquivo, "wb") as f:
        f.write(assinatura + ihdr + idat + iend)


def gerar_cena_referencia(caminho_saida: str) -> dict:
    """
    Gera a cena de referência com os 10 tipos de elementos especificados na Fase 02:
    retângulo, elipse, losango, seta, linha, desenho livre, texto solto,
    texto dentro de forma, imagem e moldura (frame).
    """
    timestamp_base = 1730000000000

    elementos = [
        # 1. Moldura (frame) agrupando a cena
        {
            "id": "ref_frame_01",
            "type": "frame",
            "name": "Quadro 1",
            "x": 40,
            "y": 30,
            "width": 1100,
            "height": 680,
            "angle": 0,
            "strokeColor": "#868e96",
            "backgroundColor": "transparent",
            "fillStyle": "solid",
            "strokeWidth": 2,
            "strokeStyle": "dashed",
            "roughness": 0,
            "opacity": 100,
            "groupIds": [],
            "frameId": None,
            "roundness": None,
            "seed": 1001,
            "version": 1,
            "versionNonce": 2001,
            "isDeleted": False,
            "boundElements": None,
            "updated": timestamp_base,
            "link": None,
            "locked": False,
        },
        # 2. Texto solto
        {
            "id": "ref_text_solto_01",
            "type": "text",
            "x": 70,
            "y": 60,
            "width": 450,
            "height": 30,
            "angle": 0,
            "strokeColor": "#1e1e1e",
            "backgroundColor": "transparent",
            "fillStyle": "solid",
            "strokeWidth": 1,
            "strokeStyle": "solid",
            "roughness": 0,
            "opacity": 100,
            "groupIds": [],
            "frameId": "ref_frame_01",
            "roundness": None,
            "seed": 1002,
            "version": 1,
            "versionNonce": 2002,
            "isDeleted": False,
            "boundElements": None,
            "updated": timestamp_base,
            "link": None,
            "locked": False,
            "text": "Cena de referência",
            "originalText": "Cena de referência",
            "fontSize": 20,
            "fontFamily": 1,
            "textAlign": "left",
            "verticalAlign": "top",
            "lineHeight": 1.25,
            "autoResize": True,
            "containerId": None,
        },
        # 3. Retângulo (forma base para texto vinculado)
        {
            "id": "ref_rect_01",
            "type": "rectangle",
            "x": 70,
            "y": 120,
            "width": 200,
            "height": 110,
            "angle": 0,
            "strokeColor": "#1971c2",
            "backgroundColor": "#d0ebff",
            "fillStyle": "solid",
            "strokeWidth": 2,
            "strokeStyle": "solid",
            "roughness": 1,
            "opacity": 100,
            "groupIds": [],
            "frameId": "ref_frame_01",
            "roundness": {"type": 3},
            "seed": 1003,
            "version": 1,
            "versionNonce": 2003,
            "isDeleted": False,
            "boundElements": [{"type": "text", "id": "ref_bound_text_01"}],
            "updated": timestamp_base,
            "link": None,
            "locked": False,
        },
        # 4. Texto dentro de forma (bound text)
        {
            "id": "ref_bound_text_01",
            "type": "text",
            "x": 80,
            "y": 160,
            "width": 180,
            "height": 30,
            "angle": 0,
            "strokeColor": "#1864ab",
            "backgroundColor": "transparent",
            "fillStyle": "solid",
            "strokeWidth": 1,
            "strokeStyle": "solid",
            "roughness": 0,
            "opacity": 100,
            "groupIds": [],
            "frameId": "ref_frame_01",
            "roundness": None,
            "seed": 1004,
            "version": 1,
            "versionNonce": 2004,
            "isDeleted": False,
            "boundElements": None,
            "updated": timestamp_base,
            "link": None,
            "locked": False,
            "text": "Texto no retângulo",
            "originalText": "Texto no retângulo",
            "fontSize": 16,
            "fontFamily": 1,
            "textAlign": "center",
            "verticalAlign": "middle",
            "lineHeight": 1.2,
            "autoResize": True,
            "containerId": "ref_rect_01",
        },
        # 5. Elipse
        {
            "id": "ref_ellipse_01",
            "type": "ellipse",
            "x": 320,
            "y": 120,
            "width": 180,
            "height": 110,
            "angle": 0,
            "strokeColor": "#2b8a3e",
            "backgroundColor": "#d3f9d8",
            "fillStyle": "solid",
            "strokeWidth": 2,
            "strokeStyle": "solid",
            "roughness": 1,
            "opacity": 100,
            "groupIds": [],
            "frameId": "ref_frame_01",
            "roundness": None,
            "seed": 1005,
            "version": 1,
            "versionNonce": 2005,
            "isDeleted": False,
            "boundElements": None,
            "updated": timestamp_base,
            "link": None,
            "locked": False,
        },
        # 6. Losango (diamond)
        {
            "id": "ref_diamond_01",
            "type": "diamond",
            "x": 550,
            "y": 115,
            "width": 160,
            "height": 120,
            "angle": 0,
            "strokeColor": "#e67700",
            "backgroundColor": "#fff3bf",
            "fillStyle": "solid",
            "strokeWidth": 2,
            "strokeStyle": "solid",
            "roughness": 1,
            "opacity": 100,
            "groupIds": [],
            "frameId": "ref_frame_01",
            "roundness": None,
            "seed": 1006,
            "version": 1,
            "versionNonce": 2006,
            "isDeleted": False,
            "boundElements": None,
            "updated": timestamp_base,
            "link": None,
            "locked": False,
        },
        # 7. Seta com ponta
        {
            "id": "ref_arrow_01",
            "type": "arrow",
            "x": 760,
            "y": 175,
            "width": 180,
            "height": 0,
            "angle": 0,
            "strokeColor": "#c92a2a",
            "backgroundColor": "transparent",
            "fillStyle": "solid",
            "strokeWidth": 2,
            "strokeStyle": "solid",
            "roughness": 1,
            "opacity": 100,
            "groupIds": [],
            "frameId": "ref_frame_01",
            "roundness": None,
            "seed": 1007,
            "version": 1,
            "versionNonce": 2007,
            "isDeleted": False,
            "boundElements": None,
            "updated": timestamp_base,
            "link": None,
            "locked": False,
            "points": [[0, 0], [180, 0]],
            "startArrowhead": None,
            "endArrowhead": "arrow",
            "startBinding": None,
            "endBinding": None,
            "lastCommittedPoint": None,
        },
        # 8. Linha poligonal
        {
            "id": "ref_line_01",
            "type": "line",
            "x": 70,
            "y": 290,
            "width": 240,
            "height": 40,
            "angle": 0,
            "strokeColor": "#495057",
            "backgroundColor": "transparent",
            "fillStyle": "solid",
            "strokeWidth": 2,
            "strokeStyle": "dashed",
            "roughness": 1,
            "opacity": 100,
            "groupIds": [],
            "frameId": "ref_frame_01",
            "roundness": None,
            "seed": 1008,
            "version": 1,
            "versionNonce": 2008,
            "isDeleted": False,
            "boundElements": None,
            "updated": timestamp_base,
            "link": None,
            "locked": False,
            "points": [[0, 0], [120, 40], [240, 0]],
            "startArrowhead": None,
            "endArrowhead": None,
            "startBinding": None,
            "endBinding": None,
            "lastCommittedPoint": None,
        },
        # 9. Desenho livre (freedraw)
        {
            "id": "ref_freedraw_01",
            "type": "freedraw",
            "x": 360,
            "y": 290,
            "width": 160,
            "height": 60,
            "angle": 0,
            "strokeColor": "#5f3dc4",
            "backgroundColor": "transparent",
            "fillStyle": "solid",
            "strokeWidth": 2,
            "strokeStyle": "solid",
            "roughness": 1,
            "opacity": 100,
            "groupIds": [],
            "frameId": "ref_frame_01",
            "roundness": None,
            "seed": 1009,
            "version": 1,
            "versionNonce": 2009,
            "isDeleted": False,
            "boundElements": None,
            "updated": timestamp_base,
            "link": None,
            "locked": False,
            "points": [[0, 20], [40, 0], [80, 50], [120, 10], [160, 40]],
            "pressures": [0.5, 0.7, 0.8, 0.6, 0.4],
            "simulatePressure": True,
        },
        # 10. Imagem
        {
            "id": "ref_image_01",
            "type": "image",
            "x": 580,
            "y": 280,
            "width": 120,
            "height": 90,
            "angle": 0,
            "strokeColor": "transparent",
            "backgroundColor": "transparent",
            "fillStyle": "solid",
            "strokeWidth": 1,
            "strokeStyle": "solid",
            "roughness": 0,
            "opacity": 100,
            "groupIds": [],
            "frameId": "ref_frame_01",
            "roundness": None,
            "seed": 1010,
            "version": 1,
            "versionNonce": 2010,
            "isDeleted": False,
            "boundElements": None,
            "updated": timestamp_base,
            "link": None,
            "locked": False,
            "status": "saved",
            "fileId": "file_ref_logo_fcte",
            "scale": [1, 1],
        },
    ]

    cena = {
        "type": "excalidraw",
        "version": 2,
        "source": "https://excalidraw.com",
        "elements": elementos,
        "appState": {
            "gridSize": None,
            "viewBackgroundColor": "#ffffff",
        },
        "files": {
            "file_ref_logo_fcte": {
                "id": "file_ref_logo_fcte",
                "mimeType": "image/png",
                "dataURL": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg==",
                "created": timestamp_base,
                "lastRetrieved": timestamp_base,
            }
        },
    }

    os.makedirs(os.path.dirname(os.path.abspath(caminho_saida)), exist_ok=True)
    with open(caminho_saida, "w", encoding="utf-8") as f:
        json.dump(cena, f, indent=2, ensure_ascii=False)

    return cena


def gerar_cena_escala(n_elementos: int, caminho_saida: str) -> dict:
    """Gera uma cena com N elementos em grade (40% retângulos, 20% elipses, 20% setas e 20% textos)."""
    assert n_elementos % 10 == 0, "O número de elementos deve ser múltiplo de 10"

    # Colunas da grade por tamanho
    if n_elementos <= 100:
        colunas = 10
    elif n_elementos <= 1000:
        colunas = 40
    elif n_elementos <= 5000:
        colunas = 100
    else:
        colunas = 100

    espacamento_x = 160
    espacamento_y = 120
    largura_base = 120
    altura_base = 70
    timestamp_base = 1730000000000

    # Padrão periódico de 10 itens: 4 retângulos, 2 elipses, 2 setas, 2 textos
    padrao_tipos = [
        "rectangle", "rectangle", "rectangle", "rectangle",
        "ellipse", "ellipse",
        "arrow", "arrow",
        "text", "text"
    ]

    elementos = []
    for i in range(n_elementos):
        tipo = padrao_tipos[i % 10]
        col = i % colunas
        row = i // colunas
        x = col * espacamento_x + 50
        y = row * espacamento_y + 50
        elem_id = f"scale_{n_elementos}_{i+1:05d}"
        seed = 100000 + i
        nonce = 200000 + i

        elem_base = {
            "id": elem_id,
            "type": tipo,
            "x": x,
            "y": y,
            "width": largura_base,
            "height": altura_base,
            "angle": 0,
            "strokeWidth": 1.5,
            "strokeStyle": "solid",
            "roughness": 1,
            "opacity": 100,
            "groupIds": [],
            "frameId": None,
            "roundness": None,
            "seed": seed,
            "version": 1,
            "versionNonce": nonce,
            "isDeleted": False,
            "boundElements": None,
            "updated": timestamp_base,
            "link": None,
            "locked": False,
        }

        if tipo == "rectangle":
            elem_base.update({
                "strokeColor": "#1971c2",
                "backgroundColor": "#e7f5ff",
                "fillStyle": "solid",
                "roundness": {"type": 3},
            })
        elif tipo == "ellipse":
            elem_base.update({
                "strokeColor": "#2f9e44",
                "backgroundColor": "#ebfbee",
                "fillStyle": "solid",
            })
        elif tipo == "arrow":
            elem_base.update({
                "strokeColor": "#e03131",
                "backgroundColor": "transparent",
                "fillStyle": "solid",
                "height": 0,
                "points": [[0, 0], [largura_base, 0]],
                "startArrowhead": None,
                "endArrowhead": "arrow",
                "startBinding": None,
                "endBinding": None,
                "lastCommittedPoint": None,
            })
        elif tipo == "text":
            rotulo = f"E{i+1}"
            elem_base.update({
                "strokeColor": "#212529",
                "backgroundColor": "transparent",
                "fillStyle": "solid",
                "height": 24,
                "text": rotulo,
                "originalText": rotulo,
                "fontSize": 14,
                "fontFamily": 1,
                "textAlign": "center",
                "verticalAlign": "middle",
                "lineHeight": 1.2,
                "autoResize": True,
                "containerId": None,
            })

        elementos.append(elem_base)

    cena = {
        "type": "excalidraw",
        "version": 2,
        "source": "https://excalidraw.com",
        "elements": elementos,
        "appState": {
            "gridSize": None,
            "viewBackgroundColor": "#ffffff",
        },
        "files": {},
    }

    os.makedirs(os.path.dirname(os.path.abspath(caminho_saida)), exist_ok=True)
    with open(caminho_saida, "w", encoding="utf-8") as f:
        json.dump(cena, f, ensure_ascii=False)

    return cena


def gerar_arquivos_invalidos(diretorio_saida: str) -> dict:
    """Gera os 9 arquivos inválidos de teste para M2.3.1."""
    os.makedirs(diretorio_saida, exist_ok=True)
    arquivos_gerados = {}

    # Caso 1: Arquivo vazio com extensão .excalidraw (0 bytes)
    c1 = os.path.join(diretorio_saida, "invalido_01_vazio.excalidraw")
    with open(c1, "wb") as f:
        pass
    arquivos_gerados["invalido_01_vazio.excalidraw"] = {
        "caminho": c1,
        "defeito": "Arquivo vazio com 0 bytes",
        "comportamento_esperado": "Avisar que o arquivo está vazio sem quebrar a página",
    }

    # Caso 2: JSON com erro de sintaxe
    c2 = os.path.join(diretorio_saida, "invalido_02_json_malformado.excalidraw")
    with open(c2, "w", encoding="utf-8") as f:
        f.write('{\n  "type": "excalidraw",\n  "version": 2,\n  "elements": [\n    {"id": "rec_01", "type": "rectangle",\n')
    arquivos_gerados["invalido_02_json_malformado.excalidraw"] = {
        "caminho": c2,
        "defeito": "JSON com sintaxe quebrada",
        "comportamento_esperado": "Tratar o erro de leitura do JSON e avisar o usuário",
    }

    # Caso 3: JSON válido sem o campo type
    c3 = os.path.join(diretorio_saida, "invalido_03_sem_campo_type.excalidraw")
    conteudo_c3 = {
        "version": 2,
        "source": "https://excalidraw.com",
        "elements": [],
        "appState": {"viewBackgroundColor": "#ffffff"},
        "files": {},
    }
    with open(c3, "w", encoding="utf-8") as f:
        json.dump(conteudo_c3, f, indent=2)
    arquivos_gerados["invalido_03_sem_campo_type.excalidraw"] = {
        "caminho": c3,
        "defeito": "JSON sem o campo type",
        "comportamento_esperado": "Rejeitar o arquivo por falta do identificador do formato",
    }

    # Caso 4: Campo type com valor desconhecido
    c4 = os.path.join(diretorio_saida, "invalido_04_type_desconhecido.excalidraw")
    conteudo_c4 = {
        "type": "desconhecido",
        "version": 2,
        "source": "https://excalidraw.com",
        "elements": [],
        "appState": {"viewBackgroundColor": "#ffffff"},
        "files": {},
    }
    with open(c4, "w", encoding="utf-8") as f:
        json.dump(conteudo_c4, f, indent=2)
    arquivos_gerados["invalido_04_type_desconhecido.excalidraw"] = {
        "caminho": c4,
        "defeito": "Campo type com valor desconhecido",
        "comportamento_esperado": "Avisar que o tipo de arquivo não é suportado",
    }

    # Caso 5: Lista de elementos com campos obrigatórios ausentes
    c5 = os.path.join(diretorio_saida, "invalido_05_elementos_sem_campos_obrigatorios.excalidraw")
    conteudo_c5 = {
        "type": "excalidraw",
        "version": 2,
        "source": "https://excalidraw.com",
        "elements": [
            {"cor": "azul"},
            {"id": "elem_incompleto"},
        ],
        "appState": {"viewBackgroundColor": "#ffffff"},
        "files": {},
    }
    with open(c5, "w", encoding="utf-8") as f:
        json.dump(conteudo_c5, f, indent=2)
    arquivos_gerados["invalido_05_elementos_sem_campos_obrigatorios.excalidraw"] = {
        "caminho": c5,
        "defeito": "Elementos sem id, type ou coordenadas",
        "comportamento_esperado": "Identificar elemento incompleto sem travar o editor",
    }

    # Caso 6: Elemento com coordenadas não numéricas
    c6 = os.path.join(diretorio_saida, "invalido_06_coordenadas_nao_numericas.excalidraw")
    conteudo_c6 = {
        "type": "excalidraw",
        "version": 2,
        "source": "https://excalidraw.com",
        "elements": [
            {
                "id": "rec_01",
                "type": "rectangle",
                "x": "cem",
                "y": None,
                "width": "duzentos",
                "height": False,
            }
        ],
        "appState": {"viewBackgroundColor": "#ffffff"},
        "files": {},
    }
    with open(c6, "w", encoding="utf-8") as f:
        json.dump(conteudo_c6, f, indent=2)
    arquivos_gerados["invalido_06_coordenadas_nao_numericas.excalidraw"] = {
        "caminho": c6,
        "defeito": "Coordenadas com texto ou null no lugar de números",
        "comportamento_esperado": "Recusar ou descartar coordenadas inválidas sem erro",
    }

    # Caso 7: Arquivo binário qualquer renomeado para .excalidraw
    c7 = os.path.join(diretorio_saida, "invalido_07_binario_renomeado.excalidraw")
    dados_binarios = b"\x7fELF\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00>\x00\x01\x00\x00\x00\xff\xfe\xfd\xfc\x80\x81\x82\x83"
    with open(c7, "wb") as f:
        f.write(dados_binarios)
    arquivos_gerados["invalido_07_binario_renomeado.excalidraw"] = {
        "caminho": c7,
        "defeito": "Arquivo binário com extensão .excalidraw",
        "comportamento_esperado": "Tratar erro na leitura de texto UTF-8 e exibir mensagem",
    }

    # Caso 8: Imagem PNG sem desenho incorporado
    c8 = os.path.join(diretorio_saida, "invalido_08_png_sem_desenho.png")
    criar_png_minimo(c8)
    arquivos_gerados["invalido_08_png_sem_desenho.png"] = {
        "caminho": c8,
        "defeito": "Imagem PNG comum sem desenho embutido",
        "comportamento_esperado": "Ao tentar abrir pelo menu, avisar que não há desenho editável",
    }

    # Caso 9: Arquivo .excalidraw truncado no meio
    c9 = os.path.join(diretorio_saida, "invalido_09_truncado_no_meio.excalidraw")
    conteudo_truncado = (
        '{\n  "type": "excalidraw",\n  "version": 2,\n  "source": "https://excalidraw.com",\n'
        '  "elements": [\n    {\n      "id": "rec_001",\n      "type": "rectangle",\n'
        '      "x": 100,\n      "y": 100,\n      "width": 200,\n      "height": 100,\n'
        '      "angle": 0,\n      "strokeColor": "#1e1e1e",\n      "backgroundColor": "#a5d8ff",\n'
        '      "fillStyle": "solid",\n      "stroke'
    )
    with open(c9, "w", encoding="utf-8") as f:
        f.write(conteudo_truncado)
    arquivos_gerados["invalido_09_truncado_no_meio.excalidraw"] = {
        "caminho": c9,
        "defeito": "Arquivo JSON cortado pela metade",
        "comportamento_esperado": "Avisar que o arquivo está incompleto ou corrompido",
    }

    return arquivos_gerados


def verificar_massa_dados(diretorio_base: str) -> bool:
    """Confere se os arquivos gerados atendem às especificações das Fases 02 e 03."""
    sucesso_total = True
    print("\nVerificando arquivos gerados...")

    # 1. Verificar Cena de Referência
    caminho_ref = os.path.join(diretorio_base, "cena_referencia.excalidraw")
    if not os.path.exists(caminho_ref):
        print(f"[ERRO] Cena de referência não encontrada: {caminho_ref}")
        sucesso_total = False
    else:
        with open(caminho_ref, "r", encoding="utf-8") as f:
            dados_ref = json.load(f)
        tipos_encontrados = {elem.get("type") for elem in dados_ref.get("elements", [])}
        tem_bound_text = any(elem.get("type") == "text" and elem.get("containerId") for elem in dados_ref.get("elements", []))
        tem_imagem_com_file = any(elem.get("type") == "image" and elem.get("fileId") in dados_ref.get("files", {}) for elem in dados_ref.get("elements", []))

        tipos_esperados = {"rectangle", "ellipse", "diamond", "arrow", "line", "freedraw", "text", "image", "frame"}
        faltantes = tipos_esperados - tipos_encontrados

        if faltantes:
            print(f"[ERRO] Cena de referência sem os tipos: {faltantes}")
            sucesso_total = False
        elif not tem_bound_text:
            print("[ERRO] Cena de referência sem texto dentro de forma.")
            sucesso_total = False
        elif not tem_imagem_com_file:
            print("[ERRO] Imagem não vinculada ao dicionário files.")
            sucesso_total = False
        else:
            print(f"OK: cena_referencia.excalidraw (10 tipos, {len(dados_ref.get('elements', []))} elementos)")

    # 2. Verificar Cenas de Escala
    tamanhos_escala = [100, 1000, 5000, 10000]
    for n in tamanhos_escala:
        caminho_escala = os.path.join(diretorio_base, f"cena_{n}.excalidraw")
        if not os.path.exists(caminho_escala):
            print(f"[ERRO] Cena de escala não encontrada: {caminho_escala}")
            sucesso_total = False
            continue
        with open(caminho_escala, "r", encoding="utf-8") as f:
            dados_esc = json.load(f)
        elementos = dados_esc.get("elements", [])
        total = len(elementos)
        contagem = {}
        for elem in elementos:
            t = elem.get("type")
            contagem[t] = contagem.get(t, 0) + 1

        pct_rect = contagem.get("rectangle", 0) / total if total > 0 else 0
        pct_ell = contagem.get("ellipse", 0) / total if total > 0 else 0
        pct_arr = contagem.get("arrow", 0) / total if total > 0 else 0
        pct_txt = contagem.get("text", 0) / total if total > 0 else 0

        valido = (
            total == n
            and abs(pct_rect - 0.40) < 1e-4
            and abs(pct_ell - 0.20) < 1e-4
            and abs(pct_arr - 0.20) < 1e-4
            and abs(pct_txt - 0.20) < 1e-4
        )

        if not valido:
            print(f"[ERRO] Cena de escala {n} fora da proporção esperada: {contagem}")
            sucesso_total = False
        else:
            print(f"OK: cena_{n}.excalidraw ({total} elementos, proporção 40/20/20/20)")

    # 3. Verificar Arquivos Inválidos
    dir_invalidos = os.path.join(diretorio_base, "invalidos")
    casos_invalidos = [
        "invalido_01_vazio.excalidraw",
        "invalido_02_json_malformado.excalidraw",
        "invalido_03_sem_campo_type.excalidraw",
        "invalido_04_type_desconhecido.excalidraw",
        "invalido_05_elementos_sem_campos_obrigatorios.excalidraw",
        "invalido_06_coordenadas_nao_numericas.excalidraw",
        "invalido_07_binario_renomeado.excalidraw",
        "invalido_08_png_sem_desenho.png",
        "invalido_09_truncado_no_meio.excalidraw",
    ]

    for nome_arq in casos_invalidos:
        caminho_arq = os.path.join(dir_invalidos, nome_arq)
        if not os.path.exists(caminho_arq):
            print(f"[ERRO] Arquivo não encontrado: {caminho_arq}")
            sucesso_total = False
        else:
            print(f"OK: invalidos/{nome_arq}")

    return sucesso_total


def main():
    parser = argparse.ArgumentParser(description="Gera a massa de dados para avaliação do Excalidraw (Fase 03)")
    parser.add_argument(
        "--output-dir",
        default=os.path.join("dados", "fase-03", "massa-de-dados"),
        help="Diretório onde os arquivos serão gerados (padrão: dados/fase-03/massa-de-dados)",
    )
    parser.add_argument("--so-referencia", action="store_true", help="Gera apenas a cena de referência")
    parser.add_argument("--so-escala", action="store_true", help="Gera apenas as cenas de escala")
    parser.add_argument("--so-invalidos", action="store_true", help="Gera apenas os arquivos inválidos")
    parser.add_argument("--verificar", action="store_true", help="Executa a verificação dos arquivos gerados")

    args = parser.parse_args()
    dir_saida = os.path.abspath(args.output_dir)
    dir_invalidos = os.path.join(dir_saida, "invalidos")
    os.makedirs(dir_saida, exist_ok=True)

    gerar_tudo = not (args.so_referencia or args.so_escala or args.so_invalidos)

    print(f"Diretório de saída: {dir_saida}")

    if gerar_tudo or args.so_referencia:
        caminho_ref = os.path.join(dir_saida, "cena_referencia.excalidraw")
        gerar_cena_referencia(caminho_ref)
        print(f"Cena de referência salva em {caminho_ref}")

    if gerar_tudo or args.so_escala:
        for n in [100, 1000, 5000, 10000]:
            caminho_esc = os.path.join(dir_saida, f"cena_{n}.excalidraw")
            gerar_cena_escala(n, caminho_esc)
            print(f"Cena de escala {n} salva em {caminho_esc}")

    if gerar_tudo or args.so_invalidos:
        gerar_arquivos_invalidos(dir_invalidos)
        print(f"9 arquivos inválidos salvos em {dir_invalidos}")

    if args.verificar or gerar_tudo:
        sucesso = verificar_massa_dados(dir_saida)
        if not sucesso:
            print("\nA verificação encontrou problemas.")
            sys.exit(1)
        else:
            print("\nTodos os arquivos foram gerados e verificados com sucesso.")


if __name__ == "__main__":
    main()

