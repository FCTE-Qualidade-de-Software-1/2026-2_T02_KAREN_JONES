# Repositório de medidas da Fase 04

Esta pasta reúne os dados da avaliação do Excalidraw na Fase 04. Todas as coletas devem usar o commit `e1b7aacb356a492aa1e0fc6eb57b8896124027f0`. Para as métricas históricas, a janela é de 18/04/2026 a 18/10/2026.

## Organização

| Pasta | Conteúdo |
| :--- | :--- |
| `brutos/` | Saídas de ferramentas, respostas da API, formulários preenchidos, capturas, gravações e fatores de variação de cada coleta. |
| `consolidados/` | Valores calculados a partir dos dados brutos e, posteriormente, os níveis e julgamentos gerados pela análise. |

Os arquivos `.gitkeep` apenas mantêm as pastas vazias no Git. Os arquivos de entrada para os testes estão na [massa de dados da Fase 03](../fase-03/massa-de-dados/README.md).

## Como guardar as coletas

1. Salve os resultados originais e as evidências em `brutos/`. Use nomes que identifiquem a métrica, como `M3.1.1_cobertura_browserslist.txt`. Se as instruções da métrica indicarem outro nome ou formato, siga essas instruções.
2. Registre junto dos dados brutos as condições da coleta, como responsável, data, versões das ferramentas e desvios. Para G1, use `M<código>_fatores.md`. Os campos completos estão na [seção 9 dos recursos e ambiente](../../docs/fase-03/recursos-ambiente.md#9-fatores-de-variação-registrados-em-cada-coleta).
3. Grave os testes manuais conforme as instruções de cada métrica. Antes de enviar evidências ao repositório, confira se não contêm dados pessoais ou credenciais. Para arquivos acima do limite do Git, siga as [instruções de G3](../../docs/fase-03/instrucoes-g3-flexibilidade.md#23-política-obrigatória-de-gravação-de-tela-para-testes-no-navegador).

Os valores calculados a partir dos dados brutos serão guardados em `consolidados/`. A verificação e a consolidação fazem parte da issue #114; o formato dos arquivos está no [plano de análise](../../docs/fase-03/plano-analise.md#3-tabela-consolidada-e-script-de-análise).

## Registro do ambiente

Cada responsável deve preparar e conferir seu próprio ambiente conforme o [plano de recursos e ambiente](../../docs/fase-03/recursos-ambiente.md). A cópia e o contêiner preparados em uma máquina não são compartilhados automaticamente com as demais.

Copie o modelo abaixo e acrescente seu registro nesta seção. Preencha somente o que for aplicável às suas métricas e indique o que ainda estiver pendente. Se usar versões, portas ou condições diferentes das previstas no plano, registre o desvio e o motivo.

### Modelo para copiar

```markdown
### Ambiente de [nome]

| Item | Registro |
| :--- | :--- |
| Data da preparação | |
| Métricas | |
| Commit do Excalidraw conferido | |
| Sistema operacional e navegador | |
| Ferramentas e versões usadas | |
| Aplicação local e porta, se necessário | |
| Desvios e motivo | |
| Pendências | |
```

Este registro é da preparação. As condições específicas de cada medição também devem ser registradas junto dos dados brutos.

### Ambiente de Luiz Henrique Soares

| Item | Registro |
| :--- | :--- |
| Data da preparação | 10/11/2026 |
| Métricas | G2: M2.1.1 a M2.4.3 |
| Commit do Excalidraw conferido | `e1b7aacb356a492aa1e0fc6eb57b8896124027f0` |
| Sistema operacional e navegador | Windows 11 build 26300; Firefox 159.0.1 |
| Ferramentas e versões usadas | OBS Studio 32.1.2; Git 2.54.0; Node.js 24.20.0; npm 11.19.0; Yarn 1.22.22 via Corepack; Docker CLI 29.7.2; Docker Compose 5.4.0; GitHub CLI 2.102.0 |
| Aplicação local e porta, se necessário | Imagem criada a partir do commit avaliado; aplicação acessível em `http://localhost:3001`, com verificação de saúde aprovada. |
| Desvios e motivo | Porta 3001 em vez de 3000, que estava ocupada. Node.js nativo 24.20.0 difere da referência 24.16.0 do plano; a imagem de referência informou 24.16.0. |
| CLI GitHub | Autenticação persistente conferida em 10/11/2026; consultas de teste REST e GraphQL ao repositório do Excalidraw responderam com sucesso. |
| Pendências | Sessão de início da coleta com os três responsáveis. |

Na preparação, a instalação das dependências e o build dos pacotes foram concluídos. Uma verificação adicional de cobertura apresentou 10 testes com falha e 10 erros; as falhas precisam ser investigadas antes de usar esse procedimento na coleta de G1. Essa verificação não é um resultado de coleta.

## Início da coleta

A sessão de início com os três responsáveis ainda precisa acontecer e ser registrada.

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 10/11/2026 | Organização do repositório de medidas da Fase 04 | Luiz Henrique Soares | |
