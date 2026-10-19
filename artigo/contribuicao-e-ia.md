# Apêndices do Artigo: Contribuição Individual e Declaração de Uso de IA

Este documento reúne os conteúdos obrigatórios dos apêndices do artigo científico da **Entrega 1 (Fases 1 e 2)** da avaliação de qualidade do **Excalidraw**, atendendo rigorosamente à **Premissa 13** da especificação e aos critérios de avaliação **AG-C5** (Transparência da contribuição individual) e **F1-C10 / F2-C9** (Declaração de uso de IA).

Os conteúdos estão apresentados em formato legível (Markdown) e acompanhados dos respectivos trechos em código **LaTeX**, prontos para integração no modelo oficial da SBC (Issue #24).

---

## 1. Apêndice A: Declaração de Uso de Inteligência Artificial

### 1.1. Texto em Markdown

Em conformidade com a política institucional da disciplina (Critérios F1-C10 e F2-C9), a equipe declara que foram utilizadas ferramentas de inteligência artificial generativa durante o desenvolvimento deste trabalho:

* **Ferramentas Utilizadas:** Antigravity / Gemini 3.8 e Claude Code.
* **Consolidação por Pull Request e Tarefas Realizadas:**
  * **PR #5 (Setup do Repositório e Governança):** Utilização do Claude Code no apoio à formatação e adaptação do `CONTRIBUTING.md`, modelos de PR/Issue e mapa dos critérios de avaliação;
  * **PR #19 (Script de Métricas PSM/CID):** Utilização do Antigravity / Gemini 3.8 no apoio ao desenvolvimento do coletor em Python (`scripts/coleta_psm.py`), estruturação das fórmulas de cálculo das três categorias e implementação da renderização de gráficos em alta resolução com a biblioteca Pillow;
  * **PR #20 (Relatório PSM/CID da Fase 1):** Utilização do Antigravity / Gemini 3.8 na formatação estruturada dos três Measurement Constructs e organização inicial das tabelas de métricas em Markdown;
  * **PR atual (Apêndices do Artigo - Issue #27):** Utilização do Antigravity / Gemini 3.8 para formatação da tabela de contribuição individual e síntese da declaração em conformidade com as rubricas.
* **Metodologia de Conferência Crítica pela Equipe:**
  * Todo o código-fonte gerado foi testado e validado em ambiente local, sendo confrontado diretamente com os dados reais do repositório;
  * Os cálculos de esforço, custos e percentuais foram auditados contra os logs primários do GitHub, assegurando ausência de divergências ou alucinações de dados;
  * As formulações dos Measurement Constructs foram confrontadas com o modelo de informação do PSM/CID (ISO/IEC 15939) e com a especificação da disciplina;
  * O documento final não contém emojis, ícones decorativos ou figurinhas, mantendo o padrão formal acadêmico exigido pela rubrica.

### 1.2. Código LaTeX para o Artigo

```latex
\section*{Apêndice A: Declaração de Uso de Inteligência Artificial}
Em conformidade com a política institucional da disciplina (Critérios F1-C10 e F2-C9), a equipe declara que foram utilizadas ferramentas de inteligência artificial generativa durante o desenvolvimento deste trabalho:
\begin{itemize}
    \item \textbf{Ferramentas Utilizadas:} Antigravity / Gemini 3.8 e Claude Code.
    \item \textbf{Consolidação por Pull Request:} PR \#5 (Claude Code -- suporte à estruturação de diretrizes e modelos de governança); PR \#19 (Antigravity / Gemini 3.8 -- implementação do coletor em Python e renderização de gráficos com Pillow); PR \#20 (Antigravity / Gemini 3.8 -- estruturação formal dos três Measurement Constructs); PR da Issue \#27 (Antigravity / Gemini 3.8 -- formatação da tabela de contribuição individual e síntese de governança).
    \item \textbf{Metodologia de Conferência Crítica pela Equipe:} Todo o código-fonte, dados numéricos e conteúdos textuais foram integralmente revisados, validados e corrigidos pelos integrantes da equipe. Os cálculos de esforço foram confrontados diretamente com os logs primários do GitHub, assegurando ausência de alucinações e conformidade com a especificação da disciplina. Nenhuma imagem com texto sobreposto ou emoji foi mantida no documento final.
\end{itemize}
```

---

## 2. Apêndice B: Tabela de Contribuição Individual da Equipe

### 2.1. Metodologia de Coleta e Apuração

Conforme estabelecido nas Premissas 3 (Gestão do Projeto) e 5 (Rastreabilidade de Dados Primários), os dados que alimentam a Tabela de Contribuição foram extraídos de forma automatizada diretamente do repositório da equipe no GitHub (`dados/gestao/raw_github_data.json`).

O percentual de esforço individual foi calculado com base no total de horas reais registradas nas issues fechadas da Entrega 1. Quando uma issue contou com atuação conjunta de mais de um integrante, as horas foram individualizadas a partir da sintaxe de rateio padronizada no guia de contribuição (`Total (@usuario1: N, @usuario2: M)`).

### 2.2. Tabela de Contribuição da Entrega 1 (Fases 1 e 2)

| Integrante | Login GitHub | Subgrupo | Issues Atribuídas | Horas Est. (h) | Horas Reais (h) | Commits / PRs | Esforço Real (%) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Christopher | `@wChrstphr` | F2/F4 | 5 | 0,75 | 2,50 | 0 / 1 | 38,46% |
| Davi Pierre | `@DaviPierre` | F1/F3 | 6 | 0,00 | 0,00 | 1 / 1 | 0,00% |
| Gabriel Monteiro | `@GabrielSMonteiro` | F1/F3 | 6 | 0,00 | 0,00 | 9 / 1 | 0,00% |
| Letícia de Carvalho | `@LeticiaSantosss` | F1/F3 | 6 | 0,00 | 0,00 | 1 / 1 | 0,00% |
| Luiz Henrique Soares | `@luizh-gsoares` | F2/F4 | 6 | 0,00 | 0,00 | 0 / 0 | 0,00% |
| Maria Eduarda | `@eduarda-ogomes` | F2/F4 | 6 | 2,75 | 4,00 | 0 / 0 | 61,54% |
| **Total** | — | — | **35** | **3,50** | **6,50** | **11 / 4** | **100,00%** |

*Nota explicativa sobre os dados iniciais:* O esforço registrado até o momento reflete a entrega da infraestrutura de governança, setup do repositório (Issue #4) e o desenvolvimento do script de medição automatizada (Issue #19). Conforme os membros do Subgrupo F1/F3 concluírem e fecharem as issues técnicas da Fase 1 e o Subgrupo F2/F4 finalizar a especificação GQM da Fase 2, os dados serão atualizados cumulativamente pelo coletor até o fechamento da Release v1.0-E1 no dia 26/10/2026.

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
Christopher & 5 & 0.8h & 2.5h & 0/1 & 38.46\% \\
Davi Pierre & 6 & 0.0h & 0.0h & 1/1 & 0.00\% \\
Gabriel Monteiro & 6 & 0.0h & 0.0h & 9/1 & 0.00\% \\
Letícia de Carvalho & 6 & 0.0h & 0.0h & 1/1 & 0.00\% \\
Luiz Henrique Soares & 6 & 0.0h & 0.0h & 0/0 & 0.00\% \\
Maria Eduarda & 6 & 2.8h & 4.0h & 0/0 & 61.54\% \\
\hline
\textbf{Total} & \textbf{35} & \textbf{3.5h} & \textbf{6.5h} & \textbf{11/4} & \textbf{100.00\%} \\
\hline
\end{tabular}
\end{table}
```

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 0.1 | 18/10/2026 | Elaboração dos apêndices do artigo com tabela de contribuição individual e declaração de uso de IA | [Maria Eduarda](https://github.com/eduarda-ogomes) | [Luiz Henrique Soares](https://github.com/luizh-gsoares) |


