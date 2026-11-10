# Coleta e Calculo de Metricas PSM/CID

Este diretorio contem a automacao responsavel por extrair dados de gestao do repositorio via API do GitHub e gerar os indicadores das tres categorias exigidas pelo framework **PSM/CID (Practical Software and Systems Measurement: Continuous Iterative Development)**:

1. **Recursos e Custos (*Resources and Cost*):** Esforco planejado (horas estimadas) vs. esforco realizado (horas reais), custo financeiro equivalente ($\text{Horas} \times \text{Valor-Hora}$) e distribuicao percentual de esforco por integrante (criterio **AG-C5**).
2. **Calendario e Progresso (*Schedule and Progress*):** Taxa de conclusao das milestones (`Fase 1` a `Fase 4`) e aderencia aos prazos planejados.
3. **Desempenho dos Processos (*Process Performance*):** Acuracia das estimativas de esforco, taxa de governanca no preenchimento de issues e *lead time* medio de conclusao.

---

## Estrutura de Arquivos

- [`config.json`](config.json): Parametros de configuracao (nome do repositorio, valor-hora de referencia em BRL, fonte salarial de mercado e mapeamento de logins da equipe).
- [`coleta_psm.py`](coleta_psm.py): Script principal de extracao, transformacao e geracao de artefatos.
- [`requirements.txt`](requirements.txt): Dependencias Python para requisicoes e plotagem de graficos.

---

## Como Executar

### 1. Instalar as dependencias

Recomenda-se o uso de um ambiente virtual Python (`venv`):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r scripts/requirements.txt
```

### 2. Executar a coleta (modo online via API do GitHub)

A partir da raiz do repositorio:

```bash
python3 scripts/coleta_psm.py
```

Caso deseje autenticar para evitar limites de requisicao da API publica do GitHub:

```bash
GITHUB_TOKEN="seu_token_aqui" python3 scripts/coleta_psm.py
```

### 3. Executar a partir do snapshot local (modo offline / auditoria)

Para recalcular indicadores e regerar os graficos usando o snapshot bruto ja salvo em `dados/gestao/raw_github_data.json` (sem necessidade de conexao com a internet):

```bash
python3 scripts/coleta_psm.py --offline
```

---

## Artefatos Gerados em `dados/gestao/`

Apos a execucao, os seguintes arquivos sao gerados e atualizados automaticamente:

- `raw_github_data.json`: Snapshot bruto da API do GitHub (issues, PRs, milestones e commits) para rastreabilidade e auditoria (**Premissa 5**).
- `01_recursos_e_custos_fases.csv`: Horas estimadas, horas reais e custos por fase.
- `02_calendario_e_progresso_fases.csv`: Total de issues, concluidas, abertas e aderencia aos prazos por fase.
- `03_desempenho_processos_fases.csv`: Acuracia de estimativa, taxa de preenchimento e *lead time* medio por fase.
- `04_contribuicao_individual.csv`: Quantidade de issues, horas estimadas, horas reais, custo, commits, PRs e percentual de esforco individual (somando 100%).
- `05_detalhamento_issues.csv`: Visao analitica de todas as issues do projeto, com o desvio da estimativa de cada issue e a classificacao (na faixa, subestimada ou superestimada).
- `06_contribuicao_por_fase.csv`, `07_resumo_entregas.csv` e `08_contribuicao_por_entrega.csv`: Os mesmos indicadores separados por fase e por entrega.
- `constructs_e_tabelas.md`: Documento contendo as fichas estruturadas no modelo **Measurement Construct**, tabelas em Markdown para o GitPage, codigo em LaTeX da tabela de contribuicao para o artigo SBC e a secao 4 com as medidas do plano de medicao e os avisos da coleta.
- `graficos/`:
  - `01_recursos_e_custos_fases.png`
  - `02_calendario_e_progresso_fases.png`
  - `03_contribuicao_individual.png`

---

## Medidas do Plano de Medicao

As tres medidas seguem o [Plano de Medicao PSM/CID](../docs/gestao/plano-medicao-psm.md) e saem na secao 4 de `constructs_e_tabelas.md`. Os dados de origem ficam em `raw_github_data.json`, entao tudo pode ser recalculado com `--offline`.

- **Ritmo de fechamento (Calendario e Progresso):** issues fechadas ate a data media da fase, nos 2 ultimos dias, apos o fim e no prazo, e issues abertas bloqueadas por uma issue aberta no campo `Depende de` (faixas como `#73 a #78` sao expandidas). O total da fase e toda issue da milestone.
- **Acerto das estimativas (Recursos e Custos):** desvio de cada issue com estimativa e horas reais, $(\text{Horas Reais} - \text{Horas Estimadas}) / \text{Horas Estimadas}$. Fica na faixa quem tem desvio entre -20% e +20%. A acuracia da fase em `03` e `07` usa so essas issues.
- **Tempo de espera por revisao (Desempenho dos Processos):** horas corridas entre a abertura do PR e a primeira revisao de outra pessoa, de qualquer tipo. Revisoes do proprio autor e de bots nao contam. A revisao formal e uma revisao `APPROVED`. Saem media, mediana, P80, P90, PRs acima de 24h, quem revisou e a matriz autor por revisor. As Fases 1 e 2 formam a linha de base.

**Janela das fases:** a Fase 1 comeca em `inicio_fase_1` do `config.json` (28/09/2026, primeiro ponto de controle). Cada fase termina as 23:59 (horario de Brasilia) do dia do `due_on` da milestone, e a seguinte comeca ali.

**Fase de um PR**, na ordem:

1. a milestone da issue ligada, pelo prefixo `[X-N]` do titulo ou por `Closes`, `Fixes` ou `Resolves #N` no corpo,
2. a fase citada no titulo e, se nao houver, no corpo (`F3`, `Fase 3`, `Fase3`, `Fase 03`, `fase-03`, `Terceira Fase`), desde que seja uma so,
3. a fase cuja janela contem a data de abertura do PR.

## Formato das Horas e Avisos

O campo `Horas reais (h)` aceita `2.5`, `2,5`, `2h30`, `1h30m`, `20m`, `@login: 2h, @outro: 1h` e tambem `@login 2h`, sem os dois-pontos. Sem `@login`, as horas sao divididas igualmente entre os responsaveis da issue.

A coleta emite aviso, com o numero da issue, no fim da execucao e na secao 4 de `constructs_e_tabelas.md` quando:

- as horas nao podem ser lidas,
- as horas nao podem ser atribuidas a ninguem (issue sem responsavel e sem `@login`, ou login fora de `config.json`),
- o total declarado difere da soma por integrante,
- um valor como `2h5` e lido como 2 horas e 5 minutos, o que pode ser engano para 2,5 horas,
- uma issue fechada nao tem horas reais (issues fechadas como `not planned` ficam de fora),
- uma faixa do campo `Depende de` esta invertida ou cobre 100 issues ou mais (ela e ignorada), ou
- um PR aberto esta ha mais de 24 horas sem revisao.

