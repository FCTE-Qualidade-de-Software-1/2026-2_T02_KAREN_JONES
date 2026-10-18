# Coleta e Calculo de Metricas PSM/CID

Este diretorio contem a automacao responsavel por extrair dados de gestao do repositorio via API do GitHub e gerar os indicadores das tres categorias exigidas pelo framework **PSM/CID (Practical Software and Systems Measurement — Continuous Iterative Development)**:

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
- `05_detalhamento_issues.csv`: Visao analitica de todas as issues do projeto.
- `constructs_e_tabelas.md`: Documento contendo as fichas estruturadas no modelo **Measurement Construct**, tabelas em Markdown para o GitPage e codigo em LaTeX da tabela de contribuicao para o artigo SBC.
- `graficos/`:
  - `01_recursos_e_custos_fases.png`
  - `02_calendario_e_progresso_fases.png`
  - `03_contribuicao_individual.png`
