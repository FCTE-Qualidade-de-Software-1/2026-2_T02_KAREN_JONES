---
sidebar_position: 3
title: Instruções para o avaliador de Manutenibilidade (G1)
description: Passo a passo de obtenção das 14 métricas de Manutenibilidade (G1) na Fase 04, com pré-condições, comandos, saídas esperadas, cálculo e nome de cada dado bruto.
---

import Link from '@docusaurus/Link';

# Instruções para o avaliador de Manutenibilidade (G1)

## Introdução

O plano de avaliação reúne o método, a instrução para o avaliador, os recursos e o cronograma [[1, p. 19]](#ref-1), e deve permitir que o avaliador execute a avaliação completamente [[1, p. 18]](#ref-1). A coleta manual deve identificar quem coletou o dado [[2, p. 51]](#ref-2).

O objetivo desta página é dar o passo a passo para que qualquer integrante obtenha, no commit avaliado, o mesmo valor das 14 métricas de [G1](../fase-02/gqm-manutenibilidade.md).

## Metodologia

Cada métrica segue o procedimento de coleta da sua ficha na Fase 02 e o método definido no [método de avaliação](./metodo-avaliacao.md#21-g1-manutenibilidade). As populações (pacotes, pacotes de base, código de produção, código de teste, janela histórica e contribuição integrada) são as das [convenções de coleta de G1](../fase-02/gqm-manutenibilidade.md#2-convenções-de-coleta), e as versões das ferramentas são as dos [recursos](./recursos-ambiente.md#5-ferramentas-de-análise-e-suas-versões). Os valores são convertidos em nível pelas [faixas de G1](../fase-02/pontuacao-julgamento.md#3-níveis-das-métricas-de-manutenibilidade-g1).

Para cada métrica, a página traz os comandos com a saída esperada, o nome do dado bruto e a regra de cálculo. O cálculo é feito a partir dos dados brutos na verificação da [#114](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/114), e por isso esta página não grava valores em `dados/fase-04/consolidados/`.

---

## 1. Preparação

Os comandos usam Bash no Linux ou no WSL2, a partir da raiz do repositório da avaliação. Todos os dados brutos ficam em `dados/fase-04/brutos/`, com nomes no formato `M<código>_<identificador>.<extensão>`, como nas [instruções de G3](./instrucoes-g3-flexibilidade.md#22-local-e-padrão-de-nomenclatura-dos-dados-brutos). Um arquivo usado por mais de uma métrica leva o código da primeira que o gera.

```bash
set -o pipefail
export BRUTOS="$PWD/dados/fase-04/brutos"
export EXC="$HOME/excalidraw-avaliado"
mkdir -p "$BRUTOS"

git clone https://github.com/excalidraw/excalidraw.git "$EXC"
git -C "$EXC" checkout e1b7aacb356a492aa1e0fc6eb57b8896124027f0
git -C "$EXC" rev-parse HEAD

cd "$EXC"
yarn --frozen-lockfile

find packages excalidraw-app \
  \( -name node_modules -o -name tests -o -name __snapshots__ -o -name examples \) -prune \
  -o -type f \( -name '*.ts' -o -name '*.tsx' \) \
  ! -name '*.test.ts' ! -name '*.test.tsx' ! -name '*.d.ts' -print \
  | sort > "$BRUTOS/M1.1.1_arquivos-producao.txt"
```

**Saída esperada:** `git rev-parse HEAD` mostra `e1b7aacb356a492aa1e0fc6eb57b8896124027f0`, a instalação termina sem erro e `M1.1.1_arquivos-producao.txt` lista os arquivos de produção de todos os pacotes. Se o commit for outro ou a instalação falhar, a coleta para e o desvio é registrado.

Cada métrica tem um registro `M<código>_fatores.md`, com os campos da [seção 9 dos recursos](./recursos-ambiente.md#9-fatores-de-variação-registrados-em-cada-coleta). Em G1, as métricas de histórico (M1.4.1, M1.4.3 e M1.5.3) registram também a data e a hora da consulta à API.

---

## 2. Q1.1: Modularidade

### 2.1 Grafo de importações

M1.1.1, M1.1.2, M1.1.3 e M1.2.1 usam o mesmo grafo de importações de valor entre arquivos. O arquivo `.madgerc` é temporário e só existe durante a execução, para não alterar o repositório avaliado.

```bash
cd "$EXC"
test ! -e .madgerc || { echo "Já existe .madgerc no checkout"; exit 1; }
cat > .madgerc <<'JSON'
{
  "fileExtensions": ["ts", "tsx"],
  "excludeRegExp": ["(^|/)tests/", "(^|/)__snapshots__/", "(^|/)examples/", "\\.test\\.tsx?$", "\\.d\\.ts$"],
  "detectiveOptions": {
    "ts": { "skipTypeImports": true, "mixedImports": true },
    "tsx": { "skipTypeImports": true, "mixedImports": true }
  }
}
JSON
npx --yes madge@8.0.0 --json --no-spinner --basedir . --ts-config tsconfig.json \
  --extensions ts,tsx packages excalidraw-app \
  > "$BRUTOS/M1.1.1_grafo-madge.json" 2> "$BRUTOS/M1.1.1_madge-avisos.log"
rm .madgerc
```

**Saída esperada:** um JSON em que cada chave é um arquivo de produção e o valor é a lista de arquivos que ele importa. As chaves devem ser os mesmos arquivos de `M1.1.1_arquivos-producao.txt`. Os arquivos que faltarem e os avisos de importações não resolvidas vão para o registro de fatores, com o efeito no valor.

### 2.2 M1.1.1: ciclos de dependência entre pacotes

[Ficha M1.1.1](../fase-02/gqm-manutenibilidade.md#m111--ciclos-de-dependência-entre-pacotes)

**Dado bruto:** `M1.1.1_grafo-madge.json`, da seção 2.1.

**Cálculo:** trocar cada arquivo pelo seu pacote (`packages/<nome>/` ou `excalidraw-app/`) e descartar as arestas dentro de um mesmo pacote. O valor é o número de pares de pacotes A e B em que A alcança B e B alcança A, direta ou indiretamente. Cada par conta uma vez. A opção `madge --circular` não serve, porque lista ciclos entre arquivos e não entre pacotes.

### 2.3 M1.1.2: importações que violam a direção declarada

[Ficha M1.1.2](../fase-02/gqm-manutenibilidade.md#m112--importações-que-violam-a-direção-declarada)

Copiar a regra de lint do commit:

```bash
cp "$EXC/packages/eslintrc.base.json" "$BRUTOS/M1.1.2_eslintrc-base.json"
```

**Dados brutos:** `M1.1.1_grafo-madge.json` e `M1.1.2_eslintrc-base.json`.

**Cálculo:** número de arestas, de arquivo de origem para arquivo de destino, que se enquadram em uma das duas condições: origem em um pacote de base e destino em `packages/excalidraw/`, ou destino em `excalidraw-app/` a partir de qualquer pacote.

### 2.4 M1.1.3: acoplamento e instabilidade de cada pacote

[Ficha M1.1.3](../fase-02/gqm-manutenibilidade.md#m113--acoplamento-e-instabilidade-de-cada-pacote)

**Dado bruto:** `M1.1.1_grafo-madge.json`, agregado por pacote como em M1.1.1.

**Cálculo:** para cada pacote P, Ca é o número de outros pacotes distintos que importam P e Ce é o número de pacotes distintos que P importa. A instabilidade é `I = Ce / (Ca + Ce)`. Quando `Ca + Ce = 0`, o valor é registrado como não aplicável, e não como zero.

---

## 3. Q1.2: Reusabilidade

### 3.1 M1.2.1: arquivos de pacotes de base com dependência de React ou do navegador

[Ficha M1.2.1](../fase-02/gqm-manutenibilidade.md#m121--arquivos-de-pacotes-de-base-com-dependência-de-react-ou-do-navegador)

1. Buscar com `grep`, em todo o código de produção, as importações de `react` e `react-dom` e os usos de `window.` e `document.`:

   ```bash
   cd "$EXC"
   xargs grep -nHE "from ['\"]react(-dom)?(/[^'\"]*)?['\"]|require\(['\"]react(-dom)?['\"]|(^|[^.[:alnum:]_])(window|document)\." \
     < "$BRUTOS/M1.1.1_arquivos-producao.txt" > "$BRUTOS/M1.2.1_ocorrencias-grep.txt"
   ```

2. Revisar cada linha encontrada e registrar em `M1.2.1_arquivos-diretos.csv`, com as colunas `arquivo,linha,valida,motivo`. A ocorrência é válida quando é uma importação de valor ou um uso real do global. Ficam de fora os comentários, as strings e as importações `import type`.
3. Marcar no grafo de M1.1.1 os arquivos com ao menos uma ocorrência válida.

**Dados brutos:** `M1.2.1_ocorrencias-grep.txt`, `M1.2.1_arquivos-diretos.csv` e `M1.1.1_grafo-madge.json`.

**Cálculo:** para cada pacote de base, o número de arquivos com dependência direta (marcados) e o número de arquivos que só alcançam um arquivo marcado pelo grafo, separados. A proporção é `(diretos + transitivos) / arquivos de produção do pacote × 100`.

### 3.2 M1.2.2: proporção de propriedades públicas documentadas

[Ficha M1.2.2](../fase-02/gqm-manutenibilidade.md#m122--proporção-de-propriedades-públicas-documentadas)

1. Copiar a declaração de `ExcalidrawProps`:

   ```bash
   cd "$EXC"
   sed -n '/^export interface ExcalidrawProps/,/^}/p' packages/excalidraw/types.ts \
     > "$BRUTOS/M1.2.2_excalidraw-props.ts"
   ```

2. Listar cada propriedade de primeiro nível em `M1.2.2_propriedades.csv`, com as colunas `propriedade,documentada,arquivo-e-secao,trecho`.
3. Para cada propriedade, procurar o nome nas páginas da API, por exemplo `grep -rn "onChange" dev-docs/docs/@excalidraw/excalidraw/api/`, e preencher `documentada` com `sim` só se houver uma descrição do propósito. O caminho e o trecho que comprovam ficam na mesma linha.

**Dados brutos:** `M1.2.2_excalidraw-props.ts` e `M1.2.2_propriedades.csv`.

**Cálculo:** `(propriedades com documentada = sim / total de propriedades) × 100`.

---

## 4. Q1.3: Analisabilidade

### 4.1 M1.3.1: perfil de risco de complexidade das funções

[Ficha M1.3.1](../fase-02/gqm-manutenibilidade.md#m131--perfil-de-risco-de-complexidade-das-funções) e [faixas de M1.3.1](../fase-02/pontuacao-julgamento.md#31-faixas-de-m131)

1. Executar o ESLint do commit com a regra `complexity` em limite 0, para que todas as funções sejam informadas:

   ```bash
   cd "$EXC"
   ./node_modules/.bin/eslint --format json --rule 'complexity: [error, 0]' \
     --ext .ts,.tsx packages excalidraw-app \
     > "$BRUTOS/M1.3.1_eslint.json" 2> "$BRUTOS/M1.3.1_eslint-erros.log"
   ```

   O código de saída 1 é esperado, porque toda função viola o limite 0. Erros de análise no arquivo de erros são registrados no formulário de fatores.

**Dados brutos:** `M1.3.1_eslint.json` e `M1.1.1_arquivos-producao.txt`.

**Cálculo:**

1. Considerar só as mensagens `ruleId = complexity` de arquivos da lista de produção e descartar as que começam com `Class field initializer`, que são os inicializadores de campos de classe.
2. Para cada função, contar as linhas próprias entre `line` e `endLine` que não estão em branco nem são comentário, descontando as linhas das funções declaradas dentro dela.
3. Classificar cada função nas faixas 1 a 10, 11 a 20, 21 a 50 e acima de 50.
4. Para cada faixa, calcular `(linhas próprias das funções da faixa / linhas próprias de todas as funções) × 100`, por pacote e no total.
5. Registrar também o percentual de funções em cada faixa e os arquivos com mais linhas nas duas faixas mais altas.

### 4.2 M1.3.2: cobertura da documentação para desenvolvedores

[Ficha M1.3.2](../fase-02/gqm-manutenibilidade.md#m132--cobertura-da-documentação-para-desenvolvedores)

1. Inspecionar `README.md`, `CONTRIBUTING.md` e `AGENTS.md` da raiz e as páginas de `dev-docs/docs/` no commit.
2. Preencher `M1.3.2_lista-verificacao.csv` com as colunas `topico,presente,arquivo-e-secao` e uma linha para cada tópico: guia de contribuição, preparação do ambiente, convenções de código e arquitetura ou organização do código. O tópico só está presente se houver um documento ou uma seção dedicada a ele.

**Dado bruto:** `M1.3.2_lista-verificacao.csv`.

**Cálculo:** número de tópicos presentes, de 0 a 4.

### 4.3 M1.3.3: verificações estáticas executadas automaticamente

[Ficha M1.3.3](../fase-02/gqm-manutenibilidade.md#m133--verificações-estáticas-executadas-automaticamente)

1. Listar os fluxos que mencionam `pull_request` e copiar cada um, junto com os scripts do `package.json`:

   ```bash
   cd "$EXC"
   grep -lw pull_request .github/workflows/*.yml > "$BRUTOS/M1.3.3_fluxos-pull-request.txt"
   while read -r F
   do
     cp "$F" "$BRUTOS/M1.3.3_$(basename "$F")"
   done < "$BRUTOS/M1.3.3_fluxos-pull-request.txt"
   cp package.json "$BRUTOS/M1.3.3_package.json"
   ```

2. Abrir cada fluxo copiado, confirmar que `pull_request` está no bloco `on:` e seguir os scripts que ele chama no `package.json`, como `test:code`, `test:other` e `test:typecheck`.
3. Preencher `M1.3.3_verificacoes.csv` com as colunas `verificacao,presente,fluxo,script` e uma linha para lint, formatação e verificação de tipos.

**Dados brutos:** `M1.3.3_fluxos-pull-request.txt`, as cópias `M1.3.3_<fluxo>.yml`, `M1.3.3_package.json` e `M1.3.3_verificacoes.csv`.

**Cálculo:** número de verificações presentes em algum fluxo disparado por `pull_request`, de 0 a 3. Uma verificação que aparece em vários fluxos conta uma vez.

---

## 5. Q1.4: Modificabilidade

### 5.1 Histórico de pull requests

M1.4.1, M1.4.3 e M1.5.3 usam a mesma população de contribuições integradas na janela de 18/04/2026 a 18/10/2026.

```bash
gh pr list --repo excalidraw/excalidraw --state merged --base master \
  --search "merged:2026-04-18..2026-10-18" --limit 1000 \
  --json number,title,author,mergedAt,headRefOid > "$BRUTOS/M1.4.1_prs.json"

node -e 'for (const p of require(process.argv[1])) console.log(p.number)' "$BRUTOS/M1.4.1_prs.json" |
while read -r N
do
  gh api "repos/excalidraw/excalidraw/pulls/$N/files?per_page=100" --paginate --slurp \
    > "$BRUTOS/M1.4.1_pr-$N-arquivos.json"
done
```

**Saída esperada:** `M1.4.1_prs.json` com um item por *pull request* e um `M1.4.1_pr-<N>-arquivos.json` para cada um. Se a lista tiver 1.000 itens, o limite da busca foi atingido, e a consulta é repetida por mês, sem sobreposição de datas.

Os *pull requests* automáticos de atualização de dependências e de traduções vão para `M1.4.1_exclusoes.csv`, com as colunas `numero,motivo`, e são contados à parte.

### 5.2 M1.4.1: mediana de arquivos de produção alterados por contribuição

[Ficha M1.4.1](../fase-02/gqm-manutenibilidade.md#m141--mediana-de-arquivos-de-produção-alterados-por-contribuição)

**Dados brutos:** os da seção 5.1, `M1.4.1_prs.json`, `M1.4.1_pr-<N>-arquivos.json` e `M1.4.1_exclusoes.csv`.

**Cálculo:** para cada *pull request* não excluído, contar os arquivos alterados (adicionados, modificados, renomeados ou removidos) que são de produção pelas convenções de G1. O valor é a mediana dessas contagens, mantendo os zeros. Com número par de *pull requests*, a mediana é a média dos dois valores centrais.

### 5.3 M1.4.2: arquivos de produção extensos

[Ficha M1.4.2](../fase-02/gqm-manutenibilidade.md#m142--arquivos-de-produção-extensos)

1. Contar as linhas de cada arquivo de produção:

   ```bash
   cd "$EXC"
   cloc --by-file --json --list-file="$BRUTOS/M1.1.1_arquivos-producao.txt" \
     > "$BRUTOS/M1.4.2_cloc.json"
   ```

2. Conferir se o número de arquivos do JSON é igual ao de `M1.1.1_arquivos-producao.txt`. Arquivos que o cloc não reconhecer vão para o registro de fatores.

**Dado bruto:** `M1.4.2_cloc.json`.

**Cálculo:** arquivo extenso é o que tem mais de 1.000 linhas no campo `code`, que já exclui linhas em branco e comentários. O valor é o número de arquivos extensos por pacote e no total, com a lista dos arquivos e a proporção sobre os arquivos de produção.

### 5.4 M1.4.3: proporção de contribuições que alteram arquivos extensos

[Ficha M1.4.3](../fase-02/gqm-manutenibilidade.md#m143--proporção-de-contribuições-que-alteram-arquivos-extensos)

**Dados brutos:** os de M1.4.1, com as mesmas exclusões, e `M1.4.2_cloc.json`.

**Cálculo:**

1. Montar o mapa de renomeações a partir dos arquivos com `status = renamed` de todos os *pull requests*, de `previous_filename` para `filename`, e aplicá-lo em sequência até chegar ao nome que o arquivo tem no commit avaliado.
2. Em cada *pull request*, levar cada arquivo alterado ao nome atual pelo mapa antes de comparar com a lista de extensos.
3. O valor é `(pull requests que alteram ao menos um arquivo extenso / pull requests incluídos) × 100`. Um *pull request* que altera vários arquivos extensos conta uma vez.

---

## 6. Q1.5: Testabilidade

### 6.1 M1.5.1: cobertura de linhas por pacote

[Ficha M1.5.1](../fase-02/gqm-manutenibilidade.md#m151--cobertura-de-linhas-por-pacote)

1. Executar a suíte com o comando do próprio projeto e copiar o relatório:

   ```bash
   cd "$EXC"
   yarn test:coverage --run 2>&1 | tee "$BRUTOS/M1.5.1_testes.log"
   cp coverage/coverage-summary.json "$BRUTOS/M1.5.1_coverage-summary.json"
   ```

2. Conferir se o relatório tem uma entrada por arquivo, além de `total`. Os arquivos de produção ausentes do relatório vão para o registro de fatores, sem serem tratados como 0%.

**Dados brutos:** `M1.5.1_coverage-summary.json` e `M1.5.1_testes.log`.

**Cálculo:** para cada pacote, `(soma de lines.covered / soma de lines.total) × 100` sobre os arquivos de produção do pacote, e o mesmo cálculo no total. A média dos percentuais dos arquivos não é usada.

### 6.2 M1.5.2: distribuição dos testes por nível

[Ficha M1.5.2](../fase-02/gqm-manutenibilidade.md#m152--distribuição-dos-testes-por-nível)

1. Listar as suítes de todos os pacotes, inclusive as de `excalidraw-app/tests/`, e buscar as chamadas que definem cada nível:

   ```bash
   cd "$EXC"
   find packages excalidraw-app -name node_modules -prune \
     -o -type f \( -name '*.test.ts' -o -name '*.test.tsx' \) -print \
     | sort > "$BRUTOS/M1.5.2_suites.txt"
   xargs grep -nHE "\brender\(|from ['\"](@playwright/test|playwright|cypress|puppeteer)['\"]" \
     < "$BRUTOS/M1.5.2_suites.txt" > "$BRUTOS/M1.5.2_ocorrencias-grep.txt"
   grep -nE '"(@playwright/test|playwright|cypress|puppeteer)"' \
     package.json packages/*/package.json excalidraw-app/package.json \
     > "$BRUTOS/M1.5.2_ferramentas-e2e.txt"
   ```

2. Preencher `M1.5.2_classificacao.csv` com as colunas `suite,nivel,evidencia` e uma linha por suíte. A suíte é de ponta a ponta se controla um navegador real, de integração se chama a função `render` dos utilitários de teste e unitária nos demais casos. Quando houver mais de um sinal, vale essa ordem. Um `render` em comentário não conta.

**Dados brutos:** `M1.5.2_suites.txt`, `M1.5.2_ocorrencias-grep.txt`, `M1.5.2_ferramentas-e2e.txt` e `M1.5.2_classificacao.csv`.

**Cálculo:** para cada nível, `(suítes do nível / total de suítes) × 100`. Os três percentuais somam 100%.

### 6.3 M1.5.3: proporção de contribuições com testes executados antes da integração

[Ficha M1.5.3](../fase-02/gqm-manutenibilidade.md#m153--proporção-de-contribuições-com-testes-executados-antes-da-integração)

1. Para cada *pull request* da seção 5.1, buscar as execuções de `test-coverage-pr.yml` sobre o último commit (`headRefOid`) e os passos de cada execução:

   ```bash
   node -e 'for (const p of require(process.argv[1])) console.log(p.number, p.headRefOid)' "$BRUTOS/M1.4.1_prs.json" |
   while read -r N SHA
   do
     gh api -X GET repos/excalidraw/excalidraw/actions/workflows/test-coverage-pr.yml/runs \
       -f head_sha="$SHA" -f per_page=100 > "$BRUTOS/M1.5.3_pr-$N-execucoes.json"
     node -e 'for (const r of require(process.argv[1]).workflow_runs) console.log(r.id)' "$BRUTOS/M1.5.3_pr-$N-execucoes.json" |
     while read -r RUN
     do
       gh api "repos/excalidraw/excalidraw/actions/runs/$RUN/jobs?per_page=100" \
         > "$BRUTOS/M1.5.3_execucao-$RUN-jobs.json"
     done
   done
   ```

**Dados brutos:** `M1.4.1_prs.json`, `M1.5.3_pr-<N>-execucoes.json` e `M1.5.3_execucao-<id>-jobs.json`.

**Cálculo:**

1. Um *pull request* está verificado se, em alguma execução, o passo `Test Coverage` tem conclusão `success` ou `failure` e `completed_at` anterior (`<`) a `mergedAt`. As conclusões `skipped` e `cancelled` e a ausência do passo não contam.
2. Os *pull requests* sem execução ou sem os passos disponíveis ficam sem evidência. Eles saem do denominador e são informados à parte.
3. O valor é a razão entre os *pull requests* verificados e os *pull requests* incluídos com evidência, vezes 100.

---

## Referências

> <Link id="ref-1">1.</Link> RAMOS, Cristiane Soares. **AULA A07 QSW1 PROC AVAL PRODUTO**. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Páginas 18 e 19. Disponível no Moodle da disciplina.

> <Link id="ref-2">2.</Link> RAMOS, Cristiane Soares. **AULA 08 QSW1 GQM**. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Página 51. Disponível no Moodle da disciplina.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 08/11/2026 | Elaboração do roteiro operacional de coleta e evidências de todas as 14 métricas G1, com auxiliares para processamento | [Davi Pierre](https://github.com/DaviPierre) |  |
| 1.1 | 10/11/2026 | Ajustes da revisão da PR #149: comandos das próprias ferramentas no lugar dos scripts, nomes dos dados brutos no padrão de G3, M1.2.1 conforme a ficha e correções de M1.3.1, M1.3.3, M1.4.3 e M1.5.2 | [Christopher Paraizo](https://github.com/wChrstphr) |  |
