# Repositório de medidas da Fase 04

Esta pasta reúne os dados usados para avaliar o Excalidraw na Fase 04. A linha de base do produto é o commit `e1b7aacb356a492aa1e0fc6eb57b8896124027f0`; a janela das métricas históricas vai de 18/04/2026 a 18/10/2026. Não se deve iniciar a coleta se o commit efetivamente avaliado for diferente.

## Organização

| Pasta | Conteúdo |
| :--- | :--- |
| `brutos/` | Saídas de ferramentas, respostas da API, formulários preenchidos, capturas, gravações e fatores de variação de cada coleta. |
| `consolidados/` | Valores calculados a partir dos dados brutos e, posteriormente, os níveis e julgamentos gerados pela análise. |

Os arquivos `.gitkeep` mantêm as pastas disponíveis antes da coleta e não representam medições. Os dados de entrada preparados para os testes estão em [massa de dados da Fase 03](../fase-03/massa-de-dados/README.md).

## Nomes e rastreabilidade

Os dados brutos seguem o padrão `M<código>_<identificador-curto>.<extensão>`, por exemplo `M3.1.1_cobertura_browserslist.txt`. Os nomes específicos e formatos previstos nas instruções de cada métrica têm precedência sobre qualquer exemplo deste README. Os registros de fatores de G1 usam `M<código>_fatores.md`; para as demais coletas, siga as instruções correspondentes e registre os fatores junto aos dados brutos.

Cada coleta deve registrar responsável, início e fim, commit, máquina, sistema operacional e navegador, versões das ferramentas, rede, estado do armazenamento, evidências e desvios aplicáveis. Para métricas históricas, registre também a janela e a data da consulta. Os campos completos constam na [seção 9 dos recursos e ambiente](../../docs/fase-03/recursos-ambiente.md#9-fatores-de-variação-registrados-em-cada-coleta).

Os testes manuais devem ter gravação de tela conforme o plano. Antes de versionar qualquer evidência, confira se ela contém dados pessoais, credenciais ou informações sensíveis. Para arquivos que excedam o limite do Git, siga as instruções da equipe, registrando o link e o hash SHA-256 conforme as [instruções de G3](../../docs/fase-03/instrucoes-g3-flexibilidade.md#23-política-obrigatória-de-gravação-de-tela-para-testes-no-navegador).

## Consolidação

A verificação independente dos dados e o cálculo das métricas pertencem à issue #114. Conforme o [plano de análise](../../docs/fase-03/plano-analise.md#3-tabela-consolidada-e-script-de-análise), `consolidados/metricas.csv` reunirá os valores, com as colunas `metrica`, `item`, `valor`, `unidade`, `status`, `motivo`, `arquivo_bruto`, `data` e `avaliador`. Cada valor deve apontar para sua evidência bruta. Os arquivos `niveis.csv`, `questoes.csv` e `caracteristicas.csv` serão produzidos na análise posterior; nenhum deles foi criado com resultados fictícios.

## Situação da preparação

A preparação do ambiente é feita de acordo com [recursos e ambiente de avaliação](../../docs/fase-03/recursos-ambiente.md). A disponibilidade de ferramentas, a aplicação local e os desvios devem ser verificados em cada máquina antes de sua coleta. A sessão de início da coleta com os três responsáveis ainda precisa ocorrer e ser registrada; este README não a substitui.

Na preparação local de 10/11/2026, foi verificada uma cópia isolada do Excalidraw no commit integral da linha de base. Na máquina de Luiz, foram identificados Windows 11 build 26300, Firefox 159.0.1, OBS Studio 32.1.2, Git 2.54.0, Node.js 24.20.0, npm 11.19.0, Docker CLI 29.7.2 e Docker Compose 5.4.0. O Node.js nativo difere da referência 24.16.0 do plano e deve ser registrado como fator de variação quando utilizado.

O comando `yarn` não está no `PATH`; o Corepack forneceu Yarn 1.22.22. Na cópia isolada, `corepack yarn --frozen-lockfile --network-timeout 600000` e `corepack yarn build:packages` foram concluídos com sucesso.

Após o início do Docker Desktop, a imagem `excalidraw-avaliacao` foi construída com o `Dockerfile` da linha de base. O contêiner `excalidraw-avaliacao` iniciou, a verificação de saúde retornou `healthy` e a aplicação carregou em `http://localhost:3001` com resposta HTTP 200. A porta 3001 foi usada em vez da 3000 prevista no plano porque a porta 3000 estava ocupada; esse desvio deve ser registrado nas coletas que usarem esse ambiente. O endereço foi vinculado somente à interface local.

A CLI GitHub `gh` 2.102.0 foi instalada. As consultas REST e GraphQL ao repositório do Excalidraw foram verificadas com uma credencial temporária. A autenticação persistente não foi concluída: a credencial disponível não tinha o escopo `read:org` exigido pelo login da CLI. Antes da coleta das métricas históricas, é necessário concluir a autenticação e verificar as consultas na máquina utilizada.

Em uma verificação pontual com a imagem de referência Node.js 24, o contêiner informou Node.js 24.16.0, npm 11.13.0 e Yarn 1.22.22; o pnpm não estava instalado. Na cópia isolada, `corepack yarn test:coverage` apresentou 10 testes com falha, 2.517 aprovados, 47 ignorados e 1 pendente, além de 10 erros. A execução também alertou para versões diferentes do Vitest (3.0.6) e do provedor de cobertura (3.0.7). As falhas precisam ser investigadas antes de usar esse procedimento para a coleta. Essas verificações de preparação não são dados de coleta.

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 10/11/2026 | Organização do repositório de medidas da Fase 04 | Luiz Henrique Soares | |
