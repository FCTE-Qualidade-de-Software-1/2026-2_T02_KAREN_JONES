# Indicadores PSM/CID e Measurement Constructs

- **Valor-hora de referencia:** R$ 45.00
- **Fonte do valor-hora:** Remuneracao media nacional para Analista de Sistemas / Engenheiro de Software Junior sob regime CLT (CBO 2124-05, Fonte: Novo CAGED / MTE, base 160h mensais)

---

## 1. Measurement Constructs (Padrao PSM/CID)

### Construct 1 — Recursos e Custos: Esforco e Custo do Projeto

| Elemento do Construct | Especificacao |
| :--- | :--- |
| **Categoria de Informacao** | Recursos e Custos (*Resources and Cost*) |
| **Necessidade de Informacao** | Avaliar se o esforco empregado pela equipe e o custo financeiro estimado permanecem dentro do planejado e se a carga de trabalho esta equilibrada entre os integrantes. |
| **Conceito Mensuravel** | Esforco de desenvolvimento, custo financeiro equivalente e distribuicao individual de trabalho. |
| **Medidas Base** | 1. `Horas Estimadas (h)`: valor registrado na abertura de cada issue.<br>2. `Horas Reais (h)`: valor apurado no fechamento da issue por integrante.<br>3. `Valor-Hora (R$)`: taxa horaria de referencia configurada em `scripts/config.json`. |
| **Medidas Derivadas** | • $\text{Custo Planejado (R\$)} = \sum \text{Horas Estimadas} \times \text{Valor-Hora}$<br>• $\text{Custo Real (R\$)} = \sum \text{Horas Reais} \times \text{Valor-Hora}$<br>• $\text{Contribuicao Individual (\%)} = (\text{Esforco do Integrante} / \text{Esforco Total da Equipe}) \times 100$ |
| **Indicador e Criterio de Decisao** | Comparacao entre horas planejadas e reais por fase e percentual individual. Desvios superiores a 25% entre planejado e realizado ou desequilibrio acentuado entre membros exigem redistribuicao de tarefas na fase seguinte. |

### Construct 2 — Calendario e Progresso: Taxa de Conclusao e Aderencia a Prazos

| Elemento do Construct | Especificacao |
| :--- | :--- |
| **Categoria de Informacao** | Calendario e Progresso (*Schedule and Progress*) |
| **Necessidade de Informacao** | Monitorar o ritmo de entrega dos artefatos de cada fase (milestone) e identificar atrasos em relacao aos prazos internos antes da submissao oficial. |
| **Conceito Mensuravel** | Progresso de conclusao de marcos (*Milestone Completion*) e pontualidade das entregas. |
| **Medidas Base** | 1. `Total de Issues da Fase`: contagem de tarefas vinculadas a milestone.<br>2. `Issues Concluidas`: contagem de tarefas com estado `closed`.<br>3. `Data Limite (Prazo)` vs. `Data de Fechamento (closed_at)`. |
| **Medidas Derivadas** | • $\text{Progresso da Fase (\%)} = (\text{Issues Concluidas} / \text{Total de Issues}) \times 100$<br>• $\text{Aderencia ao Prazo (\%)} = (\text{Issues no Prazo} / \text{Total de Issues}) \times 100$ |
| **Indicador e Criterio de Decisao** | Percentual de conclusao e entregas no prazo. Caso a aderencia ao prazo fique abaixo de 80%, a equipe deve antecipar revisoes de PR e desmembrar tarefas complexas. |

### Construct 3 — Desempenho dos Processos: Acuracia de Estimativa e Tempo de Ciclo

| Elemento do Construct | Especificacao |
| :--- | :--- |
| **Categoria de Informacao** | Desempenho dos Processos (*Process Performance*) |
| **Necessidade de Informacao** | Verificar a maturidade do processo de planejamento da equipe (qualidade das estimativas) e a agilidade do fluxo de revisao e fechamento de tarefas. |
| **Conceito Mensuravel** | Acuracia de estimativa (*Estimation Accuracy*), governanca de preenchimento e *Lead Time* de resolucao. |
| **Medidas Base** | 1. `Data de Criacao (created_at)` e `Data de Fechamento (closed_at)` das issues.<br>2. `Horas Estimadas` e `Horas Reais` por tarefa. |
| **Medidas Derivadas** | • $\text{Acuracia de Estimativa (\%)} = (\text{Horas Reais} / \text{Horas Estimadas}) \times 100$<br>• $\text{Lead Time Medio (dias)} = \frac{1}{N} \sum (\text{closed\_at} - \text{created\_at})$<br>• $\text{Taxa de Governanca (\%)} = (\text{Issues com Estimativa Preenchida} / \text{Total de Issues}) \times 100$ |
| **Indicador e Criterio de Decisao** | Acuracia ideal entre 80% e 120%. Valores fora dessa faixa indicam subestimacao ou superestimacao sistematica, orientando o ajuste das estimativas nas fases posteriores. |

---

## 2. Resumo Consolidado por Fase (Tabelas para #20 e #31)

| Fase | Issues (Total / Concluidas) | Progresso (%) | Aderencia ao Prazo (%) | Horas Estimadas (h) | Horas Reais (h) | Custo Estimado (R$) | Custo Real (R$) | Acuracia Estimativa (%) | Lead Time Medio (dias) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Fase 1 | 17 / 17 | 100.0% | 29.4% | 53.5 | 57.9 | R$ 2407.50 | R$ 2605.95 | 108.2% | 1.23 |
| Fase 2 | 26 / 24 | 92.3% | 46.2% | 59.0 | 50.9 | R$ 2655.00 | R$ 2290.50 | 86.3% | 2.67 |
| Fase 3 | 3 / 0 | 0.0% | 100.0% | 5.0 | 0.0 | R$ 225.00 | R$ 0.00 | 0.0% | 0.00 |

---

## 3. Tabela de Contribuicao Individual (Markdown e LaTeX para #27)

| Integrante | GitHub | Issues Atribuidas | Horas Estimadas (h) | Horas Reais (h) | Custo Equivalente (R$) | Commits | PRs | Contribuicao (%) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Christopher | `@wChrstphr` | 10 | 17.0 | 14.5 | R$ 652.50 | 85 | 12 | **13.33%** |
| Davi Pierre | `@DaviPierre` | 7 | 22.0 | 22.5 | R$ 1012.50 | 5 | 2 | **20.68%** |
| Gabriel Monteiro | `@GabrielSMonteiro` | 7 | 27.0 | 28.0 | R$ 1260.00 | 34 | 6 | **25.73%** |
| Leticia de Carvalho | `@LeticiaSantosss` | 7 | 12.0 | 9.9 | R$ 445.95 | 6 | 6 | **9.11%** |
| Luiz Henrique Soares | `@luizh-gsoares` | 7 | 12.0 | 12.4 | R$ 558.00 | 21 | 8 | **11.40%** |
| Maria Eduarda | `@eduarda-ogomes` | 8 | 19.5 | 21.5 | R$ 967.50 | 28 | 8 | **19.76%** |

### Codigo LaTeX para o Apendice do Artigo (#27)

```latex
\begin{table}[ht]
\centering
\caption{Tabela de contribuicao individual da equipe (Entrega 1)}
\label{tab:contribuicao}
\begin{tabular}{lccccr}
\hline
\textbf{Integrante} & \textbf{Issues} & \textbf{Horas Est.} & \textbf{Horas Reais} & \textbf{Commits/PRs} & \textbf{Esfor\c{c}o (\%)} \\
\hline
Christopher & 10 & 17.0h & 14.5h & 85/12 & 13.33\% \\
Davi Pierre & 7 & 22.0h & 22.5h & 5/2 & 20.68\% \\
Gabriel Monteiro & 7 & 27.0h & 28.0h & 34/6 & 25.73\% \\
Leticia de Carvalho & 7 & 12.0h & 9.9h & 6/6 & 9.11\% \\
Luiz Henrique Soares & 7 & 12.0h & 12.4h & 21/8 & 11.40\% \\
Maria Eduarda & 8 & 19.5h & 21.5h & 28/8 & 19.76\% \\
\hline
\textbf{Total} & \textbf{46} & \textbf{109.5h} & \textbf{108.8h} & \textbf{179/42} & \textbf{100.00\%} \\
\hline
\end{tabular}
\end{table}
```
