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
