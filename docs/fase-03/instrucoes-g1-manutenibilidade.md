---
sidebar_position: 3
title: Instruções para o avaliador — Manutenibilidade (G1)
description: Roteiro reproduzível de coleta das 14 métricas de Manutenibilidade do Excalidraw, com comandos, critérios de cálculo, evidências e formulários.
---

# Instruções para o avaliador — Manutenibilidade (G1)

Este roteiro especifica **como obter e registrar as 14 métricas de G1** do Excalidraw, organizadas pelas cinco questões de Manutenibilidade (Q1.1 a Q1.5). Ele operacionaliza as [fichas da Fase 02](../fase-02/gqm-manutenibilidade.md) e o [plano de recursos e ambiente](./recursos-ambiente.md), no âmbito da [issue #98](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/98).

**Separação entre planejamento e execução:** esta página **não apresenta resultados medidos**. Os valores, logs, planilhas revisadas e arquivos de evidência serão produzidos e conferidos na Fase 04, na [issue #111](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/111), e auditados na [issue #114](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/114). As faixas de pontuação não são redefinidas aqui; estão na [seção 3 da página de pontuação](../fase-02/pontuacao-julgamento.md#3-níveis-das-métricas-de-manutenibilidade-g1).

## 1. Resumo e rastreabilidade

| Questão | Subcaracterística | Métricas | Fonte normativa interna |
| :--- | :--- | :--- | :--- |
| Q1.1 | Modularidade | M1.1.1–M1.1.3 | [GQM de G1, seção 3](../fase-02/gqm-manutenibilidade.md#3-q11--modularidade) |
| Q1.2 | Reusabilidade | M1.2.1–M1.2.2 | [GQM de G1, seção 4](../fase-02/gqm-manutenibilidade.md#4-q12--reusabilidade) |
| Q1.3 | Analisabilidade | M1.3.1–M1.3.3 | [GQM de G1, seção 5](../fase-02/gqm-manutenibilidade.md#5-q13--analisabilidade) |
| Q1.4 | Modificabilidade | M1.4.1–M1.4.3 | [GQM de G1, seção 6](../fase-02/gqm-manutenibilidade.md#6-q14--modificabilidade) |
| Q1.5 | Testabilidade | M1.5.1–M1.5.3 | [GQM de G1, seção 7](../fase-02/gqm-manutenibilidade.md#7-q15--testabilidade) |

A tabela de [Métodos e justificativas da #95](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/95) estabelece a relação entre fonte, método, ferramenta e pontuação. **Enquanto a página `metodo-avaliacao.md` não estiver publicada, consultar a issue #95; não adicionar um link local quebrado.**

## 2. Pré-condições, preparação e convenções

### 2.1 Linha de base e limites da amostra

| Campo | Valor obrigatório |
| :--- | :--- |
| Repositório do produto | `excalidraw/excalidraw` (não o repositório da equipe avaliadora) |
| Commit | `e1b7aacb356a492aa1e0fc6eb57b8896124027f0`, de 18/10/2026 |
| Janela histórica | PRs integrados à `master` entre **18/04/2026 e 18/10/2026**, inclusive |
| Pacotes | Cada pasta de `packages/`: `common`, `element`, `excalidraw`, `fractional-indexing`, `laser-pointer`, `math`, `utils`; e a aplicação `excalidraw-app/` |
| Pacotes de base | Todos os pacotes anteriores, exceto `excalidraw`; `excalidraw-app` não é pacote de base |
| Produção | `.ts`/`.tsx` de pacotes e aplicação; excluir `tests/`, `__snapshots__/`, `*.test.ts(x)`, `*.d.ts`, dependências, exemplos e documentação |
| Testes | Suítes `*.test.ts` e `*.test.tsx` nos pacotes; excluir utilitários e fixtures que não são suítes |
| Ferramentas principais | Madge 8.0.0, ESLint 8.57.0, TypeScript 5.9.3, cloc 1.86, Vitest 3.0.6, GitHub CLI 2.102.0 e Python 3 |
| Responsável pela coleta | Christopher, conforme [cronograma](./cronograma-avaliacao.md) |

As regras acima vêm das [convenções da Fase 02](../fase-02/gqm-manutenibilidade.md#2-convenções-de-coleta); não incluir versões recentes de `master`, PRs após 18/10/2026 nem arquivos de testes no denominador de produção.

### 2.2 Arquivos auxiliares deste roteiro

Para que os comandos abaixo sejam reproduzíveis, a entrega da #98 inclui os arquivos auxiliares:

```text
scripts/
  g1_processar.py       # inventário; grafo; LOC; cobertura; testes; histórico
  g1_typescript.cjs     # inspeção AST (dependências, API e complexidade)
  g1_preparar_prs.py    # junção e auditoria de respostas API de PR/CI
  g1-madge.json         # configurações fixas do analisador de dependências
```

Esses scripts devem ser adicionados **junto com esta página**. A ausência deles impede a execução dos comandos que os referenciam. O código de coleta também deve passar por revisão antes de produzir resultados oficiais.

### 2.3 Comandos de preparação

Os exemplos abaixo são para **Bash em Linux/WSL2** (o ambiente de G1 documentado para Christopher). Substituir apenas a pasta pessoal, não o commit. Partindo da **raiz do repositório da equipe**:

```bash
export AVAL="$PWD"
export EXC="$HOME/excalidraw-avaliado-g1"
export BRUTOS="$AVAL/dados/fase-04/brutos/g1"
export CONS="$AVAL/dados/fase-04/consolidados/g1"
mkdir -p "$BRUTOS" "$CONS" "$BRUTOS/prs"

git clone https://github.com/excalidraw/excalidraw.git "$EXC"
git -C "$EXC" checkout e1b7aacb356a492aa1e0fc6eb57b8896124027f0
git -C "$EXC" rev-parse HEAD | tee "$BRUTOS/commit.txt"
# A saída DEVE ser e1b7aacb356a492aa1e0fc6eb57b8896124027f0.

cd "$EXC"
node --version | tee "$BRUTOS/versao-node.txt"
yarn --version | tee "$BRUTOS/versao-yarn.txt"
python3 --version | tee "$BRUTOS/versao-python.txt"
yarn --frozen-lockfile --network-timeout 600000 2>&1 | tee "$BRUTOS/instalacao-dependencias.log"
yarn build:packages 2>&1 | tee "$BRUTOS/build-pacotes.log"

python3 "$AVAL/scripts/g1_processar.py" inventario \
  --src "$EXC" --out "$BRUTOS/inventario.json"
```

**Saída esperada:** commit completo fixado, instalações sem erro e `inventario.json` contendo `producao`, `testes` e `pacotes`. Se o inventário estiver vazio, a instalação falhar ou o commit diferir, **interromper a coleta** e registrar o desvio. O comando `tee` preserva logs, mas pode mascarar códigos de saída em pipelines; executar antes `set -o pipefail` na mesma sessão.

**Controle ambiental:** salvar `uname -a`, `git --version`, `gh --version`, `cloc --version`, `npx madge@8.0.0 --version`, `node --version`, `yarn --version`, data/hora e identificação da máquina. O navegador e a rede são **não aplicáveis** à maioria das medidas estáticas; se usados para conferir documentação online ou GitHub, registrar a versão do navegador, data da consulta, conectividade e eventual cache. Para a API GitHub, registrar também a autenticação e possíveis respostas com rate limit, sem salvar tokens.

### 2.4 Padrão obrigatório de evidência

**Dados brutos** ficam em `dados/fase-04/brutos/g1/` (JSON de ferramentas e APIs, logs, CSVs de inspeção, capturas quando necessárias). **Consolidados** ficam em `dados/fase-04/consolidados/g1/` (contagens, médias, percentuais e tabelas). Para toda métrica, preencher o formulário da seção 8 com **ID, responsável, data e hora, commit, ferramenta/versão, comando, amostra, exclusões, arquivos brutos, valor calculado, hipótese e anomalias**. Falhas ou indisponibilidades não viram pontuação zero sem evidência.

> **Observação de compatibilidade:** relatórios do ESLint têm saída de erro por conta da regra `complexity` fixada em zero. O status de saída diferente de zero é esperado apenas nesse comando; erros fatais de análise, cobertura incompleta do grafo ou dados ausentes **não** são ignorados. As ferramentas auxiliares produzem candidatos que exigem auditoria humana onde indicado.

## 3. Q1.1 — Modularidade

### 3.1. Extração comum do grafo de dependências

As três métricas de Q1.1 e a M1.2.1 reutilizam **um único grafo de importações de valor**. A opção `skipTypeImports` do Madge evita contar declarações explícitas `import type`, mas o detector pode não identificar todas as importações implicitamente eliminadas pelo compilador; conferir o resultado com TypeScript quando aparecer uma aresta suspeita. Não confundir ciclo de arquivos com ciclo de **pacotes**.

Instale o Madge 8.0.0 **fora do repositório avaliado**, sem alterar o `package.json` do produto. Na pasta do produto, somente durante a execução, disponibilize uma `.madgerc` temporária:

```bash
cd "$EXC"
if [ -e .madgerc ]; then echo 'Já existe .madgerc: revise manualmente e não sobrescreva.'; exit 1; fi
cp "$AVAL/scripts/g1-madge.json" .madgerc
npx --yes madge@8.0.0 --json --no-spinner \
  --basedir "$EXC" --ts-config "$EXC/tsconfig.json" \
  --extensions ts,tsx packages excalidraw-app \
  > "$BRUTOS/grafo-dependencias-madge.json" \
  2> "$BRUTOS/grafo-dependencias-madge-erros.log"
rm .madgerc
python3 -m json.tool "$BRUTOS/grafo-dependencias-madge.json" > /dev/null
python3 "$AVAL/scripts/g1_processar.py" grafo \
  --inventario "$BRUTOS/inventario.json" \
  --grafo "$BRUTOS/grafo-dependencias-madge.json" --saida "$CONS"
```

**Saídas esperadas:** JSON de arquivo → dependências; `M1.1.1-pares-ciclicos.json`, `M1.1.2-violacoes.csv`, `M1.1.3-acoplamento.csv` e `grafo-pacotes.json`. Conferir a taxa de cobertura informada por `g1_processar.py` e os avisos de importações não resolvidas do Madge. A limpeza de `.madgerc` é obrigatória mesmo em caso de falha: se o comando for interrompido, removê-la manualmente **somente após confirmar que não existia antes**.

### 3.2. M1.1.1 — Ciclos de dependência entre pacotes

**[Ficha M1.1.1](../fase-02/gqm-manutenibilidade.md#m111--ciclos-de-dependência-entre-pacotes) · [Faixas de G1](../fase-02/pontuacao-julgamento.md#3-níveis-das-métricas-de-manutenibilidade-g1)**

1. Executar a extração comum da seção 3.1.
2. Abrir `"$CONS/M1.1.1-pares-ciclicos.json"` e conferir a lista de pares `(A,B)`.
3. Para cada par, verificar no `grafo-pacotes.json` que **A alcança B e B alcança A** por uma ou mais arestas de importação de valor. Cada par não ordenado é contado uma vez.
4. **Cálculo:** número de pares recíprocos. Não utilizar `madge --circular` como contagem final, pois ele identifica ciclos entre arquivos, não pares de pacotes.

**Saída esperada:** `total_pares` inteiro e lista de pares, com evidências no grafo. **Dado bruto:** `grafo-dependencias-madge.json`. **Consolidado:** `M1.1.1-pares-ciclicos.json`. Se houver caminhos não resolvidos, registrar o impacto no valor antes de pontuar.

### 3.3. M1.1.2 — Importações que violam a direção declarada

**[Ficha M1.1.2](../fase-02/gqm-manutenibilidade.md#m112--importações-que-violam-a-direção-declarada) · [Faixas de G1](../fase-02/pontuacao-julgamento.md#3-níveis-das-métricas-de-manutenibilidade-g1)**

1. Executar a seção 3.1 e abrir `"$CONS/M1.1.2-violacoes.csv"`.
2. Inspecionar cada ocorrência `origem → destino` e confirmar as condições: **pacote de base → biblioteca `excalidraw`**, ou **qualquer pacote → aplicação `excalidraw-app`**. Consultar também `packages/eslintrc.base.json` no commit avaliado.
3. Verificar arestas não resolvidas e importações de tipo; corrigir a classificação no procedimento de extração **antes** de consolidar, preservando o bruto original.
4. **Cálculo:** número de pares arquivo de origem → arquivo de destino classificados como violação. Não interpretar quantas regras foram violadas como se fossem arquivos distintos.

**Saída esperada:** CSV auditável de violações (possivelmente apenas cabeçalho, quando zero). **Bruto:** grafo do Madge. **Consolidado:** `M1.1.2-violacoes.csv` e a contagem de linhas de dados desse CSV.

### 3.4. M1.1.3 — Acoplamento e instabilidade de cada pacote

**[Ficha M1.1.3](../fase-02/gqm-manutenibilidade.md#m113--acoplamento-e-instabilidade-de-cada-pacote) · [Faixas de G1](../fase-02/pontuacao-julgamento.md#3-níveis-das-métricas-de-manutenibilidade-g1)**

1. Reutilizar o grafo da seção 3.1, sem reexecutar a coleta com opções diferentes.
2. Abrir `"$CONS/M1.1.3-acoplamento.csv"`, conferindo todos os pacotes do inventário.
3. Para cada pacote `P`, contar **Ca** (quantos outros pacotes distintos importam `P`) e **Ce** (quantos pacotes distintos `P` importa).
4. **Cálculo:** `I = Ce / (Ca + Ce)`; quando `Ca + Ce = 0`, registrar `I = não aplicável`, não zero inventado. Conferir qual pacote tem o maior `Ca`, conforme a hipótese H1.1.3.

**Saída esperada:** uma linha por pacote com `Ca`, `Ce`, `I` e sinalização de pacote sem arestas. **Bruto:** grafo. **Consolidado:** `M1.1.3-acoplamento.csv`.

## 4. Q1.2 — Reusabilidade

### 4.1. M1.2.1 — Dependência direta ou transitiva de React/navegador

**[Ficha M1.2.1](../fase-02/gqm-manutenibilidade.md#m121--arquivos-de-pacotes-de-base-com-dependência-de-react-ou-do-navegador) · [Faixas de G1](../fase-02/pontuacao-julgamento.md#3-níveis-das-métricas-de-manutenibilidade-g1)**

1. A partir do checkout com dependências instaladas, executar o extrator AST em todos os arquivos de produção:

   ```bash
   node "$AVAL/scripts/g1_typescript.cjs" mapear \
     --src "$EXC" --inventario "$BRUTOS/inventario.json" --saida "$BRUTOS"
   ```

2. Abrir `M1.2.1-sementes-para-auditoria.csv`: para cada ocorrência, confirmar que há importação **de valor** de `react`/`react-dom` ou uso efetivo dos globais `window`/`document` (não variável local, string, comentário ou referência só de tipo). Preencher `validado=sim` ou `validado=nao`, com justificativa externa ao CSV quando necessário. **Não usar automaticamente as sementes sem revisão.**
3. Construir `"$BRUTOS/M1.2.1-diretos-validados.json"` com a estrutura `{"diretos":["packages/.../arquivo.ts", ...]}`, incluindo apenas os caminhos únicos das linhas `sim` do CSV auditado:

   ```bash
   python3 - "$BRUTOS/M1.2.1-sementes-para-auditoria.csv" "$BRUTOS/M1.2.1-diretos-validados.json" <<'PY'
   import csv,json,sys
   rows=list(csv.DictReader(open(sys.argv[1],encoding='utf-8')))
   assert all(x['validado'] in ('sim','nao') for x in rows), 'Audite todas as sementes'
   with open(sys.argv[2],'w',encoding='utf-8') as f:
       json.dump({'diretos':sorted({x['arquivo'] for x in rows if x['validado']=='sim'})},f,indent=2)
   PY
   ```

4. Propagar a dependência direta pelo grafo de **importações de valor**, inclusive reexportações, e contar arquivos de produção **por pacote de base**:

   ```bash
   python3 "$AVAL/scripts/g1_processar.py" navegador \
     --inventario "$BRUTOS/inventario.json" \
     --grafo "$BRUTOS/grafo-dependencias-madge.json" \
     --diretos "$BRUTOS/M1.2.1-diretos-validados.json" --saida "$CONS"
   ```

5. **Cálculo:** para cada pacote, informar `diretas + transitivas_apenas` e `(diretas + transitivas_apenas) / arquivos_total × 100`. Conferir em especial `math` e `utils`, que estão na hipótese da ficha.

**Saídas:** `M1.2.1-arquivos-react-navegador.csv` e `M1.2.1-resumo.json`. O arquivo CSV auditado de sementes e o grafo são os **brutos** indispensáveis. Variáveis `window`/`document` sem `.` e outros padrões não cobertos pela triagem devem ser verificados por inspeção de código quando se detectarem omissões; documentar a decisão.

### 4.2. M1.2.2 — Proporção de propriedades públicas documentadas

**[Ficha M1.2.2](../fase-02/gqm-manutenibilidade.md#m122--proporção-de-propriedades-públicas-documentadas) · [Faixas de G1](../fase-02/pontuacao-julgamento.md#3-níveis-das-métricas-de-manutenibilidade-g1)**

1. Reutilizar `M1.2.2-propriedades-para-auditoria.csv`, gerado pelo comando AST da M1.2.1. Ele extrai os membros da **interface `ExcalidrawProps`** em `packages/excalidraw/types.ts` (o tipo é uma interface neste commit).
2. Abrir as páginas de `dev-docs/docs/@excalidraw/excalidraw/api/` **no checkout avaliado**. Para cada propriedade, procurar uma descrição de seu propósito, não apenas uma ocorrência do identificador:

   ```bash
   cd "$EXC"
   grep -RIn --include='*.md' --include='*.mdx' 'onChange\|initialData\|onMount' \
     dev-docs/docs/@excalidraw/excalidraw/api/ \
     > "$BRUTOS/M1.2.2-busca-documentacao-exemplo.txt"
   ```

3. Preencher **todas** as linhas do CSV auditado: `documentada=sim/nao`; quando `sim`, informar `caminho_documentacao` e `trecho_evidencia` (ou seção). O `grep` acima apenas exemplifica a busca; a verificação deve cobrir **cada propriedade extraída**, inclusive as que não constam do exemplo.
4. Calcular somente após preencher a planilha:

   ```bash
   python3 - "$BRUTOS/M1.2.2-propriedades-para-auditoria.csv" "$CONS/M1.2.2-resultado.json" <<'PY'
   import csv,json,sys
   dados=list(csv.DictReader(open(sys.argv[1],encoding='utf-8')))
   assert dados and all(x['documentada'] in ('sim','nao') for x in dados), 'Faltam decisões'
   assert all(x['caminho_documentacao'] and x['trecho_evidencia'] for x in dados if x['documentada']=='sim'), 'Faltam evidências'
   n=sum(x['documentada']=='sim' for x in dados)
   json.dump({'documentadas':n,'total_declaradas':len(dados),'percentual':100*n/len(dados)},open(sys.argv[2],'w',encoding='utf-8'),indent=2)
   PY
   ```

**Saídas:** inventário de propriedades + evidências por propriedade; percentual `documentadas / total × 100`. **Bruto:** CSV de auditoria; **consolidado:** `M1.2.2-resultado.json`.

## 5. Q1.3 — Analisabilidade

### 5.1. M1.3.1 — Perfil de risco de complexidade das funções

**[Ficha M1.3.1](../fase-02/gqm-manutenibilidade.md#m131--perfil-de-risco-de-complexidade-das-funções) · [Faixas e risco de G1](../fase-02/pontuacao-julgamento.md#31-faixas-de-m131)**

1. Executar o ESLint do commit, com a regra `complexity` configurada para relatar **todas** as funções (limite 0). Salvar a saída **JSON**, não apenas o resumo no terminal:

   ```bash
   cd "$EXC"
   ./node_modules/.bin/eslint --format json \
     --rule 'complexity: [error, 0]' --ext .ts,.tsx \
     packages excalidraw-app \
     > "$BRUTOS/M1.3.1-eslint-bruto.json" \
     2> "$BRUTOS/M1.3.1-eslint-erros.log"
   # Um código de saída 1 por excesso de complexidade é esperado; erros fatais NÃO são.
   python3 -m json.tool "$BRUTOS/M1.3.1-eslint-bruto.json" > /dev/null
   ```

2. Cruzar os avisos `ruleId=complexity` com a AST TypeScript **da mesma versão de código**, desconsiderando inicializadores de campos que não sejam funções, computando para cada função as linhas próprias não vazias/não comentários e descontando funções aninhadas:

   ```bash
   node "$AVAL/scripts/g1_typescript.cjs" complexidade \
     --src "$EXC" --inventario "$BRUTOS/inventario.json" \
     --eslint "$BRUTOS/M1.3.1-eslint-bruto.json" --saida "$CONS"
   ```

3. Abrir `M1.3.1-anomalias-para-auditoria.json`. **Não aceitar automaticamente** o consolidado se houver diagnósticos sem correspondência, funções sem diagnóstico, falhas de parsing ou linhas próprias inconsistentes. Em caso de discrepância, auditar o trecho fonte, registrar a correção em planilha e preservar os dados originais. Em particular, o vínculo de avisos ESLint com posições de funções é auxiliar e pode exigir correção humana.
4. Classificar cada função em `1–10`, `11–20`, `21–50` ou `>50` de complexidade. Calcular, **por pacote e no total**, `(linhas próprias da faixa ÷ total de linhas próprias de funções) × 100`. As quatro faixas devem somar aproximadamente **100%** (diferenças apenas de arredondamento); registrar também proporção de funções por faixa e arquivos com mais LOC nas faixas alta/muito alta. **Não usar média de complexidade como indicador**, pois a ficha pede distribuição de LOC.

**Saídas:** `M1.3.1-funcoes-complexidade.csv`, `M1.3.1-resumo.json` e `M1.3.1-anomalias-para-auditoria.json`. **Bruto:** `M1.3.1-eslint-bruto.json` e fonte congelada; **consolidado final:** tabela auditada por pacote e global. O script é um **extrator auxiliar sujeito à validação**, não uma medição já comprovada.

### 5.2. M1.3.2 — Cobertura da documentação para desenvolvedores

**[Ficha M1.3.2](../fase-02/gqm-manutenibilidade.md#m132--cobertura-da-documentação-para-desenvolvedores) · [Faixas de G1](../fase-02/pontuacao-julgamento.md#3-níveis-das-métricas-de-manutenibilidade-g1)**

1. Inspecionar **somente** `README.md`, `CONTRIBUTING.md`, `AGENTS.md` e `dev-docs/docs/` do commit fixado.
2. Criar a planilha de quatro tópicos fixos, sem acrescentar ou remover itens:

   ```bash
   cat > "$BRUTOS/M1.3.2-checklist.csv" <<'CSV'
   topico,presente,caminho-e-secao,evidencia,revisor
   guia_de_contribuicao,,,,
   preparacao_do_ambiente,,,,
   convencoes_de_codigo,,,,
   arquitetura_ou_organizacao,,,,
   CSV
   ```

3. Para cada tópico, procurar um **documento ou seção dedicada**, registrar `presente=sim/nao` e a localização exata:

   ```bash
   cd "$EXC"
   { for F in README.md CONTRIBUTING.md AGENTS.md dev-docs/docs; do
       [ ! -e "$F" ] || grep -RIn --include='*.md' --include='*.mdx' \
         -E 'contribut|develop|setup|install|architect|code style|conven' "$F" || true
     done; } > "$BRUTOS/M1.3.2-localizacoes-candidatas.txt"
   ```

   Uma ocorrência casual de palavra-chave **não conta**; confirmar a presença de instruções reais. Registrar arquivo ausente como fato, não como falha do comando.
4. **Cálculo:** contar `sim`, inteiro de **0 a 4**. A hipótese H1.3.2 depende especificamente da presença dos tópicos 1 e 2, não apenas do total. Registrar `M1.3.2-total-topicos.json` com `topicos_presentes`, `total_topicos: 4` e `hipotese_topicos_1_e_2`; não calcular enquanto houver campo `presente` vazio.

**Saídas:** checklist com quatro decisões e evidências auditáveis, localização de origem e contagem. **Brutos:** `M1.3.2-checklist.csv`, `M1.3.2-localizacoes-candidatas.txt`. **Consolidado:** `M1.3.2-total-topicos.json` com `topicos_presentes`, `total_topicos:4` e `hipotese_topicos_1_e_2`.

### 5.3. M1.3.3 — Verificações estáticas executadas automaticamente

**[Ficha M1.3.3](../fase-02/gqm-manutenibilidade.md#m133--verificações-estáticas-executadas-automaticamente) · [Faixas de G1](../fase-02/pontuacao-julgamento.md#3-níveis-das-métricas-de-manutenibilidade-g1)**

1. Conferir `.github/workflows/lint.yml` **e** os scripts que esse workflow chama no `package.json`:

   ```bash
   cd "$EXC"
   cp .github/workflows/lint.yml "$BRUTOS/M1.3.3-workflow-lint.yml"
   node -e 'const p=require("./package.json");console.log(JSON.stringify(p.scripts,null,2))' \
     > "$BRUTOS/M1.3.3-scripts-package.json"
   ```

2. Confirmar que o fluxo tem gatilho `pull_request`, que cada comando é executado automaticamente para PRs e que existe um script por verificação: **lint**, **formatação** e **verificação de tipos**. No commit examinado, os scripts esperados são `test:code`, `test:other` e `test:typecheck`; ler o corpo real de cada um antes de marcar.
3. Registrar o resultado em CSV:

   ```bash
   cat > "$BRUTOS/M1.3.3-verificacoes.csv" <<'CSV'
   verificacao,executada_por_pr,arquivo-e-comando,evidencia
   lint,,,
   formatacao,,,
   tipos,,,
   CSV
   ```

4. **Cálculo:** `número de verificações confirmadas`, inteiro de **0 a 3**. Contar uma categoria somente uma vez, mesmo se aparecer em vários fluxos. Registrar `M1.3.3-total-verificacoes.json` com `verificacoes_confirmadas` e `total_possivel: 3`; não calcular enquanto houver campo vazio.

**Saída esperada:** tabela com três decisões explícitas. **Brutos:** cópias do workflow e scripts. **Consolidado:** `M1.3.3-total-verificacoes.json` com `verificacoes_confirmadas` e `total_possivel:3`.

## 6. Q1.4 — Modificabilidade

### 6.1. Aquisição comum do histórico de PRs

As métricas M1.4.1, M1.4.3 e M1.5.3 reutilizam uma população única de contribuições integradas ao ramo principal de **18/04/2026 a 18/10/2026**. A leitura da API é feita na Fase 04, com `gh` autenticado, e a lista de PRs deve permanecer identificável por **número e SHA**. Não usar `git log --merges` como substituto: squash merges e diferentes estratégias de integração podem mudar essa contagem.

1. Validar autenticação, registrar contexto e recuperar a busca paginada:

   ```bash
   gh auth status
   gh --version > "$BRUTOS/M1.4.1-gh-versao.txt"
   gh api -X GET search/issues \
     -f q='repo:excalidraw/excalidraw is:pr is:merged base:master merged:2026-04-18..2026-10-18' \
     -f per_page=100 --paginate --slurp \
     > "$BRUTOS/M1.4.1-busca-prs.json"
   ```

2. Verificar `total_count` e eventuais limites da API de busca: **se o total exceder 1.000**, repetir em subintervalos mensais/semanais sem sobreposição e documentar as consultas. A resposta bruta da busca não contém necessariamente a lista completa de arquivos nem os detalhes do último commit.
3. Extrair os números únicos, armazenando a relação de cada PR:

   ```bash
   python3 - "$BRUTOS/M1.4.1-busca-prs.json" "$BRUTOS/prs/numeros.txt" <<'PY'
   import json,sys
   pags=json.load(open(sys.argv[1],encoding='utf-8'))
   items=[i for pagina in pags for i in pagina.get('items',[])]
   n=sorted({int(i['number']) for i in items})
   assert len(n)==len(items), 'Busca truncada ou páginas duplicadas; investigar'
   open(sys.argv[2],'w').write(''.join(f'{x}\n' for x in n))
   print(f'{len(n)} PRs encontrados; conferir total_count e fronteiras da janela')
   PY
   ```

4. Para cada número, salvar metadados completos e **todas** as páginas de arquivos alterados. Conservar resposta por PR, inclusive arquivos removidos ou renomeados:

   ```bash
   while IFS= read -r N; do
     gh api "repos/excalidraw/excalidraw/pulls/$N" \
       > "$BRUTOS/prs/pr-$N.json"
     gh api "repos/excalidraw/excalidraw/pulls/$N/files?per_page=100" \
       --paginate --slurp > "$BRUTOS/prs/pr-$N-files.json"
   done < "$BRUTOS/prs/numeros.txt"
   ```

5. Conferir `merged_at` dentro da janela, `base.ref=master` quando disponível, o autor e o título. **Separar em uma lista de exclusões revisada** PRs automáticos de atualização de dependências e traduções, com justificativa; não excluir silenciosamente todos os PRs de bots nem contar PRs apenas fechados. Registrar conflitos na classificação.

**Saída esperada:** `M1.4.1-busca-prs.json`, `prs/numeros.txt`, `prs/pr-N.json` e `prs/pr-N-files.json`. As consultas podem demandar tempo e respeitam limites de acesso: guardar erros e retomar IDs faltantes sem descartar a população.

### 6.2. M1.4.1 — Mediana de arquivos de produção alterados por contribuição

**[Ficha M1.4.1](../fase-02/gqm-manutenibilidade.md#m141--mediana-de-arquivos-de-produção-alterados-por-contribuição) · [Faixas de G1](../fase-02/pontuacao-julgamento.md#3-níveis-das-métricas-de-manutenibilidade-g1)**

1. Usar a população de PRs auditada na seção 6.1. Em cada `pr-N-files.json`, contar arquivos **de produção** adicionados, modificados ou removidos; ignorar testes, documentação, exemplos e dependências conforme o inventário da seção 2.
2. Registrar `PR`, `merged_at`, `arquivos_producao_alterados`, `excluido`, `justificativa_exclusao`, `fonte_api` em `M1.4.1-contagem-por-pr.csv`. PRs válidos com zero arquivos de produção permanecem na população, pois a ficha define contribuições integradas, não apenas contribuições de código.
3. **Cálculo:** mediana da lista de contagens de arquivos por PR incluído, mantendo valores zero. Para número par de PRs, usar média dos dois valores centrais. Não substituir por média aritmética.
4. Conferir, por amostragem, pelo menos três PRs de contagem alta e três de contagem zero diretamente na resposta salva da API.

**Saída esperada:** lista de contagens por PR e mediana. **Brutos:** JSON de PRs e arquivos. **Consolidados efetivos (gerados após o passo 7.3):** `M1.4.1-M1.4.3-prs.csv` e `M1.4.1-M1.4.3-M1.5.3-resumo.json` (`M1.4.1_mediana_arquivos`).

### 6.3. M1.4.2 — Arquivos de produção extensos

**[Ficha M1.4.2](../fase-02/gqm-manutenibilidade.md#m142--arquivos-de-produção-extensos) · [Faixas de G1](../fase-02/pontuacao-julgamento.md#3-níveis-das-métricas-de-manutenibilidade-g1)**

1. Gerar uma lista de caminhos a partir **somente** de `inventario.json`, e verificar cloc 1.86:

   ```bash
   cd "$EXC"
   cloc --version > "$BRUTOS/M1.4.2-cloc-versao.txt"
   python3 - "$BRUTOS/inventario.json" "$BRUTOS/M1.4.2-arquivos-entrada.txt" <<'PY'
   import json,sys
   inv=json.load(open(sys.argv[1],encoding='utf-8'))
   open(sys.argv[2],'w').write(''.join(x+'\n' for x in inv['producao']))
   PY
   cloc --by-file --json --list-file="$BRUTOS/M1.4.2-arquivos-entrada.txt" \
     > "$BRUTOS/M1.4.2-cloc-bruto.json"
   ```

2. Consolidar e validar que o cloc contou **todos** os arquivos da população:

   ```bash
   python3 "$AVAL/scripts/g1_processar.py" cloc \
     --inventario "$BRUTOS/inventario.json" \
     --cloc "$BRUTOS/M1.4.2-cloc-bruto.json" --saida "$CONS"
   ```

3. **Cálculo:** arquivo extenso é o que tem **mais de 1.000 LOC** (sem brancos nem comentários); contar por pacote e no total. Registrar também percentual sobre todos os arquivos de produção, conforme a faixa de julgamento de G1.

**Saídas:** `M1.4.2-linhas-arquivos.csv` com LOC por arquivo, `M1.4.2-resumo.json` com lista de extensos. **Bruto:** JSON completo do cloc. Não aplicar `wc -l`, pois ele conta linhas em branco e comentários.

### 6.4. M1.4.3 — Proporção de contribuições que alteram arquivos extensos

**[Ficha M1.4.3](../fase-02/gqm-manutenibilidade.md#m143--proporção-de-contribuições-que-alteram-arquivos-extensos) · [Faixas de G1](../fase-02/pontuacao-julgamento.md#3-níveis-das-métricas-de-manutenibilidade-g1)**

1. Usar **a mesma população de PRs de M1.4.1** (com as mesmas exclusões) e a **lista de arquivos extensos M1.4.2**, referente ao commit de 18/10/2026.
2. Para cada PR, buscar a interseção entre seus arquivos de produção alterados e os arquivos extensos. Tratar renomeações com `previous_filename` da API e verificar manualmente a correspondência do nome antigo com o atual; não inferir que uma renomeação mudou o conteúdo quando os dados não a indicam.
3. Salvar, por PR, `alterou_extenso=1/0`, os arquivos coincidentes e a evidência da API.
4. **Cálculo:** `(PRs incluídos que alteraram ≥1 arquivo extenso ÷ todos os PRs incluídos na janela) × 100`. Um PR com cinco arquivos extensos ainda conta apenas **uma vez** no numerador.

**Saída esperada:** tabela por PR e percentual único. **Brutos:** API de PRs + `M1.4.2-cloc-bruto.json`; **consolidados efetivos (gerados após o passo 7.3):** `M1.4.1-M1.4.3-prs.csv` e `M1.4.1-M1.4.3-M1.5.3-resumo.json` (`M1.4.3_percentual_prs_em_extensos`).

## 7. Q1.5 — Testabilidade

### 7.1. M1.5.1 — Cobertura de linhas por pacote

**[Ficha M1.5.1](../fase-02/gqm-manutenibilidade.md#m151--cobertura-de-linhas-por-pacote) · [Faixas de G1](../fase-02/pontuacao-julgamento.md#3-níveis-das-métricas-de-manutenibilidade-g1)**

1. Executar a suíte do commit fixado com o comando **do próprio Excalidraw** e conservar o relatório JSON, mesmo se houver falha de limiar de cobertura:

   ```bash
   cd "$EXC"
   set -o pipefail
   yarn test:coverage --run 2>&1 | tee "$BRUTOS/M1.5.1-testes-cobertura.log"
   # O Vitest do commit define os reporters text, json-summary, json, html e lcovonly.
   test -f coverage/coverage-summary.json || { echo 'Sem coverage-summary.json'; exit 1; }
   cp coverage/coverage-summary.json "$BRUTOS/M1.5.1-coverage-summary.json"
   ```

2. Conferir se `coverage/coverage-summary.json` contém entradas por arquivo (não somente `total`) e se identifica o executável do Excalidraw utilizado. Se houver arquivo de produção ausente, registrar o motivo e a regra de inclusão/exclusão da cobertura; **não presumir que falta de relatório equivale a 0%**.
3. Agregar, por pacote, os **numeradores e denominadores de linhas** antes de calcular o percentual:

   ```bash
   python3 "$AVAL/scripts/g1_processar.py" cobertura \
     --inventario "$BRUTOS/inventario.json" \
     --cobertura "$BRUTOS/M1.5.1-coverage-summary.json" --saida "$CONS"
   ```

4. **Cálculo:** `(soma de linhas executadas ÷ soma de linhas executáveis) × 100`, por pacote e no total; conferir separadamente biblioteca `excalidraw` e aplicação `excalidraw-app`, conforme H1.5.1. **Nunca tirar média simples dos percentuais de arquivos**. A ausência de pacotes no relatório exige análise e eventual registro de métrica não coletável.

**Saídas:** `M1.5.1-cobertura-pacotes.csv` e `M1.5.1-arquivos-nao-reportados.json`. **Brutos:** relatório completo JSON, log do Vitest, versões e configuração `vitest.config.mts`.

### 7.2. M1.5.2 — Distribuição dos testes por nível

**[Ficha M1.5.2](../fase-02/gqm-manutenibilidade.md#m152--distribuição-dos-testes-por-nível) · [Faixas de G1](../fase-02/pontuacao-julgamento.md#3-níveis-das-métricas-de-manutenibilidade-g1)**

1. Ler `inventario.json` e gerar a planilha inicial de **suítes** de teste, não de arquivos auxiliares:

   ```bash
   python3 "$AVAL/scripts/g1_processar.py" testes \
     --inventario "$BRUTOS/inventario.json" --src "$EXC" \
     --out "$BRUTOS/M1.5.2-classificacao-auditar.csv"
   ```

2. Para cada suíte, consultar os imports/chamadas e atribuir **exatamente uma classe** segundo a ficha:
   - **Integração:** usa de fato a função `render` dos utilitários do editor, renderizando componentes.
   - **Ponta a ponta:** usa ferramenta que controla navegador real (Playwright, Cypress ou Puppeteer), se houver.
   - **Unitário:** demais suítes.

   A classificação automática é apenas sugestão; um `render` mencionado em comentário ou um `test-utils` importado sem renderização **não bastam**. Se houver sobreposição, a ordem de precedência é ponta a ponta → integração → unitário, conforme natureza efetiva da suíte.
3. Preencher manualmente `classe_confirmada`, `evidencia` (chamada/import e linha) e `revisor` para **todas** as linhas; não deixar classes em branco.
4. Consolidar:

   ```bash
   python3 "$AVAL/scripts/g1_processar.py" testes-resumo \
     --planilha "$BRUTOS/M1.5.2-classificacao-auditar.csv" \
     --out "$CONS/M1.5.2-distribuicao.json"
   ```

5. **Cálculo:** `(número de suítes no nível ÷ total de suítes) × 100`, separadamente por nível. Os percentuais devem somar **100%**. A hipótese H1.5.2 compara unitário + integração com 50%, segundo a regra da Fase 2.

**Saídas:** planilha revisada e `M1.5.2-distribuicao.json`. **Brutos:** inventário de suítes, trechos de código e CSV auditado. **Consolidado:** totais e percentuais dos três níveis.

### 7.3. M1.5.3 — Contribuições com testes executados antes da integração

**[Ficha M1.5.3](../fase-02/gqm-manutenibilidade.md#m153--proporção-de-contribuições-com-testes-executados-antes-da-integração) · [Faixas de G1](../fase-02/pontuacao-julgamento.md#3-níveis-das-métricas-de-manutenibilidade-g1)**

Esta métrica exige evidência de **execução da etapa `Test Coverage` antes do merge**, e não apenas a existência do workflow ou um check genérico. **`success` ou `failure` da etapa contam como executada**; `skipped`, `cancelled`, não executada, ou etapa encerrada após o merge, não contam. PR sem evidência suficiente é reportado à parte e excluído do denominador, conforme a ficha.

1. Reutilizar a mesma relação de PRs e os metadados completos da seção 6.1. **Não substituir o último SHA do PR por SHA de merge**, porque podem ser diferentes.
2. Para cada PR, obter as execuções do workflow **`test-coverage-pr.yml`** para o último `head.sha` registrado no PR. Salvar a resposta bruta (não guardar somente a conclusão):

   ```bash
   while IFS= read -r N; do
     SHA=$(python3 - "$BRUTOS/prs/pr-$N.json" <<'PY'
   import json,sys
   print(json.load(open(sys.argv[1],encoding='utf-8'))['head']['sha'])
   PY
   )
     gh api -X GET "repos/excalidraw/excalidraw/actions/workflows/test-coverage-pr.yml/runs" \
       -f head_sha="$SHA" -f per_page=100 --paginate --slurp \
       > "$BRUTOS/prs/pr-$N-runs.json"
   done < "$BRUTOS/prs/numeros.txt"
   ```

3. Para **cada** `workflow_runs[].id` associado ao SHA e evento `pull_request`, guardar os detalhes e os **passos dos jobs**. Exemplo para uma execução com ID `RUN_ID`:

   ```bash
   gh api "repos/excalidraw/excalidraw/actions/runs/RUN_ID/jobs?per_page=100" \
     --paginate --slurp > "$BRUTOS/prs/pr-N-run-RUN_ID-jobs.json"
   ```

   Para percorrer **automaticamente todas** as execuções retornadas, substituindo `N` e `RUN_ID` sem digitação manual, use:

   ```bash
   python3 - "$BRUTOS/prs" <<'PY' > "$BRUTOS/prs/runs-identificados.tsv"
   import json,pathlib,sys
   root=pathlib.Path(sys.argv[1]);
   for f in sorted(root.glob('pr-*-runs.json')):
       n=f.name.split('-')[1]
       data=json.load(f.open(encoding='utf-8'))
       for page in data:
           for run in page.get('workflow_runs',[]):
               if run.get('event')=='pull_request':
                   print(f"{n}\t{run['id']}")
   PY
   while IFS=$'\t' read -r N RUN_ID; do
     gh api "repos/excalidraw/excalidraw/actions/runs/$RUN_ID/jobs?per_page=100" \
       --paginate --slurp > "$BRUTOS/prs/pr-$N-run-$RUN_ID-jobs.json"
   done < "$BRUTOS/prs/runs-identificados.tsv"
   ```

   A API pode retornar trabalhos posteriores ao merge: eles não contam. A inexistência de um run não comprova que testes foram ignorados; registrar `sem_evidencia`.
4. Construir a tabela auditável de PRs usando o script fornecido, após obter todos os JSONs:

   ```bash
   python3 "$AVAL/scripts/g1_preparar_prs.py" \
     --pasta-brutos "$BRUTOS" --out "$BRUTOS/prs-auditar.json"
   ```

5. Editar **cada** objeto de `prs-auditar.json`: preencher `excluir=true/false` e `justificativa_exclusao` quando necessário; conferir `ci_status` (`executado`, `nao_executado` ou `sem_evidencia`) e as evidências de `Test Coverage` e `completed_at`. O script sugere a classificação apenas quando os jobs estão presentes; o segundo avaliador valida os casos de evidência insuficiente ou temporalmente ambígua.
6. Consolidar as três métricas históricas **com a mesma população revisada** e a lista de extensos de M1.4.2:

   ```bash
   python3 "$AVAL/scripts/g1_processar.py" historico \
     --prs "$BRUTOS/prs-auditar.json" \
     --extensos "$CONS/M1.4.2-resumo.json" --saida "$CONS"
   ```

7. **Cálculo:** `(PRs incluídos com `Test Coverage` efetivamente executado e concluído antes do merge ÷ PRs incluídos com evidência suficiente) × 100`. Informar explicitamente **o número de PRs sem evidência**. Verificar que `M1.4.1-M1.4.3-M1.5.3-resumo.json` registra também a mediana de M1.4.1 e o percentual M1.4.3.

**Saídas:** `M1.5.3-ci-prs.csv` e `M1.4.1-M1.4.3-M1.5.3-resumo.json`. **Brutos:** respostas API das execuções e jobs, metadados de PR e planilha JSON auditada. A coleta pode demandar muitas consultas: registrar erros e **não pontuar com amostra incompleta**.

## 8. Formulário e conferência das evidências

### 8.1 Modelo de registro por métrica

Criar para cada métrica um registro `.md` ou linha de planilha em `dados/fase-04/brutos/g1/` com os campos abaixo:

| Campo | Conteúdo obrigatório |
| :--- | :--- |
| Métrica/questão | Código `M1.x.y` e `Q1.x` |
| Avaliador | Nome do responsável pela coleta |
| Data/hora | `AAAA-MM-DD HH:MM`, com fuso; data de consulta à API quando houver |
| Linha de base | SHA completo `e1b7aacb356a492aa1e0fc6eb57b8896124027f0` |
| Janela histórica | `18/04/2026–18/10/2026`, se aplicável |
| Ferramentas | Nome, versão, configuração/opções, `node`/`yarn`/sistema operacional |
| Rede/navegador | Estado de conexão e navegador/versão quando necessários; senão `não se aplica` |
| Comando/ações | Comando exato e ordem de execução, sem tokens ou segredos |
| Entrada | Caminhos e total de arquivos/PRs/funções/suítes analisados |
| Saída bruta | Caminhos dos JSONs, CSVs ou logs preservados |
| Cálculo | Fórmula da [ficha G1](../fase-02/gqm-manutenibilidade.md) com numerador e denominador |
| Valor e unidade | Contagem, percentual, mediana ou vetor por pacote, conforme a ficha |
| Hipótese | `confirmada`, `refutada` ou `não avaliável`, com condição da ficha |
| Pontuação | Aplicar posteriormente a [seção 3 de pontuação](../fase-02/pontuacao-julgamento.md#3-níveis-das-métricas-de-manutenibilidade-g1), sem alterar limites |
| Fatores de variação | Falhas, arquivos sem parse, PRs sem evidência, ajustes manuais e justificativas |
| Verificador | Responsável pela checagem independente (#114), com data e divergências |

**Persistência:** nunca salvar tokens `gh auth`, senhas, valores pessoais ou outros segredos nos logs. Manter arquivos de entrada brutos imutáveis, salvar correções e classificações revisadas em arquivos separados e registrar as revisões na mesma evidência.

### 8.2 Inspeções obrigatórias antes da Fase 04

| Validação | Condição de aceite |
| :--- | :--- |
| Escopo | `inventario.json` abrange os pacotes e aplicação, com exclusões corretas |
| Grafo | Importações resolvidas e **valor**, não apenas tipo; cobertura e arestas suspeitas auditadas |
| Complexidade | Todas as mensagens de `complexity` relacionadas a funções, LOC própria auditada e percentuais por pacote/global |
| Documentação | Cada decisão manual aponta arquivo e seção verificáveis |
| Histórico | PRs na janela fechada, exclusões justificadas, paginação completa e dados de API preservados |
| Testes | Suítes classificadas sem sobreposição e relatório Vitest por pacote, com faltantes tratados |
| CI | Evidência de passo `Test Coverage` e `completed_at < merged_at`; perdas explicitadas |
| Consistência | Fórmulas, hipóteses e faixas idênticas às da Fase 02 |

Na [issue #103](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/103), um integrante que **não escreveu este procedimento** deve executar pelo menos uma métrica de G1 a partir deste roteiro e registrar dúvidas, comandos corrigidos e o resultado em ata. Na [issue #114](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/114), outro integrante confirma amostra, saída, cálculo e pontuação. **Divergência não é corrigida sem registro.**

## 9. Limitações conhecidas e tratamento de falhas

1. O detector de importações do Madge usa análise estática e pode omitir resolução dinâmica ou importações de tipo sem sintaxe explícita. **Amostra incompleta invalida a conclusão sem ressalva**; revisar com o código do commit.
2. A análise de complexidade extrai avisos ESLint e usa posições de funções da AST para estimar LOC própria. Blocos complexos e localização dos avisos podem gerar correspondências ambíguas; o resultado precisa de **auditoria e eventual ajuste** antes de aplicar a pontuação.
3. O extrator AST de M1.2.1 produz **candidatos**, não classificação definitiva. Usos de `window`/`document` em variáveis locais e acessos sem a notação `.` devem ser conferidos.
4. API GitHub: limite de busca, rate limit, permissões e retenção de logs de Actions podem reduzir evidências históricas. Não classificar automaticamente uma execução ausente como falha conhecida: distinguir **sem evidência** de **não executado**.
5. Caso uma métrica não seja coletável, registrar justificativa, cobertura da população e efeito sobre denominadores. Seguir a regra da [Fase 02 para métricas ausentes](../fase-02/pontuacao-julgamento.md#61-métricas-não-coletadas); não criar zeros artificiais.
6. Todas as operações de coleta e os scripts auxiliares são **propostos e fornecidos**, não declarados como já executados em produção. Seus resultados oficiais devem ser obtidos no ambiente fixado e validados na Fase 04.

## Referências

- [GQM de Manutenibilidade (G1)](../fase-02/gqm-manutenibilidade.md), seções 2–9, inclusive definições, fontes, cálculos, hipóteses e verificações.
- [Níveis de pontuação e critérios de julgamento](../fase-02/pontuacao-julgamento.md), seções 3, 6 e 7.
- [Recursos e ambiente de avaliação](./recursos-ambiente.md), ferramentas e versões fixadas.
- [Cronograma de avaliação](./cronograma-avaliacao.md), coleta prevista de 10 a 12/11/2026.
- [Issue #95 — Método de avaliação](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/95), justificativas por métrica.
- AULA A07 QSW1 PROC AVAL PRODUTO. Material da disciplina, p. 18–19.
- AULA 08 QSW1 GQM. Material da disciplina, p. 45, 50–51.
- ISO/IEC 25010:2023 — Modelo de qualidade do produto; ISO/IEC 25040 — Processo de avaliação.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 08/11/2026 | Elaboração do roteiro operacional de coleta e evidências de todas as 14 métricas G1, com auxiliares para processamento | [Davi Pierre](https://github.com/DaviPierre) |  |
