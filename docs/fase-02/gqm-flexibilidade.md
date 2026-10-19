---
sidebar_position: 5
title: GQM de Flexibilidade (G3)
description: Questões, hipóteses e métricas do objetivo de medição G3, que avalia a flexibilidade da biblioteca e da aplicação web do Excalidraw
---

# GQM de Flexibilidade (G3)

Esta página detalha o objetivo G3, definido em [Método GQM e objetivos de medição](./estrutura-gqm.md#g3--flexibilidade-antiga-portabilidade). Para cada subcaracterística de Flexibilidade há uma questão, a hipótese da questão e as métricas que a respondem.

| Campo do template | Valor |
| :--- | :--- |
| Analisar | a biblioteca `@excalidraw/excalidraw` e a aplicação web, incluindo a interface pública da biblioteca, as instruções de instalação e os formatos de exportação |
| para o propósito de | entender |
| com respeito a | Flexibilidade: adaptabilidade, escalabilidade, instalabilidade e substituibilidade |
| do ponto de vista de | desenvolvedores que integram a biblioteca em seus sistemas e equipes de implantação e operação |
| no contexto de | código-fonte público na versão de 18/10/2026, avaliado por equipe independente |

As questões caracterizam o produto em relação a cada subcaracterística (AULA 08, p. 33 e 34). As hipóteses partem da [abstraction sheet de G3](./abstraction-sheets.md#5-g3--flexibilidade), como a aula permite (AULA 08, p. 34). As métricas respondem às questões de forma quantitativa (AULA 08, p. 38). Os níveis de pontuação e os critérios de julgamento de cada métrica são definidos em uma página própria da Fase 02.

---

## 1. Visão geral

| Questão | Subcaracterística | Requisitos da Fase 01 | Métricas |
| :--- | :--- | :--- | :--- |
| Q3.1 | Adaptabilidade | RQ-FLEX-01 a RQ-FLEX-04 | M3.1.1, M3.1.2, M3.1.3 |
| Q3.2 | Escalabilidade | RQ-FLEX-05 e RQ-FLEX-06 | M3.2.1, M3.2.2, M3.2.3 |
| Q3.3 | Instalabilidade | RQ-FLEX-07 a RQ-FLEX-10 | M3.3.1, M3.3.2, M3.3.3 |
| Q3.4 | Substituibilidade | RQ-FLEX-11 e RQ-FLEX-12 | M3.4.1, M3.4.2, M3.4.3 |

Os requisitos estão em [Requisitos da avaliação](../fase-01/requisitos-avaliacao.md). A seção 7 mostra qual métrica atende cada requisito.

---

## 2. Convenções de coleta

As definições abaixo valem para todas as métricas de G3 e evitam que pessoas diferentes testem coisas diferentes.

- **Versão avaliada:** commit `e1b7aac` do repositório oficial, de 18/10/2026, identificado no [escopo](../fase-01/escopo-avaliacao.md).
- **Pacote avaliado:** a biblioteca `@excalidraw/excalidraw` construída a partir da versão avaliada (script `build:packages` do repositório) e empacotada com `npm pack`. A versão publicada no npm mais próxima é usada só quando a métrica pede uma versão anterior.
- **Ambiente de teste:** a aplicação web construída a partir da versão avaliada e executada localmente, em uma máquina e em um navegador de versões fixas. O ambiente exato (máquina, sistema operacional, navegador, Node.js e gerenciadores de pacotes) é definido no plano de avaliação da Fase 03 e registrado em cada coleta.
- **Ambiente limpo:** contêiner ou máquina virtual sem as ferramentas de desenvolvimento instaladas além das exigidas pela métrica, para que nenhum pré-requisito esquecido passe despercebido.
- **Cena de referência:** desenho padronizado usado nos testes, com ao menos um elemento de cada tipo principal: retângulo, elipse, losango, seta, linha, desenho livre, texto, texto dentro de forma, imagem e moldura (*frame*). É a mesma cena usada no objetivo de Confiabilidade.
- **Cenas de escala:** cenas geradas por script com 100, 1.000, 5.000 e 10.000 elementos, em proporção fixa: 40% retângulos, 20% elipses, 20% setas e 20% textos, distribuídos em uma grade. O script fica no repositório da avaliação para que as cenas possam ser recriadas.

Os fatores que podem influenciar os resultados também são registrados junto com cada coleta (AULA 08, p. 38): o hardware, o navegador e sua versão, as versões de Node.js e dos gerenciadores de pacotes, e a composição das cenas de teste. Esses fatores foram levantados na abstraction sheet de G3.

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
| 1.0 | 19/10/2026 | Criação das questões, hipóteses e métricas do objetivo G3 | [Christopher Paraizo](https://github.com/wChrstphr) | |
