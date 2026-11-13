---
id: relatorio-psm-fase-3
title: Relatório PSM/CID da Fase 3
sidebar_label: Relatório PSM/CID (Fase 3)
sidebar_position: 3
description: Medições quantitativas das três categorias PSM/CID, análise de performance, comparação com as Fases 1 e 2, efeito da mudança do prazo e decisões de gestão da Fase 3.
---

# Relatório de Gestão com Métricas PSM/CID: Fase 3

## 1. Introdução e Metodologia

Este relatório apresenta o registro das medições, a análise de desempenho do processo, a comparação com as fases anteriores e as decisões de gestão adotadas pela equipe Karen Jones ao longo da Fase 3 do projeto de avaliação de qualidade do software Excalidraw. A Fase 3 concentrou o planejamento detalhado da avaliação, incluindo a especificação do método, os recursos e ambientes computacionais, a preparação da massa de dados, os roteiros de instrução dos avaliadores e o cronograma de execução das coletas em campo.

A coleta dos dados foi realizada de forma automatizada por meio do script `scripts/coleta_psm.py` a partir da API oficial do GitHub, com persistência dos dados brutos em `dados/gestao/raw_github_data.json` e consolidação em arquivos CSV. As medidas e os conceitos mensuráveis seguem as definições estabelecidas no [Plano de Medição PSM](../plano-medicao-psm.md), em conformidade com as normas ISO/IEC 15939 e ISO/IEC 25040.

---

## 2. Measurement Constructs da Fase 3

A equipe aplicou os três modelos de medição (*measurement constructs*) definidos no [Plano de Medição PSM](../plano-medicao-psm.md), estruturados segundo a norma ISO/IEC 15939:

### 2.1. Construct 1: Calendário e Progresso

<p className="tabela-titulo">Tabela 1: Measurement Construct para Calendário e Progresso na Fase 3</p>

| Elemento do Construct | Especificação |
| :--- | :--- |
| **Categoria de Informação** | Calendário e Progresso (*Schedule and Progress*) |
| **Necessidade de Informação** | Monitorar o ritmo de entrega dos artefatos da Fase 3 e identificar bloqueios por dependências técnicas antes do início das coletas em campo. |
| **Conceito Mensurável** | Ritmo de fechamento de tarefas e pontualidade na milestone. |
| **Medidas Base** | Total de issues da fase (23), issues fechadas (18), data limite programada e data de fechamento (*closed_at*). |
| **Medidas Derivadas** | Percentual de fechamento na primeira metade da fase, volume fechado nos dois últimos dias, percentual fechado no prazo e issues bloqueadas. |
| **Critério de Decisão** | Alerta de ritmo disparado quando menos de 50% das issues são concluídas na primeira metade do período ou quando a aderência ao prazo cai abaixo de 80%. |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>

### 2.2. Construct 2: Recursos e Custos

<p className="tabela-titulo">Tabela 2: Measurement Construct para Recursos e Custos na Fase 3</p>

| Elemento do Construct | Especificação |
| :--- | :--- |
| **Categoria de Informação** | Recursos e Custos (*Resources and Cost*) |
| **Necessidade de Informação** | Avaliar a precisão das estimativas de esforço individual e coletivo na Fase 3, verificar o custo financeiro equivalente e controlar o equilíbrio de dedicação entre os integrantes. |
| **Conceito Mensurável** | Acerto das estimativas de esforço por issue e percentual de participação individual. |
| **Medidas Base** | Horas estimadas e horas reais por issue e por integrante, taxa horária de referência de R$ 45,00 por hora (Júnior CLT via Novo CAGED). |
| **Medidas Derivadas** | Desvio por issue, desvio agregado da fase, percentual de issues na faixa ideal (entre -20% e +20%) e percentual de esforço por integrante. |
| **Critério de Decisão** | Desvio agregado fora da faixa de -20% a +20% sinaliza erro sistemático de estimativa. Participação individual fora da faixa de 8% a 30% exige redistribuição de tarefas na fase seguinte. |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>

### 2.3. Construct 3: Desempenho dos Processos

<p className="tabela-titulo">Tabela 3: Measurement Construct para Desempenho dos Processos na Fase 3</p>

| Elemento do Construct | Especificação |
| :--- | :--- |
| **Categoria de Informação** | Desempenho dos Processos (*Process Performance*) |
| **Necessidade de Informação** | Avaliar o rigor do processo de revisão por pares e o tempo de retenção das contribuições em pull requests antes da integração no branch principal. |
| **Conceito Mensurável** | Taxa de revisão formal de PRs e tempo de espera até a primeira revisão. |
| **Medidas Base** | Total de PRs integrados (17), PRs com aprovação formal registrada (12), instante de abertura e instante da primeira revisão por outro integrante. |
| **Medidas Derivadas** | Taxa de aprovação formal (%), tempo médio e mediano de espera (horas), percentis P80 e P90 de espera, e contagem de PRs com espera superior a 24 horas. |
| **Critério de Decisão** | Meta de 100% de PRs revisados formalmente. Tempo de espera mediano inferior a 24 horas e nenhum PR esperando mais de 48 horas. |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>

---

## 3. Medições Registradas da Fase 3

### 3.1. Calendário e Progresso

A milestone da Fase 3 cobriu o intervalo de 26/10/2026 a 08/11/2026, totalizando 13 dias de execução após a extensão aprovada pela equipe. Os dados apurados registram 23 issues vinculadas à fase, sendo 18 concluídas até a data de apuração deste relatório e 5 ainda em andamento ou em fase de finalização da documentação.

<p className="tabela-titulo">Tabela 4: Ritmo de fechamento das issues na Fase 3</p>

| Indicador | Meta do Plano | Valor Observado | Situação |
| :--- | :---: | :---: | :---: |
| Total de issues planejadas | N/A | 23 issues | Conforme |
| Issues concluídas | 100% | 18 issues (78,3%) | Parcial |
| Concluídas até a data média (02/11/2026 11:59) | $\ge 50,0\%$ | 0 issues (0,0%) | Não conforme |
| Concluídas nos 2 últimos dias da fase | $\le 30,0\%$ | 7 issues (38,9%) | Não conforme |
| Concluídas após o prazo final da milestone | 0 | 9 issues | Não conforme |
| Aderência aos prazos programados | $\ge 80,0\%$ | 2 issues no prazo (8,7%) | Crítico |
| Issues com bloqueio ativo | 0 | 1 issue (#105) | Atenção |
| Alerta de ritmo disparado | Não | Sim | Alerta ativo |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>

O ritmo de entregas da Fase 3 sofreu forte retenção no início do ciclo. Nenhuma issue foi fechada durante a primeira metade da fase (até 02/11). As entregas concentraram-se entre os dias 06/11 e 12/11, gerando o fechamento tardio de 9 tarefas após a data limite da milestone (08/11). A issue #105 (atualização do GitPage com a Fase 3) permaneceu bloqueada pela issue #104 (visão geral da fase), demonstrando que o encadeamento de tarefas continuou gerando efeito cascata no cronograma.

### 3.2. Recursos e Custos

O orçamento previsto para a Fase 3 foi de 48,0 horas estimadas (equivalente a R$ 2.160,00), e o esforço real registrado nas 18 issues concluídas totalizou 47,0 horas reais (equivalente a R$ 2.115,00).

<p className="tabela-titulo">Tabela 5: Recursos e custos consolidados da Fase 3</p>

| Métrica Orçamentária | Valor Estimado | Valor Real | Variação |
| :--- | :---: | :---: | :---: |
| Esforço Total da Fase | 48,0 h | 47,0 h | -2,1% |
| Custo Financeiro Equivalente (R$ 45,00/h) | R$ 2.160,00 | R$ 2.115,00 | -R$ 45,00 |
| Custo Acumulado (Fases 1, 2 e 3) | R$ 8.010,00 | R$ 7.681,95 | -4,1% |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>

Embora o esforço total agregado tenha ficado próximo do total orçado (-2,1%), a avaliação individual das estimativas por issue revelou variações expressivas nas tarefas técnicas:

<p className="tabela-titulo">Tabela 6: Acerto das estimativas por issue na Fase 3</p>

| Indicador de Acurácia | Meta do Plano | Resultado Observado | Situação |
| :--- | :---: | :---: | :---: |
| Issues avaliadas com horas registradas | N/A | 15 issues | Conforme |
| Desvio médio da fase | $\pm 20,0\%$ | +38,2% | Subestimação geral |
| Desvio mediano por issue | $0,0\%$ | 0,0% | Neutro |
| Issues na faixa ideal (-20% a +20%) | $\ge 70,0\%$ | 7 de 15 issues (46,7%) | Parcial |
| Issues subestimadas (desvio > +20%) | $\le 15,0\%$ | 7 issues (46,7%) | Crítico |
| Issues superestimadas (desvio < -20%) | $\le 15,0\%$ | 1 issue (6,7%) | Conforme |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>

O desvio médio de +38,2% ocorreu porque as tarefas de preparação de ambientes e testes operacionais demandaram mais tempo do que o previsto. Dentre as tarefas subestimadas destacam-se a issue #96 (recursos e ambiente de avaliação), que consumiu 7,0h reais frente a 2,0h estimadas (+250%), a issue #99 (instruções de G2), com 6,0h reais para 3,0h estimadas (+100%), a issue #97 (massa de dados), com 5,0h reais para 3,0h estimadas (+66,7%), e a issue #94 (estudo do processo), com 3,0h reais para 2,0h estimadas (+50%).

A distribuição do esforço real entre os integrantes na Fase 3 apresentou o seguinte quadro:

<p className="tabela-titulo">Tabela 7: Contribuição individual no esforço real da Fase 3</p>

| Integrante | Login GitHub | Issues Atribuídas | Horas Estimadas (h) | Horas Reais (h) | Custo Real (R$) | Participação na Fase (%) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| Christopher | `wChrstphr` | 5 | 8,50 | 5,50 | R$ 247,50 | 11,70% |
| Davi Pierre | `DaviPierre` | 5 | 12,00 | 13,00 | R$ 585,00 | 27,66% |
| Gabriel Monteiro | `GabrielSMonteiro` | 5 | 12,00 | 10,00 | R$ 450,00 | 21,28% |
| Letícia de Carvalho | `LeticiaSantosss` | 5 | 9,50 | 14,50 | R$ 652,50 | 30,85% |
| Luiz Henrique Soares | `luizh-gsoares` | 0 | 0,00 | 0,00 | R$ 0,00 | 0,00% |
| Maria Eduarda | `eduarda-ogomes` | 3 | 6,00 | 4,00 | R$ 180,00 | 8,51% |
| **Total** | - | **23** | **48,00** | **47,00** | **R$ 2.115,00** | **100,00%** |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>

Dois desvios em relação à faixa de equilíbrio (8% a 30%) foram registrados:
1. Luiz Henrique obteve 0,0% de participação na Fase 3, pois a divisão de trabalho da equipe alocou seus esforços na revisão das páginas e na finalização de artefatos da Fase 2, além de concentrar suas atribuições técnicas na execução da Fase 4.
2. Letícia atingiu 30,85%, ultrapassando pontualmente o limite superior devido ao acúmulo de esforço na conteinerização Docker da issue #96 e na elaboração do roteiro de testes de confiabilidade da issue #99.

### 3.3. Desempenho dos Processos

O fluxo de revisão de código e documentação foi avaliado a partir dos 17 pull requests vinculados à Fase 3:

<p className="tabela-titulo">Tabela 8: Indicadores de processo e revisão por pares na Fase 3</p>

| Indicador de Processo | Meta do Plano | Resultado Observado | Situação |
| :--- | :---: | :---: | :---: |
| Total de Pull Requests | N/A | 17 PRs | Conforme |
| PRs integrados com aprovação formal | 100% | 12 de 17 PRs (70,6%) | Evolução positiva |
| PRs integrados sem revisão formal | 0 | 5 PRs (29,4%) | Não conforme |
| Tempo médio de espera da primeira revisão | $\le 24,0$ h | 23,34 h | Conforme |
| Tempo mediano de espera da primeira revisão | $\le 12,0$ h | 22,19 h | Atenção |
| Percentil 80 (P80) de espera | $\le 24,0$ h | 45,90 h | Não conforme |
| Percentil 90 (P90) de espera | $\le 36,0$ h | 46,19 h | Não conforme |
| PRs com espera superior a 24 horas | 0 | 4 PRs (#137, #139, #141, #144) | Atenção |
| Lead Time médio das tarefas | $\le 4,0$ dias | 5,97 dias | Atenção |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>

A taxa de revisão formal atingiu 70,6% (12 PRs com aprovação registrada no GitHub), demonstrando avanço em relação às fases anteriores. Entretanto, 5 PRs foram integrados sem registro formal de aprovação na API (#132, #142, #143, #159 e #160), decorrentes de revisões realizadas verbalmente em reuniões síncronas.

O tempo de espera até a primeira revisão teve mediana de 22,19h e média de 23,34h. Quatro PRs permaneceram aguardando por mais de 24 horas: o PR #137 esperou 61,74h, o PR #139 esperou 46,19h, o PR #141 esperou 45,90h e o PR #144 esperou 26,16h.

<p className="tabela-titulo">Tabela 9: Distribuição de revisões de pull request por integrante na Fase 3</p>

| Revisor | Login GitHub | PRs Revisados | Participação nas Revisões (%) |
| :--- | :--- | :---: | :---: |
| Maria Eduarda | `eduarda-ogomes` | 7 | 58,3% |
| Christopher | `wChrstphr` | 4 | 33,3% |
| Luiz Henrique Soares | `luizh-gsoares` | 1 | 8,3% |
| Davi Pierre | `DaviPierre` | 0 | 0,0% |
| Gabriel Monteiro | `GabrielSMonteiro` | 0 | 0,0% |
| Letícia de Carvalho | `LeticiaSantosss` | 0 | 0,0% |
| **Total** | - | **12** | **100,0%** |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>

A carga de revisão de código e artefatos concentrou-se fortemente em dois integrantes: Maria Eduarda realizou 58,3% das revisões formais e Christopher realizou 33,3%, somando 91,6% de todas as avaliações de PR da fase.

---

## 4. Comparação com as Fases 1 e 2

A análise comparativa entre as três primeiras etapas do projeto permite identificar as tendências operacionais da equipe ao longo do semestre:

<p className="tabela-titulo">Tabela 10: Comparação de indicadores entre as Fases 1, 2 e 3</p>

| Indicador de Gestão | Fase 1 | Fase 2 | Fase 3 | Tendência Observada |
| :--- | :---: | :---: | :---: | :--- |
| Escopo total de issues | 18 issues | 29 issues | 23 issues | Escopo técnico equilibrado |
| Issues concluídas na data de apuração | 18 (100,0%) | 29 (100,0%) | 18 (78,3%) | Fase 3 em fechamento ativo |
| Aderência aos prazos programados | 33,3% | 48,3% | 8,7% | Piora sensível na pontualidade |
| Horas estimadas totais | 59,5 h | 70,5 h | 48,0 h | Redução do esforço planejado |
| Horas reais consumidas | 59,0 h | 64,7 h | 47,0 h | Aderência orçamentária global mantida |
| Custo financeiro real equivalente | R$ 2.655,45 | R$ 2.911,50 | R$ 2.115,00 | Custos alinhados com o orçamento |
| Desvio médio de estimativa por issue | -0,8% | -8,2% | +38,2% | Subestimação acentuada na Fase 3 |
| Issues com estimativa na faixa ideal | 50,0% | 61,5% | 46,7% | Redução da acurácia por tarefa |
| Taxa de aprovação formal de PRs | 47,1% | 48,1% | 70,6% | Aumento da taxa de aprovação formal |
| PRs com espera superior a 24 horas | 1 PR | 1 PR | 4 PRs | Aumento de retenção de PRs complexos |
| Lead Time médio das tarefas | 1,21 dias | 3,74 dias | 5,97 dias | Ciclo de vida das tarefas mais longo |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>

A comparação evidencia três dinâmicas centrais:
1. **Pontualidade e Ritmo:** A taxa de aderência ao prazo caiu de 48,3% na Fase 2 para 8,7% na Fase 3. Na Fase 2 a equipe agrupou tarefas sob os mesmos autores, o que melhorou o fluxo. Na Fase 3, as tarefas dependeram de validação técnica sequencial (ambiente, massa e piloto), o que reintroduziu esperas em cadeia e adiou as entregas.
2. **Qualidade das Estimativas:** Enquanto as Fases 1 e 2 apresentaram desvios médios contidos (-0,8% e -8,2%), a Fase 3 registrou desvio de +38,2%, com 46,7% das tarefas subestimadas. Tarefas de planejamento de teste e configuração de ambiente envolveram atritos com versões de bibliotecas e contêineres que não existiam nas fases puramente documentais.
3. **Maturidade de Revisão:** A taxa de aprovação formal de PRs subiu de 47,1% (Fase 1) e 48,1% (Fase 2) para 70,6% na Fase 3, mostrando que a equipe passou a utilizar os mecanismos do GitHub de forma mais disciplinada. Por outro lado, o volume de revisores diminuiu, sobrecarregando Maria Eduarda e Christopher e fazendo o tempo de espera P80 saltar de 7,53h (Fase 2) para 45,90h (Fase 3).

---

## 5. Análise do Efeito da Mudança do Prazo da Milestone

A data limite original da milestone da Fase 3 era 03/11/2026. Durante a execução, a equipe estendeu o prazo em 5 dias, fixando o término da milestone em 08/11/2026.

### 5.1. Motivação da Extensão

A prorrogação foi motivada por dificuldades imprevistas na preparação prática dos instrumentos de avaliação:
- A configuração do contêiner Docker oficial e a validação do monorepo local para viabilizar as métricas de Confiabilidade (G2) e Manutenibilidade (G1).
- A geração da massa de dados sintética de desenhos no formato JSON do Excalidraw, necessária para submeter o aplicativo a diferentes cargas de elementos gráficos.
- A elaboração de roteiros passo a passo com critérios de pontuação claros, reduzindo a ambiguidade para os avaliadores que executarão a Fase 4.

### 5.2. Impacto Quantitativo no Cronograma

Apesar da ampliação de 5 dias no prazo global da milestone, a taxa de aderência aos prazos programados nas issues permaneceu em 8,7% (apenas 2 issues concluídas no prazo original registrado nos metadados). Esse resultado decorreu de três fatores:
1. Os prazos das issues individuais não foram repactuados quando a milestone foi estendida, permanecendo vinculados às estimativas iniciais do ciclo.
2. Sete issues fecharam na janela final da nova milestone (dias 07/11 e 08/11), demonstrando que o prazo estendido absorveu o trabalho, mas postergou o esforço para o novo limite.
3. Nove issues ultrapassaram a data limite estendida de 08/11, fechando entre 09/11 e 13/11, incluindo artefatos de apoio como a automação do script PSM (#135) e a homologação do teste piloto (#103).

A extensão de prazo foi necessária para garantir a consistência técnica dos roteiros de teste, evitando que a equipe iniciasse a coleta em campo com instrumentos falhos. Contudo, a medição evidenciou que estender a milestone sem antecipar os gargalos de dependência reproduziu a concentração de entregas na véspera.

---

## 6. Interpretação e Decisões de Gestão

Em continuidade às decisões D1 a D6 registradas na Linha de Base da Entrega 1 no [Registro de Medições e Decisões](../registro-medicoes.md), a equipe formalizou quatro novas decisões de gestão (D7 a D10) a partir dos resultados apurados na Fase 3:

### Decisão D7: Rebalanceamento de Carga Individual para a Fase 4
- **Diagnóstico:** Luiz Henrique ficou com 0,0% de esforço registrado na Fase 3, descumprindo o piso de 8% da equipe, enquanto Letícia atingiu 30,85%, ultrapassando o teto de 30%. Davi e Gabriel concentraram cerca de 27% e 21% da fase.
- **Ação adotada:** Atribuir a Luiz Henrique o papel principal em 8 tarefas da Fase 4, totalizando 23,0 horas estimadas, abrangendo a preparação do ambiente de medidas (#110), a coleta de métricas de confiabilidade (#112), a análise de dados de G2 (#116), a síntese do julgamento final (#120) e as conclusões do artigo científico (#125). Em contrapartida, as tarefas de coleta prática da Fase 4 foram aliviadas para Letícia.
- **Impacto esperado:** Reequilibrar a participação acumulada da equipe na Entrega 2, mantendo todos os membros dentro da faixa de 8% a 30% no balanço consolidado.

### Decisão D8: Aplicação de Fator de Calibração de 1,3x em Tarefas Técnicas
- **Diagnóstico:** A acurácia das estimativas da Fase 3 apresentou desvio médio de +38,2%, com 7 de 15 issues subestimadas, concentradas em atividades práticas que envolveram ferramentas externas, compilação de código e geração de dados sintéticos.
- **Ação adotada:** Aplicar fator de correção de 1,3x nas estimativas de esforço das tarefas da Fase 4 que envolvam manipulação de ferramentas de teste (Docker, SonarQube, Stryker e Cypress), mantendo estimativas regulares apenas para redação documental pura.
- **Impacto esperado:** Conter estouros de cronograma e elevar o percentual de issues concluídas dentro da faixa ideal de estimativa para mais de 70% na Fase 4.

### Decisão D9: Acordo de Nível de Serviço (SLA) de 24 Horas para Revisão de Pull Requests
- **Diagnóstico:** Embora a taxa de aprovação formal tenha alcançado 70,6%, quatro PRs aguardaram mais de 24 horas pela primeira revisão, com casos extremos de 46h e 61h. Além disso, 91,6% das revisões ficaram a cargo de apenas dois membros.
- **Ação adotada:** Estabelecer que todo integrante ao concluir sua tarefa diária deve verificar e revisar os PRs pendentes antes de iniciar nova issue. Fixar tempo máximo de 24 horas corridas para a emissão do primeiro parecer em qualquer PR aberto.
- **Impacto esperado:** Reduzir o tempo de espera mediano para menos de 12 horas, zerar PRs com retenção acima de 24 horas e distribuir a carga de revisão entre os seis integrantes na Fase 4.

### Decisão D10: Abertura Imediata e Desacoplamento das Tarefas da Fase 4
- **Diagnóstico:** A baixa aderência ao prazo na Fase 3 (8,7%) decorreu do acoplamento estrito entre etapas conceituais e operacionais, aliado à abertura tardia de issues de infraestrutura no GitHub Projects.
- **Ação adotada:** Abrir e detalhar todas as issues da Fase 4 desde o primeiro dia da milestone, permitindo que a infraestrutura (#110) e a coleta antecipada de Flexibilidade (#113) avancem em paralelo com as coletas de Manutenibilidade e Confiabilidade, sem esperar o término formal das documentações da Fase 3.
- **Impacto esperado:** Aumentar a taxa de conclusão de tarefas na primeira metade do ciclo e elevar a taxa de aderência aos prazos programados para mais de 70%.

---

## 7. Rastreabilidade com os Dados Primários

Os dados quantitativos e indicadores apresentados neste relatório são respaldados pelos artefatos e dados primários disponíveis no repositório:
- Script de coleta e processamento: `scripts/coleta_psm.py`
- Dados brutos em formato JSON: `dados/gestao/raw_github_data.json`
- Detalhamento de issues por fase: `dados/gestao/05_detalhamento_issues.csv`
- Contribuição e horas por integrante: `dados/gestao/06_contribuicao_por_fase.csv`
- Métricas e tempos de espera de pull requests: `dados/gestao/07_metricas_pull_requests.csv`
- Resumo consolidado de processos: `dados/gestao/03_desempenho_processos_fases.csv`
- [Plano de Medição PSM](../plano-medicao-psm.md)
- [Painel de Medição PSM](../painel-psm.md)
- [Registro de Medições e Decisões](../registro-medicoes.md)

---

## Referências

1. FCTE. **AULA 09 QSW1 PSM resumo**. Universidade de Brasília, Faculdade de Ciências e Tecnologias em Engenharia, 2026.
2. CARD, David et al. **Practical Software and Systems Measurement (PSM): A Foundation for Objective Project Management**. Version 4.0d. PSM Support Center, 2021.
3. ISO/IEC. **ISO/IEC 15939: Systems and software engineering: Measurement process**. International Organization for Standardization, Genebra, 2017.
4. ISO/IEC. **ISO/IEC 25040: Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): Evaluation process**. International Organization for Standardization, Genebra, 2011.

---

## Histórico de Versões

<p className="tabela-titulo">Tabela 11: Histórico de versões do documento</p>

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 12/11/2026 | Registro das medições PSM/CID da Fase 3, comparação com as Fases 1 e 2, análise da extensão de prazo e decisões de gestão D7 a D10 | [Gabriel Monteiro](https://github.com/GabrielSMonteiro) | |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>
