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
| Fase 1 | 18 / 18 | 100.0% | 33.3% | 59.5 | 59.0 | R$ 2677.50 | R$ 2655.45 | 99.2% | 1.21 |
| Fase 2 | 29 / 29 | 100.0% | 48.3% | 70.5 | 64.7 | R$ 3172.50 | R$ 2911.50 | 91.8% | 3.74 |
| Fase 3 | 23 / 23 | 100.0% | 8.7% | 48.0 | 65.5 | R$ 2160.00 | R$ 2947.50 | 136.5% | 7.62 |
| Fase 4 | 28 / 27 | 96.4% | 53.6% | 96.0 | 74.5 | R$ 4320.00 | R$ 3350.25 | 87.6% | 12.74 |

---

## 3. Tabela de Contribuicao Individual (Markdown e LaTeX para #27)

| Integrante | GitHub | Issues Atribuidas | Horas Estimadas (h) | Horas Reais (h) | Custo Equivalente (R$) | Commits | PRs | Contribuicao (%) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Christopher | `@wChrstphr` | 29 | 75.5 | 52.6 | R$ 2369.25 | 169 | 28 | **19.97%** |
| Davi Pierre | `@DaviPierre` | 14 | 38.0 | 37.0 | R$ 1665.00 | 13 | 6 | **14.03%** |
| Gabriel Monteiro | `@GabrielSMonteiro` | 18 | 49.5 | 57.0 | R$ 2565.00 | 69 | 16 | **21.62%** |
| Leticia de Carvalho | `@LeticiaSantosss` | 16 | 27.0 | 29.9 | R$ 1345.95 | 16 | 11 | **11.34%** |
| Luiz Henrique Soares | `@luizh-gsoares` | 15 | 32.0 | 32.9 | R$ 1480.50 | 38 | 16 | **12.48%** |
| Maria Eduarda | `@eduarda-ogomes` | 22 | 52.0 | 54.2 | R$ 2439.00 | 83 | 17 | **20.56%** |

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
Christopher & 29 & 75.5h & 52.6h & 169/28 & 19.97\% \\
Davi Pierre & 14 & 38.0h & 37.0h & 13/6 & 14.03\% \\
Gabriel Monteiro & 18 & 49.5h & 57.0h & 69/16 & 21.62\% \\
Leticia de Carvalho & 16 & 27.0h & 29.9h & 16/11 & 11.34\% \\
Luiz Henrique Soares & 15 & 32.0h & 32.9h & 38/16 & 12.48\% \\
Maria Eduarda & 22 & 52.0h & 54.2h & 83/17 & 20.56\% \\
\hline
\textbf{Total} & \textbf{114} & \textbf{274.0h} & \textbf{263.7h} & \textbf{388/94} & \textbf{100.00\%} \\
\hline
\end{tabular}
\end{table}
```


---

## 4. Medidas do Plano de Medicao

### Ritmo de fechamento das issues

| Fase | Inicio | Data media | Fim | Fechadas / Total | Fechadas ate a data media (%) | Fechadas nos 2 ultimos dias | Fechadas apos o fim | Fechadas no prazo (%) | Bloqueadas | Alerta de ritmo |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Fase 1 | 28/09/2026 00:00 | 08/10/2026 11:59 | 18/10/2026 23:59 | 18 / 18 | 0.0 | 13 | 5 | 27.8 | - | sim |
| Fase 2 | 18/10/2026 23:59 | 22/10/2026 23:59 | 26/10/2026 23:59 | 29 / 29 | 55.2 | 8 | 5 | 44.8 | - | nao |
| Fase 3 | 26/10/2026 23:59 | 02/11/2026 11:59 | 08/11/2026 23:59 | 23 / 23 | 0.0 | 7 | 14 | 8.7 | - | sim |
| Fase 4 | 08/11/2026 23:59 | 15/11/2026 11:59 | 21/11/2026 23:59 | 27 / 28 | 7.1 | 8 | 0 | 50.0 | - | sim |

### Acerto das estimativas por issue

Desvio = (horas reais - horas estimadas) / horas estimadas. Na faixa = desvio entre -20% e +20%. O desvio de cada issue esta em `05_detalhamento_issues.csv`.

| Fase | Issues avaliadas | Desvio da fase (%) | Desvio mediano (%) | Na faixa (%) | Subestimadas | Superestimadas |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Fase 1 | 18 | -0.8 | 0.0 | 50.0 | 4 | 5 |
| Fase 2 | 26 | -8.2 | -11.65 | 61.5 | 3 | 7 |
| Fase 3 | 23 | 36.5 | 0.0 | 47.8 | 11 | 1 |
| Fase 4 | 25 | -12.4 | 0.0 | 48.0 | 3 | 10 |

### Tempo de espera dos PRs por revisao

Horas corridas entre a abertura do PR e a primeira revisao de outra pessoa.

| Fase | PRs | Integrados | Integrados com aprovacao | Revisao formal (%) | Sem revisao | Media (h) | Mediana (h) | P80 (h) | P90 (h) | Acima de 24h |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Fase 1 | 17 | 17 | 8 | 47.1 | 9 | 13.68 | 10.82 | 22.28 | 40.59 | 1 |
| Fase 2 | 29 | 27 | 13 | 48.1 | 16 | 3.66 | 0.4 | 7.53 | 7.57 | 1 |
| Fase 3 | 23 | 23 | 15 | 65.2 | 8 | 24.17 | 20.88 | 45.9 | 61.74 | 5 |
| Fase 4 | 25 | 25 | 14 | 56.0 | 10 | 18.0 | 2.65 | 48.16 | 56.29 | 4 |
| Total | 94 | 92 | 50 | 54.3 | 43 | 15.48 | 7.53 | 26.16 | 48.16 | 11 |

### Quem revisou

| Fase | Revisor | PRs revisados | Participacao (%) |
| :--- | :---: | :---: | :---: |
| Fase 1 | eduarda-ogomes | 5 | 62.5 |
| Fase 1 | luizh-gsoares | 2 | 25.0 |
| Fase 1 | GabrielSMonteiro | 1 | 12.5 |
| Fase 2 | luizh-gsoares | 7 | 53.8 |
| Fase 2 | wChrstphr | 5 | 38.5 |
| Fase 2 | eduarda-ogomes | 1 | 7.7 |
| Fase 3 | wChrstphr | 7 | 46.7 |
| Fase 3 | eduarda-ogomes | 7 | 46.7 |
| Fase 3 | luizh-gsoares | 1 | 6.7 |
| Fase 4 | wChrstphr | 10 | 62.5 |
| Fase 4 | eduarda-ogomes | 6 | 37.5 |
| Total | wChrstphr | 22 | 42.3 |
| Total | eduarda-ogomes | 19 | 36.5 |
| Total | luizh-gsoares | 10 | 19.2 |
| Total | GabrielSMonteiro | 1 | 1.9 |

### Autor por revisor

| Fase | Autor | Revisor | PRs |
| :--- | :---: | :---: | :---: |
| Fase 1 | DaviPierre | eduarda-ogomes | 1 |
| Fase 1 | GabrielSMonteiro | eduarda-ogomes | 2 |
| Fase 1 | LeticiaSantosss | GabrielSMonteiro | 1 |
| Fase 1 | eduarda-ogomes | luizh-gsoares | 2 |
| Fase 1 | wChrstphr | eduarda-ogomes | 2 |
| Fase 2 | GabrielSMonteiro | wChrstphr | 1 |
| Fase 2 | eduarda-ogomes | luizh-gsoares | 1 |
| Fase 2 | eduarda-ogomes | wChrstphr | 1 |
| Fase 2 | luizh-gsoares | wChrstphr | 3 |
| Fase 2 | wChrstphr | eduarda-ogomes | 1 |
| Fase 2 | wChrstphr | luizh-gsoares | 6 |
| Fase 3 | DaviPierre | wChrstphr | 2 |
| Fase 3 | GabrielSMonteiro | eduarda-ogomes | 3 |
| Fase 3 | GabrielSMonteiro | wChrstphr | 2 |
| Fase 3 | LeticiaSantosss | wChrstphr | 2 |
| Fase 3 | eduarda-ogomes | wChrstphr | 1 |
| Fase 3 | wChrstphr | eduarda-ogomes | 4 |
| Fase 3 | wChrstphr | luizh-gsoares | 1 |
| Fase 4 | GabrielSMonteiro | wChrstphr | 2 |
| Fase 4 | eduarda-ogomes | wChrstphr | 4 |
| Fase 4 | luizh-gsoares | eduarda-ogomes | 2 |
| Fase 4 | luizh-gsoares | wChrstphr | 4 |
| Fase 4 | wChrstphr | eduarda-ogomes | 4 |
| Total | DaviPierre | eduarda-ogomes | 1 |
| Total | DaviPierre | wChrstphr | 2 |
| Total | GabrielSMonteiro | eduarda-ogomes | 5 |
| Total | GabrielSMonteiro | wChrstphr | 5 |
| Total | LeticiaSantosss | GabrielSMonteiro | 1 |
| Total | LeticiaSantosss | wChrstphr | 2 |
| Total | eduarda-ogomes | luizh-gsoares | 3 |
| Total | eduarda-ogomes | wChrstphr | 6 |
| Total | luizh-gsoares | eduarda-ogomes | 2 |
| Total | luizh-gsoares | wChrstphr | 7 |
| Total | wChrstphr | eduarda-ogomes | 11 |
| Total | wChrstphr | luizh-gsoares | 7 |

### PRs

| PR | Fase | Origem da fase | Autor | Situacao | Aberto em | Primeira revisao | Espera (h) | Aprovado | Revisores |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| #193 | Fase 4 | issue #130 | eduarda-ogomes | integrado | 20/11/2026 20:31 | - | - | nao | - |
| #192 | Fase 4 | issue #181 | wChrstphr | integrado | 20/11/2026 19:49 | 20/11/2026 20:12 | 0.39 | sim | eduarda-ogomes |
| #191 | Fase 4 | issue #190 | wChrstphr | integrado | 18/11/2026 20:03 | 20/11/2026 20:13 | 48.16 | sim | eduarda-ogomes |
| #189 | Fase 4 | issue #126 | eduarda-ogomes | integrado | 18/11/2026 12:38 | 20/11/2026 19:59 | 55.35 | sim | wChrstphr |
| #188 | Fase 4 | issue #119 | wChrstphr | integrado | 18/11/2026 11:51 | 20/11/2026 20:09 | 56.29 | sim | eduarda-ogomes |
| #187 | Fase 4 | issue #119 | wChrstphr | integrado | 18/11/2026 10:13 | 20/11/2026 20:05 | 57.87 | sim | eduarda-ogomes |
| #186 | Fase 4 | issue #125 | luizh-gsoares | integrado | 17/11/2026 23:27 | 17/11/2026 23:33 | 0.11 | sim | wChrstphr |
| #185 | Fase 4 | issue #124 | eduarda-ogomes | integrado | 17/11/2026 22:26 | 17/11/2026 23:36 | 1.17 | sim | wChrstphr |
| #184 | Fase 4 | issue #122 | eduarda-ogomes | integrado | 17/11/2026 20:57 | 17/11/2026 23:36 | 2.65 | sim | wChrstphr |
| #182 | Fase 4 | issue #129 | luizh-gsoares | integrado | 17/11/2026 12:34 | 17/11/2026 20:49 | 8.24 | sim | eduarda-ogomes |
| #180 | Fase 4 | issue #115 | luizh-gsoares | integrado | 17/11/2026 11:53 | 17/11/2026 12:07 | 0.23 | sim | wChrstphr |
| #179 | Fase 4 | titulo | luizh-gsoares | integrado | 17/11/2026 11:50 | 17/11/2026 11:55 | 0.07 | sim | wChrstphr |
| #178 | Fase 4 | issue #120 | luizh-gsoares | integrado | 16/11/2026 12:54 | - | - | nao | - |
| #177 | Fase 4 | issue #123 | GabrielSMonteiro | integrado | 16/11/2026 01:36 | - | - | nao | - |
| #176 | Fase 4 | issue #116 | luizh-gsoares | integrado | 16/11/2026 00:10 | - | - | nao | - |
| #175 | Fase 4 | issue #118 | wChrstphr | integrado | 15/11/2026 21:26 | - | - | nao | - |
| #173 | Fase 4 | issue #115 | wChrstphr | integrado | 15/11/2026 20:01 | - | - | nao | - |
| #172 | Fase 3 | issue #85 | LeticiaSantosss | integrado | 15/11/2026 19:37 | 15/11/2026 19:55 | 0.31 | sim | wChrstphr |
| #171 | Fase 3 | issue #106 | LeticiaSantosss | integrado | 15/11/2026 18:55 | - | - | nao | - |
| #170 | Fase 4 | issue #112 | luizh-gsoares | integrado | 15/11/2026 18:26 | - | - | nao | - |
| #169 | Fase 4 | issue #114 | wChrstphr | integrado | 15/11/2026 15:00 | - | - | nao | - |
| #168 | Fase 4 | issue #111 | wChrstphr | integrado | 15/11/2026 14:39 | - | - | nao | - |
| #167 | Fase 4 | issue #109 | GabrielSMonteiro | integrado | 14/11/2026 20:56 | 15/11/2026 15:16 | 18.32 | sim | wChrstphr |
| #166 | Fase 4 | issue #133 | GabrielSMonteiro | integrado | 14/11/2026 20:42 | 15/11/2026 15:14 | 18.55 | sim | wChrstphr |
| #165 | Fase 3 | issue #105 | GabrielSMonteiro | integrado | 14/11/2026 19:47 | 15/11/2026 15:05 | 19.29 | sim | wChrstphr |
| #164 | Fase 3 | issue #104 | DaviPierre | integrado | 14/11/2026 11:36 | - | - | nao | - |
| #163 | Fase 3 | issue #107 | GabrielSMonteiro | integrado | 13/11/2026 00:06 | 15/11/2026 14:55 | 62.83 | sim | wChrstphr |
| #162 | Fase 4 | data | GabrielSMonteiro | integrado | 12/11/2026 23:01 | - | - | nao | - |
| #161 | Fase 3 | titulo | GabrielSMonteiro | integrado | 12/11/2026 22:44 | - | - | nao | - |
| #160 | Fase 3 | issue #103 | eduarda-ogomes | integrado | 12/11/2026 13:57 | - | - | nao | - |
| #159 | Fase 3 | issue #99 | LeticiaSantosss | integrado | 11/11/2026 22:35 | - | - | nao | - |
| #158 | Fase 4 | issue #113 | eduarda-ogomes | integrado | 11/11/2026 14:54 | 11/11/2026 16:45 | 1.84 | nao | wChrstphr |
| #157 | Fase 4 | issue #110 | luizh-gsoares | integrado | 10/11/2026 21:55 | 10/11/2026 22:37 | 0.69 | sim | eduarda-ogomes, wChrstphr |
| #156 | Fase 1 | issue #155 | wChrstphr | integrado | 10/11/2026 21:48 | 11/11/2026 20:04 | 22.28 | sim | eduarda-ogomes |
| #154 | Fase 2 | issue #153 | wChrstphr | integrado | 10/11/2026 12:51 | 11/11/2026 15:16 | 26.43 | sim | eduarda-ogomes |
| #152 | Fase 3 | issue #95 | LeticiaSantosss | integrado | 09/11/2026 20:51 | 10/11/2026 11:30 | 14.66 | sim | wChrstphr |
| #151 | Fase 3 | issue #135 | wChrstphr | integrado | 09/11/2026 19:19 | 10/11/2026 08:56 | 13.61 | sim | eduarda-ogomes |
| #150 | Fase 3 | issue #101 | wChrstphr | integrado | 08/11/2026 23:48 | 09/11/2026 00:09 | 0.35 | sim | luizh-gsoares |
| #149 | Fase 3 | issue #95 | DaviPierre | integrado | 08/11/2026 23:41 | 09/11/2026 00:58 | 1.28 | sim | wChrstphr |
| #148 | Fase 3 | titulo | DaviPierre | integrado | 08/11/2026 22:42 | 09/11/2026 19:35 | 20.88 | sim | wChrstphr |
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
| #91 | Fase 2 | issue #90 | eduarda-ogomes | integrado | 28/10/2026 17:16 | 28/10/2026 17:23 | 0.11 | sim | wChrstphr |
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
| fechada sem horas reais | #125 | '[ARTIGO] Conclusão: julgamento, relações entre as características e trabalhos futuros' fechada sem horas reais registradas |
| fechada sem horas reais | #126 | '[GESTAO] Relatório PSM/CID da Fase 4 e consolidado da Entrega 2' fechada sem horas reais registradas |
| horas nao lidas | #126 | valor ilegivel: '### Revisor

_No response_' |
