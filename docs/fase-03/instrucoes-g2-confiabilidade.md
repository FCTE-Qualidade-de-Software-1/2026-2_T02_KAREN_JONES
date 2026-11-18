---
sidebar_position: 7
title: Instruções para o avaliador de Confiabilidade (G2)
description: Procedimentos reproduzíveis para coletar as dez métricas de Confiabilidade na Fase 04
---

import Link from '@docusaurus/Link';

# Instruções para o avaliador de Confiabilidade (G2)

## Introdução

O plano de avaliação reúne o método, a instrução para o avaliador, os recursos e o cronograma [[1, p. 19]](#ref-1), e deve permitir que o avaliador execute a avaliação completamente [[1, p. 18]](#ref-1). A coleta manual deve identificar quem coletou o dado [[2, p. 51]](#ref-2).

O objetivo desta página é dar o passo a passo para que o responsável obtenha, no commit e na janela histórica avaliados, o valor das dez métricas de [G2](../fase-02/gqm-confiabilidade.md), com os formulários, arquivos brutos e gravações que tornam cada resultado verificável.

## Metodologia

Cada métrica segue a definição, a fórmula e o procedimento de coleta da sua ficha na [Fase 02](../fase-02/gqm-confiabilidade.md) e o método definido no [método de avaliação](./metodo-avaliacao.md#22-g2-confiabilidade). As versões, a máquina responsável e os fatores de variação são os dos [recursos](./recursos-ambiente.md), e as entradas dos testes vêm da [massa de dados](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/dados/fase-03/massa-de-dados/README.md), com a cena de referência e os nove arquivos inválidos. Os valores são convertidos em nível pelas [faixas de G2](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2). A ligação de cada métrica ao método, ao recurso e à faixa está na [rastreabilidade da Fase 03](./visao-geral.md#rastreabilidade-entre-as-fases-02-e-03).

Para cada métrica, a página traz os passos com a saída esperada, o nome do dado bruto e a regra de cálculo. As métricas M2.1.1 a M2.1.3 usam o histórico do GitHub e as demais são testes no navegador, gravados em vídeo.

## 1. Preparação, identificação e arquivos de evidência

### 1.1 Responsável e ambiente

O responsável indicado no [plano de recursos](./recursos-ambiente.md#3-máquinas-dos-responsáveis-pela-coleta) para **todas as métricas de G2** é **Luiz Henrique Soares**. Sua máquina é Windows 11 Home Single Language (build 26300), Intel i5-14450HX e 16 GB de RAM. Para os testes de navegador, usar **Firefox 159.0.1**, com atualizações automáticas desativadas. Se outra pessoa ou máquina executar o teste, registrar a mudança como desvio, sem apresentar a coleta como equivalente à linha de base.
**Terminal:** executar os comandos deste documento no **Git Bash** (ou WSL), não no PowerShell nem no CMD, porque eles usam continuação de linha com `\` e aspas simples. A única exceção é o `taskkill` do cenário C4 de M2.4.1, que roda no CMD ou PowerShell. Registrar o terminal usado e sua versão no formulário.


Para M2.1.1 a M2.1.3, usar GitHub CLI **2.102.0**, autenticada (`gh auth status`) e com acesso à API do GitHub. A janela de contribuições integradas é **18/04/2026 a 18/10/2026**, inclusive, sobre `excalidraw/excalidraw`, ramo `master`.

Para M2.2.1 a M2.4.3, obter o Excalidraw no commit **`e1b7aacb356a492aa1e0fc6eb57b8896124027f0`**. Na raiz do repositório Excalidraw:

```bash
git checkout e1b7aacb356a492aa1e0fc6eb57b8896124027f0
git rev-parse HEAD
docker build -t excalidraw-avaliacao .
docker run -d --name excalidraw-avaliacao -p 3000:80 excalidraw-avaliacao
docker ps --filter name=excalidraw-avaliacao
```

**Saída esperada:** `git rev-parse HEAD` imprime exatamente o hash acima, `docker build` termina sem erro, `docker ps` mostra o contêiner em execução e `http://localhost:3000` carrega o editor. Não usar `docker compose` para esse ambiente: a configuração indicada no [plano](./recursos-ambiente.md#23-aplicação-em-execução-ambiente-de-teste) é a imagem de produção do `Dockerfile`.

Os comandos do GitHub não dependem do Docker. O contêiner só é necessário para os testes do editor no navegador.

### 1.2 Pasta e convenção de nomes

Todos os dados brutos e formulários devem ser colocados em `dados/fase-04/brutos/` do [repositório da avaliação](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES), e não no repositório do Excalidraw. Crie a pasta, caso ainda não exista. Em um terminal Bash, na raiz do repositório de avaliação:

```bash
mkdir -p dados/fase-04/brutos
```

Em PowerShell, o equivalente é `New-Item -ItemType Directory -Force dados/fase-04/brutos`. Os comandos adiante assumem a pasta `dados/fase-04/brutos/`. Onde aparecer `M2.X.X`, substituir pelo código exato da métrica. Não sobrescrever evidências de repetições: acrescentar `_r1`, `_r2`, `_r3` ou o número do caso quando indicado.

**Formulário obrigatório em toda coleta:** criar `M2.X.X_coleta.csv`, com uma linha de identificação para a execução e, nas linhas seguintes, resultados por teste. Preencher antes de iniciar a coleta, com os campos da Tabela 1.

<p className="tabela-titulo">Tabela 1: Campos do formulário de coleta</p>

| Campo | Valor a registrar |
| :--- | :--- |
| `metrica`, `avaliador` | Código M2.X.X e nome de quem executou |
| `inicio`, `fim` | Data, hora e fuso, com `fim` preenchido ao terminar |
| `commit`, `janela_historica` | Hash do Excalidraw e intervalo de datas quando for histórico |
| `maquina`, `sistema`, `navegador` | Equipamento, Windows/build, Firefox e versão, ou `n/a` se não aplicável |
| `ferramentas` | Versões usadas: `gh --version` ou Docker/Firefox e comparador existente, conforme a métrica, e sempre o terminal usado (Git Bash ou WSL) e sua versão |
| `rede`, `colaboracao` | Online/offline, bloqueios, conexão do serviço de colaboração |
| `perfil`, `cache`, `armazenamento` | Perfil do Firefox, cache limpo ou não, dados locais limpos ou preservados |
| `id_caso`, `entrada`, `acao`, `resultado`, `observacao` | Identificação, arquivo de entrada, ação realizada, passou/falhou e motivo |
| `evidencias`, `desvios` | Caminhos dos JSON, CSV, HAR e vídeos, e diferença em relação ao roteiro |

<p className="tabela-fonte">Fonte: [Letícia de Carvalho](https://github.com/LeticiaSantosss), 2026.</p>

Um CSV simples pode ser preenchido no Excel/LibreOffice e exportado em formato CSV. Não há necessidade de desenvolver um programa de coleta. Usar `aprovado`, `reprovado` ou `nao_executado` para o resultado. **Não transformar `nao_executado` em falha nem em aprovação**: declarar a métrica incompleta.

**Vídeos:** iniciar a gravação de **toda coleta manual no navegador** com OBS Studio, mostrar data/hora e ação executada, e salvar em MP4 usando os nomes definidos abaixo. Os vídeos são a evidência da coleta manual. Capturas de tela podem complementá-los, mas não substituí-los. Não gravar credenciais, tokens ou informações pessoais de terceiros.

### 1.3 Critério de encerramento

Para cada métrica, conferir se todas as entradas e PRs estão identificados, se os arquivos brutos têm o nome indicado, se o formulário contém avaliador, horário e fatores de variação, se o valor foi calculado com o denominador definido na Fase 02, se há evidência para cada aprovação ou falha e se o resultado foi associado à [faixa de pontuação de G2](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2). Não preencher resultados numéricos antes da execução real.

## 2. Q2.1: Ausência de falhas

### 2.1 M2.1.1: Proporção de correções entre as contribuições integradas

**Ficha:** [M2.1.1](../fase-02/gqm-confiabilidade.md#m211-proporção-de-correções-entre-as-contribuições-integradas). **Faixa:** [seção 4, M2.1.1](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2).

1. Com a GitHub CLI (`gh`) autenticada (`gh auth status`), consultar os *pull requests* integrados no ramo `master` do Excalidraw durante a janela histórica de **18/04/2026 a 18/10/2026**. Na raiz do repositório de avaliação, executar:

   ```bash
   gh api --method GET search/issues \
     -f q='repo:excalidraw/excalidraw is:pr is:merged base:master merged:2026-04-18..2026-10-18' \
     -F per_page=100 --paginate --slurp \
     > dados/fase-04/brutos/M2.1.1_prs_integrados.json
   ```

   **Saída esperada:** arquivo `M2.1.1_prs_integrados.json` com as respostas da API, incluindo os PRs integrados na janela. Se a API indicar mais de 1.000 resultados ou `incomplete_results=true`, subdividir a consulta em intervalos menores, salvar os arquivos separadamente e registrar a divisão utilizada. O diretório `dados/fase-04/brutos/` deve existir antes da execução.

2. Abrir `M2.1.1_prs_integrados.json`. Como foi utilizado `--slurp`, o conteúdo é uma lista de páginas. Em cada página, os PRs ficam no campo `items`. Identificar para cada PR seu número (`number`), título (`title`), autor (`user.login`) e data de integração. Conferir que o total de itens retornados corresponde ao total indicado pela busca, sem utilizar apenas `total_count` como se fosse a lista de PRs.

3. Registrar um PR por linha em **`M2.1.1_prs.csv`**, com as colunas `numero,titulo,autor,merged_at,escopo,automacao_excluida,elegivel,eh_fix,motivo`. Remover duplicações pelo número do PR e excluir as contribuições automáticas de **atualização de dependências e traduções**, conforme a ficha da Fase 2. Justificar cada exclusão na coluna `motivo`. Classificar como correção (`eh_fix=sim`) somente a contribuição elegível cujo título começa com `fix` (por exemplo, `fix(editor): ...`). Registrar também o escopo indicado no título, como `editor` ou `app`.

4. **Calcular:** `100 × número de PRs elegíveis classificados como fix / número total de PRs elegíveis integrados`. Registrar separadamente a distribuição das correções por escopo. **Saída esperada:** percentual entre 0 e 100, acompanhado das quantidades utilizadas no numerador e no denominador e da distribuição por escopo. Se não houver PRs elegíveis, informar que o cálculo não é possível. Os PRs elegíveis são a população de M2.1.1 a M2.1.3, e as automações excluídas ficam marcadas com `automacao_excluida=sim` em [`M2.1.1_prs.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/dados/fase-04/brutos/Q2.1-ausencia-de-falhas/M2.1.1_prs.csv).

**Dados brutos:** `dados/fase-04/brutos/M2.1.1_prs_integrados.json` e `dados/fase-04/brutos/M2.1.1_prs.csv`. Registrar identificação do avaliador, data, horário, versão da CLI, janela histórica, resultado e desvios em `dados/fase-04/brutos/M2.1.1_coleta.csv`. **Sem vídeo**, pois a coleta utiliza a API do GitHub.

### 2.2 M2.1.2: Mediana do tempo entre o relato e a correção

**Ficha:** [M2.1.2](../fase-02/gqm-confiabilidade.md#m212-mediana-do-tempo-entre-o-relato-e-a-correção). **Faixa:** [seção 4, M2.1.2](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2).

1. Partir dos PRs elegíveis com `eh_fix=sim` da coleta M2.1.1. Para **cada número de PR**, substituir `NUMERO` e executar:

   ```bash
   gh api graphql -f query='query($n: Int!) {
     repository(owner: "excalidraw", name: "excalidraw") {
       pullRequest(number: $n) {
         number mergedAt
         closingIssuesReferences(first: 100) {
           nodes { number createdAt url repository { nameWithOwner } }
           pageInfo { hasNextPage endCursor }
         }
       }
     }
   }' -F n=NUMERO > dados/fase-04/brutos/M2.1.2_pr_NUMERO.json
   ```

2. **Saída esperada:** `data.repository.pullRequest.mergedAt` e, para os PRs com relato vinculado, `closingIssuesReferences.nodes[].createdAt`. Se `hasNextPage=true`, consultar as páginas seguintes pelo cursor (adaptar `first: 100` para `first: 100, after: $cursor` e declarar `$cursor: String` na consulta), guardando todas as respostas. Se houver erro ou falta de autorização, não classificar a ausência como “sem relato”.
3. Criar **`M2.1.2_pares.csv`** com `pr,issue,abertura_utc,integracao_utc,dias,observacao`. Para cada vínculo válido, calcular `(integração UTC − abertura UTC) / 86.400 segundos`, em dias corridos, conservando casas decimais. Usar apenas relatos do repositório `excalidraw/excalidraw` (`repository.nameWithOwner`). Registrar **uma linha por PR**: se ele encerra mais de um relato, usar o de abertura mais antiga e listar os demais em `observacao`. Não excluir relatos pela data de abertura: vale a data de integração do PR dentro da janela, como na ficha. Registrar PRs sem vínculo à parte para medir a cobertura. A ficha define a mediana dos intervalos de relatos explicitamente vinculados, e não dos PRs sem referência.
4. Ordenar os valores de `dias`: para `n` ímpar, escolher o central e, para `n` par, calcular a média dos dois centrais. Informar **mediana em dias** e `100 × PRs fix com ao menos um relato vinculado / total de PRs fix elegíveis`. **Saída esperada:** número de dias e percentual de cobertura. Sem vínculos, informar `não calculável`. Registrar a mediana exata, sem arredondar. O nível sai das [faixas de M2.1.2](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2), lidas como contínuas conforme a [leitura das faixas de medianas](../fase-02/pontuacao-julgamento.md#24-leitura-das-faixas-de-medianas).

**Dados brutos:** `M2.1.2_pr_NUMERO.json` para cada correção, `M2.1.2_pares.csv` e `M2.1.2_coleta.csv`. **Sem vídeo**.

### 2.3 M2.1.3: Proporção de contribuições revisadas antes da integração

**Ficha:** [M2.1.3](../fase-02/gqm-confiabilidade.md#m213-proporção-de-contribuições-revisadas-antes-da-integração). **Faixa:** [seção 4, M2.1.3](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2).

1. Para **todos os PRs elegíveis** de M2.1.1, consultar as revisões pelo número:

   ```bash
   gh api graphql -f query='query($n: Int!) {
     repository(owner: "excalidraw", name: "excalidraw") {
       pullRequest(number: $n) {
         number author { login } mergedAt
         reviews(first: 100, states: APPROVED) {
           nodes { author { login } submittedAt state }
           pageInfo { hasNextPage endCursor }
         }
       }
     }
   }' -F n=NUMERO > dados/fase-04/brutos/M2.1.3_pr_NUMERO.json
   ```

2. **Saída esperada:** nome do autor, data de integração e revisões `APPROVED` com autor e horário. Se a página estiver incompleta (`hasNextPage=true`), buscar as páginas seguintes com cursor, como em M2.1.2, e salvar também essas respostas.
3. Preencher **`M2.1.3_revisoes.csv`** com `pr,autor_pr,merged_at,revisor,submitted_at,aprovacao_valida,motivo`. Aprovação válida: estado `APPROVED`, revisor **diferente do autor do PR** e `submittedAt` anterior à integração. Contar **cada PR no máximo uma vez** se houver uma ou mais aprovações válidas. Checks de CI e comentários sem aprovação não contam.
4. **Calcular:** `100 × PRs elegíveis com ao menos uma aprovação válida ÷ total de PRs elegíveis integrados`, a mesma população de M2.1.1. A [ficha de M2.1.3](../fase-02/gqm-confiabilidade.md#m213-proporção-de-contribuições-revisadas-antes-da-integração) fala em contribuições integradas na janela, sem citar exclusões. A instrução aplica as mesmas exclusões de automações de M2.1.1, registradas em [`M2.1.1_prs.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/dados/fase-04/brutos/Q2.1-ausencia-de-falhas/M2.1.1_prs.csv), para que as três métricas de Q2.1 usem uma única população. **Saída esperada:** percentual de 0 a 100. Registrar o número de PRs sem aprovação válida.

**Dados brutos:** `M2.1.3_pr_NUMERO.json`, `M2.1.3_revisoes.csv` e `M2.1.3_coleta.csv`. **Sem vídeo**.

## 3. Q2.2: Disponibilidade

### 3.1 M2.2.1: Proporção de funções essenciais disponíveis sem conexão

**Ficha:** [M2.2.1](../fase-02/gqm-confiabilidade.md#m221-proporção-de-funções-essenciais-disponíveis-sem-conexão). **Faixa:** [seção 4, M2.2.1](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2).

1. Abrir `http://localhost:3000` **online** no Firefox. No DevTools (`F12`), abrir **Aplicativo/Armazenamento → Service Workers** (a denominação pode variar com o idioma) e verificar que há um trabalhador registrado e ativado. Registrar seu estado no formulário. Aguardar o carregamento completo.
2. Iniciar OBS, **`M2.2.1_gravacao_offline.mp4`**. Em **Rede/Network** do DevTools, ativar **Offline**. Não desativar o servidor Docker: o objetivo é testar o navegador sem rede após o carregamento inicial.
3. Executar **nesta ordem** e registrar cada resultado: (1) recarregar a página e ver o editor, (2) criar retângulo e elipse, (3) escrever texto, (4) mover e redimensionar, (5) desfazer e refazer, (6) salvar `.excalidraw`, (7) reabrir o arquivo salvo, (8) exportar PNG, (9) exportar SVG e (10) verificar texto legível na fonte padrão. Para itens com saída, comprovar que o arquivo foi realmente gerado ou reaberto.
4. Preencher **`M2.2.1_funcoes.csv`** com `item,funcao,resultado,evidencia,observacao`. Uma função recebe `aprovado` apenas se for concluída offline. Voltar ao estado online ao terminar.
5. **Calcular:** `(funções que funcionam ÷ 10) × 100`. **Saída esperada:** dez registros e percentual. Anexar os arquivos exportados com prefixo `M2.2.1_` quando necessários à evidência.

**Dados brutos:** `M2.2.1_funcoes.csv`, `M2.2.1_coleta.csv`, exports `M2.2.1_*` e **vídeo** `M2.2.1_gravacao_offline.mp4`.

### 3.2 M2.2.2: Origens externas necessárias para o editor local

**Ficha:** [M2.2.2](../fase-02/gqm-confiabilidade.md#m222-origens-externas-necessárias-para-o-editor-local). **Faixa:** [seção 4, M2.2.2](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2).

1. Começar **sem sessão de colaboração**. Em um perfil limpo do Firefox, abrir DevTools (`F12`) → **Rede/Network** e limpar o cache em **Armazenamento/Storage**. Ativar a opção de preservar o registro das requisições de rede.
2. Iniciar OBS em **`M2.2.2_gravacao_bloqueios.mp4`**. Abrir `http://localhost:3000`. Considerar o carregamento concluído quando o painel de rede ficar 5 segundos sem novas requisições. Exportar a lista pelo menu **Salvar tudo como HAR** em **`M2.2.2_abertura.har`**.
3. Do HAR, listar os **domínios distintos** das URLs requisitadas, excluindo apenas `localhost:3000` (origem local). Domínio é o nome de host sem a porta: subdomínios diferentes contam como domínios distintos (por exemplo, `fonts.googleapis.com` e `fonts.gstatic.com`), `localhost` em outra porta conta como externo e é anotado em `observacao`, e URLs `data:` e `blob:` não entram na lista. Preencher **`M2.2.2_dominios.csv`** com `dominio,urls_observadas,indispensavel,resultado_forma,resultado_texto,observacao`.
4. Para **cada domínio isoladamente** limpar o painel de rede, usar o bloqueio de URLs/requisições do DevTools para bloquear `*://DOMINIO/*` (ou o padrão equivalente que a ferramenta aceitar), limpar o cache, recarregar a página e tentar **criar uma forma e um texto**. Retirar esse bloqueio antes de testar o próximo domínio. Anotar mensagens no console, falhas na rede e se o editor ainda desenha em `M2.2.2_bloqueios.csv`. Se o recurso do Firefox não aceitar o padrão, registrar o padrão efetivamente aplicado e verificar no painel de rede se o bloqueio ocorreu.
5. Marcar `indispensavel=sim` **somente** se bloqueio impedir criar forma **ou** texto. Caso contrário, `não`. **Saída esperada:** total de domínios externos distintos e quantos são indispensáveis, não um percentual. A pontuação da Fase 02 usa **ambas** as contagens. A hipótese H2.2.2 se confirma se nenhum domínio externo for indispensável.

`M2.2.2_bloqueios.csv: dominio,padrao_bloqueio_aplicado,bloqueio_confirmado_na_rede,forma_criada,texto_criado,erros_console,minuto_no_video`
**Dados brutos:** `M2.2.2_abertura.har`, `M2.2.2_dominios.csv`, `M2.2.2_bloqueios.csv`, `M2.2.2_coleta.csv` e **vídeo** `M2.2.2_gravacao_bloqueios.mp4`.

## 4. Q2.3: Tolerância a falhas

### 4.1 M2.3.1: Proporção de arquivos inválidos tratados com mensagem

**Ficha:** [M2.3.1](../fase-02/gqm-confiabilidade.md#m231-proporção-de-arquivos-inválidos-tratados-com-mensagem). **Faixa:** [seção 4, M2.3.1](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2).

1. Confirmar a presença dos **nove arquivos** em `dados/fase-03/massa-de-dados/invalidos/`, identificados de `invalido_01_*` a `invalido_09_*`, e consultar os nomes e defeitos na [tabela da massa](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/dados/fase-03/massa-de-dados/README.md).
2. Iniciar OBS em **`M2.3.1_gravacao_menu.mp4`**. Para cada arquivo, abrir o editor em estado inicial, usar **Abrir** no menu de arquivos e selecionar a entrada. Registrar se apareceu mensagem e se é possível criar um retângulo **sem recarregar**. Repetir com os nove arquivos, reiniciando a cena/aba antes de cada tentativa.
3. Iniciar segunda gravação **`M2.3.1_gravacao_arrastar.mp4`** e repetir as nove entradas, agora por **arrastar e soltar** no editor. Registrar a mensagem exibida (ou a ausência dela) e se o editor continua utilizável.
4. Preencher **`M2.3.1_tentativas.csv`** com `arquivo,via,mensagem_exibida,texto_mensagem,retangulo_criado,caso_tratado,observacao`. Para cada arquivo, registrar se o Excalidraw apresentou uma mensagem e se continuou permitindo criar um retângulo sem recarregar a página.
Um caso é considerado tratado quando o editor apresenta uma mensagem e, em seguida, permite criar formas sem recarregar a página, conforme a [ficha de M2.3.1](../fase-02/gqm-confiabilidade.md#m231-proporção-de-arquivos-inválidos-tratados-com-mensagem). Em `caso_tratado`, registrar `sim` ou `não` por tentativa (18 linhas: 9 arquivos × 2 vias).
**Consolidação:** como na ficha, um arquivo só conta como tratado se for tratado nas duas rodadas (menu e arrastar e soltar). Registrar a decisão em `M2.3.1_casos.csv`, com `arquivo,tratado_menu,tratado_arrastar,tratado_consolidado`.
5. **Calcular:** `(casos tratados ÷ 9) × 100`. **Saída esperada:** nove decisões consolidadas, percentual de 0 a 100 e registros das tentativas.

**Dados brutos:** `M2.3.1_tentativas.csv`, `M2.3.1_casos.csv`, `M2.3.1_coleta.csv` e **vídeos** `M2.3.1_gravacao_menu.mp4`, `M2.3.1_gravacao_arrastar.mp4`.

### 4.2 M2.3.2: Continuidade do editor após falha da colaboração

**Ficha:** [M2.3.2](../fase-02/gqm-confiabilidade.md#m232-continuidade-do-editor-após-falha-da-colaboração). **Faixa:** [seção 4, M2.3.2](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2).

1. Com a internet **online** e a aplicação local aberta, criar sessão de colaboração pelo recurso **Live collaboration/Colaboração**, copiar o link e abri-lo em **segunda janela** do Firefox. Confirmar que um retângulo criado na janela A aparece na janela B **antes** da interrupção. 
2. Iniciar OBS em **`M2.3.2_gravacao_r1.mp4`**. Na janela A, ativar **Offline** em DevTools → Rede. Verificar: **V1** desenho permanece visível, **V2** ainda é possível criar e editar um elemento, **V3** há aviso de desconexão, **V4** é possível salvar `.excalidraw` e **V5** após desativar Offline, a edição feita sem conexão aparece na janela B. 
3. Repetir todo o teste **três vezes**, criando estado inicial verificável e salvando as gravações em **`M2.3.2_gravacao_r1.mp4`**, **`_r2.mp4`**, **`_r3.mp4`**. Manter a segunda janela visível no vídeo ao conferir a sincronização. Guardar os arquivos salvos como `M2.3.2_desenho_r1.excalidraw` etc.
4. Preencher **`M2.3.2_verificacoes.csv`** com `repeticao,verificacao,resultado,evidencia,observacao`. Uma verificação é aprovada **somente se passar nas três repetições**.
5. **Calcular:** `100 × verificações aprovadas / 5`. **Saída esperada:** percentual em incrementos de 20. Para a análise da hipótese H2.3.2, considerar separadamente os resultados de V1 a V4, que avaliam a continuidade do editor durante a interrupção da colaboração. A verificação V5 também compõe o cálculo da métrica e avalia o comportamento da colaboração após o restabelecimento da conexão.

**Dados brutos:** `M2.3.2_verificacoes.csv`, `M2.3.2_coleta.csv`, `M2.3.2_desenho_r1.excalidraw` a `_r3.excalidraw`, **três vídeos** com sufixos `_r1`, `_r2`, `_r3`.

## 5. Q2.4: Recuperabilidade

### 5.1 Comparação das exportações (M2.4.1 a M2.4.3)

Os três métodos da [Fase 03](./metodo-avaliacao.md#22-g2-confiabilidade) comparam os elementos dos arquivos `.excalidraw`, e não a aparência da tela. A comparação usa o `scripts/compara_elementos.py`, escrito para M3.4.2, executado na raiz do repositório da avaliação. Cada métrica abaixo traz o comando pronto, seguindo este modelo. Antes da primeira coleta, rodar `python --version` e `python scripts/compara_elementos.py --help` para registrar a versão e confirmar os parâmetros:

```bash
python scripts/compara_elementos.py \
  --original dados/fase-04/brutos/ORIGINAL.excalidraw \
  --reimportados dados/fase-04/brutos/RESULTADO.excalidraw \
  --output-json dados/fase-04/brutos/RELATORIO.json \
  --output-csv dados/fase-04/brutos/RELATORIO.csv
```

Os nomes são trocados pelos arquivos de cada caso. **Saída esperada:** JSON e CSV com os elementos preservados, as diferenças e o percentual. O comparador confere tipo, posição, tamanho, estilo básico e texto com tolerância, mas não garante igualdade de rotação, agrupamento, vínculos de setas, arquivos incorporados nem ausência de elementos extras. Em M2.4.1 e M2.4.3, essas propriedades são conferidas também no JSON original e no exportado, com as diferenças registradas no CSV do caso. Um resultado de 100% no comparador, sozinho, não basta para `aprovado`. A versão do Python entra nos fatores de variação.

### 5.2 M2.4.1: Proporção de cenários de fechamento com restauração do desenho

**Ficha:** [M2.4.1](../fase-02/gqm-confiabilidade.md#m241-proporção-de-cenários-de-fechamento-com-restauração-do-desenho). **Faixa:** [seção 4, M2.4.1](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2).

1. Usar `dados/fase-03/massa-de-dados/cena_referencia.excalidraw` como cena inicial (dez elementos). Abrir pela interface do Excalidraw, aguardar o salvamento local e exportar **`M2.4.1_cN_antes.excalidraw`**, substituindo `N` pelo cenário. **Não limpar o armazenamento local entre fechar e reabrir**, porque ele é justamente o objeto avaliado.
2. Testar cada cenário separadamente, com uma gravação por cenário (`M2.4.1_gravacao_c1.mp4` a `_c4.mp4`). C1 recarrega a página, C2 fecha a aba e reabre, C3 encerra o Firefox normalmente e C4 encerra o processo do navegador pelo sistema operacional, um segundo depois da última edição. Em C4, o comando é `taskkill /F /IM firefox.exe /T` no CMD ou PowerShell, que encerra todos os processos do Firefox, porque finalizar só um processo filho não derruba o navegador. A última edição (por exemplo, mover o retângulo 20 unidades à direita) é anotada antes do teste. O intervalo real entre a edição e o encerramento é lido depois no relógio do vídeo, e o cenário é repetido se passar de 3 segundos.
3. Ao reabrir a aplicação, sem importar manualmente o arquivo inicial, exportar o desenho **restaurado** como **`M2.4.1_cN_depois.excalidraw`**. Se não houver desenho, salvar evidência da tela e registrar falha.
4. Comparar cada par com o comparador, na raiz do repositório da avaliação, e conferir também no JSON as propriedades que ele não cobre por completo (rotação, agrupamento, vínculos de setas, arquivos incorporados e elementos extras):

   ```bash
   for c in c1 c2 c3 c4; do
     python scripts/compara_elementos.py \
       --original dados/fase-04/brutos/M2.4.1_${c}_antes.excalidraw \
       --reimportados dados/fase-04/brutos/M2.4.1_${c}_depois.excalidraw \
       --output-json dados/fase-04/brutos/M2.4.1_${c}_comparacao.json \
       --output-csv dados/fase-04/brutos/M2.4.1_${c}_comparacao.csv
   done
   ```

   Em C4, não exportar nada entre a última edição e o encerramento. A referência é a cena inicial mais a edição registrada antes do teste, e a única diferença aceita no relatório é essa edição, e qualquer outra diferença reprova o cenário. Se a gravação não permitir confirmar o intervalo ou a edição, registrar teste inconclusivo. Não declarar `aprovado` só porque o comparador mostrou 100%.
5. Preencher **`M2.4.1_cenarios.csv`** com `cenario,acao,arquivo_antes,arquivo_depois,elementos_iguais,propriedades_iguais,resultado,observacao`. Um cenário passa somente quando **todos os elementos e propriedades** esperados são restaurados. **Calcular:** `(cenários que passam ÷ 4) × 100`. **Saída esperada:** quatro decisões e percentual de 0 a 100.

**Dados brutos:** `M2.4.1_cenarios.csv`, `M2.4.1_coleta.csv`, arquivos `M2.4.1_cN_antes.excalidraw`, `_depois.excalidraw`, relatórios `M2.4.1_cN_comparacao.json/.csv` e **quatro vídeos**.

### 5.3 M2.4.2: Proporção de arquivos reabertos sem perda

**Ficha:** [M2.4.2](../fase-02/gqm-confiabilidade.md#m242-proporção-de-arquivos-reabertos-sem-perda). **Faixa:** [seção 4, M2.4.2](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2).

1. Conferir o conjunto fixo de sete entradas em `dados/fase-03/massa-de-dados/reabertura/`, descrito no [conjunto de reabertura da massa de dados](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/dados/fase-03/massa-de-dados/README.md#4-conjunto-de-reabertura-reabertura) e na [massa definida nos recursos](./recursos-ambiente.md#6-massa-de-dados): (1) cena de referência da versão avaliada, (2) a (5) a mesma cena salva nas versões `v0.15.0`, `v0.16.4`, `v0.17.6` e `v0.18.0`, (6) `test_embedded_v1.png` e (7) `smiley_embedded_v2.png`, os dois PNGs de exemplo de `packages/excalidraw/tests/fixtures/` no commit avaliado.
2. Os arquivos das quatro versões antigas foram produzidos por [Christopher Paraizo](https://github.com/wChrstphr) na preparação da massa ([#97](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/97)), com `scripts/gerar_massa_versoes_antigas.py`. O script constrói cada versão a partir da *tag* do Excalidraw, abre a cena de referência pela interface e salva o arquivo sem alterá-lo. O [`manifesto.csv`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/dados/fase-03/massa-de-dados/reabertura/manifesto.csv) registra a origem, o SHA-256 e as perdas de cada caso, como a moldura que a `v0.15.0` não salva. Essa perda é da gravação, não da reabertura: o caso continua no conjunto e o denominador permanece sete.
3. No Firefox com a **versão avaliada** do Excalidraw em `http://localhost:3000`, iniciar OBS **`M2.4.2_gravacao_reabertura.mp4`**. Para cada um dos sete arquivos, limpar a cena de trabalho, abrir o arquivo pelo menu de importação da aplicação e exportar o estado reaberto como **`M2.4.2_cN_reaberto.excalidraw`**. Guardar a entrada copiada como **`M2.4.2_cN_entrada.ext`** (`.excalidraw` ou `.png`).
4. Comparar cada estado reaberto com sua referência original, usando o comparador e conferindo **tipo, posição, tamanho e texto**, além de elementos presentes. Nos casos 1 a 5, a referência é `M2.4.2_cN_entrada.excalidraw`. Nos casos 6 e 7 (PNG), a referência é a cena que o próprio arquivo contém, e não os pixels da prévia. Ela vem de `reabertura/c6_referencia.excalidraw` e `c7_referencia.excalidraw`, copiadas como `M2.4.2_cN_referencia.excalidraw`. Executar na raiz do repositório da avaliação:

   ```bash
   for c in c1 c2 c3 c4 c5 c6 c7; do
     case $c in
       c6|c7) ORIG=dados/fase-04/brutos/M2.4.2_${c}_referencia.excalidraw ;;
       *)     ORIG=dados/fase-04/brutos/M2.4.2_${c}_entrada.excalidraw ;;
     esac
     python scripts/compara_elementos.py \
       --original "$ORIG" \
       --reimportados dados/fase-04/brutos/M2.4.2_${c}_reaberto.excalidraw \
       --output-json dados/fase-04/brutos/M2.4.2_${c}_comparacao.json \
       --output-csv dados/fase-04/brutos/M2.4.2_${c}_comparacao.csv
   done
   ```

   Registrar qualquer perda ou alteração.
5. Preencher **`M2.4.2_arquivos.csv`** com `caso,versao_origem,arquivo_entrada,arquivo_reaberto,tipos_preservados,posicoes_preservadas,tamanhos_preservados,textos_preservados,resultado,observacao`. Arquivo aprovado = sem perda de elementos nem dessas propriedades. **Calcular:** `(arquivos reabertos sem perda ÷ arquivos do conjunto) × 100`. **Saída esperada:** quantidade de arquivos reabertos sem perda, total de arquivos do conjunto (7) e percentual correspondente. Se algum arquivo do conjunto estiver indisponível, registrar a pendência e não apresentar o resultado como definitivo.

**Dados brutos:** `M2.4.2_arquivos.csv`, `M2.4.2_coleta.csv`, `M2.4.2_c1_entrada.excalidraw` a `M2.4.2_c7_entrada.png` conforme extensão, seus `_reaberto.excalidraw`, relatórios `M2.4.2_cN_comparacao.json/.csv` e **vídeo** `M2.4.2_gravacao_reabertura.mp4`.


### 5.4 M2.4.3: Cobertura de desfazer e refazer

**Ficha:** [M2.4.3](../fase-02/gqm-confiabilidade.md#m243-cobertura-de-desfazer-e-refazer). **Faixa:** [seção 4, M2.4.3](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2).

1. Em `http://localhost:3000`, preparar uma **cena inicial conhecida** para cada ação e reiniciar o caso independentemente para que o histórico de uma ação não afete outra. Iniciar OBS em **`M2.4.3_gravacao_acoes.mp4`**.
2. Executar exatamente estes **dez tipos de ação**, um caso por vez: **A1** criar elemento, **A2** apagar elemento, **A3** mover elemento, **A4** redimensionar, **A5** girar, **A6** mudar cor/estilo, **A7** editar texto, **A8** agrupar e desagrupar, **A9** alterar ordem de sobreposição e **A10** vincular seta a uma forma. Para A8, executar dois subcasos independentes: **A8a** (agrupar) e **A8b** (desagrupar, partindo de uma cena já agrupada), cada um com os quatro estados do passo 3 e com `a8a` e `a8b` no lugar de `aN` nos nomes dos arquivos. A8 só passa se A8a e A8b passarem, e a pontuação continua sobre 10 ações.
3. Em cada caso, exportar quatro estados com os nomes **`M2.4.3_aN_antes.excalidraw`**, **`_depois.excalidraw`**, **`_desfeito.excalidraw`** e **`_refeito.excalidraw`**. Ordem: exportar antes → realizar a ação → exportar depois → `Ctrl+Z` → exportar desfeito → `Ctrl+Y` (ou o comando Refazer da interface, registrando qual foi usado) → exportar refeito. Se o comando não funcionar, registrar exatamente o comportamento, sem reconstruir o estado manualmente.
4. Comparar **antes versus desfeito** (relatório `undo`) e **depois versus refeito** (relatório `redo`) com o comparador, na raiz do repositório da avaliação, e fazer a inspeção adicional das propriedades (especialmente `angle`, `groupIds`, vínculos de setas e ordem dos elementos, não cobertos integralmente pelo comparador atual):

   ```bash
   for a in a1 a2 a3 a4 a5 a6 a7 a8a a8b a9 a10; do
     B=dados/fase-04/brutos/M2.4.3_${a}
     python scripts/compara_elementos.py \
       --original ${B}_antes.excalidraw --reimportados ${B}_desfeito.excalidraw \
       --output-json ${B}_undo.json --output-csv ${B}_undo.csv
     python scripts/compara_elementos.py \
       --original ${B}_depois.excalidraw --reimportados ${B}_refeito.excalidraw \
       --output-json ${B}_redo.json --output-csv ${B}_redo.csv
   done
   ```

   **Saída esperada:** igualdade de estado em **ambas** as comparações para considerar a ação aprovada.
5. Preencher **`M2.4.3_acoes.csv`** com `acao,descricao,antes_igual_desfeito,depois_igual_refeito,resultado,divergencias,evidencia`. Para A8, registrar uma linha `A8` com o resultado consolidado e citar A8a e A8b em `divergencias` ou `evidencia`. **Calcular:** `100 × ações aprovadas / 10`. **Saída esperada:** dez registros, percentual de 0 a 100 e evidência de cada par de comparações.

**Dados brutos:** `M2.4.3_acoes.csv`, `M2.4.3_coleta.csv`, **44 exportações** (`M2.4.3_a1_*` a `a10_*`, com `a8a` e `a8b` no lugar de `a8`), relatórios `M2.4.3_aN_undo.json/.csv`, `M2.4.3_aN_redo.json/.csv` e **vídeo** `M2.4.3_gravacao_acoes.mp4`.

## 6. Conferência final da coleta

Antes de enviar os resultados para a Fase 04, quem executou a coleta confere a lista abaixo.

- [ ] As dez métricas têm formulário `M2.X.X_coleta.csv` com responsável e horário.
- [ ] M2.1.1 a M2.1.3 possuem respostas JSON originais da API e tabelas de cálculo.
- [ ] M2.2.1 a M2.4.3 têm vídeo de tela com o nome previsto em cada seção.
- [ ] Os casos do navegador foram executados no commit, no Firefox e no ambiente especificados, ou os desvios estão explícitos.
- [ ] Os arquivos originais de teste, exportações e registros de comparação estão em `dados/fase-04/brutos/`.
- [ ] Contagens, percentuais e mediana conferem com os denominadores da Fase 02, e as ausências de dados estão identificadas.
- [ ] Cada resultado está vinculado ao seu nível da [tabela de pontuação G2](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2).
- [ ] As sete entradas de M2.4.2 conferem com o SHA-256 do `manifesto.csv`.

## Referências

> <Link id="ref-1">1.</Link> RAMOS, Cristiane Soares. **AULA A07 QSW1 PROC AVAL PRODUTO**. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Páginas 18 e 19. Disponível no Moodle da disciplina.

> <Link id="ref-2">2.</Link> RAMOS, Cristiane Soares. **AULA 08 QSW1 GQM**. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Página 51. Disponível no Moodle da disciplina.

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 10/11/2026 | Instruções de coleta das dez métricas de G2, com vínculos às Fases 02 e 03, formulários, arquivos brutos e gravações | [Letícia de Carvalho](https://github.com/LeticiaSantosss) |  |
| 1.1 | 11/11/2026 | Terminal Git Bash; regras de M2.1.2 (faixas em dias, janela, vários relatos), consolidação de M2.3.1, subcasos A8a e A8b em M2.4.3, domínio e arquivo de bloqueios em M2.2.2; `taskkill` em M2.4.1 e comandos do comparador em M2.4.1 a M2.4.3; correção de fórmulas | [Letícia de Carvalho](https://github.com/LeticiaSantosss) |  |
| 1.2 | 18/11/2026 | Revisão de coerência, cross-links e redação: Introdução, Metodologia e Referências como em G1, títulos das métricas com o nome da ficha, rastreabilidade trocada por link à visão geral | [Christopher Paraizo](https://github.com/wChrstphr) |  |
| 1.3 | 18/11/2026 | Revisão de coerência, cross-links e redação: faixas de M2.1.2 e regra de M2.3.1 linkadas à Fase 02, população de PRs elegíveis declarada, origem das versões antigas de M2.4.2, título e fonte do formulário, sem resultado prévio nem meta-frases | [Christopher Paraizo](https://github.com/wChrstphr) |  |
| 1.4 | 18/11/2026 | Revisão de coerência, cross-links e redação: posição na barra lateral da Fase 03 | [Christopher Paraizo](https://github.com/wChrstphr) | |
