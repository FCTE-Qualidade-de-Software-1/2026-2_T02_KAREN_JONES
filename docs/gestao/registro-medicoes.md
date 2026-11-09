---
id: registro-medicoes
title: Registro de Medições e Decisões
sidebar_label: Registro de Medições
sidebar_position: 4
toc_min_heading_level: 2
toc_max_heading_level: 3
description: Registro contínuo de medições periódicas, diagnóstico causal de atrasos por dependências de tarefas e decisões formais de gestão (PSM/CID).
---

import Link from '@docusaurus/Link';

# Registro de Medições e Decisões de Gestão

Este documento consolida o **registro contínuo e cronológico de medições**, as **análises causais de desvio** e as **decisões formais de gestão** adotadas pela equipe Karen Jones ao longo das quatro fases do projeto de avaliação de qualidade do **Excalidraw**.

O acompanhamento estabelece a interpretação periódica dos indicadores de gestão e a formalização das medidas corretivas adotadas, conectando-se diretamente aos critérios e conceitos definidos no [Plano de Medição PSM](plano-medicao-psm.md). Os números brutos e gráficos consolidados estão disponíveis no [Painel de Medição PSM](painel-psm.md).

---

## 1. Ciclo de Medição e Cronograma de Leituras

Para monitorar tempestivamente o fluxo de trabalho e evitar acúmulos na véspera das entregas oficiais, a equipe estabeleceu um ciclo de **quatro leituras formais**:

<p className="tabela-titulo">Tabela 1: Cronograma do ciclo de medições periódicas da equipe</p>

| Leitura | Data | Marco do Projeto | Escopo Analisado | Objetivo Principal | Status |
| :---: | :---: | :--- | :--- | :--- | :---: |
| **Medição 0** | 04/11/2026 | Linha de Base / Fechamento da Entrega 1 | Fases 1 e 2 consolidadas | Analisar retrospectivamente o aprendizado da E1, a acurácia de custos e o impacto das dependências entre tarefas. | **Concluída** |
| **Medição 1** | 11/11/2026 | Ponto de Controle Intermediário da Fase 3 | Fase 3 em andamento | Avaliar a aderência aos prazos parciais de projeto (métodos de teste, formulários e roteiros) e destravamento de dependências. | *Programada* |
| **Medição 2** | 18/11/2026 | Conclusão da Fase 3 e Validação da Fase 4 | Fase 3 e início da Fase 4 | Checar prontidão dos instrumentos de teste antes da coleta em campo e calibrar alocação de esforço. | *Programada* |
| **Medição 3** | 22/11/2026 | Fechamento da Entrega 2 | Fases 3 e 4 consolidadas | Avaliar execução completa dos testes, fechamento do artigo SBC e consolidação final do orçamento. | *Programada* |

<p className="tabela-fonte">Fonte: [Maria Eduarda](https://github.com/eduarda-ogomes), 2026.</p>

---

## 2. Medição 0: Linha de Base da Entrega 1 (04/11/2026)

### 2.1. Análise Causal dos Atrasos de Cronograma: O Impacto das Dependências

A apuração quantitativa da Entrega 1 revelou que, no momento do encerramento do prazo original da Entrega 1, a equipe havia atingido **100% de progresso na Fase 1** e **92,6% na Fase 2 (25 de 27 issues)**, alcançando a conclusão integral de **100% (44 de 44 issues)** após o fechamento das tarefas complementares [#28](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/28) e [#30](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/30) auditadas em 05/11/2026. A **taxa de aderência aos prazos internos**, por sua vez, foi de **29,4% na Fase 1** e **44,4% na Fase 2** (consolidando 38,6% na Entrega 1).

A análise qualitativa e a auditoria de datas do repositório demonstraram que a causa primária desse comportamento não foi falta de esforço ou subestimação de horas, mas sim a **gestão de dependências entre tarefas**:

1. **Gargalo por Bloqueios em Cadeia na Fase 1:**
   * Na Fase 1, as tarefas iniciais de escopo ([#13](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/13)), partes interessadas ([#6](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/6)) e modelo de qualidade ([#7](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/7)) constituíam pré-requisitos lógicos para praticamente todos os demais artefatos da disciplina.
   * Quando essas issues de cabeceira foram atribuídas a integrantes que possuíam janelas de disponibilidade mais concentradas no meio da semana, os demais membros da equipe ficaram temporariamente ociosos ou impedidos de avançar em suas branches.
   * Como resultado direto desse encadeamento, 12 das 17 issues da Fase 1 foram finalizadas em lote em 19/10/2026 (véspera da entrega), fazendo com que o *Cycle Time* aparentasse ser curto (1,23 dias), mas gerando uma sobrecarga operacional crítica nas revisões de PRs.

2. **Mitigação Parcial e Agrupamento na Fase 2:**
   * Na Fase 2, a equipe adotou a estratégia de agrupar blocos inteiros de tarefas interdependentes sob a responsabilidade de um mesmo integrante (por exemplo, as fichas e metas GQM de [#52](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/52) a [#55](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/55) atribuídas ao Christopher).
   * Essa prática reduziu o tempo de espera entre branches e eliminou pontos de bloqueio externo, elevando a aderência ao prazo de 29,4% para 44,4% (+15 p.p.).

3. **Decisão Operacional para as Fases 3 e 4:**
   * Para institucionalizar esse aprendizado, a equipe formalizou a política de [Priorização no GitHub Project](priorizacao-issues.md). As tarefas passam a ser classificadas com **Prioridade Alta** (bloqueiam 15+ issues), **Média** (5 a 14) ou **Normal** (menos de 5), garantindo que nós críticos sejam iniciados no primeiro dia do ciclo e nunca fiquem retidos.

---

### 2.2. Balanço Orçamentário e Equilíbrio de Participação

1. **Estabilidade de Esforço e Custo:**
   * O esforço real total da Entrega 1 foi de **114,31 h** (equivalente a R$ 5.143,95), frente a um esforço planejado de **116,00 h** (R$ 5.220,00), resultando em uma acurácia global consolidada de **98,5%** (dentro da faixa ideal de 80% a 120%).
   * A margem de calibração adicionada na Fase 2 compensou com sucesso a leve subestimação da Fase 1 (onde foram consumidas 57,91 h reais para 53,50 h previstas).

2. **Equilíbrio Individual na Entrega:**
   * Conforme demonstrado no [Painel de Medição PSM](painel-psm.md), a participação de todos os seis membros situou-se entre **8,67% e 24,93% do esforço acumulado**, respeitando a meta de governança do Construct 2 (entre 8% e 30%).
   * A divisão funcional em dois subgrupos (F1/F3 e F2/F4) funcionou adequadamente: os membros mais demandados na Fase 1 tiveram sua carga aliviada na Fase 2, e vice-versa.

---

### 2.3. Avaliação dos Critérios de Decisão da Entrega 1

Conforme definido no [Plano de Medição PSM](plano-medicao-psm.md), a equipe avaliou os seis critérios de decisão estabelecidos para a Linha de Base ao encerramento da Entrega 1:

<p className="tabela-titulo">Tabela 2: Avaliação dos critérios de decisão da Linha de Base (Entrega 1)</p>

| Critério de Decisão (Constructs PSM) | Meta Estabelecida | Resultado Observado | Situação | Análise e Encaminhamento |
| :--- | :---: | :---: | :---: | :--- |
| **Desvio de Esforço Orçamentário** | Dentro de $\pm 20\%$ | **-1,5%** (114,31h reais vs. 116,00h est.) | **Atendido** | Excelente precisão orçamentária; margem de calibração equilibrou a Entrega 1. |
| **Disparidade de Esforço Individual** | Redução da dispersão | De 29,35 p.p. para **27,48 p.p.** | **Atendido** | Todos os membros entre 8,67% e 24,93% do esforço acumulado (faixa ideal: 8% a 30%). |
| **Ganho de Acurácia de Estimativa** | Ganho positivo ($> 0$) | -1,6 p.p. (F1: 108,2%; F2: 90,2%) | **Não atendido** | Ambas as fases mantiveram-se na faixa ideal (80% a 120%), com o consolidado convergindo para 98,5%. |
| **Aderência aos Prazos Internos** | 100,0% no prazo | **38,6%** (29,4% na F1; 44,4% na F2) | **Não atendido** | Atrasos causados por bloqueios em cadeia; motivou a política de [Priorização no Project](priorizacao-issues.md). |
| **Taxa de Revisão por Pares (PRs)** | 100,0% aprovados | **46,7%** (14 de 30 PRs) | **Não atendido** | Revisões informais não deixaram rastro na API; Decisão D5 exige registro formal de aprovação no GitHub. |
| **Issues Pendentes na Submissão** | Zero issues abertas | [#28](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/28) e [#30](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/30) abertas | **Não atendido** | Issues fechadas em 05/11; submissão no Moodle realizada via release [`v0.1`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/releases/tag/v0.1). Saneado na Decisão D6. |

<p className="tabela-fonte">Fonte: [Maria Eduarda](https://github.com/eduarda-ogomes), com base na coleta de 05/11/2026 e no histórico de fechamento de issues, 2026.</p>

---

### 2.4. Registro Consolidado de Decisões de Gestão (D1 a D6)

<p className="tabela-titulo">Tabela 3: Registro histórico de decisões de gestão adotadas na Entrega 1</p>

| ID | Marco / Fase | Problema / Oportunidade Detectada | Decisão de Gestão Adotada | Impacto Observado / Esperado |
| :---: | :---: | :--- | :--- | :--- |
| **D1** | Fase 1 | Alto acoplamento entre requisitos e projeto causava sobreposição de papéis. | Divisão da equipe em dois subgrupos técnicos (F1/F3 e F2/F4) e consolidação do esforço por Entrega. | Equilíbrio individual alcançado entre 8,67% e 24,93% no consolidado da Entrega 1. |
| **D2** | Fase 1 | Risco de discrepâncias manuais e inconsistência de dados no GitPage. | Automação da coleta via `scripts/coleta_psm.py` e integração contínua via GitHub Actions. | Coleta 100% automatizada e auditável a partir da API oficial do GitHub. |
| **D3** | Fase 1 | Tarefas desenvolvidas em paridade distorciam a contagem de esforço individual. | Adoção do rateio explícito no corpo da issue (`@usuario1: N, @usuario2: M`). | Atribuição exata de esforço para o apêndice de contribuição do artigo SBC. |
| **D4** | Fase 2 | Leve subestimação de esforço na Fase 1 (+8,2%) por debates metodológicos. | Aplicação de margem de calibração de 20% no planejamento de tarefas complexas (GQM). | Acurácia orçamentária convergente em 98,5% na Entrega 1 (114,31h / 116,00h). |
| **D5** | Fase 2 | Branches dependentes travadas e revisões informais sem registro no GitHub API (taxa formal apurada de 46,7%). | Utilização de *Stacked PRs* e exigência estrita de aprovação formal via GitHub antes do merge. | Redução do tempo ocioso entre branches e meta de 100% de aprovação formal registrada para a Entrega 2. |
| **D6** | Transição E2 | Issues de fechamento da Fase 2 e planejamento da Fase 3 com metadados parciais. | Saneamento das issues da Fase 2, vinculação de assignees na Fase 3 e priorização por dependência. | Retorno da governança para 100% e início antecipado das tarefas de bloqueio. |

<p className="tabela-fonte">Fonte: [Maria Eduarda](https://github.com/eduarda-ogomes), 2026.</p>

---

## 3. Medição 1: Ponto de Controle Intermediário da Fase 3 (11/11/2026)

> **Data Prevista de Coleta:** 11/11/2026  
> **Responsável pela Coleta:** [Maria Eduarda](https://github.com/eduarda-ogomes)  
> **Revisor Designado:** [Christopher](https://github.com/wChrstphr)

### 3.1. Dados Quantitativos da Coleta

<p className="tabela-titulo">Tabela 4: Indicadores preliminares apurados na Medição 1</p>

| Indicador | Meta / Esperado | Valor Coletado | Situação |
| :--- | :---: | :---: | :---: |
| Issues Concluídas na Fase 3 | Pelo menos 10 de 19 | *A coletar em 11/11* | — |
| Progresso da Fase 3 (%) | Pelo menos 50,0% | *A coletar em 11/11* | — |
| Aderência aos Prazos Intermediários | Pelo menos 70,0% | *A coletar em 11/11* | — |
| Horas Reais Consumidas (h) | Aprox. 22,0 h | *A coletar em 11/11* | — |
| Governança de Preenchimento | 100,0% | *A coletar em 11/11* | — |

### 3.2. Análise Crítica e Gatilhos de Ação
* **Verificação de Gargalos:** Avaliar se as issues de Prioridade Alta da Fase 3 ([#94](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/94) e [#95](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/95)) foram homologadas sem travar a elaboração dos questionários e roteiros.
* **Gatilho de Decisão:** Caso o progresso em 11/11 esteja abaixo de 50%, convocar reunião extraordinária no Discord para redistribuição imediata de tarefas bloqueadas.

---

## 4. Medição 2: Conclusão da Fase 3 e Validação da Fase 4 (18/11/2026)

> **Data Prevista de Coleta:** 18/11/2026  
> **Responsável pela Coleta:** [Maria Eduarda](https://github.com/eduarda-ogomes)  
> **Revisor Designado:** [Christopher](https://github.com/wChrstphr)

### 4.1. Dados Quantitativos da Coleta

<p className="tabela-titulo">Tabela 5: Indicadores apurados no fechamento da Fase 3</p>

| Indicador | Meta / Esperado | Valor Coletado | Situação |
| :--- | :---: | :---: | :---: |
| Conclusão dos Artefatos de Projeto | 19 de 19 issues | *A coletar em 18/11* | — |
| Aderência ao Cronograma da Fase 3 | Pelo menos 80,0% | *A coletar em 18/11* | — |
| Prontidão para Execução da Fase 4 | Ambientes e roteiros 100% testados | *A coletar em 18/11* | — |
| Esforço Total da Fase 3 | Até 45,50 h | *A coletar em 18/11* | — |

### 4.2. Decisões de Transição para a Execução em Campo
* Registro das medidas corretivas para o início da coleta de dados de usabilidade e desempenho no Excalidraw durante a Fase 4.

---

## 5. Medição 3: Fechamento da Entrega 2 (22/11/2026)

> **Data Prevista de Coleta:** 22/11/2026  
> **Responsável pela Coleta:** [Maria Eduarda](https://github.com/eduarda-ogomes)  
> **Revisor Designado:** [Christopher](https://github.com/wChrstphr)

### 5.1. Dados Quantitativos da Coleta

<p className="tabela-titulo">Tabela 6: Indicadores finais apurados no fechamento da Entrega 2</p>

| Indicador | Meta / Esperado | Valor Coletado | Situação |
| :--- | :---: | :---: | :---: |
| Conclusão dos Testes e Avaliações | 100% das issues da E2 | *A coletar em 22/11* | — |
| Acurácia Orçamentária da E2 | Entre 80% e 120% | *A coletar em 22/11* | — |
| Equilíbrio Individual Acumulado | Faixa de 8% a 30% por membro | *A coletar em 22/11* | — |
| Taxa de Revisão por Pares (PRs) | 100% aprovados formalmente | *A coletar em 22/11* | — |

---

## Referências

> <Link id="ref-1">1.</Link> CARD, David et al. **Practical Software and Systems Measurement (PSM): A Foundation for Objective Project Management**. Version 4.0d. PSM Support Center, 2021. Disponível em: [https://psmsc.com](https://psmsc.com). Acesso em: 18 out. 2026.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 07/11/2026 | Criação do Registro de Medições e Decisões com Medição 0 (Linha de base E1), análise causal de dependência de tarefas, decisões D1-D6 e templates das medições 1 e 2 | [Maria Eduarda](https://github.com/eduarda-ogomes) | [Christopher](https://github.com/wChrstphr) |
| 1.1 | 08/11/2026 | Alinhamento do gatilho de 50%, Medição 3 em 22/11, esclarecimento do progresso da F2, Construct 2 e autoria das fontes | [Maria Eduarda](https://github.com/eduarda-ogomes) | [Christopher](https://github.com/wChrstphr) |
