from PIL import Image, ImageDraw, ImageFont
import os

def create_methodology_diagram(output_path):
    width = 2400
    height = 1380
    img = Image.new('RGB', (width, height), color='#FFFFFF')
    draw = ImageDraw.Draw(img)

    font_dir = '/usr/share/fonts/truetype/liberation'
    font_title = ImageFont.truetype(os.path.join(font_dir, 'LiberationSans-Bold.ttf'), 40)
    font_subtitle = ImageFont.truetype(os.path.join(font_dir, 'LiberationSans-Regular.ttf'), 24)
    font_phase_title = ImageFont.truetype(os.path.join(font_dir, 'LiberationSans-Bold.ttf'), 23)
    font_phase_sub = ImageFont.truetype(os.path.join(font_dir, 'LiberationSans-Italic.ttf'), 18)
    font_tag = ImageFont.truetype(os.path.join(font_dir, 'LiberationSans-Bold.ttf'), 17)
    font_item_bold = ImageFont.truetype(os.path.join(font_dir, 'LiberationSans-Bold.ttf'), 17)
    font_item = ImageFont.truetype(os.path.join(font_dir, 'LiberationSans-Regular.ttf'), 17)
    font_group = ImageFont.truetype(os.path.join(font_dir, 'LiberationSans-Bold.ttf'), 20)
    font_gov_title = ImageFont.truetype(os.path.join(font_dir, 'LiberationSans-Bold.ttf'), 22)
    font_gov_sub = ImageFont.truetype(os.path.join(font_dir, 'LiberationSans-Regular.ttf'), 19)

    # 1. Título e Subtítulo
    draw.text((width // 2, 45), "Metodologia de Avaliação da Qualidade do Excalidraw", fill='#0F172A', font=font_title, anchor='mm')
    draw.text((width // 2, 85), "Processo sistemático da ISO/IEC 25040 integrado à abordagem GQM e governança no GitHub", fill='#475569', font=font_subtitle, anchor='mm')

    # Marcadores das Entregas
    # Entrega 1 (Fases 1 e 2)
    draw.rounded_rectangle([50, 115, 1170, 155], radius=6, fill='#EFF6FF', outline='#3B82F6', width=2)
    draw.text((610, 135), "ENTREGA 1 (Fases Concluídas e Relatadas Neste Artigo)", fill='#1D4ED8', font=font_group, anchor='mm')

    # Entrega 2 (Fases 3 e 4)
    draw.rounded_rectangle([1230, 115, 2350, 155], radius=6, fill='#F8FAFC', outline='#64748B', width=2)
    draw.text((1790, 135), "ENTREGA 2 (Fases Planejadas para a Etapa Subsequente)", fill='#334155', font=font_group, anchor='mm')

    phases = [
        {
            "tag": "Caixa 1",
            "num": "Fase 1",
            "title": "Requisitos de Avaliação",
            "resp": "Subgrupo F1/F3 (Davi, Gabriel, Letícia)",
            "border": "#2563EB",
            "header_bg": "#DBEAFE",
            "items": [
                ("Propósito:", "Diagnóstico e melhoria do produto"),
                ("Linha de base:", "Commit e1b7aac (18/10/2026)"),
                ("Partes interessadas:", "7 grupos e matriz de prioridades"),
                ("Características:", "Manutenib., Confiab., Flexib."),
                ("Modelo de qualidade:", "13 subcaracterísticas investigadas"),
                ("Requisitos técnicos:", "36 perguntas de avaliação (RQ-*)")
            ]
        },
        {
            "tag": "Caixa 2",
            "num": "Fase 2",
            "title": "Especificação da Avaliação",
            "resp": "Subgrupo F2/F4 (Christopher, Luiz, Eduarda)",
            "border": "#059669",
            "header_bg": "#D1FAE5",
            "items": [
                ("Objetivos GQM:", "G1, G2 e G3 (nível conceitual)"),
                ("Questões operacionais:", "13 questões e hipóteses formais"),
                ("Catálogo de métricas:", "36 medidas objetivas e fórmulas"),
                ("Régua de pontuação:", "Escala de 5 níveis SIG (++ a --)"),
                ("Faixas de aceitação:", "Limites estabelecidos pré-coleta"),
                ("Critérios de julgamento:", "Atende, Não Atende, Inconclusivo")
            ]
        },
        {
            "tag": "Caixa 3",
            "num": "Fase 3",
            "title": "Projeto da Avaliação",
            "resp": "Subgrupo F1/F3 (Davi, Gabriel, Letícia)",
            "border": "#7C3AED",
            "header_bg": "#EDE9FE",
            "items": [
                ("Procedimentos:", "Roteiros de inspeção estática"),
                ("Ferramentas estáticas:", "ESLint, TypeScript, cloc, ts-morph"),
                ("Testes automatizados:", "Vitest, cobertura e testes E2E"),
                ("Ambiente de teste:", "Node.js, Chromium e scripts"),
                ("Plano de medição:", "Responsáveis, cronograma e meios"),
                ("Plano de análise:", "Processamento e agregação prévia")
            ]
        },
        {
            "tag": "Caixa 4",
            "num": "Fase 4",
            "title": "Execução e Julgamento",
            "resp": "Subgrupo F2/F4 (Christopher, Luiz, Eduarda)",
            "border": "#D97706",
            "header_bg": "#FEF3C7",
            "items": [
                ("Coleta de dados:", "Medição prática sobre a baseline"),
                ("Análise de hipóteses:", "Confronto de resultados e metas"),
                ("Agregação matemática:", "Média das métricas e questões"),
                ("Julgamento de qualidade:", "Aplicação dos critérios formais"),
                ("Pontos de melhoria:", "Diagnóstico de fragilidades do código"),
                ("Proposição de ações:", "Intervenções e protótipo de tela")
            ]
        }
    ]

    box_w = 535
    box_h = 610
    y_start = 180
    gap = 50
    x_offset = 50

    for i, p in enumerate(phases):
        x = x_offset + i * (box_w + gap)

        # Sombra
        draw.rounded_rectangle([x + 3, y_start + 3, x + box_w + 3, y_start + box_h + 3], radius=14, fill='#E2E8F0')
        # Caixa principal
        draw.rounded_rectangle([x, y_start, x + box_w, y_start + box_h], radius=14, fill='#FFFFFF', outline=p['border'], width=3)

        # Cabeçalho
        header_h = 100
        draw.rounded_rectangle([x, y_start, x + box_w, y_start + header_h], radius=14, fill=p['header_bg'])
        draw.rectangle([x, y_start + header_h - 14, x + box_w, y_start + header_h], fill=p['header_bg'])
        draw.line([x, y_start + header_h, x + box_w, y_start + header_h], fill=p['border'], width=2)

        # Tag no topo direito do cabeçalho
        tag_w = 80
        tag_h = 24
        tag_x = x + box_w - tag_w - 15
        tag_y = y_start + 14
        draw.rounded_rectangle([tag_x, tag_y, tag_x + tag_w, tag_y + tag_h], radius=5, fill=p['border'])
        draw.text((tag_x + tag_w // 2, tag_y + tag_h // 2), p['tag'], fill='#FFFFFF', font=font_tag, anchor='mm')

        # Título da fase
        draw.text((x + 16, y_start + 16), f"{p['num']}: {p['title']}", fill='#0F172A', font=font_phase_title)
        draw.text((x + 16, y_start + 55), p['resp'], fill='#334155', font=font_phase_sub)

        # Itens
        cur_y = y_start + header_h + 24
        for label, val in p['items']:
            # Ponto colorido
            draw.ellipse([x + 18, cur_y + 4, x + 28, cur_y + 14], fill=p['border'])
            draw.text((x + 36, cur_y), label, fill='#0F172A', font=font_item_bold)
            label_len = draw.textlength(label, font=font_item_bold)
            draw.text((x + 42 + label_len, cur_y), val, fill='#334155', font=font_item)
            cur_y += 76

        # Setas de transição entre as fases
        if i < len(phases) - 1:
            ax1 = x + box_w + 6
            ax2 = x + box_w + gap - 6
            ay = y_start + 290
            draw.line([ax1, ay, ax2, ay], fill='#64748B', width=4)
            draw.polygon([(ax2, ay), (ax2 - 14, ay - 10), (ax2 - 14, ay + 10)], fill='#64748B')

    # Caixa 5: Governança Técnica da Equipe e Fluxo no GitHub
    gov_y = y_start + box_h + 30
    gov_h = 490
    draw.rounded_rectangle([x_offset + 3, gov_y + 3, width - x_offset + 3, gov_y + gov_h + 3], radius=14, fill='#E2E8F0')
    draw.rounded_rectangle([x_offset, gov_y, width - x_offset, gov_y + gov_h], radius=14, fill='#F8FAFC', outline='#475569', width=3)

    # Cabeçalho da Governança
    gov_header_h = 65
    draw.rounded_rectangle([x_offset, gov_y, width - x_offset, gov_y + gov_header_h], radius=14, fill='#E2E8F0')
    draw.rectangle([x_offset, gov_y + gov_header_h - 14, width - x_offset, gov_y + gov_header_h], fill='#E2E8F0')
    draw.line([x_offset, gov_y + gov_header_h, width - x_offset, gov_y + gov_header_h], fill='#475569', width=2)

    # Tag Caixa 5
    draw.rounded_rectangle([x_offset + 20, gov_y + 18, x_offset + 105, gov_y + 46], radius=5, fill='#475569')
    draw.text((x_offset + 62, gov_y + 32), "Caixa 5", fill='#FFFFFF', font=font_tag, anchor='mm')

    draw.text((x_offset + 125, gov_y + 20), "Estrutura Organizacional da Equipe e Governança no GitHub", fill='#0F172A', font=font_gov_title)
    draw.text((x_offset + 950, gov_y + 23), "Práticas transversais assegurando rastreabilidade, integridade técnica e validação contínua", fill='#475569', font=font_gov_sub)

    # 3 Colunas na Caixa 5
    col_w = 720
    col_gap = 40
    c_y = gov_y + gov_header_h + 24

    # Coluna 1
    c1_x = x_offset + 30
    draw.text((c1_x, c_y), "Divisão da Equipe em Subgrupos", fill='#1E293B', font=font_phase_title)
    draw.text((c1_x, c_y + 40), "• 6 integrantes distribuídos em 2 subgrupos estáveis de 3 membros.", fill='#334155', font=font_item)
    draw.text((c1_x, c_y + 75), "• Subgrupo F1/F3: Requisitos de Avaliação (F1) e Projeto dos Testes (F3).", fill='#334155', font=font_item)
    draw.text((c1_x, c_y + 110), "• Subgrupo F2/F4: Especificação GQM (F2) e Execução prática das medições (F4).", fill='#334155', font=font_item)
    draw.text((c1_x, c_y + 145), "• Frentes transversais conjuntas: redação do artigo científico e pontos de controle.", fill='#334155', font=font_item)

    # Coluna 2
    c2_x = c1_x + col_w + col_gap
    draw.text((c2_x, c_y), "Fluxo de Trabalho e Branches no GitHub", fill='#1E293B', font=font_phase_title)
    draw.text((c2_x, c_y + 40), "• Proibição estrita de envios ou alterações diretas na branch principal (main).", fill='#334155', font=font_item)
    draw.text((c2_x, c_y + 75), "• Toda atividade inicia por issue padronizada com estimativa de esforço e prazos.", fill='#334155', font=font_item)
    draw.text((c2_x, c_y + 110), "• Branches temáticas no padrão tipo/área-descrição (ex.: docs/f1-..., docs/artigo-...).", fill='#334155', font=font_item)
    draw.text((c2_x, c_y + 145), "• Rastreabilidade de ponta a ponta vinculando issues, commits e artefatos.", fill='#334155', font=font_item)

    # Coluna 3
    c3_x = c2_x + col_w + col_gap
    draw.text((c3_x, c_y), "Revisão por Pares e Transparência no Uso de IA", fill='#1E293B', font=font_phase_title)
    draw.text((c3_x, c_y + 40), "• Pull Requests integrados somente após aprovação de integrante não autor.", fill='#334155', font=font_item)
    draw.text((c3_x, c_y + 75), "• Revisão técnica cruzada garantindo conformidade com a rubrica e com o código.", fill='#334155', font=font_item)
    draw.text((c3_x, c_y + 110), "• Declaração formal e transparente de ferramentas de IA generativa em cada PR.", fill='#334155', font=font_item)
    draw.text((c3_x, c_y + 145), "• Conferência crítica humana obrigatória de todo texto, fórmula e imagem gerada.", fill='#334155', font=font_item)

    # Conexões verticais conectando Caixa 5 às 4 Fases
    for px in [x_offset + box_w // 2, x_offset + box_w + gap + box_w // 2, x_offset + 2*(box_w + gap) + box_w // 2, x_offset + 3*(box_w + gap) + box_w // 2]:
        draw.line([px, y_start + box_h, px, gov_y], fill='#94A3B8', width=3)
        draw.polygon([(px, y_start + box_h + 4), (px - 7, y_start + box_h + 16), (px + 7, y_start + box_h + 16)], fill='#94A3B8')

    img.save(output_path, 'PNG', quality=95)
    print(f"Diagrama salvo com sucesso em: {output_path}")

if __name__ == '__main__':
    create_methodology_diagram('artigo/figura-metodologia.png')
    create_methodology_diagram('docs/images/figura-metodologia.png')
