---
sidebar_position: 4
title: Descrição e Arquitetura do Produto
description: Caracterização estruturada do Excalidraw, arquitetura em monorepo, diagrama de contexto, interfaces e implicações para a avaliação.
---

import Link from '@docusaurus/Link';

# Descrição estruturada e arquitetura do Excalidraw

## Introdução

Identificar o produto avaliado é uma das atividades da fase de estabelecer os requisitos da avaliação [[1, p. 4]](#ref-1). A descrição cobre o Excalidraw, sua organização em pacotes, suas interfaces externas e as restrições que limitam o que pode ser medido, para que o [escopo](./escopo-avaliacao.md) e os [requisitos](./requisitos-avaliacao.md) partam de uma visão concreta do produto.

## Metodologia

A descrição responde às perguntas de caracterização do produto apresentadas na aula, como as principais tarefas, os componentes que serão submetidos à avaliação e os requisitos para executá-lo [[1, p. 10]](#ref-1). Os dados técnicos foram conferidos no repositório oficial, no commit `e1b7aac` de 18/10/2026 [[2]](#ref-2), a mesma versão usada em toda a avaliação.

---

## 1. Caracterização do Produto

O **Excalidraw** é um editor de desenho e diagramação que roda no navegador, com traço que imita esboços feitos à mão. A mesma base de código entrega dois produtos:

1. **Aplicação web e PWA (*Progressive Web App*):** editor para esboços, diagramas e notas visuais, com colaboração em tempo real criptografada de ponta a ponta e funcionamento sem conexão.
2. **Biblioteca React (`@excalidraw/excalidraw`):** pacote publicado no npm que permite a terceiros incorporar o editor em suas próprias aplicações React.

<p className="tabela-titulo">Tabela 1: Caracterização do Excalidraw</p>

| Dimensão Técnica | Especificação no Projeto |
| :--- | :--- |
| **Nome do Produto** | Excalidraw |
| **Classificação de Software** | Aplicação web de página única (SPA) e PWA, e biblioteca de componentes React ([tipo de produto](./tipo-produto.md)) |
| **Linguagem Principal** | TypeScript |
| **Framework Base** | React |
| **Arquitetura do Repositório** | Monorepo com Yarn Workspaces (`excalidraw-app`, `packages/*` e `examples/*`) |
| **Licença** | MIT (código aberto, permissiva) |
| **Repositório Oficial** | [github.com/excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) |
| **Versão avaliada** | Commit `e1b7aac` de 18/10/2026, com a biblioteca na versão 0.18.0 ([escopo](./escopo-avaliacao.md)) |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>

"SPA" (aplicação de página única) e "PWA" descrevem a arquitetura da aplicação web: uma única página carregada no navegador, que atualiza a interface sem recarregar e, depois do primeiro acesso, funciona sem conexão. Não são categorias de tipo de software. A classificação do produto segundo Pressman e a IEEE 1062 está em [tipo de produto](./tipo-produto.md#2-classificação-segundo-pressman).

---

## 2. Estrutura de Módulos e Pacotes do Monorepo

O monorepo declara três grupos de workspaces: `excalidraw-app`, `packages/*` e `examples/*`. A Tabela 2 resume a responsabilidade de cada parte. Os pacotes de matemática e utilitários são pensados para uso fora do editor, e a [Fase 02](../fase-02/gqm-manutenibilidade.md#4-q12-reusabilidade) verifica se de fato não dependem de React nem do navegador.

<p className="tabela-titulo">Tabela 2: Módulos do monorepo e responsabilidades</p>

| Diretório/componente | Responsabilidade observável | Interfaces ou evidência |
| :--- | :--- | :--- |
| `excalidraw-app/` | Aplicação web: composição da interface, mecanismos de colaboração, armazenamento local, integrações e configuração de build. | `App.tsx`, `index.tsx`, `collab/`, `data/`, `vite.config.mts`. |
| `packages/excalidraw/` | Editor React reutilizável, componentes de UI, cena, ações, renderização e APIs de importação/exportação. | `index.tsx`, `components/`, `data/`, `scene/`, `renderer/` e `package.json`. |
| `packages/element/` | Operações e estruturas de elementos geométricos da cena. | `packages/element/src/` e seu manifesto. |
| `packages/math/`, `packages/common/`, `packages/utils/` | Rotinas de cálculo, tipos/utilitários e funcionalidades compartilhadas. | Diretórios e manifestos em `packages/`. |
| `packages/fractional-indexing/`, `packages/laser-pointer/` | Funcionalidades de apoio específicas, como ordenação e ponteiro. | Diretórios e manifestos em `packages/`. |
| `examples/` | Exemplos de integração e uso, úteis para testar reusabilidade. | Workspaces declarados no `package.json` raiz. |
| `excalidraw-app/collab/` | Coordenação da sessão colaborativa e comunicação em tempo real. | `Collab.tsx`, `Portal.tsx`, dependências de `socket.io-client`. |
| `excalidraw-app/data/` | Armazenamento local, persistência e comunicação com serviços remotos. | `LocalData.ts`, `firebase.ts`, `localStorage.ts`, `FileManager.ts`. |
| `.github/workflows/`, configurações e testes | CI, checagens, testes automatizados e ferramentas de análise de código. | `vitest.config.mts`, `tsconfig.json`, scripts `test:code`, `test:typecheck`, `test:app`. |

<p className="tabela-fonte">Fonte: [Davi Pierre](https://github.com/DaviPierre), 2026.</p>

---

## 3. Interfaces Externas e Integrações do Sistema

O Excalidraw roda quase todo no navegador e se comunica com poucos serviços externos:

1. **APIs do navegador (Canvas 2D e área de transferência):** a superfície de desenho usa a API Canvas 2D.
2. **Rough.js:** biblioteca externa que transforma formas geométricas (retângulos, arcos, elipses) em traços com pequenas variações, que imitam o desenho à mão.
3. **Persistência local (IndexedDB e LocalStorage):** salva o desenho continuamente, sem login e sem conexão.
4. **Servidor de colaboração (Socket.IO):** encaminha as mensagens criptografadas de ponta a ponta entre os participantes de uma sala, sem acesso ao conteúdo dos desenhos.
5. **Entrada por diferentes dispositivos:** mouse, trackpad com gesto de pinça, telas sensíveis ao toque e canetas com sensibilidade à pressão.

---

## 4. Diagrama de Contexto e Arquitetura

A Figura 1 mostra as fronteiras entre os pacotes do monorepo, os perfis de usuários e as interfaces com o navegador e os serviços de rede.

<p className="tabela-titulo">Figura 1: Diagrama de contexto e arquitetura do Excalidraw</p>

![Diagrama de contexto e arquitetura do Excalidraw](../images/arquitetura-excalidraw.png)

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026. Redesenhada no Excalidraw por [Christopher Paraizo](https://github.com/wChrstphr) ([arquivo editável](../images/arquitetura-excalidraw.excalidraw)).</p>

---

## 5. Dependências Tecnológicas e Restrições Operacionais

A arquitetura impõe restrições que a avaliação precisa considerar:

- **Desenho em Canvas:** como o desenho é feito em Canvas, e não em elementos HTML ou SVG, ferramentas de inspeção da página enxergam pouco dos elementos desenhados.
- **Dependência do Rough.js:** a aparência dos traços e parte do consumo de processamento dependem dessa biblioteca externa.
- **Criptografia na colaboração:** como o conteúdo é criptografado no cliente e o servidor só encaminha dados ilegíveis, a recuperação de falhas de sincronização precisa ser analisada no código do cliente.

---

## 6. Implicações Arquiteturais para a Avaliação de Qualidade

A Tabela 3 separa, para cada subcaracterística do [modelo de qualidade](./modelo-de-qualidade.md), o que é viável medir e o que fica fora do escopo. As métricas finais de cada subcaracterística estão nas páginas de [G1](../fase-02/gqm-manutenibilidade.md), [G2](../fase-02/gqm-confiabilidade.md) e [G3](../fase-02/gqm-flexibilidade.md) da Fase 02.

<p className="tabela-titulo">Tabela 3: Implicações da arquitetura para a avaliação</p>

| Subcaracterística | O que é viável medir (dentro do escopo) | O que fica fora do escopo |
| :--- | :--- | :--- |
| **Modularidade** | Dependências entre `excalidraw-app/` e os pacotes de `packages/`, acoplamento entre pacotes e ciclos de importação. | Código interno das bibliotecas de terceiros. |
| **Reusabilidade** | Isolamento dos pacotes publicados, ausência de importações da aplicação e exports públicos documentados. | Uso da biblioteca em aplicações de terceiros além dos exemplos do repositório. |
| **Analisabilidade** | Tamanho e complexidade do código, verificações de lint e tipagem e documentação técnica. | Percepção de legibilidade por desenvolvedores, que exigiria um estudo com pessoas. |
| **Modificabilidade** | Número de arquivos alterados por contribuição e arquivos extensos no código. | Custo real das alterações, em horas, para a equipe do projeto. |
| **Testabilidade** | Razão entre arquivos de teste e de produção, testes automatizados e sua execução na CI. | Testes manuais em dispositivos físicos variados. |
| **Ausência de falhas** | Verificações antes da integração (tipos, lint, testes e revisão) e registro e tratamento de defeitos no histórico público. | Taxa de falhas observada pelos usuários em produção, que exigiria telemetria privada. |
| **Disponibilidade** | Funcionamento sem conexão após o primeiro carregamento (Service Worker e manifesto PWA) e independência do editor local em relação a recursos remotos. | Disponibilidade dos servidores de excalidraw.com e indicadores de SLA. |
| **Tolerância a Falhas** | Tratamento de arquivos inválidos ou corrompidos e continuidade do editor local quando a rede ou a sessão colaborativa falham. | Falhas da infraestrutura de produção e do servidor de colaboração implantado. |
| **Recuperabilidade** | Restauração do último estado ao reabrir a aplicação, abertura de arquivos salvos e de versões anteriores, desfazer e refazer. | Recuperação de dados guardados nos servidores de produção. |
| **Adaptabilidade** | Navegadores e APIs declarados, integração da biblioteca em ambientes React e empacotadores e uso com toque e caneta. | Todas as combinações de navegadores e dispositivos. |
| **Escalabilidade** | Abertura, edição, salvamento e exportação de desenhos com número crescente de elementos, em ensaios locais. | Usuários simultâneos e latência dos serviços em produção. |
| **Instalabilidade** | Instalação, atualização e remoção da biblioteca pelo npm, build e implantação da aplicação, inclusive com Docker, e documentação dos pré-requisitos. | Ambientes e sistemas operacionais além dos usados nos ensaios. |
| **Substituibilidade** | Formatos de exportação, documentação do formato `.excalidraw` e conteúdo preservado ao exportar e reimportar. | Migração para todos os editores de diagramas concorrentes. |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>

As exclusões gerais e o que cada uma impede de concluir estão nas [exclusões do escopo](./escopo-avaliacao.md#4-o-que-está-fora-do-escopo-e-por-quê).

---

## 7. Rastreabilidade com os Requisitos da Avaliação

A arquitetura descrita aqui fundamenta os [requisitos de avaliação](./requisitos-avaliacao.md):

- [RQ-MAN-01 a RQ-MAN-03](./requisitos-avaliacao.md#2-requisitos-de-manutenibilidade) analisam as fronteiras entre `excalidraw-app/` e os pacotes da [seção 2](#2-estrutura-de-módulos-e-pacotes-do-monorepo).
- [RQ-CONF-03 a RQ-CONF-07](./requisitos-avaliacao.md#3-requisitos-de-confiabilidade) tratam do isolamento entre o editor local e as falhas de rede, do servidor de colaboração e dos arquivos abertos.
- [RQ-FLEX-07 a RQ-FLEX-10](./requisitos-avaliacao.md#4-requisitos-de-flexibilidade) tratam da instalação da biblioteca no npm e da implantação da aplicação, inclusive com Docker.

---

## Referências

> <Link id="ref-1">1.</Link> RAMOS, Cristiane Soares. **AULA A07 QSW1 PROC AVAL PRODUTO**. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Páginas 4 e 10. Disponível no Moodle da disciplina.
>
> <Link id="ref-2">2.</Link> EXCALIDRAW. Repositório oficial, commit `e1b7aac` de 18/10/2026. Disponível em: [https://github.com/excalidraw/excalidraw/tree/e1b7aacb356a492aa1e0fc6eb57b8896124027f0](https://github.com/excalidraw/excalidraw/tree/e1b7aacb356a492aa1e0fc6eb57b8896124027f0). Acesso em: 10 nov. 2026.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 18/10/2026 | Criação da descrição estruturada do produto, mapeamento de módulos, diagrama de contexto e análise de implicações para avaliação | [Gabriel Monteiro](https://github.com/GabrielSMonteiro) | [Maria Eduarda](https://github.com/eduarda-ogomes) |
| 1.1 | 20/10/2026 | Diagrama de contexto e arquitetura redesenhado no Excalidraw e publicado em PNG, com o arquivo editável | [Christopher Paraizo](https://github.com/wChrstphr) | |
| 1.2 | 10/11/2026 | Introdução e Metodologia, versão avaliada corrigida para o commit `e1b7aac` (biblioteca 0.18.0), pacotes e interfaces conferidos no repositório, linhas de Modificabilidade e Substituibilidade na tabela de implicações, tabela de módulos trazida do tipo de produto, subcaracterística Ausência de falhas adotada, tabelas e figura com título e fonte, requisitos com links, referências numeradas e retirada da citação ao critério da disciplina | [Christopher Paraizo](https://github.com/wChrstphr) | [Gabriel Monteiro](https://github.com/GabrielSMonteiro) |
| 1.3 | 18/11/2026 | Revisão de coerência, cross-links e redação: SPA e PWA explicados como arquitetura abaixo da tabela de caracterização, coluna de decisão metodológica e exemplos sem fonte retirados das implicações, Adaptabilidade e Escalabilidade separadas, introdução com o objetivo direto | [Christopher Paraizo](https://github.com/wChrstphr) | |
