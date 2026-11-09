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
| Fase 2 | 27 / 27 | 100.0% | 44.4% | 62.5 | 56.4 | R$ 2812.50 | R$ 2538.00 | 90.2% | 3.97 |
| Fase 3 | 23 / 11 | 47.8% | 8.7% | 48.0 | 31.5 | R$ 2160.00 | R$ 1417.50 | 121.2% | 4.98 |
| Fase 4 | 24 / 0 | 0.0% | 91.7% | 80.0 | 0.0 | R$ 3600.00 | R$ 0.00 | 0.0% | 0.00 |
| Sem Fase | 1 / 1 | 100.0% | 100.0% | 2.0 | 2.0 | R$ 90.00 | R$ 90.00 | 100.0% | 0.01 |

---

## 3. Tabela de Contribuicao Individual (Markdown e LaTeX para #27)

| Integrante | GitHub | Issues Atribuidas | Horas Estimadas (h) | Horas Reais (h) | Custo Equivalente (R$) | Commits | PRs | Contribuicao (%) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Christopher | `@wChrstphr` | 23 | 52.5 | 24.0 | R$ 1080.00 | 101 | 17 | **16.24%** |
| Davi Pierre | `@DaviPierre` | 13 | 37.0 | 34.0 | R$ 1530.00 | 6 | 5 | **23.00%** |
| Gabriel Monteiro | `@GabrielSMonteiro` | 16 | 44.5 | 38.5 | R$ 1732.50 | 48 | 9 | **26.05%** |
| Leticia de Carvalho | `@LeticiaSantosss` | 16 | 30.5 | 11.4 | R$ 513.45 | 9 | 7 | **7.72%** |
| Luiz Henrique Soares | `@luizh-gsoares` | 15 | 35.0 | 12.4 | R$ 558.00 | 21 | 8 | **8.39%** |
| Maria Eduarda | `@eduarda-ogomes` | 19 | 46.5 | 27.5 | R$ 1237.50 | 42 | 11 | **18.60%** |

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
Christopher & 23 & 52.5h & 24.0h & 101/17 & 16.24\% \\
Davi Pierre & 13 & 37.0h & 34.0h & 6/5 & 23.00\% \\
Gabriel Monteiro & 16 & 44.5h & 38.5h & 48/9 & 26.05\% \\
Leticia de Carvalho & 16 & 30.5h & 11.4h & 9/7 & 7.72\% \\
Luiz Henrique Soares & 15 & 35.0h & 12.4h & 21/8 & 8.39\% \\
Maria Eduarda & 19 & 46.5h & 27.5h & 42/11 & 18.60\% \\
\hline
\textbf{Total} & \textbf{102} & \textbf{246.0h} & \textbf{147.8h} & \textbf{227/57} & \textbf{100.00\%} \\
\hline
\end{tabular}
\end{table}
```


---

## 4. Medidas do Plano de Medicao

### Ritmo de fechamento das issues

| Fase | Inicio | Data media | Fim | Fechadas / Total | Fechadas ate a data media (%) | Fechadas nos 2 ultimos dias | Fechadas apos o fim | Fechadas no prazo (%) | Bloqueadas | Alerta de ritmo |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Fase 1 | 28/09/2026 00:00 | 08/10/2026 11:59 | 18/10/2026 23:59 | 17 / 17 | 0.0 | 13 | 4 | 23.5 | - | sim |
| Fase 2 | 18/10/2026 23:59 | 22/10/2026 23:59 | 26/10/2026 23:59 | 27 / 27 | 59.3 | 8 | 3 | 40.7 | - | nao |
| Fase 3 | 26/10/2026 23:59 | 02/11/2026 11:59 | 08/11/2026 23:59 | 11 / 23 | 0.0 | 7 | 2 | 8.7 | #95 #98 #99 #103 #104 #105 #107 | sim |
| Fase 4 | 08/11/2026 23:59 | 15/11/2026 11:59 | 21/11/2026 23:59 | 0 / 24 | 0.0 | 0 | 0 | 0.0 | #108 #109 #110 #111 #112 #113 #114 #115 #116 #117 #118 #119 #120 #121 #122 #123 #124 #125 #126 #127 #128 #130 | nao |

### Acerto das estimativas por issue

Desvio = (horas reais - horas estimadas) / horas estimadas. Na faixa = desvio entre -20% e +20%. O desvio de cada issue esta em `05_detalhamento_issues.csv`.

| Fase | Issues avaliadas | Desvio da fase (%) | Desvio mediano (%) | Na faixa (%) | Subestimadas | Superestimadas |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Fase 1 | 17 | 8.2 | 0.0 | 52.9 | 4 | 4 |
| Fase 2 | 24 | -9.8 | -13.8 | 58.3 | 3 | 7 |
| Fase 3 | 12 | 21.2 | 0.0 | 50.0 | 5 | 1 |
| Sem Fase | 1 | 0.0 | 0.0 | 100.0 | 0 | 0 |

### Tempo de espera dos PRs por revisao

Horas corridas entre a abertura do PR e a primeira revisao de outra pessoa.

| Fase | PRs | Integrados | Integrados com aprovacao | Revisao formal (%) | Sem revisao | Media (h) | Mediana (h) | P80 (h) | P90 (h) | Acima de 24h |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Fase 1 | 16 | 16 | 7 | 43.8 | 9 | 12.45 | 10.71 | 22.08 | 40.59 | 1 |
| Fase 2 | 27 | 25 | 11 | 44.0 | 16 | 1.91 | 0.4 | 2.86 | 7.53 | 0 |
| Fase 3 | 14 | 12 | 9 | 75.0 | 4 | 23.1 | 23.59 | 45.9 | 46.19 | 4 |
| Total | 57 | 53 | 27 | 50.9 | 29 | 12.11 | 1.69 | 23.68 | 45.9 | 5 |

### Quem revisou

| Fase | Revisor | PRs revisados | Participacao (%) |
| :--- | :---: | :---: | :---: |
| Fase 1 | eduarda-ogomes | 4 | 57.1 |
| Fase 1 | luizh-gsoares | 2 | 28.6 |
| Fase 1 | GabrielSMonteiro | 1 | 14.3 |
| Fase 2 | luizh-gsoares | 7 | 63.6 |
| Fase 2 | wChrstphr | 4 | 36.4 |
| Fase 3 | eduarda-ogomes | 6 | 60.0 |
| Fase 3 | wChrstphr | 3 | 30.0 |
| Fase 3 | luizh-gsoares | 1 | 10.0 |
| Total | luizh-gsoares | 10 | 35.7 |
| Total | eduarda-ogomes | 10 | 35.7 |
| Total | wChrstphr | 7 | 25.0 |
| Total | GabrielSMonteiro | 1 | 3.6 |

### Autor por revisor

| Fase | Autor | Revisor | PRs |
| :--- | :---: | :---: | :---: |
| Fase 1 | DaviPierre | eduarda-ogomes | 1 |
| Fase 1 | GabrielSMonteiro | eduarda-ogomes | 2 |
| Fase 1 | LeticiaSantosss | GabrielSMonteiro | 1 |
| Fase 1 | eduarda-ogomes | luizh-gsoares | 2 |
| Fase 1 | wChrstphr | eduarda-ogomes | 1 |
| Fase 2 | GabrielSMonteiro | wChrstphr | 1 |
| Fase 2 | eduarda-ogomes | luizh-gsoares | 1 |
| Fase 2 | luizh-gsoares | wChrstphr | 3 |
| Fase 2 | wChrstphr | luizh-gsoares | 6 |
| Fase 3 | DaviPierre | wChrstphr | 1 |
| Fase 3 | GabrielSMonteiro | eduarda-ogomes | 3 |
| Fase 3 | eduarda-ogomes | wChrstphr | 2 |
| Fase 3 | wChrstphr | eduarda-ogomes | 3 |
| Fase 3 | wChrstphr | luizh-gsoares | 1 |
| Total | DaviPierre | eduarda-ogomes | 1 |
| Total | DaviPierre | wChrstphr | 1 |
| Total | GabrielSMonteiro | eduarda-ogomes | 5 |
| Total | GabrielSMonteiro | wChrstphr | 1 |
| Total | LeticiaSantosss | GabrielSMonteiro | 1 |
| Total | eduarda-ogomes | luizh-gsoares | 3 |
| Total | eduarda-ogomes | wChrstphr | 2 |
| Total | luizh-gsoares | wChrstphr | 3 |
| Total | wChrstphr | eduarda-ogomes | 4 |
| Total | wChrstphr | luizh-gsoares | 7 |

### PRs

| PR | Fase | Origem da fase | Autor | Situacao | Aberto em | Primeira revisao | Espera (h) | Aprovado | Revisores |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| #150 | Fase 3 | issue #101 | wChrstphr | integrado | 08/11/2026 23:48 | 09/11/2026 00:09 | 0.35 | sim | luizh-gsoares |
| #149 | Fase 3 | issue #95 | DaviPierre | aberto | 08/11/2026 23:41 | 09/11/2026 00:58 | 1.28 | nao | wChrstphr |
| #148 | Fase 3 | titulo | DaviPierre | aberto | 08/11/2026 22:42 | - | - | nao | - |
| #147 | Fase 3 | issue #97 | GabrielSMonteiro | integrado | 08/11/2026 19:30 | 08/11/2026 21:36 | 2.1 | sim | eduarda-ogomes |
| #146 | Fase 3 | issue #100 | GabrielSMonteiro | integrado | 07/11/2026 21:52 | 08/11/2026 21:22 | 23.5 | sim | eduarda-ogomes |
| #145 | Fase 3 | issue #86 | GabrielSMonteiro | integrado | 07/11/2026 21:33 | 08/11/2026 21:14 | 23.68 | sim | eduarda-ogomes |
| #144 | Fase 3 | issue #134 | eduarda-ogomes | integrado | 07/11/2026 19:55 | 08/11/2026 22:04 | 26.16 | sim | wChrstphr |
| #143 | Fase 3 | issue #102 | LeticiaSantosss | integrado | 06/11/2026 15:51 | - | - | nao | - |
| #142 | Fase 3 | issue #87 | DaviPierre | integrado | 05/11/2026 18:16 | - | - | nao | - |
| #141 | Fase 3 | issue #140 | wChrstphr | integrado | 05/11/2026 16:37 | 07/11/2026 14:31 | 45.9 | sim | eduarda-ogomes |
| #139 | Fase 3 | issue #138 | wChrstphr | integrado | 05/11/2026 16:15 | 07/11/2026 14:26 | 46.19 | sim | eduarda-ogomes |
| #137 | Fase 3 | issue #136 | wChrstphr | integrado | 05/11/2026 00:36 | 07/11/2026 14:21 | 61.74 | sim | eduarda-ogomes |
| #132 | Fase 3 | issue #131 | eduarda-ogomes | integrado | 04/11/2026 13:11 | - | - | nao | - |
| #93 | Fase 2 | issue #92 | wChrstphr | integrado | 30/10/2026 14:14 | - | - | nao | - |
| #91 | Fase 3 | data | eduarda-ogomes | integrado | 28/10/2026 17:16 | 28/10/2026 17:23 | 0.11 | sim | wChrstphr |
| #89 | Fase 2 | issue #88 | wChrstphr | integrado | 26/10/2026 20:40 | 26/10/2026 20:47 | 0.12 | sim | luizh-gsoares |
| #84 | Fase 2 | issue #75 | luizh-gsoares | integrado | 26/10/2026 19:56 | 26/10/2026 20:10 | 0.24 | sim | wChrstphr |
| #83 | Fase 2 | issue #74 | GabrielSMonteiro | integrado | 26/10/2026 11:08 | 26/10/2026 18:40 | 7.53 | sim | wChrstphr |
| #82 | Fase 2 | issue #77 | LeticiaSantosss | integrado | 25/10/2026 20:00 | - | - | nao | - |
| #81 | Fase 2 | issue #78 | eduarda-ogomes | integrado | 25/10/2026 01:21 | - | - | nao | - |
| #80 | Fase 2 | issue #73 | eduarda-ogomes | integrado | 25/10/2026 01:20 | - | - | nao | - |
| #79 | Fase 2 | data | eduarda-ogomes | integrado | 20/10/2026 20:58 | - | - | nao | - |
| #72 | Fase 2 | issue #24 | wChrstphr | integrado | 20/10/2026 14:07 | - | - | nao | - |
| #71 | Fase 2 | issue #70 | luizh-gsoares | integrado | 20/10/2026 13:41 | - | - | nao | - |
| #69 | Fase 2 | issue #57 | wChrstphr | integrado | 19/10/2026 21:12 | - | - | nao | - |
| #68 | Fase 2 | issue #56 | wChrstphr | integrado | 19/10/2026 20:49 | - | - | nao | - |
| #67 | Fase 2 | issue #56 | wChrstphr | fechado sem merge | 19/10/2026 20:46 | - | - | nao | - |
| #66 | Fase 2 | issue #56 | luizh-gsoares | fechado sem merge | 19/10/2026 15:06 | - | - | nao | - |
| #65 | Fase 2 | issue #55 | wChrstphr | integrado | 19/10/2026 13:10 | 19/10/2026 13:20 | 0.16 | sim | luizh-gsoares |
| #64 | Fase 2 | issue #54 | wChrstphr | integrado | 19/10/2026 13:04 | 19/10/2026 13:27 | 0.37 | sim | luizh-gsoares |
| #63 | Fase 2 | issue #29 | luizh-gsoares | integrado | 19/10/2026 12:50 | 19/10/2026 20:24 | 7.57 | sim | wChrstphr |
| #62 | Fase 2 | issue #53 | wChrstphr | integrado | 19/10/2026 12:45 | 19/10/2026 13:27 | 0.7 | sim | luizh-gsoares |
| #61 | Fase 2 | issue #29 | luizh-gsoares | integrado | 19/10/2026 12:05 | 19/10/2026 12:48 | 0.73 | sim | wChrstphr |
| #60 | Fase 2 | issue #52 | wChrstphr | integrado | 19/10/2026 11:57 | 19/10/2026 12:19 | 0.37 | sim | luizh-gsoares |
| #59 | Fase 2 | issue #22 | wChrstphr | integrado | 19/10/2026 11:52 | - | - | nao | - |
| #58 | Fase 2 | issue #33 | luizh-gsoares | integrado | 19/10/2026 11:49 | - | - | nao | - |
| #51 | Fase 2 | issue #22 | wChrstphr | integrado | 19/10/2026 10:50 | 19/10/2026 11:14 | 0.4 | sim | luizh-gsoares |
| #50 | Fase 1 | issue #18 | LeticiaSantosss | integrado | 19/10/2026 09:24 | - | - | nao | - |
| #49 | Fase 2 | issue #25 | GabrielSMonteiro | integrado | 19/10/2026 03:05 | - | - | nao | - |
| #48 | Fase 2 | issue #33 | luizh-gsoares | integrado | 19/10/2026 00:17 | - | - | nao | - |
| #47 | Fase 1 | issue #17 | luizh-gsoares | integrado | 18/10/2026 23:59 | - | - | nao | - |
| #46 | Fase 1 | issue #21 | LeticiaSantosss | integrado | 18/10/2026 23:45 | - | - | nao | - |
| #45 | Fase 1 | issue #10 | DaviPierre | integrado | 18/10/2026 23:30 | - | - | nao | - |
| #44 | Fase 1 | titulo | LeticiaSantosss | integrado | 18/10/2026 22:42 | - | - | nao | - |
| #43 | Fase 2 | issue #31 | eduarda-ogomes | integrado | 18/10/2026 21:45 | - | - | nao | - |
| #42 | Fase 1 | issue #15 | GabrielSMonteiro | integrado | 18/10/2026 21:11 | - | - | nao | - |
| #41 | Fase 1 | corpo | eduarda-ogomes | integrado | 18/10/2026 21:09 | - | - | nao | - |
| #40 | Fase 1 | issue #14 | GabrielSMonteiro | integrado | 18/10/2026 20:53 | 18/10/2026 22:09 | 1.26 | sim | eduarda-ogomes |
| #39 | Fase 1 | issue #9 | GabrielSMonteiro | integrado | 18/10/2026 20:34 | 18/10/2026 21:22 | 0.79 | sim | eduarda-ogomes |
| #38 | Fase 1 | data | LeticiaSantosss | integrado | 18/10/2026 20:03 | - | - | nao | - |
| #37 | Fase 2 | issue #27 | eduarda-ogomes | integrado | 18/10/2026 16:15 | 18/10/2026 19:07 | 2.86 | sim | luizh-gsoares |
| #35 | Fase 1 | issue #20 | eduarda-ogomes | integrado | 18/10/2026 08:24 | 18/10/2026 19:06 | 10.71 | sim | luizh-gsoares |
| #34 | Fase 1 | issue #19 | eduarda-ogomes | integrado | 17/10/2026 21:01 | 18/10/2026 19:06 | 22.08 | sim | luizh-gsoares |
| #5 | Fase 1 | issue #4 | wChrstphr | integrado | 17/10/2026 11:26 | 17/10/2026 12:13 | 0.78 | sim | eduarda-ogomes |
| #3 | Fase 1 | data | LeticiaSantosss | integrado | 15/10/2026 18:46 | 17/10/2026 11:22 | 40.59 | sim | GabrielSMonteiro |
| #2 | Fase 1 | data | GabrielSMonteiro | integrado | 15/10/2026 13:42 | - | - | nao | - |
| #1 | Fase 1 | data | DaviPierre | integrado | 14/10/2026 21:49 | 15/10/2026 08:45 | 10.93 | sim | eduarda-ogomes |

### Avisos da coleta

| Tipo | Issue/PR | Mensagem |
| :--- | :---: | :---: |
| fechada sem horas reais | #27 | '[ARTIGO] Tabela de contribuição e declaração de uso de IA' fechada sem horas reais registradas |
| fechada sem horas reais | #74 | '[ARTIGO] Fase 2: visão geral do GQM e ligação com a Fase 1' fechada sem horas reais registradas |
| fechada sem horas reais | #138 | '[GESTAO] Sincronizar o prazo das issues com o GitHub Projects' fechada sem horas reais registradas |
| fechada sem horas reais | #140 | '[GESTAO] Documentar a priorização e as datas do GitHub Project' fechada sem horas reais registradas |
