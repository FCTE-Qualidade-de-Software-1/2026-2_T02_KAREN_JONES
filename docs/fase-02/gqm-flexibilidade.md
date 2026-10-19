---
sidebar_position: 5
title: GQM de Flexibilidade (G3)
description: Questões, hipóteses e métricas do objetivo de medição G3, que avalia a flexibilidade da biblioteca e da aplicação web do Excalidraw
---

# GQM de Flexibilidade (G3)

Esta página detalha o objetivo G3, definido em [Método GQM e objetivos de medição](./estrutura-gqm.md#g3--flexibilidade-antiga-portabilidade). Para cada subcaracterística de Flexibilidade há uma questão, a hipótese da questão e as métricas que a respondem.

| Campo do template | Valor |
| :--- | :--- |
| Analisar | a biblioteca `@excalidraw/excalidraw` e a aplicação web, incluindo a interface pública da biblioteca, as instruções de instalação e os formatos de exportação |
| para o propósito de | entender |
| com respeito a | Flexibilidade: adaptabilidade, escalabilidade, instalabilidade e substituibilidade |
| do ponto de vista de | desenvolvedores que integram a biblioteca em seus sistemas e equipes de implantação e operação |
| no contexto de | código-fonte público na versão de 18/10/2026, avaliado por equipe independente |

As questões caracterizam o produto em relação a cada subcaracterística (AULA 08, p. 33 e 34). As hipóteses partem da [abstraction sheet de G3](./abstraction-sheets.md#5-g3--flexibilidade), como a aula permite (AULA 08, p. 34). As métricas respondem às questões de forma quantitativa (AULA 08, p. 38). Os níveis de pontuação e os critérios de julgamento de cada métrica são definidos em uma página própria da Fase 02.

---

## 1. Visão geral

| Questão | Subcaracterística | Requisitos da Fase 01 | Métricas |
| :--- | :--- | :--- | :--- |
| Q3.1 | Adaptabilidade | RQ-FLEX-01 a RQ-FLEX-04 | M3.1.1, M3.1.2, M3.1.3 |
| Q3.2 | Escalabilidade | RQ-FLEX-05 e RQ-FLEX-06 | M3.2.1, M3.2.2, M3.2.3 |
| Q3.3 | Instalabilidade | RQ-FLEX-07 a RQ-FLEX-10 | M3.3.1, M3.3.2, M3.3.3 |
| Q3.4 | Substituibilidade | RQ-FLEX-11 e RQ-FLEX-12 | M3.4.1, M3.4.2, M3.4.3 |

Os requisitos estão em [Requisitos da avaliação](../fase-01/requisitos-avaliacao.md). A seção 7 mostra qual métrica atende cada requisito.

---

## 2. Convenções de coleta

As definições abaixo valem para todas as métricas de G3 e evitam que pessoas diferentes testem coisas diferentes.

- **Versão avaliada:** commit `e1b7aac` do repositório oficial, de 18/10/2026, identificado no [escopo](../fase-01/escopo-avaliacao.md).
- **Pacote avaliado:** a biblioteca `@excalidraw/excalidraw` construída a partir da versão avaliada (script `build:packages` do repositório) e empacotada com `npm pack`. A versão publicada no npm mais próxima é usada só quando a métrica pede uma versão anterior.
- **Ambiente de teste:** a aplicação web construída a partir da versão avaliada e executada localmente, em uma máquina e em um navegador de versões fixas. O ambiente exato (máquina, sistema operacional, navegador, Node.js e gerenciadores de pacotes) é definido no plano de avaliação da Fase 03 e registrado em cada coleta.
- **Ambiente limpo:** contêiner ou máquina virtual sem as ferramentas de desenvolvimento instaladas além das exigidas pela métrica, para que nenhum pré-requisito esquecido passe despercebido.
- **Cena de referência:** desenho padronizado usado nos testes, com ao menos um elemento de cada tipo principal: retângulo, elipse, losango, seta, linha, desenho livre, texto, texto dentro de forma, imagem e moldura (*frame*). É a mesma cena usada no objetivo de Confiabilidade.
- **Cenas de escala:** cenas geradas por script com 100, 1.000, 5.000 e 10.000 elementos, em proporção fixa: 40% retângulos, 20% elipses, 20% setas e 20% textos, distribuídos em uma grade. O script fica no repositório da avaliação para que as cenas possam ser recriadas.

Os fatores que podem influenciar os resultados também são registrados junto com cada coleta (AULA 08, p. 38): o hardware, o navegador e sua versão, as versões de Node.js e dos gerenciadores de pacotes, e a composição das cenas de teste. Esses fatores foram levantados na abstraction sheet de G3.

---

## 3. Q3.1 — Adaptabilidade

**Questão:** O Excalidraw pode ser usado em diferentes navegadores, dispositivos e ambientes de integração sem adaptações no código?

**Requisitos:** RQ-FLEX-01 (navegadores suportados), RQ-FLEX-02 (versões de React, renderização no servidor e empacotadores), RQ-FLEX-03 (dependências que limitam ambientes) e RQ-FLEX-04 (dispositivos móveis, toque e caneta).

**Hipótese:** a aplicação funciona nas versões recentes dos principais navegadores, mas não em navegadores antigos. A biblioteca aceita mais de uma versão principal de React e precisa ser carregada apenas no navegador quando usada em frameworks com renderização no servidor. O editor aceita toque e caneta.

### M3.1.1 — Cobertura de usuários pelos navegadores declarados

| Campo | Descrição |
| :--- | :--- |
| Definição | Percentual dos usuários de navegadores no mundo cobertos pela lista de navegadores que a aplicação declara suportar. |
| Procedimento de cálculo | Aplicar a consulta de navegadores declarada no campo `browserslist` (perfil `production`) do `package.json` da aplicação à base de uso global da ferramenta Browserslist. Unidade: percentual. Escala: 0 a 100. Também é registrada a lista de navegadores excluídos explicitamente. |
| Fonte dos dados | Campo `browserslist` de `excalidraw-app/package.json` e de `packages/excalidraw/package.json`. |
| Procedimento de coleta | Comando `npx browserslist --coverage=global "<consulta>"`, registrando a versão da ferramenta e da base de dados de uso (`caniuse-lite`), porque a base muda com o tempo. |
| Critério de interpretação | Confirma a hipótese se a cobertura for alta e a lista excluir navegadores antigos. Quanto menor a cobertura, mais usuários ficam sem suporte declarado. |
| Questão respondida | Q3.1 |
| Características desejáveis | Simples. Objetiva, porque a lista é a que o próprio projeto declara e a base de uso é pública. Fácil de coletar com um comando. Robusta, porque permite comparar com outros projetos que usam a mesma ferramenta. |

### M3.1.2 — Proporção de ambientes de integração com sucesso

| Campo | Descrição |
| :--- | :--- |
| Definição | Percentual das combinações de versão de React e de empacotador em que um projeto mínimo constrói e exibe o editor sem erros. |
| Procedimento de cálculo | Combinações: React 17, 18 e 19 (as versões declaradas em `peerDependencies`) com Vite e com Next.js, este usando a importação apenas no navegador indicada na documentação. São 6 combinações. Uma combinação tem sucesso se o projeto constrói sem erros e o editor aparece e permite criar uma forma. Calcular (combinações com sucesso ÷ 6) × 100. Unidade: percentual. Escala: 0 a 100. |
| Fonte dos dados | Pacote avaliado; campo `peerDependencies` de `packages/excalidraw/package.json`; guia de integração em `dev-docs/docs/@excalidraw/excalidraw/integration.mdx`; exemplo `examples/with-nextjs`. |
| Procedimento de coleta | Criar um projeto mínimo para cada combinação seguindo apenas o guia de instalação e integração, instalar o pacote avaliado, construir e abrir no navegador do ambiente de teste. Registrar erros de construção e de execução. |
| Critério de interpretação | Confirma a hipótese se as 6 combinações tiverem sucesso. Cada combinação que falha é um ambiente em que o integrador precisa adaptar o próprio sistema para usar a biblioteca. |
| Questão respondida | Q3.1 |
| Características desejáveis | Objetiva, porque o critério de sucesso é definido antes do teste. Válida, porque testa a integração de fato, e não só a declaração de compatibilidade. Robusta, porque a matriz pode crescer com novas versões. |

### M3.1.3 — Proporção de ações de edição que funcionam por toque e caneta

| Campo | Descrição |
| :--- | :--- |
| Definição | Percentual de uma lista fixa de ações de edição que podem ser feitas em um dispositivo com tela de toque, sem mouse nem teclado físico. |
| Procedimento de cálculo | Ações: (1) criar uma forma; (2) desenhar à mão livre; (3) selecionar um elemento; (4) mover um elemento; (5) redimensionar um elemento; (6) aproximar e afastar com pinça; (7) deslocar a tela com dois dedos; (8) escrever texto com o teclado virtual; (9) desfazer; (10) abrir o menu principal. Calcular (ações que funcionam ÷ 10) × 100, separadamente para toque com o dedo e para caneta, quando houver caneta disponível. Unidade: percentual. Escala: 0 a 100. |
| Fonte dos dados | Aplicação web em um *tablet* ou celular com navegador de versão fixa, definido no plano de avaliação; tratamento de eventos de toque e caneta em `packages/excalidraw/components/App.tsx`. |
| Procedimento de coleta | Teste manual roteirizado no dispositivo, registrando cada ação como funciona ou não funciona, com gravação de tela. |
| Critério de interpretação | Confirma a hipótese se o valor for 100%. Cada ação que falha é algo que o usuário de dispositivo móvel não consegue fazer. |
| Questão respondida | Q3.1 |
| Características desejáveis | Simples. Objetiva, porque cada ação tem resultado binário com evidência gravada. Válida para RQ-FLEX-04. |

---

## 4. Q3.2 — Escalabilidade

**Questão:** O editor continua utilizável quando o desenho cresce?

**Requisitos:** RQ-FLEX-05 (desempenho com mais elementos) e RQ-FLEX-06 (abrir, salvar e exportar desenhos grandes).

**Hipótese:** o editor continua utilizável com algumas centenas de elementos, e o desempenho cai de forma perceptível com milhares. Exportar um desenho grande é mais lento do que abri-lo.

### M3.2.1 — Tempo de abertura por tamanho de cena

| Campo | Descrição |
| :--- | :--- |
| Definição | Tempo entre a abertura de um arquivo e a exibição completa da cena, para cada uma das cenas de escala. |
| Procedimento de cálculo | Mediana de 5 aberturas de cada cena, em segundos. O resultado é uma curva de tempo por número de elementos. Unidade: segundos. Escala: absoluta. |
| Fonte dos dados | Aplicação web no ambiente de teste; cenas de escala. |
| Procedimento de coleta | Gravação no painel de desempenho (*Performance*) das ferramentas do navegador, do momento em que o arquivo é solto no editor até o último quadro desenhado. A página é recarregada e o armazenamento local é limpo entre as repetições. |
| Critério de interpretação | Confirma a hipótese se o tempo for baixo até 1.000 elementos e crescer de forma perceptível a partir daí. A forma da curva mostra se o tempo cresce na mesma proporção do desenho ou mais rápido que ele. |
| Questão respondida | Q3.2 |
| Características desejáveis | Objetiva, porque a medição é feita pela ferramenta do navegador. Robusta, por usar a mediana de repetições. Válida para RQ-FLEX-06. Depende do hardware, que é fixado e registrado. |

### M3.2.2 — Taxa de quadros durante a edição por tamanho de cena

| Campo | Descrição |
| :--- | :--- |
| Definição | Quadros por segundo exibidos enquanto o usuário arrasta um grupo de elementos e desloca a tela, para cada uma das cenas de escala. |
| Procedimento de cálculo | Mediana dos quadros por segundo em 5 gravações de 10 segundos para cada cena: arrastar uma seleção de 50 elementos e deslocar a tela. Unidade: quadros por segundo. Escala: absoluta. |
| Fonte dos dados | Aplicação web no ambiente de teste; cenas de escala. |
| Procedimento de coleta | Painel de desempenho das ferramentas do navegador, com roteiro de movimento fixo. |
| Critério de interpretação | Confirma a hipótese se a taxa for fluida até algumas centenas de elementos e cair de forma perceptível com milhares. Taxas baixas significam movimento travado para o usuário. |
| Questão respondida | Q3.2 |
| Características desejáveis | Objetiva e robusta, pelos mesmos motivos de M3.2.1. Válida para RQ-FLEX-05, porque mede o que o usuário percebe ao editar. |

### M3.2.3 — Tamanho máximo de cena salva e exportada

| Campo | Descrição |
| :--- | :--- |
| Definição | Maior cena de escala que pode ser salva em `.excalidraw` e exportada em PNG e em SVG sem que o navegador trave. |
| Procedimento de cálculo | Para cada cena, em ordem crescente, executar salvar, exportar em PNG e exportar em SVG, registrando o tempo de cada operação. A operação falha se não termina em 30 segundos ou se o navegador avisa que a página não está respondendo. O resultado é o número de elementos da maior cena em que as três operações terminam. Unidade: elementos. Escala: ordinal (100, 1.000, 5.000 ou 10.000). |
| Fonte dos dados | Aplicação web no ambiente de teste; cenas de escala. |
| Procedimento de coleta | Teste manual roteirizado com cronômetro do painel de desempenho, comparando o tempo de exportar com o tempo de abrir (M3.2.1) na mesma cena. |
| Critério de interpretação | Confirma a hipótese se as cenas maiores forem abertas mas tiverem exportação mais lenta que a abertura. O valor mostra até onde o usuário pode levar um desenho sem perder a capacidade de salvar e compartilhar. |
| Questão respondida | Q3.2 |
| Características desejáveis | Simples. Objetiva, porque o limite de tempo é fixo. Válida para RQ-FLEX-06. |

---

## 5. Q3.3 — Instalabilidade

**Questão:** A biblioteca e a aplicação podem ser instaladas, construídas e implantadas seguindo apenas a documentação, em ambientes diferentes?

**Requisitos:** RQ-FLEX-07 (instalar, atualizar e remover a biblioteca), RQ-FLEX-08 (construção, implantação e pré-requisitos), RQ-FLEX-09 (suporte a Docker) e RQ-FLEX-10 (instruções documentadas e reproduzíveis).

**Hipótese:** a biblioteca é instalada com um único comando dos gerenciadores de pacotes usuais. A imagem Docker é construída sem passos manuais adicionais, e as instruções de execução local são suficientes, desde que as versões de ferramentas exigidas sejam respeitadas.

### M3.3.1 — Proporção de operações de pacote bem-sucedidas

| Campo | Descrição |
| :--- | :--- |
| Definição | Percentual das operações de instalação, atualização e remoção da biblioteca que terminam sem erro nos gerenciadores de pacotes usuais. |
| Procedimento de cálculo | Gerenciadores: npm, Yarn e pnpm. Operações: (1) instalar o pacote avaliado em um projeto React vazio; (2) atualizar da versão publicada 0.17.6 para o pacote avaliado; (3) remover o pacote. São 9 combinações. Uma operação tem sucesso se termina sem erro e o projeto continua construindo. Também é registrado o número de comandos de cada instalação. Calcular (operações com sucesso ÷ 9) × 100. Unidade: percentual. Escala: 0 a 100. |
| Fonte dos dados | Pacote avaliado; versão 0.17.6 do registro npm; guia de instalação em `dev-docs/docs/@excalidraw/excalidraw/installation.mdx`. |
| Procedimento de coleta | Execução dos comandos em ambiente limpo, registrando a saída de cada um. |
| Critério de interpretação | Confirma a hipótese se o valor for 100% e a instalação exigir um único comando. Cada operação que falha é um passo que o integrador precisa resolver por conta própria. |
| Questão respondida | Q3.3 |
| Características desejáveis | Simples. Objetiva, porque o sucesso é dado pelo código de saída dos comandos. Fácil de coletar. Válida para RQ-FLEX-07. |

### M3.3.2 — Proporção de passos documentados reproduzidos sem ajuste

| Campo | Descrição |
| :--- | :--- |
| Definição | Percentual dos passos das instruções oficiais de execução local que funcionam exatamente como escritos, em ambiente limpo. |
| Procedimento de cálculo | Numerar cada comando ou ação das seções de execução local (com Node.js e Yarn) e com Docker Compose do guia de desenvolvimento. Executar os passos na ordem. Um passo é reproduzido sem ajuste se funciona sem nenhuma ação não escrita no guia. Calcular (passos reproduzidos sem ajuste ÷ total de passos) × 100. Também é registrado cada pré-requisito necessário e não declarado. Unidade: percentual. Escala: 0 a 100. |
| Fonte dos dados | `README.md` e `dev-docs/docs/introduction/development.mdx`; campo `engines` do `package.json` da raiz. |
| Procedimento de coleta | Execução em ambiente limpo, registrando cada ajuste necessário e o motivo. |
| Critério de interpretação | Confirma a hipótese se todos os passos forem reproduzidos quando as versões exigidas de ferramentas são usadas. Cada ajuste é algo que a documentação deixou de dizer. |
| Questão respondida | Q3.3 |
| Características desejáveis | Objetiva, porque a regra de "sem ajuste" é fixa e cada ajuste é registrado com o motivo. Válida para RQ-FLEX-08 e RQ-FLEX-10. |

### M3.3.3 — Implantação com Docker

| Campo | Descrição |
| :--- | :--- |
| Definição | Resultado da construção e da execução da imagem Docker da aplicação, a partir do `Dockerfile` da versão avaliada, sem passos além dos documentados. |
| Procedimento de cálculo | Verificações: (1) a imagem é construída sem erro; (2) o contêiner inicia; (3) a verificação de saúde (*healthcheck*) declarada no `Dockerfile` passa; (4) o editor abre no navegador e permite criar uma forma. Calcular (verificações que passam ÷ 4) × 100. Também é registrado o tempo de construção. Unidade: percentual. Escala: 0 a 100. |
| Fonte dos dados | `Dockerfile` e `docker-compose.yml` da raiz; instruções de Docker do guia de desenvolvimento. |
| Procedimento de coleta | Comandos `docker build` e `docker run` em ambiente limpo com Docker instalado, registrando a saída e a versão do Docker. |
| Critério de interpretação | Confirma a hipótese se o valor for 100%. Cada verificação que falha é um obstáculo para quem precisa implantar a aplicação em um servidor próprio. |
| Questão respondida | Q3.3 |
| Características desejáveis | Simples. Objetiva, porque cada verificação tem resultado binário. Fácil de coletar. Válida para RQ-FLEX-09. |

---

## Referências

- AULA 08 QSW1 GQM. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Páginas 33, 34 e 38.
- Especificação do trabalho final da disciplina de Qualidade de Software 1 (2026-2 Trabalho final completo v1). Página 1, premissa 2.
- ISO/IEC 25010:2023. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model*.
- Excalidraw. Repositório oficial, commit `e1b7aac` de 18/10/2026. Disponível em: https://github.com/excalidraw/excalidraw/tree/e1b7aacb356a492aa1e0fc6eb57b8896124027f0.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 19/10/2026 | Criação das questões, hipóteses e métricas do objetivo G3 | [Christopher Paraizo](https://github.com/wChrstphr) | |
