---
id: priorizacao-issues
title: Priorização e datas no GitHub Project
sidebar_label: Priorização no Project
sidebar_position: 2
description: Como os campos Prioridade, Início e Prazo do GitHub Project da equipe são calculados, com o construct no modelo PSM.
---

# Priorização e datas no GitHub Project

Esta página explica como são preenchidos os campos `Prioridade`, `Início` e `Prazo` do [Project da equipe](https://github.com/orgs/FCTE-Qualidade-de-Software-1/projects/36). Ela complementa os relatórios PSM/CID, como o da [Fase 2](relatorios/relatorio-psm-fase-2.md), e serve de apoio ao plano de medição da [#134](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/134).

## 1. Measurement construct da prioridade

| Elemento do Construct | Especificação |
| :--- | :--- |
| **Categoria de Informação** | Calendário e Progresso (*Schedule and Progress*) |
| **Necessidade de Informação** | Saber quais issues atrasam mais trabalho da equipe se ficarem paradas, para evitar que um integrante fique bloqueado esperando outro. |
| **Conceito Mensurável** | Impacto em cadeia de uma issue aberta sobre as demais issues abertas. |
| **Medida Base** | Seção "Depende de" de cada issue aberta. |
| **Medida Derivada** | Issues travadas = quantidade de issues abertas que dependem da issue, direta ou indiretamente. |
| **Indicador** | Nível de prioridade: `Alta`, `Média` ou `Normal`. |
| **Critério de Decisão** | Issue `Alta` atrasada é o primeiro assunto da leitura semanal do plano de medição, que decide entre cobrar o responsável ou redistribuir a issue. |

## 2. Níveis de prioridade

| Nível | Issues travadas |
| :--- | :---: |
| `Alta` | 15 ou mais |
| `Média` | De 5 a 14 |
| `Normal` | Menos de 5 |

Se a issue B depende da A, e a C depende da B, a A trava duas issues. As faixas foram definidas com a distribuição de 05/11/2026: as issues de `Alta` travam 17 ou mais, e nenhuma trava 15 ou 16. Só as issues abertas recebem prioridade, e a contagem considera só dependências que ainda estão abertas.

A prioridade mede impacto, não urgência. A urgência aparece no `Prazo`, que é o campo usado para ordenar o quadro.

### Retrato em 05/11/2026

Das 45 issues abertas, 8 ficaram em `Alta`, 14 em `Média` e 23 em `Normal`.

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

*Tabela 1: Issues de prioridade alta em 05/11/2026 (Fonte: seção "Depende de" das issues).*

Issues em `Média`, com a quantidade de issues travadas: [#111](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/111) (14), [#112](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/112) (14), [#113](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/113) (14), [#114](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/114) (13), [#115](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/115) (9), [#116](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/116) (9), [#117](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/117) (9), [#101](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/101) (6), [#102](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/102) (6), [#120](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/120) (6), [#133](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/133) (6), [#134](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/134) (6), [#104](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/104) (5), [#135](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/135) (5).

## 3. Datas do quadro

| Campo | Origem | Atualização |
| :--- | :--- | :--- |
| `Prazo` | Seção "Prazo" da issue. | Automática pelo script `scripts/sincronizar_projeto.py`, conforme a [#138](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/138). |
| `Início` | Regra abaixo. | Calculada uma vez em 05/11/2026. Não muda sozinha. |

`Início` de uma issue aberta é a data mais tardia entre o começo da fase (Fase 3 em 04/11 e Fase 4 em 09/11), a criação da issue e o dia seguinte ao último prazo das dependências abertas. Uma issue da milestone Fase 4 com prazo anterior a 09/11 usa o começo da Fase 3. `Início` de uma issue fechada é a data de criação. Quando a regra passa do prazo, `Início` fica igual ao `Prazo`.

## 4. Limites

- `Prioridade` e `Início` não se atualizam sozinhos: precisam ser recalculados quando as dependências ou os prazos mudarem.
- A contagem só enxerga o que está na seção "Depende de". Uma dependência não registrada não entra no cálculo.
- A medida conta issues e não considera horas, então uma issue curta pode travar tanto quanto uma longa.

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 05/11/2026 | Criação da página, com o construct da prioridade, as regras das datas e o retrato de 05/11 | [Christopher Paraizo](https://github.com/wChrstphr) | |
