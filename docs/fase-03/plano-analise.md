---
sidebar_position: 6
title: Plano de análise
description: Tratamento dos dados coletados na Fase 04, tabela consolidada das medições, apresentação dos resultados e comparação com as hipóteses e os fatores de variação
---

import Link from '@docusaurus/Link';

# Plano de análise

## Introdução

O plano de análise simula a interpretação antes de a medição começar: define como as medidas são processadas, de que forma são apresentadas e como as hipóteses e os fatores de variação serão comparados com os valores reais [[1, p. 46]](#ref-1). Ele foi fixado antes da [coleta da Fase 04](./cronograma-avaliacao.md), de 10 a 12/11/2026, para que nenhuma decisão de tratamento ou de apresentação seja tomada depois de ver os dados.

O objetivo desta página é descrever o caminho dos dados coletados até a resposta das questões e o julgamento das características de [G1](../fase-02/gqm-manutenibilidade.md), [G2](../fase-02/gqm-confiabilidade.md) e [G3](../fase-02/gqm-flexibilidade.md).

## Metodologia

A maior parte das regras de análise já foi definida na Fase 02: o cálculo e o critério de interpretação de cada métrica estão nas fichas do GQM, e a pontuação, a agregação e o julgamento estão nos [níveis de pontuação](../fase-02/pontuacao-julgamento.md). Esta página liga essas regras às [instruções do avaliador](./instrucoes-g3-flexibilidade.md) e aos [recursos de avaliação](./recursos-ambiente.md) da Fase 03 e acrescenta só o que faltava: o tratamento dos dados, o formato da tabela consolidada, as formas de apresentação, a comparação das hipóteses e a revisão da interpretação, seguindo a orientação de organizar os dados por questão e objetivo, com gráficos e tabelas [[1, p. 56]](#ref-1).

---

## 1. Fluxo da análise

A análise segue seis etapas, da medição ao julgamento. A conversão do valor em nível e a agregação até a característica seguem os passos já definidos nas [diretrizes de interpretação do Plano GQM](../fase-02/plano-gqm.md#5-diretrizes-de-interpretação). A tabela mostra o que cada etapa recebe, o que produz e onde está a regra.

<p className="tabela-titulo">Tabela 1: Etapas da análise</p>

| Etapa | Entrada | Saída | Regra |
| :--- | :--- | :--- | :--- |
| 1. Coleta | Comandos, formulários e gravações das instruções do avaliador | Arquivos em `dados/fase-04/brutos/` | Procedimento de coleta das fichas de [G1](../fase-02/gqm-manutenibilidade.md), [G2](../fase-02/gqm-confiabilidade.md) e [G3](../fase-02/gqm-flexibilidade.md), [instruções de G3](./instrucoes-g3-flexibilidade.md#3-instruções-detalhadas-por-métrica) e [seção 2](#2-tratamento-dos-dados) |
| 2. Consolidação | Arquivos brutos | Valor medido de cada métrica, em `dados/fase-04/consolidados/metricas.csv` | Procedimento de cálculo de cada ficha e [seção 3](#3-tabela-consolidada-e-script-de-análise) |
| 3. Conversão | `metricas.csv` | Valor pontuado de cada métrica | Coluna "Valor pontuado" das faixas de [G1](../fase-02/pontuacao-julgamento.md#3-níveis-das-métricas-de-manutenibilidade-g1), [G2](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2) e [G3](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3) |
| 4. Pontuação e julgamento | Valores das métricas | Nível de cada métrica, média de cada questão e julgamento de cada característica | [Faixas](../fase-02/pontuacao-julgamento.md#2-como-as-faixas-foram-definidas), [agregação](../fase-02/pontuacao-julgamento.md#6-agregação-da-métrica-à-característica) e [julgamento](../fase-02/pontuacao-julgamento.md#71-julgamento-de-cada-característica) |
| 5. Apresentação | Resultados da etapa 4 | Tabelas e gráficos do relatório | [Seção 4](#4-apresentação-dos-resultados) |
| 6. Interpretação | Resultados, hipóteses e fatores de variação registrados | Hipóteses confirmadas ou refutadas e [pontos de melhoria](../fase-02/pontuacao-julgamento.md#73-pontos-de-melhoria), revisados | Seções [5](#5-hipóteses-e-fatores-de-variação) e [6](#6-interpretação-e-revisão) |

<p className="tabela-fonte">Fonte: [Christopher Paraizo](https://github.com/wChrstphr), 2026.</p>

A etapa 2 é feita por um script de cálculo, na verificação dos dados brutos, e as etapas 3 a 5 por um script de análise, na análise de cada característica. Com os dois scripts, qualquer pessoa pode repetir o cálculo a partir dos mesmos dados.

---

## 2. Tratamento dos dados

As regras abaixo cobrem situações que as fichas e os níveis de pontuação não tratam. Elas existem para que nenhuma decisão sobre os dados seja tomada depois de conhecer o resultado.

**Valores extremos.** Nenhum valor é descartado nas medições repetidas, como as cinco repetições de tempo de abertura e de taxa de quadros. O valor da métrica é a mediana prevista na ficha ou nas [instruções do avaliador](./instrucoes-g3-flexibilidade.md#3-instruções-detalhadas-por-métrica), que já reduz o efeito de uma repetição muito diferente das outras.

**Falha do ambiente.** Quando a medição falha por causa do ambiente (rede, máquina, ferramenta de medição) e não do Excalidraw, a coleta é repetida uma vez, com o motivo registrado na tabela consolidada. Se a falha se repetir, a métrica é tratada como [não coletada](../fase-02/pontuacao-julgamento.md#61-métricas-não-coletadas). As [condições de controle das coletas](./recursos-ambiente.md#3-máquinas-dos-responsáveis-pela-coleta) ajudam a separar uma falha do ambiente de uma falha do produto.

**Nome dos arquivos brutos.** Os arquivos de G1, G2 e G3 ficam em `dados/fase-04/brutos/` e seguem a convenção `M<código>_<identificador-curto>.<extensão>` das [instruções de G3](./instrucoes-g3-flexibilidade.md#22-local-e-padrão-de-nomenclatura-dos-dados-brutos), por exemplo `M1.4.2_cloc_por_arquivo.csv`. Com um padrão único, o script de cálculo encontra o arquivo de qualquer métrica pelo código.

---

## 3. Tabela consolidada e script de análise

Na verificação dos dados brutos, feita por quem não coletou, um script de cálculo lê os arquivos de `dados/fase-04/brutos/`, calcula o valor de cada métrica pelo procedimento da ficha e reúne todos os valores de G1, G2 e G3 em um único arquivo, `dados/fase-04/consolidados/metricas.csv`. As métricas que dependem de julgamento humano, como as verificadas por formulário, têm o valor conferido à mão e registrado no mesmo arquivo. Cada linha guarda um valor medido. A métrica com um valor por cena, por formato ou por pacote ocupa uma linha para cada um, porque cada valor é pontuado separadamente antes da média, pela [regra das métricas com vários valores](../fase-02/pontuacao-julgamento.md#23-regras-gerais).

<p className="tabela-titulo">Tabela 2: Colunas de metricas.csv</p>

| Coluna | Conteúdo | Exemplo |
| :--- | :--- | :--- |
| `metrica` | Código da métrica | `M3.2.1` |
| `item` | Cena, formato ou pacote do valor, vazio quando a métrica tem um valor só | `cena_1000`, `svg` |
| `valor` | Valor medido, calculado pelo procedimento da ficha, com ponto como separador decimal, vazio quando não coletada | `0.84` |
| `unidade` | Unidade do valor | `s`, `%`, `itens` |
| `status` | `coletada` ou `nao_coletada` | `coletada` |
| `motivo` | Obrigatório quando a métrica não foi coletada ou quando a coleta foi repetida | `rede caiu na 1ª coleta` |
| `arquivo_bruto` | Caminho do arquivo bruto que originou o valor | `dados/fase-04/brutos/M3.2.1_tempos_abertura.csv` |
| `data` | Data da coleta, no formato AAAA-MM-DD | `2026-11-11` |
| `avaliador` | Usuário do GitHub de quem coletou | `login-github` |

<p className="tabela-fonte">Fonte: [Christopher Paraizo](https://github.com/wChrstphr), 2026.</p>

Exemplo com valores fictícios: uma métrica de valor único, uma métrica com um valor por cena e uma métrica não coletada.

```csv
metrica,item,valor,unidade,status,motivo,arquivo_bruto,data,avaliador
M1.4.2,,4.1,%,coletada,,dados/fase-04/brutos/M1.4.2_cloc_por_arquivo.csv,2026-11-10,login-github
M3.2.1,cena_100,0.31,s,coletada,,dados/fase-04/brutos/M3.2.1_tempos_abertura.csv,2026-11-11,login-github
M3.2.1,cena_1000,0.84,s,coletada,,dados/fase-04/brutos/M3.2.1_tempos_abertura.csv,2026-11-11,login-github
M3.1.3,,,itens,nao_coletada,dispositivo de toque falhou na coleta e na repetição,dados/fase-04/brutos/M3.1.3_formulario_toque.md,2026-11-12,login-github
```

A análise de cada característica parte de `metricas.csv`. O script de análise, em Python com a biblioteca matplotlib, converte cada valor medido no valor pontuado e no nível, aplica a agregação e o julgamento e gera as tabelas e os gráficos da [seção 4](#4-apresentação-dos-resultados). Ele grava em `dados/fase-04/consolidados/`:

- `niveis.csv`: valor pontuado, nível e pontos de cada linha de `metricas.csv`.
- `questoes.csv`: média e nível de cada questão, com o número de métricas coletadas.
- `caracteristicas.csv`: média, nível e julgamento de cada característica.

Os dois scripts são implementados na Fase 04 e ficam em `scripts/`, junto aos demais scripts do repositório. Esta seção é a especificação da entrada e das saídas deles.

---

## 4. Apresentação dos resultados

Os resultados são organizados por questão e por objetivo, com tabelas e gráficos [[1, p. 56]](#ref-1). As formas de apresentação são fixadas aqui para que não sejam escolhidas depois, a favor de um resultado.

**Tabela por questão.** Cada questão do GQM tem uma tabela no relatório da Fase 04, no modelo abaixo, que liga cada métrica ao seu nível e à sua hipótese.

<p className="tabela-titulo">Tabela 3: Modelo da tabela de resultados de uma questão</p>

| Métrica | Valor | Nível | Hipótese | Resultado da hipótese |
| :--- | :---: | :---: | :--- | :--- |
| Código da métrica, com link para a ficha | Valor pontuado | `++` a `--` | Código da hipótese | Confirmada ou refutada |
| **Média da questão** | | Nível da questão | | |

<p className="tabela-fonte">Fonte: [Christopher Paraizo](https://github.com/wChrstphr), 2026.</p>

**Gráfico por característica.** Cada característica tem um gráfico de barras horizontais com uma barra por questão, de comprimento igual à média da questão, em um eixo de 1 a 5. Uma linha vertical marca o 3, nível `o`, que é o mínimo para a característica [atender](../fase-02/pontuacao-julgamento.md#71-julgamento-de-cada-característica). O gráfico mostra de uma vez quais questões puxam a característica para baixo.

**Gráficos específicos.** Em quatro métricas, o tipo de gráfico para demonstração das métricas será diferente, por conta da natureza da mesma:

- [M1.3.1](../fase-02/gqm-manutenibilidade.md#m131--perfil-de-risco-de-complexidade-das-funções): barra empilhada com a parte das linhas em cada faixa de risco de complexidade, que mostra qual dos três limites definiu o nível.
- [M3.2.1](../fase-02/gqm-flexibilidade.md#m321--tempo-de-abertura-por-tamanho-de-cena): curva do tempo de abertura pelo tamanho da cena, com os limites das faixas marcados, que mostra a partir de qual tamanho o tempo passa a interromper o usuário.
- [M3.2.2](../fase-02/gqm-flexibilidade.md#m322--taxa-de-quadros-durante-a-edição-por-tamanho-de-cena): curva da taxa de quadros pelo tamanho da cena, com a meta de 60 quadros por segundo, que mostra onde a edição deixa de ser fluida.
- [M3.4.2](../fase-02/gqm-flexibilidade.md#m342--proporção-de-elementos-preservados-na-exportação-e-reimportação): uma barra por formato de exportação, que mostra se a perda de elementos se concentra em um formato.

---

## 5. Hipóteses e fatores de variação

O nível de cada métrica e a sua hipótese são avaliados separadamente, pela [regra das hipóteses](../fase-02/pontuacao-julgamento.md#72-hipóteses). Na Fase 04, cada hipótese de baseline é comparada com o valor real [[1, p. 46]](#ref-1) pela regra de confirmação do critério de interpretação da ficha da métrica, e o resultado, *confirmada* ou *refutada*, é registrado na página de resultados de cada característica. Na maior parte das hipóteses, o valor comparado é o próprio valor pontuado. Nas demais, a regra usa uma contagem, um pacote ou uma cena específica, como [H3.2.1](../fase-02/gqm-flexibilidade.md#4-q32--escalabilidade), que considera só a cena de 1.000 elementos.

Os fatores de variação de cada coleta, como máquina, navegador e estado da rede, são registrados junto com a medição, conforme os [recursos de avaliação](./recursos-ambiente.md#9-fatores-de-variação-registrados-em-cada-coleta). Quando uma hipótese for refutada, a análise verifica primeiro se algum fator registrado explica o resultado, consultando o quadrante 4º, de impacto nas hipóteses, da abstraction sheet do objetivo ([G1](../fase-02/abstraction-sheets.md#3-g1--manutenibilidade), [G2](../fase-02/abstraction-sheets.md#4-g2--confiabilidade) ou [G3](../fase-02/abstraction-sheets.md#5-g3--flexibilidade)). Só depois a refutação é atribuída ao Excalidraw.

Não é feita análise estatística do efeito de cada fator, porque os fatores não são variados de propósito na coleta: eles são mantidos sob as [condições de controle](./recursos-ambiente.md#3-máquinas-dos-responsáveis-pela-coleta) e apenas registrados.

---

## 6. Interpretação e revisão

Na interpretação, a equipe GQM organiza os dados e os apresenta em uma sessão de *feedback*, mas não deve realizar a interpretação [[1, p. 56]](#ref-1). Nesta avaliação a mesma equipe mede e interpreta, e a revisão do *pull request* do relatório de cada característica cumpre esse papel, com duas regras:

- **Revisor independente:** quem revisa o relatório de uma característica não pode ter coletado as métricas dela.
- **Revisão da interpretação:** o revisor confere se cada conclusão decorre do valor medido e da regra correspondente, e se toda explicação por um fator de variação tem registro na coleta que a sustente.

A decisão conjunta da equipe acontece na [escolha da ação de melhoria](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/118), em 16/11/2026, a partir dos pontos de melhoria aprovados na revisão.

---

## Referências

> <Link id="ref-1">1.</Link> RAMOS, Cristiane Soares. **AULA 08 QSW1 GQM**. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Páginas 46 e 56. Disponível no Moodle da disciplina.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 08/11/2026 | Criação do plano de análise: fluxo, tratamento dos dados, tabela consolidada, apresentação, hipóteses e interpretação | [Christopher Paraizo](https://github.com/wChrstphr) | |
