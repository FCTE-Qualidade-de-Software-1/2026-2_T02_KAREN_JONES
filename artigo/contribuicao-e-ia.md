# Apêndices do Artigo: Contribuição Individual e Declaração de Uso de IA

Este documento reúne os conteúdos obrigatórios dos apêndices do artigo científico da **Entrega 2 (Fases 1 a 4)** da avaliação de qualidade do **Excalidraw**, atendendo à **Premissa 13** da especificação e aos critérios de avaliação **AG-C5** (Transparência da contribuição individual) e **AG-C3** (Declaração de uso de IA).

Os conteúdos estão apresentados em formato legível (Markdown) e acompanhados dos respectivos trechos em código **LaTeX**, integrados no modelo oficial da SBC em [`main.tex`](./main.tex).

---

## 1. Apêndice A: Declaração de Uso de Inteligência Artificial

### 1.1. Texto do artigo

A equipe utilizou IA generativa exclusivamente como apoio técnico, com revisão humana antes de cada integração. O Claude Code foi utilizado no rascunho de abstraction sheets, questões e fichas GQM, scripts de análise e testes de coleta. O Google Antigravity, com Gemini 3.8 e Claude Sonnet 5.5, apoiou o script de coleta das métricas de gestão PSM/CID, a estruturação de seções do artigo em LaTeX e a navegação do GitPages. O GitHub Copilot apoiou a edição de páginas Markdown, workflows de CI/CD e rotinas de automação, e o Grammarly, a revisão ortográfica e de estilo. Os integrantes conferiram citações, páginas, dados empíricos e códigos com as fontes e o repositório, e o registro por PR está disponível no repositório.

O texto acima está na seção "Declaração de Uso de Inteligência Artificial" de [`main.tex`](./main.tex).

### 1.2. Registro por pull request

Resumo da seção "Uso de IA" de cada pull request integrado. PRs que não declararam uso de IA ficam fora da tabela.

| PR | Ferramenta | Uso declarado |
| :---: | :--- | :--- |
| #5 | Claude Code | Guia de contribuição e modelos de issue e PR. |
| #34 | Antigravity / Gemini | Script de coleta das métricas PSM/CID e gráficos. |
| #35 | Antigravity / Gemini | Textos e tabelas dos Measurement Constructs da Fase 1. |
| #37 | Antigravity / Gemini | Tabela de contribuição e declaração de IA. |
| #39 | Não informada | Revisão gramatical do propósito da avaliação. |
| #40 | Grammarly | Correção ortográfica do documento de ODS. |
| #41 | Antigravity / Gemini | Seção de histórico de versões do guia de contribuição. |
| #42 | Grammarly e Gemini | Revisão do documento de interessados. |
| #43 | Antigravity / Gemini 3.8 | Measurement Constructs e tabelas do relatório PSM/CID da Fase 2. |
| #46 | Gemini | Formatação da ata de reunião da Fase 1. |
| #47 | GitHub Copilot | Metadados e links do GitPages. |
| #48 | GitHub Copilot | Workflow de LaTeX e arquivo temporário. |
| #50 | Não informada | Referências cruzadas da visão geral da Fase 1. |
| #51 | Claude Code | Rascunho do método GQM e dos objetivos de medição. |
| #58 | GitHub Copilot | Workflow de compilação e README do artigo. |
| #60 | Claude Code | Rascunho das abstraction sheets e da ata da reunião GQM. |
| #61 | GitHub Copilot | Visão geral da Fase 2 e referências cruzadas. |
| #62 | Claude Code | Rascunho das questões e fichas do GQM G1. |
| #63 | GitHub Copilot | Card da página inicial e tabelas. |
| #64 | Claude Code | Rascunho das questões e fichas do GQM G2. |
| #65 | Claude Code | Rascunho das questões e fichas do GQM G3. |
| #68 | Claude Code | Busca de artigos e regras de agregação e julgamento. |
| #69 | Claude Code | Plano GQM e diagramas da hierarquia. |
| #71 | GitHub Copilot | Tabela e referências cruzadas da visão geral da Fase 2. |
| #72 | Claude Code | Migração do artigo para o modelo SBC e redesenho das imagens. |
| #79 | Antigravity (Gemini 3.8 e Claude Sonnet 5.5) | Correção do coletor PSM/CID, gráficos e tabelas. |
| #80 | Antigravity / Gemini 3.8 | Seção de metodologia do artigo. |
| #81 | Antigravity / Gemini 3.8 | Seção de pontuação e julgamento do artigo. |
| #82 | Não informada | Organização e revisão do texto do G3 no artigo e formatação LaTeX. |
| #83 | Antigravity | Ajuste da paginação em LaTeX. |
| #84 | GitHub Copilot | Redação e adaptação do resumo do G1 para LaTeX. |
| #159 | Claude | Conferência do documento de instruções com GQM e redação de correções. |
| #163 | Gemini | Verificação de conformidade das medições PSM com os dados do GitHub. |
| #166 | Claude Sonnet 4.6 | Estruturação das seções no formato SBC. |
| #168 | Claude Code | Revisão do script de coleta de métricas da Fase 4. |
| #169 | Claude Code | Revisão e melhoria do script de cálculo de métricas de G1. |
| #171 | Claude | Rascunho das atas de reunião no modelo padronizado. |
| #172 | Claude | Conversão de conteúdo de metodologia e criação de âncoras para o GitPages. |
| #173 | Claude Code | Escrita do script de análise e do rascunho de resultados de G1. |
| #175 | Claude Code | Redação e fusão das páginas de resultados de G3. |
| #177 | Gemini | Formatação de tabelas e ajuste de espaço em LaTeX para o plano de avaliação. |
| #184 | Antigravity | Apoio na edição dos arquivos de navegação da Fase 4 e validação de build. |
| #185 | Antigravity / Gemini | Redação acadêmica de parágrafos contínuos e tabelas de resultados no artigo. |
| #187 | Claude Code | Verificação da documentação oficial de desenvolvimento do Excalidraw. |
| #188 | Claude Code | Apoio na coleta automatizada de M2.3.1 com Playwright. |
| #189 | Antigravity | Estruturação de dados das tabelas e revisão estilística do painel PSM. |

Em todos os casos, o autor do PR declarou ter revisado o conteúdo gerado antes da integração.

## 2. Apêndice B: Tabela de Contribuição Individual da Equipe

### 2.1. Metodologia de Coleta e Apuração

Conforme estabelecido nas Premissas 3 (Gestão do Projeto) e 5 (Rastreabilidade de Dados Primários), os dados que alimentam a Tabela de Contribuição foram extraídos de forma automatizada diretamente do repositório da equipe no GitHub (`dados/gestao/raw_github_data.json` e `dados/gestao/04_contribuicao_individual.csv`).

O percentual de esforço individual foi calculado com base no total de horas reais registradas nas issues ao longo de todas as quatro fases do projeto (Fases 1, 2, 3 e 4). Quando uma issue contou com atuação conjunta de mais de um integrante, as horas foram individualizadas a partir da sintaxe de rateio padronizada no guia de contribuição (`Total (@usuario1: N, @usuario2: M)`).

### 2.2. Tabela de Contribuição Consolidada do Projeto (Fases 1 a 4)

| Integrante | Login GitHub | Subgrupo | Issues Atribuídas | Horas Est. (h) | Horas Reais (h) | Commits / PRs | Esforço Real (%) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Christopher | `@wChrstphr` | F2/F4 | 29 | 75,50 | 52,65 | 169 / 28 | 19,97% |
| Davi Pierre | `@DaviPierre` | F1/F3 | 14 | 38,00 | 37,00 | 13 / 6 | 14,03% |
| Gabriel Monteiro | `@GabrielSMonteiro` | F1/F3 | 18 | 49,50 | 57,00 | 69 / 16 | 21,62% |
| Letícia de Carvalho | `@LeticiaSantosss` | F1/F3 | 16 | 27,00 | 29,91 | 16 / 11 | 11,34% |
| Luiz Henrique Soares | `@luizh-gsoares` | F2/F4 | 15 | 32,00 | 32,90 | 38 / 16 | 12,48% |
| Maria Eduarda | `@eduarda-ogomes` | F2/F4 | 22 | 52,00 | 54,20 | 83 / 17 | 20,56% |
| **Total** | - | - | **114** | **274,00** | **263,66** | **388 / 94** | **100,00%** |

*Nota explicativa sobre os dados:* Os valores decorrem da coleta oficial de dados com corte em 20/11/2026 e consolidam todo o ciclo de vida do projeto (Fases 1 a 4), totalizando 98 issues únicas (114 atribuições em razão de tarefas compartilhadas). As tarefas conjuntas contam o rateio proporcional de cada responsável. Todos os seis integrantes mantiveram-se dentro da faixa de equilíbrio de esforço entre 8% e 30% estipulada nas diretrizes de gestão.

### 2.3. Código LaTeX para o Artigo

```latex
\section{Tabela de Contribuição dos Membros da Equipe}
Em atendimento à Premissa 13 da especificação e ao Critério AG-C5 da disciplina, a Tabela~\ref{tab:contribuicao} apresenta o esforço e a participação percentual individual dos integrantes ao longo das quatro fases do projeto. O percentual foi calculado pela razão entre as horas reais de cada integrante e o total de 263,7\,h apuradas nas \textit{issues} de desenvolvimento (corte de dados em 20/11/2026), totalizando 100,00\% do trabalho executado.

\begin{table}[!ht]
\centering
\caption{Tabela de contribuição individual da equipe}
\label{tab:contribuicao}
\vspace{2pt}
\footnotesize
\renewcommand{\arraystretch}{0.85}
\begin{tabular}{lccccr}
\toprule
\textbf{Integrante} & \textbf{Issues} & \textbf{Horas Est.} & \textbf{Horas Reais} & \textbf{Commits/PRs} & \textbf{Esforço (\%)} \\
\midrule
Christopher          & 29 & 75.5h & 52.6h & 169/28 & 19.97\% \\
Davi Pierre          & 14 & 38.0h & 37.0h & 13/6   & 14.03\% \\
Gabriel Monteiro     & 18 & 49.5h & 57.0h & 69/16  & 21.62\% \\
Letícia de Carvalho  & 16 & 27.0h & 29.9h & 16/11  & 11.34\% \\
Luiz Henrique Soares & 15 & 32.0h & 32.9h & 38/16  & 12.48\% \\
Maria Eduarda        & 22 & 52.0h & 54.2h & 83/17  & 20.56\% \\
\midrule
\textbf{Total}       & \textbf{114} & \textbf{274.0h} & \textbf{263.7h} & \textbf{388/94} & \textbf{100.00\%} \\
\bottomrule
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
| 1.3 | 05/11/2026 | Tabela de contribuição atualizada com a coleta de 05/11 (114,31h reais nas Fases 1 e 2) | [Christopher Paraizo](https://github.com/wChrstphr) | |
| 1.4 | 20/11/2026 | Atualização definitiva da tabela de contribuição consolidada das quatro fases (263,66h reais) e declaração de IA final da Entrega 2 | [Maria Eduarda](https://github.com/eduarda-ogomes) | |
