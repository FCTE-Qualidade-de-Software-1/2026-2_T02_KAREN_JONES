---
sidebar_position: 0.5
title: Método de avaliação e justificativa por métrica
description: Método de obtenção, ferramenta e justificativa de cada uma das 36 métricas GQM da avaliação do Excalidraw, ligados às fichas e às faixas de pontuação da Fase 02.
---

import Link from '@docusaurus/Link';

# Método de avaliação e justificativa por métrica

## Introdução

O plano de avaliação deve definir o método de avaliação e explicar como usá-lo, para que o avaliador possa executar a avaliação completamente [[1, p. 18]](#ref-1). O Plano de Medição também deve indicar o meio de coleta de cada medida, por formulário ou por ferramenta [[2, p. 45]](#ref-2).

O objetivo desta página é definir e justificar o método de obtenção de cada uma das 36 métricas de [G1](../fase-02/gqm-manutenibilidade.md) (14), [G2](../fase-02/gqm-confiabilidade.md) (10) e [G3](../fase-02/gqm-flexibilidade.md) (12).

## Metodologia

Cada método parte do procedimento de coleta da ficha da métrica na Fase 02 e do valor que a métrica precisa entregar às faixas dos [níveis de pontuação](../fase-02/pontuacao-julgamento.md). As métricas, as fórmulas e as faixas não mudam aqui. O commit avaliado, a janela histórica e as versões das ferramentas estão na [linha de base](./recursos-ambiente.md#1-linha-de-base) e nas [ferramentas](./recursos-ambiente.md#5-ferramentas-de-análise-e-suas-versões) da página de recursos, e as populações (código de produção, pacotes de base, suítes, contribuições integradas) seguem as seções 2 dos três GQM.

O passo a passo de cada métrica está nas instruções para o avaliador de [G1](./instrucoes-g1-manutenibilidade.md), de G2 ([#99](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/99)) e de [G3](./instrucoes-g3-flexibilidade.md).

---

## 1. Classes de método

Cada métrica usa uma classe de método ou a combinação de duas, como AE + MH quando os dados vêm do código e dos *pull requests*. Nenhum procedimento troca a unidade da métrica, por exemplo contando arquivos quando a ficha pede linhas, ou ciclos de arquivos quando ela pede pares de pacotes.

<p className="tabela-titulo">Tabela 1: Classes de método</p>

| Código | Classe | Como funciona |
| :--- | :--- | :--- |
| AE | Análise estática | Extração automatizada de propriedades do código, das configurações e das dependências no commit avaliado. |
| MH | Mineração de histórico | Consultas paginadas à API do GitHub, com janela e filtros fixos. A resposta bruta é guardada. |
| ID | Inspeção documental | Lista de verificação com itens definidos antes da coleta e, para cada item, o caminho e o trecho que o comprovam. A simples menção a um termo não basta. |
| TA | Teste automatizado | Execução de testes ou scripts, com a saída e o ambiente registrados. |
| TM | Teste manual roteirizado | Cenário, entradas, sequência de ações e condição de aprovação definidos antes da execução, com formulário e gravação de tela. |
| MD | Medição de desempenho | Instrumentação do navegador na máquina definida, com as repetições e a estatística da Fase 02. |
| EA | Experimentação em ambiente limpo | Instalação, compilação e operação em contêiner ou projeto mínimo, com as versões registradas. |

<p className="tabela-fonte">Fonte: [Davi Pierre](https://github.com/DaviPierre), 2026.</p>

---

## 2. Matriz de métodos por métrica

Cada linha liga a métrica à sua ficha e explica por que o método entrega o dado que a faixa de pontuação precisa.

### 2.1 G1: Manutenibilidade

Os valores são convertidos em nível pelas [faixas de G1](../fase-02/pontuacao-julgamento.md#3-níveis-das-métricas-de-manutenibilidade-g1).

<p className="tabela-titulo">Tabela 2: Métodos das métricas de G1</p>

| Métrica | Método e fonte de dados | Ferramenta e evidência | Justificativa |
| :--- | :--- | :--- | :--- |
| [M1.1.1](../fase-02/gqm-manutenibilidade.md#m111-ciclos-de-dependência-entre-pacotes): ciclos de dependência entre pacotes | AE: extrair as importações de valor dos arquivos de produção, resolver os nomes do `tsconfig`, agregar o grafo por pacote e contar os pares de pacotes que se alcançam mutuamente. | Madge 8.0.0 (`--json`), grafo em JSON. | A unidade é o par de pacotes em ciclo, não o ciclo de arquivos. A contagem absoluta alimenta a faixa. |
| [M1.1.2](../fase-02/gqm-manutenibilidade.md#m112-importações-que-violam-a-direção-declarada): importações que violam a direção declarada | AE: classificar as arestas do grafo de M1.1.1 e contar as importações de pacotes de base para `excalidraw` e de qualquer pacote para `excalidraw-app`. | Madge 8.0.0, `packages/eslintrc.base.json`, lista de arestas que violam a direção. | O grafo já resolve os destinos das duas restrições. O ESLint sozinho não cobre todas as camadas. |
| [M1.1.3](../fase-02/gqm-manutenibilidade.md#m113-acoplamento-e-instabilidade-de-cada-pacote): acoplamento e instabilidade de cada pacote | AE: obter as dependências distintas de cada pacote e calcular Ca, Ce e `I = Ce / (Ca + Ce)`. | Grafo de M1.1.1, tabela por pacote. | Ca, Ce e I permitem comparar a estrutura dos pacotes. O pacote sem arestas é registrado à parte. |
| [M1.2.1](../fase-02/gqm-manutenibilidade.md#m121-arquivos-de-pacotes-de-base-com-dependência-de-react-ou-do-navegador): arquivos de pacotes de base com dependência de React ou do navegador | AE: marcar com `grep` os arquivos que importam `react` ou `react-dom` ou usam `window.` ou `document.`, sem contar comentários, e propagar a dependência pelo grafo de M1.1.1. | `grep` e Madge 8.0.0, lista de arquivos diretos e transitivos. | A busca textual sozinha não vê o acoplamento transitivo. A contagem e a proporção por pacote alimentam a faixa. |
| [M1.2.2](../fase-02/gqm-manutenibilidade.md#m122-proporção-de-propriedades-públicas-documentadas): proporção de propriedades públicas documentadas | ID: listar as propriedades de `ExcalidrawProps` e procurar, uma a uma, a descrição do propósito na documentação da API. | `packages/excalidraw/types.ts`, `dev-docs/docs/@excalidraw/excalidraw/api/`, lista de verificação. | O numerador exige uma descrição, não só o nome. O resultado é `documentadas / declaradas × 100`. |
| [M1.3.1](../fase-02/gqm-manutenibilidade.md#m131-perfil-de-risco-de-complexidade-das-funções): perfil de risco de complexidade das funções | AE: obter a complexidade e o intervalo de linhas de cada função, descontar as linhas das funções aninhadas e agrupar as linhas pelas faixas 1 a 10, 11 a 20, 21 a 50 e acima de 50. | ESLint 8.57.0 com `@typescript-eslint/parser`, relatório JSON. | A ficha pontua o percentual de linhas por faixa de risco, por pacote e no total, não a média de complexidade. Os inicializadores de campos de classe ficam de fora. |
| [M1.3.2](../fase-02/gqm-manutenibilidade.md#m132-cobertura-da-documentação-para-desenvolvedores): cobertura da documentação para desenvolvedores | ID: verificar os quatro tópicos fixos (contribuição, ambiente, convenções de código e arquitetura) e apontar a seção que comprova cada um. | `README.md`, `CONTRIBUTING.md`, `AGENTS.md`, `dev-docs/docs/`, lista de verificação. | A contagem de 0 a 4 tópicos corresponde diretamente aos níveis. |
| [M1.3.3](../fase-02/gqm-manutenibilidade.md#m133-verificações-estáticas-executadas-automaticamente): verificações estáticas executadas automaticamente | ID: listar todos os fluxos disparados por `pull_request` e seguir os scripts que eles chamam até encontrar lint, formatação e verificação de tipos. | `.github/workflows/`, `package.json`, mapa de fluxo, script e verificação. | Só contam as verificações configuradas para *pull request*. O resultado vai de 0 a 3. |
| [M1.4.1](../fase-02/gqm-manutenibilidade.md#m141-mediana-de-arquivos-de-produção-alterados-por-contribuição): mediana de arquivos de produção alterados por contribuição | MH: listar os *pull requests* integrados na janela, excluir os automáticos previstos na ficha, obter os arquivos de cada um e calcular a mediana dos arquivos de produção. | `gh api`, respostas paginadas. | A mediana controla os valores extremos e entrega arquivos por contribuição, como pede a ficha. |
| [M1.4.2](../fase-02/gqm-manutenibilidade.md#m142-arquivos-de-produção-extensos): arquivos de produção extensos | AE: contar as linhas de código de cada arquivo no commit avaliado, sem linhas vazias nem comentários, e listar os que têm mais de 1.000. | cloc 1.86 (`--by-file`), contagem por arquivo. | O limite é estrito (acima de 1.000). O total e a proporção sobre os arquivos de produção alimentam a faixa. |
| [M1.4.3](../fase-02/gqm-manutenibilidade.md#m143-proporção-de-contribuições-que-alteram-arquivos-extensos): proporção de contribuições que alteram arquivos extensos | AE + MH: cruzar os arquivos extensos de M1.4.2 com os arquivos dos *pull requests* de M1.4.1, levando os nomes antigos de arquivos renomeados para o nome atual. | Saídas de M1.4.1 e M1.4.2, tabela por *pull request*. | Mede a proporção de *pull requests* que tocam ao menos um arquivo extenso, sem contar um *pull request* mais de uma vez. |
| [M1.5.1](../fase-02/gqm-manutenibilidade.md#m151-cobertura-de-linhas-por-pacote): cobertura de linhas por pacote | TA: executar `yarn test:coverage` no ambiente definido e somar as linhas cobertas e executáveis de cada pacote. | Vitest 3.0.6 com `@vitest/coverage-v8` 3.0.7, relatório `json-summary`. | Preserva o denominador de linhas executáveis e o percentual por pacote, sem trocá-lo pela cobertura global. |
| [M1.5.2](../fase-02/gqm-manutenibilidade.md#m152-distribuição-dos-testes-por-nível): distribuição dos testes por nível | AE + ID: classificar as suítes `*.test.ts(x)` dos pacotes e da aplicação em ponta a ponta (controle de navegador real), integração (uso de `render`) ou unitárias (as demais). | `grep` nas importações e chamadas, lista de verificação dos casos ambíguos. | Cada suíte fica em uma única classe. O resultado é a proporção de suítes em cada nível. |
| [M1.5.3](../fase-02/gqm-manutenibilidade.md#m153-proporção-de-contribuições-com-testes-executados-antes-da-integração): proporção de contribuições com testes executados antes da integração | MH: para o último commit de cada *pull request*, buscar as execuções de `test-coverage-pr.yml` e verificar se o passo `Test Coverage` terminou antes de `merged_at` (`<`). | API do GitHub Actions (`runs` e `jobs`), tabela de evidências por *pull request*. | Executado é o passo com conclusão `success` ou `failure` antes da integração. `skipped`, `cancelled` e ausência não contam. Os casos sem evidência ficam fora do denominador e são informados. |

<p className="tabela-fonte">Fonte: [Davi Pierre](https://github.com/DaviPierre), 2026.</p>

### 2.2 G2: Confiabilidade

Os valores são convertidos em nível pelas [faixas de G2](../fase-02/pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2).

<p className="tabela-titulo">Tabela 3: Métodos das métricas de G2</p>

| Métrica | Método e fonte de dados | Ferramenta e evidência | Justificativa |
| :--- | :--- | :--- | :--- |
| [M2.1.1](../fase-02/gqm-confiabilidade.md#m211-proporção-de-correções-entre-as-contribuições-integradas): proporção de correções entre as contribuições integradas | MH: filtrar os *pull requests* integrados na janela e classificar como correção os que têm `fix` no início do título, excluindo as automações previstas na ficha. | `gh api`, listagem paginada e tabela por tipo. | A convenção de título do projeto torna a classificação observável. O resultado é a fração de correções entre os *pull requests* elegíveis, não uma estimativa de defeitos. |
| [M2.1.2](../fase-02/gqm-confiabilidade.md#m212-mediana-do-tempo-entre-o-relato-e-a-correção): mediana do tempo entre o relato e a correção | MH: para as correções integradas na janela com `closingIssuesReferences`, obter a abertura da issue e a data de integração e calcular a mediana das diferenças em dias. | GraphQL do GitHub, pares de issue e *pull request*. | Os vínculos explícitos tornam cada intervalo auditável. A proporção de correções com relato vinculado é informada. |
| [M2.1.3](../fase-02/gqm-confiabilidade.md#m213-proporção-de-contribuições-revisadas-antes-da-integração): proporção de contribuições revisadas antes da integração | MH: obter as revisões `APPROVED` dos *pull requests* elegíveis, comparar o revisor com o autor e verificar se a aprovação veio antes da integração. | GraphQL do GitHub (`reviews`), tabela de *pull request*, revisor e data. | A evidência é a aprovação de outra pessoa. Um *check* automatizado não conta como revisão. |
| [M2.2.1](../fase-02/gqm-confiabilidade.md#m221-proporção-de-funções-essenciais-disponíveis-sem-conexão): proporção de funções essenciais disponíveis sem conexão | TM: depois do primeiro carregamento com rede e do registro do *service worker*, desligar a rede e executar o roteiro das 10 funções essenciais. | Aplicação local, DevTools (modo *offline*), formulário e gravação. | O roteiro fixo reduz o julgamento subjetivo. O resultado é `funções aprovadas / 10 × 100`. |
| [M2.2.2](../fase-02/gqm-confiabilidade.md#m222-origens-externas-necessárias-para-o-editor-local): origens externas necessárias para o editor local | TM + ID: abrir o editor sem colaboração e com o cache limpo, extrair os domínios pelo HAR e bloquear cada origem para testar o desenho. | DevTools (aba *Network* e HAR), lista de domínios, evidências de bloqueio. | Separa os domínios apenas requisitados dos indispensáveis. A contagem alimenta a faixa. |
| [M2.3.1](../fase-02/gqm-confiabilidade.md#m231-proporção-de-arquivos-inválidos-tratados-com-mensagem): proporção de arquivos inválidos tratados com mensagem | TM: abrir os 9 arquivos inválidos pelo menu e por arrastar e soltar, verificar a mensagem e a criação de uma forma sem recarregar. | [Massa de dados](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/tree/main/dados/fase-03/massa-de-dados), aplicação local, formulário e gravação. | Arquivos com defeitos conhecidos e uma condição de aprovação observável permitem calcular os casos tratados sobre 9, nas duas formas de abertura. |
| [M2.3.2](../fase-02/gqm-confiabilidade.md#m232-continuidade-do-editor-após-falha-da-colaboração): continuidade do editor após falha da colaboração | TM: com a sessão ativa em duas janelas, cortar a rede de uma, verificar as 5 condições e repetir 3 vezes. | Aplicação, serviço de colaboração, DevTools (modo *offline*), formulários e gravações. | A condição só é aprovada se passar nas três repetições. O percentual é sobre 5, e as conclusões valem só para o cliente público. |
| [M2.4.1](../fase-02/gqm-confiabilidade.md#m241-proporção-de-cenários-de-fechamento-com-restauração-do-desenho): proporção de cenários de fechamento com restauração do desenho | TM + TA: aplicar os 4 cenários de recarga, fechamento e encerramento forçado e comparar a exportação restaurada com a cena inicial. | Cena de referência, navegador, script comparador, exportações JSON e gravação. | A comparação de elementos e propriedades substitui o julgamento visual. O resultado é `cenários restaurados / 4`. |
| [M2.4.2](../fase-02/gqm-confiabilidade.md#m242-proporção-de-arquivos-reabertos-sem-perda): proporção de arquivos reabertos sem perda | TM + TA: produzir os 7 arquivos das versões definidas e dos exemplos embutidos, abri-los na versão avaliada e comparar os elementos. | Versões v0.15.0, v0.16.4, v0.17.6 e v0.18.0, exemplos em PNG, script comparador. | Identifica perdas de tipo, posição, tamanho e texto. O resultado é o percentual de arquivos sem perda. |
| [M2.4.3](../fase-02/gqm-confiabilidade.md#m243-cobertura-de-desfazer-e-refazer): cobertura de desfazer e refazer | TM + TA: executar as 10 ações definidas, exportar os estados anterior, posterior, após desfazer e após refazer e compará-los. | Aplicação local, `.excalidraw`, script comparador, gravação. | O critério é a igualdade de estado, não a aparência. O resultado é `ações aprovadas / 10 × 100`. |

<p className="tabela-fonte">Fonte: [Davi Pierre](https://github.com/DaviPierre), 2026.</p>

### 2.3 G3: Flexibilidade

Os valores são convertidos em nível pelas [faixas de G3](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3).

<p className="tabela-titulo">Tabela 4: Métodos das métricas de G3</p>

| Métrica | Método e fonte de dados | Ferramenta e evidência | Justificativa |
| :--- | :--- | :--- | :--- |
| [M3.1.1](../fase-02/gqm-flexibilidade.md#m311-cobertura-de-usuários-pelos-navegadores-declarados): cobertura de usuários pelos navegadores declarados | AE: executar a consulta `production` do `browserslist` declarado e obter a cobertura global na mesma base de dados. | Browserslist 4.24.4 e `caniuse-lite`, saída da linha de comando. | A cobertura depende da versão da base de uso, que é registrada. |
| [M3.1.2](../fase-02/gqm-flexibilidade.md#m312-proporção-de-ambientes-de-integração-com-sucesso): proporção de ambientes de integração com sucesso | EA + TM: preparar as 6 combinações de React 17, 18 e 19 com Vite e Next.js, compilar, abrir e criar uma forma. | Projetos mínimos versionados, npm e Yarn, registros de compilação e gravação. | O sucesso exige a compilação e o editor funcionando. O resultado é `combinações aprovadas / 6`. |
| [M3.1.3](../fase-02/gqm-flexibilidade.md#m313-proporção-de-ações-de-edição-que-funcionam-por-toque-e-caneta): proporção de ações de edição que funcionam por toque e caneta | TM: realizar as 10 ações no aparelho de toque e, separadamente, com caneta, preenchendo o formulário por ação. | iPad, caneta e navegador definidos nos [recursos](./recursos-ambiente.md#4-dispositivo-com-toque-e-caneta-m313), gravação de tela. | As duas formas de entrada são registradas separadamente. O resultado é o percentual de cada uma. |
| [M3.2.1](../fase-02/gqm-flexibilidade.md#m321-tempo-de-abertura-por-tamanho-de-cena): tempo de abertura por tamanho de cena | MD: abrir 5 vezes cada cena de 100, 1.000, 5.000 e 10.000 elementos e medir do arrastar do arquivo ao último quadro. | DevTools (aba *Performance*), cenas geradas, registros de tempo. | A mediana de cinco tempos por cena reduz o ruído. A comparação usa sempre a mesma máquina. |
| [M3.2.2](../fase-02/gqm-flexibilidade.md#m322-taxa-de-quadros-durante-a-edição-por-tamanho-de-cena): taxa de quadros durante a edição por tamanho de cena | MD: para cada cena, fazer 5 sessões de 10 s arrastando um grupo de 50 elementos e deslocando a tela com roteiro fixo. | DevTools (aba *Performance*), gravações, planilha de quadros por segundo. | A mediana por cena evita tomar uma única amostra como desempenho geral. O hardware e o monitor são controlados. |
| [M3.2.3](../fase-02/gqm-flexibilidade.md#m323-tamanho-máximo-de-cena-salva-e-exportada): tamanho máximo de cena salva e exportada | TM + MD: testar cenas crescentes, salvar `.excalidraw` e exportar PNG e SVG, marcando falha acima de 30 s ou em travamento. | Cenas de escala, cronômetro do navegador, arquivos exportados, gravação. | O valor é a maior cena aprovada nas três operações, em elementos. |
| [M3.3.1](../fase-02/gqm-flexibilidade.md#m331-proporção-de-operações-de-pacote-bem-sucedidas): proporção de operações de pacote bem-sucedidas | EA: instalar, atualizar da versão 0.17.6 para a avaliada e remover o pacote com npm, Yarn e pnpm, verificando a compilação a cada operação. | Ambiente limpo, gerenciadores de pacotes, registros completos das 9 operações. | O resultado é `operações bem-sucedidas / 9 × 100`. O ambiente limpo evita a interferência de dependências já instaladas. |
| [M3.3.2](../fase-02/gqm-flexibilidade.md#m332-proporção-de-passos-documentados-reproduzidos-sem-ajuste): proporção de passos documentados reproduzidos sem ajuste | EA + ID: listar os comandos das instruções de desenvolvimento com Node.js, Yarn e Docker Compose e executá-los literalmente em ambiente limpo. | Guia de desenvolvimento, ambiente limpo, lista de verificação, registros. | Cada ajuste não documentado é uma falha do passo. O percentual mede se as instruções bastam para operar o projeto. |
| [M3.3.3](../fase-02/gqm-flexibilidade.md#m333-implantação-com-docker): implantação com Docker | EA + TM: construir a imagem, iniciar o contêiner, validar o *healthcheck* e abrir o editor para desenhar. | `Dockerfile`, `docker-compose.yml`, Docker, registros e captura. | Os 4 critérios verificam construção, execução, saúde e uso, não só a construção da imagem. O percentual é sobre 4. |
| [M3.4.1](../fase-02/gqm-flexibilidade.md#m341-formatos-de-exportação-abertos-disponíveis): formatos de exportação abertos disponíveis | ID + TM: listar as opções de salvar e exportar e verificar se há especificação pública de cada formato. | Interface do editor, `packages/excalidraw/scene/export.ts`, capturas. | Conta só os formatos abertos, separando-os dos serviços proprietários. |
| [M3.4.2](../fase-02/gqm-flexibilidade.md#m342-proporção-de-elementos-preservados-na-exportação-e-reimportação): proporção de elementos preservados na exportação e reimportação | TM + TA: exportar a cena de referência em `.excalidraw`, PNG e SVG com a cena incorporada, reimportar e comparar os elementos. | Massa de dados, script comparador, exportações originais e reimportadas. | Mede o percentual de elementos preservados por formato, com igualdade de tipo, posição, tamanho, estilo e texto. |
| [M3.4.3](../fase-02/gqm-flexibilidade.md#m343-proporção-dos-campos-do-formato-excalidraw-documentados): proporção dos campos do formato `.excalidraw` documentados | AE + ID: listar os campos distintos do JSON da cena de referência, incluindo a raiz e os tipos de elemento, e procurar a descrição de cada um na documentação do esquema. | Leitor de JSON, `dev-docs/docs/codebase/json-schema.mdx`, lista de verificação. | O resultado é `campos documentados / campos encontrados × 100`. A falta de um esquema formal é anotada à parte. |

<p className="tabela-fonte">Fonte: [Davi Pierre](https://github.com/DaviPierre), 2026.</p>

---

## 3. Repetibilidade e julgamento humano

### 3.1 Medições automáticas

Toda medição automática registra o commit completo do Excalidraw, o commit do repositório da avaliação, as versões das ferramentas e a janela histórica, como pede a [seção 9 dos recursos](./recursos-ambiente.md#9-fatores-de-variação-registrados-em-cada-coleta). O comando, os parâmetros e a saída bruta são guardados, e não só o valor final. Nas consultas à API, as respostas são paginadas e a data da consulta é registrada.

Quando uma métrica não puder ser calculada, a coleta registra o motivo e o denominador afetado e segue a regra de [métricas não coletadas](../fase-02/pontuacao-julgamento.md#61-métricas-não-coletadas). A falta de dados nunca vira zero.

### 3.2 Métricas que dependem de julgamento humano

Os métodos ID, TM e EA usam condições de aprovação escritas antes do teste, para que o avaliador não decida na hora o que é sucesso. É o caso de M1.2.2 (a propriedade tem descrição do propósito?), M1.3.2 (o tópico tem documento ou seção dedicada?), M1.5.2 (a suíte usa de fato um navegador real ou `render`?), de M2.2.1 a M2.4.3 (o cenário passou conforme o roteiro?) e de M3.1.2 a M3.4.2 (compilação, operação, desempenho e preservação dos elementos).

Em cada caso manual, o avaliador usa a mesma massa de dados, segue os passos na ordem, marca passou ou falhou pela condição escrita e guarda a gravação integral da tela nos testes no navegador. A coleta manual identifica quem registrou o dado [[2, p. 51]](#ref-2). Uma captura isolada complementa a gravação, mas não a substitui.

A verificação da [#114](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/114) é o segundo olhar, feito por quem não coletou, sobre o caminho do dado bruto ao cálculo e à pontuação. Quando houver discordância, ficam registradas as duas leituras, a evidência e a decisão, sem apagar o registro original.

### 3.3 Condições dos testes instrumentados

M3.2.1 e M3.2.2 são executadas só na máquina de Maria Eduarda, descrita nos [recursos](./recursos-ambiente.md#3-máquinas-dos-responsáveis-pela-coleta), com navegador, tela, modo de energia, armazenamento local e número de repetições controlados. M2.3.1, M2.4.1, M2.4.2 e M3.4.2 usam as entradas da [massa de dados](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/tree/main/dados/fase-03/massa-de-dados) e guardam os arquivos de entrada e de saída para a comparação automatizada. M2.2.1 e M2.3.2 separam o que depende da rede do que é comportamento local e registram as falhas de serviços externos, sem concluir nada sobre os servidores de produção. M3.1.2, M3.3.1 e M3.3.2 usam ambientes limpos e guardam as saídas de compilação e instalação, para mostrar os pré-requisitos não documentados.

---

## 4. Ligação com as outras páginas

A cadeia completa vai da ficha da métrica na Fase 02 ao método desta página, aos [recursos e ambiente](./recursos-ambiente.md), às instruções para o avaliador, aos dados brutos da Fase 04, ao [plano de análise](./plano-analise.md) e, por fim, às faixas e ao julgamento da Fase 02, com a verificação da #114 no meio do caminho. A conversão dos valores em níveis de 1 a 5, as médias por questão e por característica, o arredondamento e a regra para métricas ausentes estão nos [níveis de pontuação](../fase-02/pontuacao-julgamento.md).

---

## Referências

> <Link id="ref-1">1.</Link> RAMOS, Cristiane Soares. **AULA A07 QSW1 PROC AVAL PRODUTO**. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Página 18. Disponível no Moodle da disciplina.

> <Link id="ref-2">2.</Link> RAMOS, Cristiane Soares. **AULA 08 QSW1 GQM**. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Páginas 45 e 51. Disponível no Moodle da disciplina.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 08/11/2026 | Proposta inicial de métodos, ferramentas, evidências e justificativas para as 36 métricas dos objetivos G1, G2 e G3 | [Davi Pierre](https://github.com/DaviPierre) |  |
| 1.1 | 10/11/2026 | Ajustes da revisão da PR #149: abertura com Introdução e Metodologia, links no lugar de repetições, M1.5.3 com `<` e formato das citações e das tabelas | [Christopher Paraizo](https://github.com/wChrstphr) |  |
