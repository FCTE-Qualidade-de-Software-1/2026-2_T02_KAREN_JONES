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

Os valores calculados a partir dos dados brutos serão guardados em `consolidados/`. A verificação e a consolidação fazem parte da issue #114, e o formato dos arquivos está no [plano de análise](../../docs/fase-03/plano-analise.md#3-tabela-consolidada-e-script-de-análise).

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
| Sistema operacional e navegador | Windows 11 build 26300, Firefox 159.0.1 |
| Ferramentas e versões usadas | OBS Studio 32.1.2, Git 2.54.0, Node.js 24.20.0, npm 11.19.0, Yarn 1.22.22 via Corepack, Docker CLI 29.7.2, Docker Compose 5.4.0, GitHub CLI 2.102.0 |
| Aplicação local e porta, se necessário | Imagem criada a partir do commit avaliado, aplicação acessível em `http://localhost:3001`, com verificação de saúde aprovada. |
| Desvios e motivo | Porta 3001 em vez de 3000, que estava ocupada. Node.js nativo 24.20.0 difere da referência 24.16.0 do plano, e a imagem de referência informou 24.16.0. |
| CLI GitHub | Autenticação persistente conferida em 10/11/2026, com consultas de teste REST e GraphQL ao repositório do Excalidraw respondendo com sucesso. |
| Pendências | Sessão de início da coleta com os três responsáveis. |

Na preparação, a instalação das dependências e o build dos pacotes foram concluídos. Uma verificação adicional de cobertura apresentou 10 testes com falha e 10 erros, e as falhas precisam ser investigadas antes de usar esse procedimento na coleta de G1. Essa verificação não é um resultado de coleta.

### Ambiente de Maria Eduarda

| Item | Registro |
| :--- | :--- |
| Data da preparação | 10/11/2026 |
| Métricas | G3: M3.1.1 a M3.4.3 |
| Commit do Excalidraw conferido | `e1b7aacb356a492aa1e0fc6eb57b8896124027f0` |
| Sistema operacional e navegador | Zorin OS 18.1 (Linux), Mozilla Firefox 159.0.1 |
| Ferramentas e versões usadas | Git 2.43.0, Node.js 24.16.0, npm 11.13.0, Docker 29.9.3 (build 5457199), Docker Compose 5.7.0, Python 3.12.3 |
| Aplicação local e porta, se necessário | Imagem `excalidraw-avaliacao` criada a partir do commit avaliado, contêiner `excalidraw-avaliacao-teste` em execução com verificação de integridade aprovada, e aplicação acessível em `http://localhost:3000`. |
| Desvios e motivo | Nenhum desvio em relação ao planejado, com porta 3000 padrão utilizada com sucesso e versões de Node.js e Docker idênticas às previstas no plano de recursos e ambiente da Fase 03. |
| Pendências | Sessão de início da coleta com os três responsáveis. |

Na preparação, a imagem Docker foi gerada com sucesso via `docker build -t excalidraw-avaliacao .` e o contêiner inicializado via `docker run -d --name excalidraw-avaliacao-teste -p 3000:80 excalidraw-avaliacao`. O healthcheck respondeu com status positivo e a interface gráfica do editor no navegador respondeu com sucesso (código HTTP 200 via Nginx e canvas funcional), validando os pré-requisitos para as coletas de M3.3.2 e M3.3.3.

### Ambiente de [Christopher Paraizo](https://github.com/wChrstphr)

| Item | Registro |
| :--- | :--- |
| Data da preparação | 11/11/2026 |
| Métricas | G1: M1.1.1 a M1.5.3 |
| Commit do Excalidraw conferido | `e1b7aacb356a492aa1e0fc6eb57b8896124027f0` |
| Sistema operacional e navegador | Windows 11 Pro 25H2 build 26200.9711, com WSL2 Ubuntu 24.04.5 LTS. Navegador não se aplica. |
| Ferramentas e versões usadas | Git 2.43.0, Node.js 24.16.0, npm 11.13.0, Yarn 1.22.22 via Corepack, GitHub CLI 2.102.0, GNU grep 3.11, Madge 8.0.0, cloc 1.86, Vitest 3.0.6 com `@vitest/coverage-v8` 3.0.7, `@typescript-eslint/parser` 5.62.0 e TypeScript 5.9.3. ESLint 8.57.0 executado com `npx eslint@8.57.0`. |
| Aplicação local e porta, se necessário | Não se aplica. |
| Desvios e motivo | Nenhum. |
| CLI GitHub | Autenticação conferida em 11/11/2026. Consultas REST e GraphQL ao repositório do Excalidraw responderam com sucesso. |
| Pendências | Sessão de início da coleta com os três responsáveis. |

Na preparação, a instalação das dependências, a cobertura e o build dos pacotes foram concluídos com os comandos da [seção 2.1 dos recursos e ambiente](../../docs/fase-03/recursos-ambiente.md#21-preparação-a-partir-do-commit-avaliado). A cobertura executou os 143 arquivos de teste sem falhas com `CI=true` e 8 processos. Essa verificação não é um resultado de coleta.

Três problemas da preparação levaram a correções na seção 2.1. O `yarn` do pacote `cmdtest` do Ubuntu impedia os comandos. As 10 falhas e os 10 erros relatados no ambiente de Luiz vêm de rodar a cobertura depois de `yarn build:packages`. Sem `CI=true`, o Vitest não encerra o comando.

## Início da coleta

A sessão de início com os três responsáveis ainda precisa acontecer e ser registrada.

---

## Catálogo de Arquivos Brutos: Objetivo G3 (Flexibilidade)

### Q3.1: Adaptabilidade

| Arquivo | Métrica | Descrição |
| :--- | :---: | :--- |
| `Q3.1-adaptabilidade/M3.1.1_cobertura_browserslist.txt` | **M3.1.1** | Saída do comando oficial do Browserslist com o percentual de cobertura populacional global de navegadores. |
| `Q3.1-adaptabilidade/M3.1.2_matriz_integracao.csv` | **M3.1.2** | Matriz de avaliação das 6 combinações de integração (React 17, 18, 19 cruzados com Vite e Next.js). |
| `Q3.1-adaptabilidade/M3.1.2_build_logs.zip` | **M3.1.2** | Arquivo compactado contendo todos os logs brutos de compilação e instalação dos 6 ambientes. |
| `Q3.1-adaptabilidade/M3.1.2_evidencia_ambiente.png` | **M3.1.2** | Mosaico comprobatório com capturas de tela do canvas e desenho de formas nos ambientes validados. |
| `Q3.1-adaptabilidade/M3.1.3_formulario_toque_caneta.csv` | **M3.1.3** | Formulário de auditoria empírica das 10 ações por toque e caneta stylus no tablet iPad A16. |
| `Q3.1-adaptabilidade/M3.1.3_gravacao_toque.mp4` | **M3.1.3** | Gravação de tela oficial da execução das 10 ações de teste por toque direto com o dedo no iPad. |
| `Q3.1-adaptabilidade/M3.1.3_gravacao_caneta.mp4` | **M3.1.3** | Gravação de tela oficial da execução das 10 ações de teste com a caneta capacitiva stylus Goojodoq no iPad. |

### Q3.2: Escalabilidade

| Arquivo | Métrica | Descrição |
| :--- | :---: | :--- |
| `Q3.2-escalabilidade/M3.2.1_tempos_abertura.csv` | **M3.2.1** | Tabela com todas as repetições e medianas do tempo de abertura por escala no DevTools. |
| `Q3.2-escalabilidade/traces_abertura/` | **M3.2.1** | Perfis de rastreamento completos (`.json`) exportados da aba Performance do Chrome DevTools para cada cena e repetição. |
| `Q3.2-escalabilidade/M3.2.2_fps_edicao.csv` | **M3.2.2** | Planilha para registro das taxas de quadros por segundo (FPS) durante edição contínua. |
| `Q3.2-escalabilidade/M3.2.3_tamanho_maximo_salvamento.csv` | **M3.2.3** | Planilha para teste de estresse de salvamento e exportação de cenas grandes. |

### Q3.3: Instalabilidade

| Arquivo | Métrica | Descrição |
| :--- | :---: | :--- |
| `Q3.3-instalabilidade/M3.3.1_log_operacoes_pacote.txt` | **M3.3.1** | Log detalhado da execução de operações de pacote via npm, yarn e pnpm. |
| `Q3.3-instalabilidade/M3.3.1_resultados_pacote.csv` | **M3.3.1** | Tabela comparativa das 9 operações de pacote por gerenciador. |
| `Q3.3-instalabilidade/M3.3.2_log_reproducao_passos.txt` | **M3.3.2** | Registro textual da auditoria dos 7 passos documentados de compilação e execução local. |
| `Q3.3-instalabilidade/M3.3.2_passos_ajustes.csv` | **M3.3.2** | Tabela dos 7 passos documentados com classificação e justificativas. |
| `Q3.3-instalabilidade/M3.3.3_verificacoes_docker.csv` | **M3.3.3** | Tabela de conferência das 4 verificações de implantação com Docker (build, run, healthcheck, navegação). |

### Q3.4: Substituibilidade

| Arquivo | Métrica | Descrição |
| :--- | :---: | :--- |
| `Q3.4-substituibilidade/M3.4.1_catalogo_formatos.csv` | **M3.4.1** | Catálogo dos formatos abertos suportados pelo Excalidraw, tipos MIME e especificações de referência. |
| `Q3.4-substituibilidade/M3.4.2_preservacao_formatos.csv` | **M3.4.2** | Resumo da proporção de preservação de elementos após exportação e reimportação nos 3 formatos. |
| `Q3.4-substituibilidade/M3.4.2_relatorio_preservacao.json` | **M3.4.2** | Relatório técnico detalhado da comparação elemento a elemento realizado por `compara_elementos.py`. |
| `Q3.4-substituibilidade/M3.4.2_arquivos_reimportados.zip` | **M3.4.2** | Pacote ZIP contendo os arquivos exportados e reimportados da cena de referência. |
| `Q3.4-substituibilidade/reimportacao_arquivos/` | **M3.4.2** | Arquivos brutos gerados durante o ciclo de exportação e reimportação (.excalidraw, .png, .svg). |
| `Q3.4-substituibilidade/M3.4.3_campos_encontrados.json` | **M3.4.3** | Lista de todas as 52 propriedades reais extraídas da cena de referência do Excalidraw. |
| `Q3.4-substituibilidade/M3.4.3_conferencia_campos.csv` | **M3.4.3** | Auditoria campo a campo contra o guia oficial de especificação técnica (`json-schema.mdx`). |
| `Q3.4-substituibilidade/M3.4.3_relatorio.txt` | **M3.4.3** | Relatório de auditoria com percentual de campos documentados e lista de campos omitidos. |

---

## Catálogo de Arquivos Consolidados

| Arquivo | Finalidade e Conteúdo |
| :--- | :--- |
| `consolidados/G3_metricas_consolidadas.csv` | Tabela consolidada com as 12 métricas de G3, incluindo valores medidos, unidades, escala de 1 a 5, nível na régua, hipóteses formuladas, status e apontamento para os arquivos brutos. |
| `consolidados/G3_questoes_pontuacao.csv` | Resumo executivo das 4 questões GQM (Q3.1 Adaptabilidade, Q3.2 Escalabilidade, Q3.3 Instalabilidade, Q3.4 Substituibilidade) e da pontuação global do objetivo G3 (3,90 estrelas, Nível Bom). |

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 10/11/2026 | Organização do repositório de medidas da Fase 04 | [Luiz Henrique Soares](https://github.com/luizh-gsoares) | [Maria Eduarda](https://github.com/eduarda-ogomes) |
| 1.1 | 10/11/2026 | Registro do ambiente de medição de Maria Eduarda (G3) e validação da preparação do contêiner Docker | [Maria Eduarda](https://github.com/eduarda-ogomes) | [Luiz Henrique Soares](https://github.com/luizh-gsoares) |
| 1.2 | 11/11/2026 | Registro do ambiente de medição de Christopher (G1) | [Christopher Paraizo](https://github.com/wChrstphr) | |
| 1.3 | 11/11/2026 | Inclusão do catálogo de dados brutos e consolidados coletados para o objetivo G3 (Flexibilidade) | [Maria Eduarda](https://github.com/eduarda-ogomes) | [Christopher Paraizo](https://github.com/wChrstphr) |
