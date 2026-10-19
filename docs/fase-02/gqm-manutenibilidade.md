---
sidebar_position: 3
title: GQM de Manutenibilidade (G1)
description: Questões, hipóteses e métricas do objetivo de medição G1, que avalia a manutenibilidade do código-fonte do Excalidraw
---

# GQM de Manutenibilidade (G1)

Esta página detalha o objetivo G1, definido em [Método GQM e objetivos de medição](./estrutura-gqm.md#g1--manutenibilidade). Para cada subcaracterística de Manutenibilidade há uma questão, a hipótese da questão e as métricas que a respondem.

| Campo do template | Valor |
| :--- | :--- |
| Analisar | o código-fonte do Excalidraw (biblioteca, aplicação web e pacotes auxiliares), seus testes, sua documentação para desenvolvedores e o histórico público de alterações |
| para o propósito de | entender |
| com respeito a | Manutenibilidade: modularidade, reusabilidade, analisabilidade, modificabilidade e testabilidade |
| do ponto de vista de | mantenedores e contribuidores do projeto |
| no contexto de | código-fonte público na versão de 18/10/2026, avaliado por equipe independente |

As questões caracterizam o código em relação a cada subcaracterística (AULA 08, p. 33 e 34). As hipóteses partem da [abstraction sheet de G1](./abstraction-sheets.md#3-g1--manutenibilidade), como a aula permite (AULA 08, p. 34). As métricas respondem às questões de forma quantitativa (AULA 08, p. 38). Os níveis de pontuação e os critérios de julgamento de cada métrica são definidos em uma página própria da Fase 02.

---

## 1. Visão geral

| Questão | Subcaracterística | Requisitos da Fase 01 | Métricas |
| :--- | :--- | :--- | :--- |
| Q1.1 | Modularidade | RQ-MAN-01 a RQ-MAN-03 | M1.1.1, M1.1.2, M1.1.3 |
| Q1.2 | Reusabilidade | RQ-MAN-04 e RQ-MAN-05 | M1.2.1, M1.2.2 |
| Q1.3 | Analisabilidade | RQ-MAN-06 a RQ-MAN-08 | M1.3.1, M1.3.2, M1.3.3 |
| Q1.4 | Modificabilidade | RQ-MAN-09 e RQ-MAN-10 | M1.4.1, M1.4.2, M1.4.3 |
| Q1.5 | Testabilidade | RQ-MAN-11 a RQ-MAN-13 | M1.5.1, M1.5.2, M1.5.3 |

Os requisitos estão em [Requisitos da avaliação](../fase-01/requisitos-avaliacao.md). A seção 8 mostra qual métrica atende cada requisito.

---

## 2. Convenções de coleta

As definições abaixo valem para todas as métricas de G1 e evitam que pessoas diferentes contem coisas diferentes.

- **Versão avaliada:** commit `e1b7aac` do repositório oficial, de 18/10/2026, identificado no [escopo](../fase-01/escopo-avaliacao.md).
- **Pacote:** cada pasta em `packages/` (`common`, `element`, `excalidraw`, `fractional-indexing`, `laser-pointer`, `math` e `utils`) e a aplicação web em `excalidraw-app/`.
- **Pacotes de base:** todos os pacotes, exceto a biblioteca `excalidraw` e a aplicação web.
- **Código de produção:** arquivos `.ts` e `.tsx` dos pacotes. Ficam de fora as pastas `tests/` e `__snapshots__/`, os arquivos `*.test.ts(x)` e `*.d.ts`, a documentação (`dev-docs/`), os exemplos (`examples/`) e as dependências instaladas (`node_modules/`).
- **Código de teste:** arquivos `*.test.ts(x)` e o conteúdo das pastas `tests/` dos pacotes.
- **Janela histórica:** contribuições integradas ao ramo principal entre 18/04/2026 e 18/10/2026, os seis meses que antecedem a versão avaliada. A janela delimita os dados de histórico do projeto (objeto O6 do escopo).
- **Contribuição integrada:** *pull request* aceito (*merged*) no ramo principal do repositório.

Os fatores que podem influenciar os resultados também são registrados junto com cada coleta (AULA 08, p. 38): o commit avaliado, a janela histórica e a versão de cada ferramenta. Esses fatores foram levantados na abstraction sheet de G1.

---

## Referências

- AULA 08 QSW1 GQM. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Páginas 33, 34, 38 e 41.
- Especificação do trabalho final da disciplina de Qualidade de Software 1 (2026-2 Trabalho final completo v1). Página 1, premissa 2.
- ISO/IEC 25010:2023. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model*.
- Excalidraw. Repositório oficial, commit `e1b7aac` de 18/10/2026. Disponível em: https://github.com/excalidraw/excalidraw/tree/e1b7aacb356a492aa1e0fc6eb57b8896124027f0.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 19/10/2026 | Criação das questões, hipóteses e métricas do objetivo G1 | [Christopher Paraizo](https://github.com/wChrstphr) | |
