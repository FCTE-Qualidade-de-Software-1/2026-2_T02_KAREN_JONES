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

## 2. Como as faixas foram definidas

Cada métrica tem cinco faixas de valores, uma para cada nível. As faixas vêm de quatro origens, aplicadas nesta ordem:

1. **Faixas publicadas para a própria métrica.** O modelo de Heitlager, Kuipers e Visser publica faixas para a complexidade das funções (p. 6) e para a cobertura de testes (p. 7). As métricas M1.3.1 e M1.5.1 usam essas faixas sem alteração.
2. **Faixas de proporção desejável.** Para as métricas que medem a parte de um conjunto que atende a um critério (por exemplo, funções que funcionam sem conexão ou contribuições revisadas), a equipe reaproveita as faixas de cobertura de testes do modelo, que medem o mesmo tipo de grandeza: a parte do código que os testes alcançam (p. 7).
3. **Faixas de proporção indesejável.** Para as métricas que medem a parte de um conjunto que tem um problema (por exemplo, importações que violam a direção declarada), a equipe reaproveita as faixas de duplicação de código do modelo, que medem a parte do código que é cópia de outra (p. 7).
4. **Referências externas ou faixas da equipe.** As métricas de tempo e de fluidez usam limites publicados de tempo de resposta e de taxa de quadros. As métricas restantes têm faixas definidas pela equipe, sempre com a justificativa registrada na tabela.

O modelo também avalia propriedades que não são métricas de código por meio de listas de verificação (p. 8), mas não publica as faixas usadas nesses casos. Por isso, o reaproveitamento das faixas de cobertura e de duplicação nas origens 2 e 3 é uma decisão da equipe, e não uma regra do modelo.

### 2.1 Faixas de proporção desejável

Quanto maior o valor, melhor. Faixas de cobertura de testes de Heitlager, Kuipers e Visser (2007, p. 7):

| Nível | `++` | `+` | `o` | `-` | `--` |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Percentual | 95 a 100 | 80 a 95 | 60 a 80 | 20 a 60 | 0 a 20 |

### 2.2 Faixas de proporção indesejável

Quanto menor o valor, melhor. Faixas de duplicação de código de Heitlager, Kuipers e Visser (2007, p. 7):

| Nível | `++` | `+` | `o` | `-` | `--` |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Percentual | 0 a 3 | 3 a 5 | 5 a 10 | 10 a 20 | 20 a 100 |

### 2.3 Regras gerais

- **Valor no limite:** um valor igual ao limite entre duas faixas fica no nível melhor. Por exemplo, 95% em uma proporção desejável é `++`, e 3% em uma proporção indesejável é `++`.
- **Sem arredondamento:** os percentuais são comparados com as faixas sem arredondar. Por exemplo, 94,9% é `+`.
- **Listas fixas:** quando a métrica é uma lista fixa de itens, as tabelas das seções 3 a 5 mostram quantos itens correspondem a cada nível. Em listas curtas, um único item que falha já tira a métrica do nível `++`. Isso é intencional, porque cada item da lista é uma função considerada essencial.
- **Métricas com vários valores:** quando a métrica tem um valor por cena, por formato ou por tipo de entrada, cada valor é pontuado e a pontuação da métrica é a média dos pontos, como na agregação da seção 6.

---

## Referências

- AULA A07 QSW1 PROC AVAL PRODUTO. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Páginas 4, 16 e 17.
- HEITLAGER, I.; KUIPERS, T.; VISSER, J. A Practical Model for Measuring Maintainability. In: *6th International Conference on the Quality of Information and Communications Technology (QUATIC 2007)*. IEEE, 2007. p. 30–39. Páginas 5 a 8 da versão dos autores, disponível em: https://www.di.uminho.pt/~joost/publications/HeitlagerKuipersVisser-Quatic2007.pdf.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 19/10/2026 | Criação da escala, das faixas de cada métrica, das regras de agregação e dos critérios de julgamento | [Christopher Paraizo](https://github.com/wChrstphr) | |
