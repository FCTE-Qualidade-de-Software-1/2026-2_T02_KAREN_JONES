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

## 3. Níveis das métricas de Manutenibilidade (G1)

Os códigos das métricas são os das fichas do [GQM de Manutenibilidade](./gqm-manutenibilidade.md): M1.1.1 é a primeira métrica da questão Q1.1, M1.1.2 é a segunda, e assim por diante. A coluna "Valor pontuado" indica qual resultado da ficha é comparado com as faixas.

| Métrica | Valor pontuado | `++` | `+` | `o` | `-` | `--` | Origem das faixas |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| M1.1.1 | Pares de pacotes em ciclo ÷ 28 pares possíveis × 100 (ver seção 3.2) | 0 pares | 1 par | 2 pares | 3 a 5 pares | 6 ou mais | Proporção indesejável (seção 2.2) |
| M1.1.2 | Importações que violam a direção ÷ importações de valor entre pacotes diferentes × 100 | 0 a 3% | 3 a 5% | 5 a 10% | 10 a 20% | acima de 20% | Proporção indesejável (seção 2.2) |
| M1.1.3 | Dependências entre pacotes que contrariam o Princípio das Dependências Estáveis ÷ dependências entre pacotes × 100 | 0 a 3% | 3 a 5% | 5 a 10% | 10 a 20% | acima de 20% | Proporção indesejável (seção 2.2), com a regra de Martin (1997) |
| M1.2.1 | Arquivos dos pacotes de base com dependência de React ou do navegador ÷ arquivos de produção dos pacotes de base × 100 | 0 a 3% | 3 a 5% | 5 a 10% | 10 a 20% | acima de 20% | Proporção indesejável (seção 2.2) |
| M1.2.2 | Percentual de propriedades documentadas | 95 a 100% | 80 a 95% | 60 a 80% | 20 a 60% | abaixo de 20% | Proporção desejável (seção 2.1) |
| M1.3.1 | Perfil de risco de complexidade, no total | ver tabela 3.1 | ver tabela 3.1 | ver tabela 3.1 | ver tabela 3.1 | ver tabela 3.1 | Publicada (Heitlager; Kuipers; Visser, 2007, p. 6) |
| M1.3.2 | Tópicos presentes (de 4) | 4 | — | 3 | 1 ou 2 | 0 | Proporção desejável (seção 2.1) |
| M1.3.3 | Verificações automáticas (de 3) | 3 | — | 2 | 1 | 0 | Proporção desejável (seção 2.1) |
| M1.4.1 | Mediana de arquivos de produção por contribuição | até 2 | 3 ou 4 | 5 a 8 | 9 a 16 | mais de 16 | Equipe (ver abaixo) |
| M1.4.2 | Arquivos com mais de 1.000 linhas ÷ arquivos de produção × 100 | 0 a 3% | 3 a 5% | 5 a 10% | 10 a 20% | acima de 20% | Proporção indesejável (seção 2.2) |
| M1.4.3 | Percentual de contribuições que alteram arquivos extensos | 0 a 3% | 3 a 5% | 5 a 10% | 10 a 20% | acima de 20% | Proporção indesejável (seção 2.2) |
| M1.5.1 | Cobertura de linhas, no total | 95 a 100% | 80 a 95% | 60 a 80% | 20 a 60% | abaixo de 20% | Publicada (Heitlager; Kuipers; Visser, 2007, p. 7) |
| M1.5.2 | Níveis de teste presentes (de 3: unitário, integração e ponta a ponta) | 3 | — | 2 | 1 | 0 | Proporção desejável (seção 2.1) |
| M1.5.3 | Percentual de contribuições com testes executados antes da integração | 95 a 100% | 80 a 95% | 60 a 80% | 20 a 60% | abaixo de 20% | Proporção desejável (seção 2.1) |

Um traço (—) indica que nenhum valor possível da lista cai naquele nível.

### 3.1 Faixas de M1.3.1

A métrica M1.3.1 distribui as linhas de código pelas faixas de risco de complexidade das funções: baixo (1 a 10), moderado (11 a 20), alto (21 a 50) e muito alto (acima de 50). O nível é o melhor cujos três limites são respeitados ao mesmo tempo (Heitlager; Kuipers; Visser, 2007, p. 6):

| Nível | Linhas em risco moderado (máximo) | Linhas em risco alto (máximo) | Linhas em risco muito alto (máximo) |
| :---: | :---: | :---: | :---: |
| `++` | 25% | 0% | 0% |
| `+` | 30% | 5% | 0% |
| `o` | 40% | 10% | 0% |
| `-` | 50% | 15% | 5% |
| `--` | acima de 50% | acima de 15% | acima de 5% |

O nível `--` é atribuído quando qualquer um dos limites do nível `-` é ultrapassado. Por exemplo, um código com 20% das linhas em risco moderado, 3% em risco alto e 1% em risco muito alto é `-`, porque ultrapassa o limite de 0% de risco muito alto dos níveis `++`, `+` e `o`.

### 3.2 Justificativas específicas

Esta seção explica só as métricas em que o valor pontuado não é o próprio resultado da ficha ou em que as faixas não vêm diretamente da seção 2. As demais pontuam o percentual ou a lista fixa da ficha, com as faixas indicadas na tabela.

- **M1.1.1:** o Excalidraw tem 8 pacotes, como definido nas [convenções de coleta de G1](./gqm-manutenibilidade.md#2-convenções-de-coleta): as sete pastas de `packages/` (`common`, `element`, `excalidraw`, `fractional-indexing`, `laser-pointer`, `math` e `utils`) e a aplicação web (`excalidraw-app/`). A métrica conta os pares de pacotes em ciclo, isto é, dois pacotes em que cada um depende do outro, direta ou indiretamente. Com 8 pacotes, existem 28 pares possíveis (8 × 7 ÷ 2). Para usar as faixas de proporção indesejável, o número de pares em ciclo é dividido por 28. Assim, 1 par em ciclo (3,6%) fica no nível `+`, e 6 ou mais pares (21,4% ou mais) ficam no nível `--`.
- **M1.1.2, M1.2.1 e M1.4.2:** as fichas dessas métricas dão contagens de importações ou de arquivos. Para usar as faixas de proporção indesejável, cada contagem é dividida pelo total indicado na coluna "Valor pontuado", para que o resultado não dependa do tamanho do projeto.
- **M1.1.3:** o Princípio das Dependências Estáveis diz que um pacote deve depender apenas de pacotes mais estáveis do que ele, ou seja, a instabilidade *I* deve diminuir no sentido das dependências (Martin, 1997, p. 8 e 10). Uma dependência de A para B contraria o princípio quando *I* de A é menor que *I* de B. A contagem usa as mesmas dependências entre pacotes de M1.1.3. A hipótese sobre o pacote com maior Ca continua sendo verificada à parte, como descrito no GQM de G1.
- **M1.4.1:** não foi encontrada referência publicada com faixas para o número de arquivos por contribuição. A equipe usa faixas que dobram de tamanho (2, 4, 8 e 16 arquivos), porque cada nível abaixo representa o dobro de arquivos para quem revisa a contribuição.

---

## Referências

- AULA A07 QSW1 PROC AVAL PRODUTO. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Páginas 4, 16 e 17.
- HEITLAGER, I.; KUIPERS, T.; VISSER, J. A Practical Model for Measuring Maintainability. In: *6th International Conference on the Quality of Information and Communications Technology (QUATIC 2007)*. IEEE, 2007. p. 30–39. Páginas 5 a 8 da versão dos autores, disponível em: https://www.di.uminho.pt/~joost/publications/HeitlagerKuipersVisser-Quatic2007.pdf.
- MARTIN, R. C. Stability. *The C++ Report*, 1997. Páginas 8 e 10. Disponível em: https://objectmentor.com/resources/articles/stability.pdf.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 19/10/2026 | Criação da escala, das faixas de cada métrica, das regras de agregação e dos critérios de julgamento | [Christopher Paraizo](https://github.com/wChrstphr) | |
