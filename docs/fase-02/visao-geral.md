---
sidebar_position: 0
title: Visão Geral da Fase 02
description: O que estamos definindo na segunda fase da avaliação de qualidade do Excalidraw e como os documentos desta fase se organizam
---

# Fase 02: Especificação da Avaliação

## Introdução

A [Fase 01](../fase-01/visao-geral.md) definiu por que avaliar o Excalidraw, o que avaliar e quais características de qualidade priorizar. A Fase 02 responde à pergunta seguinte: **o que exatamente será medido, e como cada resultado será interpretado?**

Para isso, a equipe usa o [método *Goal–Question–Metric* (GQM)](./estrutura-gqm.md). Cada característica [priorizada](../fase-01/priorizacao-caracteristicas.md) vira um objetivo de medição, desdobrado em questões, hipóteses e métricas, com níveis de pontuação e critérios de julgamento definidos antes da coleta. A coleta em si fica para a Fase 04, depois que a Fase 03 projetar a avaliação.

## Metodologia

A fase seguiu as etapas de definição do GQM adaptadas ao contexto da avaliação, descritas em [Método GQM e objetivos de medição](./estrutura-gqm.md#2-como-as-etapas-do-gqm-foram-adaptadas). As páginas foram produzidas na ordem da Tabela 1: do método às métricas de cada objetivo, e destas à pontuação e ao plano que reúne tudo.

## Documentos desta fase

<p className="tabela-titulo">Tabela 1: Documentos da Fase 02</p>

| Documento | Conteúdo |
| :--- | :--- |
| [Método GQM e objetivos de medição](./estrutura-gqm.md) | Resumo do método, adaptação das etapas ao contexto da avaliação e os objetivos [G1](./estrutura-gqm.md#g1-manutenibilidade), [G2](./estrutura-gqm.md#g2-confiabilidade) e [G3](./estrutura-gqm.md#g3-flexibilidade-antiga-portabilidade) |
| [Abstraction sheets](./abstraction-sheets.md) | Uma ficha por objetivo, preenchida em reunião da equipe |
| [GQM de Manutenibilidade (G1)](./gqm-manutenibilidade.md) | Questões [Q1.1](./gqm-manutenibilidade.md#3-q11-modularidade) a [Q1.5](./gqm-manutenibilidade.md#7-q15-testabilidade), hipóteses e fichas das métricas |
| [GQM de Confiabilidade (G2)](./gqm-confiabilidade.md) | Questões [Q2.1](./gqm-confiabilidade.md#3-q21-ausência-de-falhas) a [Q2.4](./gqm-confiabilidade.md#6-q24-recuperabilidade), hipóteses e fichas das métricas |
| [GQM de Flexibilidade (G3)](./gqm-flexibilidade.md) | Questões [Q3.1](./gqm-flexibilidade.md#3-q31-adaptabilidade) a [Q3.4](./gqm-flexibilidade.md#6-q34-substituibilidade), hipóteses e fichas das métricas |
| [Níveis de pontuação e critérios de julgamento](./pontuacao-julgamento.md) | Faixas de valores e regras de interpretação, da métrica até a característica |
| [Plano GQM](./plano-gqm.md) | Diagramas da hierarquia, hipóteses, diretrizes de interpretação e rastreabilidade com a Fase 01 |

<p className="tabela-fonte">Fonte: [Luiz Henrique Soares](https://github.com/luizh-gsoares), 2026.</p>

## Relação com a Fase 01

Os objetivos de medição derivam do [modelo de qualidade](../fase-01/modelo-de-qualidade.md) e da [priorização das características](../fase-01/priorizacao-caracteristicas.md). Cada questão reúne os [requisitos de avaliação](../fase-01/requisitos-avaliacao.md) da mesma subcaracterística. Os objetos medidos são os delimitados no [escopo da avaliação](../fase-01/escopo-avaliacao.md), e o ponto de vista dos objetivos vem das [partes interessadas](../fase-01/interessados.md).

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 19/10/2026 | Criação da visão geral da Fase 02 e das referências cruzadas com a Fase 01 | [Luiz Henrique Soares](https://github.com/luizh-gsoares) | [Christopher](https://github.com/wChrstphr) |
| 1.1 | 19/10/2026 | Publicação dos GQM de G1, G2 e G3 na tabela de documentos | [Luiz Henrique Soares](https://github.com/luizh-gsoares) | [Christopher](https://github.com/wChrstphr) |
| 1.2 | 20/10/2026 | Publicação das páginas de pontuação e do Plano GQM, com referência cruzada | [Luiz Henrique Soares](https://github.com/luizh-gsoares) | [Luiz Henrique Soares](https://github.com/luizh-gsoares) |
| 1.3 | 06/11/2026 | Título sem travessão, retirada da coluna de situação, com todas as páginas já publicadas, referências cruzadas resumidas em um parágrafo, links para objetivos e questões, tabela com título e fonte | [Christopher Paraizo](https://github.com/wChrstphr) | |
| 1.4 | 10/11/2026 | Inclusão da Metodologia | [Christopher Paraizo](https://github.com/wChrstphr) | |
