---
sidebar_position: 1
title: Introdução
description: "Contexto do projeto de avaliação de qualidade do Excalidraw: Grupo Karen Jones, FCTE/UnB"
---

# Introdução

Este projeto é desenvolvido no âmbito da disciplina de **Qualidade de Software 1** da **FCTE, Universidade de Brasília (UnB)**, pelo **Grupo Karen Jones** no segundo semestre de 2026.

O objetivo é conduzir uma avaliação de qualidade do software open source [Excalidraw](https://excalidraw.com/), usando como referência as normas da família **ISO/IEC 25000 (SQuaRE)**. A equipe percorre o processo da ISO/IEC 25040, dos requisitos à interpretação dos resultados.

---

## O que é o Excalidraw

O Excalidraw é uma ferramenta de quadro branco virtual voltada para diagramação rápida e colaboração. Ele roda no navegador, tem suporte a edição em tempo real entre múltiplos usuários e gera desenhos no estilo de esboço à mão.

O repositório é público, a licença é MIT e o projeto é mantido por uma comunidade ativa no GitHub. Isso nos deu acesso a tudo o que precisamos para fazer uma avaliação baseada no código e nos artefatos reais do projeto.

- **Repositório:** [github.com/excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)
- **Tecnologias principais:** TypeScript e React
- **Estrutura:** monorepo com aplicação web (`excalidraw-app/`) e biblioteca separada (`packages/excalidraw/`)

---

## Por que escolhemos o Excalidraw

Duas razões principais guiaram a escolha:

- **Código acessível e bem documentado:** o repositório público, com histórico de commits, issues e pull requests, nos permite ir além da superfície e olhar para o que realmente está acontecendo no desenvolvimento.
- **Diversidade de contextos de uso:** o Excalidraw é ao mesmo tempo uma aplicação web para usuários finais e uma biblioteca npm para desenvolvedores que querem embedar o editor em outras aplicações. Isso cria perspectivas de avaliação bastante diferentes.

---

## Características avaliadas

Com base no que o Excalidraw nos oferece para examinar e nas necessidades dos grupos de interessados que mapeamos, escolhemos três características da **ISO/IEC 25010:2023**:

<p className="tabela-titulo">Tabela 1: Características avaliadas</p>

| Característica | O que estamos investigando |
| :--- | :--- |
| **Manutenibilidade** | A organização do código, a clareza dos módulos, a facilidade de fazer mudanças sem introduzir problemas e a cobertura de testes. |
| **Confiabilidade** | O comportamento da aplicação em situações de falha ou perda de conexão, o salvamento automático e as verificações do processo de desenvolvimento que evitam falhas. |
| **Flexibilidade** | O funcionamento em diferentes navegadores e dispositivos, a facilidade de instalar a biblioteca, as opções de exportação dos dados e a Escalabilidade com desenhos grandes. |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>

---

## Como o projeto está estruturado

O trabalho segue as quatro fases do processo de avaliação definido pela norma ISO/IEC 25040:

- **Fase 01: [Estabelecer requisitos de avaliação](./fase-01/visao-geral.md):** definir o propósito, delimitar o escopo, mapear os interessados e escolher o modelo de qualidade. Concluída.
- **Fase 02: [Especificar a avaliação](./fase-02/visao-geral.md):** definir os objetivos de medição com o método GQM, as métricas e os critérios para pontuar e julgar os resultados. Concluída.
- **Fase 03: [Projetar a avaliação](./fase-03/visao-geral.md):** planejar o método de avaliação, as instruções para os avaliadores, os recursos necessários, a massa de dados e o cronograma. Concluída.
- **Fase 04: [Executar a avaliação](./fase-04/visao-geral.md):** coletar os dados, compará-los com os critérios definidos, interpretar os resultados e propor melhorias. Concluída.

A divisão em subgrupos e a governança do trabalho no GitHub estão descritas na [metodologia da equipe](./gestao/metodologia-equipe.md). Para consultar rapidamente a hierarquia completa entre objetivos, questões, hipóteses e métricas, acesse o [Plano GQM](./fase-02/plano-gqm.md).

---

## Integrantes (Grupo Karen Jones)

<p className="tabela-titulo">Tabela 2: Integrantes da equipe Karen Jones</p>

| Nome | GitHub |
| :--- | :--- |
| Christopher Paraizo | [@wChrstphr](https://github.com/wChrstphr) |
| Davi Pierre | [@DaviPierre](https://github.com/DaviPierre) |
| Gabriel Monteiro | [@GabrielSMonteiro](https://github.com/GabrielSMonteiro) |
| Letícia de Carvalho | [@LeticiaSantosss](https://github.com/LeticiaSantosss) |
| Luiz Henrique Soares | [@luizh-gsoares](https://github.com/luizh-gsoares) |
| Maria Eduarda | [@eduarda-ogomes](https://github.com/eduarda-ogomes) |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>

---

## Histórico de Versões

<p className="tabela-titulo">Tabela 3: Histórico de versões do documento</p>

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 18/10/2026 | Estruturação inicial da página de introdução do projeto | [Gabriel Monteiro](https://github.com/GabrielSMonteiro) | [Christopher Paraizo](https://github.com/wChrstphr) |
| 1.1 | 19/10/2026 | Atualização da estrutura com a indicação da Fase 02 | [Luiz Henrique Soares](https://github.com/luizh-gsoares) | [Christopher Paraizo](https://github.com/wChrstphr) |
| 1.2 | 10/11/2026 | Revisão e alinhamento da terminologia da ISO/IEC 25010:2023 | [Christopher Paraizo](https://github.com/wChrstphr) | [Gabriel Monteiro](https://github.com/GabrielSMonteiro) |
| 1.3 | 14/11/2026 | Indicação da Fase 02 como concluída e da Fase 03 como fase atual com link para visão geral | [Gabriel Monteiro](https://github.com/GabrielSMonteiro) | [Christopher Paraizo](https://github.com/wChrstphr) |
| 1.4 | 17/11/2026 | Indicação de todas as quatro fases como concluídas com links para as respectivas visões gerais | [Maria Eduarda](https://github.com/eduarda-ogomes) | |
| 1.5 | 18/11/2026 | Revisão de coerência e cross-links: Escalabilidade em Flexibilidade e link à metodologia da equipe | [Christopher Paraizo](https://github.com/wChrstphr) | |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>
