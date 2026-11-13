---
sidebar_position: 0
title: "Visão Geral da Fase 04"
description: "Visão geral da execução da avaliação, estrutura dos documentos, repositório de dados brutos e consolidados, e síntese dos resultados da qualidade."
---

# Fase 04: Execução da Avaliação

## Introdução

A [Fase 01](../fase-01/visao-geral.md) estabeleceu os requisitos e o propósito da avaliação, a [Fase 02](../fase-02/visao-geral.md) definiu o modelo GQM e os critérios de julgamento, e a Fase 03 planejou os métodos, recursos e instruções de coleta. A Fase 04 materializa a execução prática da avaliação sobre a versão congelada do Excalidraw no commit `e1b7aacb356a492aa1e0fc6eb57b8896124027f0`. O objetivo desta página é apresentar a estrutura da fase de execução, relacionar os documentos produzidos, disponibilizar os dados empíricos brutos e consolidados, e sintetizar os resultados obtidos na avaliação da qualidade.

## Metodologia

A condução da Fase 04 segue as instruções e a infraestrutura homologadas na Fase 03. Os avaliadores executam a medição das 36 métricas nas estações de trabalho e contêineres Docker padronizados, gerando evidências primárias registradas em pastas específicas. Os dados brutos passam por conferência independente e cálculo automático para geração das tabelas consolidadas. A partir dos dados consolidados, as pontuações são atribuídas conforme a régua Heitlager de 1 a 5 pontos e os critérios de corte da TÜViT da Fase 02, fundamentando o diagnóstico de fraquezas e as ações de melhoria de engenharia de software.

## Documentos desta fase

<p className="tabela-titulo">Tabela 1: Documentos da Fase 04</p>

| Documento | Conteúdo | Situação |
| :--- | :--- | :--- |
| [Insights e descobertas: Flexibilidade (G3)](./insights-e-descobertas-g3.md) | Relatório preliminar da coleta empírica com diagnósticos técnicos, comportamento do software e oportunidades de melhoria mapeadas | Publicado |
| [Resultados e julgamento: Flexibilidade (G3)](./resultados-g3-flexibilidade.md) | Relatório formal consolidando a obtenção das medidas de G3, respostas às quatro questões GQM, confronto de hipóteses e julgamento da característica | Publicado |
| Resultados e julgamento: Manutenibilidade (G1) | Relatório formal de medição, respostas GQM e julgamento de modularidade, reusabilidade, analisabilidade, modificabilidade e testabilidade | Em elaboração |
| Resultados e julgamento: Confiabilidade (G2) | Relatório formal de medição, respostas GQM e julgamento de ausência de falhas, maturidade e recuperabilidade | Em elaboração |
| Julgamento integrado e relações entre as características | Avaliação global do produto, coerência com o propósito da avaliação e cruzamento das características | Em elaboração |
| Oportunidades de melhoria e escolha da ação | Diagnóstico das fraquezas mapeadas nas medições e detalhamento da intervenção de melhoria de software | Em elaboração |

<p className="tabela-fonte">Fonte: [Maria Eduarda](https://github.com/eduarda-ogomes), 2026.</p>

## Repositório de medidas e dados da avaliação

Todas as evidências geradas durante os testes estão disponibilizadas no repositório de medidas do projeto, organizadas em duas camadas:

1. **Dados brutos (`dados/fase-04/brutos/`):** Arquivos primários obtidos diretamente das execuções, preservados sem alteração manual para garantir auditabilidade. Incluem saídas de terminal, matrizes de compatibilidade em CSV, perfis temporais em JSON gerados pelo Chrome DevTools, capturas de tela e gravações de vídeo em dispositivo móvel com caneta stylus.
2. **Dados consolidados (`dados/fase-04/consolidados/`):** Tabelas geradas após a verificação e o recálculo dos indicadores, consolidando as métricas, os níveis Heitlager e o status das hipóteses operacionais em formato legível por humanos e scripts.

As instruções para reprodução dos comandos e o inventário dos arquivos brutos constam no guia do [Repositório de Dados da Fase 04](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/dados/fase-04/README.md).

## Síntese dos resultados por característica

Os resultados refletem a aplicação estrita das faixas de pontuação da Fase 02:

- **G3: Flexibilidade:** Concluída com média agregada de **3,9 pontos (Nível Bom `+`)**, obtendo 9 hipóteses confirmadas e 3 refutadas. O software **atende** aos critérios de qualidade para a característica, apresentando excelente suporte tátil e alta capacidade de persistência, com pontos de atenção no suporte a SSR em frameworks legados e na documentação do formato de arquivo.
- **G1: Manutenibilidade e G2: Confiabilidade:** Coletas concluídas, em processo de verificação independente e redação dos relatórios analíticos pelos responsáveis.

## Relação com as fases anteriores

A execução da Fase 04 concretiza as diretrizes do plano de medição e do cronograma estabelecidos na Fase 03, utilizando os ambientes e a massa de dados padronizados. A interpretação dos valores utiliza diretamente as hipóteses e as réguas dos [níveis de pontuação e critérios de julgamento da Fase 02](../fase-02/pontuacao-julgamento.md). Essa estrutura garante que o diagnóstico final atenda às necessidades das partes interessadas delineadas na [Fase 01](../fase-01/interessados.md).

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| `1.0` | 13/11/2026 | Criação da página de visão geral da Fase 04 com tabela de documentos, estrutura de dados e síntese de resultados | [Maria Eduarda](https://github.com/eduarda-ogomes) | |
