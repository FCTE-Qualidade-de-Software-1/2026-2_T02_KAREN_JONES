---
id: priorizacao-issues
title: Priorização e datas no GitHub Project
sidebar_label: Priorização no Project
sidebar_position: 2
description: Como os campos Prioridade, Início e Prazo do GitHub Project da equipe são preenchidos.
---

import Link from '@docusaurus/Link';

# Priorização e datas no GitHub Project

## Introdução

Esta página explica como são preenchidos os campos `Prioridade`, `Início` e `Prazo` do [Project da equipe](https://github.com/orgs/FCTE-Qualidade-de-Software-1/projects/36). Esses campos operacionalizam o critério de desbloqueio de dependências do construct de Calendário e Progresso do [Plano de Medição PSM](plano-medicao-psm.md#41-construct-1-calendário-e-progresso-ritmo-de-fechamento-e-dependências), definido na [#134](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/134).

## Metodologia

Os dados vêm das seções "Prazo" e "Depende de" de cada issue, previstas na [política de contribuição](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/CONTRIBUTING.md#3-issues). A `Prioridade` conta as issues abertas travadas por cada issue, o `Início` combina as datas da fase com os prazos das dependências e o `Prazo` é copiado da issue. A prioridade é descrita num construct no mesmo template do plano, e o retrato de 05/11/2026 registra o primeiro cálculo.

## Prioridade

A prioridade mede quantas issues abertas ficam travadas, direta ou indiretamente, por uma issue. Se a B depende da A, e a C depende da B, a A trava duas issues. A urgência fica no `Prazo`, que é o campo usado para ordenar o quadro.

<p className="tabela-titulo">Tabela 1: Níveis de prioridade</p>

| Nível | Issues travadas |
| :--- | :---: |
| `Alta` | 15 ou mais |
| `Média` | De 5 a 14 |
| `Normal` | Menos de 5 |

<p className="tabela-fonte">Fonte: [Christopher Paraizo](https://github.com/wChrstphr), 2026.</p>

## Construct de medição

O construct segue o template da disciplina [[1, p. 19]](#ref-1), como no [Plano de Medição PSM](plano-medicao-psm.md#41-construct-1-calendário-e-progresso-ritmo-de-fechamento-e-dependências), na categoria Calendário e Progresso [[2, p. 2]](#ref-2).

<p className="tabela-titulo">Tabela 2: Construct da prioridade</p>

| Elemento | Especificação |
| :--- | :--- |
| **Necessidade de informação** | Saber quais issues atrasam mais trabalho da equipe se ficarem paradas. |
| **Conceito mensurável** | Impacto em cadeia de uma issue aberta sobre as demais. |
| **Medida base** | Dependências abertas na seção "Depende de" de cada issue. |
| **Medida derivada** | Quantidade de issues abertas travadas, direta ou indiretamente. |
| **Indicador** | Nível `Alta`, `Média` ou `Normal`. |
| **Critério de decisão** | Issue `Alta` ou `Média` aberta a 48 h do `Prazo` aciona pareamento imediato ou divisão do trabalho, conforme o critério de desbloqueio de dependências do [Plano de Medição PSM](plano-medicao-psm.md#41-construct-1-calendário-e-progresso-ritmo-de-fechamento-e-dependências). |

<p className="tabela-fonte">Fonte: [Christopher Paraizo](https://github.com/wChrstphr), 2026.</p>

## Retrato em 05/11/2026

Das 45 issues abertas no cálculo, 8 ficaram em `Alta`, 14 em `Média` e 23 em `Normal`.

<p className="tabela-titulo">Tabela 3: Issues de prioridade alta</p>

| Issue | Issues travadas | Prazo |
| :--- | :---: | :---: |
| [#94](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/94) | 26 | 05/11 |
| [#95](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/95) | 25 | 06/11 |
| [#96](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/96) | 25 | 05/11 |
| [#97](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/97) | 24 | 06/11 |
| [#98](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/98) | 19 | 07/11 |
| [#99](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/99) | 19 | 07/11 |
| [#100](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/100) | 19 | 07/11 |
| [#110](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/110) | 17 | 08/11 |

<p className="tabela-fonte">Fonte: [Christopher Paraizo](https://github.com/wChrstphr), 2026.</p>

## Datas

Os dois campos de data desenham as barras na visualização de roteiro do Project [[3]](#ref-3).

- **`Prazo`:** copiado da issue pelo [script de sincronização](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/scripts/sincronizar_projeto.py), a partir da [#139](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/pull/139).
- **`Início`:** data mais tardia entre o começo da fase pela milestone (26/10 na Fase 3 e 09/11 na Fase 4), a criação da issue e o dia seguinte ao último prazo das dependências abertas. Issue da Fase 4 com prazo antes de 09/11 usa o começo da Fase 3. Se a data passar do `Prazo`, fica igual a ele. Issue fechada usa a data de criação.

## Limites

- `Prioridade` e `Início` não se atualizam sozinhos: são recalculados nas leituras semanais da [#134](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/134).
- Uma dependência fora da seção "Depende de" não entra na contagem.
- A medida conta issues, não horas.
- O retrato de 05/11/2026 usou 04/11, data da Leitura 0 do plano, como começo da Fase 3, e não o começo da milestone. Issues criadas antes de 04/11 podem ter `Início` diferente do que a regra acima daria.

## Referências

> <Link id="ref-1">1.</Link> RAMOS, Cristiane Soares. **AULA 09 QSW1 PSM resumo**. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Página 19. Disponível no Moodle da disciplina.
>
> <Link id="ref-2">2.</Link> **2026-2 Trabalho final completo**. Especificação do trabalho final de Qualidade de Software 1, FCTE/UnB, 2026. Página 2, seção 2: Gestão do Projeto com métricas PSM/CID. Disponível no Moodle da disciplina.
>
> <Link id="ref-3">3.</Link> GITHUB. **Personalizando o layout do roteiro**. Disponível em: https://docs.github.com/pt/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/customizing-the-roadmap-layout. Acesso em: 05 nov. 2026.

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 05/11/2026 | Criação da página | [Christopher Paraizo](https://github.com/wChrstphr) | |
| 1.1 | 05/11/2026 | Inclusão de referências e links entre documentos | [Christopher Paraizo](https://github.com/wChrstphr) | |
| 1.2 | 06/11/2026 | Títulos acima das tabelas, fontes abaixo e nome do autor com link | [Christopher Paraizo](https://github.com/wChrstphr) | |
| 1.3 | 18/11/2026 | Revisão de coerência, cross-links e redação: Introdução e Metodologia, critério de decisão igual ao do plano, começo da Fase 3 pela milestone e referência à especificação atualizada | [Christopher Paraizo](https://github.com/wChrstphr) | |
