# Apêndices do Artigo: Contribuição Individual e Declaração de Uso de IA

Este documento reúne os conteúdos obrigatórios dos apêndices do artigo científico da **Entrega 1 (Fases 1 e 2)** da avaliação de qualidade do **Excalidraw**, atendendo rigorosamente à **Premissa 13** da especificação e aos critérios de avaliação **AG-C5** (Transparência da contribuição individual) e **F1-C10 / F2-C9** (Declaração de uso de IA).

Os conteúdos estão apresentados em formato legível (Markdown) e acompanhados dos respectivos trechos em código **LaTeX**, prontos para integração no modelo oficial da SBC (Issue #24).

---

## 1. Apêndice A: Declaração de Uso de Inteligência Artificial

### 1.1. Texto do artigo

A equipe utilizou IA generativa como apoio, com revisão humana antes de cada integração. O Claude Code foi usado no rascunho das abstraction sheets, questões e fichas GQM. O Antigravity, com Gemini 3.8 e Claude Sonnet 5.5, apoiou o script de coleta das métricas de gestão, a estruturação de seções do artigo e a formatação em LaTeX. O GitHub Copilot apoiou a edição das páginas do GitPages, do workflow de compilação e de trechos do artigo, e o Grammarly, a revisão ortográfica. Os integrantes conferiram citações, páginas e dados com as fontes e o repositório, e o registro por pull request está no repositório.

O texto acima está na seção "Declaração de Uso de Inteligência Artificial" de [`main.tex`](./main.tex).

### 1.2. Registro por pull request

Resumo da seção "Uso de IA" de cada pull request integrado. PRs que não declararam uso de IA ficam fora da tabela.

| PR | Ferramenta | Uso declarado |
| :---: | :--- | :--- |
| #5 | Claude Code | Guia de contribuição e modelos de issue e PR |
| #34 | Antigravity / Gemini | Script de coleta das métricas PSM/CID e gráficos |
| #35 | Antigravity / Gemini | Textos e tabelas dos Measurement Constructs da Fase 1 |
| #37 | Antigravity / Gemini | Tabela de contribuição e declaração de IA |
| #39 | Não informada | Revisão gramatical do propósito da avaliação |
| #40 | Grammarly | Correção ortográfica do documento de ODS |
| #41 | Antigravity / Gemini | Seção de histórico de versões do guia de contribuição |
| #42 | Grammarly e Gemini | Revisão do documento de interessados |
| #43 | Antigravity / Gemini 3.8 | Measurement Constructs e tabelas do relatório PSM/CID da Fase 2 |
| #46 | Gemini | Formatação da ata de reunião da Fase 1 |
| #47 | GitHub Copilot | Metadados e links do GitPages |
| #48 | GitHub Copilot | Workflow de LaTeX e arquivo temporário |
| #50 | Não informada | Referências cruzadas da visão geral da Fase 1 |
| #51 | Claude Code | Rascunho do método GQM e dos objetivos de medição |
| #58 | GitHub Copilot | Workflow de compilação e README do artigo |
| #60 | Claude Code | Rascunho das abstraction sheets e da ata da reunião GQM |
| #61 | GitHub Copilot | Visão geral da Fase 2 e referências cruzadas |
| #62 | Claude Code | Rascunho das questões e fichas do GQM G1 |
| #63 | GitHub Copilot | Card da página inicial e tabelas |
| #64 | Claude Code | Rascunho das questões e fichas do GQM G2 |
| #65 | Claude Code | Rascunho das questões e fichas do GQM G3 |
| #68 | Claude Code | Busca de artigos e regras de agregação e julgamento |
| #69 | Claude Code | Plano GQM e diagramas da hierarquia |
| #71 | GitHub Copilot | Tabela e referências cruzadas da visão geral da Fase 2 |
| #72 | Claude Code | Migração do artigo para o modelo SBC e redesenho das imagens |
| #79 | Antigravity (Gemini 3.8 e Claude Sonnet 5.5) | Correção do coletor PSM/CID, gráficos e tabelas |
| #80 | Antigravity / Gemini 3.8 | Seção de metodologia do artigo |
| #81 | Antigravity / Gemini 3.8 | Seção de pontuação e julgamento do artigo |
| #82 | Não informada | Organização e revisão do texto do G3 no artigo e formatação LaTeX |
| #83 | Antigravity | Ajuste da paginação em LaTeX |
| #84 | GitHub Copilot | Redação e adaptação do resumo do G1 para LaTeX |

Em todos os casos, o autor do PR declarou ter revisado o conteúdo gerado antes da integração.

## 2. Apêndice B: Tabela de Contribuição Individual da Equipe

### 2.1. Metodologia de Coleta e Apuração

Conforme estabelecido nas Premissas 3 (Gestão do Projeto) e 5 (Rastreabilidade de Dados Primários), os dados que alimentam a Tabela de Contribuição foram extraídos de forma automatizada diretamente do repositório da equipe no GitHub (`dados/gestao/raw_github_data.json`).

O percentual de esforço individual foi calculado com base no total de horas reais registradas nas issues das milestones Fase 1 e Fase 2. Quando uma issue contou com atuação conjunta de mais de um integrante, as horas foram individualizadas a partir da sintaxe de rateio padronizada no guia de contribuição (`Total (@usuario1: N, @usuario2: M)`).

### 2.2. Tabela de Contribuição da Entrega 1 (Fases 1 e 2)

| Integrante | Login GitHub | Subgrupo | Issues Atribuídas | Horas Est. (h) | Horas Reais (h) | Commits / PRs | Esforço Real (%) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Christopher | `@wChrstphr` | F2/F4 | 14 | 25,00 | 21,00 | 87 / 14 | 18,45% |
| Davi Pierre | `@DaviPierre` | F1/F3 | 6 | 20,00 | 21,00 | 5 / 2 | 18,45% |
| Gabriel Monteiro | `@GabrielSMonteiro` | F1/F3 | 7 | 27,00 | 28,00 | 37 / 6 | 24,60% |
| Letícia de Carvalho | `@LeticiaSantosss` | F1/F3 | 7 | 12,00 | 9,91 | 6 / 6 | 8,71% |
| Luiz Henrique Soares | `@luizh-gsoares` | F2/F4 | 7 | 12,00 | 12,40 | 21 / 8 | 10,90% |
| Maria Eduarda | `@eduarda-ogomes` | F2/F4 | 8 | 19,50 | 21,50 | 31 / 10 | 18,89% |
| **Total** | - | - | **49** | **115,50** | **113,81** | **187 / 46** | **100,00%** |

*Nota explicativa sobre os dados:* Os valores vêm da coleta de 05/11/2026 e somam as milestones Fase 1 e Fase 2, inclusive a [#28](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/28) e as correções [#88](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/88) e [#92](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/92), fechadas depois de 26/10. As issues compartilhadas contam para cada responsável. Commits e PRs cobrem o projeto inteiro até a data da coleta. Ainda faltam horas de [#26](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/26), [#27](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/27) e [#74](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/74) e a parte de Davi Pierre na [#23](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/23), então os percentuais podem mudar.

### 2.3. Código LaTeX para o Artigo

```latex
\section*{Apêndice B: Tabela de Contribuição Individual dos Integrantes}
Em atendimento à Premissa 13 da especificação e ao Critério AG-C5 da rubrica de avaliação, a Tabela \ref{tab:contribuicao} detalha a alocação de esforço de cada integrante da equipe ao final da primeira entrega, totalizando rigorosamente 100\% do trabalho executado.

\begin{table}[ht]
\centering
\caption{Tabela de contribuição individual da equipe (Entrega 1)}
\label{tab:contribuicao}
\begin{tabular}{lccccr}
\hline
\textbf{Integrante} & \textbf{Issues} & \textbf{Horas Est.} & \textbf{Horas Reais} & \textbf{Commits/PRs} & \textbf{Esforço (\%)} \\
\hline
Christopher & 14 & 25.0h & 21.0h & 87/14 & 18.45\% \\
Davi Pierre & 6 & 20.0h & 21.0h & 5/2 & 18.45\% \\
Gabriel Monteiro & 7 & 27.0h & 28.0h & 37/6 & 24.60\% \\
Letícia de Carvalho & 7 & 12.0h & 9.9h & 6/6 & 8.71\% \\
Luiz Henrique Soares & 7 & 12.0h & 12.4h & 21/8 & 10.90\% \\
Maria Eduarda & 8 & 19.5h & 21.5h & 31/10 & 18.89\% \\
\hline
\textbf{Total} & \textbf{49} & \textbf{115.5h} & \textbf{113.8h} & \textbf{187/46} & \textbf{100.00\%} \\
\hline
\end{tabular}
\end{table}
```

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 18/10/2026 | Elaboração dos apêndices do artigo com tabela de contribuição individual e declaração de uso de IA | [Maria Eduarda](https://github.com/eduarda-ogomes) | [Luiz Henrique Soares](https://github.com/luizh-gsoares) |
| 1.1 | 20/10/2026 | Atualização da tabela de contribuição pós-merge da main com avanço da Fase 2 (83,9h reais) | [Maria Eduarda](https://github.com/eduarda-ogomes) | - |
| 1.2 | 26/10/2026 | Declaração de IA reescrita conforme o artigo e registro de uso de IA por pull request até o PR #84 | [Christopher Paraizo](https://github.com/wChrstphr) | |
| 1.3 | 05/11/2026 | Tabela de contribuição atualizada com a coleta de 05/11 (113,81h reais nas Fases 1 e 2) | [Christopher Paraizo](https://github.com/wChrstphr) | |
