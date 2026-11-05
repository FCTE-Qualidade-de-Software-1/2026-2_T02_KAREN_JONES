---
id: priorizacao-issues
title: Priorização e datas no GitHub Project
sidebar_label: Priorização no Project
sidebar_position: 2
description: Decisão da equipe sobre a prioridade das issues, measurement construct no template PSM e regras dos campos Prioridade, Início e Prazo do GitHub Project.
---

import Link from '@docusaurus/Link';

# Priorização e datas no GitHub Project

## Introdução

O PSM é uma abordagem de medição dirigida por informação, feita para apoiar quem toma decisões no projeto [[1, p. 3]](#ref-1). Nele, uma medida só se justifica se responde a uma necessidade de informação, e essas necessidades nascem de riscos, problemas e falta de informação [[1, p. 6]](#ref-1). A especificação do trabalho final também pede o registro de medições, interpretações e decisões de gestão [[2, p. 1]](#ref-2).

Os relatórios da [Fase 1](relatorios/relatorio-psm-fase-1.md) e da [Fase 2](relatorios/relatorio-psm-fase-2.md) aplicam essa abordagem depois que a fase termina. As Fases 3 e 4 trouxeram outro problema, ainda durante a execução: as issues têm prazos curtos e dependem umas das outras, então uma issue parada pode travar o trabalho de outros integrantes. O dado existia em cada issue, na seção "Depende de" exigida pela [política de contribuição](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/CONTRIBUTING.md#3-issues), mas o filtro do [Project da equipe](https://github.com/orgs/FCTE-Qualidade-de-Software-1/projects/36) não lê o corpo da issue.

Esta página registra a decisão tomada para resolver esse problema, o construct que a sustenta e as regras dos campos `Prioridade`, `Início` e `Prazo`. Ela serve de apoio ao plano de medição da [#134](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/134) e ao relatório PSM da Fase 3 ([#107](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/107)).

---

## Objetivos

- Identificar quais issues abertas atrasam mais trabalho da equipe se ficarem paradas;
- Registrar as alternativas avaliadas e a justificativa da regra escolhida;
- Descrever a prioridade como um *measurement construct*, no template adotado na disciplina [[1, p. 19]](#ref-1);
- Definir como os campos `Prioridade`, `Início` e `Prazo` são preenchidos e quando precisam ser atualizados;
- Registrar o retrato de 05/11/2026 e os limites da medida.

---

## Metodologia

A prioridade foi tratada como uma medida da categoria Calendário e Progresso, uma das categorias de informação do PSM [[1, p. 14]](#ref-1) e uma das três exigidas pela especificação [[2, p. 2]](#ref-2). Backlog é um dos conceitos mensuráveis de exemplo dessa categoria [[1, p. 20]](#ref-1).

O trabalho seguiu estas etapas:

- Levantamento do corpo de todas as issues abertas em 05/11/2026, pela API do GitHub;
- Extração das dependências na seção "Depende de", prevista no [modelo de issue](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/.github/ISSUE_TEMPLATE/tarefa.yml);
- Cálculo de cinco alternativas de regra, comparadas na [Tabela 1](#decisão);
- Escolha da regra e definição das faixas a partir da distribuição obtida;
- Preenchimento dos campos no Project e recálculo independente em 05/11/2026, com o mesmo resultado para as 45 issues do retrato.

As medidas foram avaliadas pelos critérios de seleção da aula [[1, p. 23]](#ref-1). A coleta é viável e não interrompe ninguém, porque usa um dado que a equipe já preenche, e o resultado é fácil de interpretar. O cálculo e a redação tiveram apoio do Claude Code, com a declaração feita na [PR #141](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/pull/141), conforme a [seção de uso de IA da política](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/CONTRIBUTING.md#7-uso-de-ia).

---

## Decisão

*Tabela 1: Alternativas de prioridade calculadas sobre as 45 issues abertas (Fonte: seção "Depende de" e seção "Prazo" das issues, 05/11/2026).*

| Opção | Regra | Resultado | Avaliação |
| :--- | :--- | :--- | :--- |
| **A. Impacto em cadeia (escolhida)** | Conta as issues travadas, direta ou indiretamente | 8 `Alta`, 14 `Média`, 23 `Normal` | Separa os gargalos e não repete o `Prazo`. |
| B. Dependência direta | `Alta` se alguma issue depende dela | 38 `Alta`, 7 `Normal` | Quase tudo fica `Alta`, então o nível não ajuda a escolher. Esta regra foi a primeira aplicada e acabou substituída. |
| C. Urgência | `Alta` se vence em até 2 dias | 14 `Alta` | Muda todo dia e repete o que o `Prazo` já mostra. |
| D. Manual | A equipe decide em reunião | Não calculado | Depende de alguém manter atualizado. |
| E. Sem prioridade | Ordena só por `Prazo` | Não se aplica | Não mostra o que trava mais trabalho. |

A opção A foi escolhida por [Christopher Paraizo](https://github.com/wChrstphr) em 05/11/2026, e a regra é submetida à equipe na revisão da PR [#141](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/pull/141). A prioridade mede impacto, e a urgência aparece no `Prazo`, que é o campo usado para ordenar o quadro.

---

## Measurement construct da prioridade

O construct segue todos os campos do template da disciplina [[1, p. 19]](#ref-1) e complementa os constructs de Calendário e Progresso dos relatórios PSM, como o [da Fase 2](relatorios/relatorio-psm-fase-2.md#22-construct-2--calendário-e-progresso-prontidão-do-pc1-e-fechamento-da-e1).

*Tabela 2: Measurement construct da prioridade das issues (Fonte: elaborado pelo autor, a partir de AULA 09, p. 19).*

| Campo do template | Especificação |
| :--- | :--- |
| **Categoria de informação** | Calendário e Progresso [[1, p. 14]](#ref-1) |
| **Necessidade de informação** (*Information Need*) | Saber quais issues atrasam mais trabalho da equipe se ficarem paradas, para evitar que um integrante fique bloqueado esperando outro. |
| **Conceito mensurável** (*Measurable Concept*) | Impacto em cadeia de uma issue aberta sobre as demais issues abertas. |
| **Entidades relevantes** (*Relevant Entities*) | Issues abertas do [repositório](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues). |
| **Atributos** (*Attributes*) | Estado da issue e referências `#número` na seção "Depende de". |
| **Medida base** (*Base Measures*) | Dependências abertas declaradas em cada issue. |
| **Método de medição** (*Measurement Method*) | Ler a seção "Depende de", extrair cada `#número` e manter só as issues que estão abertas. |
| **Tipo de método** (*Type of Measurement Method*) | Objetivo. |
| **Escala** (*Scale*) | Inteiros a partir de zero. |
| **Tipo de escala** (*Type of Scale*) | Razão. |
| **Unidade de medida** (*Unit of Measurement*) | Dependência. |
| **Medida derivada** (*Derived Measure*) | Issues travadas. |
| **Função de medição** (*Measurement Function*) | Contar as issues abertas distintas alcançadas ao seguir as dependências, direta ou indiretamente, a partir da issue. |
| **Indicador** (*Indicator*) | Nível de prioridade: `Alta`, `Média` ou `Normal`. |
| **Modelo de análise** (*Model*) | Classificar as issues travadas nas faixas da [Tabela 3](#níveis-de-prioridade). |
| **Critério de decisão** (*Decision Criteria*) | Issue `Alta` aberta depois do `Prazo` é o primeiro assunto da leitura semanal do plano de medição ([#134](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/134)), que decide entre cobrar o responsável ou redistribuir a issue. |

---

## Níveis de prioridade

*Tabela 3: Faixas do indicador de prioridade (Fonte: elaborado pelo autor).*

| Nível | Issues travadas |
| :--- | :---: |
| `Alta` | 15 ou mais |
| `Média` | De 5 a 14 |
| `Normal` | Menos de 5 |

A aula admite faixas de operação como critério de decisão, baseadas em cálculos, acordos ou históricos [[1, p. 7]](#ref-1). Estas faixas se baseiam na distribuição de 05/11/2026, porque a equipe ainda não tem histórico dessa medida: as issues `Alta` travam 17 ou mais, e nenhuma trava 15 ou 16.

A contagem acumula a cadeia inteira. A [#94](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/94) só aparece como dependência direta da [#95](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/95), mas a [#95](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/95) trava a [#98](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/98), a [#98](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/98) trava a [#111](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/111), a [#111](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/111) trava a [#114](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/114), e a cadeia segue. Por isso a [#94](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/94) chega a 26 issues travadas.

### Retrato em 05/11/2026

O cálculo cobriu 45 issues abertas, com 8 em `Alta`, 14 em `Média` e 23 em `Normal`. A [#140](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/140), aberta depois do cálculo para documentar esta decisão, entrou em `Normal` e não trava nenhuma issue.

*Tabela 4: Issues de prioridade alta em 05/11/2026 (Fonte: seções "Depende de" e "Prazo" das issues).*

| Issue `Alta` | Título | Issues travadas | Prazo |
| :--- | :--- | :---: | :---: |
| [#94](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/94) | [F3] Estudo do processo de projetar a avaliação e estrutura do plano | 26 | 05/11 |
| [#95](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/95) | [F3] Método de avaliação e justificativa por métrica | 25 | 06/11 |
| [#96](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/96) | [F3] Recursos e ambiente de avaliação | 25 | 05/11 |
| [#97](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/97) | [F3] Massa de dados: cena de referência, cenas de escala e arquivos inválidos | 24 | 06/11 |
| [#98](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/98) | [F3] Instruções para o avaliador de G1 (Manutenibilidade) | 19 | 07/11 |
| [#99](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/99) | [F3] Instruções para o avaliador de G2 (Confiabilidade) | 19 | 07/11 |
| [#100](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/100) | [F3] Instruções para o avaliador de G3 (Flexibilidade) | 19 | 07/11 |
| [#110](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/110) | [F4] Preparar o ambiente e o repositório de medidas | 17 | 08/11 |

Issues em `Média`, com a quantidade de issues travadas: [#111](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/111) (14), [#112](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/112) (14), [#113](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/113) (14), [#114](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/114) (13), [#115](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/115) (9), [#116](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/116) (9), [#117](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/117) (9), [#101](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/101) (6), [#102](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/102) (6), [#120](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/120) (6), [#133](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/133) (6), [#134](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/134) (6), [#104](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/104) (5), [#135](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/135) (5).

Issues em `Normal`, com a quantidade de issues travadas: [#107](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/107) (4), [#103](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/103) (3), [#118](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/118) (3), [#126](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/126) (3), [#108](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/108) (2), [#109](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/109) (2), [#119](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/119) (2), [#121](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/121) (2), [#123](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/123) (2), [#124](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/124) (2), [#125](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/125) (2), [#127](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/127) (2), [#122](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/122) (1), [#128](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/128) (1), [#129](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/129) (1), [#136](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/136) (1), [#85](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/85) (0), [#86](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/86) (0), [#87](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/87) (0), [#105](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/105) (0), [#106](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/106) (0), [#130](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/130) (0), [#138](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/138) (0).

### Interpretação

A interpretação relaciona o indicador à necessidade de informação [[1, p. 15]](#ref-1). Em 05/11/2026, o maior risco de bloqueio está no início do plano da Fase 3: a [#94](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/94) trava 26 das 45 issues (57,8%) e, junto com a [#96](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/96), tem prazo em 05/11. A [#110](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/110) é a única issue `Alta` da [milestone Fase 4](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/milestone/4) e aparece porque 17 issues dependem, em cadeia, do ambiente preparado. Essas issues devem ser as primeiras a serem acompanhadas, pois é aí que o atraso se propaga mais.

---

## Datas do quadro

Os campos `Prioridade`, `Prazo` e `Início` são campos personalizados do Project, de seleção única [[3]](#ref-3) e de data [[4]](#ref-4). Eles foram criados porque os campos nativos `Priority` e `Target date` da organização recusaram a escrita pela API, com a conta usada em 05/11/2026. A visualização de roteiro do Project posiciona os itens na linha do tempo a partir de campos de data [[5]](#ref-5), então o `Início` e o `Prazo` são os campos que desenham as barras.

*Tabela 5: Origem e atualização dos campos de data (Fonte: elaborado pelo autor).*

| Campo | Origem | Atualização |
| :--- | :--- | :--- |
| `Prazo` | Seção "Prazo" da issue. | Automática, pelo [`scripts/sincronizar_projeto.py`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/scripts/sincronizar_projeto.py) e pelo [workflow de sincronização](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/.github/workflows/sync-project-metrics.yml), a partir da PR [#139](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/pull/139) ([#138](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/138)). |
| `Início` | Regra abaixo. | Calculada uma vez em 05/11/2026. Não muda sozinha. |

`Início` de uma issue aberta é a data mais tardia entre o começo da fase, a criação da issue e o dia seguinte ao último prazo das dependências abertas. O cálculo adotou 04/11 como começo da Fase 3 e 09/11 como começo da Fase 4, o dia seguinte ao prazo da [milestone Fase 3](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/milestone/3). Uma issue da milestone Fase 4 com prazo anterior a 09/11 usa o começo da Fase 3. `Início` de uma issue fechada é a data de criação. Quando a regra passa do prazo, `Início` fica igual ao `Prazo`.

O cálculo também mostrou prazos sem folga, que a equipe deve observar: as issues da Tabela 6 vencem no mesmo dia da dependência, e a [#98](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/98), a [#99](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/99) e a [#100](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/100) têm só o dia 07/11, porque a [#95](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/95) vence em 06/11.

*Tabela 6: Issues com o mesmo prazo da dependência (Fonte: seções "Depende de" e "Prazo" das issues, 05/11/2026).*

| Issue | Depende de | Prazo das duas |
| :--- | :--- | :---: |
| [#102](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/102) | [#95](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/95) | 06/11 |
| [#105](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/105) | [#104](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/104) | 08/11 |
| [#107](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/107) | [#135](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/135) | 08/11 |
| [#127](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/127) | [#126](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/126) | 20/11 |

---

## Limites

- `Prioridade` e `Início` não se atualizam sozinhos: precisam ser recalculados quando as dependências ou os prazos mudarem. O recálculo está previsto nas leituras semanais da [#134](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/134).
- A contagem só enxerga o que está na seção "Depende de". Uma dependência não registrada não entra no cálculo.
- A medida conta issues e não considera horas, então uma issue curta pode travar tanto quanto uma longa.
- As faixas vêm de um único retrato e podem precisar de ajuste quando houver histórico.

---

## Conclusão

A contagem em cadeia dá à equipe uma resposta objetiva sobre o que acompanhar primeiro, usando um dado que já existia nas issues e sem acrescentar trabalho de registro. Ela separa oito gargalos entre 45 issues e deixa a urgência para o `Prazo`, de modo que cada campo responde a uma pergunta diferente. A utilidade da medida ainda precisa ser confirmada nas leituras semanais da [#134](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/134), inclusive para saber se as faixas continuam adequadas.

---

## Referências Bibliográficas

> <Link id="ref-1">1.</Link> RAMOS, Cristiane Soares. **AULA 09 QSW1 PSM resumo**. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Páginas 3, 6, 7, 14, 15, 19, 20 e 23. Disponível no Moodle da disciplina.
>
> <Link id="ref-2">2.</Link> **2026-2 Trabalho final completo v1**. Especificação do trabalho final da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Página 1, premissa 3, e página 2, seção 2. Disponível no Moodle da disciplina.
>
> <Link id="ref-3">3.</Link> GITHUB. **Sobre campos de seleção única**. Disponível em: https://docs.github.com/pt/issues/planning-and-tracking-with-projects/understanding-fields/about-single-select-fields. Acesso em: 05 nov. 2026.
>
> <Link id="ref-4">4.</Link> GITHUB. **Sobre campos de data**. Disponível em: https://docs.github.com/pt/issues/planning-and-tracking-with-projects/understanding-fields/about-date-fields. Acesso em: 05 nov. 2026.
>
> <Link id="ref-5">5.</Link> GITHUB. **Personalizando o layout do roteiro**. Disponível em: https://docs.github.com/pt/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/customizing-the-roadmap-layout. Acesso em: 05 nov. 2026.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 05/11/2026 | Criação da página, com o construct da prioridade, as regras das datas e o retrato de 05/11 | [Christopher Paraizo](https://github.com/wChrstphr) | |
| 1.1 | 05/11/2026 | Reestruturação com introdução, objetivos, metodologia, decisão, interpretação, conclusão, referências e links entre documentos, e construct com todos os campos do template | [Christopher Paraizo](https://github.com/wChrstphr) | |
