---
id: painel-psm
title: Painel de medição PSM/CID
sidebar_label: Painel de Medição PSM
sidebar_position: 2
toc_min_heading_level: 2
toc_max_heading_level: 3
description: Painel com os indicadores do Plano de Medição PSM/CID por fase, por entrega e no projeto, Curva S, recursos e custos, desempenho do processo e insights da evolução entre as Fases 1 a 4, no retrato de 18/11/2026.
---

import Link from '@docusaurus/Link';

# Painel de medição PSM/CID

## 1. Introdução

O painel apresenta os indicadores definidos no [Plano de Medição PSM](plano-medicao-psm.md), que segue o modelo Practical Software and Systems Measurement (PSM/CID) [[1]](#ref-1), para as quatro fases da avaliação do Excalidraw. No retrato de 18/11/2026, a Entrega 1 está concluída (47 de 47 issues) e a Entrega 2 tem 42 de 50 issues concluídas, com as 8 abertas na Fase 4. A interpretação das causas de desvio e as decisões de gestão ficam no [Registro de Medições e Decisões](registro-medicoes.md).

## 2. Metodologia

As tabelas são o retrato de 18/11/2026 dos dados gerados automaticamente pelo `scripts/coleta_psm.py`, que lê issues, PRs e revisões pela API do GitHub. A fonte é o commit [`9733fa2`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/tree/9733fa2a68625d07405c3b2d2275851d6d4a7f68/dados/gestao), a última atualização automática de 18/11/2026: `07_resumo_entregas.csv` para as entregas, `01_recursos_e_custos_fases.csv`, `02_calendario_e_progresso_fases.csv` e `03_desempenho_processos_fases.csv` para as fases, `05_detalhamento_issues.csv` para a situação de cada issue, `08_contribuicao_por_entrega.csv` e `04_contribuicao_individual.csv` para a participação individual e `constructs_e_tabelas.md` para a revisão de PRs. As figuras, ao contrário das tabelas, continuam se atualizando: o workflow `coleta-psm.yml` roda todo dia e regenera as imagens de `static/img/gestao/`, que podem mostrar valores posteriores ao retrato.

Os indicadores seguem as medidas derivadas dos constructs do plano. A acurácia da estimativa considera só as issues com horas estimadas e reais preenchidas. O lead time das issues é a média, em dias, entre a abertura e o fechamento das issues fechadas, e a meta de até 3 dias vem da [linha de base do plano](plano-medicao-psm.md#5-linha-de-base-das-fases-1-e-2-dados-históricos). Uma issue conta no prazo quando fecha até o campo `Prazo` ou quando segue aberta antes dele.

O retrato da Entrega 1 difere da linha de base do plano, apurada em 09/11/2026. Depois dessa data, as issues [#90](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/90), [#153](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/153) e [#155](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/155) passaram a contar nas milestones das Fases 1 e 2 (de 44 para 47 issues) e os PRs integrados das duas fases passaram de 41 para 44.

---

## 3. Resumo por entrega e por fase

<p className="tabela-titulo">Tabela 1: Resumo por fase e por entrega. Retrato de 18/11/2026</p>

| Escopo | Issues (concl. / total) | Progresso (%) | Aderência ao prazo (%) | Horas est. (h) | Horas reais (h) | Custo est. (R$) | Custo real (R$) | Acurácia (%) | [Lead time das issues](plano-medicao-psm.md#5-linha-de-base-das-fases-1-e-2-dados-históricos) (dias) | Governança da estimativa (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Fase 1 *(requisitos)* | 18 / 18 | 100,0 | 33,3 | 59,50 | 59,01 | 2.677,50 | 2.655,45 | 99,2 | 1,21 | 100,0 |
| Fase 2 *(especificação GQM e artigo)* | 29 / 29 | 100,0 | 48,3 | 70,50 | 64,70 | 3.172,50 | 2.911,50 | 91,8 | 3,74 | 89,7 |
| **Entrega 1 (F1 + F2)** | **47 / 47** | **100,0** | **42,6** | **130,00** | **123,71** | **5.850,00** | **5.566,95** | **95,2** | **2,77** | **93,6** |
| Fase 3 *(projeto da avaliação)* | 23 / 23 | 100,0 | 8,7 | 48,00 | 62,50 | 2.160,00 | 2.812,50 | 135,9 | 7,62 | 100,0 |
| Fase 4 *(execução da avaliação)* | 19 / 27 | 70,4 | 55,6 | 92,00 | 63,75 | 4.140,00 | 2.868,75 | 102,8 | 12,34 | 100,0 |
| **Entrega 2 (F3 + F4)** | **42 / 50** | **84,0** | **34,0** | **140,00** | **126,25** | **6.300,00** | **5.681,25** | **116,9** | **9,76** | **100,0** |
| **Projeto (F1 a F4)** | **89 / 97** | **91,8** | **38,1** | **270,00** | **249,96** | **12.150,00** | **11.248,20** | **106,4** | **6,36** | **96,9** |

<p className="tabela-fonte">Fonte: [Maria Eduarda](https://github.com/eduarda-ogomes), com base em <code>dados/gestao/07_resumo_entregas.csv</code>, <code>01_recursos_e_custos_fases.csv</code>, <code>02_calendario_e_progresso_fases.csv</code> e <code>03_desempenho_processos_fases.csv</code> do retrato de 18/11/2026.</p>

---

## 4. Calendário e progresso

A Curva S compara o esforço planejado acumulado, pelos prazos internos das issues no [GitHub Project](priorizacao-issues.md), com o esforço realizado, pela data de conclusão das issues.

<p className="tabela-titulo">Figura 1: Curva S de desempenho de execução (planejado vs. realizado)</p>

![Curva S de desempenho de execução: esforço acumulado planejado versus realizado](/img/gestao/08_desempenho_execucao_curva_s.png)

<p className="tabela-fonte">Fonte: [Maria Eduarda](https://github.com/eduarda-ogomes), com base em <code>dados/gestao/02_calendario_e_progresso_fases.csv</code> e <code>scripts/gerar_grafico_desempenho.py</code>, 2026.</p>

### 4.1. Aderência ao cronograma interno

<p className="tabela-titulo">Tabela 2: Conclusão e aderência aos prazos internos. Retrato de 18/11/2026</p>

| Recorte | Total de issues | Concluídas | Abertas | Progresso (%) | Concluídas no prazo | Concluídas após o prazo | Abertas antes do prazo | Abertas em atraso | Aderência ao prazo (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Fase 1 | 18 | 18 | 0 | 100,0 | 6 | 12 | 0 | 0 | 33,3 |
| Fase 2 | 29 | 29 | 0 | 100,0 | 14 | 15 | 0 | 0 | 48,3 |
| **Entrega 1 (F1 + F2)** | **47** | **47** | **0** | **100,0** | **20** | **27** | **0** | **0** | **42,6** |
| Fase 3 | 23 | 23 | 0 | 100,0 | 2 | 21 | 0 | 0 | 8,7 |
| Fase 4 | 27 | 19 | 8 | 70,4 | 7 | 12 | 8 | 0 | 55,6 |
| **Entrega 2 (F3 + F4)** | **50** | **42** | **8** | **84,0** | **9** | **33** | **8** | **0** | **34,0** |

<p className="tabela-fonte">Fonte: [Maria Eduarda](https://github.com/eduarda-ogomes), com base em <code>dados/gestao/05_detalhamento_issues.csv</code> do retrato de 18/11/2026.</p>

A aderência da Fase 4 inclui as 8 issues abertas cujo prazo ainda não venceu. Considerando só as concluídas, 7 de 19 fecharam no prazo.

---

## 5. Recursos e custos: contribuição individual por entrega e no projeto

A equipe consolida a participação por entrega (Entrega 1 = Fases 1 e 2, Entrega 2 = Fases 3 e 4), em razão da divisão em dois subgrupos (F1/F3 e F2/F4). As issues compartilhadas contam para cada responsável, e o custo usa o valor-hora de R$ 45,00 do [Construct 2 do plano](plano-medicao-psm.md#42-construct-2-recursos-e-custos-acurácia-das-estimativas-de-esforço).

### 5.1. Contribuição individual na Entrega 1 (Fases 1 e 2)

<p className="tabela-titulo">Tabela 3: Esforço e custo individual na Entrega 1 (Fases 1 e 2). Retrato de 18/11/2026</p>

| Integrante | Login GitHub | Subgrupo | Issues atribuídas | Horas est. (h) | Horas reais (h) | Custo real (R$) | Esforço real (%) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Christopher Paraizo | `@wChrstphr` | F2/F4 | 15 | 37,00 | 28,40 | 1.278,00 | 22,96 |
| Davi Pierre | `@DaviPierre` | F1/F3 | 6 | 20,00 | 21,00 | 945,00 | 16,98 |
| Gabriel Monteiro | `@GabrielSMonteiro` | F1/F3 | 8 | 27,50 | 28,50 | 1.282,50 | 23,04 |
| Letícia de Carvalho | `@LeticiaSantosss` | F1/F3 | 7 | 12,00 | 9,91 | 445,95 | 8,01 |
| Luiz Henrique Soares | `@luizh-gsoares` | F2/F4 | 7 | 12,00 | 12,40 | 558,00 | 10,02 |
| Maria Eduarda | `@eduarda-ogomes` | F2/F4 | 9 | 21,50 | 23,50 | 1.057,50 | 19,00 |
| **Total da Entrega 1** | | | **52** | **130,00** | **123,71** | **5.566,95** | **100** |

<p className="tabela-fonte">Fonte: [Maria Eduarda](https://github.com/eduarda-ogomes), com base em <code>dados/gestao/08_contribuicao_por_entrega.csv</code> do retrato de 18/11/2026.</p>

Nas duas entregas e no acumulado do projeto, todos os integrantes ficam dentro da faixa de equilíbrio de 8% a 30% do esforço definida no [Construct 2 do plano](plano-medicao-psm.md#42-construct-2-recursos-e-custos-acurácia-das-estimativas-de-esforço). Os valores da Entrega 1 diferem do [Apêndice B do artigo](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/artigo/contribuicao-e-ia.md), fechado na entrega, pelas issues incluídas depois, descritas na [Metodologia](#2-metodologia).

<p className="tabela-titulo">Figura 2: Participação percentual no esforço da Entrega 1 com discriminação por fase</p>

![Participação percentual no esforço real da Entrega 1 com discriminação de Fase 1 e Fase 2](/img/gestao/05_esforco_integrante_entrega_1.png)

<p className="tabela-fonte">Fonte: [Maria Eduarda](https://github.com/eduarda-ogomes), com base em <code>dados/gestao/08_contribuicao_por_entrega.csv</code>, 2026.</p>

### 5.2. Contribuição individual na Entrega 2 (Fases 3 e 4)

<p className="tabela-titulo">Tabela 4: Esforço e custo individual na Entrega 2 (Fases 3 e 4). Retrato de 18/11/2026</p>

| Integrante | Login GitHub | Subgrupo | Issues atribuídas | Horas est. (h) | Horas reais (h) | Custo real (R$) | Esforço real (%) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Christopher Paraizo | `@wChrstphr` | F2/F4 | 13 | 34,50 | 11,55 | 519,75 | 9,15 |
| Davi Pierre | `@DaviPierre` | F1/F3 | 8 | 18,00 | 16,00 | 720,00 | 12,67 |
| Gabriel Monteiro | `@GabrielSMonteiro` | F1/F3 | 10 | 22,00 | 28,50 | 1.282,50 | 22,57 |
| Letícia de Carvalho | `@LeticiaSantosss` | F1/F3 | 10 | 19,50 | 18,00 | 810,00 | 14,26 |
| Luiz Henrique Soares | `@luizh-gsoares` | F2/F4 | 8 | 20,00 | 20,50 | 922,50 | 16,24 |
| Maria Eduarda | `@eduarda-ogomes` | F2/F4 | 11 | 26,00 | 31,70 | 1.426,50 | 25,11 |
| **Total da Entrega 2** | | | **60** | **140,00** | **126,25** | **5.681,25** | **100** |

<p className="tabela-fonte">Fonte: [Maria Eduarda](https://github.com/eduarda-ogomes), com base em <code>dados/gestao/08_contribuicao_por_entrega.csv</code> do retrato de 18/11/2026.</p>

As 50 issues da Entrega 2 correspondem a 60 atribuições, por causa das tarefas compartilhadas entre integrantes.

<p className="tabela-titulo">Figura 3: Participação percentual no esforço da Entrega 2 com discriminação por fase</p>

![Participação percentual no esforço real da Entrega 2 com discriminação de Fase 3 e Fase 4](/img/gestao/05_esforco_integrante_entrega_2.png)

<p className="tabela-fonte">Fonte: [Maria Eduarda](https://github.com/eduarda-ogomes), com base em <code>dados/gestao/08_contribuicao_por_entrega.csv</code>, 2026.</p>

### 5.3. Esforço e custo acumulados no projeto (Fases 1 a 4)

No cômputo geral do projeto (Fases 1, 2, 3 e 4), a equipe somou 260,16 horas reais executadas frente a 274,00 horas estimadas, totalizando R$ 11.707,20 em custo real apurado à taxa horária de R$ 45,00. A tabela a seguir sintetiza a contribuição individual acumulada em todo o repositório, extraída de [`dados/gestao/04_contribuicao_individual.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/dados/gestao/04_contribuicao_individual.csv):

<p className="tabela-titulo">Tabela 5: Esforço acumulado e custo individual no projeto (Fases 1 a 4). Retrato de 18/11/2026</p>

| Integrante | Login GitHub | Issues atribuídas | Horas est. (h) | Horas reais (h) | Custo real (R$) | Commits | PRs abertos | Esforço real (%) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Christopher** | `@wChrstphr` | 29 | 75,50 | 52,65 | R$ 2.369,25 | 158 | 28 | **20,24%** |
| **Davi Pierre** | `@DaviPierre` | 14 | 38,00 | 37,00 | R$ 1.665,00 | 13 | 6 | **14,22%** |
| **Gabriel Monteiro** | `@GabrielSMonteiro` | 18 | 49,50 | 57,00 | R$ 2.565,00 | 69 | 16 | **21,91%** |
| **Letícia de Carvalho** | `@LeticiaSantosss` | 17 | 31,50 | 29,41 | R$ 1.323,45 | 16 | 11 | **11,30%** |
| **Luiz Henrique Soares** | `@luizh-gsoares` | 15 | 32,00 | 32,90 | R$ 1.480,50 | 38 | 16 | **12,65%** |
| **Maria Eduarda** | `@eduarda-ogomes` | 20 | 47,50 | 51,20 | R$ 2.304,00 | 77 | 16 | **19,68%** |
| **Total do Projeto** | **Equipe** | **97 (113 atrib.)** | **274,00** | **260,16** | **R$ 11.707,20** | **371** | **93** | **100,00%** |

<p className="tabela-fonte">Fonte: [Maria Eduarda](https://github.com/eduarda-ogomes), com base em <code>dados/gestao/04_contribuicao_individual.csv</code> do retrato de 18/11/2026.</p>

As 97 issues do projeto correspondem a 112 atribuições.

<p className="tabela-titulo">Figura 4: Distribuição de tarefas e commits por integrante no projeto</p>

![Volume de issues atribuídas e commits registrados por integrante](/img/gestao/03_contribuicao_individual.png)

<p className="tabela-fonte">Fonte: [Maria Eduarda](https://github.com/eduarda-ogomes), com base em <code>dados/gestao/04_contribuicao_individual.csv</code>, 2026.</p>

---

## 6. Desempenho dos processos e governança

<p className="tabela-titulo">Tabela 6: Indicadores de processo e governança. Retrato de 18/11/2026</p>

| Indicador | Fase 1 | Fase 2 | Entrega 1 | Fase 3 | Fase 4 | Entrega 2 | Meta do plano |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Acurácia da estimativa (%) | 99,2 | 91,8 | **95,2** | 135,9 | 102,8 | **116,9** | 80 a 120 |
| [Lead time das issues](plano-medicao-psm.md#5-linha-de-base-das-fases-1-e-2-dados-históricos) (dias) | 1,21 | 3,74 | **2,77** | 7,62 | 12,34 | **9,76** | até 3 |
| Governança da estimativa (%) | 100,0 | 89,7 | **93,6** | 100,0 | 100,0 | **100,0** | 100 |
| Revisão formal por pares (%) | 47,1 (8 de 17) | 48,1 (13 de 27) | **47,7 (21 de 44)** | 65,2 (15 de 23) | 47,4 (9 de 19) | **57,1 (24 de 42)** | 100 |
| Espera por revisão, mediana (h) | 10,82 | 0,40 | **0,79** | 20,88 | 1,50 | **13,61** | até 24 |
| PRs com espera acima de 24 h | 1 | 1 | **2** | 5 | 0 | **5** | 0 |

<p className="tabela-fonte">Fonte: [Maria Eduarda](https://github.com/eduarda-ogomes), com base em <code>dados/gestao/03_desempenho_processos_fases.csv</code>, <code>07_resumo_entregas.csv</code> e na seção de revisão de PRs de <code>constructs_e_tabelas.md</code> do retrato de 18/11/2026.</p>

A Fase 3 é a única fora da faixa de acurácia: as horas reais superaram as estimadas em 35,9%, o que aciona a recalibração do [Construct 2](plano-medicao-psm.md#42-construct-2-recursos-e-custos-acurácia-das-estimativas-de-esforço). O lead time passou da meta nas Fases 3 e 4, e a revisão formal ficou abaixo de 100% em todas as fases, com 52,3% (45 de 86 PRs) no projeto inteiro. A taxa conta os PRs integrados com aprovação (`APPROVED`) de outro integrante no GitHub, e a espera conta só os PRs que receberam revisão (21 na Entrega 1 e 25 na Entrega 2).

<p className="tabela-titulo">Figura 5: Acurácia da estimativa de esforço por fase em relação à faixa ideal (80% a 120%)</p>

![Acurácia da estimativa por fase em relação à faixa ideal de 80% a 120%](/img/gestao/06_acuracia_estimativa_fases.png)

<p className="tabela-fonte">Fonte: [Maria Eduarda](https://github.com/eduarda-ogomes), com base em <code>dados/gestao/01_recursos_e_custos_fases.csv</code>, 2026.</p>

---

## 7. Insights de gestão: evolução da organização da equipe da Fase 1 à Fase 4

A análise comparativa das métricas PSM/CID ao longo do projeto mostra como a equipe diagnosticou o gargalo de dependências entre tarefas nas Fases 1 e 2 e como a adoção de **prazos individuais escalonados nas issues** e de **priorização por impacto de bloqueio** nas Fases 3 e 4 elevou a pontualidade das entregas na Fase 4.

<p className="tabela-titulo">Tabela 7: Comparativo das métricas PSM/CID e evolução do fluxo de trabalho entre as Fases 1, 2, 3 e 4</p>

| Dimensão (PSM/CID) | Métrica Específica | Fase 1 | Fase 2 | Fase 3 | Fase 4 (parcial) | Evolução e Impacto no Fluxo |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Calendário e Progresso** | Aderência aos prazos internos | 33,3% (6/18) | 48,3% (14/29) | 8,7% (2/23) | **55,6% (15/27)** | Maior índice do projeto na Fase 4 após a adoção dos prazos individuais escalonados. O valor inclui as 8 issues abertas antes do prazo: das 19 concluídas, 7 fecharam no prazo. |
| **Ritmo de Execução** | Conclusão na 1ª metade da fase | 0,0% (0/18) | 55,2% (16/29) | 0,0% (0/23) | 7,4% (2/27) | Salto de 0,0% na Fase 1 para 55,2% na Fase 2 com a redução de dependências cruzadas nos blocos do GQM. |
| **Ritmo de Execução** | Concentração nos 2 últimos dias | 72,2% (13/18) | 27,6% (8/29) | 30,4% (7/23) | **0,0% (0/27)** | Redução da entrega em lote de 72,2% na Fase 1 para 27,6% na Fase 2, distribuindo as conclusões conforme os prazos individuais. |
| **Desempenho do Processo** | Tempo médio de espera de PR | 13,68 h | 3,66 h | 24,17 h | **5,19 h** | Queda de 73,2% da Fase 1 para a Fase 2 e estabilização em 5,19 h na Fase 4. |
| **Desempenho do Processo** | Tempo mediano de espera de PR | 10,82 h | 0,40 h (24 min) | 20,88 h | **1,50 h** | Redução expressiva de 10,82 h na Fase 1 para 0,40 h na Fase 2 e manutenção de respostas rápidas (1,50 h) na Fase 4. |
| **Desempenho do Processo** | PRs com espera acima de 24 h | 1 PR | 1 PR | 5 PRs | **0 PRs** | Eliminação completa de filas críticas de revisão na Fase 4. |
| **Desempenho do Processo** | Governança de estimativa | 100,0% | 89,7% | 100,0% | **100,0%** | Recuperação integral do preenchimento de estimativas nas Fases 3 e 4 (100,0%). |
| **Recursos e Custos** | Acurácia da estimativa de esforço | 99,2% | 91,8% | 135,9% | **102,8%** | Alta precisão nas Fases 1 e 2 e retorno ao centro da faixa ideal (80% a 120%) na Fase 4 (102,8%). |

<p className="tabela-fonte">Fonte: [Maria Eduarda](https://github.com/eduarda-ogomes), com base em <code>dados/gestao/constructs_e_tabelas.md</code>, <code>02_calendario_e_progresso_fases.csv</code> e <code>03_desempenho_processos_fases.csv</code>, 2026.</p>

### 7.1. Diferença entre as Fases 1 e 2: O Diagnóstico do Gargalo de Dependências

Na Entrega 1, a comparação entre a Fase 1 e a Fase 2 permitiu identificar a causa raiz dos atrasos de cronograma:

* **Bloqueio em Cadeia na Fase 1:** Na Fase 1, as issues foram divididas entre os integrantes sem considerar as dependências entre elas e sem prazos individuais intermediários. Como as tarefas iniciais de escopo, partes interessadas e modelo de qualidade eram pré-requisitos para as demais, o acúmulo de agenda de um integrante travava o início das tarefas dependentes. Isso resultou em 0,0% de conclusão na primeira metade da fase, 72,2% das entregas concentradas nos dois últimos dias e apenas 33,3% de aderência ao prazo.
* **Avanço Parcial na Fase 2:** Na Fase 2, a atribuição de blocos correlatos de questões e métricas GQM a um mesmo responsável reduziu parte das esperas entre integrantes. Com menos dependências cruzadas, 55,2% das issues foram concluídas já na primeira metade da fase, a concentração nos dois últimos dias caiu de 72,2% para 27,6%, a aderência ao prazo subiu de 33,3% para 48,3% (+15,0 p.p.) e o tempo mediano de espera por revisão de PR caiu de 10,82 h para 0,40 h (24 minutos). Contudo, nas tarefas finais que voltavam a depender de múltiplos membros (como o fechamento do artigo), o gargalo de espera reapareceu.

### 7.2. A Mudança nas Fases 3 e 4: Prazos Individuais nas Issues e Controle de Dependências

A partir da análise das métricas PSM na [reunião de 04/11/2026](atas/2026-11-04-apresentacao-psm.md), a equipe mudou a forma de gerenciar os prazos e as dependências para as Fases 3 e 4, conforme detalhado em [Priorização e datas no GitHub Project](priorizacao-issues.md):

* **Prazos Individuais por Issue:** Em vez de trabalhar apenas com a data limite geral da fase, cada issue passou a ter um prazo individual definido para o responsável entregar a sua atividade a tempo de não atrasar as tarefas seguintes.
* **Prioridade pelo Volume de Desbloqueio:** As issues receberam etiquetas de prioridade conforme a quantidade de atividades que liberam no fluxo, destacando no quadro do projeto quais entregas não podiam sofrer atraso.
* **Efeito de Transição na Fase 3:** Como as issues da Fase 3 já estavam montadas e em andamento quando a medida foi adotada em 04/11/2026, e houve atrito técnico não previsto na preparação dos contêineres e testes-piloto, a aderência da Fase 3 ainda sofreu impacto (8,7%) e exigiu 62,50 h reais frente a 48,00 h estimadas (acurácia de 135,9%).
* **Resultado Consolidado na Fase 4:** Na Fase 4, planejada integralmente desde a abertura com os prazos individuais escalonados em cada issue, a melhoria apareceu de imediato nos indicadores: a **aderência aos prazos atingiu 55,6% do total da fase** (15 de 27 issues no prazo: 7 concluídas no prazo e 8 abertas antes do prazo), superando todas as fases anteriores do projeto. Além disso, a acurácia de esforço convergiu para **102,8%** e nenhum PR ficou aguardando revisão por mais de 24 horas.

### 7.3. Conclusão do Insight de Gestão

O histórico de medições do PSM/CID comprovou que os atrasos iniciais da equipe não decorriam de falta de esforço ou de erro nas estimativas de horas (a acurácia manteve-se excelente: 99,2% na Fase 1, 91,8% na Fase 2 e 102,8% na Fase 4). O problema estava na ausência de prazos individuais intermediários que respeitassem a ordem de dependência entre as tarefas. A introdução dos prazos individuais por issue destravou o fluxo de trabalho entre os membros e permitiu que a Fase 4 alcançasse o maior índice de entregas no prazo de todo o semestre.

---

## Referências

> <Link id="ref-1">1.</Link> CARD, David et al. **Practical Software and Systems Measurement (PSM): A Foundation for Objective Project Management**. Version 4.0d. PSM Support Center, 2021. Disponível em: [https://psmsc.com](https://psmsc.com). Acesso em: 18 out. 2026.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 07/11/2026 | Criação do Painel Executivo PSM/CID consolidado por entrega com Curva S, distribuição de esforço e indicadores de processo | [Maria Eduarda](https://github.com/eduarda-ogomes) | |
| 1.1 | 09/11/2026 | Taxa de revisão por pares das Fases 1 e 2 recalculada pela coleta automática de PRs | [Christopher Paraizo](https://github.com/wChrstphr) | |
| 1.2 | 18/11/2026 | Atualização dos dados consolidados das Fases 1 a 4 e inclusão da seção de insights sobre prazos individuais por issue e evolução entre as fases | [Maria Eduarda](https://github.com/eduarda-ogomes) | |
| 1.3 | 18/11/2026 | Inclusão dos recursos e custos da Entrega 2, balanço acumulado do projeto e gráficos de esforço individual | [Maria Eduarda](https://github.com/eduarda-ogomes) | |
| 1.4 | 20/11/2026 | Alinhamento da Tabela 5 com a coleta final de métricas PSM/CID (260,16h reais) | [Maria Eduarda](https://github.com/eduarda-ogomes) | |

