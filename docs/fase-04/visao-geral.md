---
sidebar_position: 0
title: "Visão Geral da Fase 04"
description: "Visão geral da execução da avaliação, estrutura dos documentos, repositório de dados brutos e consolidados, e síntese dos resultados da qualidade."
---

# Fase 04: Execução da Avaliação

## Introdução

A [Fase 01](../fase-01/visao-geral.md) estabeleceu os requisitos e o propósito da avaliação, a [Fase 02](../fase-02/visao-geral.md) definiu o modelo GQM e os critérios de julgamento, e a [Fase 03](../fase-03/visao-geral.md) planejou os métodos, recursos e instruções de coleta. A Fase 04 materializa a execução prática da avaliação sobre a versão congelada do Excalidraw no commit `e1b7aacb356a492aa1e0fc6eb57b8896124027f0`. O objetivo desta página é apresentar a estrutura da fase de execução, relacionar os documentos produzidos, disponibilizar os dados empíricos brutos e consolidados, e sintetizar os resultados obtidos na avaliação da qualidade.

## Metodologia

A condução da Fase 04 segue as instruções e a infraestrutura homologadas na Fase 03. Os avaliadores executam a medição das 36 métricas nas estações de trabalho e contêineres Docker padronizados, gerando evidências primárias registradas em pastas específicas. Os dados brutos passam por conferência independente e cálculo automático para geração das tabelas consolidadas. A partir dos dados consolidados, as pontuações são atribuídas conforme a régua Heitlager de 1 a 5 pontos e os critérios de corte da TÜViT da Fase 02, fundamentando o diagnóstico de fraquezas e as ações de melhoria de engenharia de software.

## Documentos desta fase

<p className="tabela-titulo">Tabela 1: Documentos da Fase 04</p>

| Documento | Conteúdo | Situação |
| :--- | :--- | :--- |
| [Resultados: Manutenibilidade (G1)](./resultados-g1-manutenibilidade.md) | Medição das 14 métricas, confronto de hipóteses, respostas às questões Q1.1 a Q1.5, julgamento e pontos de melhoria de G1 | Publicado |
| [Resultados e Julgamento: Confiabilidade (G2)](./resultados-g2-confiabilidade.md) | Medição das 10 métricas, análise das questões Q2.1 a Q2.4, testes manuais com gravação em vídeo, rastreabilidade e julgamento de G2 | Publicado |
| [Resultados e julgamento: Flexibilidade (G3)](./resultados-g3-flexibilidade.md) | Medição das 12 métricas, análise das questões Q3.1 a Q3.4, matrizes de compatibilidade, testes de carga, rastreabilidade e julgamento de G3 | Publicado |
| [Julgamento Final e Relações entre Características](./julgamento.md) | Julgamento consolidado do produto, coerência com o propósito da Fase 01, análise das relações entre características e limites de validade | Publicado |
| [Oportunidades de melhoria](./melhorias.md) | Levantamento das oportunidades com base nas métricas em níveis críticos, critérios de priorização, ação proposta e avaliação do impacto | Publicado |

<p className="tabela-fonte">Fonte: [Maria Eduarda](https://github.com/eduarda-ogomes), 2026.</p>

## Repositório de medidas e dados da avaliação

Todas as evidências geradas durante os testes estão disponibilizadas no repositório de medidas do projeto, organizadas em duas camadas:

1. **Dados brutos (`dados/fase-04/brutos/`):** Arquivos primários obtidos diretamente das execuções, preservados sem alteração manual para garantir auditabilidade. Incluem saídas de terminal, matrizes de compatibilidade em CSV, perfis temporais em JSON gerados pelo Chrome DevTools, capturas de tela e gravações de vídeo em dispositivo móvel com caneta stylus.
2. **Dados consolidados (`dados/fase-04/consolidados/`):** Tabelas geradas após a verificação e o recálculo dos indicadores, consolidando as métricas, os níveis Heitlager e o status das hipóteses operacionais em formato legível por humanos e scripts.

As instruções para reprodução dos comandos e o inventário dos arquivos brutos constam no guia do [Repositório de Dados da Fase 04](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/dados/fase-04/README.md).

## Síntese dos resultados por característica

Os resultados refletem a aplicação estrita das faixas de pontuação da Fase 02:

- **G1: Manutenibilidade:** Média agregada de **2,9 pontos (Nível Regular `o`)**, com 9 hipóteses confirmadas e 5 refutadas. O produto **não atende** aos critérios de qualidade para a característica devido ao bloqueio da subcaracterística de Reusabilidade (Q1.2 no nível `--`), provocado pelo acoplamento de 69,07% dos arquivos dos pacotes de base com React e o navegador (M1.2.1) e por 42,31% das propriedades públicas sem documentação (M1.2.2).
- **G2: Confiabilidade:** Média agregada de **3,9 pontos (Nível Bom `+`)**, com 6 hipóteses confirmadas e 4 refutadas. O produto **atende** aos critérios de qualidade para a característica, demonstrando operação offline plena (M2.2.1 em `++`), continuidade em falhas de colaboração (M2.3.2 em `++`) e compatibilidade retroativa na recuperação de arquivos (M2.4.2 em `++`), com ponto de atenção na ausência de revisão humana em 55,48% das integrações (M2.1.3 em `-`).
- **G3: Flexibilidade:** Média agregada de **3,9 pontos (Nível Bom `+`)**, com 9 hipóteses confirmadas e 3 refutadas. O produto **atende** aos critérios de qualidade para a característica, apresentando excelente suporte tátil e alta capacidade de persistência e conversão de formatos (M3.1.3 e M3.4.2 em `++`), com pontos de atenção no suporte a SSR em frameworks legados (M3.1.2) e na documentação do formato de arquivo (M3.4.3).
- **Julgamento integrado e melhoria:** Sob a ótica de uso e interoperabilidade, o Excalidraw atende aos requisitos de qualidade (G2 e G3 em nível `+`), mas não atende em Manutenibilidade interna do código. A ação de melhoria proposta foca na documentação das propriedades públicas de `ExcalidrawProps` (M1.2.2), intervenção viável capaz de elevar a reusabilidade e permitir que G1 atinja o nível de atendimento.

## Relação com as fases anteriores

A execução da Fase 04 concretiza as diretrizes do plano de medição e do cronograma estabelecidos na [Fase 03](../fase-03/visao-geral.md), utilizando os ambientes e a massa de dados padronizados. A interpretação dos valores utiliza diretamente as hipóteses e as réguas dos [níveis de pontuação e critérios de julgamento da Fase 02](../fase-02/pontuacao-julgamento.md). Essa estrutura garante que o diagnóstico final atenda às necessidades das partes interessadas delineadas na [Fase 01](../fase-01/interessados.md).

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| `1.0` | 13/11/2026 | Criação da página de visão geral da Fase 04 com tabela de documentos, estrutura de dados e síntese de resultados | [Maria Eduarda](https://github.com/eduarda-ogomes) | |
| `1.1` | 17/11/2026 | Atualização da tabela de documentos publicados, consolidação dos resultados de G1, G2, G3, julgamento final e oportunidades de melhoria | [Maria Eduarda](https://github.com/eduarda-ogomes) | |
