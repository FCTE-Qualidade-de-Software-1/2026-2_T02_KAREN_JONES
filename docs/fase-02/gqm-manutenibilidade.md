---
sidebar_position: 3
title: GQM de Manutenibilidade (G1)
description: Questões, hipóteses e métricas do objetivo de medição G1, que avalia a manutenibilidade do código-fonte do Excalidraw
---

# GQM de Manutenibilidade (G1)

Esta página detalha o objetivo G1, definido em [Método GQM e objetivos de medição](./estrutura-gqm.md#g1--manutenibilidade). Para cada subcaracterística de Manutenibilidade há uma questão, a hipótese da questão e as métricas que a respondem.

| Campo do template | Valor |
| :--- | :--- |
| Analisar | o código-fonte do Excalidraw (biblioteca, aplicação web e pacotes auxiliares), seus testes, sua documentação para desenvolvedores e o histórico público de alterações |
| para o propósito de | entender |
| com respeito a | Manutenibilidade: modularidade, reusabilidade, analisabilidade, modificabilidade e testabilidade |
| do ponto de vista de | mantenedores e contribuidores do projeto |
| no contexto de | código-fonte público na versão de 18/10/2026, avaliado por equipe independente |

As questões caracterizam o código em relação a cada subcaracterística (AULA 08, p. 33 e 34). As hipóteses partem da [abstraction sheet de G1](./abstraction-sheets.md#3-g1--manutenibilidade), como a aula permite (AULA 08, p. 34). As métricas respondem às questões de forma quantitativa (AULA 08, p. 38). Os níveis de pontuação e os critérios de julgamento de cada métrica são definidos em uma página própria da Fase 02.

---

## 1. Visão geral

| Questão | Subcaracterística | Requisitos da Fase 01 | Métricas |
| :--- | :--- | :--- | :--- |
| Q1.1 | Modularidade | RQ-MAN-01 a RQ-MAN-03 | M1.1.1, M1.1.2, M1.1.3 |
| Q1.2 | Reusabilidade | RQ-MAN-04 e RQ-MAN-05 | M1.2.1, M1.2.2 |
| Q1.3 | Analisabilidade | RQ-MAN-06 a RQ-MAN-08 | M1.3.1, M1.3.2, M1.3.3 |
| Q1.4 | Modificabilidade | RQ-MAN-09 e RQ-MAN-10 | M1.4.1, M1.4.2, M1.4.3 |
| Q1.5 | Testabilidade | RQ-MAN-11 a RQ-MAN-13 | M1.5.1, M1.5.2, M1.5.3 |

Os requisitos estão em [Requisitos da avaliação](../fase-01/requisitos-avaliacao.md). A seção 8 mostra qual métrica atende cada requisito.

---

## 2. Convenções de coleta

As definições abaixo valem para todas as métricas de G1 e evitam que pessoas diferentes contem coisas diferentes.

- **Versão avaliada:** commit `e1b7aac` do repositório oficial, de 18/10/2026, identificado no [escopo](../fase-01/escopo-avaliacao.md).
- **Pacote:** cada pasta em `packages/` (`common`, `element`, `excalidraw`, `fractional-indexing`, `laser-pointer`, `math` e `utils`) e a aplicação web em `excalidraw-app/`.
- **Pacotes de base:** todos os pacotes, exceto a biblioteca `excalidraw` e a aplicação web.
- **Código de produção:** arquivos `.ts` e `.tsx` dos pacotes. Ficam de fora as pastas `tests/` e `__snapshots__/`, os arquivos `*.test.ts(x)` e `*.d.ts`, a documentação (`dev-docs/`), os exemplos (`examples/`) e as dependências instaladas (`node_modules/`).
- **Código de teste:** arquivos de suíte `*.test.ts(x)`, os que o Vitest reconhece como testes pelo seu padrão de nomes (o projeto não define outro em `vitest.config.mts`). Os demais arquivos das pastas `tests/` (utilitários, dados de exemplo e *snapshots*) dão apoio às suítes e não são contados como arquivos de teste nem como código de produção.
- **Janela histórica:** contribuições integradas ao ramo principal entre 18/04/2026 e 18/10/2026, os seis meses que antecedem a versão avaliada. A janela delimita os dados de histórico do projeto (objeto O6 do escopo).
- **Contribuição integrada:** *pull request* aceito (*merged*) no ramo principal do repositório.

Os fatores que podem influenciar os resultados também são registrados junto com cada coleta (AULA 08, p. 38): o commit avaliado, a janela histórica e a versão de cada ferramenta. Esses fatores foram levantados na abstraction sheet de G1.

---

## 3. Q1.1 — Modularidade

**Questão:** Em que medida o código está dividido em pacotes independentes, com dependências em uma única direção?

**Requisitos:** RQ-MAN-01 (limites entre aplicação e biblioteca), RQ-MAN-02 (direção das dependências e ausência de ciclos) e RQ-MAN-03 (coesão e dependências desnecessárias).

**Hipótese:** não há ciclos de dependência em tempo de execução entre os pacotes, e nenhum pacote importa código da aplicação web. A biblioteca `excalidraw` é o pacote que mais recebe dependências dos demais.

### M1.1.1 — Ciclos de dependência entre pacotes

| Campo | Descrição |
| :--- | :--- |
| Definição | Número de pares de pacotes que dependem um do outro em tempo de execução, direta ou indiretamente. |
| Procedimento de cálculo | Montar o grafo de dependências entre arquivos de produção, considerando só importações de valor (importações apenas de tipo são descartadas, porque desaparecem na compilação). Agrupar os arquivos por pacote e contar os pares de pacotes A e B em que A alcança B e B alcança A. Unidade: pares de pacotes. Escala: absoluta, de 0 em diante. |
| Fonte dos dados | Código de produção de todos os pacotes. |
| Procedimento de coleta | Ferramenta Madge (versão 8.0.0), com o `tsconfig.json` do repositório para resolver os nomes `@excalidraw/*` e com a opção de ignorar importações de tipo, exportando o grafo completo entre arquivos (opção `--json`). Um script agrega as arestas por pacote, descarta as internas a um mesmo pacote e verifica, para cada par, se um pacote alcança o outro. A lista de ciclos entre arquivos (opção `--circular`) não basta: `A/a1 → B/b1` e `B/b2 → A/a2` não formam ciclo entre arquivos, mas formam ciclo entre os pacotes A e B. |
| Critério de interpretação | Confirma a hipótese se o valor for 0. Cada par encontrado indica dois pacotes que não podem ser alterados ou reutilizados separadamente. |
| Questão respondida | Q1.1 |
| Características desejáveis | Simples (contagem). Objetiva, porque o grafo sai das importações declaradas no código. Fácil de coletar com uma ferramenta automática. Válida, porque ciclos medem diretamente a falta de direção nas dependências. Baseada na estrutura do programa, e não na linguagem. |

### M1.1.2 — Importações que violam a direção declarada

| Campo | Descrição |
| :--- | :--- |
| Definição | Número de importações de valor que contrariam a direção de dependência declarada pelo próprio projeto: pacotes de base importando da biblioteca `excalidraw`, ou qualquer pacote importando da aplicação web. |
| Procedimento de cálculo | Resolver o destino de cada importação de valor dos arquivos de produção, inclusive caminhos relativos, nomes `@excalidraw/*` e reexportações (`export ... from`), para o pacote do arquivo importado. Contar as importações que se enquadram em uma das duas condições: (1) origem em um pacote de base e destino na biblioteca; (2) destino na aplicação web, a partir de qualquer pacote. A condição 1 é a regra de lint `packages/eslintrc.base.json` do Excalidraw, que proíbe os pacotes de base de importar da biblioteca qualquer coisa além de tipos. A condição 2 vem da organização do repositório, em que a aplicação web é a camada mais externa e consome a biblioteca. Unidade: importações (pares arquivo de origem → arquivo de destino). Escala: absoluta. |
| Fonte dos dados | Código de produção de todos os pacotes; arquivo `packages/eslintrc.base.json`. |
| Procedimento de coleta | O grafo de importações de valor de M1.1.1, em que o Madge já resolve os destinos para arquivos. Um script classifica cada aresta pelas duas condições e conta as que as violam. O ESLint do projeto não serve sozinho como coleta, porque a regra não trata de importações da aplicação web e só é aplicada nos pacotes cuja configuração a estende (`common` e `element`). |
| Critério de interpretação | Confirma a hipótese se o valor for 0. Cada importação encontrada é um ponto em que o código não respeita a arquitetura que o próprio projeto declara. |
| Questão respondida | Q1.1 |
| Características desejáveis | Simples e objetiva, porque a direção esperada vem de uma regra escrita pelo projeto, e não de opinião da equipe. Fácil de coletar. Válida para os limites entre aplicação, biblioteca e pacotes de base (RQ-MAN-01). |

### M1.1.3 — Acoplamento e instabilidade de cada pacote

| Campo | Descrição |
| :--- | :--- |
| Definição | Acoplamento aferente (Ca), acoplamento eferente (Ce) e instabilidade *I* de cada pacote (Martin, 2002). Ca é o número de outros pacotes que importam o pacote; Ce é o número de outros pacotes que ele importa. *I* é a proporção das dependências do pacote que apontam para fora dele: um pacote estável (I perto de 0) é usado por muitos e usa poucos; um instável (I perto de 1) usa muitos e é usado por poucos. |
| Procedimento de cálculo | Ca e Ce por contagem de pacotes distintos; *I* = Ce / (Ca + Ce). Consideram-se só importações de valor no código de produção. Unidade: pacotes (Ca e Ce) e adimensional (*I*). Escala: absoluta (Ca e Ce) e 0 a 1 (*I*). |
| Fonte dos dados | Código de produção de todos os pacotes. |
| Procedimento de coleta | O mesmo grafo de M1.1.1, agregado por pacote, contando as arestas distintas entre pacotes. |
| Critério de interpretação | Confirma a hipótese se a biblioteca tiver o maior Ca entre os pacotes. *I* é registrado para comparar os pacotes entre si: um pacote de base com *I* alto depende de muitos outros e é mais difícil de reutilizar. |
| Questão respondida | Q1.1 |
| Características desejáveis | Simples (uma razão). Objetiva e robusta, porque permite comparar pacotes entre si e com outras versões. Válida, porque é uma medida consagrada de acoplamento entre módulos. Independente da linguagem. |

---

## 4. Q1.2 — Reusabilidade

**Questão:** Os pacotes podem ser usados fora do editor, e a interface pública da biblioteca está documentada para quem vai reutilizá-la?

**Requisitos:** RQ-MAN-04 (reutilização dos componentes e dos pacotes menores) e RQ-MAN-05 (interface pública documentada).

**Hipótese:** os pacotes `math` e `utils` não dependem de React nem de recursos do navegador. A maior parte das propriedades públicas da biblioteca está documentada, mas parte delas só aparece nos tipos do código.

### M1.2.1 — Arquivos de pacotes de base com dependência de React ou do navegador

| Campo | Descrição |
| :--- | :--- |
| Definição | Número de arquivos de produção de cada pacote de base que dependem de React ou do navegador, diretamente ou por meio de outros arquivos. A dependência é direta quando o arquivo importa `react` ou `react-dom`, ou usa os objetos globais do navegador `window` e `document`. É transitiva quando o arquivo importa um valor (inclusive por reexportação) de outro arquivo que depende de React ou do navegador, em qualquer pacote. |
| Procedimento de cálculo | Contagem por pacote, separando os arquivos com dependência direta dos que só têm dependência transitiva. Unidade: arquivos. Escala: absoluta. Também é registrada a proporção em relação ao total de arquivos de produção do pacote. |
| Fonte dos dados | Código de produção de todos os pacotes. |
| Procedimento de coleta | Busca no código de produção de todos os pacotes por importações de `react` e `react-dom` e por usos de `window.` e `document.` (ferramenta `grep`), excluindo comentários. Os arquivos encontrados são marcados no grafo de importações de valor de M1.1.1, e um script conta os arquivos dos pacotes de base que alcançam algum arquivo marcado. |
| Critério de interpretação | Confirma a hipótese se o valor for 0 em `math` e `utils`. Nos demais pacotes de base, valores maiores indicam que o pacote só funciona dentro de um navegador ou junto com React. |
| Questão respondida | Q1.2 |
| Características desejáveis | Simples e fácil de coletar. Objetiva, porque depende só do texto do código. Válida como indicador de reutilização fora do editor, já que essas dependências impedem o uso em outros ambientes, como servidores. |

### M1.2.2 — Proporção de propriedades públicas documentadas

| Campo | Descrição |
| :--- | :--- |
| Definição | Percentual das propriedades do componente principal da biblioteca (`ExcalidrawProps`) que estão descritas na documentação oficial para desenvolvedores. |
| Procedimento de cálculo | (propriedades descritas na documentação ÷ propriedades declaradas em `ExcalidrawProps`) × 100. Unidade: percentual. Escala: 0 a 100. |
| Fonte dos dados | Tipo `ExcalidrawProps` em `packages/excalidraw/types.ts`; páginas da pasta `dev-docs/docs/@excalidraw/excalidraw/api/`. |
| Procedimento de coleta | Listar os nomes das propriedades declaradas no tipo e procurar cada nome nas páginas da documentação. Uma propriedade conta como documentada se tiver ao menos uma descrição do seu propósito. |
| Critério de interpretação | Confirma a hipótese se o valor for alto, mas menor que 100%. Quanto menor o valor, mais quem integra a biblioteca precisa ler o código para usá-la. |
| Questão respondida | Q1.2 |
| Características desejáveis | Simples (uma razão). Objetiva, porque a lista de propriedades vem do código. Fácil de coletar, com uma lista finita. Válida para a separação entre interface pública e detalhes internos (RQ-MAN-05). |

---

## 5. Q1.3 — Analisabilidade

**Questão:** O código pode ser entendido com facilidade, com apoio de documentação e de verificações automáticas?

**Requisitos:** RQ-MAN-06 (compreensão do código), RQ-MAN-07 (documentação de convenções, arquitetura e contribuição) e RQ-MAN-08 (lint, formatação e verificação de tipos).

**Hipótese:** a maior parte das funções tem complexidade baixa, e as de complexidade alta se concentram em poucos arquivos, principalmente no componente principal do editor. A documentação para desenvolvedores cobre a contribuição e a preparação do ambiente. Lint, formatação e verificação de tipos são executados automaticamente.

### M1.3.1 — Perfil de risco de complexidade das funções

| Campo | Descrição |
| :--- | :--- |
| Definição | Distribuição das linhas de código de produção pelas quatro faixas de risco de complexidade ciclomática das funções em que estão: risco baixo (complexidade de 1 a 10), moderado (11 a 20), alto (21 a 50) e muito alto (acima de 50). A complexidade ciclomática conta os caminhos independentes de execução de uma função (McCabe, 1976). As faixas são as do Software Engineering Institute, adotadas no modelo de manutenibilidade de Heitlager, Kuipers e Visser (2007, p. 6). |
| Procedimento de cálculo | Para cada função, obter a complexidade ciclomática e as linhas de código próprias: as linhas da função que não estão em branco nem são comentários, descontadas as linhas das funções declaradas dentro dela, para que cada linha seja contada uma única vez. Classificar cada função em uma faixa e calcular, para cada faixa, (linhas próprias das funções da faixa ÷ linhas próprias de todas as funções) × 100, por pacote e no total. Também são registrados o percentual de funções em cada faixa e a lista dos arquivos com mais linhas nas faixas de risco alto e muito alto. Unidade: percentual de linhas de código. Escala: 0 a 100 em cada faixa, e as quatro faixas somam 100. |
| Fonte dos dados | Código de produção de todos os pacotes. |
| Procedimento de coleta | ESLint (versão 8.57.0) com o analisador `@typescript-eslint/parser` e a regra `complexity` ativada com limite 0, que informa a complexidade de cada função e as linhas em que ela começa e termina. Um script conta as linhas próprias de cada função a partir desses intervalos. Os inicializadores de campos de classe, que a regra também informa, não são funções e ficam de fora. |
| Critério de interpretação | Confirma a hipótese se a maior parte das funções e das linhas estiver na faixa de risco baixo e se as linhas das faixas de risco alto e muito alto estiverem concentradas em poucos arquivos. O resultado é dado em linhas, e não em média de complexidade, porque a média esconde as poucas funções muito complexas (Heitlager; Kuipers; Visser, 2007, p. 6). Funções muito complexas são mais difíceis de entender e de testar. |
| Questão respondida | Q1.3 |
| Características desejáveis | Objetiva e consistente, porque o cálculo é definido pela regra da ferramenta e as faixas vêm de fonte publicada. Fácil de coletar automaticamente. Robusta, porque permite comparar pacotes. Baseada na estrutura de controle do programa, e não na sintaxe da linguagem. |

### M1.3.2 — Cobertura da documentação para desenvolvedores

| Campo | Descrição |
| :--- | :--- |
| Definição | Número de tópicos de documentação para desenvolvedores presentes, de uma lista de quatro: (1) guia de contribuição; (2) preparação do ambiente de desenvolvimento; (3) convenções de código; (4) descrição da arquitetura ou da organização do código. |
| Procedimento de cálculo | Soma dos tópicos presentes. Um tópico está presente se houver um documento ou uma seção dedicada a ele. Unidade: tópicos. Escala: 0 a 4. |
| Fonte dos dados | `README.md`, `CONTRIBUTING.md` e `AGENTS.md` da raiz; páginas de `dev-docs/docs/` (documentação publicada em docs.excalidraw.com). |
| Procedimento de coleta | Inspeção dos arquivos, preenchendo uma lista de verificação com o caminho do documento que comprova cada tópico. |
| Critério de interpretação | Confirma a hipótese se pelo menos os tópicos 1 e 2 estiverem presentes. Cada tópico ausente obriga quem chega ao projeto a descobrir a informação pelo código. |
| Questão respondida | Q1.3 |
| Características desejáveis | Simples. Objetiva, porque a lista é fixa e cada item exige um documento como evidência. Fácil de coletar. Válida para RQ-MAN-07. |

### M1.3.3 — Verificações estáticas executadas automaticamente

| Campo | Descrição |
| :--- | :--- |
| Definição | Número de verificações estáticas executadas automaticamente em toda alteração proposta, de uma lista de três: lint, formatação e verificação de tipos. |
| Procedimento de cálculo | Soma das verificações que aparecem em um fluxo de integração contínua disparado por *pull request*. Unidade: verificações. Escala: 0 a 3. |
| Fonte dos dados | Arquivos de fluxo em `.github/workflows/` e scripts do `package.json` da raiz. |
| Procedimento de coleta | Inspeção dos fluxos disparados por `pull_request` e dos scripts que eles chamam (por exemplo, `test:code`, `test:other` e `test:typecheck`). |
| Critério de interpretação | Confirma a hipótese se o valor for 3. Uma verificação que não roda automaticamente depende da disciplina de cada contribuidor. |
| Questão respondida | Q1.3 |
| Características desejáveis | Simples e objetiva, com evidência nos arquivos de configuração. Fácil de coletar. Válida para RQ-MAN-08. |

---

## 6. Q1.4 — Modificabilidade

**Questão:** As alterações no código ficam restritas a poucas partes, ou tendem a se espalhar e a passar por arquivos que concentram responsabilidades demais?

**Requisitos:** RQ-MAN-09 (alcance das alterações) e RQ-MAN-10 (arquivos ou funções que concentram responsabilidades).

**Hipótese:** a maioria das contribuições altera poucos arquivos. Há poucos arquivos muito extensos, mas eles são alterados por uma parte relevante das contribuições, o que torna essas alterações mais arriscadas.

### M1.4.1 — Mediana de arquivos de produção alterados por contribuição

| Campo | Descrição |
| :--- | :--- |
| Definição | Mediana do número de arquivos de produção alterados por contribuição integrada na janela histórica. |
| Procedimento de cálculo | Para cada contribuição integrada na janela, contar os arquivos de produção alterados (adicionados, modificados ou removidos). Calcular a mediana dessas contagens. A mediana é usada no lugar da média para que poucas contribuições muito grandes não distorçam o resultado. Unidade: arquivos. Escala: absoluta. |
| Fonte dos dados | Histórico de *pull requests* do repositório oficial no GitHub. |
| Procedimento de coleta | API do GitHub (`gh api`), listando as contribuições integradas na janela e os arquivos de cada uma (`pulls/{número}/files`). Contribuições automáticas de atualização de dependências e de traduções são excluídas e contadas à parte. |
| Critério de interpretação | Confirma a hipótese se a mediana for baixa. Medianas altas indicam que mudanças comuns exigem mexer em muitos lugares. |
| Questão respondida | Q1.4 |
| Características desejáveis | Simples. Objetiva, porque os dados vêm do registro do repositório. Robusta a valores extremos, por usar a mediana. Fácil de coletar automaticamente. Válida para RQ-MAN-09. |

### M1.4.2 — Arquivos de produção extensos

| Campo | Descrição |
| :--- | :--- |
| Definição | Número de arquivos de produção com mais de 1.000 linhas de código, sem contar linhas em branco e comentários. |
| Procedimento de cálculo | Contagem por pacote e no total, com a lista dos arquivos encontrados. O limite de 1.000 linhas é uma convenção da equipe para identificar arquivos que reúnem muitas responsabilidades; a justificativa das faixas fica nos níveis de pontuação. Unidade: arquivos. Escala: absoluta. |
| Fonte dos dados | Código de produção de todos os pacotes. |
| Procedimento de coleta | Contagem de linhas por arquivo com a ferramenta cloc (versão 1.86, opção `--by-file`), aplicando as convenções da seção 2. |
| Critério de interpretação | Confirma a hipótese se houver poucos arquivos acima do limite. Cada arquivo encontrado é candidato a concentrar responsabilidades demais (RQ-MAN-10). |
| Questão respondida | Q1.4 |
| Características desejáveis | Simples e fácil de coletar. Objetiva, porque o limite é fixo e a ferramenta define o que é linha de código. Robusta, porque permite comparar pacotes e versões. |

### M1.4.3 — Proporção de contribuições que alteram arquivos extensos

| Campo | Descrição |
| :--- | :--- |
| Definição | Percentual das contribuições integradas na janela histórica que alteram pelo menos um dos arquivos identificados em M1.4.2. |
| Procedimento de cálculo | (contribuições que alteram ao menos um arquivo extenso ÷ contribuições integradas na janela) × 100. Unidade: percentual. Escala: 0 a 100. |
| Fonte dos dados | Histórico de *pull requests* (mesmos dados de M1.4.1) e lista de arquivos de M1.4.2. |
| Procedimento de coleta | Cruzamento, por script, da lista de arquivos de cada contribuição com a lista de arquivos extensos. Arquivos renomeados na janela são acompanhados pelo nome atual. |
| Critério de interpretação | Confirma a hipótese se o percentual for relevante, isto é, se os arquivos extensos forem alterados com frequência. Quanto maior o valor, mais o trabalho de manutenção passa pelos arquivos mais difíceis de alterar. |
| Questão respondida | Q1.4 |
| Características desejáveis | Simples (uma razão). Objetiva. Fácil de coletar a partir dos dados de M1.4.1 e M1.4.2. Válida, porque liga o tamanho dos arquivos ao esforço real de manutenção. |

---

## 7. Q1.5 — Testabilidade

**Questão:** O código pode ser verificado por testes automatizados, em diferentes níveis, executados a cada alteração?

**Requisitos:** RQ-MAN-11 (condições para testes automatizados), RQ-MAN-12 (níveis de teste) e RQ-MAN-13 (execução automática).

**Hipótese:** a biblioteca tem cobertura de testes maior do que a aplicação web. Predominam testes unitários e de integração. Os testes rodam em toda contribuição antes da integração.

### M1.5.1 — Cobertura de linhas por pacote

| Campo | Descrição |
| :--- | :--- |
| Definição | Percentual das linhas do código de produção de cada pacote executadas pelo conjunto de testes automatizados do projeto. |
| Procedimento de cálculo | (linhas executadas pelos testes ÷ linhas executáveis) × 100, por pacote e no total. Unidade: percentual. Escala: 0 a 100. |
| Fonte dos dados | Código de produção e de teste de todos os pacotes; configuração de cobertura em `vitest.config.mts`. |
| Procedimento de coleta | Execução do comando do próprio projeto `yarn test:coverage` (Vitest), no ambiente definido no plano de avaliação, lendo o relatório `json-summary` gerado. |
| Critério de interpretação | Confirma a hipótese se a cobertura da biblioteca for maior que a da aplicação web. Pacotes com cobertura baixa têm mais código que pode ser alterado sem nenhum teste perceber a mudança. Os limites mínimos já configurados pelo projeto em `vitest.config.mts` servem de referência. |
| Questão respondida | Q1.5 |
| Características desejáveis | Objetiva e consistente, porque usa a configuração do próprio projeto. Robusta, porque permite comparar pacotes. Fácil de coletar com um comando. Válida para RQ-MAN-11, com a limitação de que cobertura mede código executado, e não a qualidade das verificações. |

### M1.5.2 — Distribuição dos testes por nível

| Campo | Descrição |
| :--- | :--- |
| Definição | Percentual dos arquivos de teste em cada nível: unitário, integração e ponta a ponta. |
| Procedimento de cálculo | Classificar cada arquivo de teste por um critério fixo: **integração**, se renderiza componentes do editor (usa a função `render` dos utilitários de teste); **ponta a ponta**, se usa uma ferramenta que controla um navegador real (como Playwright, Cypress ou Puppeteer); **unitário**, nos demais casos. Calcular (arquivos do nível ÷ total de arquivos de teste) × 100. Unidade: percentual. Escala: 0 a 100 para cada nível. |
| Fonte dos dados | Código de teste de todos os pacotes; `package.json` da raiz e dos pacotes, para identificar ferramentas de teste de ponta a ponta. |
| Procedimento de coleta | Busca no código de teste (ferramenta `grep`) pelas chamadas e importações que definem cada nível. |
| Critério de interpretação | Confirma a hipótese se os testes unitários e de integração somarem a maior parte dos arquivos de teste. Um nível ausente indica um tipo de falha que os testes automatizados não alcançam. |
| Questão respondida | Q1.5 |
| Características desejáveis | Objetiva, porque o critério de classificação é mecânico e não depende de julgamento. Fácil de coletar. Válida para RQ-MAN-12. |

### M1.5.3 — Proporção de contribuições com testes executados antes da integração

| Campo | Descrição |
| :--- | :--- |
| Definição | Percentual das contribuições integradas na janela histórica em que a etapa de testes automatizados foi efetivamente executada e terminou antes da integração. |
| Procedimento de cálculo | Uma contribuição conta como verificada se, em alguma execução do fluxo `test-coverage-pr.yml` sobre o último commit da contribuição, o passo `Test Coverage` tiver sido executado (conclusão `success` ou `failure`, e não `skipped`, `cancelled` ou ausente) e tiver terminado antes do horário de integração (`merged_at`). Contribuições sem registros suficientes para essa decisão (execução não encontrada ou passos indisponíveis) são contadas à parte e ficam fora do denominador. Cálculo: (contribuições verificadas ÷ contribuições integradas na janela com evidência suficiente) × 100. O número de contribuições sem evidência é informado junto com o percentual. Unidade: percentual. Escala: 0 a 100. |
| Fonte dos dados | Execuções do fluxo `test-coverage-pr.yml` de cada contribuição no GitHub, com os passos de cada job; horário de integração de cada contribuição. |
| Procedimento de coleta | API do GitHub (`gh api`): para cada contribuição, as execuções do fluxo sobre o último commit (`actions/workflows/test-coverage-pr.yml/runs?head_sha=...`), os passos de cada job, com conclusão e horário de término (`actions/runs/{id}/jobs`), e o campo `merged_at` da contribuição (`pulls/{número}`). Um script aplica a regra do procedimento de cálculo. A existência de um *check* no commit não basta, porque a execução pode terminar depois da integração ou falhar na instalação das dependências, antes do passo de testes. |
| Critério de interpretação | Confirma a hipótese se o valor for 100% ou próximo disso. Contribuições sem testes executados foram integradas sem verificação automática de comportamento. |
| Questão respondida | Q1.5 |
| Características desejáveis | Simples. Objetiva, porque usa os registros do próprio GitHub, e não a configuração declarada. Fácil de coletar automaticamente. Válida para RQ-MAN-13. |

---

## 8. Rastreabilidade com a Fase 01

| Requisito | Subcaracterística | Questão | Métricas |
| :--- | :--- | :--- | :--- |
| RQ-MAN-01 | Modularidade | Q1.1 | M1.1.2 |
| RQ-MAN-02 | Modularidade | Q1.1 | M1.1.1, M1.1.2 |
| RQ-MAN-03 | Modularidade | Q1.1 | M1.1.3 |
| RQ-MAN-04 | Reusabilidade | Q1.2 | M1.2.1 |
| RQ-MAN-05 | Reusabilidade | Q1.2 | M1.2.2 |
| RQ-MAN-06 | Analisabilidade | Q1.3 | M1.3.1 |
| RQ-MAN-07 | Analisabilidade | Q1.3 | M1.3.2 |
| RQ-MAN-08 | Analisabilidade | Q1.3 | M1.3.3 |
| RQ-MAN-09 | Modificabilidade | Q1.4 | M1.4.1 |
| RQ-MAN-10 | Modificabilidade | Q1.4 | M1.4.2, M1.4.3 |
| RQ-MAN-11 | Testabilidade | Q1.5 | M1.5.1 |
| RQ-MAN-12 | Testabilidade | Q1.5 | M1.5.2 |
| RQ-MAN-13 | Testabilidade | Q1.5 | M1.5.3 |

Todos os 13 requisitos de Manutenibilidade da Fase 01 são atendidos por pelo menos uma métrica.

---

## 9. Verificação das métricas

A aula pede verificar se as métricas podem ser coletadas e se são consistentes com as questões e o objetivo (AULA 08, p. 42). A equipe fez essa verificação no código da versão avaliada, sem registrar valores, porque a medição propriamente dita pertence à Fase 04.

| Métrica | O que foi verificado |
| :--- | :--- |
| M1.1.1 e M1.1.3 | O Madge 8.0.0 monta o grafo de dependências do código usando o `tsconfig.json` do repositório, que mapeia os nomes `@excalidraw/*` para as pastas dos pacotes. |
| M1.1.2 | A regra de direção existe em `packages/eslintrc.base.json`, mas só `common` e `element` têm configuração que a estende; por isso a coleta usa o grafo de M1.1.1, e não o lint. O projeto exige importações de tipo separadas (regra `consistent-type-imports` em `.eslintrc.json`), o que permite distinguir importações de tipo das de valor. |
| M1.2.1 | Os pacotes de base têm código-fonte próprio em `packages/*/src`, onde a busca pode ser feita. A dependência transitiva é necessária: `packages/utils/src/index.ts` reexporta valores de `@excalidraw/excalidraw/scene/export`, que usa `document`, e uma busca restrita a `utils` não encontraria esse uso. |
| M1.2.2 | O tipo `ExcalidrawProps` está em `packages/excalidraw/types.ts`, e a documentação das propriedades está em `dev-docs/docs/@excalidraw/excalidraw/api/props/`. |
| M1.3.1 | O ESLint 8.57.0 com `@typescript-eslint/parser` analisou com sucesso um arquivo `.tsx` do editor e informou a complexidade e as linhas de início e fim de cada função, o que permite contar as linhas próprias de cada uma. A ferramenta lizard foi descartada porque não reconheceu a maior parte das funções em arquivos `.tsx`. |
| M1.3.2 | `README.md`, `CONTRIBUTING.md` (que remete à documentação publicada) e a pasta `dev-docs/docs/` estão na versão avaliada. |
| M1.3.3 e M1.5.3 | O fluxo `lint.yml` é disparado por `pull_request` e executa os scripts de formatação, lint e tipos. O fluxo `test-coverage-pr.yml` é disparado por `pull_request` e executa os testes no passo `Test Coverage`, depois da instalação das dependências. A API do GitHub retorna, para cada execução do fluxo, os passos do job com conclusão e horário de término. |
| M1.4.1 e M1.4.3 | A API do GitHub retorna as contribuições integradas e a lista de arquivos alterados por cada uma. |
| M1.4.2 | O cloc 1.86 contou as linhas de código de arquivos `.ts` da versão avaliada, separando linhas em branco e comentários. |
| M1.5.1 | O script `test:coverage` e a configuração de cobertura existem na versão avaliada. A execução depende da instalação das dependências do projeto, que será feita no ambiente definido no plano de avaliação. |
| M1.5.2 | As suítes estão em arquivos `*.test.ts(x)` dos pacotes, e os utilitários de teste do editor (`packages/excalidraw/tests/test-utils.ts`) expõem a função `render`. As pastas `tests/` também têm arquivos de apoio, como `test-utils.ts` e `helpers/`, que a convenção da seção 2 deixa fora da contagem. |

---

## Referências

- AULA 08 QSW1 GQM. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Páginas 33, 34, 38, 41 e 42.
- Especificação do trabalho final da disciplina de Qualidade de Software 1 (2026-2 Trabalho final completo v1). Página 1, premissa 2.
- MARTIN, R. C. *Agile Software Development: Principles, Patterns, and Practices*. Prentice Hall, 2002.
- HEITLAGER, I.; KUIPERS, T.; VISSER, J. A Practical Model for Measuring Maintainability. In: *6th International Conference on the Quality of Information and Communications Technology (QUATIC 2007)*. IEEE, 2007. p. 30–39. Página 6 da versão dos autores, disponível em: https://www.di.uminho.pt/~joost/publications/HeitlagerKuipersVisser-Quatic2007.pdf.
- McCABE, T. J. A Complexity Measure. *IEEE Transactions on Software Engineering*, v. SE-2, n. 4, p. 308–320, 1976.
- ISO/IEC 25010:2023. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model*.
- Excalidraw. Repositório oficial, commit `e1b7aac` de 18/10/2026. Disponível em: https://github.com/excalidraw/excalidraw/tree/e1b7aacb356a492aa1e0fc6eb57b8896124027f0.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 19/10/2026 | Criação das questões, hipóteses e métricas do objetivo G1 | [Christopher Paraizo](https://github.com/wChrstphr) | [Luiz Henrique Soares](https://github.com/luizh-gsoares), [Maria Eduarda](https://github.com/eduarda-ogomes) |
| 1.1 | 19/10/2026 | M1.3.1 passa a medir o perfil de risco de complexidade em linhas de código, para usar as faixas de Heitlager, Kuipers e Visser (2007) | [Christopher Paraizo](https://github.com/wChrstphr) | |
