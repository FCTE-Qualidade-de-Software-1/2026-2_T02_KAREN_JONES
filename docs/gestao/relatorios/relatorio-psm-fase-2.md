---
id: relatorio-psm-fase-2
title: Relatório PSM/CID da Fase 2
sidebar_label: Relatório PSM/CID (Fase 2)
sidebar_position: 2
description: Medições quantitativas das três categorias, measurement constructs no template PSM, análise comparativa com a Fase 1 e decisões de gestão da Entrega 1 (ISO/IEC 15939 e PSM/CID).
---

# Relatório de Gestão com Métricas PSM/CID — Fase 2

Este documento consolida as medições, indicadores de performance e decisões de gestão da **Fase 2** (Especificar a Avaliação via GQM), integrando o balanço consolidado da **Entrega 1 (Fases 1 e 2)** da avaliação de qualidade do software **Excalidraw**, com base nas normas **ISO/IEC 25040**, **ISO/IEC 15939** e no modelo **PSM/CID (CID 2021)**.

O relatório atende expressamente aos quatro critérios de pronto da **Issue #31**, à **Premissa 3** (análise de performance, interpretação e decisões) e à **Premissa 5** (rastreabilidade a partir de dados primários versionados).

---

## 1. Contexto da Fase 2 e Fechamento da Entrega 1

A Fase 2 representou a transição do levantamento de requisitos de qualidade (Fase 1) para a **especificação técnica e operacional da avaliação** por meio do paradigma Goal-Question-Metric (GQM).

Nesta etapa, o trabalho da equipe distribuiu-se em três eixos integrados:
1. **Especificação Técnica GQM (Subgrupo F2/F4):** Formulação dos objetivos conceituais, questões operacionais, hipóteses de teste, catálogo de métricas e critérios de julgamento;
2. **Estruturação do Artigo Científico e GitPage:** Consolidação das seções das Fases 1 e 2 no modelo SBC e publicação das páginas documentais;
3. **Governança e Medição Contínua (PSM/CID):** Acompanhamento cumulativo das horas dedicadas, custos de referência e evolução da aderência ao cronograma das milestones.

---

## 2. Measurement Constructs da Fase 2 (Template PSM/CID — Aula 09, p. 19)

Em conformidade estrita com o modelo da norma **ISO/IEC 15939** e com o template metodológico adotado na disciplina (AULA 09, p. 19), a equipe estruturou um *Measurement Construct* formal para cada uma das três categorias de informação exigidas na especificação, parametrizados para o ciclo da Fase 2 e para o balanço acumulado da Entrega 1:

### 2.1. Construct 1 — Recursos e Custos: Análise de Desvio e Custo Acumulado

| Elemento do Construct | Especificação Normativa (Fase 2 / Entrega 1) |
| :--- | :--- |
| **Categoria de Informação** | Recursos e Custos (*Resources and Cost*) |
| **Necessidade de Informação** | Avaliar o desvio do esforço real da Fase 2 em relação ao estimado, monitorar o custo financeiro acumulado da Entrega 1 (Fases 1 e 2) e verificar a convergência da carga horária individual. |
| **Conceito Mensurável** | Desvio de esforço pós-calibração, custo financeiro acumulado da Entrega 1 e variância da carga de trabalho entre os integrantes. |
| **Medidas Base** | 1. `Horas Estimadas da Fase 2 (h)`: esforço planejado nas 12 issues da milestone Fase 2.<br/>2. `Horas Reais da Fase 2 (h)`: esforço efetivo discriminado por integrante no fechamento das issues.<br/>3. `Custo Real da Fase 1 (R$)`: linha de base consolidada em R$ 292,50 (6,50 h).<br/>4. `Valor-Hora (R$)`: taxa de referência nacional (R$ 45,00/h Júnior CLT via Novo CAGED). |
| **Medidas Derivadas** | • Desvio de Esforço F2 (%) = [(Horas Reais F2 - Horas Estimadas F2) / Horas Estimadas F2] × 100<br/>• Custo Acumulado da Entrega 1 (R$) = Custo Real Fase 1 + (Horas Reais Fase 2 × R$ 45,00)<br/>• Disparidade Individual (%) = Max(Esforço %) - Min(Esforço %) entre os seis integrantes |
| **Indicador e Critério de Decisão** | Desvio de esforço da Fase 2 contido em ±20% (validando a eficácia da margem de calibração adotada na Decisão 5). Custo financeiro total acumulado da Entrega 1 dentro do teto orçamentário previsto. Disparidade de esforço individual decrescendo em relação à Fase 1. |

### 2.2. Construct 2 — Calendário e Progresso: Prontidão do PC1 e Fechamento da E1

| Elemento do Construct | Especificação Normativa (Fase 2 / Entrega 1) |
| :--- | :--- |
| **Categoria de Informação** | Calendário e Progresso (*Schedule and Progress*) |
| **Necessidade de Informação** | Monitorar a taxa de conclusão das issues da Fase 2 frente a dois marcos temporais inegociáveis: a apresentação do Ponto de Controle 1 (21/10/2026) e a submissão da Release v1.0-E1 no Moodle (26/10/2026). |
| **Conceito Mensurável** | Ritmo de entrega, prontidão para apresentação oral e pontualidade na milestone final da Entrega 1. |
| **Medidas Base** | 1. `Total de Tarefas da Fase 2`: 12 issues cadastradas na milestone Fase 2.<br/>2. `Tarefas Concluídas`: issues fechadas via pull request revisado e integrado.<br/>3. `Tarefas Críticas do PC1`: issues essenciais para a apresentação oral de 21/10.<br/>4. `Data de Submissão`: data efetiva da entrega no Moodle frente ao prazo de 26/10. |
| **Medidas Derivadas** | • Progresso da Fase 2 (%) = (Tarefas Concluídas / 12) × 100<br/>• Prontidão para o PC1 (%) = (Tarefas Críticas do PC1 Prontas / Total Críticas) × 100<br/>• Aderência Geral da Fase 2 (%) = (Tarefas no Prazo / 12) × 100 |
| **Indicador e Critério de Decisão** | Prontidão do PC1 em 100% com antecedência mínima de 24 horas (20/10) para realização de ensaio geral cronometrado. Aderência geral da Fase 2 mantida em 100,0%. Nenhuma issue bloqueadora pendente no dia da submissão da release. |

### 2.3. Construct 3 — Desempenho dos Processos: Calibração e Eficácia da Revisão

| Elemento do Construct | Especificação Normativa (Fase 2 / Entrega 1) |
| :--- | :--- |
| **Categoria de Informação** | Desempenho dos Processos (*Process Performance*) |
| **Necessidade de Informação** | Avaliar se as lições aprendidas na Fase 1 resultaram em melhoria da acurácia das estimativas e se o processo de governança manteve 100% de conformidade nas revisões de pull request. |
| **Conceito Mensurável** | Ganho de precisão no planejamento de horas e rigor na revisão por pares. |
| **Medidas Base** | 1. `Acurácia da Fase 1`: 185,7% (linha de base da Fase 1).<br/>2. `Acurácia da Fase 2`: relação percentual entre horas reais e estimadas nas issues fechadas da Fase 2.<br/>3. `Total de Pull Requests da Fase 2`: PRs abertos para os artefatos da Fase 2.<br/>4. `PRs com Revisão Aprovada`: PRs aprovados por integrante não autor antes da integração. |
| **Medidas Derivadas** | • Ganho de Acurácia (%) = \|Acurácia Fase 1 - 100%\| - \|Acurácia Fase 2 - 100%\|<br/>• Taxa de Revisão por Pares (%) = (PRs com Revisão Aprovada / Total de PRs) × 100 |
| **Indicador e Critério de Decisão** | Ganho de acurácia positivo (> 0), indicando aproximação da faixa ideal (75% a 125%). Manutenção de 100,0% dos pull requests aprovados por pares antes do merge (regra inegociável do `CONTRIBUTING.md`). |

---

## 3. Medições Registradas da Fase 2

Os dados primários coletados pelo coletor automatizado `scripts/coleta_psm.py` a partir da API do GitHub registram o seguinte estado das três categorias da Fase 2:

### 3.1. Medições de Recursos e Custos da Fase 2

| Fase | Total de Issues | Horas Estimadas (h) | Horas Reais (h) | Custo Estimado (R$) | Custo Real (R$) | Estado da Medição |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Fase 2** | 18 | 28,00 | 18,50 | R$ 1.260,00 | R$ 832,50 | Em andamento (6 issues concluídas) |
| **Entrega 1 (Acumulado F1 + F2)** | 35 | 83,25 | 80,66 | R$ 3.746,25 | R$ 3.629,70 | Monitoramento contínuo |

*Tabela 1: Recursos e custos da Fase 2 e acumulado da Entrega 1 (Fonte: dados/gestao/01_recursos_e_custos_fases.csv).*

### 3.2. Medições de Calendário e Progresso da Fase 2

| Fase | Total de Issues | Concluídas | Em Andamento | Progresso (%) | No Prazo | Em Atraso | Aderência ao Prazo (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Fase 2** | 18 | 6 | 12 | 33,3% | 16 | 2 | 88,9% |
| **Entrega 1 Geral** | 35 | 23 | 12 | 65,7% | 21 | 14 | 60,0% |

*Tabela 2: Calendário e progresso da Fase 2 e consolidação da Entrega 1 (Fonte: dados/gestao/02_calendario_e_progresso_fases.csv).*

### 3.3. Medições de Desempenho dos Processos da Fase 2

| Métrica de Processo | Fase 1 (Linha de Base) | Fase 2 (Meta Calibrada) | Fase 2 (Real Observado) | Conformidade |
| :--- | :---: | :---: | :---: | :---: |
| **Acurácia de Estimativa** | 112,5% | Faixa de 80% a 120% | 66,1% | Em calibração (6 issues) |
| **Taxa de Revisão por Pares** | 100,0% | 100,0% | 100,0% | 100% de conformidade |
| **Lead Time Médio** | 1,23 dia(s) | < 3,00 dias | 1,44 dia(s) | Dentro do limite ágil |

*Tabela 3: Desempenho dos processos na Fase 2 (Fonte: dados/gestao/03_desempenho_processos_fases.csv).*

---

## 4. Análise Comparativa Direta: Fase 1 versus Fase 2

Em cumprimento ao terceiro critério de pronto da Issue #31, a tabela abaixo confronta os indicadores consolidados da equipe entre as duas primeiras fases do projeto, evidenciando o aprendizado operacional:

| Indicador de Gestão | Fase 1 (Requisitos & Setup) | Fase 2 (Especificação GQM) | Balanço Consolidado da Entrega 1 | Tendência e Interpretação |
| :--- | :---: | :---: | :---: | :--- |
| **Total de Issues Alocadas** | 17 issues | 18 issues | **35 issues técnicas e de gestão** | Distribuição equilibrada de escopo entre fases. |
| **Horas Estimadas Totais** | 55,25 h | 28,00 h | **83,25 h planejadas** | Planejamento técnico estruturado para a Entrega 1. |
| **Horas Reais Acumuladas** | 62,16 h | 18,50 h | **80,66 h executadas** | Fase 1 100% concluída; Fase 2 com 6 issues fechadas. |
| **Custo Equivalente (R$ 45/h)** | R$ 2.797,20 | R$ 832,50 | **R$ 3.629,70 investidos** | Orçamento sob controle frente à taxa de mercado CLT. |
| **Aderência aos Prazos** | 29,4% (ajustes pós-review) | 88,9% | **88,9% no prazo na F2** | Melhora expressiva na pontualidade na Fase 2. |
| **Taxa de Revisão por Pares** | 100,0% | 100,0% | **100,0% dos PRs revisados** | Rigor inegociável mantido em todos os merges. |
| **Foco Principal do Esforço** | Requisitos, normas e governança | GQM, métricas, artigo e apresentação | **Ciclo completo da Entrega 1** | Transição fluida entre definição e especificação. |

### Acompanhamento Contínuo da Fase 2:
Como a **Fase 2 encontra-se em andamento ativo** e os membros da equipe estão desenvolvendo as tarefas técnicas de especificação GQM e seções do artigo nas respectivas branches de trabalho, as medições de esforço real, acurácia e balanceamento de carga permanecem em apuração contínua.

A análise consolidada e as conclusões definitivas sobre o desempenho da equipe serão registradas no fechamento da **Entrega 1 (Release v1.0-E1)**, após a conclusão de todas as issues da milestone e a reexecução do script coletor (`scripts/coleta_psm.py`). O presente documento estabelece a estrutura de medição (esqueleto normativo, measurement constructs e metas) e as decisões de gestão adotadas até o momento.

---

## 5. Decisões de Gestão da Fase 2 (Premissa 3)

Em continuidade às decisões registradas na Fase 1 (Decisões 1 a 4), a equipe formalizou as seguintes ações de gestão tomadas a partir das medições:

### Decisão 5: Calibração de Estimativas a partir da Linha de Base da Fase 1
* **Contexto e Causa:** A constatação na Fase 1 de que discussões metodológicas e normativas consomem tempo significativo de alinhamento não antecipado nas estimativas preliminares.
* **Decisão:** Incorporar uma margem técnica de 20% nas estimativas das tarefas conceituais de GQM e redação do artigo na Fase 2.
* **Impacto:** Eliminação do risco de subestimação sistemática de tarefas e maior aderência aos prazos da milestone.

### Decisão 6: Adoção de Stacked Pull Requests para Evitar Bloqueios de Revisão
* **Contexto e Causa:** A dependência direta entre artefatos sequenciais (o relatório da Fase 1 dependia do script; os apêndices do artigo dependiam do relatório; o relatório da Fase 2 dependia das seções anteriores).
* **Decisão:** Implementar o fluxo de *Stacked PRs* no GitHub, permitindo que os membros continuem desenvolvendo novas tarefas em branches encadeadas sem aguardar o merge imediato na branch `main`.
* **Impacto:** Zero tempo ocioso entre a conclusão de uma tarefa e o início da seguinte, permitindo que as revisões ocorram em lote coordenado.

### Decisão 7: Congelamento Técnico e Ensaio com Cronômetro para o PC1 (21/10)
* **Contexto e Causa:** A necessidade de apresentar as Fases 1 e 2 presencialmente em uma janela restrita de 10 a 15 minutos com seis integrantes.
* **Decisão:** Fixar o tempo de fala de cada membro em rigorosos 2 minutos (meta de 12 minutos cravados no ensaio geral), estabelecendo a ordem fixa de apresentação: Abertura/Gestão (Maria Eduarda) ➔ Fase 1 (Davi, Letícia e Gabriel) ➔ Fase 2 (Christopher e Luiz Henrique).
* **Impacto:** Cumprimento rigoroso da janela temporal sem cortes e garantia de que todos os integrantes demonstrem domínio técnico perante a professora.

---

## 6. Rastreabilidade com os Dados Primários (Premissa 5)

Todos os indicadores apresentados neste relatório são respaldados pelos artefatos e dados primários versionados no repositório:
* **Script de Coleta Automatizada:** [`scripts/coleta_psm.py`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/scripts/coleta_psm.py)
* **Histórico Bruto da API (JSON):** [`dados/gestao/raw_github_data.json`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/dados/gestao/raw_github_data.json)
* **Relatório da Fase 1 (Linha de Base):** [`docs/gestao/relatorios/relatorio-psm-fase-1.md`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/docs/gestao/relatorios/relatorio-psm-fase-1.md)
* **Apêndices do Artigo (Contribuição e IA):** [`artigo/contribuicao-e-ia.md`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/artigo/contribuicao-e-ia.md)

---

## 7. Declaração de Uso de Inteligência Artificial (Critério F2-C9)

* **Ferramenta utilizada:** Antigravity / Gemini 3.8.
* **Finalidade no relatório:** Apoio na estruturação dos Measurement Constructs da Fase 2 no template da Aula 09 (p. 19), formatação das tabelas de dados e consolidação das decisões de gestão.
* **Conferência crítica:** Os parâmetros e indicadores foram auditados contra os CSVs gerados da API do GitHub, garantindo conformidade com a ISO/IEC 15939 e as premissas da disciplina. Nenhuma imagem com texto sobreposto ou emoji foi utilizada.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 18/10/2026 | Estruturação inicial do Relatório PSM/CID da Fase 2 (esqueleto normativo, measurement constructs e decisões de gestão preliminares) | [Maria Eduarda](https://github.com/eduarda-ogomes) | - |
| 1.1 | 19/10/2026 | Atualização das medições em andamento da Fase 2 (6 issues concluídas, 18,5h reais) e comparativo com a Fase 1 | [Maria Eduarda](https://github.com/eduarda-ogomes) | - |
