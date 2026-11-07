#!/usr/bin/env python3
"""
Gera o gráfico de linha de desempenho de execução do projeto (Curva S):
Horas Estimadas Acumuladas vs. Horas Reais Acumuladas ao longo do tempo.
Utiliza apenas bibliotecas padrão e PIL para renderização em alta resolução.
"""

import csv
from datetime import datetime
from collections import defaultdict
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


def fontes_pages(escala: int):
    base = "/usr/share/fonts/truetype/inter-zorin-os/"
    try:
        return (
            ImageFont.truetype(base + "Inter-Bold.ttf", 20 * escala),
            ImageFont.truetype(base + "Inter-Medium.ttf", 13 * escala),
            ImageFont.truetype(base + "Inter-Bold.ttf", 12 * escala),
            ImageFont.truetype(base + "Inter-Regular.ttf", 11 * escala),
            ImageFont.truetype(base + "Inter-Medium.ttf", 10 * escala)
        )
    except Exception:
        dj = "/usr/share/fonts/truetype/dejavu/"
        try:
            return (
                ImageFont.truetype(dj + "DejaVuSans-Bold.ttf", 20 * escala),
                ImageFont.truetype(dj + "DejaVuSans.ttf", 13 * escala),
                ImageFont.truetype(dj + "DejaVuSans-Bold.ttf", 12 * escala),
                ImageFont.truetype(dj + "DejaVuSans.ttf", 11 * escala),
                ImageFont.truetype(dj + "DejaVuSans.ttf", 10 * escala)
            )
        except Exception:
            f = ImageFont.load_default()
            return f, f, f, f, f


def gerar_grafico_desempenho(csv_path: Path, output_paths: list[Path]) -> None:
    with open(csv_path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    pontos = []
    for r in rows:
        if r.get("estado") == "closed" and r.get("data_fechamento") and r["data_fechamento"] != "N/A":
            try:
                dt = datetime.strptime(r["data_fechamento"], "%d/%m/%Y")
                est = float(r["estimativa_h"]) if r.get("estimativa_h") else 0.0
                real = float(r["horas_reais_h"]) if r.get("horas_reais_h") else 0.0
                pontos.append((dt, est, real))
            except Exception:
                pass

    if not pontos:
        print("[AVISO] Nenhuma issue concluída encontrada com data de fechamento válida.")
        return

    pontos.sort(key=lambda x: x[0])
    datas_unicas = sorted(list(set(p[0] for p in pontos)))

    por_data = defaultdict(lambda: {"est": 0.0, "real": 0.0})
    for dt, est, real in pontos:
        por_data[dt]["est"] += est
        por_data[dt]["real"] += real

    datas_labels = [d.strftime("%d/%m") for d in datas_unicas]
    acum_est, acum_real = [], []
    s_est, s_real = 0.0, 0.0
    for d in datas_unicas:
        s_est += por_data[d]["est"]
        s_real += por_data[d]["real"]
        acum_est.append(round(s_est, 1))
        acum_real.append(round(s_real, 1))

    escala = 2
    w, h = 1000 * escala, 620 * escala
    img = Image.new("RGB", (w, h), "#ffffff")
    draw = ImageDraw.Draw(img)
    f_titulo, f_sub, f_bold, f_txt, f_small = fontes_pages(escala)

    # Borda externa do card
    draw.rounded_rectangle(
        [10 * escala, 10 * escala, w - 10 * escala, h - 10 * escala],
        radius=6 * escala, outline="#e5e7eb", width=2 * escala
    )

    # Título e subtítulo
    draw.text((60 * escala, 28 * escala), "Desempenho de Execução: Curva S de Esforço Acumulado", fill="#111827", font=f_titulo)
    draw.text((60 * escala, 58 * escala), "Evolução temporal das Horas Estimadas (Planejado) vs. Horas Reais (Executado) — Fases 1 e 2", fill="#4b5563", font=f_sub)

    # Legenda
    cor_est = "#2563eb"   # Azul real
    cor_real = "#059669"  # Verde esmeralda

    # Item 1: Planejado
    draw.line([(60 * escala, 98 * escala), (85 * escala, 98 * escala)], fill=cor_est, width=3 * escala)
    draw.ellipse([70 * escala, 95 * escala, 76 * escala, 101 * escala], fill=cor_est)
    draw.text((95 * escala, 90 * escala), "Horas Estimadas Acumuladas (Planejado)", fill="#111827", font=f_bold)

    # Item 2: Executado
    draw.line([(400 * escala, 98 * escala), (425 * escala, 98 * escala)], fill=cor_real, width=3 * escala)
    draw.ellipse([410 * escala, 95 * escala, 416 * escala, 101 * escala], fill=cor_real)
    draw.text((435 * escala, 90 * escala), "Horas Reais Acumuladas (Executado)", fill="#111827", font=f_bold)

    # Área de plotagem
    x0 = 80 * escala
    x1 = w - 80 * escala
    y_top = 145 * escala
    y_bot = h - 85 * escala

    max_val = max(max(acum_est), max(acum_real))
    max_y = float(((int(max_val * 1.15) // 25) + 1) * 25)
    ticks = [int(max_y * i / 6) for i in range(7)]

    # Grade horizontal
    for val in ticks:
        y = y_bot - (y_bot - y_top) * (val / max_y)
        draw.line([(x0, y), (x1, y)], fill="#f3f4f6" if val > 0 else "#e5e7eb", width=escala)
        lbl = f"{val}h"
        bb = draw.textbbox((0, 0), lbl, font=f_txt)
        draw.text((x0 - (bb[2] - bb[0]) - 12 * escala, y - (bb[3] - bb[1]) / 2), lbl, fill="#6b7280", font=f_txt)

    n = len(datas_labels)
    step_x = (x1 - x0) / max(n - 1, 1)
    pts_est = []
    pts_real = []

    for i in range(n):
        cx = x0 + i * step_x
        draw.line([(cx, y_top), (cx, y_bot)], fill="#f9fafb", width=escala)
        
        lbl = datas_labels[i]
        bb = draw.textbbox((0, 0), lbl, font=f_txt)
        draw.text((cx - (bb[2] - bb[0]) / 2, y_bot + 12 * escala), lbl, fill="#374151", font=f_txt)
        
        cy_est = y_bot - (y_bot - y_top) * (acum_est[i] / max_y)
        cy_real = y_bot - (y_bot - y_top) * (acum_real[i] / max_y)
        pts_est.append((cx, cy_est))
        pts_real.append((cx, cy_real))

    # Marco temporal: Release E1 (26/10)
    if "26/10" in datas_labels:
        idx_e1 = datas_labels.index("26/10")
        mx = x0 + idx_e1 * step_x
        for yy in range(int(y_top), int(y_bot), 8 * escala):
            draw.line([(mx, yy), (mx, min(yy + 4 * escala, y_bot))], fill="#cbd5e1", width=escala)
        txt_marco = "Marco: Release E1 (26/10)"
        bb_m = draw.textbbox((0, 0), txt_marco, font=f_small)
        draw.text((mx - (bb_m[2] - bb_m[0]) / 2, y_top - 18 * escala), txt_marco, fill="#64748b", font=f_small)

    # Linhas
    for i in range(n - 1):
        draw.line([pts_est[i], pts_est[i + 1]], fill=cor_est, width=3 * escala)
        draw.line([pts_real[i], pts_real[i + 1]], fill=cor_real, width=3 * escala)

    # Pontos
    r = 5 * escala
    for i in range(n):
        cx, cy_e = pts_est[i]
        _, cy_r = pts_real[i]
        draw.ellipse([cx - r, cy_e - r, cx + r, cy_e + r], fill=cor_est, outline="#ffffff", width=2 * escala)
        draw.ellipse([cx - r, cy_r - r, cx + r, cy_r + r], fill=cor_real, outline="#ffffff", width=2 * escala)

    # Rótulo de valores finais
    bb_e = draw.textbbox((0, 0), f"{acum_est[-1]}h", font=f_bold)
    draw.text((pts_est[-1][0] - (bb_e[2] - bb_e[0]) - 10 * escala, pts_est[-1][1] - 22 * escala), f"{acum_est[-1]}h", fill=cor_est, font=f_bold)

    bb_r = draw.textbbox((0, 0), f"{acum_real[-1]}h", font=f_bold)
    draw.text((pts_real[-1][0] - (bb_r[2] - bb_r[0]) - 10 * escala, pts_real[-1][1] + 8 * escala), f"{acum_real[-1]}h", fill=cor_real, font=f_bold)

    # Badge no rodapé
    acuracia_acum = (acum_real[-1] / acum_est[-1]) * 100 if acum_est[-1] > 0 else 100.0
    status_str = "Faixa Ideal de Excelência (80% a 120%)" if 80 <= acuracia_acum <= 120 else "Em Calibração"
    badge_txt = f"Acurácia Global Acumulada: {acuracia_acum:.1f}%  |  Status: {status_str}"
    bb_b = draw.textbbox((0, 0), badge_txt, font=f_small)
    bw = bb_b[2] - bb_b[0] + 24 * escala
    bh = bb_b[3] - bb_b[1] + 12 * escala
    bx = (w - bw) / 2
    by = h - 45 * escala
    draw.rounded_rectangle([bx, by, bx + bw, by + bh], radius=4 * escala, fill="#ecfdf5", outline="#a7f3d0", width=escala)
    draw.text((bx + 12 * escala, by + 6 * escala), badge_txt, fill="#065f46", font=f_small)

    img_final = img.resize((1000, 620), Image.Resampling.LANCZOS)
    for p in output_paths:
        p.parent.mkdir(parents=True, exist_ok=True)
        img_final.save(p, format="PNG", dpi=(300, 300))
        print(f"[PNG] Gerado: {p}")


if __name__ == "__main__":
    raiz = Path(__file__).resolve().parent.parent
    csv_file = raiz / "dados" / "gestao" / "05_detalhamento_issues.csv"
    destinos = [
        raiz / "dados" / "gestao" / "graficos" / "08_desempenho_execucao_curva_s.png",
        raiz / "static" / "img" / "gestao" / "08_desempenho_execucao_curva_s.png",
    ]
    gerar_grafico_desempenho(csv_file, destinos)
