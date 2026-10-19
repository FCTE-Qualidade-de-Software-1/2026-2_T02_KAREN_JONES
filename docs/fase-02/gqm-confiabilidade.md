---
sidebar_position: 4
title: GQM de Confiabilidade (G2)
description: Questões, hipóteses e métricas do objetivo de medição G2, que avalia a confiabilidade do editor e da aplicação web do Excalidraw
---

# GQM de Confiabilidade (G2)

Esta página detalha o objetivo G2, definido em [Método GQM e objetivos de medição](./estrutura-gqm.md#g2--confiabilidade). Para cada subcaracterística de Confiabilidade há uma questão, a hipótese da questão e as métricas que a respondem.

| Campo do template | Valor |
| :--- | :--- |
| Analisar | o editor, a aplicação web e os mecanismos de colaboração e de salvamento no navegador, além do histórico público de defeitos relatados |
| para o propósito de | entender |
| com respeito a | Confiabilidade: ausência de falhas (Maturidade, na edição de 2011), disponibilidade, tolerância a falhas e recuperabilidade |
| do ponto de vista de | usuários finais |
| no contexto de | código-fonte público na versão de 18/10/2026, avaliado por equipe independente, sem acesso aos servidores de produção |

As questões caracterizam o produto em relação a cada subcaracterística (AULA 08, p. 33 e 34). As hipóteses partem da [abstraction sheet de G2](./abstraction-sheets.md#4-g2--confiabilidade), como a aula permite (AULA 08, p. 34). As métricas respondem às questões de forma quantitativa (AULA 08, p. 38). Os níveis de pontuação e os critérios de julgamento de cada métrica são definidos em uma página própria da Fase 02.

---

## 1. Visão geral

| Questão | Subcaracterística | Requisitos da Fase 01 | Métricas |
| :--- | :--- | :--- | :--- |
| Q2.1 | Ausência de falhas | RQ-CONF-01 e RQ-CONF-02 | M2.1.1, M2.1.2, M2.1.3 |
| Q2.2 | Disponibilidade | RQ-CONF-03 e RQ-CONF-04 | M2.2.1, M2.2.2 |
| Q2.3 | Tolerância a falhas | RQ-CONF-05 a RQ-CONF-07 | M2.3.1, M2.3.2 |
| Q2.4 | Recuperabilidade | RQ-CONF-08 a RQ-CONF-11 | M2.4.1, M2.4.2, M2.4.3 |

Os requisitos estão em [Requisitos da avaliação](../fase-01/requisitos-avaliacao.md). A seção 7 mostra qual métrica atende cada requisito.

---

## 2. Convenções de coleta

As definições abaixo valem para todas as métricas de G2 e evitam que pessoas diferentes contem ou testem coisas diferentes.

- **Versão avaliada:** commit `e1b7aac` do repositório oficial, de 18/10/2026, identificado no [escopo](../fase-01/escopo-avaliacao.md).
- **Janela histórica:** contribuições integradas e relatos abertos entre 18/04/2026 e 18/10/2026, os seis meses que antecedem a versão avaliada. A janela delimita os dados de histórico do projeto (objeto O6 do escopo).
- **Contribuição integrada:** *pull request* aceito (*merged*) no ramo principal do repositório.
- **Correção:** contribuição integrada cujo título começa com o tipo `fix`. O próprio Excalidraw exige que todo título de *pull request* comece com um tipo padronizado (`feat`, `fix`, `docs`, `refactor` e outros), verificado automaticamente pelo fluxo `semantic-pr-title.yml`. Esse padrão é usado porque a maior parte dos relatos de defeito no repositório não recebe rótulo, o que tornaria a contagem por rótulo pouco confiável.
- **Ambiente de teste:** a aplicação web construída a partir da versão avaliada, executada localmente com a configuração de produção do repositório, em um navegador de versão fixa. O ambiente exato (máquina, sistema operacional, navegador e versões) é definido no plano de avaliação da Fase 03 e registrado em cada coleta.
- **Cena de referência:** desenho padronizado usado nos testes, com ao menos um elemento de cada tipo principal: retângulo, elipse, losango, seta, linha, desenho livre, texto, texto dentro de forma, imagem e moldura (*frame*).

Os fatores que podem influenciar os resultados também são registrados junto com cada coleta (AULA 08, p. 38): o commit avaliado, a janela histórica, o navegador e sua versão, e o estado da rede durante os testes. Esses fatores foram levantados na abstraction sheet de G2.

---

## Referências

- AULA 08 QSW1 GQM. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Páginas 33, 34 e 38.
- Especificação do trabalho final da disciplina de Qualidade de Software 1 (2026-2 Trabalho final completo v1). Página 1, premissa 2.
- ISO/IEC 25010:2023. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model*.
- Excalidraw. Repositório oficial, commit `e1b7aac` de 18/10/2026. Disponível em: https://github.com/excalidraw/excalidraw/tree/e1b7aacb356a492aa1e0fc6eb57b8896124027f0.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 19/10/2026 | Criação das questões, hipóteses e métricas do objetivo G2 | [Christopher Paraizo](https://github.com/wChrstphr) | |
