---
sidebar_position: 1
title: Introdução
description: Contexto do projeto de avaliação de qualidade do Excalidraw — Grupo Karen Jones, FCTE/UnB
---

# Introdução

Este projeto é desenvolvido no âmbito da disciplina de **Qualidade de Software 1** da **FCTE — Universidade de Brasília (UnB)**, pelo **Grupo Karen Jones** no segundo semestre de 2026.

O objetivo é conduzir uma avaliação de qualidade do software open source [Excalidraw](https://excalidraw.com/), usando como referência as normas da família **ISO/IEC 25000 (SQuaRE)**. Não se trata de um uso superficial da norma: a ideia é percorrer o processo de avaliação da ISO/IEC 25040 de verdade, desde a definição dos requisitos até a execução e interpretação dos resultados.

---

## O que é o Excalidraw

O Excalidraw é uma ferramenta de quadro branco virtual voltada para diagramação rápida e colaboração. Ele roda no navegador, tem suporte a edição em tempo real entre múltiplos usuários e gera desenhos num estilo de esboço à mão — o que o diferencia de ferramentas como draw.io ou Miro.

O repositório é público, a licença é MIT e o projeto é mantido por uma comunidade ativa no GitHub. Isso nos deu acesso a tudo o que precisamos para fazer uma avaliação baseada no código e nos artefatos reais do projeto.

- **Repositório:** [github.com/excalidraw/excalidraw](https://github.com/excalidraw/excalidraw)
- **Tecnologias principais:** TypeScript e React
- **Estrutura:** monorepo com aplicação web (`excalidraw-app/`) e biblioteca separada (`packages/excalidraw/`)

---

## Por que escolhemos o Excalidraw

Três razões principais guiaram a escolha:

- **Código acessível e bem documentado:** o repositório público, com histórico de commits, issues e pull requests, nos permite ir além da superfície e olhar para o que realmente está acontecendo no desenvolvimento.
- **Diversidade de contextos de uso:** o Excalidraw é ao mesmo tempo uma aplicação web para usuários finais e uma biblioteca npm para desenvolvedores que querem embedar o editor em outras aplicações. Isso cria perspectivas de avaliação bastante diferentes.
- **Conexão com a disciplina:** as características que escolhemos avaliar — Manutenabilidade, Confiabilidade e Portabilidade — aparecem de forma natural no projeto e nos permitem exercitar os conceitos da norma com situações reais.

---

## Características avaliadas

Com base no que o Excalidraw nos oferece para examinar e nas necessidades dos grupos de interessados que mapeamos, escolhemos três características da **ISO/IEC 25010:2023**:

| Característica | O que estamos investigando |
| :--- | :--- |
| **Manutenabilidade** | A organização do código, a clareza dos módulos, a facilidade de fazer mudanças sem introduzir problemas e a cobertura de testes. |
| **Confiabilidade** | O comportamento da aplicação em situações de falha ou perda de conexão, o salvamento automático e a maturidade do processo de desenvolvimento. |
| **Portabilidade** | O funcionamento em diferentes navegadores e dispositivos, a facilidade de instalar a biblioteca e as opções de exportação dos dados. |

---

## Como o projeto está estruturado

O trabalho segue as quatro fases do processo de avaliação definido pela ISO/IEC 25040:

- **Fase 01 — Estabelecer requisitos de avaliação:** definir o propósito, delimitar o escopo, mapear os interessados e escolher o modelo de qualidade. É o que estamos fazendo agora.
- **Fase 02 — Especificar a avaliação:** definir as métricas com base na ISO/IEC 25023 e os critérios que vamos usar para julgar os resultados.
- **Fase 03 — Projetar a avaliação:** decidir o método de coleta, as ferramentas, as responsabilidades e o cronograma de execução.
- **Fase 04 — Executar a avaliação:** coletar os dados, compará-los com os critérios definidos, interpretar os resultados e propor melhorias.

---

## Integrantes (Grupo Karen Jones)

| Nome | GitHub |
| :--- | :--- |
| Christopher | [@wChrstphr](https://github.com/wChrstphr) |
| Davi Pierre | [@DaviPierre](https://github.com/DaviPierre) |
| Gabriel Monteiro | [@GabrielSMonteiro](https://github.com/GabrielSMonteiro) |
| Letícia de Carvalho | [@LeticiaSantosss](https://github.com/LeticiaSantosss) |
| Luiz Henrique Soares | [@luizh-gsoares](https://github.com/luizh-gsoares) |
| Maria Eduarda | [@eduarda-ogomes](https://github.com/eduarda-ogomes) |
