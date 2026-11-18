---
id: relatorio-psm-fase-3
title: Relatório PSM/CID da Fase 3
sidebar_label: Relatório PSM/CID (Fase 3)
sidebar_position: 3
description: Medições quantitativas das três categorias PSM/CID, análise de performance, comparação com as Fases 1 e 2, efeito da mudança do prazo e decisões de gestão da Fase 3.
---

import Link from '@docusaurus/Link';

# Relatório de Gestão com Métricas PSM/CID: Fase 3

## 1. Introdução

Este relatório apresenta as medições, a comparação com as fases anteriores e as decisões de gestão da equipe Karen Jones na Fase 3 do projeto de avaliação de qualidade do Excalidraw. A Fase 3 concentrou o planejamento detalhado da avaliação: método, recursos e ambientes, massa de dados, instruções dos avaliadores e cronograma das coletas. A milestone da fase cobriu o período de 26/10/2026 a 08/11/2026.

---

## 2. Metodologia

As medidas, os modelos de análise e os critérios de decisão são os do [Plano de Medição PSM](../plano-medicao-psm.md), que segue o template da Aula 09 [[1, p. 19]](#ref-1), o PSM/CID [[2]](#ref-2) e a ISO/IEC 15939 [[3]](#ref-3). Este relatório não cria limiares próprios: cada meta citada nas tabelas vem do plano.

Os números da Fase 3 são do retrato de 18/11/2026 dos dados gerados pelo `scripts/coleta_psm.py`, o mesmo do [Painel de Medição PSM](../painel-psm.md), com as 23 issues da fase fechadas. Os arquivos usados são:

- `dados/gestao/02_calendario_e_progresso_fases.csv`, para progresso e aderência ao prazo.
- `dados/gestao/01_recursos_e_custos_fases.csv` e `dados/gestao/03_desempenho_processos_fases.csv`, para horas, custo, acurácia e lead time.
- `dados/gestao/05_detalhamento_issues.csv` e `dados/gestao/06_contribuicao_por_fase.csv`, para o desvio por issue e a contribuição individual.
- `dados/gestao/constructs_e_tabelas.md`, seção 4, para ritmo de fechamento, tempo de espera dos PRs e revisores.

As Fases 1 e 2 entram na comparação com os valores da [linha de base do plano](../plano-medicao-psm.md#5-linha-de-base-das-fases-1-e-2-dados-históricos) (09/11/2026), que orientou as decisões da Entrega 2. O retrato de 18/11 das mesmas fases, com issues e PRs que mudaram de milestone depois, está no painel.

O relatório difere do plano em dois pontos:

- **Desvio por issue.** Além da acurácia da fase, o relatório mostra o desvio de cada issue e quantas ficaram entre -20% e +20%, a mesma faixa do [Construct 2](../plano-medicao-psm.md#42-construct-2-recursos-e-custos-acurácia-das-estimativas-de-esforço) aplicada issue a issue. Essa medida é complementar e não tem critério de decisão próprio.
- **Issues avaliadas.** A acurácia e o desvio usam só as 21 issues com horas estimadas e reais preenchidas. As issues [#138](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/138) e [#140](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/140) fecharam sem horas reais e ficam de fora, mas entram no total de horas da fase.

---

## 3. Medições Registradas da Fase 3

### 3.1. Calendário e Progresso

A milestone cobriu 13 dias, de 26/10/2026 a 08/11/2026, após a extensão de prazo analisada na [seção 5](#5-análise-do-efeito-da-mudança-do-prazo-da-milestone). As 23 issues vinculadas à fase estão concluídas no retrato de 18/11.

<p className="tabela-titulo">Tabela 1: Ritmo de fechamento das issues na Fase 3</p>

| Indicador | Referência no plano | Valor Observado | Situação |
| :--- | :---: | :---: | :---: |
| Issues concluídas | 100% | 23 de 23 (100,0%) | Conforme |
| Concluídas até a data média (02/11/2026 11:59) | ≥ 50,0% | 0 issues (0,0%) | Não conforme |
| Concluídas nos 2 últimos dias da fase | Fechamento contínuo | 7 issues (30,4%) | Atenção |
| Concluídas após o fim da milestone | 0 | 14 issues | Não conforme |
| Aderência aos prazos programados | 100,0% | 2 issues no prazo (8,7%) | Crítico |
| Alerta de ritmo disparado | Não | Sim | Alerta ativo |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>

O ritmo de entregas da Fase 3 sofreu forte retenção no início do ciclo. Nenhuma issue foi fechada na primeira metade da fase (até 02/11), o que dispara o critério de [Ritmo de Execução](../plano-medicao-psm.md#41-construct-1-calendário-e-progresso-ritmo-de-fechamento-e-dependências). As entregas concentraram-se entre 06/11 e 15/11, e 14 issues fecharam depois do fim da milestone. A issue [#105](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/105) (atualização do GitPage com a Fase 3) ficou bloqueada pela issue [#104](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/104) (visão geral da fase), e as duas fecharam só em 14 e 15/11, o que mostra o encadeamento de tarefas gerando efeito cascata no cronograma.

### 3.2. Recursos e Custos

O orçamento previsto para a Fase 3 foi de 48,00 horas (R$ 2.160,00), e o esforço real registrado nas 23 issues somou 62,50 horas (R$ 2.812,50).

<p className="tabela-titulo">Tabela 2: Recursos e custos consolidados da Fase 3</p>

| Métrica Orçamentária | Valor Estimado | Valor Real | Variação |
| :--- | :---: | :---: | :---: |
| Esforço total da fase (23 issues) | 48,00 h | 62,50 h | +30,2% |
| Custo financeiro equivalente (R$ 45,00/h) | R$ 2.160,00 | R$ 2.812,50 | +R$ 652,50 |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>

Nas 21 issues avaliadas, as horas reais (62,50 h) superaram as estimadas (46,00 h) em 35,9%, o que corresponde à acurácia de 135,9%, fora da faixa de 80% a 120% do [Construct 2](../plano-medicao-psm.md#42-construct-2-recursos-e-custos-acurácia-das-estimativas-de-esforço). A Tabela 3 separa esse desvio agregado, que pondera cada issue pelas horas, da média simples dos desvios por issue.

<p className="tabela-titulo">Tabela 3: Acerto das estimativas por issue na Fase 3</p>

| Indicador de Acurácia | Referência no plano | Resultado Observado | Situação |
| :--- | :---: | :---: | :---: |
| Issues avaliadas com horas registradas | N/A | 21 de 23 issues | Conforme |
| Desvio agregado da fase (soma das horas) | -20,0% a +20,0% | +35,9% | Subestimação |
| Média dos desvios por issue | Sem meta | +32,5% | Subestimação |
| Desvio mediano por issue | Sem meta | 0,0% | Neutro |
| Issues na faixa de -20% a +20% | Sem meta | 10 de 21 issues (47,6%) | Parcial |
| Issues subestimadas (desvio > +20%) | Sem meta | 10 issues (47,6%) | Atenção |
| Issues superestimadas (desvio < -20%) | Sem meta | 1 issue (4,8%) | Conforme |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>

O desvio de +35,9% ocorreu porque as tarefas de preparação de ambientes e testes operacionais demandaram mais tempo do que o previsto. Dentre as tarefas subestimadas destacam-se a issue [#96](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/96) (recursos e ambiente de avaliação), que consumiu 7,0 h reais frente a 2,0 h estimadas (+250%), a issue [#99](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/99) (instruções de G2), com 6,0 h reais para 3,0 h estimadas (+100%), e as issues [#97](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/97) (massa de dados) e [#107](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/107) (este relatório), com 5,0 h reais para 3,0 h estimadas (+66,7%).

A distribuição do esforço real entre os integrantes na Fase 3 apresentou o seguinte quadro:

<p className="tabela-titulo">Tabela 4: Contribuição individual no esforço real da Fase 3</p>

| Integrante | Login GitHub | Issues Atribuídas | Horas Estimadas (h) | Horas Reais (h) | Custo Real (R$) | Participação na Fase (%) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| Christopher Paraizo | `wChrstphr` | 5 | 8,50 | 5,50 | R$ 247,50 | 8,8% |
| Davi Pierre | `DaviPierre` | 5 | 12,00 | 16,00 | R$ 720,00 | 25,6% |
| Gabriel Monteiro | `GabrielSMonteiro` | 5 | 12,00 | 17,00 | R$ 765,00 | 27,2% |
| Letícia de Carvalho | `LeticiaSantosss` | 5 | 9,50 | 18,00 | R$ 810,00 | 28,8% |
| Luiz Henrique Soares | `luizh-gsoares` | 0 | 0,00 | 0,00 | R$ 0,00 | 0,0% |
| Maria Eduarda | `eduarda-ogomes` | 3 | 6,00 | 6,00 | R$ 270,00 | 9,6% |
| **Total** | - | **23** | **48,00** | **62,50** | **R$ 2.812,50** | **100,0%** |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>

Luiz Henrique ficou sem esforço registrado na Fase 3, abaixo do piso de 8% do critério de Equilíbrio de Carga, porque a divisão de trabalho da equipe alocou seus esforços na revisão das páginas e na finalização de artefatos da Fase 2, além de concentrar suas atribuições técnicas na execução da Fase 4. Os demais integrantes ficaram entre 8,8% e 28,8%. Na apuração de 12/11, Letícia de Carvalho somava 30,85% e passava do teto de 30%. Com as horas finais das issues, ela fica dentro da faixa.

### 3.3. Desempenho dos Processos

O fluxo de revisão de código e documentação foi avaliado a partir dos 23 pull requests integrados vinculados à Fase 3:

<p className="tabela-titulo">Tabela 5: Indicadores de processo e revisão por pares na Fase 3</p>

| Indicador de Processo | Referência no plano | Resultado Observado | Situação |
| :--- | :---: | :---: | :---: |
| PRs integrados com aprovação formal | 100% | 15 de 23 PRs (65,2%) | Evolução positiva |
| PRs integrados sem revisão formal | 0 | 8 PRs (34,8%) | Não conforme |
| Tempo médio de espera da primeira revisão | ≤ 24,0 h | 24,17 h | Atenção |
| Tempo mediano de espera da primeira revisão | ≤ 24,0 h | 20,88 h | Conforme |
| P80 e P90 de espera | Sem meta | 45,90 h e 61,74 h | Informativo |
| PRs com espera superior a 24 horas (notificação) | 0 | 5 PRs | Não conforme |
| PRs com espera superior a 48 horas (reatribuição) | 0 | 2 PRs | Não conforme |
| [Lead time das issues](../plano-medicao-psm.md#5-linha-de-base-das-fases-1-e-2-dados-históricos) | ≤ 3,0 dias | 7,62 dias | Não conforme |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>

A taxa de revisão formal atingiu 65,2% (15 PRs com aprovação registrada no GitHub), acima das fases anteriores. Os outros 8 PRs foram integrados sem aprovação formal na API (#132, #142, #143, #159, #160, #161, #164 e #171), o que contraria o critério de Conformidade Rigorosa do [Construct 3](../plano-medicao-psm.md#43-construct-3-desempenho-dos-processos-tempo-de-espera-por-revisão-de-pr).

O tempo de espera até a primeira revisão teve mediana de 20,88 h e média de 24,17 h. Cinco PRs esperaram mais de 24 horas, limite que aciona a notificação do revisor no plano: o PR #163 esperou 62,83 h, o PR #137 esperou 61,74 h, o PR #139 esperou 46,19 h, o PR #141 esperou 45,90 h e o PR #144 esperou 26,16 h. Os dois primeiros passaram de 48 horas, limite em que o plano manda reatribuir a revisão.

<p className="tabela-titulo">Tabela 6: Distribuição de revisões de pull request por integrante na Fase 3</p>

| Revisor | Login GitHub | PRs Revisados | Participação nas Revisões (%) |
| :--- | :--- | :---: | :---: |
| Christopher Paraizo | `wChrstphr` | 7 | 46,7% |
| Maria Eduarda | `eduarda-ogomes` | 7 | 46,7% |
| Luiz Henrique Soares | `luizh-gsoares` | 1 | 6,7% |
| Davi Pierre | `DaviPierre` | 0 | 0,0% |
| Gabriel Monteiro | `GabrielSMonteiro` | 0 | 0,0% |
| Letícia de Carvalho | `LeticiaSantosss` | 0 | 0,0% |
| **Total** | - | **15** | **100,0%** |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>

A carga de revisão concentrou-se em dois integrantes: Christopher Paraizo e Maria Eduarda fizeram 14 das 15 revisões formais da fase (93,3%).

---

## 4. Comparação com as Fases 1 e 2

A tabela compara a Fase 3 com a [linha de base do plano](../plano-medicao-psm.md#5-linha-de-base-das-fases-1-e-2-dados-históricos) para as Fases 1 e 2:

<p className="tabela-titulo">Tabela 7: Comparação de indicadores entre as Fases 1, 2 e 3</p>

| Indicador de Gestão | Fase 1 | Fase 2 | Fase 3 | Tendência Observada |
| :--- | :---: | :---: | :---: | :--- |
| Issues concluídas / total | 17 / 17 | 27 / 27 | 23 / 23 | Escopo concluído nas três fases |
| Horas estimadas | 53,50 h | 62,50 h | 48,00 h | Redução do esforço planejado |
| Horas reais | 57,91 h | 56,40 h | 62,50 h | Aumento na Fase 3 |
| Acurácia da estimativa | 108,2% | 90,2% | 135,9% | Fase 3 fora da faixa de 80% a 120% |
| Custo real equivalente | R$ 2.605,95 | R$ 2.538,00 | R$ 2.812,50 | Custo maior na Fase 3 |
| Aderência aos prazos | 29,4% | 44,4% | 8,7% | Piora sensível na pontualidade |
| Lead time das issues | 1,23 dias | 3,97 dias | 7,62 dias | Ciclo das tarefas mais longo |
| Taxa de revisão formal de PRs | 43,8% (7 de 16) | 44,0% (11 de 25) | 65,2% (15 de 23) | Aumento da revisão formal |
| Espera por revisão (média e mediana) | 12,45 h e 10,71 h | 1,91 h e 0,40 h | 24,17 h e 20,88 h | Aumento da espera na Fase 3 |

<p className="tabela-fonte">Fonte: [Christopher Paraizo](https://github.com/wChrstphr), 2026.</p>

A comparação evidencia três dinâmicas centrais:
1. **Pontualidade e Ritmo:** A aderência ao prazo caiu de 44,4% na Fase 2 para 8,7% na Fase 3. Na Fase 2 a equipe agrupou tarefas sob os mesmos autores, o que melhorou o fluxo. Na Fase 3, as tarefas dependeram de validação técnica sequencial (ambiente, massa e piloto), o que reintroduziu esperas em cadeia e adiou as entregas.
2. **Qualidade das Estimativas:** As Fases 1 e 2 ficaram dentro da faixa de acurácia (108,2% e 90,2%), e a Fase 3 fechou em 135,9%, com 10 das 21 issues avaliadas subestimadas. Tarefas de planejamento de teste e configuração de ambiente envolveram atritos com versões de bibliotecas e contêineres que não existiam nas fases puramente documentais.
3. **Maturidade de Revisão:** A taxa de revisão formal subiu de 43,8% (Fase 1) e 44,0% (Fase 2) para 65,2% na Fase 3, o que mostra uso mais disciplinado dos mecanismos do GitHub. Por outro lado, a revisão ficou concentrada em dois integrantes, e a mediana de espera passou de 0,40 h (Fase 2) para 20,88 h (Fase 3).

---

## 5. Análise do Efeito da Mudança do Prazo da Milestone

A data limite original da milestone da Fase 3 era 03/11/2026. Durante a execução, a equipe estendeu o prazo em 5 dias, fixando o término da milestone em 08/11/2026.

### 5.1. Motivação da Extensão

A prorrogação foi motivada por dificuldades imprevistas na preparação prática dos instrumentos de avaliação:
- A configuração do contêiner Docker oficial e a validação do monorepo local para viabilizar as métricas de Confiabilidade (G2) e Manutenibilidade (G1).
- A geração da massa de dados sintética de desenhos no formato JSON do Excalidraw, necessária para submeter o aplicativo a diferentes cargas de elementos gráficos.
- A elaboração de roteiros passo a passo com critérios de pontuação claros, reduzindo a ambiguidade para os avaliadores que executarão a Fase 4.

### 5.2. Impacto Quantitativo no Cronograma

Apesar da ampliação de 5 dias no prazo global da milestone, a aderência aos prazos programados nas issues ficou em 8,7% (apenas 2 issues concluídas no prazo registrado nos metadados). Esse resultado decorreu de três fatores:
1. Os prazos das issues individuais não foram repactuados quando a milestone foi estendida, permanecendo vinculados às estimativas iniciais do ciclo.
2. Sete issues fecharam na janela final da nova milestone (07/11 e 08/11), o que mostra que o prazo estendido absorveu o trabalho, mas postergou o esforço para o novo limite.
3. Catorze issues ultrapassaram a data limite estendida de 08/11 e fecharam entre 09/11 e 15/11, incluindo artefatos de apoio como a automação do script PSM ([#135](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/135)) e a homologação do teste piloto ([#103](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/103)).

A extensão de prazo foi necessária para garantir a consistência técnica dos roteiros de teste, evitando que a equipe iniciasse a coleta em campo com instrumentos falhos. Contudo, a medição evidenciou que estender a milestone sem antecipar os gargalos de dependência reproduziu a concentração de entregas na véspera.

---

## 6. Interpretação e Decisões de Gestão

Em continuidade às decisões D1 a D6 registradas na Linha de Base da Entrega 1 no [Registro de Medições e Decisões](../registro-medicoes.md), a equipe formalizou quatro novas decisões de gestão (D7 a D10) a partir dos resultados apurados na Fase 3. Cada uma aplica um critério de decisão do [Plano de Medição PSM](../plano-medicao-psm.md):

### Decisão D7: Rebalanceamento de Carga Individual para a Fase 4
- **Diagnóstico:** Luiz Henrique ficou sem esforço registrado na Fase 3, abaixo do piso de 8% do critério de Equilíbrio de Carga do [Construct 2](../plano-medicao-psm.md#42-construct-2-recursos-e-custos-acurácia-das-estimativas-de-esforço). Na apuração de 12/11, Letícia de Carvalho somava 30,85%, acima do teto de 30%, e Davi e Gabriel concentravam cerca de 27% e 21% da fase.
- **Ação adotada:** Atribuir a Luiz Henrique o papel principal em 8 tarefas da Fase 4, totalizando 23,0 horas estimadas, abrangendo a preparação do ambiente de medidas (#110), a coleta de métricas de confiabilidade (#112), a análise de dados de G2 (#116), a síntese do julgamento final (#120) e as conclusões do artigo científico (#125). Em contrapartida, as tarefas de coleta prática da Fase 4 foram aliviadas para Letícia de Carvalho.
- **Impacto esperado:** Reequilibrar a participação acumulada da equipe na Entrega 2, mantendo todos os membros dentro da faixa de 8% a 30% no balanço consolidado.

### Decisão D8: Aplicação do Fator de Calibração de 1,2× em Tarefas Técnicas
- **Diagnóstico:** A acurácia da Fase 3 fechou em 135,9%, acima da faixa de 80% a 120%, com 10 de 21 issues subestimadas, concentradas em atividades práticas que envolveram ferramentas externas, compilação de código e geração de dados sintéticos.
- **Ação adotada:** Aplicar o fator corretivo de 1,2× do critério de Recalibração de Planejamento do [Construct 2](../plano-medicao-psm.md#42-construct-2-recursos-e-custos-acurácia-das-estimativas-de-esforço) nas estimativas das tarefas da Fase 4 que envolvam ferramentas de teste (Docker, SonarQube, Stryker e Cypress), mantendo estimativas regulares apenas para redação documental pura.
- **Impacto esperado:** Conter estouros de cronograma e trazer a acurácia da Fase 4 de volta à faixa de 80% a 120%.

### Decisão D9: Revisão de Pull Requests em até 24 Horas
- **Diagnóstico:** Embora a taxa de revisão formal tenha chegado a 65,2%, cinco PRs aguardaram mais de 24 horas pela primeira revisão, dois deles acima de 48 horas. Além disso, 93,3% das revisões ficaram a cargo de apenas dois membros.
- **Ação adotada:** Aplicar o critério de Alerta de PR Travado do [Construct 3](../plano-medicao-psm.md#43-construct-3-desempenho-dos-processos-tempo-de-espera-por-revisão-de-pr): PR sem revisão há 24 horas gera notificação ao revisor indicado, e com 48 horas a revisão é reatribuída. Além disso, todo integrante, ao concluir sua tarefa diária, verifica e revisa os PRs pendentes antes de iniciar nova issue.
- **Impacto esperado:** Zerar PRs com espera acima de 24 horas e distribuir a carga de revisão entre os seis integrantes na Fase 4.

### Decisão D10: Abertura Imediata e Desacoplamento das Tarefas da Fase 4
- **Diagnóstico:** A baixa aderência ao prazo na Fase 3 (8,7%) decorreu do acoplamento estrito entre etapas conceituais e operacionais, aliado à abertura tardia de issues de infraestrutura no GitHub Projects.
- **Ação adotada:** Abrir e detalhar todas as issues da Fase 4 desde o primeiro dia da milestone, permitindo que a infraestrutura (#110) e a coleta antecipada de Flexibilidade (#113) avancem em paralelo com as coletas de Manutenibilidade e Confiabilidade, sem esperar o término formal das documentações da Fase 3.
- **Impacto esperado:** Atingir pelo menos 50% das issues fechadas na primeira metade da Fase 4, como pede o critério de Ritmo de Execução do [Construct 1](../plano-medicao-psm.md#41-construct-1-calendário-e-progresso-ritmo-de-fechamento-e-dependências), e elevar a aderência aos prazos programados.

---

## Referências

> <Link id="ref-1">1.</Link> RAMOS, Cristiane Soares. **AULA 09 QSW1 PSM resumo**. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Disponível no Moodle da disciplina.
>
> <Link id="ref-2">2.</Link> PRACTICAL SOFTWARE MEASUREMENT. **Practical Software and Systems Measurement: A Foundation for Objective Project Management (PSM/CID)**. Version 4.0d, CID, 2021. Disponível em: https://www.psmsc.com.
>
> <Link id="ref-3">3.</Link> ISO/IEC/IEEE. **ISO/IEC/IEEE 15939:2017: Systems and software engineering: Measurement process**. International Organization for Standardization, Genebra, 2017.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 12/11/2026 | Registro das medições PSM/CID da Fase 3, comparação com as Fases 1 e 2, análise da extensão de prazo e decisões de gestão D7 a D10 | [Gabriel Monteiro](https://github.com/GabrielSMonteiro) | [Christopher Paraizo](https://github.com/wChrstphr) |
| 1.1 | 18/11/2026 | Revisão de coerência e cross-links: números pelo retrato de 18/11/2026 e limiares alinhados ao plano | [Christopher Paraizo](https://github.com/wChrstphr) | |
