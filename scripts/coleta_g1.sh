#!/usr/bin/env bash
# Coleta dos dados brutos das 14 métricas de G1 (Manutenibilidade).
#
# Repete os comandos de docs/fase-03/instrucoes-g1-manutenibilidade.md, na
# ordem das seções, e grava as saídas em dados/fase-04/brutos/. Não calcula
# valores: o cálculo é feito na verificação dos dados brutos (issue #114).
#
# Uso, a partir da raiz deste repositório:
#   EXC=/caminho/do/clone scripts/coleta_g1.sh [etapa]
#
# Etapas: preparacao, grafo, reusabilidade, analisabilidade, extensos,
# testes, historico. Sem argumento, roda todas na ordem.
#
# Variáveis:
#   EXC     clone do Excalidraw no commit avaliado (padrão $HOME/excalidraw-avaliado)
#   BRUTOS  pasta dos dados brutos (padrão dados/fase-04/brutos deste repositório)

set -euo pipefail

COMMIT="e1b7aacb356a492aa1e0fc6eb57b8896124027f0"
REPO="excalidraw/excalidraw"
JANELA="2026-04-18..2026-10-18"

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export EXC="${EXC:-$HOME/excalidraw-avaliado}"
export BRUTOS="${BRUTOS:-$RAIZ/dados/fase-04/brutos}"
PRODUCAO="$BRUTOS/M1.1.1_arquivos-producao.txt"

log() { printf '[%s] %s\n' "$(date '+%Y-%m-%d %H:%M:%S %z')" "$*"; }
falha() { log "ERRO: $*"; exit 1; }

conferir_clone() {
  [ -d "$EXC/.git" ] || falha "EXC=$EXC não é um clone Git"
  local head
  head="$(git -C "$EXC" rev-parse HEAD)"
  [ "$head" = "$COMMIT" ] || falha "commit $head diferente de $COMMIT"
  [ -z "$(git -C "$EXC" status --porcelain)" ] || falha "o clone tem alterações locais"
  log "Clone $EXC no commit $head, árvore limpa"
}

exigir_producao() {
  [ -s "$PRODUCAO" ] || falha "rode a etapa preparacao antes"
}

# Seção 1: preparação
preparacao() {
  log "Seção 1: lista de arquivos de produção e versões das ferramentas"
  mkdir -p "$BRUTOS"
  cd "$EXC"
  find packages excalidraw-app \
    \( -name node_modules -o -name tests -o -name __snapshots__ -o -name examples \) -prune \
    -o -type f \( -name '*.ts' -o -name '*.tsx' \) \
    ! -name '*.test.ts' ! -name '*.test.tsx' ! -name '*.d.ts' -print \
    | sort > "$PRODUCAO"
  log "$(wc -l < "$PRODUCAO") arquivos de produção"

  {
    echo "# Versões das ferramentas, $(date '+%Y-%m-%d %H:%M:%S %z')"
    echo "commit: $(git rev-parse HEAD)"
    echo "clone: $EXC"
    echo "uname: $(uname -srm)"
    grep PRETTY_NAME /etc/os-release || true
    echo "git: $(git --version)"
    echo "node: $(node --version)"
    echo "npm: $(npm --version)"
    echo "yarn: $(yarn --version)"
    echo "gh: $(gh --version | head -1)"
    echo "grep: $(grep --version | head -1)"
    echo "madge: $(npx --yes madge@8.0.0 --version)"
    echo "cloc: $(cloc --version)"
    echo "eslint: $(npx --yes eslint@8.57.0 --version 2>/dev/null)"
    echo "eslint do projeto (não usado em M1.3.1): $(./node_modules/.bin/eslint --version)"
    echo "vitest: $(./node_modules/.bin/vitest --version)"
    echo "typescript: $(./node_modules/.bin/tsc --version)"
    echo "yarn why @typescript-eslint/parser:"
    yarn why @typescript-eslint/parser 2>/dev/null | grep -E 'Found|info' || true
    echo "yarn why @vitest/coverage-v8:"
    yarn why @vitest/coverage-v8 2>/dev/null | grep -E 'Found|info' || true
  } > "$BRUTOS/M1_versoes-ferramentas.txt"
}

# Seções 2.1, 2.3: grafo de importações e regra de lint
grafo() {
  exigir_producao
  log "Seção 2.1: grafo de importações com o Madge"
  cd "$EXC"
  [ ! -e .madgerc ] || falha "já existe .madgerc no checkout"
  trap 'rm -f "$EXC/.madgerc"' EXIT
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
  trap - EXIT

  log "Seção 2.3: regra de lint da direção das importações"
  cp "$EXC/packages/eslintrc.base.json" "$BRUTOS/M1.1.2_eslintrc-base.json"
}

# Seções 3.1 e 3.2: reusabilidade
reusabilidade() {
  exigir_producao
  log "Seção 3.1: ocorrências de React e do navegador"
  cd "$EXC"
  xargs grep -nHE "from ['\"]react(-dom)?(/[^'\"]*)?['\"]|require\(['\"]react(-dom)?['\"]|(^|[^.[:alnum:]_])(window|document)\." \
    < "$PRODUCAO" > "$BRUTOS/M1.2.1_ocorrencias-grep.txt"

  log "Seção 3.2: declaração de ExcalidrawProps"
  sed -n '/^export interface ExcalidrawProps/,/^}/p' packages/excalidraw/types.ts \
    > "$BRUTOS/M1.2.2_excalidraw-props.ts"
}

# Seções 4.1 e 4.3: analisabilidade
analisabilidade() {
  log "Seção 4.1: complexidade com o ESLint 8.57.0"
  cd "$EXC"
  local codigo=0
  npx --yes eslint@8.57.0 --format json --rule 'complexity: [error, 0]' \
    --ext .ts,.tsx packages excalidraw-app \
    > "$BRUTOS/M1.3.1_eslint.json" 2> "$BRUTOS/M1.3.1_eslint-erros.log" || codigo=$?
  [ "$codigo" -le 1 ] || falha "ESLint terminou com código $codigo"
  log "ESLint terminou com código $codigo (1 é o esperado)"

  log "Seção 4.3: fluxos disparados por pull_request"
  grep -lw pull_request .github/workflows/*.yml > "$BRUTOS/M1.3.3_fluxos-pull-request.txt"
  while read -r F
  do
    cp "$F" "$BRUTOS/M1.3.3_$(basename "$F")"
  done < "$BRUTOS/M1.3.3_fluxos-pull-request.txt"
  cp package.json "$BRUTOS/M1.3.3_package.json"
}

# Seção 5.3: arquivos extensos
extensos() {
  exigir_producao
  log "Seção 5.3: linhas por arquivo com o cloc"
  cd "$EXC"
  cloc --by-file --json --list-file="$PRODUCAO" > "$BRUTOS/M1.4.2_cloc.json"
}

# Seções 6.1 e 6.2: testes
testes() {
  log "Seção 6.1: cobertura (sequência dos recursos e ambiente, seção 2.1)"
  cd "$EXC"
  rm -rf packages/*/dist coverage
  CI=true yarn test:coverage --minWorkers=1 --maxWorkers=8 2>&1 | tee "$BRUTOS/M1.5.1_testes.log"
  cp coverage/coverage-summary.json "$BRUTOS/M1.5.1_coverage-summary.json"

  log "Seção 6.2: suítes e sinais de nível"
  find packages excalidraw-app -name node_modules -prune \
    -o -type f \( -name '*.test.ts' -o -name '*.test.tsx' \) -print \
    | sort > "$BRUTOS/M1.5.2_suites.txt"
  xargs grep -nHE "\brender\(|from ['\"](@playwright/test|playwright|cypress|puppeteer)['\"]" \
    < "$BRUTOS/M1.5.2_suites.txt" > "$BRUTOS/M1.5.2_ocorrencias-grep.txt"
  # Nenhuma ferramenta de ponta a ponta é uma saída válida: grep devolve 1.
  grep -nE '"(@playwright/test|playwright|cypress|puppeteer)"' \
    package.json packages/*/package.json excalidraw-app/package.json \
    > "$BRUTOS/M1.5.2_ferramentas-e2e.txt" || [ $? -eq 1 ]
}

# Seções 5.1 e 6.3: histórico de pull requests e execuções
historico() {
  log "Seção 5.1: pull requests integrados em $JANELA"
  echo "inicio: $(date '+%Y-%m-%d %H:%M:%S %z')" > "$BRUTOS/M1_historico-consulta.txt"
  gh pr list --repo "$REPO" --state merged --base master \
    --search "merged:$JANELA" --limit 1000 \
    --json number,title,author,mergedAt,headRefOid > "$BRUTOS/M1.4.1_prs.json"
  local total
  total="$(node -e 'console.log(require(process.argv[1]).length)' "$BRUTOS/M1.4.1_prs.json")"
  [ "$total" -lt 1000 ] || falha "a busca atingiu 1.000 itens, repetir por mês"
  log "$total pull requests"

  node -e 'for (const p of require(process.argv[1])) console.log(p.number)' "$BRUTOS/M1.4.1_prs.json" |
  while read -r N
  do
    gh api "repos/$REPO/pulls/$N/files?per_page=100" --paginate --slurp \
      > "$BRUTOS/M1.4.1_pr-$N-arquivos.json"
  done

  log "Seção 6.3: execuções de test-coverage-pr.yml"
  node -e 'for (const p of require(process.argv[1])) console.log(p.number, p.headRefOid)' "$BRUTOS/M1.4.1_prs.json" |
  while read -r N SHA
  do
    gh api -X GET "repos/$REPO/actions/workflows/test-coverage-pr.yml/runs" \
      -f head_sha="$SHA" -f per_page=100 > "$BRUTOS/M1.5.3_pr-$N-execucoes.json"
    node -e 'for (const r of require(process.argv[1]).workflow_runs) console.log(r.id)' "$BRUTOS/M1.5.3_pr-$N-execucoes.json" |
    while read -r RUN
    do
      gh api "repos/$REPO/actions/runs/$RUN/jobs?per_page=100" \
        > "$BRUTOS/M1.5.3_execucao-$RUN-jobs.json"
    done
  done
  echo "fim: $(date '+%Y-%m-%d %H:%M:%S %z')" >> "$BRUTOS/M1_historico-consulta.txt"
}

ETAPAS=(preparacao grafo reusabilidade analisabilidade extensos testes historico)

main() {
  conferir_clone
  if [ $# -gt 0 ]; then
    printf '%s\n' "${ETAPAS[@]}" | grep -qx "$1" || falha "etapa desconhecida: $1"
    "$1"
  else
    for E in "${ETAPAS[@]}"; do (cd "$RAIZ" && "$E"); done
  fi
  conferir_clone
  log "Coleta concluída"
}

main "$@"
