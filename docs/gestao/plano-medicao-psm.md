---
id: plano-medicao-psm
title: Plano de Medição PSM/CID
sidebar_label: Plano de Medição PSM
sidebar_position: 1
description: Plano de medição do projeto baseado nas necessidades de informação da equipe, measurement constructs (ISO/IEC 15939) e critérios de decisão práticos.
---

import Link from '@docusaurus/Link';

# Plano de Medição PSM/CID

Este documento define o **Plano de Medição** da equipe Karen Jones para o projeto de avaliação de qualidade do software **Excalidraw**, fundamentado na norma **ISO/IEC 15939** e no método **Practical Software and Systems Measurement (PSM/CID)** [[1]](#ref-1).

Na apresentação das métricas PSM de 04/11/2026, a professora orientou que as métricas de gestão devem responder a perguntas que ajudem a equipe a monitorar e aprimorar o próprio processo de desenvolvimento de software, indicando como referência o trabalho desenvolvido pela equipe **T01 Mary Jackson** [[2]](#ref-2). 

Em versões anteriores (Fases 1 e 2), a medição continha *measurement constructs* com necessidades de informação genéricas, e as decisões nem sempre se conectavam a ações operacionais no repositório. Este plano refaz a estrutura de medição do projeto inteiro para as Fases 1 a 4, estabelecendo uma medida por categoria de informação, partindo de perguntas reais da equipe e definindo critérios de decisão vinculados a ações concretas.

O detalhamento analítico do PSM/CID concentra-se no GitPage da equipe, mantendo no artigo acadêmico o apêndice de contribuição e uso de inteligência artificial.

---

## 1. Origem das Medidas e Perguntas da Equipe

A especificação da disciplina exige medidas cobrindo três categorias de informação do PSM [[3]](#ref-3). Cada medida foi selecionada na **Tabela 5 do PSM/CID Parte 1** [[1, p. 19-24]](#ref-1) e adaptada para responder diretamente aos desafios observados no fluxo de trabalho:

<p className="tabela-titulo">Tabela 1: Categorias de informação, conceitos mensuráveis e perguntas da equipe</p>

| Categoria de Informação (PSM) | Conceito Mensurável | Medida no PSM/CID (Tabela 5) | Pergunta Orientadora da Equipe |
| :--- | :--- | :--- | :--- |
| **1. Calendário e Progresso** (*Schedule and Progress*) | Progresso das unidades de trabalho (*Work Unit Progress*) | *Committed vs. Completed Work Items* (Linha 1) | **As issues da fase fecham ao longo da fase ou se acumulam na véspera da entrega por bloqueios de dependência?** |
| **2. Recursos e Custos** (*Resources and Cost*) | Desempenho financeiro e esforço (*Financial Performance*) | *Estimate vs. Actual Effort* (Linha 8) e *Estimation Accuracy* (Linha 9) | **Nossas estimativas de esforço por issue são confiáveis o bastante para planejar a fase seguinte?** |
| **3. Desempenho dos Processos** (*Process Performance*) | Eficiência e velocidade do processo (*Process Efficiency Speed*) | *Cycle Time* (Linha 32) e *Peer Review Efficiency* | **Quanto tempo um Pull Request espera por revisão até o merge, e quem está revisando?** |

<p className="tabela-fonte">Fonte: [Maria Eduarda](https://github.com/eduarda-ogomes), com base no PSM/CID Parte 1 [[1]](#ref-1) e na equipe T01 Mary Jackson [[2]](#ref-2), 2026.</p>

---

## 2. Instâncias do Modelo de Informação (Measurement Constructs)

Os três *Measurement Constructs* seguem rigorosamente o **template oficial de 15 campos da disciplina** (Aula 09, slide 19) [[4, p. 19]](#ref-4), derivado da norma **ISO/IEC 15939**.

### 2.1. Construct 1: Calendário e Progresso: Ritmo de Fechamento e Dependências

A equipe identificou na Entrega 1 um gargalo significativo: as tarefas foram distribuídas sem atentar para o caminho crítico de dependências entre issues. Integrantes que dependiam de documentos base ficaram com o trabalho travado aguardando colegas com agendas sobrecarregadas, o que empurrou a conclusão das tarefas para a véspera dos marcos. Este construct avalia se o fechamento ocorre de forma contínua ou em lote, integrando-se à [Priorização no Project](priorizacao-issues.md).

<p className="tabela-titulo">Tabela 2: Measurement Construct de Calendário e Progresso</p>

| Campo do Template (Aula 09, p. 19) | Especificação no Projeto Karen Jones |
| :--- | :--- |
| **Categoria de Informação** | Calendário e Progresso (*Schedule and Progress*) |
| **Necessidade de Informação** | Saber se as issues fecham de maneira cadenciada ao longo do cronograma da fase ou se acumulam na véspera por bloqueios de dependência em cascata. |
| **Conceito Mensurável** | Ritmo de progresso das unidades de trabalho (*Work Unit Progress — Committed vs. Completed*). |
| **Entidades Relevantes** | Tarefas (*issues*) vinculadas às *milestones* das Fases 1 a 4 no GitHub. |
| **Atributos** | Estado da issue (`open` ou `closed`), data de criação (`created_at`), data de fechamento (`closed_at`), campo `Prazo`, campo `Depende de` e nível de `Prioridade` no Project. |
| **Medidas Básicas** | 1. `Total_Issues`: total de issues planejadas para a fase.<br/>2. `Issues_Fechadas`: contagem de issues fechadas.<br/>3. `Data_Fechamento`: timestamp exato de fechamento de cada issue.<br/>4. `Issues_Bloqueadas`: issues abertas cujo `Depende de` possui ao menos uma issue ainda aberta. |
| **Método de Medição** | Leitura diária e automática da API REST do GitHub via script `scripts/coleta_psm.py` e extração de dependências para o Project. |
| **Tipo de Método de Medição** | Objetivo. |
| **Escala** | Inteiros não negativos e timestamps de calendário. |
| **Tipo de Escala** | Razão (*Ratio*) para contagens; Intervalar para datas. |
| **Unidade de Medida** | Unidade de trabalho (issue) e data/hora. |
| **Medidas Derivadas** | 1. **Progresso da Fase (%):** `(Issues_Fechadas / Total_Issues) × 100`<br/>2. **Taxa de Fechamento na 1ª Metade (%):** percentual de issues fechadas até a data média da fase.<br/>3. **Aderência ao Prazo (%):** percentual de issues fechadas até o dia do campo `Prazo`. |
| **Função de Medição** | Cálculo aritmético sobre os registros de data extraídos dos metadados das issues. |
| **Indicador** | Curva S de esforço acumulado planejado vs. realizado (`dados/gestao/graficos/08_desempenho_execucao_curva_s.png`), tabela de aderência e quadro kanban ordenado por `Prioridade` e `Prazo`. |
| **Modelo de Análise** | Fechamento contínuo apresenta inclinação constante ao longo da fase; fechamento em "degrau" ou "efeito manada" nos últimos 2 dias sinaliza gargalo operacional por dependência ou subestimação. |
| **Critérios de Decisão** | **1. Ritmo de Execução:** Se na metade do tempo da fase o progresso for inferior a 50%, a equipe realiza reunião extraordinária na leitura de quarta-feira para redistribuir escopo.<br/>**2. Desbloqueio de Dependências:** Issue com prioridade `Alta` (trava 15+ issues) ou `Média` (trava 5 a 14 issues) aberta a 48h do prazo aciona pareamento imediato ou divisão de trabalho. |

<p className="tabela-fonte">Fonte: [Maria Eduarda](https://github.com/eduarda-ogomes), 2026.</p>

---

### 2.2. Construct 2: Recursos e Custos: Acurácia das Estimativas de Esforço

O planejamento das entregas seguintes depende diretamente da fidelidade das estimativas de esforço. Subestimar horas sobrecarrega os membros e gera atrasos; superestimar infla o custo e subutiliza a capacidade técnica.

<p className="tabela-titulo">Tabela 3: Measurement Construct de Recursos e Custos</p>

| Campo do Template (Aula 09, p. 19) | Especificação no Projeto Karen Jones |
| :--- | :--- |
| **Categoria de Informação** | Recursos e Custos (*Resources and Cost*) |
| **Necessidade de Informação** | Avaliar se as estimativas de esforço da equipe são precisas o suficiente para dimensionar a alocação de tarefas nas fases subsequentes sem sobrecarga. |
| **Conceito Mensurável** | Desempenho financeiro e acurácia de estimativa de esforço (*Estimation Accuracy — Estimate vs. Actual Effort*). |
| **Entidades Relevantes** | Tarefas (*issues*) com seções "Estimativa (h)" e "Horas reais (h)" preenchidas. |
| **Atributos** | Esforço previsto na abertura da issue e esforço real gasto reportado no fechamento. |
| **Medidas Básicas** | 1. `E` = Horas estimadas da issue (número real em horas).<br/>2. `R` = Horas reais executadas da issue (com suporte a rateio por integrante `@usuario: N`).<br/>3. `Vh` = Valor-hora de referência da equipe (R$ 45,00/h, baseado em salário de Engenheiro de Software Júnior, CBO 2124-05, Novo CAGED/MTE). |
| **Método de Medição** | Extração automatizada das seções Markdown dos corpos das issues via expressão regular no script `scripts/coleta_psm.py`. |
| **Tipo de Método de Medição** | 1. Subjetivo (estimativa de engenharia do responsável na abertura). 2. Objetivo (apuração das horas gastas no fechamento). |
| **Escala** | Números reais positivos de zero ao infinito. |
| **Tipo de Escala** | Razão (*Ratio*). |
| **Unidade de Medida** | Horas (h) e Moeda corrente (Reais — R$). |
| **Medidas Derivadas** | 1. **Acurácia da Fase (%):** `(Soma(R) / Soma(E)) × 100`<br/>2. **Desvio de Esforço (%):** `((Soma(R) - Soma(E)) / Soma(E)) × 100`<br/>3. **Custo Real da Fase (R$):** `Soma(R) × 45,00` |
| **Função de Medição** | Razão percentual entre horas reais e horas estimadas acumuladas por fase e entrega. |
| **Indicador** | Gráfico de acurácia por fase em relação à faixa ideal (`static/img/gestao/06_acuracia_estimativa_fases.png`) e tabela comparativa de esforço e custo. |
| **Modelo de Análise** | Acurácia ideal situa-se na faixa de **80% a 120%** (desvio de até ±20%). Valores acima de 120% indicam subestimação do esforço; valores abaixo de 80% indicam superestimação. |
| **Critérios de Decisão** | **1. Recalibração de Planejamento:** Se a acurácia de uma fase consolidada fechar fora da faixa `[80%, 120%]`, as estimativas da fase seguinte devem ser recalibradas coletivamente na reunião semanal (se subestimada, aplicar fator corretivo de 1,2× no planejamento).<br/>**2. Equilíbrio de Carga:** Integrante que acumular participação inferior a 8% ou superior a 30% do esforço da entrega tem tarefas redistribuídas imediatamente. |

<p className="tabela-fonte">Fonte: [Maria Eduarda](https://github.com/eduarda-ogomes), 2026.</p>

---

### 2.3. Construct 3: Desempenho dos Processos: Tempo de Espera por Revisão de PR

Na Entrega 1, tarefas interdependentes muitas vezes demoravam a ser integradas não porque o autor não havia produzido o artefato, mas porque o Pull Request aguardava dias pela revisão dos pares na fila do repositório. Este construct monitora a fluidez da esteira de revisão para evitar que a etapa de validação se torne um gargalo silencioso.

<p className="tabela-titulo">Tabela 4: Measurement Construct de Desempenho dos Processos</p>

| Campo do Template (Aula 09, p. 19) | Especificação no Projeto Karen Jones |
| :--- | :--- |
| **Categoria de Informação** | Desempenho dos Processos (*Process Performance*) |
| **Necessidade de Informação** | Saber quanto tempo um Pull Request aguarda por revisão até o merge, se a revisão por pares está sendo cumprida formalmente e quem está revisando as entregas. |
| **Conceito Mensurável** | Eficiência e velocidade do processo de revisão (*Peer Review Efficiency & PR Review Lead Time*). |
| **Entidades Relevantes** | Pull Requests integrados e abertos no repositório GitHub. |
| **Atributos** | Timestamp de abertura do PR (`created_at`), timestamp da primeira submissão de revisão (`submitted_at`), timestamp de merge (`merged_at`), autor do PR e revisores aprovadores (`reviews`). |
| **Medidas Básicas** | 1. `T_abertura`: data/hora de abertura do PR.<br/>2. `T_revisao`: data/hora da aprovação formal de revisão.<br/>3. `T_merge`: data/hora do merge na branch `main`.<br/>4. `Revisores`: login dos integrantes que realizaram a aprovação formal via GitHub. |
| **Método de Medição** | Apuração de Pull Requests e revisores no GitHub. A automação completa via script coletor está em implementação na issue [#135](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/135), sendo realizada atualmente de forma manual e auditável pela equipe. |
| **Tipo de Método de Medição** | Objetivo. |
| **Escala** | Datas de calendário e números reais não negativos. |
| **Tipo de Escala** | Intervalar para timestamps; Razão para tempo decorrido. |
| **Unidade de Medida** | Horas e dias úteis. |
| **Medidas Derivadas** | 1. **Tempo de Espera por Revisão (dias):** `Média(T_revisao - T_abertura)`<br/>2. **Taxa de Revisão Formal por Pares (%):** `(PRs com Aprovação Formal / Total de PRs Integrados) × 100`<br/>3. **Distribuição de Revisores:** proporção de revisões feitas por cada integrante da equipe. |
| **Função de Medição** | Diferença temporal exata entre a abertura do PR e a revisão formal aprovada no GitHub. |
| **Indicador** | Tabela de tempo de espera e taxa de aprovação por fase, além da matriz de autores vs. revisores. |
| **Modelo de Análise** | Tempo de espera superior a 1 dia útil (24h) indica sobrecarga dos revisores ou falta de priorização; taxa de revisão formal abaixo de 100% viola a política de contribuição (`CONTRIBUTING.md`). |
| **Critérios de Decisão** | **1. Alerta de PR Travado:** Todo PR aberto há mais de **24 horas úteis (1 dia)** sem revisão gera notificação direta ao revisor indicado no grupo de comunicação; se atingir 48h, o papel de revisor é reatribuído a qualquer outro integrante disponível.<br/>**2. Conformidade Rigorosa:** Nenhum merge direto por autor é permitido; PRs sem aprovação formal no GitHub bloqueiam o fechamento da issue correspondente. |

<p className="tabela-fonte">Fonte: [Maria Eduarda](https://github.com/eduarda-ogomes), 2026.</p>

---

## 3. Linha de Base das Fases 1 e 2 (Dados Históricos)

Para apoiar as decisões das Fases 3 e 4, a equipe compilou os dados auditados das Fases 1 e 2, consolidados em `dados/gestao/` e apresentados detalhadamente no [Painel de Medição PSM](painel-psm.md) e no [Registro de Medições](registro-medicoes.md):

<p className="tabela-titulo">Tabela 5: Linha de base comparativa entre Fase 1, Fase 2 e Entrega 1</p>

| Indicador de Gestão | Fase 1 (Requisitos) | Fase 2 (GQM & Artigo E1) | Consolidado Entrega 1 (F1 + F2) | Meta do Construct | Análise da Linha de Base |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Issues Concluídas / Total** | 17 / 17 | 27 / 27 | **44 / 44** | 100% | Escopo da Entrega 1 integralmente concluído. |
| **Horas Estimadas (h)** | 53,50 h | 62,50 h | **116,00 h** | — | Planejamento acumulado da Entrega 1. |
| **Horas Reais Executadas (h)** | 57,91 h | 56,40 h | **114,31 h** | — | 100% das horas registradas com rastreabilidade. |
| **Acurácia da Estimativa (%)** | 108,2% | 90,2% | **98,5%** | 80% a 120% | Atendido. Ambas as fases situaram-se na faixa ideal. |
| **Custo Real Investido (R$)** | R$ 2.605,95 | R$ 2.538,00 | **R$ 5.143,95** | $\le$ R$ 5.220,00 | Executado abaixo do teto financeiro estimado. |
| **Aderência aos Prazos (%)** | 29,4% | 44,4% | **38,6%** | 100,0% | Não atendido. Concentração de entregas na véspera persistiu. |
| **Lead Time Médio (dias)** | 1,23 dias | 3,97 dias | **2,91 dias** | $\le$ 3,00 dias | Média ponderada das 44 issues concluídas da Entrega 1. |
| **Taxa de Revisão por Pares (%)** | 50,0% (5 de 10) | 45,0% (9 de 20) | **46,7% (14 de 30)** | 100,0% | Não atendido. Apenas revisões formais registradas via GitHub. |

<p className="tabela-fonte">Fonte: [Maria Eduarda](https://github.com/eduarda-ogomes), com base em `dados/gestao/` e no [Painel de Medição PSM](painel-psm.md), 2026.</p>

### 3.1. Diagnóstico da Linha de Base: O Efeito das Dependências

A inspeção detalhada da linha de base confirma a dinâmica observada:
1. **Fase 1 (Aderência de 29,4%):** As 12 issues fechadas em atraso foram encerradas em lote em 19/10/2026 (véspera da entrega). Tarefas como GitPage (`#18`), Escopo (`#13`) e Padronização (`#16`) dependiam diretamente das definições de Requisitos (`#8`) e Modelo (`#7`).
2. **Fase 2 (Aderência de 44,4%):** Houve avanço expressivo ao agrupar blocos GQM por integrante (`#52` a `#55`). Contudo, a redação do artigo (`#73` a `#78`) voltou a sofrer atrasos em cadeia por dependência síncrona.
3. **Ação para as Fases 3 e 4:** Essa constatação motivou a adoção do sistema de **Prioridade por Dependências no Project**, garantindo que as tarefas de cabeceira com mais dependentes sejam iniciadas no primeiro dia do ciclo.

---

## 4. Integração com a Priorização e Datas no GitHub Project

Para operacionalizar os critérios de decisão de Calendário e Progresso, o plano de medição conecta-se diretamente à página de [Priorização e datas no GitHub Project](priorizacao-issues.md) (Issue [#140](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/140)):

* **Prioridade Automatizada:** Mede o número de issues abertas que dependem, direta ou indiretamente, de uma determinada tarefa:
  * **`Alta`:** Trava **15 ou mais** issues abertas.
  * **`Média`:** Trava **de 5 a 14** issues abertas.
  * **`Normal`:** Trava **menos de 5** issues abertas.
* **Sincronização de Prazos:** A data limite interna das issues alimenta automaticamente o campo de data `Prazo` no Project #36 via mutação GraphQL no script `scripts/sincronizar_projeto.py` (Issue [#138](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/138)).
* **Recálculo Periódico:** Como a prioridade e a data sugerida de início mudam conforme as dependências são concluídas, os campos `Prioridade` e `Início` são recalculados semanalmente durante a rotina de leitura do PSM.

---

## 5. Rotina de Governança e Calendário das Leituras Semanais

Para garantir que a medição sirva como ferramenta ativa de gestão, as medições são extraídas diariamente pelo GitHub Actions (`.github/workflows/coleta-psm.yml`), e a equipe realiza reuniões de acompanhamento semanais, com interpretação dos indicadores e deliberação registrada em ata:

<p className="tabela-titulo">Tabela 6: Cronograma de reuniões e leituras de medição do PSM/CID</p>

| Marco | Data | Momento do Projeto | Pauta Principal da Leitura de Medição |
| :---: | :---: | :--- | :--- |
| **Leitura 0** | **04/11/2026** *(Quarta-feira)* | Linha de Base / Fechamento da E1 | • Analisar retrospectivamente o aprendizado da E1, acurácia e esforço.<br/>• Identificar bloqueios em cadeia e formular as decisões D1 a D6. |
| **Leitura 1** | **11/11/2026** *(Quarta-feira)* | Meio da Fase 3 e Coleta da Fase 4 | • Verificar se o ritmo de fechamento da Fase 3 atingiu $\ge 50\%$.<br/>• Auditar se há issues de prioridade `Alta` em risco de atrasar a Fase 4.<br/>• Recalcular `Prioridade` e `Início` no Project.<br/>• Verificar tempo de espera dos PRs de instruções (G1, G2, G3). |
| **Leitura 2** | **18/11/2026** *(Quarta-feira)* | Reta Final da Fase 4 e Redação Final | • Avaliar se a acurácia da Fase 4 está na faixa de 80% a 120%.<br/>• Cobrar PRs abertos há mais de 24h para destravar a consolidação do artigo e site.<br/>• Conferir o equilíbrio de esforço acumulado na Entrega 2 entre os 6 membros.<br/>• Decidir ações finais antes da Release `v2.0-E2`. |
| **Leitura 3** | **22/11/2026** *(Domingo)* | Fechamento da Entrega 2 | • Avaliar execução completa dos testes e artefatos da E2.<br/>• Fechamento do artigo SBC e consolidação final do orçamento e esforço individual. |

<p className="tabela-fonte">Fonte: [Maria Eduarda](https://github.com/eduarda-ogomes), 2026.</p>

Toda decisão adotada nessas leituras (redistribuição de tarefa, pareamento, cobrança de revisão de PR ou recalibração de estimativa) é documentada na ata da respectiva reunião em `docs/gestao/atas/` e no [Registro de Medições](registro-medicoes.md).

---

## Referências

> <Link id="ref-1">1.</Link> PRACTICAL SOFTWARE MEASUREMENT. **Practical Software and Systems Measurement: A Foundation for Objective Project Management (PSM/CID)**. Version 4.0d, CID, 2021. Disponível em: https://www.psmsc.com. Acesso em: 04 nov. 2026.
>
> <Link id="ref-2">2.</Link> EQUIPE T01 MARY JACKSON. **Plano de Medição e Registro de Medições**. Repositório 2026-2_T01_MARY_JACKSON, FCTE/UnB, 2026. Disponível em: https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T01_MARY_JACKSON/blob/main/docs/gestao/plano-de-medicao.md. Acesso em: 05 nov. 2026.
>
> <Link id="ref-3">3.</Link> **2026-2 Trabalho final completo**. Especificação do projeto final de Qualidade de Software 1, FCTE/UnB, 2026. Seção 2: Produtos de trabalho e premissas.
>
> <Link id="ref-4">4.</Link> RAMOS, Cristiane Soares. **AULA 09 QSW1 PSM resumo**. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Slides 6, 7, 19 e 23. Disponível no Moodle da disciplina.
>
> <Link id="ref-5">5.</Link> ISO/IEC/IEEE. **ISO/IEC/IEEE 15939:2017: Systems and software engineering — Measurement process**. International Organization for Standardization, Geneva, 2017.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 07/11/2026 | Elaboração do plano de medição PSM/CID com base nas necessidades reais da equipe, constructs da Aula 09, linha de base auditada e critérios de decisão | [Maria Eduarda](https://github.com/eduarda-ogomes) | [Christopher Paraizo](https://github.com/wChrstphr) |
| 1.1 | 08/11/2026 | Correção de referências, alinhamento do ciclo de 4 leituras, lead time de 2,91 dias, esclarecimento do status do Construct 3 e remoção de termos de premissa | [Maria Eduarda](https://github.com/eduarda-ogomes) | [Christopher Paraizo](https://github.com/wChrstphr) |
