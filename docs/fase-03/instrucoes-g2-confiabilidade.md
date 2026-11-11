---
sidebar_position: 3
title: Instruções ao avaliador — G2 Confiabilidade
description: Procedimentos reproduzíveis para coletar as dez métricas de Confiabilidade na Fase 04
---

# Instruções ao avaliador — G2 Confiabilidade

## 1. Finalidade e documentos de referência

Este documento orienta o responsável pela coleta das dez métricas de G2. Ele **não altera** suas definições, fórmulas, conjuntos de teste ou faixas de julgamento: transforma as fichas da Fase 02 em passos de execução e registros verificáveis para a Fase 04.

- [GQM de Confiabilidade (G2)](../fase-02/gqm-confiabilidade.md): definição, cálculo e critérios de cada métrica.
- [Pontuação e julgamento — seção 4](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2): faixas `++`, `+`, `o`, `-` e `--`.
- [Método de avaliação — seção 2.2](./metodo-avaliacao.md#22-g2-confiabilidade): tipo de método e meio de coleta.
- [Recursos e ambiente](./recursos-ambiente.md): versões, máquina responsável, preparação e fatores de variação.
- [Massa de dados](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/dados/fase-03/massa-de-dados/README.md): cena de referência e nove arquivos inválidos.

| Métrica e ficha da Fase 02 | Método | Pontuação |
| :--- | :--- | :--- |
| [M2.1.1 — Correções integradas](../fase-02/gqm-confiabilidade.md#m211--proporção-de-correções-entre-as-contribuições-integradas) | Histórico de PRs via `gh api` | [Faixa de M2.1.1](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2) |
| [M2.1.2 — Tempo relato/correção](../fase-02/gqm-confiabilidade.md#m212--mediana-do-tempo-entre-o-relato-e-a-correção) | GitHub GraphQL | [Faixa de M2.1.2](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2) |
| [M2.1.3 — Revisão antes da integração](../fase-02/gqm-confiabilidade.md#m213--proporção-de-contribuições-revisadas-antes-da-integração) | GitHub GraphQL | [Faixa de M2.1.3](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2) |
| [M2.2.1 — Funções offline](../fase-02/gqm-confiabilidade.md#m221--proporção-de-funções-essenciais-disponíveis-sem-conexão) | Navegador | [Faixa de M2.2.1](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2) |
| [M2.2.2 — Origens externas](../fase-02/gqm-confiabilidade.md#m222--origens-externas-necessárias-para-o-editor-local) | Navegador e HAR | [Faixa de M2.2.2](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2) |
| [M2.3.1 — Arquivos inválidos](../fase-02/gqm-confiabilidade.md#m231--proporção-de-arquivos-inválidos-tratados-com-mensagem) | Navegador e massa de dados | [Faixa de M2.3.1](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2) |
| [M2.3.2 — Falha da colaboração](../fase-02/gqm-confiabilidade.md#m232--continuidade-do-editor-após-falha-da-colaboração) | Navegador, três repetições | [Faixa de M2.3.2](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2) |
| [M2.4.1 — Restauração após fechamento](../fase-02/gqm-confiabilidade.md#m241--proporção-de-cenários-de-fechamento-com-restauração-do-desenho) | Navegador e comparação de arquivos | [Faixa de M2.4.1](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2) |
| [M2.4.2 — Reabertura sem perda](../fase-02/gqm-confiabilidade.md#m242--proporção-de-arquivos-reabertos-sem-perda) | Navegador e comparação de arquivos | [Faixa de M2.4.2](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2) |
| [M2.4.3 — Desfazer/refazer](../fase-02/gqm-confiabilidade.md#m243--cobertura-de-desfazer-e-refazer) | Navegador e comparação de arquivos | [Faixa de M2.4.3](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2) |

## 2. Preparação, identificação e arquivos de evidência

### 2.1 Responsável e ambiente

O responsável indicado no [plano de recursos](./recursos-ambiente.md#3-máquinas-dos-responsáveis-pela-coleta) para **todas as métricas de G2** é **Luiz Henrique Soares**. Sua máquina é Windows 11 Home Single Language (build 26300), Intel i5-14450HX e 16 GB de RAM. Para os testes de navegador, usar **Firefox 159.0.1**, com atualizações automáticas desativadas. Se outra pessoa ou máquina executar o teste, registrar a mudança como desvio, sem apresentar a coleta como equivalente à linha de base.

Para M2.1.1–M2.1.3, usar GitHub CLI **2.102.0**, autenticada (`gh auth status`) e com acesso à API do GitHub. A janela de contribuições integradas é **18/04/2026–18/10/2026**, inclusive, sobre `excalidraw/excalidraw`, ramo `master`.

Para M2.2.1–M2.4.3, obter o Excalidraw no commit **`e1b7aacb356a492aa1e0fc6eb57b8896124027f0`**. Na raiz do repositório Excalidraw:

```bash
git checkout e1b7aacb356a492aa1e0fc6eb57b8896124027f0
git rev-parse HEAD
docker build -t excalidraw-avaliacao .
docker run -d --name excalidraw-avaliacao -p 3000:80 excalidraw-avaliacao
docker ps --filter name=excalidraw-avaliacao
```

**Saída esperada:** `git rev-parse HEAD` imprime exatamente o hash acima; `docker build` termina sem erro; `docker ps` mostra o contêiner em execução; `http://localhost:3000` carrega o editor. Não usar `docker compose` para esse ambiente: a configuração indicada no [plano](./recursos-ambiente.md#23-aplicação-em-execução-ambiente-de-teste) é a imagem de produção do `Dockerfile`.

**Separação das máquinas:** comandos de GitHub podem ser executados sem iniciar Docker; o contêiner só é necessário para os testes do editor no navegador. Não é preciso rodar as dez métricas na máquina de quem escreveu este documento: a coleta de Fase 04 pertence ao responsável designado.

### 2.2 Pasta e convenção de nomes

Todos os dados brutos e formulários devem ser colocados em `dados/fase-04/brutos/` **do repositório de avaliação Karen Jones** (não no repositório do Excalidraw). Crie a pasta, caso ainda não exista. Em um terminal Bash, na raiz do repositório de avaliação:

```bash
mkdir -p dados/fase-04/brutos
```

Em PowerShell, o equivalente é `New-Item -ItemType Directory -Force dados/fase-04/brutos`. Os comandos adiante assumem a pasta `dados/fase-04/brutos/`; onde aparecer `M2.X.X`, substituir pelo código exato da métrica. Não sobrescrever evidências de repetições: acrescentar `_r1`, `_r2`, `_r3` ou o número do caso quando indicado.

**Formulário obrigatório em toda coleta:** criar `M2.X.X_coleta.csv`, com uma linha de identificação para a execução e, nas linhas seguintes, resultados por teste. Preencher **antes** de iniciar a coleta:

| Campo | Valor a registrar |
| :--- | :--- |
| `metrica`, `avaliador` | Código M2.X.X e nome de quem executou |
| `inicio`, `fim` | Data, hora e fuso; preencher `fim` ao terminar |
| `commit`, `janela_historica` | Hash do Excalidraw; intervalo de datas quando for histórico |
| `maquina`, `sistema`, `navegador` | Equipamento, Windows/build, Firefox e versão; `n/a` se não aplicável |
| `ferramentas` | Versões usadas: `gh --version` ou Docker/Firefox e comparador existente, conforme a métrica |
| `rede`, `colaboracao` | Online/offline, bloqueios, conexão do serviço de colaboração |
| `perfil`, `cache`, `armazenamento` | Perfil do Firefox, cache limpo ou não, dados locais limpos ou preservados |
| `id_caso`, `entrada`, `acao`, `resultado`, `observacao` | Identificação, arquivo de entrada, ação realizada, passou/falhou e motivo |
| `evidencias`, `desvios` | Caminhos dos JSON, CSV, HAR, vídeos; diferença em relação ao roteiro |

Um CSV simples pode ser preenchido no Excel/LibreOffice e exportado em formato CSV; não há necessidade de desenvolver um programa de coleta. Usar `aprovado`, `reprovado` ou `nao_executado` para o resultado. **Não transformar `nao_executado` em falha nem em aprovação**: declarar a métrica incompleta.

**Vídeos:** iniciar a gravação de **toda coleta manual no navegador** com OBS Studio, mostrar data/hora e ação executada, e salvar em MP4 usando os nomes definidos abaixo. Os vídeos são evidência para [F4-C2]; capturas de tela podem complementá-los, mas não substituí-los. Não gravar credenciais, tokens ou informações pessoais de terceiros.

### 2.3 Critério de encerramento

Para cada métrica, conferir: (1) todas as entradas/PRs estão identificados; (2) os arquivos brutos têm o nome indicado; (3) o formulário contém avaliador, horário e fatores de variação; (4) o valor foi calculado com o denominador definido na Fase 02; (5) há evidência para cada aprovação ou falha; (6) o resultado foi associado à [faixa de pontuação de G2](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2). Não preencher resultados numéricos antes da execução real.

## 3. Q2.1 — Histórico de contribuições

### M2.1.1 — Proporção de correções entre as contribuições integradas

**Ficha:** [M2.1.1](../fase-02/gqm-confiabilidade.md#m211--proporção-de-correções-entre-as-contribuições-integradas). **Faixa:** [seção 4, M2.1.1](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2).

1. Com a GitHub CLI (`gh`) autenticada (`gh auth status`), consultar os *pull requests* integrados no ramo `master` do Excalidraw durante a janela histórica de **18/04/2026 a 18/10/2026**. Na raiz do repositório de avaliação, executar:

   ```bash
   gh api --method GET search/issues \
     -f q='repo:excalidraw/excalidraw is:pr is:merged base:master merged:2026-04-18..2026-10-18' \
     -F per_page=100 --paginate --slurp \
     > dados/fase-04/brutos/M2.1.1_prs_integrados.json
   ```

   **Saída esperada:** arquivo `M2.1.1_prs_integrados.json` com as respostas da API, incluindo os PRs integrados na janela. Uma consulta prévia pela interface do GitHub apresentou **150 PRs**; esse total deve ser conferido novamente na coleta. Se a API indicar mais de 1.000 resultados ou `incomplete_results=true`, subdividir a consulta em intervalos menores, salvar os arquivos separadamente e registrar a divisão utilizada. O diretório `dados/fase-04/brutos/` deve existir antes da execução.

2. Abrir `M2.1.1_prs_integrados.json`. Como foi utilizado `--slurp`, o conteúdo é uma lista de páginas; em cada página, os PRs ficam no campo `items`. Identificar para cada PR seu número (`number`), título (`title`), autor (`user.login`) e data de integração. Conferir que o total de itens retornados corresponde ao total indicado pela busca; não utilizar apenas `total_count` como se fosse a lista de PRs.

3. Registrar um PR por linha em **`M2.1.1_prs.csv`**, com as colunas `numero,titulo,autor,merged_at,escopo,automacao_excluida,elegivel,eh_fix,motivo`. Remover duplicações pelo número do PR e excluir as contribuições automáticas de **atualização de dependências e traduções**, conforme a ficha da Fase 2. Justificar cada exclusão na coluna `motivo`. Classificar como correção (`eh_fix=sim`) somente a contribuição elegível cujo título começa com `fix` (por exemplo, `fix(editor): ...`). Registrar também o escopo indicado no título, como `editor` ou `app`.

4. **Calcular:** `100 × número de PRs elegíveis classificados como fix / número total de PRs elegíveis integrados`. Registrar separadamente a distribuição das correções por escopo. **Saída esperada:** percentual entre 0 e 100, acompanhado das quantidades utilizadas no numerador e no denominador e da distribuição por escopo. Se não houver PRs elegíveis, informar que o cálculo não é possível.

**Dados brutos:** `dados/fase-04/brutos/M2.1.1_prs_integrados.json` e `dados/fase-04/brutos/M2.1.1_prs.csv`. Registrar identificação do avaliador, data, horário, versão da CLI, janela histórica, resultado e desvios em `dados/fase-04/brutos/M2.1.1_coleta.csv`. **Sem vídeo**, pois a coleta utiliza a API do GitHub.

### M2.1.2 — Mediana entre abertura do relato e integração da correção

**Ficha:** [M2.1.2](../fase-02/gqm-confiabilidade.md#m212--mediana-do-tempo-entre-o-relato-e-a-correção). **Faixa:** [seção 4, M2.1.2](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2).

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
3. Criar **`M2.1.2_pares.csv`** com `pr,issue,abertura_utc,integracao_utc,dias,observacao`. Para cada vínculo válido, calcular `(integração UTC − abertura UTC) / 86.400 segundos`, em dias corridos, conservando casas decimais. Manter uma linha por par PR–issue; não contar duas vezes o mesmo par. Registrar PRs sem vínculo à parte para medir a cobertura. A ficha define a mediana dos intervalos de relatos explicitamente vinculados, e não dos PRs sem referência.
4. Ordenar os valores de `dias`: para `n` ímpar, escolher o central; para `n` par, calcular a média dos dois centrais. Informar **mediana em dias** e `100 × PRs fix com ao menos um relato vinculado / total de PRs fix elegíveis`. **Saída esperada:** número de dias e percentual de cobertura. Sem vínculos, informar `não calculável`.

**Dados brutos:** `M2.1.2_pr_NUMERO.json` para cada correção, `M2.1.2_pares.csv` e `M2.1.2_coleta.csv`. **Sem vídeo**.

### M2.1.3 — Proporção de contribuições revisadas antes da integração

**Ficha:** [M2.1.3](../fase-02/gqm-confiabilidade.md#m213--proporção-de-contribuições-revisadas-antes-da-integração). **Faixa:** [seção 4, M2.1.3](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2).

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

2. **Saída esperada:** nome do autor, data de integração e revisões `APPROVED` com autor e horário. Se a página estiver incompleta (`hasNextPage=true`), buscar as páginas seguintes com cursor, como em M2.1.2; salvar também essas respostas.
3. Preencher **`M2.1.3_revisoes.csv`** com `pr,autor_pr,merged_at,revisor,submitted_at,aprovacao_valida,motivo`. Aprovação válida: estado `APPROVED`, revisor **diferente do autor do PR** e `submittedAt` anterior à integração. Contar **cada PR no máximo uma vez** se houver uma ou mais aprovações válidas. Checks de CI e comentários sem aprovação não contam.
4. **Calcular:** `100 × PRs elegíveis com aprovação válida / total de PRs elegíveis`. **Saída esperada:** percentual de 0 a 100. Registrar o número de PRs sem aprovação válida.

**Dados brutos:** `M2.1.3_pr_NUMERO.json`, `M2.1.3_revisoes.csv` e `M2.1.3_coleta.csv`. **Sem vídeo**.

## 4. Q2.2 — Disponibilidade

### M2.2.1 — Dez funções essenciais sem conexão

**Ficha:** [M2.2.1](../fase-02/gqm-confiabilidade.md#m221--proporção-de-funções-essenciais-disponíveis-sem-conexão). **Faixa:** [seção 4, M2.2.1](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2).

1. Abrir `http://localhost:3000` **online** no Firefox. No DevTools (`F12`), abrir **Aplicativo/Armazenamento → Service Workers** (a denominação pode variar com o idioma), verificar que há um trabalhador registrado e ativado; registrar seu estado no formulário. Aguardar o carregamento completo.
2. Iniciar OBS, **`M2.2.1_gravacao_offline.mp4`**. Em **Rede/Network** do DevTools, ativar **Offline**. Não desativar o servidor Docker: o objetivo é testar o navegador sem rede após o carregamento inicial.
3. Executar **nesta ordem** e registrar cada resultado: (1) recarregar a página e ver o editor; (2) criar retângulo e elipse; (3) escrever texto; (4) mover e redimensionar; (5) desfazer e refazer; (6) salvar `.excalidraw`; (7) reabrir o arquivo salvo; (8) exportar PNG; (9) exportar SVG; (10) verificar texto legível na fonte padrão. Para itens com saída, comprovar que o arquivo foi realmente gerado ou reaberto.
4. Preencher **`M2.2.1_funcoes.csv`** com `item,funcao,resultado,evidencia,observacao`. Uma função recebe `aprovado` apenas se for concluída offline. Voltar ao estado online ao terminar.
5. **Calcular:** `100 × funções aprovadas / 10`. **Saída esperada:** dez registros e percentual. Anexar os arquivos exportados com prefixo `M2.2.1_` quando necessários à evidência.

**Dados brutos:** `M2.2.1_funcoes.csv`, `M2.2.1_coleta.csv`, exports `M2.2.1_*` e **vídeo** `M2.2.1_gravacao_offline.mp4`.

### M2.2.2 — Domínios externos necessários ao desenho local

**Ficha:** [M2.2.2](../fase-02/gqm-confiabilidade.md#m222--origens-externas-necessárias-para-o-editor-local). **Faixa:** [seção 4, M2.2.2](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2).

1. Começar **sem sessão de colaboração**. Em um perfil limpo do Firefox, abrir DevTools (`F12`) → **Rede/Network**; desativar cache na aba de rede e limpar cache/armazenamento do site em **Armazenamento/Storage**. Ativar preservação do registro de rede.
2. Iniciar OBS em **`M2.2.2_gravacao_bloqueios.mp4`**. Abrir `http://localhost:3000`, aguardar o término dos carregamentos e exportar a lista de requisições pelo menu **Salvar tudo como HAR** em **`M2.2.2_abertura.har`**.
3. Do HAR, listar as **origens/domínios distintos** das URLs requisitadas, excluindo apenas `localhost:3000` (origem local). Preencher **`M2.2.2_dominios.csv`** com `dominio,urls_observadas,eh_externo,indispensavel,resultado_forma,resultado_texto,observacao`.
4. Para **cada domínio externo isoladamente**, usar o bloqueio de URLs/requisições do DevTools para bloquear `*://DOMINIO/*` (ou o padrão equivalente que a ferramenta aceitar), limpar o cache, recarregar a página e tentar **criar uma forma e um texto**. Retirar esse bloqueio antes de testar o próximo domínio. Anotar mensagens no console, falhas na rede e se o editor ainda desenha. Se o recurso do Firefox não aceitar o padrão, registrar o padrão efetivamente aplicado e verificar no painel de rede se o bloqueio ocorreu.
5. Marcar `indispensavel=sim` **somente** se bloquear aquele domínio impedir criar forma **ou** texto; caso contrário, `não`. **Saída esperada:** total de domínios externos distintos e quantos são indispensáveis, não um percentual. A pontuação da Fase 02 usa **ambas** as contagens.

**Dados brutos:** `M2.2.2_abertura.har`, `M2.2.2_dominios.csv`, `M2.2.2_coleta.csv` e **vídeo** `M2.2.2_gravacao_bloqueios.mp4`.

## 5. Q2.3 — Tolerância a falhas

### M2.3.1 — Nove arquivos inválidos tratados com mensagem

**Ficha:** [M2.3.1](../fase-02/gqm-confiabilidade.md#m231--proporção-de-arquivos-inválidos-tratados-com-mensagem). **Faixa:** [seção 4, M2.3.1](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2).

1. Confirmar a presença dos **nove arquivos** em `dados/fase-03/massa-de-dados/invalidos/`, identificados de `invalido_01_*` a `invalido_09_*`; consultar os nomes e defeitos na [tabela da massa](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/dados/fase-03/massa-de-dados/README.md).
2. Iniciar OBS em **`M2.3.1_gravacao_menu.mp4`**. Para cada arquivo, abrir o editor em estado inicial, usar **Abrir** no menu de arquivos e selecionar a entrada. Registrar se apareceu mensagem de erro (transcrever seu texto) e se é possível criar um retângulo **sem recarregar**. Repetir com os nove arquivos, reiniciando a cena/aba antes de cada tentativa.
3. Iniciar segunda gravação **`M2.3.1_gravacao_arrastar.mp4`** e repetir as nove entradas, agora por **arrastar e soltar** no editor. Para arquivos `.png`, observar e registrar se o navegador o trata como imagem comum em vez de importação de desenho; aplicar a condição de mensagem prevista na ficha e não ocultar essa diferença entre fluxos.
4. Preencher **`M2.3.1_tentativas.csv`** com `arquivo,via,mensagem_exibida,texto_mensagem,retangulo_criado,caso_tratado,observacao` (18 linhas: nove × duas vias). Um arquivo só conta como **caso tratado** se **nas duas vias** houver mensagem de erro **e** o editor continuar utilizável sem recarga. Se o comportamento das duas vias divergir, marcar o arquivo como não aprovado e explicar.
5. **Calcular:** `100 × número de arquivos tratados nas duas vias / 9`. **Saída esperada:** nove decisões consolidadas, percentual de 0 a 100 e registros das 18 tentativas.

**Dados brutos:** `M2.3.1_tentativas.csv`, `M2.3.1_coleta.csv` e **vídeos** `M2.3.1_gravacao_menu.mp4`, `M2.3.1_gravacao_arrastar.mp4`.

### M2.3.2 — Continuidade após falha da colaboração

**Ficha:** [M2.3.2](../fase-02/gqm-confiabilidade.md#m232--continuidade-do-editor-após-falha-da-colaboração). **Faixa:** [seção 4, M2.3.2](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2).

1. Com a internet **online** e a aplicação local aberta, criar sessão de colaboração pelo recurso **Live collaboration/Colaboração**, copiar o link e abri-lo em **segunda janela** do Firefox. Confirmar que um retângulo criado na janela A aparece na janela B **antes** da interrupção. Registrar se o serviço público estava disponível; se não estava, interromper e registrar `nao_executado`, sem atribuir automaticamente uma falha ao cliente.
2. Iniciar OBS em **`M2.3.2_gravacao_r1.mp4`**. Na janela A, ativar **Offline** em DevTools → Rede. Verificar: **V1** desenho permanece visível; **V2** ainda é possível criar e editar um elemento; **V3** há aviso de desconexão; **V4** é possível salvar `.excalidraw`; **V5** após desativar Offline, a edição feita sem conexão aparece na janela B. Aguardar a reconexão e registrar o tempo de espera para V5.
3. Repetir todo o teste **três vezes**, criando estado inicial verificável e salvando as gravações em **`M2.3.2_gravacao_r1.mp4`**, **`_r2.mp4`**, **`_r3.mp4`**; manter a segunda janela visível no vídeo ao conferir a sincronização. Guardar os arquivos salvos como `M2.3.2_desenho_r1.excalidraw` etc.
4. Preencher **`M2.3.2_verificacoes.csv`** com `repeticao,verificacao,resultado,evidencia,observacao`, total de 15 linhas. Uma verificação é aprovada **somente se passar nas três repetições**.
5. **Calcular:** `100 × verificações aprovadas / 5`. **Saída esperada:** percentual em incrementos de 20. A hipótese H2.3.2, separadamente, depende de **V1 a V4**; V5 mede a volta da colaboração. A conclusão refere-se ao **cliente** e à disponibilidade observada do serviço público no momento, sem avaliar a infraestrutura do servidor.

**Dados brutos:** `M2.3.2_verificacoes.csv`, `M2.3.2_coleta.csv`, `M2.3.2_desenho_r1.excalidraw` a `_r3.excalidraw`, **três vídeos** com sufixos `_r1`, `_r2`, `_r3`.

## 6. Q2.4 — Recuperabilidade

### Comparação das exportações (M2.4.1 a M2.4.3)

Os três métodos da [Fase 03](./metodo-avaliacao.md#22-g2-confiabilidade) exigem **comparar os elementos dos arquivos `.excalidraw`**, não decidir pela aparência da tela. Há no projeto um comparador **já existente**, `scripts/compara_elementos.py`, descrito originalmente para M3.4.2. Quando ele for usado, executar **na raiz do repositório Karen Jones**:

```bash
python scripts/compara_elementos.py \
  --original dados/fase-04/brutos/ORIGINAL.excalidraw \
  --reimportados dados/fase-04/brutos/RESULTADO.excalidraw \
  --output-json dados/fase-04/brutos/RELATORIO.json \
  --output-csv dados/fase-04/brutos/RELATORIO.csv
```

Substituir os nomes pelos arquivos de cada caso. **Saída esperada:** JSON/CSV com elementos preservados, diferenças e percentual. **Atenção:** esse comparador foi criado para M3.4.2; verifica tipo, posição, tamanho, estilo básico e texto com tolerância, mas **não garante igualdade completa** de rotação, agrupamento, vínculos de setas, arquivos incorporados nem ausência de elementos extras. Portanto, para M2.4.1 e M2.4.3 conferir também essas propriedades no JSON original e no exportado, usando um editor de texto, e registrar as diferenças no CSV do caso. **Não declarar `aprovado` apenas porque o comparador mostrou 100%**. O uso desse arquivo existente não pede criar um novo script; registrar a versão de Python usada como fator de variação, caso ele seja executado.

### M2.4.1 — Restauração após quatro formas de fechamento

**Ficha:** [M2.4.1](../fase-02/gqm-confiabilidade.md#m241--proporção-de-cenários-de-fechamento-com-restauração-do-desenho). **Faixa:** [seção 4, M2.4.1](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2).

1. Usar `dados/fase-03/massa-de-dados/cena_referencia.excalidraw` como cena inicial (dez elementos). Abrir pela interface do Excalidraw, aguardar o salvamento local e exportar **`M2.4.1_cN_antes.excalidraw`**, substituindo `N` pelo cenário. **Não limpar o armazenamento local entre fechar e reabrir**, porque ele é justamente o objeto avaliado.
2. Iniciar uma gravação por cenário (`M2.4.1_gravacao_c1.mp4` até `_c4.mp4`) e testar **separadamente**: **C1** recarregar a página; **C2** fechar a aba e reabrir `http://localhost:3000`; **C3** encerrar o Firefox normalmente e reabrir; **C4** depois de exportar o estado inicial, executar **uma última edição definida** (por exemplo, mover o retângulo exatamente 20 unidades à direita, registrando a posição esperada), esperar **1 segundo** e **forçar o encerramento do processo do Firefox no Windows** pelo Gerenciador de Tarefas → Detalhes → `firefox.exe` → Finalizar tarefa; registrar o processo escolhido e o horário. Para C3/C4, usar perfil de teste próprio e confirmar que não há sessões pessoais em risco.
3. Ao reabrir a aplicação, sem importar manualmente o arquivo inicial, exportar o desenho **restaurado** como **`M2.4.1_cN_depois.excalidraw`**. Se não houver desenho, salvar evidência da tela e registrar falha; não importar a cena para mascarar a perda.
4. Comparar cada par com o comparador disponível e a verificação adicional indicada acima. **Exceção controlada em C4:** não exportar um arquivo entre a última edição e a interrupção, pois isso alteraria o intervalo de um segundo. A referência é a cena inicial **mais a mudança exata registrada antes do teste**; conferir no JSON restaurado a nova posição/propriedade e os demais elementos inalterados. O arquivo `_antes.excalidraw` documenta a cena antes dessa mudança. Se a gravação não permitir confirmar o tempo ou a posição esperada, registrar teste inconclusivo.
5. Preencher **`M2.4.1_cenarios.csv`** com `cenario,acao,arquivo_antes,arquivo_depois,elementos_iguais,propriedades_iguais,resultado,observacao`. Um cenário passa somente quando **todos os elementos e propriedades** esperados são restaurados. **Calcular:** `100 × cenários aprovados / 4`. **Saída esperada:** quatro decisões e percentual de 0 a 100.

**Dados brutos:** `M2.4.1_cenarios.csv`, `M2.4.1_coleta.csv`, arquivos `M2.4.1_cN_antes.excalidraw`, `_depois.excalidraw`, relatórios `M2.4.1_cN_comparacao.json/.csv` e **quatro vídeos**.

### M2.4.2 — Reabertura dos sete arquivos sem perda

**Ficha:** [M2.4.2](../fase-02/gqm-confiabilidade.md#m242--proporção-de-arquivos-reabertos-sem-perda). **Faixa:** [seção 4, M2.4.2](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2).

1. Conferir o conjunto **fixo de sete entradas**, conforme a [massa definida nos recursos](./recursos-ambiente.md#6-massa-de-dados): **(1)** cena de referência salva na versão avaliada; **(2)** cena salva na versão `v0.15.0`; **(3)** `v0.16.4`; **(4)** `v0.17.6`; **(5)** `v0.18.0`; **(6)** `packages/excalidraw/tests/fixtures/test_embedded_v1.png`; **(7)** `packages/excalidraw/tests/fixtures/smiley_embedded_v2.png`. Os PNGs devem ser obtidos da árvore do Excalidraw no commit indicado; não substituí-los por PNGs comuns.
2. Os arquivos das quatro versões antigas são **produtos da preparação da massa (#97)**, não arquivos inventados nesta instrução: abrir cada versão correspondente, montar/salvar a cena compatível no formato `.excalidraw`, identificar a versão produtora e guardar **também a exportação original para comparação**. Se a versão antiga não suporta determinado tipo da cena atual (por exemplo, moldura), registrar essa incompatibilidade e resolver a definição da entrada com a equipe responsável por #97 **antes** da medição; não omitir a versão nem alterar silenciosamente o denominador sete.
3. No Firefox com a **versão avaliada** do Excalidraw em `http://localhost:3000`, iniciar OBS **`M2.4.2_gravacao_reabertura.mp4`**. Para cada um dos sete arquivos, limpar a cena de trabalho, abrir o arquivo pelo menu de importação da aplicação e exportar o estado reaberto como **`M2.4.2_cN_reaberto.excalidraw`**. Guardar a entrada copiada como **`M2.4.2_cN_entrada.ext`** (`.excalidraw` ou `.png`).
4. Comparar cada estado reaberto com sua referência original, usando a comparação existente e conferindo **tipo, posição, tamanho e texto**, além de elementos presentes. Para os PNGs embutidos, usar como referência a cena que o próprio arquivo contém, extraída/aberta pelo editor, **não** os pixels da imagem de prévia. Registrar qualquer perda ou alteração.
5. Preencher **`M2.4.2_arquivos.csv`** com `caso,versao_origem,arquivo_entrada,arquivo_reaberto,tipos_preservados,posicoes_preservadas,tamanhos_preservados,textos_preservados,resultado,observacao`. Arquivo aprovado = sem perda de elementos nem dessas propriedades. **Calcular:** `100 × arquivos aprovados / 7`. **Saída esperada:** sete decisões. **Se faltar qualquer um dos sete arquivos, registrar `nao_executado` e não publicar percentual como resultado definitivo.**

**Dados brutos:** `M2.4.2_arquivos.csv`, `M2.4.2_coleta.csv`, `M2.4.2_c1_entrada.excalidraw` a `M2.4.2_c7_entrada.png` conforme extensão, seus `_reaberto.excalidraw`, relatórios `M2.4.2_cN_comparacao.json/.csv` e **vídeo** `M2.4.2_gravacao_reabertura.mp4`.

**Pendência de dependência:** o README atual de `dados/fase-03/massa-de-dados/` descreve a cena e os inválidos, mas não disponibiliza os quatro `.excalidraw` históricos. Essa parte depende da conclusão/verificação da **issue #97**. O procedimento acima não considera arquivos ainda não gerados como medições realizadas.

### M2.4.3 — Dez ações com desfazer e refazer

**Ficha:** [M2.4.3](../fase-02/gqm-confiabilidade.md#m243--cobertura-de-desfazer-e-refazer). **Faixa:** [seção 4, M2.4.3](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2).

1. Em `http://localhost:3000`, preparar uma **cena inicial conhecida** para cada ação; reiniciar o caso independentemente para que o histórico de uma ação não afete outra. Iniciar OBS em **`M2.4.3_gravacao_acoes.mp4`**.
2. Executar exatamente estes **dez tipos de ação**, um caso por vez: **A1** criar elemento; **A2** apagar elemento; **A3** mover elemento; **A4** redimensionar; **A5** girar; **A6** mudar cor/estilo; **A7** editar texto; **A8** agrupar e desagrupar; **A9** alterar ordem de sobreposição; **A10** vincular seta a uma forma. Para A8, registrar separadamente o agrupamento e o desagrupamento dentro do mesmo caso e comprovar o retorno do estado de ambos.
3. Em cada caso, exportar quatro estados com os nomes **`M2.4.3_aN_antes.excalidraw`**, **`_depois.excalidraw`**, **`_desfeito.excalidraw`** e **`_refeito.excalidraw`**. Ordem: exportar antes → realizar a ação → exportar depois → `Ctrl+Z` → exportar desfeito → `Ctrl+Y` (ou o comando Refazer da interface, registrando qual foi usado) → exportar refeito. Se o comando não funcionar, registrar exatamente o comportamento, sem reconstruir o estado manualmente.
4. Comparar **antes versus desfeito** e **depois versus refeito** com o comparador disponível e a inspeção adicional das propriedades (especialmente `angle`, `groupIds`, vínculos de setas e ordem dos elementos, não cobertos integralmente pelo comparador atual). **Saída esperada:** igualdade de estado em **ambas** as comparações para considerar a ação aprovada.
5. Preencher **`M2.4.3_acoes.csv`** com `acao,descricao,antes_igual_desfeito,depois_igual_refeito,resultado,divergencias,evidencia`. **Calcular:** `100 × ações aprovadas / 10`. **Saída esperada:** dez registros, percentual de 0 a 100 e evidência de cada par de comparações.

**Dados brutos:** `M2.4.3_acoes.csv`, `M2.4.3_coleta.csv`, **40 exportações** (`M2.4.3_a1_*` a `a10_*`), relatórios `M2.4.3_aN_undo.json/.csv`, `M2.4.3_aN_redo.json/.csv` e **vídeo** `M2.4.3_gravacao_acoes.mp4`.

## 7. Conferência final da coleta

Antes de enviar os resultados para a Fase 04, quem executou deve revisar a lista abaixo. O documento de instruções pode ser entregue na Fase 03 **antes** de realizar as coletas: os CSVs, HARs, vídeos e resultados são produzidos **somente na Fase 04**.

- [ ] As dez métricas têm formulário `M2.X.X_coleta.csv` com responsável e horário.
- [ ] M2.1.1–M2.1.3 possuem respostas JSON originais da API e tabelas de cálculo.
- [ ] M2.2.1–M2.4.3 têm vídeo de tela com o nome previsto em cada seção.
- [ ] Os casos do navegador foram executados no commit, no Firefox e no ambiente especificados, ou os desvios estão explícitos.
- [ ] Os arquivos originais de teste, exportações e registros de comparação estão em `dados/fase-04/brutos/`.
- [ ] Contagens, percentuais e mediana conferem com os denominadores da Fase 02; ausências de dados estão identificadas.
- [ ] Cada resultado está vinculado ao seu nível da [tabela de pontuação G2](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2).
- [ ] A massa de sete arquivos de M2.4.2 foi efetivamente disponibilizada/validada pela issue #97 antes de declarar a métrica concluída.

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 10/11/2026 | Instruções de coleta das dez métricas de G2, com vínculos às Fases 02 e 03, formulários, arquivos brutos e gravações | [Letícia Santos](https://github.com/LeticiaSantosss) | A definir |