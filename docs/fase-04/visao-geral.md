---
sidebar_position: 0
title: Visão geral da Fase 04
description: Execução da avaliação do Excalidraw, documentos da Fase 04 e caminho dos dados brutos até o julgamento e a ação de melhoria.
---

# Fase 04: Executar a avaliação

## Introdução

A [Fase 03](../fase-03/visao-geral.md) definiu como, com quais recursos e quando cada uma das 36 métricas seria obtida. A **Fase 04** executa esse plano sobre o commit `e1b7aacb356a492aa1e0fc6eb57b8896124027f0` do Excalidraw: coleta as medidas, compara os valores com as hipóteses e os níveis da [Fase 02](../fase-02/pontuacao-julgamento.md), julga cada característica priorizada na [Fase 01](../fase-01/visao-geral.md) e escolhe a ação de melhoria a executar.

## Metodologia

A coleta segue as instruções de [G1](../fase-03/instrucoes-g1-manutenibilidade.md), [G2](../fase-03/instrucoes-g2-confiabilidade.md) e [G3](../fase-03/instrucoes-g3-flexibilidade.md) e grava as evidências, com o identificador da métrica no nome do arquivo, em `dados/fase-04/brutos/`. Os valores calculados a partir delas ficam em `dados/fase-04/consolidados/`, no formato do [plano de análise](../fase-03/plano-analise.md#3-tabela-consolidada-e-script-de-análise), que também orienta o [fluxo da análise](../fase-03/plano-analise.md#1-fluxo-da-análise).

Cada página de resultados atribui o nível de cada métrica, confronta as hipóteses e responde às questões e ao objetivo GQM. O julgamento aplica a [agregação](../fase-02/pontuacao-julgamento.md#6-agregação-da-métrica-à-característica) e o [julgamento de cada característica](../fase-02/pontuacao-julgamento.md#71-julgamento-de-cada-característica) da Fase 02, sem nota única para o produto. As métricas nos níveis mais baixos alimentam as oportunidades de melhoria, conforme a [regra dos pontos de melhoria](../fase-02/pontuacao-julgamento.md#73-pontos-de-melhoria).

## Documentos desta fase

<p className="tabela-titulo">Tabela 1: Documentos da execução da avaliação</p>

| Documento | Finalidade |
| :--- | :--- |
| [Resultados de G1: Manutenibilidade](./resultados-g1-manutenibilidade.md) | Níveis das 14 métricas, confronto das hipóteses e respostas às questões [Q1.1](../fase-02/gqm-manutenibilidade.md#3-q11-modularidade) a [Q1.5](../fase-02/gqm-manutenibilidade.md#7-q15-testabilidade) e ao objetivo G1. |
| [Resultados de G2: Confiabilidade](./resultados-g2-confiabilidade.md) | Níveis das 10 métricas, desvios de execução, confronto das hipóteses e respostas às questões [Q2.1](../fase-02/gqm-confiabilidade.md#3-q21-ausência-de-falhas) a [Q2.4](../fase-02/gqm-confiabilidade.md#6-q24-recuperabilidade) e ao objetivo G2. |
| [Resultados de G3: Flexibilidade](./resultados-g3-flexibilidade.md) | Níveis das 12 métricas, confronto das hipóteses e respostas às questões [Q3.1](../fase-02/gqm-flexibilidade.md#3-q31-adaptabilidade) a [Q3.4](../fase-02/gqm-flexibilidade.md#6-q34-substituibilidade) e ao objetivo G3. |
| [Julgamento final](./julgamento.md) | Julgamento de cada característica, coerência com o propósito da Fase 01, relações entre as características e limites de validade. |
| [Oportunidades de melhoria](./melhorias.md) | Pontos de melhoria, critérios de escolha, ação proposta e critério de sucesso. |
| [Dados da Fase 04](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/dados/fase-04/README.md) | Organização dos dados brutos e consolidados e registro do ambiente de cada coleta. |

<p className="tabela-fonte">Fonte: [Christopher Paraizo](https://github.com/wChrstphr), 2026.</p>

A rastreabilidade completa vai do requisito da Fase 01 à métrica da Fase 02, ao procedimento da [Tabela 2 da Fase 03](../fase-03/visao-geral.md#rastreabilidade-entre-as-fases-02-e-03) e à evidência em `dados/fase-04/brutos/`.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 18/11/2026 | Criação da visão geral da Fase 04 com os documentos da fase e o caminho dos dados ao julgamento | [Christopher Paraizo](https://github.com/wChrstphr) |  |
