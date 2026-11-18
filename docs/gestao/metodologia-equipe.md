---
title: Metodologia da equipe
description: Como a equipe Karen Jones conduz a avaliação do Excalidraw com as quatro fases da ISO/IEC 25040, a divisão em subgrupos e a governança no GitHub.
sidebar_label: Metodologia da equipe
sidebar_position: 5
---

# Metodologia da equipe

A condução deste trabalho combina o processo de avaliação da qualidade da norma ISO/IEC 25040 [\[1\]](#ref-1), o desdobramento orientado a metas do paradigma GQM (Goal Question Metric) [\[2\]](#ref-2) e práticas rigorosas de governança técnica no repositório. A Figura 1 sintetiza a metodologia adotada pela equipe, articulada nas quatro fases sequenciais da avaliação e na dimensão transversal de governança.

![Diagrama da metodologia da equipe com quatro caixas sequenciais, uma para cada fase da avaliação da qualidade (requisitos, especificação, projeto e execução), e uma quinta caixa transversal de estrutura da equipe e governança no GitHub.](../images/figura-metodologia.png)

*Figura 1: Diagrama metodológico do processo de avaliação da qualidade. Fonte: Equipe Karen Jones.*

## Caixa 1: Requisitos de Avaliação (Fase 1)

Estabelece o escopo e as prioridades do estudo antes da medição empírica. A equipe definiu como propósito identificar pontos de melhoria no Excalidraw, adotando o commit congelado `e1b7aac` como linha de base estática. A partir da identificação de sete partes interessadas e de uma matriz de impacto × risco técnico, priorizaram-se três características da ISO/IEC 25010:2023: Manutenibilidade (P1), Confiabilidade (P2) e Flexibilidade (P3). Foram delineadas 13 subcaracterísticas e 36 requisitos formais de avaliação (RQ-MAN-01 a RQ-FLEX-12). Esta etapa foi conduzida pelo Subgrupo F1/F3 na Entrega 1.

Detalhes nas [páginas da Fase 1](../fase-01/visao-geral.md).

## Caixa 2: Especificação da Avaliação (Fase 2)

Traduz os requisitos de qualidade em medição objetiva via GQM. As características foram desdobradas em três objetivos conceituais (G1, G2 e G3), 13 questões com hipóteses técnicas e um catálogo de 36 métricas com fórmulas matemáticas de cálculo. Para garantir imparcialidade prévia à coleta, definiu-se uma escala ordinal de cinco níveis (Heitlager/SIG) e critérios conclusivos de corte inspirados na TÜViT (Atende, Não Atende e Inconclusivo). Esta etapa foi conduzida pelo Subgrupo F2/F4 na Entrega 1.

Detalhes nas [páginas da Fase 2](../fase-02/visao-geral.md) e em [Pontuação e julgamento](../fase-02/pontuacao-julgamento.md).

## Caixa 3: Projeto da Avaliação (Fase 3)

Planeja a infraestrutura de medição e automação para inspeção estática e testes no ecossistema TypeScript e React, selecionando ferramentas consagradas (ESLint, API do TypeScript, ts-morph, cloc e Vitest). Formalizam-se o Plano de Medição e o Plano de Análise, preparando o processamento dos dados. A execução está planejada para a Entrega 2 sob a responsabilidade do Subgrupo F1/F3.

Detalhes em [Recursos e ambiente](../fase-03/recursos-ambiente.md) e nas demais páginas da Fase 3.

## Caixa 4: Execução da Avaliação e Julgamento (Fase 4)

Materializa a coleta empírica das 36 métricas sobre a linha de base congelada, confrontando os resultados com as hipóteses formuladas. A consolidação adota agregação matemática em duas etapas (média das métricas por questão e média das questões por característica), aplicando os critérios de corte da TÜViT para emissão do diagnóstico final e recomendação de melhorias na Entrega 2 pelo Subgrupo F2/F4.


## Caixa 5: Estrutura da Equipe e Governança no GitHub

Sustentação operacional transversal do projeto. A equipe organizou-se em dois subgrupos estáveis de três integrantes (Tabela 1) para atuar em paralelo sem sobreposição de escopo. A escrita do artigo e as apresentações ocorrem de maneira compartilhada por todos os membros.

*Tabela 1: Estrutura organizacional da equipe e distribuição de responsabilidades.*

| Subgrupo | Integrantes | Fases | Escopo principal |
| :--- | :--- | :--- | :--- |
| Subgrupo F1/F3 | Davi Pierre, Gabriel Monteiro e Letícia de Carvalho | Fase 1 e Fase 3 | Requisitos, interessados, modelo de qualidade e projeto de testes |
| Subgrupo F2/F4 | Christopher Paraizo, Luiz Henrique Soares e Maria Eduarda | Fase 2 e Fase 4 | Objetivos e métricas GQM, pontuação, execução prática e ações de melhoria |

O fluxo de trabalho no GitHub é estritamente regido pelo [guia de contribuição](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/CONTRIBUTING.md), vedando envios diretos na branch principal (`main`). Toda atividade nasce vinculada a uma issue padronizada com estimativa de horas, é desenvolvida em branch temática individual e integrada via pull request com fechamento automático da issue, declaração obrigatória de uso de IA generativa e revisão formal por ao menos um membro do grupo.

O acompanhamento da gestão usa as métricas PSM/CID, com medições periódicas, interpretação contínua e decisões formais registradas no [Registro de Medições e Decisões](../gestao/registro-medicoes.md) e consolidadas no [Painel de Medição PSM](../gestao/painel-psm.md).

## Referências

#### [1] {/* #ref-1 */}

ISO/IEC. *ISO/IEC 25040: Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Evaluation process.*

#### [2] {/* #ref-2 */}

BASILI, V. R.; CALDIERA, G.; ROMBACH, H. D. The Goal Question Metric Approach. In: *Encyclopedia of Software Engineering*. Wiley, 1994.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| `1.0` | 15/11/2026 | Página da metodologia da equipe, adaptada da seção removida do artigo | [Letícia Santos](https://github.com/LeticiaSantosss) | [Christopher Paraizo](https://github.com/wChrstphr) |
