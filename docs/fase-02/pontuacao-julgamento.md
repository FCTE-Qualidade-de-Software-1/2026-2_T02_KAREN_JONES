---
sidebar_position: 6
title: Níveis de pontuação e critérios de julgamento
description: Escala de pontuação das métricas de G1, G2 e G3, faixas de valores de cada métrica, agregação até a característica e critérios para julgar os resultados
---

# Níveis de pontuação e critérios de julgamento

Esta página define como cada resultado das métricas de [G1](./gqm-manutenibilidade.md), [G2](./gqm-confiabilidade.md) e [G3](./gqm-flexibilidade.md) será transformado em um nível de pontuação e como esses níveis serão combinados e julgados. A aula pede que, na especificação da avaliação, sejam estabelecidos níveis de pontuação para as métricas e critérios para julgamento (AULA A07, p. 4), desdobrando as subcaracterísticas em atributos que possam ser medidos e pontuados (AULA A07, p. 16). Julgar a qualidade é interpretar os resultados das medições (AULA A07, p. 17).

Todas as regras desta página foram definidas antes da coleta, que acontece na Fase 04. Assim, as faixas não podem ser ajustadas para favorecer ou prejudicar o resultado.

---

## 1. Escala de pontuação

A equipe adota a escala de cinco níveis do modelo de manutenibilidade de Heitlager, Kuipers e Visser (2007), usada para pontuar tanto as propriedades medidas quanto as características: `++` / `+` / `o` / `-` / `--` (Heitlager; Kuipers; Visser, 2007, p. 5). O modelo foi criado para ligar métricas de código-fonte às características de qualidade da ISO/IEC 9126, que deu origem à ISO/IEC 25010, e tem regras explícitas para pontuar e para agregar os resultados.

| Nível | Símbolo | Pontos | Leitura |
| :--- | :---: | :---: | :--- |
| Excelente | `++` | 5 | O resultado está na melhor faixa prevista. |
| Bom | `+` | 4 | O resultado está acima do esperado para um projeto típico. |
| Regular | `o` | 3 | O resultado está na faixa intermediária. |
| Ruim | `-` | 2 | O resultado indica um problema que afeta a característica. |
| Muito ruim | `--` | 1 | O resultado indica um problema grave ou generalizado. |

Os nomes dos níveis e os pontos de 1 a 5 são da equipe. O modelo usa só os símbolos e calcula médias entre níveis (p. 8), o que exige um valor numérico para cada um.

---

## Referências

- AULA A07 QSW1 PROC AVAL PRODUTO. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Páginas 4, 16 e 17.
- HEITLAGER, I.; KUIPERS, T.; VISSER, J. A Practical Model for Measuring Maintainability. In: *6th International Conference on the Quality of Information and Communications Technology (QUATIC 2007)*. IEEE, 2007. p. 30–39. Página 5 da versão dos autores, disponível em: https://www.di.uminho.pt/~joost/publications/HeitlagerKuipersVisser-Quatic2007.pdf.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 19/10/2026 | Criação da escala, das faixas de cada métrica, das regras de agregação e dos critérios de julgamento | [Christopher Paraizo](https://github.com/wChrstphr) | |
