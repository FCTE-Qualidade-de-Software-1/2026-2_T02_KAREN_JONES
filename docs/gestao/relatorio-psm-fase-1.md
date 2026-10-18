---
id: relatorio-psm-fase-1
title: Relatório PSM/CID da Fase 1
sidebar_label: Relatório PSM/CID (Fase 1)
sidebar_position: 1
description: Medições quantitativas, measurement constructs, interpretação e decisões de gestão da Fase 1 (ISO/IEC 15939 e PSM/CID).
---

# Relatório de Gestão com Métricas PSM/CID — Fase 1

Este documento consolida as medições, indicadores e decisões de gestão da **Fase 1** do projeto de avaliação da qualidade do software **Excalidraw**, com base nas normas **ISO/IEC 25040**, **ISO/IEC 15939** e no modelo **PSM/CID (Practical Software Measurement / Practical Software and Systems Measurement, CID 2021)**.

O relatório atende expressamente à **Premissa 3** (obrigatoriedade de registro contínuo de medições, interpretação e decisões de gestão) e à **Premissa 5** (rastreabilidade completa e auditabilidade baseada em dados primários versionados).

---

## 1. Organização da Equipe e Estratégia de Trabalho

Para garantir foco técnico e paralelismo sem sobreposição de tarefas ou bloqueios em cadeia, a equipe de seis integrantes foi estruturada em **dois subgrupos de três membros**, com responsabilidades técnicas distribuídas nas quatro fases do processo de avaliação:

| Subgrupo | Integrantes | Fases Técnicas Principais | Escopo de Atuação |
| :--- | :--- | :--- | :--- |
| **Subgrupo F1/F3** | Davi Pierre, Gabriel Monteiro, Letícia de Carvalho | **Fase 1** (Requisitos) e **Fase 3** (Projeto) | Definição de propósito, partes interessadas, modelo de qualidade, seleção de características, métodos de teste, recursos e ambiente de avaliação. |
| **Subgrupo F2/F4** | Christopher, Luiz Henrique Soares, Maria Eduarda | **Fase 2** (Especificação) e **Fase 4** (Execução) | Definição de metas e questões GQM, hipóteses, métricas, níveis de pontuação, coleta prática no Excalidraw, análise estatística e proposição de melhorias. |

### Atividades Transversais e Integração

As frentes de **Gestão do Projeto (PSM/CID)**, **Artigo Científico (SBC)** e **Apresentações dos Pontos de Controle (PC1 a PC4)** são transversais e contam com a participação direta de ambos os subgrupos:

* **Gestão e Rastreabilidade:** Conduzida com governança por issues, formulários padronizados e script automatizado em Python conectado à API do GitHub.
* **Artigo da SBC:** Redação compartilhada com seções específicas alocadas para cada integrante, incluindo a tabela de contribuição individual calculada com base nas horas reais registradas.
* **Pontos de Controle:** Apresentações com tempo de fala distribuído entre os seis integrantes.

---

## 2. Parâmetros Metodológicos e Linha de Base Financeira

Para a valoração financeira do esforço dispendido pela equipe, foi definida uma taxa horária de referência em `scripts/config.json`:

* **Valor-Hora de Referência:** R$ 45,00
* **Moeda:** Real Brasileiro (BRL)
* **Justificativa Metodológica:** Remuneração média nacional para Analista de Sistemas / Engenheiro de Software Júnior sob regime formal CLT (CBO 2124-05, Fonte: Novo CAGED / Ministério do Trabalho e Emprego, base de 160h a 200h mensais). Essa taxa é adotada como *proxy* de mercado para quantificar o custo do esforço técnico e de gestão empregado no projeto.

---

## 3. Categoria 1: Recursos e Custos (*Resources and Cost*)

### 3.1. Measurement Construct — Recursos e Custos

| Elemento do Construct | Especificação |
| :--- | :--- |
| **Categoria de Informação** | Recursos e Custos (*Resources and Cost*) |
| **Necessidade de Informação** | Avaliar se o esforço empregado pela equipe e o custo financeiro estimado permanecem dentro do planejado e se a carga de trabalho está equilibrada entre os integrantes. |
| **Conceito Mensurável** | Esforço de trabalho, custo financeiro equivalente e distribuição individual de carga. |
| **Medidas Base** | 1. `Horas Estimadas (h)`: valor planejado informado na abertura da issue.<br/>2. `Horas Reais (h)`: esforço apurado no encerramento da issue discriminado por integrante.<br/>3. `Valor-Hora (R$)`: taxa horária de referência configurada (R$ 45,00/h). |
| **Medidas Derivadas** | • Custo Planejado (R$) = Somatório das Horas Estimadas × Valor-Hora<br/>• Custo Real (R$) = Somatório das Horas Reais × Valor-Hora<br/>• Esforço Individual (%) = (Horas Reais do Integrante / Total de Horas Reais da Equipe) × 100 |
| **Indicador e Critério de Decisão** | Comparação entre horas estimadas e realizadas por fase e verificação da distribuição percentual. Desvios acumulados superiores a 25% entre planejado e realizado ou desbalanceamento extremo exigem redistribuição de tarefas na fase seguinte. |

### 3.2. Medições Obtidas na Fase 1

Os dados primários coletados pelo script automatizado a partir dos registros do GitHub consolidam o seguinte balanço de recursos da Fase 1:

| Fase | Horas Estimadas (h) | Horas Reais (h) | Custo Estimado (R$) | Custo Real (R$) | Variação de Esforço (%) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Fase 1** | 3,50 | 6,50 | R$ 157,50 | R$ 292,50 | +85,7% |

*Tabela 1: Recursos e custos da Fase 1 (Fonte: dados/gestao/01_recursos_e_custos_fases.csv).*

![Recursos e Custos por Fase](/img/gestao/01_recursos_e_custos_fases.png)

*Figura 1: Comparativo entre horas e custos estimados versus realizados por fase do projeto.*

### 3.3. Contribuição Individual e Equilíbrio da Carga de Trabalho

A transparência da contribuição individual (exigência do critério **AG-C5**) é monitorada por meio do cruzamento entre issues atribuídas, horas reais dedicadas, commits e pull requests:

| Integrante | Login GitHub | Subgrupo | Issues Atribuídas | Horas Est. (h) | Horas Reais (h) | Custo Real (R$) | Commits / PRs | Esforço Real (%) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Christopher | `wChrstphr` | F2/F4 | 5 | 0,75 | 2,50 | R$ 112,50 | 0 / 1 | 38,46% |
| Davi Pierre | `DaviPierre` | F1/F3 | 6 | 0,00 | 0,00 | R$ 0,00 | 1 / 1 | 0,00% |
| Gabriel Monteiro | `GabrielSMonteiro` | F1/F3 | 6 | 0,00 | 0,00 | R$ 0,00 | 9 / 1 | 0,00% |
| Letícia de Carvalho | `LeticiaSantosss` | F1/F3 | 6 | 0,00 | 0,00 | R$ 0,00 | 1 / 1 | 0,00% |
| Luiz Henrique Soares | `luizh-gsoares` | F2/F4 | 6 | 0,00 | 0,00 | R$ 0,00 | 0 / 0 | 0,00% |
| Maria Eduarda | `eduarda-ogomes` | F2/F4 | 6 | 2,75 | 4,00 | R$ 180,00 | 0 / 0 | 61,54% |
| **Total** | — | — | **35** | **3,50** | **6,50** | **R$ 292,50** | **11 / 4** | **100,00%** |

*Tabela 2: Distribuição de esforço e contribuição individual (Fonte: dados/gestao/04_contribuicao_individual.csv).*

![Contribuição Individual](/img/gestao/03_contribuicao_individual.png)

*Figura 2: Distribuição percentual do esforço real apurado entre os membros da equipe.*

### 3.4. Interpretação — Análise de Estimativa (Linha de Base) e Performance

1. **Linha de Base Financeira e de Esforço:** A Fase 1 representa a implantação inicial do projeto. As primeiras 6,5 horas de trabalho real concentraram-se na estruturação da infraestrutura de governança (Issue #4, envolvendo a configuração de templates, critérios de avaliação e guia de contribuição) e no desenvolvimento da ferramenta automatizada de métricas PSM/CID (Issue #19).
2. **Esforço Inicial Concentrado:** Como o Subgrupo F2/F4 assumiu a liderança técnica da automação da gestão nas primeiras 48 horas, o percentual de esforço temporário reflete esse arranque inicial (Maria Eduarda com 4,0h e Christopher com 2,5h). Conforme os membros do Subgrupo F1/F3 finalizarem e fecharem as issues técnicas da Fase 1 (Issues #9, #10, #11, #12, #13, #14, #15 e #16), a distribuição convergirá para a equidade planejada em torno de 16,6% por integrante.

---

## 4. Categoria 2: Calendário e Progresso (*Schedule and Progress*)

### 4.1. Measurement Construct — Calendário e Progresso

| Elemento do Construct | Especificação |
| :--- | :--- |
| **Categoria de Informação** | Calendário e Progresso (*Schedule and Progress*) |
| **Necessidade de Informação** | Acompanhar o cumprimento dos prazos das entregas parciais e o ritmo de fechamento das tarefas frente às datas dos Pontos de Controle. |
| **Conceito Mensurável** | Progresso das atividades e aderência ao cronograma das milestones. |
| **Medidas Base** | 1. `Total de Tarefas`: número de issues vinculadas à milestone da fase.<br/>2. `Tarefas Concluídas`: número de issues em estado fechado (`closed`).<br/>3. `Data de Conclusão`: data efetiva de fechamento comparada ao prazo estipulado. |
| **Medidas Derivadas** | • Progresso (%) = (Tarefas Concluídas / Total de Tarefas) × 100<br/>• Aderência ao Prazo (%) = (Tarefas no Prazo / Total de Tarefas) × 100 |
| **Indicador e Critério de Decisão** | Percentual de tarefas concluídas no prazo por fase. Caso a aderência fique abaixo de 80% ou ocorra atraso crítico em tarefas com dependentes, a equipe deve renegociar escopo ou priorizar tarefas bloqueadoras imediatamente. |

### 4.2. Medições de Progresso da Fase 1

| Fase | Total de Issues | Concluídas | Em Andamento | Progresso (%) | No Prazo | Em Atraso | Aderência ao Prazo (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Fase 1** | 12 | 2 | 10 | 16,7% | 12 | 0 | 100,0% |
| **Fase 2** | 14 | 0 | 14 | 0,0% | 14 | 0 | 100,0% |

*Tabela 3: Acompanhamento de calendário e progresso das fases (Fonte: dados/gestao/02_calendario_e_progresso_fases.csv).*

![Calendário e Progresso por Fase](/img/gestao/02_calendario_e_progresso_fases.png)

*Figura 3: Progresso percentual de conclusão e aderência ao cronograma das fases.*

### 4.3. Interpretação de Progresso

* **Milestone da Fase 1 (Prazo: 21/10):** Das 12 issues da Fase 1, as tarefas fundamentais de infraestrutura e gestão foram as primeiras entregues e validadas (Issues #4 e #19). As 10 issues restantes estão em andamento ativo e dentro da janela temporal estipulada para o Ponto de Controle 1.
* **Aderência:** A taxa de aderência é de **100,0%**, sem ocorrência de atrasos registrados em tarefas concluídas ou em aberto.

---

## 5. Categoria 3: Desempenho dos Processos (*Process Performance*)

### 5.1. Measurement Construct — Desempenho dos Processos

| Elemento do Construct | Especificação |
| :--- | :--- |
| **Categoria de Informação** | Desempenho dos Processos (*Process Performance*) |
| **Necessidade de Informação** | Avaliar a eficácia dos processos de planejamento e entrega da equipe, identificando oportunidades de melhoria contínua na estimativa e na governança. |
| **Conceito Mensurável** | Qualidade do planejamento, velocidade de ciclo e conformidade do fluxo de trabalho. |
| **Medidas Base** | 1. `Lead Time (dias)`: tempo transcorrido entre a criação da issue e seu fechamento.<br/>2. `Contagem de Estimativas`: presença de valor preenchido na abertura da issue.<br/>3. `Revisões Realizadas`: conferência de aprovação de PR por integrante não autor. |
| **Medidas Derivadas** | • Acurácia de Estimativa (%) = (Horas Reais / Horas Estimadas) × 100<br/>• Taxa de Governança (%) = (Issues com Estimativa / Total de Issues) × 100<br/>• Lead Time Médio (dias) = Média do Lead Time das tarefas fechadas |
| **Indicador e Critério de Decisão** | Acurácia ideal entre 75% e 125%; taxa de governança superior a 90%; 100% dos PRs revisados por pares antes do merge. Desvios sistemáticos de estimativa exigem recalibração na fase subsequente. |

### 5.2. Indicadores de Processo da Fase 1

| Fase | Acurácia da Estimativa (%) | Taxa de Governança de Estimativa (%) | Lead Time Médio (dias) | Taxa de Revisão por Pares (%) |
| :--- | :---: | :---: | :---: | :---: |
| **Fase 1** | 185,7% | 16,7% | 0,00 dia(s) | 100,0% |

*Tabela 4: Indicadores de desempenho dos processos (Fonte: dados/gestao/03_desempenho_processos_fases.csv).*

### 5.3. Interpretação de Desempenho

1. **Acurácia da Estimativa Inicial:** A relação entre horas reais e estimadas nas duas primeiras tarefas fechadas ficou em 185,7% (6,5h reais frente a 3,5h estimadas inicialmente). Isso ocorreu porque o esforço de parametrização e pesquisa da fonte salarial no Novo CAGED exigiu discussões metodológicas adicionais não antecipadas na estimativa preliminar. Essa medição servirá como lição aprendida para calibrar as estimativas das próximas fases.
2. **Governança de Estimativa:** A taxa de preenchimento de estimativas na abertura está em 16,7% porque as issues das subfases técnicas foram inicialmente criadas em lote com o placeholder `_A preencher pelo responsável_`. Os responsáveis preenchem a estimativa formal no momento do início do trabalho.
3. **Revisão por Pares:** O fluxo estabelecido no `CONTRIBUTING.md` foi integralmente seguido: nenhum pull request foi integrado à branch principal sem a aprovação explícita de ao menos um revisor não autor.

---

## 6. Decisões de Gestão da Equipe (Premissa 3)

Em conformidade direta com a **Premissa 3 da especificação**, que exige a documentação explícita de como as medições influenciam a condução do projeto, a equipe registrou as seguintes decisões de gestão tomadas a partir dos dados:

### Decisão 1: Estruturação Organizacional em Subgrupos Especializados (F1/F3 e F2/F4)
* **Contexto e Causa:** O trabalho de avaliação de qualidade possui alto acoplamento entre fases correlatas (os requisitos da Fase 1 alimentam o projeto da Fase 3; a especificação da Fase 2 determina a execução da Fase 4).
* **Decisão:** Dividir a equipe em dois subgrupos estáveis de três membros. O Subgrupo 1 assume as Fases 1 e 3, enquanto o Subgrupo 2 assume as Fases 2 e 4. A gestão e as entregas globais (artigo e PC) permanecem integradas.
* **Impacto:** Eliminação de sobreposição de papéis e redução expressiva do tempo de alinhamento individual.

### Decisão 2: Automação Integral da Rastreabilidade via Script em Python
* **Contexto e Causa:** O controle manual de planilhas para acompanhar 33 issues e 6 integrantes geraria divergências e violaria a Premissa 5 (rastreabilidade primária).
* **Decisão:** Desenvolver e versionar o script `scripts/coleta_psm.py` para consultar a API do GitHub e persistir os dados brutos em `dados/gestao/raw_github_data.json`, gerando automaticamente os CSVs e gráficos.
* **Impacto:** Garantia de 100% de auditabilidade dos dados e redução do esforço burocrático de coleta a zero.

### Decisão 3: Padronização do Registro de Esforço Compartilhado (`@usuario: N`)
* **Contexto e Causa:** Tarefas estruturais ou de revisão contam frequentemente com mais de um integrante atuando. O registro agregado distorceria a tabela de contribuição individual.
* **Decisão:** Formalizar no guia de contribuição e no script o suporte ao formato `Total (@usuario1: N, @usuario2: M)`, rateando com precisão o tempo real dedicado por cada membro.
* **Impacto:** Transparência inequívoca no percentual individual de esforço para o critério AG-C5 do artigo.

### Decisão 4: Planejamento Escalonado para o Ponto de Controle 1 (21/10)
* **Contexto e Causa:** A proximidade da data da primeira apresentação presencial (21/10) exige consolidação prévia das entregas da Fase 1 e montagem antecipada dos slides.
* **Decisão:** Estabelecer o congelamento das documentações da Fase 1 com antecedência mínima de 24 horas em relação ao PC1, permitindo ensaio geral e alinhamento do tempo de fala entre os seis integrantes.
* **Impacto:** Mitigação do risco de apresentação descoordenada ou de estouro do limite de tempo estipulado pela professora.

---

## 7. Rastreabilidade e Evidências dos Dados

Conforme determina a **Premissa 5**, todos os números apresentados neste relatório possuem vínculo direto e verificável com os dados primários do repositório:

* **Dados brutos da API (JSON):** [`dados/gestao/raw_github_data.json`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/dados/gestao/raw_github_data.json)
* **Tabelas geradas (CSV):** Diretório [`dados/gestao/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/tree/main/dados/gestao/)
* **Script de coleta e processamento:** [`scripts/coleta_psm.py`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/scripts/coleta_psm.py)
* **Parâmetros de configuração:** [`scripts/config.json`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/scripts/config.json)

---

## 8. Declaração de Uso de Inteligência Artificial (Critério F1-C10)

* **Ferramenta utilizada:** Antigravity / Gemini 3.8.
* **Finalidade no relatório:** Apoio na estruturação lógica dos Measurement Constructs, organização dos indicadores segundo o modelo PSM/CID e redação inicial das análises de performance e estimativa.
* **Conferência crítica:** O texto foi integralmente revisado pela equipe, confrontando cada número com os CSVs extraídos da API do GitHub, verificando a exatidão das referências normativas e validando o conteúdo contra a especificação e as premissas da disciplina. Nenhuma imagem com texto sobreposto ou emoji foi utilizada.
