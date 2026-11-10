# Repositório de Medidas — Fase 04

Este diretório contém os dados brutos e consolidados da avaliação empírica do software Excalidraw (commit `e1b7aac`), atendendo aos critérios **F4-C1** (obtenção das medidas) e **F4-C2** (dados brutos e rastreabilidade).

---

## Estrutura de Diretórios

- **`brutos/`**: Saídas diretas de ferramentas, logs de execução de scripts, tabelas de conferência e formulários de medição preenchidos.
- **`consolidados/`**: Planilhas e relatórios finais processados a partir dos dados brutos, utilizados diretamente para responder às questões GQM.

---

## Arquivos de Dados Brutos — Objetivo G3 (Flexibilidade)

| Arquivo | Métrica | Descrição |
| :--- | :---: | :--- |
| `M3.1.1_cobertura_browserslist.txt` | **M3.1.1** | Saída do comando oficial do Browserslist com o percentual de cobertura populacional global de navegadores. |
| `M3.1.3_formulario_toque_caneta.csv` | **M3.1.3** | Modelo de formulário para conferência das 10 ações por toque e caneta stylus no tablet. |
| `M3.2.1_tempos_abertura.csv` | **M3.2.1** | Modelo de planilha para registro das 5 repetições do tempo de abertura das cenas de escala no DevTools. |
| `M3.2.2_fps_edicao.csv` | **M3.2.2** | Modelo de planilha para registro das taxas de quadros por segundo (FPS) durante edição contínua. |
| `M3.2.3_tamanho_maximo_salvamento.csv` | **M3.2.3** | Modelo de planilha para teste de estresse de salvamento e exportação de cenas grandes. |
| `M3.4.1_catalogo_formatos.csv` | **M3.4.1** | Catálogo dos formatos abertos suportados pelo Excalidraw, tipos MIME e especificações de referência. |
| `M3.4.3_campos_encontrados.json` | **M3.4.3** | Lista de todas as 52 propriedades reais extraídas da cena de referência do Excalidraw. |
| `M3.4.3_conferencia_campos.csv` | **M3.4.3** | Auditoria campo a campo contra o guia oficial de especificação técnica (`json-schema.mdx`). |
| `M3.4.3_relatorio.txt` | **M3.4.3** | Relatório de auditoria com percentual de campos documentados e lista de campos omitidos. |
