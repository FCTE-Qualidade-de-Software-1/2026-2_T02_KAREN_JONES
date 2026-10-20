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

1. **Faixas publicadas para a própria métrica.** O modelo de Heitlager, Kuipers e Visser publica faixas para a complexidade das funções (p. 6) e para a cobertura de testes (p. 7). As métricas [M1.3.1](./gqm-manutenibilidade.md#m131--perfil-de-risco-de-complexidade-das-funções) e [M1.5.1](./gqm-manutenibilidade.md#m151--cobertura-de-linhas-por-pacote) usam essas faixas sem alteração.
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
- **Listas fixas:** quando a métrica é uma lista fixa de itens, as tabelas das seções [3](#3-níveis-das-métricas-de-manutenibilidade-g1) a [5](#5-níveis-das-métricas-de-flexibilidade-g3) mostram quantos itens correspondem a cada nível. Em listas curtas, um único item que falha já tira a métrica do nível `++`. Isso é intencional, porque cada item da lista é uma função considerada essencial.
- **Métricas com vários valores:** quando a métrica tem um valor por cena, por formato ou por tipo de entrada, cada valor é pontuado e a pontuação da métrica é a média dos pontos, como na agregação da [seção 6](#6-agregação-da-métrica-à-característica).

---

## 3. Níveis das métricas de Manutenibilidade (G1)

Os códigos das métricas são os das fichas do [GQM de Manutenibilidade](./gqm-manutenibilidade.md): [M1.1.1](./gqm-manutenibilidade.md#m111--ciclos-de-dependência-entre-pacotes) é a primeira métrica da questão [Q1.1](./gqm-manutenibilidade.md#3-q11--modularidade), [M1.1.2](./gqm-manutenibilidade.md#m112--importações-que-violam-a-direção-declarada) é a segunda, e assim por diante. A coluna "Valor pontuado" indica qual resultado da ficha é comparado com as faixas.

| Métrica | Valor pontuado | `++` | `+` | `o` | `-` | `--` | Origem das faixas |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| [M1.1.1](./gqm-manutenibilidade.md#m111--ciclos-de-dependência-entre-pacotes) | Pares de pacotes em ciclo ÷ 28 pares possíveis × 100 (ver [seção 3.2](#32-justificativas-específicas)) | 0 pares | 1 par | 2 pares | 3 a 5 pares | 6 ou mais | Proporção indesejável ([seção 2.2](#22-faixas-de-proporção-indesejável)) |
| [M1.1.2](./gqm-manutenibilidade.md#m112--importações-que-violam-a-direção-declarada) | Importações que violam a direção ÷ importações de valor entre pacotes diferentes × 100 | 0 a 3% | 3 a 5% | 5 a 10% | 10 a 20% | acima de 20% | Proporção indesejável ([seção 2.2](#22-faixas-de-proporção-indesejável)) |
| [M1.1.3](./gqm-manutenibilidade.md#m113--acoplamento-e-instabilidade-de-cada-pacote) | Dependências entre pacotes que contrariam o Princípio das Dependências Estáveis ÷ dependências entre pacotes × 100 | 0 a 3% | 3 a 5% | 5 a 10% | 10 a 20% | acima de 20% | Proporção indesejável ([seção 2.2](#22-faixas-de-proporção-indesejável)), com a regra de Martin (1997) |
| [M1.2.1](./gqm-manutenibilidade.md#m121--arquivos-de-pacotes-de-base-com-dependência-de-react-ou-do-navegador) | Arquivos dos pacotes de base com dependência de React ou do navegador ÷ arquivos de produção dos pacotes de base × 100 | 0 a 3% | 3 a 5% | 5 a 10% | 10 a 20% | acima de 20% | Proporção indesejável ([seção 2.2](#22-faixas-de-proporção-indesejável)) |
| [M1.2.2](./gqm-manutenibilidade.md#m122--proporção-de-propriedades-públicas-documentadas) | Percentual de propriedades documentadas | 95 a 100% | 80 a 95% | 60 a 80% | 20 a 60% | abaixo de 20% | Proporção desejável ([seção 2.1](#21-faixas-de-proporção-desejável)) |
| [M1.3.1](./gqm-manutenibilidade.md#m131--perfil-de-risco-de-complexidade-das-funções) | Perfil de risco de complexidade, no total | ver [tabela 3.1](#31-faixas-de-m131) | ver [tabela 3.1](#31-faixas-de-m131) | ver [tabela 3.1](#31-faixas-de-m131) | ver [tabela 3.1](#31-faixas-de-m131) | ver [tabela 3.1](#31-faixas-de-m131) | Publicada (Heitlager; Kuipers; Visser, 2007, p. 6) |
| [M1.3.2](./gqm-manutenibilidade.md#m132--cobertura-da-documentação-para-desenvolvedores) | Tópicos presentes (de 4) | 4 | nenhum | 3 | 1 ou 2 | 0 | Proporção desejável ([seção 2.1](#21-faixas-de-proporção-desejável)) |
| [M1.3.3](./gqm-manutenibilidade.md#m133--verificações-estáticas-executadas-automaticamente) | Verificações automáticas (de 3) | 3 | nenhum | 2 | 1 | 0 | Proporção desejável ([seção 2.1](#21-faixas-de-proporção-desejável)) |
| [M1.4.1](./gqm-manutenibilidade.md#m141--mediana-de-arquivos-de-produção-alterados-por-contribuição) | Mediana de arquivos de produção por contribuição | até 2 | 3 ou 4 | 5 a 8 | 9 a 16 | mais de 16 | Equipe (ver abaixo) |
| [M1.4.2](./gqm-manutenibilidade.md#m142--arquivos-de-produção-extensos) | Arquivos com mais de 1.000 linhas ÷ arquivos de produção × 100 | 0 a 3% | 3 a 5% | 5 a 10% | 10 a 20% | acima de 20% | Proporção indesejável ([seção 2.2](#22-faixas-de-proporção-indesejável)) |
| [M1.4.3](./gqm-manutenibilidade.md#m143--proporção-de-contribuições-que-alteram-arquivos-extensos) | Percentual de contribuições que alteram arquivos extensos | 0 a 3% | 3 a 5% | 5 a 10% | 10 a 20% | acima de 20% | Proporção indesejável ([seção 2.2](#22-faixas-de-proporção-indesejável)) |
| [M1.5.1](./gqm-manutenibilidade.md#m151--cobertura-de-linhas-por-pacote) | Cobertura de linhas, no total | 95 a 100% | 80 a 95% | 60 a 80% | 20 a 60% | abaixo de 20% | Publicada (Heitlager; Kuipers; Visser, 2007, p. 7) |
| [M1.5.2](./gqm-manutenibilidade.md#m152--distribuição-dos-testes-por-nível) | Níveis de teste presentes (de 3: unitário, integração e ponta a ponta) | 3 | nenhum | 2 | 1 | 0 | Proporção desejável ([seção 2.1](#21-faixas-de-proporção-desejável)) |
| [M1.5.3](./gqm-manutenibilidade.md#m153--proporção-de-contribuições-com-testes-executados-antes-da-integração) | Percentual de contribuições com testes executados antes da integração | 95 a 100% | 80 a 95% | 60 a 80% | 20 a 60% | abaixo de 20% | Proporção desejável ([seção 2.1](#21-faixas-de-proporção-desejável)) |

A palavra "nenhum" indica que nenhum valor possível da lista cai naquele nível.

### 3.1 Faixas de M1.3.1

A métrica [M1.3.1](./gqm-manutenibilidade.md#m131--perfil-de-risco-de-complexidade-das-funções) distribui as linhas de código pelas faixas de risco de complexidade das funções: baixo (1 a 10), moderado (11 a 20), alto (21 a 50) e muito alto (acima de 50). O nível é o melhor cujos três limites são respeitados ao mesmo tempo (Heitlager; Kuipers; Visser, 2007, p. 6):

| Nível | Linhas em risco moderado (máximo) | Linhas em risco alto (máximo) | Linhas em risco muito alto (máximo) |
| :---: | :---: | :---: | :---: |
| `++` | 25% | 0% | 0% |
| `+` | 30% | 5% | 0% |
| `o` | 40% | 10% | 0% |
| `-` | 50% | 15% | 5% |
| `--` | acima de 50% | acima de 15% | acima de 5% |

O nível `--` é atribuído quando qualquer um dos limites do nível `-` é ultrapassado. Por exemplo, um código com 20% das linhas em risco moderado, 3% em risco alto e 1% em risco muito alto é `-`, porque ultrapassa o limite de 0% de risco muito alto dos níveis `++`, `+` e `o`.

### 3.2 Justificativas específicas

Esta seção explica só as métricas em que o valor pontuado não é o próprio resultado da ficha ou em que as faixas não vêm diretamente da [seção 2](#2-como-as-faixas-foram-definidas). As demais pontuam o percentual ou a lista fixa da ficha, com as faixas indicadas na tabela.

- **[M1.1.1](./gqm-manutenibilidade.md#m111--ciclos-de-dependência-entre-pacotes):** o Excalidraw tem 8 pacotes, como definido nas [convenções de coleta de G1](./gqm-manutenibilidade.md#2-convenções-de-coleta): as sete pastas de `packages/` (`common`, `element`, `excalidraw`, `fractional-indexing`, `laser-pointer`, `math` e `utils`) e a aplicação web (`excalidraw-app/`). A métrica conta os pares de pacotes em ciclo, isto é, dois pacotes em que cada um depende do outro, direta ou indiretamente. Com 8 pacotes, existem 28 pares possíveis (8 × 7 ÷ 2). Para usar as faixas de proporção indesejável, o número de pares em ciclo é dividido por 28. Assim, 1 par em ciclo (3,6%) fica no nível `+`, e 6 ou mais pares (21,4% ou mais) ficam no nível `--`.
- **[M1.1.2](./gqm-manutenibilidade.md#m112--importações-que-violam-a-direção-declarada), [M1.2.1](./gqm-manutenibilidade.md#m121--arquivos-de-pacotes-de-base-com-dependência-de-react-ou-do-navegador) e [M1.4.2](./gqm-manutenibilidade.md#m142--arquivos-de-produção-extensos):** as fichas dessas métricas dão contagens de importações ou de arquivos. Para usar as faixas de proporção indesejável, cada contagem é dividida pelo total indicado na coluna "Valor pontuado", para que o resultado não dependa do tamanho do projeto.
- **[M1.1.3](./gqm-manutenibilidade.md#m113--acoplamento-e-instabilidade-de-cada-pacote):** o Princípio das Dependências Estáveis diz que um pacote deve depender apenas de pacotes mais estáveis do que ele, ou seja, a instabilidade *I* deve diminuir no sentido das dependências (Martin, 1997, p. 8 e 10). Uma dependência de A para B contraria o princípio quando *I* de A é menor que *I* de B. A contagem usa as mesmas dependências entre pacotes de M1.1.3. A hipótese sobre o pacote com maior Ca continua sendo verificada à parte, pelo critério de interpretação da ficha.
- **[M1.4.1](./gqm-manutenibilidade.md#m141--mediana-de-arquivos-de-produção-alterados-por-contribuição):** não foi encontrada referência publicada com faixas para o número de arquivos por contribuição. A equipe usa faixas que dobram de tamanho (2, 4, 8 e 16 arquivos), porque cada nível abaixo representa o dobro de arquivos para quem revisa a contribuição.

---

## 4. Níveis das métricas de Confiabilidade (G2)

Os códigos das métricas são os das fichas do [GQM de Confiabilidade](./gqm-confiabilidade.md).

| Métrica | Valor pontuado | `++` | `+` | `o` | `-` | `--` | Origem das faixas |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| [M2.1.1](./gqm-confiabilidade.md#m211--proporção-de-correções-entre-as-contribuições-integradas) | Percentual de correções entre as contribuições integradas | 0 a 20% | 20 a 40% | 40 a 60% | 60 a 80% | acima de 80% | Equipe (ver abaixo) |
| [M2.1.2](./gqm-confiabilidade.md#m212--mediana-do-tempo-entre-o-relato-e-a-correção) | Mediana de dias entre o relato e a correção | até 7 | 8 a 14 | 15 a 30 | 31 a 90 | mais de 90 | Equipe (ver abaixo) |
| [M2.1.3](./gqm-confiabilidade.md#m213--proporção-de-contribuições-revisadas-antes-da-integração) | Percentual de contribuições revisadas por outra pessoa | 95 a 100% | 80 a 95% | 60 a 80% | 20 a 60% | abaixo de 20% | Proporção desejável ([seção 2.1](#21-faixas-de-proporção-desejável)) |
| [M2.2.1](./gqm-confiabilidade.md#m221--proporção-de-funções-essenciais-disponíveis-sem-conexão) | Funções que funcionam sem conexão (de 10) | 10 | 8 ou 9 | 6 ou 7 | 2 a 5 | 0 ou 1 | Proporção desejável ([seção 2.1](#21-faixas-de-proporção-desejável)) |
| [M2.2.2](./gqm-confiabilidade.md#m222--origens-externas-necessárias-para-o-editor-local) | Domínios externos indispensáveis e total de domínios externos | nenhum domínio externo | nenhum indispensável; 1 a 3 externos | nenhum indispensável; 4 ou mais externos | 1 indispensável | 2 ou mais indispensáveis | Equipe (ver abaixo) |
| [M2.3.1](./gqm-confiabilidade.md#m231--proporção-de-arquivos-inválidos-tratados-com-mensagem) | Arquivos inválidos tratados (de 9) | 9 | 8 | 6 ou 7 | 2 a 5 | 0 ou 1 | Proporção desejável ([seção 2.1](#21-faixas-de-proporção-desejável)) |
| [M2.3.2](./gqm-confiabilidade.md#m232--continuidade-do-editor-após-falha-da-colaboração) | Verificações que passam após a falha da colaboração (de 5) | 5 | 4 | 3 | 1 ou 2 | 0 | Proporção desejável ([seção 2.1](#21-faixas-de-proporção-desejável)) |
| [M2.4.1](./gqm-confiabilidade.md#m241--proporção-de-cenários-de-fechamento-com-restauração-do-desenho) | Cenários de fechamento com restauração (de 4) | 4 | nenhum | 3 | 1 ou 2 | 0 | Proporção desejável ([seção 2.1](#21-faixas-de-proporção-desejável)) |
| [M2.4.2](./gqm-confiabilidade.md#m242--proporção-de-arquivos-reabertos-sem-perda) | Arquivos reabertos sem perda (de 7) | 7 | 6 | 5 | 2 a 4 | 0 ou 1 | Proporção desejável ([seção 2.1](#21-faixas-de-proporção-desejável)) |
| [M2.4.3](./gqm-confiabilidade.md#m243--cobertura-de-desfazer-e-refazer) | Tipos de ação desfeitos e refeitos (de 10) | 10 | 8 ou 9 | 6 ou 7 | 2 a 5 | 0 ou 1 | Proporção desejável ([seção 2.1](#21-faixas-de-proporção-desejável)) |

O conjunto de [M2.4.2](./gqm-confiabilidade.md#m242--proporção-de-arquivos-reabertos-sem-perda) tem 7 arquivos: a cena de referência salva pela versão avaliada e pelas versões v0.15.0, v0.16.4, v0.17.6 e v0.18.0, e as duas imagens com desenho incorporado.

### 4.1 Justificativas específicas

Esta seção explica só as métricas em que o valor pontuado não é o próprio resultado da ficha ou em que as faixas não vêm diretamente da [seção 2](#2-como-as-faixas-foram-definidas). As demais pontuam o percentual ou a lista fixa da ficha, com as faixas indicadas na tabela.

- **[M2.1.1](./gqm-confiabilidade.md#m211--proporção-de-correções-entre-as-contribuições-integradas):** menos correções significam menos falhas encontradas no período, por isso o valor menor é o melhor. Não foi encontrada referência publicada com a proporção esperada de correções. As faixas de proporção indesejável não servem aqui, porque foram feitas para algo raro, como a duplicação de código: qualquer projeto ativo teria mais de 20% de correções e ficaria no nível `--`. Por isso, a equipe divide a escala de 0 a 100% em cinco faixas de mesma largura, sem escolher limites próprios.
- **[M2.1.2](./gqm-confiabilidade.md#m212--mediana-do-tempo-entre-o-relato-e-a-correção):** não foi encontrada referência publicada com faixas para o tempo de correção. A equipe usa unidades de calendário que um usuário percebe: uma semana, duas semanas, um mês e três meses.
- **[M2.2.2](./gqm-confiabilidade.md#m222--origens-externas-necessárias-para-o-editor-local):** um domínio indispensável é um serviço externo cuja queda impede o uso do editor, por isso basta um para o nível `-`. Domínios externos que não são indispensáveis não impedem o uso, mas ainda são dependências de terceiros, e por isso diferenciam os níveis `++`, `+` e `o`. Os limites são da equipe.

---

## 5. Níveis das métricas de Flexibilidade (G3)

Os códigos das métricas são os das fichas do [GQM de Flexibilidade](./gqm-flexibilidade.md).

| Métrica | Valor pontuado | `++` | `+` | `o` | `-` | `--` | Origem das faixas |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| [M3.1.1](./gqm-flexibilidade.md#m311--cobertura-de-usuários-pelos-navegadores-declarados) | Percentual de usuários cobertos pelos navegadores declarados | 95 a 100% | 80 a 95% | 60 a 80% | 20 a 60% | abaixo de 20% | Proporção desejável ([seção 2.1](#21-faixas-de-proporção-desejável)) |
| [M3.1.2](./gqm-flexibilidade.md#m312--proporção-de-ambientes-de-integração-com-sucesso) | Combinações de React e empacotador com sucesso (de 6) | 6 | 5 | 4 | 2 ou 3 | 0 ou 1 | Proporção desejável ([seção 2.1](#21-faixas-de-proporção-desejável)) |
| [M3.1.3](./gqm-flexibilidade.md#m313--proporção-de-ações-de-edição-que-funcionam-por-toque-e-caneta) | Ações que funcionam por toque (de 10) | 10 | 8 ou 9 | 6 ou 7 | 2 a 5 | 0 ou 1 | Proporção desejável ([seção 2.1](#21-faixas-de-proporção-desejável)) |
| [M3.2.1](./gqm-flexibilidade.md#m321--tempo-de-abertura-por-tamanho-de-cena) | Tempo de abertura de cada cena de escala | até 1 s | 1 a 2 s | 2 a 5 s | 5 a 10 s | mais de 10 s | Nielsen (1993) e RAIL (ver abaixo) |
| [M3.2.2](./gqm-flexibilidade.md#m322--taxa-de-quadros-durante-a-edição-por-tamanho-de-cena) | Quadros por segundo de cada cena ÷ 60 × 100 | 57 ou mais | 48 a 57 | 36 a 48 | 12 a 36 | menos de 12 | Proporção desejável ([seção 2.1](#21-faixas-de-proporção-desejável)), com a meta de 60 quadros do RAIL |
| [M3.2.3](./gqm-flexibilidade.md#m323--tamanho-máximo-de-cena-salva-e-exportada) | Maior cena salva e exportada | 10.000 elementos | 5.000 | 1.000 | 100 | nenhuma | Equipe (ver abaixo) |
| [M3.3.1](./gqm-flexibilidade.md#m331--proporção-de-operações-de-pacote-bem-sucedidas) | Operações de pacote com sucesso (de 9) | 9 | 8 | 6 ou 7 | 2 a 5 | 0 ou 1 | Proporção desejável ([seção 2.1](#21-faixas-de-proporção-desejável)) |
| [M3.3.2](./gqm-flexibilidade.md#m332--proporção-de-passos-documentados-reproduzidos-sem-ajuste) | Percentual de passos reproduzidos sem ajuste | 95 a 100% | 80 a 95% | 60 a 80% | 20 a 60% | abaixo de 20% | Proporção desejável ([seção 2.1](#21-faixas-de-proporção-desejável)) |
| [M3.3.3](./gqm-flexibilidade.md#m333--implantação-com-docker) | Verificações do Docker que passam (de 4) | 4 | nenhum | 3 | 1 ou 2 | 0 | Proporção desejável ([seção 2.1](#21-faixas-de-proporção-desejável)) |
| [M3.4.1](./gqm-flexibilidade.md#m341--formatos-de-exportação-abertos-disponíveis) | Formatos de exportação abertos | 4 ou mais | 3 | 2 | 1 | 0 | Equipe (ver abaixo) |
| [M3.4.2](./gqm-flexibilidade.md#m342--proporção-de-elementos-preservados-na-exportação-e-reimportação) | Percentual de elementos preservados em cada formato | 95 a 100% | 80 a 95% | 60 a 80% | 20 a 60% | abaixo de 20% | Proporção desejável ([seção 2.1](#21-faixas-de-proporção-desejável)) |
| [M3.4.3](./gqm-flexibilidade.md#m343--proporção-dos-campos-do-formato-excalidraw-documentados) | Percentual de campos do formato documentados | 95 a 100% | 80 a 95% | 60 a 80% | 20 a 60% | abaixo de 20% | Proporção desejável ([seção 2.1](#21-faixas-de-proporção-desejável)) |

### 5.1 Justificativas específicas

Esta seção explica só as métricas em que o valor pontuado não é o próprio resultado da ficha ou em que as faixas não vêm diretamente da [seção 2](#2-como-as-faixas-foram-definidas). As demais pontuam o percentual ou a lista fixa da ficha, com as faixas indicadas na tabela.

- **[M3.1.3](./gqm-flexibilidade.md#m313--proporção-de-ações-de-edição-que-funcionam-por-toque-e-caneta):** a pontuação usa o toque com o dedo. Se houver caneta disponível, as duas formas de entrada são pontuadas e a pontuação da métrica é a média das duas.
- **[M3.2.1](./gqm-flexibilidade.md#m321--tempo-de-abertura-por-tamanho-de-cena):** os limites de 1 e de 10 segundos são os de Nielsen (1993): até 1 segundo, o raciocínio do usuário não é interrompido, e 10 segundos é o limite para manter a atenção dele na tarefa. Os limites intermediários de 2 e de 5 segundos são as metas do modelo RAIL, do Google, para carregar uma página já visitada e uma página nova. O RAIL trata do carregamento de páginas; a equipe o aplica à abertura de um arquivo por ser a referência publicada mais próxima. Cada uma das quatro cenas de escala é pontuada, e a pontuação da métrica é a média.
- **[M3.2.2](./gqm-flexibilidade.md#m322--taxa-de-quadros-durante-a-edição-por-tamanho-de-cena):** o RAIL considera fluida a animação com 60 quadros por segundo. A taxa medida é convertida em percentual dessa meta e pontuada com as faixas de proporção desejável. Cada cena é pontuada, e a pontuação da métrica é a média.
- **[M3.2.3](./gqm-flexibilidade.md#m323--tamanho-máximo-de-cena-salva-e-exportada):** a métrica tem cinco resultados possíveis (as quatro cenas de escala ou nenhuma), e cada um corresponde a um nível.
- **[M3.4.1](./gqm-flexibilidade.md#m341--formatos-de-exportação-abertos-disponíveis):** a hipótese de G3 espera três formatos abertos (`.excalidraw`, PNG e SVG), o que corresponde ao nível `+`. Cada formato a menos desce um nível. Os limites são da equipe.
- **[M3.4.2](./gqm-flexibilidade.md#m342--proporção-de-elementos-preservados-na-exportação-e-reimportação):** cada um dos três formatos é pontuado, e a pontuação da métrica é a média.

---

## 6. Agregação: da métrica à característica

As pontuações são combinadas em duas etapas, com pesos iguais, como no modelo de Heitlager, Kuipers e Visser (2007, p. 8):

1. **Questão:** a pontuação de cada questão é a média aritmética dos pontos das suas métricas. Como cada questão corresponde a uma subcaracterística, essa é também a pontuação da subcaracterística.
2. **Característica:** a pontuação de cada característica (G1, G2 e G3) é a média aritmética das médias das suas questões, sem arredondá-las antes.

A média é convertida em nível pelo arredondamento para o inteiro mais próximo. Uma média terminada exatamente em 0,5 é arredondada para baixo, para que o resultado não seja favorecido em caso de empate. O relatório mostra a média com uma casa decimal e o nível correspondente. Essa regra de arredondamento é da equipe, porque o modelo não a define.

Não é calculada uma pontuação única para o Excalidraw. Os autores do modelo também não veem valor em um número único: as pontuações por subcaracterística dizem mais e podem ser rastreadas até as métricas que as originaram (Heitlager; Kuipers; Visser, 2007, p. 8).

### 6.1 Métricas não coletadas

Uma métrica que não puder ser coletada na Fase 04 fica fora da média da sua questão, e o motivo é registrado no relatório. Uma questão sem nenhuma métrica coletada fica sem pontuação e é marcada como não avaliada. Se mais da metade das métricas de uma característica não for coletada, a característica não é julgada, porque o resultado não representaria o objetivo.

### 6.2 Exemplo de cálculo

Valores fictícios, apenas para mostrar o cálculo:

| Questão | Pontos das métricas | Média | Nível da questão |
| :--- | :--- | :---: | :---: |
| Questão A | `++` (5), `o` (3), `+` (4) | 4,0 | `+` |
| Questão B | `-` (2), `o` (3) | 2,5 | `-` |
| Questão C | `--` (1), `-` (2), `o` (3) | 2,0 | `-` |

Média da característica: (4,0 + 2,5 + 2,0) ÷ 3 = 2,8, que é arredondada para 3, nível `o`. A questão B tem média 2,5 e fica no nível `-`, pela regra de arredondamento para baixo.

---

## 7. Critérios de julgamento

### 7.1 Julgamento de cada característica

Cada característica recebe um de três resultados:

| Resultado | Condição |
| :--- | :--- |
| **Atende** | A característica tem nível `o` ou melhor, e nenhuma das suas questões está no nível `--`. |
| **Não atende** | A característica tem nível `-` ou `--`, ou pelo menos uma das suas questões está no nível `--`. |
| **Inconclusiva** | Mais da metade das métricas da característica não foi coletada ([seção 6.1](#61-métricas-não-coletadas)). |

O limite vem do esquema de certificação de manutenibilidade da TÜViT, que usa o modelo de Heitlager, Kuipers e Visser em uma escala de 1 a 5 estrelas. Para obter o certificado, um sistema precisa de ao menos 2 estrelas em todas as subcaracterísticas e de ao menos 3 estrelas na característica (Baggen; Schill; Visser, 2010, p. 3). Na escala desta página, 2 estrelas correspondem ao nível `-` e 3 estrelas ao nível `o`. A equipe aplica o mesmo limite às três características avaliadas.

No exemplo da [seção 6.2](#62-exemplo-de-cálculo), a característica atende: o nível dela é `o`, e nenhuma questão está no nível `--`.

### 7.2 Hipóteses

O nível de pontuação e a hipótese de cada métrica são avaliados separadamente. A hipótese é confirmada ou refutada pelo critério de interpretação da ficha da métrica, nas páginas de [G1](./gqm-manutenibilidade.md), [G2](./gqm-confiabilidade.md) e [G3](./gqm-flexibilidade.md). Uma métrica pode estar no nível `++` e refutar a hipótese, por exemplo quando a equipe esperava um resultado pior. O relatório registra os dois resultados, porque as hipóteses auxiliam na interpretação dos resultados (AULA 08, p. 34): uma hipótese refutada mostra onde a expectativa da equipe sobre o Excalidraw estava errada.

### 7.3 Pontos de melhoria

Toda métrica no nível `-` ou `--` é registrada no relatório como ponto de melhoria, com a questão e a subcaracterística afetadas. Como cada nível pode ser rastreado até a métrica que o originou, o relatório indica a causa de cada resultado ruim, e não só o resultado (Heitlager; Kuipers; Visser, 2007, p. 8).

---

## 8. Limitações

- **Calibração:** as faixas do modelo foram definidas pela experiência dos autores com sistemas industriais (Heitlager; Kuipers; Visser, 2007, p. 6). Depois, o modelo passou a ser recalibrado todo ano com uma base de sistemas reais, de forma que 5%, 30%, 30%, 30% e 5% dos sistemas fiquem em cada nível (Baggen; Schill; Visser, 2010, p. 2). A equipe não tem acesso a essa base e usa as faixas publicadas em 2007, sem recalibrar para projetos em TypeScript.
- **Reaproveitamento de faixas:** as faixas de cobertura e de duplicação foram publicadas para essas duas propriedades. Usá-las para outras proporções ([seção 2](#2-como-as-faixas-foram-definidas)) é uma decisão da equipe.
- **Faixas da equipe:** as métricas [M1.4.1](./gqm-manutenibilidade.md#m141--mediana-de-arquivos-de-produção-alterados-por-contribuição), [M2.1.1](./gqm-confiabilidade.md#m211--proporção-de-correções-entre-as-contribuições-integradas), [M2.1.2](./gqm-confiabilidade.md#m212--mediana-do-tempo-entre-o-relato-e-a-correção), [M2.2.2](./gqm-confiabilidade.md#m222--origens-externas-necessárias-para-o-editor-local), [M3.2.3](./gqm-flexibilidade.md#m323--tamanho-máximo-de-cena-salva-e-exportada) e [M3.4.1](./gqm-flexibilidade.md#m341--formatos-de-exportação-abertos-disponíveis) têm faixas definidas pela equipe, com as justificativas das seções [3.2](#32-justificativas-específicas), [4.1](#41-justificativas-específicas) e [5.1](#51-justificativas-específicas).
- **Norma de origem:** o modelo foi feito para a ISO/IEC 9126. A equipe aplica a mesma escala e a mesma agregação às subcaracterísticas da ISO/IEC 25010 escolhidas na Fase 01.

---

## Referências

- AULA 08 QSW1 GQM. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Página 34.
- AULA A07 QSW1 PROC AVAL PRODUTO. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Páginas 4, 16 e 17.
- BAGGEN, R.; SCHILL, K.; VISSER, J. Standardized Code Quality Benchmarking for Improving Software Maintainability. In: *4th International Workshop on Software Quality and Maintainability (SQM 2010)*, 2010. Páginas 2 e 3. Disponível em: https://webarchive.di.uminho.pt/wiki.di.uminho.pt/twiki/pub/Personal/Joost/PublicationList/SQM2010-StandardizedCodeQuality.pdf. Versão ampliada: BAGGEN, R. et al. *Software Quality Journal*, v. 20, p. 287-307, 2012.
- GOOGLE. Measure performance with the RAIL model. *web.dev*, atualizado em 10/06/2020. Seções "Load" e "Animation". Disponível em: https://web.dev/articles/rail.
- HEITLAGER, I.; KUIPERS, T.; VISSER, J. A Practical Model for Measuring Maintainability. In: *6th International Conference on the Quality of Information and Communications Technology (QUATIC 2007)*. IEEE, 2007. p. 30-39. Páginas 5 a 8 da versão dos autores, disponível em: https://www.di.uminho.pt/~joost/publications/HeitlagerKuipersVisser-Quatic2007.pdf.
- MARTIN, R. C. Stability. *The C++ Report*, 1997. Páginas 8 e 10. Disponível em: https://objectmentor.com/resources/articles/stability.pdf.
- NIELSEN, J. *Usability Engineering*. Academic Press, 1993. Capítulo 5. Trecho disponível em: https://www.nngroup.com/articles/response-times-3-important-limits/.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 19/10/2026 | Criação da escala, das faixas de cada métrica, das regras de agregação e dos critérios de julgamento | [Christopher Paraizo](https://github.com/wChrstphr) | |
