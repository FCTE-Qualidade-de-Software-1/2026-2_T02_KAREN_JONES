---
sidebar_position: 3
title: Recursos e ambiente de avaliação
description: Hardware, software, ambiente limpo, ferramentas com versões, massa de dados e conhecimento exigido do avaliador para a coleta da Fase 04
---

import Link from '@docusaurus/Link';

# Recursos e ambiente de avaliação

## Introdução

O plano de avaliação da Fase 03 inclui a especificação dos recursos necessários para executar a avaliação [[1, p. 18]](#ref-1). As convenções de coleta de [G2](../fase-02/gqm-confiabilidade.md#2-convenções-de-coleta) e [G3](../fase-02/gqm-flexibilidade.md#2-convenções-de-coleta) deixaram o ambiente exato para esta fase, que o define e o registra em cada coleta.

O objetivo desta página é especificar os recursos e o ambiente da coleta da Fase 04: o commit avaliado, as máquinas dos responsáveis, o sistema operacional, o navegador, as ferramentas com suas versões, a massa de dados e o conhecimento exigido do avaliador.

## Metodologia

As versões do produto vêm do `package.json` [[2]](#ref-2) e do `Dockerfile` [[3]](#ref-3) do Excalidraw no commit avaliado. As máquinas, o dispositivo de toque e as versões efetivas das ferramentas foram informados por cada responsável antes da coleta, e os campos marcados como _a preencher_ dependem desses dados. A seção 8 liga cada recurso às métricas que dependem dele, e a seção 9 lista os fatores de variação que cada coleta registra. O método e os passos de coleta estão no [método de avaliação](./metodo-avaliacao.md) e nas instruções de [G1](./instrucoes-g1-manutenibilidade.md), [G2](./instrucoes-g2-confiabilidade.md) e [G3](./instrucoes-g3-flexibilidade.md), e as datas no [cronograma](./cronograma-avaliacao.md).

---

## 1. Linha de base

<p className="tabela-titulo">Tabela 1: Linha de base da avaliação</p>

| Item | Valor | Fonte |
| :--- | :--- | :--- |
| Produto | Excalidraw: aplicação web e biblioteca `@excalidraw/excalidraw` | [Escopo](../fase-01/escopo-avaliacao.md) |
| Commit avaliado | `e1b7aacb356a492aa1e0fc6eb57b8896124027f0` (`e1b7aac`), de 18/10/2026, ramo `master` | [Escopo](../fase-01/escopo-avaliacao.md) |
| Janela histórica | 18/04/2026 a 18/10/2026 | Convenções de coleta de [G1](../fase-02/gqm-manutenibilidade.md#2-convenções-de-coleta) e [G2](../fase-02/gqm-confiabilidade.md#2-convenções-de-coleta) |
| Gerenciador de pacotes do projeto | Yarn 1.22.22 | Campo `packageManager` do `package.json` da raiz, no commit |
| Node.js exigido pelo projeto | `>=18.0.0` | Campo `engines` do `package.json` da raiz, no commit |
| Node.js da imagem Docker do projeto | 24, fixado pelo digest `sha256:8530f76a96d88820d288761f022e318970dda93d01536919fbc16076b7983e63` | `Dockerfile`, no commit |
| Servidor da imagem Docker do projeto | `nginx:stable-alpine-slim`, fixado pelo digest `sha256:2c605dbeab79a6b2a63340474fe58119d0ef95bdc4b1f41df0aa689659b3d13b` | `Dockerfile`, no commit |
| TypeScript, Vite, Vitest | 5.9.3, 5.0.12 e 3.0.6 (com `@vitest/coverage-v8` 3.0.7) | `package.json` da raiz, no commit |

<p className="tabela-fonte">Fonte: [Letícia de Carvalho](https://github.com/LeticiaSantosss), 2026.</p>

O projeto exige Node.js 18 ou mais recente, mas a imagem Docker oficial usa a versão 24. A coleta usa a versão do `Dockerfile` (seção 2). Qualquer teste feito com outra versão de Node.js é registrado como fator de variação (seção 9).

---

## 2. Ambiente de código, ambiente limpo e aplicação em execução

### 2.1 Preparação a partir do commit avaliado

Todos os responsáveis partem do mesmo commit:

```bash
git clone https://github.com/excalidraw/excalidraw.git
cd excalidraw
git checkout e1b7aacb356a492aa1e0fc6eb57b8896124027f0
git rev-parse HEAD
```

O último comando deve imprimir `e1b7aacb356a492aa1e0fc6eb57b8896124027f0`. Se imprimir outro valor, a coleta não pode começar. A comparação usa o hash completo porque `git rev-parse --short HEAD` pode imprimir mais de 7 caracteres, como `e1b7aacb3`, conforme o tamanho do repositório.

O Yarn não vem com o Node.js. Antes de instalar as dependências, ative-o pelo Corepack, que acompanha o Node.js, e confira a versão:

```bash
corepack enable
yarn --version
```

O comando deve imprimir `1.22.22`, a versão do campo `packageManager`. No Ubuntu, o pacote `cmdtest` instala outro programa chamado `yarn`, que imprime `0.32+git`. Nesse caso, remova o pacote com `sudo apt remove cmdtest` ou instale o Yarn com `npm install -g yarn@1.22.22`, e repita a conferência.

Para as métricas que dependem do código (análise estática e testes), as dependências são instaladas com a mesma opção do `Dockerfile` do projeto:

```bash
yarn --frozen-lockfile --network-timeout 600000
CI=true yarn test:coverage --minWorkers=1 --maxWorkers=8
yarn build:packages
```

`--frozen-lockfile` impede que as versões de dependências mudem em relação ao `yarn.lock` do commit. `yarn test:coverage` é o comando de cobertura do próprio projeto, usado em [M1.5.1](../fase-02/gqm-manutenibilidade.md#m151-cobertura-de-linhas-por-pacote). Três cuidados evitam falhas que não vêm do código avaliado:

<p className="tabela-titulo">Tabela 2: Cuidados na execução da cobertura</p>

| Cuidado | Motivo |
| :--- | :--- |
| Rodar a cobertura antes de `yarn build:packages` | Com as pastas `packages/*/dist` presentes, os testes de `Sidebar.test.tsx` e `DefaultSidebar.test.tsx` carregam duas cópias do contexto do editor e falham (10 testes e 10 erros). O fluxo de testes do projeto também não constrói os pacotes antes. Se elas já existirem, remova-as com `rm -rf packages/*/dist` antes da cobertura. |
| `CI=true` | Sem ele, o Vitest termina os testes e fica aguardando alterações nos arquivos, sem encerrar o comando. |
| `--minWorkers=1 --maxWorkers=8` | Com todos os núcleos em uso, o teste de exportação com fonte CJK de `export.test.ts` passa do limite de 30 segundos. O número de processos usado é registrado como fator de variação (seção 9). |

<p className="tabela-fonte">Fonte: [Christopher Paraizo](https://github.com/wChrstphr), 2026.</p>

Em 11/11/2026, essa sequência executou a suíte de testes sem falhas e gerou o relatório de cobertura na máquina de Christopher Paraizo.

### 2.2 Ambiente limpo

O ambiente limpo segue as [convenções de coleta de G3](../fase-02/gqm-flexibilidade.md#2-convenções-de-coleta): contêiner ou máquina virtual sem ferramentas de desenvolvimento além das exigidas pela métrica. Ele é usado em [M3.1.2](../fase-02/gqm-flexibilidade.md#m312-proporção-de-ambientes-de-integração-com-sucesso), [M3.3.1](../fase-02/gqm-flexibilidade.md#m331-proporção-de-operações-de-pacote-bem-sucedidas) e [M3.3.2](../fase-02/gqm-flexibilidade.md#m332-proporção-de-passos-documentados-reproduzidos-sem-ajuste). Para os passos com Node.js, a imagem é a mesma do `Dockerfile` do Excalidraw, fixada pelo digest:

```bash
docker run --rm -it node:24@sha256:8530f76a96d88820d288761f022e318970dda93d01536919fbc16076b7983e63 bash
```

Dentro do contêiner, o avaliador clona o repositório e segue somente o guia do projeto, sem instalar antes as ferramentas da [seção 5](#5-ferramentas-de-análise-e-suas-versões). Toda ferramenta que faltar e que o guia não declare é registrada como pré-requisito não declarado, como pede M3.3.2. As versões de `node`, `npm`, `yarn` e `pnpm` do contêiner são registradas na primeira coleta e comparadas com as da seção 5.

A imagem `node:24` não traz Docker. Por isso, os passos com Docker Compose de M3.3.2 rodam numa máquina virtual limpa que tem apenas Docker e Docker Compose instalados, o mesmo ambiente de [M3.3.3](../fase-02/gqm-flexibilidade.md#m333-implantação-com-docker). As versões dos dois são registradas na coleta.

### 2.3 Aplicação em execução (ambiente de teste)

As convenções de G2 e G3 definem o ambiente de teste como a aplicação web construída a partir do commit avaliado, executada localmente com a configuração de produção. A página usa a imagem do próprio `Dockerfile` do projeto, que gera a compilação de produção e a serve com nginx:

```bash
docker build -t excalidraw-avaliacao .
docker run -d --name excalidraw-avaliacao -p 3000:80 excalidraw-avaliacao
```

A aplicação abre no navegador em `http://localhost:3000`. Navegadores tratam `localhost` como origem segura, o que permite registrar o _service worker_ exigido por [M2.2.1](../fase-02/gqm-confiabilidade.md#m221-proporção-de-funções-essenciais-disponíveis-sem-conexão).

Duas regras evitam erros de configuração:

- O `docker-compose.yml` do projeto passa `NODE_ENV=development` na construção e desativa a verificação de saúde. Por isso ele **não** é usado para o ambiente de teste de G2 e G3 nem para a verificação 3 de [M3.3.3](../fase-02/gqm-flexibilidade.md#m333-implantação-com-docker), que depende da verificação de saúde do `Dockerfile`. Para M3.3.3 usam-se `docker build` e `docker run`, e o estado da verificação é lido com `docker inspect --format '{{.State.Health.Status}}' excalidraw-avaliacao`.
- O `docker-compose.yml` é usado só em [M3.3.2](../fase-02/gqm-flexibilidade.md#m332-proporção-de-passos-documentados-reproduzidos-sem-ajuste), porque o guia de desenvolvimento do projeto traz passos com Docker Compose e a métrica mede se eles funcionam como escritos.

### 2.4 Rede e serviços externos

<p className="tabela-titulo">Tabela 3: Rede e serviços externos</p>

| Recurso | Métricas que dependem | Observação |
| :--- | :--- | :--- |
| Internet aberta durante a coleta | [M2.3.2](../fase-02/gqm-confiabilidade.md#m232-continuidade-do-editor-após-falha-da-colaboração), [M3.1.1](../fase-02/gqm-flexibilidade.md#m311-cobertura-de-usuários-pelos-navegadores-declarados), [M3.1.2](../fase-02/gqm-flexibilidade.md#m312-proporção-de-ambientes-de-integração-com-sucesso), [M3.3.1](../fase-02/gqm-flexibilidade.md#m331-proporção-de-operações-de-pacote-bem-sucedidas) | M2.3.2 usa o servidor de colaboração configurado na versão avaliada. Ele é infraestrutura de produção operada pelo projeto, coberta pela exclusão de servidores gerenciados de produção ([Escopo, seção 4](../fase-01/escopo-avaliacao.md)), e o objeto O3 limita a análise ao código do cliente ([Escopo, seção 2](../fase-01/escopo-avaliacao.md)). O resultado vale para o comportamento do cliente, não para o serviço. |
| Registro npm | [M3.1.2](../fase-02/gqm-flexibilidade.md#m312-proporção-de-ambientes-de-integração-com-sucesso), [M3.3.1](../fase-02/gqm-flexibilidade.md#m331-proporção-de-operações-de-pacote-bem-sucedidas) | M3.3.1 também instala a versão publicada 0.17.6. |
| API do GitHub, com a CLI `gh` autenticada | [M1.4.1](../fase-02/gqm-manutenibilidade.md#m141-mediana-de-arquivos-de-produção-alterados-por-contribuição), [M1.4.3](../fase-02/gqm-manutenibilidade.md#m143-proporção-de-contribuições-que-alteram-arquivos-extensos), [M1.5.3](../fase-02/gqm-manutenibilidade.md#m153-proporção-de-contribuições-com-testes-executados-antes-da-integração), [M2.1.1](../fase-02/gqm-confiabilidade.md#m211-proporção-de-correções-entre-as-contribuições-integradas), [M2.1.2](../fase-02/gqm-confiabilidade.md#m212-mediana-do-tempo-entre-o-relato-e-a-correção), [M2.1.3](../fase-02/gqm-confiabilidade.md#m213-proporção-de-contribuições-revisadas-antes-da-integração) | A autenticação evita o limite de requisições de usuários anônimos. As respostas brutas são salvas no repositório da avaliação. |
| Base de uso de navegadores (`caniuse-lite`) | [M3.1.1](../fase-02/gqm-flexibilidade.md#m311-cobertura-de-usuários-pelos-navegadores-declarados) | A base muda com o tempo. A versão usada e a data da coleta são registradas. |

<p className="tabela-fonte">Fonte: [Letícia de Carvalho](https://github.com/LeticiaSantosss), 2026.</p>

---

## 3. Máquinas dos responsáveis pela coleta

Cada responsável registra a sua máquina antes de coletar. A tabela abaixo é preenchida uma vez, e cada coleta aponta para a linha usada (seção 9).

<p className="tabela-titulo">Tabela 4: Máquinas dos responsáveis pela coleta</p>

| Responsável | Métricas coletadas | Processador | Memória | Sistema operacional e versão | Navegador e versão |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Christopher Paraizo | Análise estática e histórico: M1.1.1 a M1.5.3 | Intel Core i7-12650H | 32 GB | Windows 11 Pro 25H2 (build 26200.9711), com WSL2 (Ubuntu 24.04.5 LTS) | não se aplica |
| Luiz Henrique Soares | Histórico de defeitos: M2.1.1 a M2.1.3 | Intel(R) Core(TM) i5-14450HX | 15,6 GB utilizável (16 GB instalados) | Windows 11 Home Single Language (Build 26300) | não se aplica |
| Luiz Henrique Soares | Testes no navegador de G2: M2.2.1 a M2.4.3 | Intel(R) Core(TM) i5-14450HX | 15,6 GB utilizável (16 GB instalados) | Windows 11 Home Single Language (Build 26300) | Mozilla Firefox 159.0.1 |
| Maria Eduarda | Adaptabilidade, instalabilidade e substituibilidade: M3.1.1, M3.1.2, M3.3.1 a M3.4.3 | AMD Ryzen 7 5700U with Radeon Graphics | 10 GB utilizável (16 GB instalados) | Zorin OS 18.1 (Kernel Linux 7.0.0-34-generic) | Mozilla Firefox 159.0.1 |
| Maria Eduarda | Escalabilidade: M3.2.1 a M3.2.3 | AMD Ryzen 7 5700U with Radeon Graphics | 10 GB utilizável (16 GB instalados) | Zorin OS 18.1 (Kernel Linux 7.0.0-34-generic) | Mozilla Firefox 159.0.1 |

<p className="tabela-fonte">Fonte: [Letícia de Carvalho](https://github.com/LeticiaSantosss), 2026.</p>

**Máquina de desempenho.** [M3.2.1](../fase-02/gqm-flexibilidade.md#m321-tempo-de-abertura-por-tamanho-de-cena) e [M3.2.2](../fase-02/gqm-flexibilidade.md#m322-taxa-de-quadros-durante-a-edição-por-tamanho-de-cena) dependem do hardware, porque o tempo de abertura e a taxa de quadros mudam com o processador, a memória, a placa gráfica e a tela. Por isso elas são coletadas somente na máquina da Maria Eduarda, e resultados dessas duas métricas obtidos em outra máquina não são usados. [M3.2.3](../fase-02/gqm-flexibilidade.md#m323-tamanho-máximo-de-cena-salva-e-exportada) é coletada na mesma máquina, porque compara o salvamento e a exportação com o tempo de abertura de M3.2.1 na mesma cena. Na máquina da Maria Eduarda, a placa gráfica é a **AMD Radeon Graphics (integrada, Lucienne)** e a tela opera em **Full HD (1920 × 1080) a 60 Hz**, atendendo à [faixa de M3.2.2](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3), que converte os quadros por segundo em percentual da meta de 60 quadros.

**Condições de controle nas coletas de desempenho.** Carregador conectado, mesmo modo de energia em todas as repetições, navegador com perfil novo e sem extensões, uma única aba aberta, zoom de 100% e nenhum outro programa pesado em execução.

**Navegador.** Todos os testes no navegador usam o mesmo navegador e a mesma versão, fixados antes da Fase 04: Mozilla Firefox 159.0.1. Os testes de G2 e G3 exigem do navegador as funções de: modo _offline_, bloqueio de requisições por domínio, exportação do registro de rede (HAR), painel de desempenho (_Performance_) e limpeza do armazenamento local. A atualização automática do navegador fica desligada durante a coleta.

**Sistema operacional.** O cenário 4 de [M2.4.1](../fase-02/gqm-confiabilidade.md#m241-proporção-de-cenários-de-fechamento-com-restauração-do-desenho) exige encerrar o processo do navegador pelo sistema operacional. O comando ou o procedimento usado é registrado junto com o sistema operacional de quem coleta.

---

## 4. Dispositivo com toque e caneta (M3.1.3)

[M3.1.3](../fase-02/gqm-flexibilidade.md#m313-proporção-de-ações-de-edição-que-funcionam-por-toque-e-caneta) é um teste manual roteirizado em um _tablet_ ou celular com navegador de versão fixa, com gravação de tela.

<p className="tabela-titulo">Tabela 5: Dispositivo com toque e caneta</p>

| Campo | Valor |
| :--- | :--- |
| Modelo do aparelho | iPad (A16) |
| Sistema operacional e versão | iPadOS 26.6.1 |
| Navegador e versão | Safari (versão nativa do iPadOS 26.6.1) |
| Tela | 10.9" (Liquid Retina, 2360 × 1640) |
| Caneta (modelo, ou "não disponível") | Caneta Goojodoq |
| Responsável | Maria Eduarda |

<p className="tabela-fonte">Fonte: [Letícia de Carvalho](https://github.com/LeticiaSantosss), 2026.</p>

O aparelho precisa aceitar toque com mais de um dedo (ações 6 e 7: pinça e deslocamento com dois dedos) e ter teclado virtual (ação 8). Quando há caneta, as duas formas de entrada são testadas e pontuadas, e a pontuação da métrica é a média das duas ([Pontuação, seção 5.1](../fase-02/pontuacao-julgamento.md#51-justificativas-específicas)).

---

## 5. Ferramentas de análise e suas versões

A versão efetiva de cada ferramenta é registrada na primeira coleta, com o comando de versão e a saída. Versões já definidas na Fase 02 não mudam.

<p className="tabela-titulo">Tabela 6: Ferramentas de análise e suas versões</p>

| Ferramenta | Versão | Métricas | Comando de versão |
| :--- | :--- | :--- | :--- |
| Madge | 8.0.0 | M1.1.1, M1.1.2, M1.1.3, M1.2.1 | `madge --version` |
| ESLint, com `@typescript-eslint/parser` | 8.57.0 (ESLint), 5.62.0 (`@typescript-eslint/parser`) e 5.9.3 (TypeScript) | M1.3.1 | `npx eslint@8.57.0 --version` e `yarn why @typescript-eslint/parser`. Dentro do clone, `npx eslint --version` imprime 7.32.0, a versão do próprio projeto, que não é a usada na métrica |
| cloc | 1.86 | M1.4.2 | `cloc --version` |
| GitHub CLI (`gh`) | 2.102.0 | M1.4.1, M1.4.3, M1.5.3, M2.1.1, M2.1.2, M2.1.3 | `gh --version` |
| Vitest com `@vitest/coverage-v8` | 3.0.6 (Vitest) e 3.0.7 (coverage-v8) | M1.5.1 | `yarn vitest --version` |
| `grep` | GNU grep 3.11 (Ubuntu/WSL2, Christopher Paraizo) | M1.2.1, M1.5.2 | `grep --version` |
| Browserslist e `caniuse-lite` | 4.24.4 (Browserslist) / `caniuse-lite` 1.0.30001701 | M3.1.1 | `npx browserslist --version` e `yarn why caniuse-lite` |
| Node.js (ambiente Docker) | 24.16.0 | M3.3.1, M3.3.2 e M3.3.3 | `node --version` dentro do contêiner |
| Node.js (execução nativa) | Referência 24.16.0, a da imagem Docker (seção 1). Registrado: v24.16.0 (Christopher Paraizo) | M1.1.1, M1.1.2, M1.1.3, M1.2.1, M1.3.1, M1.5.1, M3.1.1 | `node --version` na máquina de quem coleta |
| Yarn | 1.22.22 | M1.5.1, M3.3.2 | `yarn --version` |
| npm e pnpm | npm 11.13.0 (Maria Eduarda e Christopher Paraizo). pnpm: _a preencher_ | M3.3.1 | `npm --version` e `pnpm --version` |
| Docker e Docker Compose | Docker 29.9.3 (Maria Eduarda) / Docker 29.9.0 (Christopher Paraizo) | M3.3.2, M3.3.3 | `docker --version` e `docker compose version` |
| Vite e Next.js dos projetos mínimos | _a preencher na criação dos projetos mínimos_ | M3.1.2 | `package.json` de cada projeto |
| Scripts e geradores de cenas da avaliação | Commit exato do repositório da avaliação | M1.1.1 a M1.5.3, M2.4.1 a M2.4.3, M3.2.1 a M3.2.3, M3.4.2, M3.4.3 | `git rev-parse HEAD` |

<p className="tabela-fonte">Fonte: [Letícia de Carvalho](https://github.com/LeticiaSantosss), 2026.</p>

As marcações v0.15.0, v0.16.4, v0.17.6 e v0.18.0, usadas em [M2.4.2](../fase-02/gqm-confiabilidade.md#m242-proporção-de-arquivos-reabertos-sem-perda), podem exigir uma versão de Node.js diferente da do commit avaliado. A versão usada em cada construção é registrada.

---

## 6. Massa de dados

Sem os dados de entrada abaixo, as métricas de Confiabilidade (G2) e Flexibilidade (G3) não podem ser calculadas. Todos os arquivos encontram-se versionados no repositório em `dados/fase-03/massa-de-dados/` e podem ser integralmente recriados por script, assegurando repetibilidade e reprodutibilidade independente.

<p className="tabela-titulo">Tabela 7: Massa de dados</p>

| Conjunto | Conteúdo | Origem | Métricas |
| :--- | :--- | :--- | :--- |
| Cena de referência | Ao menos um elemento de cada tipo: retângulo, elipse, losango, seta, linha, desenho livre, texto, texto dentro de forma, imagem e moldura (_frame_) | Criada pela equipe via script gerador | M2.4.1, M2.4.2, M3.4.2, M3.4.3 |
| Cenas de escala | Quatro cenas, com 100, 1.000, 5.000 e 10.000 elementos, em proporção fixa de 40% de retângulos, 20% de elipses, 20% de setas e 20% de textos, em grade | Geradas por script do repositório da avaliação | M3.2.1, M3.2.2, M3.2.3 |
| Roteiro de movimento | Arrastar uma seleção de 50 elementos e deslocar a tela, por 10 segundos, em 5 gravações por cena | Roteiro fixo da equipe | M3.2.2 |
| Arquivos inválidos | Os 9 casos listados em M2.3.1, de arquivo vazio a arquivo `.excalidraw` truncado | Preparados pela equipe via script gerador | M2.3.1 |
| Conjunto de reabertura | A cena de referência salva pela versão avaliada e pelas versões v0.15.0, v0.16.4, v0.17.6 e v0.18.0, mais `test_embedded_v1.png` e `smiley_embedded_v2.png` (7 arquivos) | Equipe e `packages/excalidraw/tests/fixtures/` | M2.4.2 |
| Dados do GitHub | Respostas brutas da API para a janela de 18/04/2026 a 18/10/2026 | Coletadas com `gh`, salvas em JSON | M1.4.1, M1.4.3, M1.5.3, M2.1.1, M2.1.2, M2.1.3 |
| Projetos mínimos | Um projeto para cada combinação de React 17, 18 e 19 com Vite e com Next.js (6 projetos) | Criados pela equipe a partir do guia de integração | M3.1.2 |

<p className="tabela-fonte">Fonte: [Letícia de Carvalho](https://github.com/LeticiaSantosss), 2026.</p>

### 6.1 Justificativa da massa de dados

Desenhar livremente durante as coletas impediria que dois avaliadores obtivessem o mesmo valor de tempo ou taxa de quadros. Por isso, a avaliação usa uma massa de dados fixa salva em `dados/fase-03/massa-de-dados/`, gerada por script.

- **Cena de referência:** reúne um elemento de cada um dos 10 tipos definidos na Fase 02 (retângulo, elipse, losango, seta, linha, desenho livre, texto solto, texto dentro de forma, imagem e moldura). Ela é usada em [M2.4.1](../fase-02/gqm-confiabilidade.md#m241-proporção-de-cenários-de-fechamento-com-restauração-do-desenho) (restauração de sessão após fechar a aba ou matar o processo), [M2.4.2](../fase-02/gqm-confiabilidade.md#m242-proporção-de-arquivos-reabertos-sem-perda) (compatibilidade de reabertura entre versões antigas e a atual), [M3.4.2](../fase-02/gqm-flexibilidade.md#m342-proporção-de-elementos-preservados-na-exportação-e-reimportação) (preservação de propriedades na exportação e reimportação em `.excalidraw`, PNG e SVG) e [M3.4.3](../fase-02/gqm-flexibilidade.md#m343-proporção-dos-campos-do-formato-excalidraw-documentados) (documentação dos campos do formato). Manter a mesma cena em todas essas métricas permite comparar os resultados diretamente.
- **Cenas de escala:** quatro arquivos com 100, 1.000, 5.000 e 10.000 elementos, na proporção de 40% retângulos, 20% elipses, 20% setas e 20% textos, dispostos em grade. Essa proporção reflete diagramas típicos, onde caixas e textos predominam sobre conexões. Os quatro volumes permitem traçar a curva de tempo de abertura ([M3.2.1](../fase-02/gqm-flexibilidade.md#m321-tempo-de-abertura-por-tamanho-de-cena)), medir a taxa de quadros ao arrastar 50 elementos ([M3.2.2](../fase-02/gqm-flexibilidade.md#m322-taxa-de-quadros-durante-a-edição-por-tamanho-de-cena)) e identificar o tamanho máximo de cena que a aplicação consegue salvar e exportar sem travar o navegador ([M3.2.3](../fase-02/gqm-flexibilidade.md#m323-tamanho-máximo-de-cena-salva-e-exportada)). A disposição em grade evita que formas fiquem escondidas umas atrás das outras.
- **Arquivos inválidos:** os 9 casos cobrem os erros de entrada mais comuns para avaliar a tolerância a falhas em [M2.3.1](../fase-02/gqm-confiabilidade.md#m231-proporção-de-arquivos-inválidos-tratados-com-mensagem): arquivo vazio, JSON com sintaxe quebrada, JSON sem o campo `type`, tipo desconhecido, elementos sem campos obrigatórios, coordenadas com texto ou `null`, arquivo binário renomeado para `.excalidraw`, imagem PNG comum sem desenho embutido e arquivo cortado pela metade. O teste verifica se o editor exibe mensagem de erro e continua utilizável em vez de travar o navegador.

O script [`scripts/gerar_massa_dados.py`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/scripts/gerar_massa_dados.py) recria toda a massa de dados com o comando:

```bash
python scripts/gerar_massa_dados.py --verificar
```

O detalhamento de cada arquivo está no [README da pasta de massa de dados](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/dados/fase-03/massa-de-dados/README.md).

---

## 7. Conhecimento exigido do avaliador

### 7.1 Informática

O avaliador precisa saber:

- Usar Git e a linha de comando (clonar, trocar de commit, executar scripts).
- Instalar e usar Node.js, npm, Yarn e pnpm.
- Construir e executar imagens Docker (`build`, `run`, `inspect`).
- Usar as ferramentas do navegador para rede, desempenho, modo _offline_ e bloqueio de requisições.
- Consultar a API do GitHub com `gh api`, incluindo consultas GraphQL.
- Ler TypeScript e React o suficiente para localizar arquivos, importações e funções citados nas métricas.
- Executar os scripts da avaliação e interpretar a saída.

### 7.2 Domínio da aplicação

O avaliador precisa ter usado o Excalidraw e saber criar formas, setas ligadas a formas, texto, molduras e imagens. Também precisa saber agrupar elementos, mudar a ordem de sobreposição, desfazer e refazer, salvar e abrir arquivos `.excalidraw`, exportar em PNG e SVG com os dados do desenho incorporados e abrir uma sessão de colaboração entre duas janelas.

### 7.3 Domínio da avaliação

O avaliador precisa conhecer o método GQM, as convenções de coleta de G1, G2 e G3, a escala de pontuação de `++` a `--` e as [regras de agregação](../fase-02/pontuacao-julgamento.md#6-agregação-da-métrica-à-característica), para registrar cada medida na unidade e na forma previstas.

---

## 8. Rastreabilidade: recursos e métricas

### 8.1 Recursos

<p className="tabela-titulo">Tabela 8: Recursos da avaliação</p>

| Código | Recurso | Seção | Métricas que dependem dele |
| :---: | :--- | :---: | :--- |
| R1 | Repositório clonado no commit `e1b7aac` | 2.1 | M1.1.1 a M1.5.3 |
| R2 | Node.js 24 e Yarn 1.22.22, com as dependências instaladas | 2.1 | M1.1.1, M1.1.2, M1.1.3, M1.2.1, M1.3.1, M1.5.1, M3.1.1 |
| R3 | Ferramentas de análise estática e scripts | 5 | M1.1.1, M1.1.2, M1.1.3, M1.2.1, M1.3.1, M1.4.2, M1.4.3, M1.5.2 |
| R4 | `gh` autenticado e acesso à API do GitHub | 2.4 | M1.4.1, M1.4.3, M1.5.3, M2.1.1, M2.1.2, M2.1.3 |
| R5 | Aplicação de produção (imagem Docker) e navegador de versão fixa | 2.3 e 3 | M2.2.1 a M2.4.3, M3.2.3, M3.4.1 a M3.4.3 |
| R6 | Máquina da Maria Eduarda | 3 | M3.2.1, M3.2.2, M3.2.3 |
| R7 | Dispositivo com toque e caneta | 4 | M3.1.3 |
| R8 | Massa de dados | 6 | M2.2.1, M2.3.1, M2.4.1 a M2.4.3, M3.2.1 a M3.2.3, M3.4.2, M3.4.3 |
| R9 | Ambiente limpo, com npm, Yarn, pnpm e Docker | 2.2 | M3.1.2, M3.3.1, M3.3.2, M3.3.3 |
| R10 | Gravação e captura de tela | 9 | M2.2.1, M2.3.1, M2.3.2, M3.1.3, M3.4.1 |
| R11 | Acesso à internet (servidor de colaboração, npm, base de navegadores) | 2.4 | M2.3.2, M3.1.1, M3.1.2, M3.3.1 |

<p className="tabela-fonte">Fonte: [Letícia de Carvalho](https://github.com/LeticiaSantosss), 2026.</p>

### 8.2 Métricas

<p className="tabela-titulo">Tabela 9: Recursos usados por métrica</p>

| Métrica | Recursos | Observação |
| :--- | :--- | :--- |
| M1.1.1, M1.1.2, M1.1.3 | R1, R2, R3 | Mesmo grafo de importações, gerado com o Madge. |
| M1.2.1 | R1, R2, R3 | `grep` mais o grafo de M1.1.1. |
| M1.2.2, M1.3.2, M1.3.3 | R1 | Inspeção de arquivos do repositório. |
| M1.3.1 | R1, R2, R3 | ESLint com a regra `complexity` e script. |
| M1.4.1 | R4 | Exclui contribuições automáticas e de traduções. |
| M1.4.2 | R1, R3 | `cloc`, com as convenções da seção 2 de G1. |
| M1.4.3 | R1, R3, R4 | Cruza o histórico com a lista de arquivos extensos. |
| M1.5.1 | R1, R2 | `yarn test:coverage`. |
| M1.5.2 | R1, R3 | `grep` no código de teste. |
| M1.5.3 | R4 | Execuções do fluxo `test-coverage-pr.yml`. |
| M2.1.1, M2.1.2, M2.1.3 | R4 | M2.1.2 e M2.1.3 usam a API GraphQL. |
| M2.2.1 | R5, R8, R10 | Rede desligada pelo modo _offline_ do navegador. |
| M2.2.2 | R5 | Registro de rede (HAR) com e sem bloqueio de cada domínio. |
| M2.3.1 | R5, R8, R10 | 9 arquivos, abertos pelo menu e arrastados. |
| M2.3.2 | R5, R10, R11 | Duas janelas, 3 repetições. |
| M2.4.1 | R5, R8 | Inclui encerrar o processo do navegador pelo sistema operacional. |
| M2.4.2 | R2, R5, R8 | Constrói a aplicação a partir das marcações de versões anteriores. |
| M2.4.3 | R5, R8 | Exporta a cena antes, depois, após desfazer e após refazer. |
| M3.1.1 | R2, R11 | `npx browserslist --coverage=global`. |
| M3.1.2 | R9, R11 | 6 projetos mínimos. |
| M3.1.3 | R7, R10 | Teste manual no dispositivo. |
| M3.2.1, M3.2.2 | R6, R8 | Somente na máquina da Maria Eduarda. |
| M3.2.3 | R5, R6, R8 | Na máquina da Maria Eduarda, compara com o tempo de abertura de M3.2.1 na mesma cena. |
| M3.3.1 | R9, R11 | npm, Yarn e pnpm. |
| M3.3.2 | R9 | Passos do guia de desenvolvimento, com Node.js, Yarn e Docker Compose. |
| M3.3.3 | R9 | `docker build` e `docker run`, sem Docker Compose. |
| M3.4.1 | R5, R10 | Inspeção dos menus de exportação. |
| M3.4.2, M3.4.3 | R5, R8 | Usam a cena de referência. |

<p className="tabela-fonte">Fonte: [Letícia de Carvalho](https://github.com/LeticiaSantosss), 2026.</p>

---

## 9. Fatores de variação registrados em cada coleta

Os fatores que podem influenciar os resultados são registrados junto com cada coleta. Cada coleta preenche os campos abaixo e guarda o registro ao lado dos dados brutos.

<p className="tabela-titulo">Tabela 10: Fatores de variação registrados em cada coleta</p>

| Campo | O que registrar |
| :--- | :--- |
| Métrica e responsável | Código da métrica e quem coletou |
| Data e hora | Início e fim da coleta |
| Commit | Saída de `git rev-parse HEAD` |
| Máquina | Linha da tabela da seção 3 (ou do aparelho da seção 4) |
| Sistema operacional e navegador | Versões exatas, incluindo o modo de energia nas coletas de desempenho |
| Versões das ferramentas | Saída dos comandos de versão da seção 5 |
| Node.js, Yarn e Docker | Versões usadas, e se diferem das da seção 1 |
| Rede | Conectada ou _offline_, e o servidor de colaboração, se usado |
| Estado do armazenamento | Cache e armazenamento local limpos ou não, e o perfil do navegador |
| Janela histórica e base de navegadores | Datas da janela e versão de `caniuse-lite`, quando aplicável |
| Evidências | Caminho dos arquivos de gravação de tela, capturas, HAR e dados brutos |
| Desvios | Qualquer diferença em relação ao método e o motivo |

<p className="tabela-fonte">Fonte: [Letícia de Carvalho](https://github.com/LeticiaSantosss), 2026.</p>

**Gravação de tela.** Os testes manuais no computador usam o software OBS Studio. A ferramenta grava a tela inteira com a hora visível, e os arquivos são salvos no repositório da avaliação com o código da métrica no nome. No aparelho de toque (iPad), usa-se a gravação de tela nativa do próprio iPadOS.

---

## Referências

> <Link id="ref-1">1.</Link> RAMOS, Cristiane Soares. **AULA A07 QSW1 PROC AVAL PRODUTO**. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Página 18. Disponível no Moodle da disciplina.
>
> <Link id="ref-2">2.</Link> EXCALIDRAW. [`package.json` da raiz do repositório no commit `e1b7aac`](https://github.com/excalidraw/excalidraw/blob/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/package.json). GitHub, 2026.
>
> <Link id="ref-3">3.</Link> EXCALIDRAW. [`Dockerfile`](https://github.com/excalidraw/excalidraw/blob/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/Dockerfile) e [`docker-compose.yml`](https://github.com/excalidraw/excalidraw/blob/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/docker-compose.yml) no commit `e1b7aac`. GitHub, 2026.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 05/11/2026 | Primeira versão da especificação de recursos e ambiente da Fase 04 | [Letícia Santos](https://github.com/LeticiaSantosss) | [Maria Eduarda](https://github.com/eduarda-ogomes) |
| 1.1 | 07/11/2026 | Preenchimento dos dados de hardware de Christopher e Maria Eduarda, especificações do tablet iPad (M3.1.3), ferramentas e gravação de tela | [Maria Eduarda](https://github.com/eduarda-ogomes) | [Letícia Santos](https://github.com/LeticiaSantosss) |
| 1.2 | 08/11/2026 | Detalhamento e justificativa da massa de dados para G2 e G3 | [Gabriel Santos](https://github.com/gabriel-nitro) | [Letícia Santos](https://github.com/LeticiaSantosss) |
| 1.3 | 09/11/2026 | Preenchimento dos dados de hardware de Luiz e das versões de ferramentas faltantes | [Letícia Santos](https://github.com/LeticiaSantosss) | |
| 1.4 | 10/11/2026 | Correção do ambiente limpo, das versões de Node.js, npm, Docker e TypeScript, dos links para as métricas de G3 e da formatação das tabelas | [Christopher Paraizo](https://github.com/wChrstphr) | |
| 1.5 | 11/11/2026 | Conferência do commit pelo hash completo, ativação do Yarn 1.22.22 antes da instalação das dependências, comando de versão do ESLint 8.57.0, ordem e opções do comando de cobertura e versões de Node.js e npm de Christopher Paraizo | [Christopher Paraizo](https://github.com/wChrstphr) | |
| 1.6 | 18/11/2026 | Revisão de coerência e cross-links: Introdução e Metodologia, M3.2.3 na máquina de Maria Eduarda e links às fichas | [Christopher Paraizo](https://github.com/wChrstphr) | |
