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

## 3. Q1.1 — Modularidade

**Questão:** Em que medida o código está dividido em pacotes independentes, com dependências em uma única direção?

**Requisitos:** RQ-MAN-01 (limites entre aplicação e biblioteca), RQ-MAN-02 (direção das dependências e ausência de ciclos) e RQ-MAN-03 (coesão e dependências desnecessárias).

**Hipótese:** não há ciclos de dependência em tempo de execução entre os pacotes, e nenhum pacote importa código da aplicação web. A biblioteca `excalidraw` é o pacote mais dependente dos demais, e os pacotes de base são os mais estáveis.

### M1.1.1 — Ciclos de dependência entre pacotes

| Campo | Descrição |
| :--- | :--- |
| Definição | Número de pares de pacotes que dependem um do outro em tempo de execução, direta ou indiretamente. |
| Procedimento de cálculo | Montar o grafo de dependências entre arquivos de produção, considerando só importações de valor (importações apenas de tipo são descartadas, porque desaparecem na compilação). Agrupar os arquivos por pacote e contar os pares de pacotes A e B em que A alcança B e B alcança A. Unidade: pares de pacotes. Escala: absoluta, de 0 em diante. |
| Fonte dos dados | Código de produção de todos os pacotes. |
| Procedimento de coleta | Ferramenta Madge (versão 8.0.0), com o `tsconfig.json` do repositório para resolver os nomes `@excalidraw/*` e com a opção de ignorar importações de tipo. A lista de ciclos entre arquivos é agrupada por pacote com um script. |
| Critério de interpretação | Confirma a hipótese se o valor for 0. Cada par encontrado indica dois pacotes que não podem ser alterados ou reutilizados separadamente. |
| Questão respondida | Q1.1 |
| Características desejáveis | Simples (contagem). Objetiva, porque o grafo sai das importações declaradas no código. Fácil de coletar com uma ferramenta automática. Válida, porque ciclos medem diretamente a falta de direção nas dependências. Baseada na estrutura do programa, e não na linguagem. |

### M1.1.2 — Importações que violam a direção declarada

| Campo | Descrição |
| :--- | :--- |
| Definição | Número de importações de valor que contrariam a direção de dependência declarada pelo próprio projeto: pacotes de base importando da biblioteca `excalidraw`, ou qualquer pacote importando da aplicação web. |
| Procedimento de cálculo | Contar, nos arquivos de produção, as importações de valor cujo destino é proibido pela regra. A regra é a configuração de lint `packages/eslintrc.base.json` do Excalidraw, que proíbe os pacotes de base de importar da biblioteca qualquer coisa além de tipos. Unidade: importações. Escala: absoluta. |
| Fonte dos dados | Código de produção dos pacotes de base e da biblioteca; arquivo `packages/eslintrc.base.json`. |
| Procedimento de coleta | Busca no código das importações de `@excalidraw/excalidraw` e de `excalidraw-app` (ferramenta `grep` ou ESLint com a regra do projeto), descartando as importações apenas de tipo (`import type`). |
| Critério de interpretação | Confirma a hipótese se o valor for 0. Cada importação encontrada é um ponto em que o código não respeita a arquitetura que o próprio projeto declara. |
| Questão respondida | Q1.1 |
| Características desejáveis | Simples e objetiva, porque a direção esperada vem de uma regra escrita pelo projeto, e não de opinião da equipe. Fácil de coletar. Válida para os limites entre aplicação, biblioteca e pacotes de base (RQ-MAN-01). |

### M1.1.3 — Instabilidade de cada pacote

| Campo | Descrição |
| :--- | :--- |
| Definição | Instabilidade *I* de cada pacote (Martin, 2002): a proporção das dependências do pacote que apontam para fora dele. Um pacote estável (I perto de 0) é usado por muitos e usa poucos; um instável (I perto de 1) usa muitos e é usado por poucos. |
| Procedimento de cálculo | *I* = Ce / (Ca + Ce), em que Ce (acoplamento eferente) é o número de outros pacotes que o pacote importa e Ca (acoplamento aferente) é o número de outros pacotes que o importam. Consideram-se só importações de valor no código de produção. Unidade: adimensional. Escala: 0 a 1. |
| Fonte dos dados | Código de produção de todos os pacotes. |
| Procedimento de coleta | O mesmo grafo de M1.1.1, contando as arestas distintas entre pacotes. |
| Critério de interpretação | Confirma a hipótese se os pacotes de base tiverem *I* menor que a biblioteca e a biblioteca tiver *I* menor que a aplicação web. Um pacote de base com *I* alto depende de muitos outros e é mais difícil de reutilizar. |
| Questão respondida | Q1.1 |
| Características desejáveis | Simples (uma razão). Objetiva e robusta, porque permite comparar pacotes entre si e com outras versões. Válida, porque é uma medida consagrada de acoplamento entre módulos. Independente da linguagem. |

---

## Referências

- AULA 08 QSW1 GQM. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Páginas 33, 34, 38 e 41.
- Especificação do trabalho final da disciplina de Qualidade de Software 1 (2026-2 Trabalho final completo v1). Página 1, premissa 2.
- MARTIN, R. C. *Agile Software Development: Principles, Patterns, and Practices*. Prentice Hall, 2002.
- ISO/IEC 25010:2023. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model*.
- Excalidraw. Repositório oficial, commit `e1b7aac` de 18/10/2026. Disponível em: https://github.com/excalidraw/excalidraw/tree/e1b7aacb356a492aa1e0fc6eb57b8896124027f0.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 19/10/2026 | Criação das questões, hipóteses e métricas do objetivo G1 | [Christopher Paraizo](https://github.com/wChrstphr) | |
