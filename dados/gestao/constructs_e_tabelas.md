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
| Fase 1 | 17 / 17 | 100.0% | 29.4% | 55.2 | 62.2 | R$ 2486.25 | R$ 2797.20 | 112.5% | 1.23 |
| Fase 2 | 18 / 6 | 33.3% | 88.9% | 28.0 | 18.5 | R$ 1260.00 | R$ 832.50 | 66.1% | 1.44 |

---

## 3. Tabela de Contribuicao Individual (Markdown e LaTeX para #27)

| Integrante | GitHub | Issues Atribuidas | Horas Estimadas (h) | Horas Reais (h) | Custo Equivalente (R$) | Commits | PRs | Contribuicao (%) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Christopher | `@wChrstphr` | 11 | 9.0 | 7.0 | R$ 315.00 | 21 | 5 | **8.68%** |
| Davi Pierre | `@DaviPierre` | 6 | 18.0 | 19.0 | R$ 855.00 | 5 | 2 | **23.56%** |
| Gabriel Monteiro | `@GabrielSMonteiro` | 6 | 27.0 | 28.0 | R$ 1260.00 | 29 | 5 | **34.71%** |
| Leticia de Carvalho | `@LeticiaSantosss` | 6 | 8.5 | 5.9 | R$ 265.95 | 5 | 5 | **7.33%** |
| Luiz Henrique Soares | `@luizh-gsoares` | 6 | 3.2 | 2.2 | R$ 101.25 | 8 | 5 | **2.79%** |
| Maria Eduarda | `@eduarda-ogomes` | 6 | 17.5 | 18.5 | R$ 832.50 | 14 | 5 | **22.94%** |

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
Christopher & 11 & 9.0h & 7.0h & 21/5 & 8.68\% \\
Davi Pierre & 6 & 18.0h & 19.0h & 5/2 & 23.56\% \\
Gabriel Monteiro & 6 & 27.0h & 28.0h & 29/5 & 34.71\% \\
Leticia de Carvalho & 6 & 8.5h & 5.9h & 5/5 & 7.33\% \\
Luiz Henrique Soares & 6 & 3.2h & 2.2h & 8/5 & 2.79\% \\
Maria Eduarda & 6 & 17.5h & 18.5h & 14/5 & 22.94\% \\
\hline
\textbf{Total} & \textbf{41} & \textbf{83.2h} & \textbf{80.7h} & \textbf{82/27} & \textbf{100.00\%} \\
\hline
\end{tabular}
\end{table}
```
