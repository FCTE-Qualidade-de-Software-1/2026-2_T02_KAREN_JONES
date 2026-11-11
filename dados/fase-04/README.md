# Repositório de Medidas — Fase 04

Este diretório contém os dados brutos e consolidados da avaliação empírica do software Excalidraw (commit `e1b7aac`), atendendo aos critérios **F4-C1** (obtenção das medidas) e **F4-C2** (dados brutos e rastreabilidade).

---

## Estrutura de Diretórios

- **`brutos/`**: Saídas diretas de ferramentas, logs de execução de scripts, traces DevTools, tabelas de conferência e formulários de medição organizados por questão GQM:
  - **`Q3.1-adaptabilidade/`**: Medidas de compatibilidade de navegadores (M3.1.1), integração de bibliotecas (M3.1.2) e usabilidade móvel por toque/caneta (M3.1.3).
  - **`Q3.2-escalabilidade/`**: Medidas de tempo de abertura (M3.2.1), taxas de quadros em edição contínua (M3.2.2) e persistência/exportação de grandes volumes (M3.2.3), incluindo a subpasta `traces_abertura/` com os perfis brutos de desempenho gerados pelo Chrome DevTools.
  - **`Q3.3-instalabilidade/`**: Medidas de ciclo de vida de pacotes com múltiplos gerenciadores (M3.3.1), reprodutibilidade de passos de compilação documentados (M3.3.2) e implantação oficial via Docker (M3.3.3).
  - **`Q3.4-substituibilidade/`**: Catálogo de formatos abertos (M3.4.1), testes de reimportação e preservação de elementos (M3.4.2 com subpasta `reimportacao_arquivos/`) e auditoria de completude da documentação do esquema (M3.4.3).
- **`consolidados/`**: Planilhas e relatórios finais processados a partir dos dados brutos, utilizados diretamente para responder às questões GQM.

---

## Catálogo de Arquivos Brutos — Objetivo G3 (Flexibilidade)

### Q3.1 — Adaptabilidade
| Arquivo | Métrica | Descrição |
| :--- | :---: | :--- |
| `Q3.1-adaptabilidade/M3.1.1_cobertura_browserslist.txt` | **M3.1.1** | Saída do comando oficial do Browserslist com o percentual de cobertura populacional global de navegadores. |
| `Q3.1-adaptabilidade/M3.1.2_matriz_integracao.csv` | **M3.1.2** | Matriz de avaliação das 6 combinações de integração (React 17, 18, 19 × Vite, Next.js). |
| `Q3.1-adaptabilidade/M3.1.2_build_logs.zip` | **M3.1.2** | Arquivo compactado contendo todos os logs brutos de compilação e instalação dos 6 ambientes. |
| `Q3.1-adaptabilidade/M3.1.2_evidencia_ambiente.png` | **M3.1.2** | Mosaico comprobatório com capturas de tela do canvas e desenho de formas nos ambientes validados. |
| `Q3.1-adaptabilidade/M3.1.3_formulario_toque_caneta.csv` | **M3.1.3** | Formulário de auditoria empírica das 10 ações por toque e caneta stylus no tablet iPad A16. |
| `Q3.1-adaptabilidade/M3.1.3_gravacao_toque.mp4` | **M3.1.3** | Gravação de tela oficial (8,4 MB) da execução das 10 ações de teste por toque direto com o dedo no iPad. |
| `Q3.1-adaptabilidade/M3.1.3_gravacao_caneta.mp4` | **M3.1.3** | Gravação de tela oficial (4,7 MB) da execução das 10 ações de teste com a caneta capacitiva stylus Goojodoq no iPad. |

### Q3.2 — Escalabilidade
| Arquivo | Métrica | Descrição |
| :--- | :---: | :--- |
| `Q3.2-escalabilidade/M3.2.1_tempos_abertura.csv` | **M3.2.1** | Tabela com todas as repetições e medianas do tempo de abertura por escala no DevTools. |
| `Q3.2-escalabilidade/traces_abertura/` | **M3.2.1** | Perfis de rastreamento completos (`.json`) exportados da aba Performance do Chrome DevTools para cada cena e repetição. |
| `Q3.2-escalabilidade/M3.2.2_fps_edicao.csv` | **M3.2.2** | Planilha para registro das taxas de quadros por segundo (FPS) durante edição contínua. |
| `Q3.2-escalabilidade/M3.2.3_tamanho_maximo_salvamento.csv` | **M3.2.3** | Planilha para teste de estresse de salvamento e exportação de cenas grandes. |

### Q3.3 — Instalabilidade
| Arquivo | Métrica | Descrição |
| :--- | :---: | :--- |
| `Q3.3-instalabilidade/M3.3.1_log_operacoes_pacote.txt` | **M3.3.1** | Log detalhado da execução de instalação, atualização e desinstalação via npm, yarn e pnpm. |
| `Q3.3-instalabilidade/M3.3.1_resultados_pacote.csv` | **M3.3.1** | Tabela comparativa das 9 operações de pacote por gerenciador (cenário público e local). |
| `Q3.3-instalabilidade/M3.3.2_log_reproducao_passos.txt` | **M3.3.2** | Registro textual da auditoria dos 7 passos documentados de compilação e execução local. |
| `Q3.3-instalabilidade/M3.3.2_passos_ajustes.csv` | **M3.3.2** | Tabela dos 7 passos documentados com classificação (sem ajuste vs com ajuste) e justificativas. |
| `Q3.3-instalabilidade/M3.3.3_verificacoes_docker.csv` | **M3.3.3** | Tabela de conferência das 4 verificações de implantação com Docker (build, run, healthcheck, navegação). |

### Q3.4 — Substituibilidade
| Arquivo | Métrica | Descrição |
| :--- | :---: | :--- |
| `Q3.4-substituibilidade/M3.4.1_catalogo_formatos.csv` | **M3.4.1** | Catálogo dos formatos abertos suportados pelo Excalidraw, tipos MIME e especificações de referência. |
| `Q3.4-substituibilidade/M3.4.2_preservacao_formatos.csv` | **M3.4.2** | Resumo da proporção de preservação de elementos após exportação e reimportação nos 3 formatos. |
| `Q3.4-substituibilidade/M3.4.2_relatorio_preservacao.json` | **M3.4.2** | Relatório técnico detalhado da comparação elemento a elemento realizado por `compara_elementos.py`. |
| `Q3.4-substituibilidade/M3.4.2_arquivos_reimportados.zip` | **M3.4.2** | Pacote ZIP contendo os arquivos exportados e reimportados da cena de referência. |
| `Q3.4-substituibilidade/reimportacao_arquivos/` | **M3.4.2** | Arquivos brutos gerados durante o ciclo de exportação e reimportação (.excalidraw, .png, .svg). |
| `Q3.4-substituibilidade/M3.4.3_campos_encontrados.json` | **M3.4.3** | Lista de todas as 52 propriedades reais extraídas da cena de referência do Excalidraw. |
| `Q3.4-substituibilidade/M3.4.3_conferencia_campos.csv` | **M3.4.3** | Auditoria campo a campo contra o guia oficial de especificação técnica (`json-schema.mdx`). |
| `Q3.4-substituibilidade/M3.4.3_relatorio.txt` | **M3.4.3** | Relatório de auditoria com percentual de campos documentados e lista de campos omitidos. |

---

## Catálogo de Arquivos Consolidados

| Arquivo | Finalidade e Conteúdo |
| :--- | :--- |
| `consolidados/G3_metricas_consolidadas.csv` | Tabela consolidada com as 12 métricas de G3, incluindo valores medidos, unidades, pontuação atribuída (0 a 100), nível na régua, hipóteses formuladas, status (confirmada/refutada) e apontamento para os arquivos brutos. |
| `consolidados/G3_questoes_pontuacao.csv` | Resumo executivo das 4 questões GQM (Q3.1 Adaptabilidade, Q3.2 Escalabilidade, Q3.3 Instalabilidade, Q3.4 Substituibilidade) e da pontuação global ponderada do objetivo G3 (78,65 pts — Nível Bom). |

