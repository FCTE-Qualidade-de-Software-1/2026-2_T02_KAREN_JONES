---
sidebar_position: 3
title: Tipo de Produto e Arquitetura do Excalidraw
description: Classificação do produto e descrição estruturada da arquitetura, interfaces, dependências e restrições do Excalidraw
---

# Tipo de produto e descrição estruturada do Excalidraw

## 1. Identificação e versão analisada

| Campo | Identificação |
| :--- | :--- |
| Produto | **Excalidraw** — editor visual de quadro branco em estilo de esboço, com uma aplicação web e uma biblioteca React reutilizável |
| Repositório de referência | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) |
| Licença | MIT, conforme `LICENSE` do projeto oficial |
| Versão de referência para a análise estrutural | Commit [`e1b7aacb356a492aa1e0fc6eb57b8896124027f0`](https://github.com/excalidraw/excalidraw/tree/e1b7aacb356a492aa1e0fc6eb57b8896124027f0) da branch `master`, datado de **18/10/2026** |
| Aplicação | [`excalidraw-app/`](https://github.com/excalidraw/excalidraw/tree/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/excalidraw-app) |
| Biblioteca | [`packages/excalidraw/`](https://github.com/excalidraw/excalidraw/tree/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/packages/excalidraw) — pacote npm `@excalidraw/excalidraw` |
| Stack principal | TypeScript, React, Vite, Yarn Workspaces e Vitest (conforme os manifestos e arquivos de configuração do commit analisado) |

O **commit**, e não o nome variável da branch nem a versão isolada de um pacote npm, constitui a linha de base reprodutível do código-fonte. A documentação abaixo descreve o conteúdo inspecionado nesse commit; não representa medição de qualidade concluída nem auditoria da infraestrutura de produção.

## 2. Classificação segundo Pressman

O Excalidraw enquadra-se principalmente como **aplicação Web (WebApp)**: é oferecido ao usuário final por interface gráfica em navegador, suporta criação e edição de desenhos e pode prestar serviços colaborativos. Pela finalidade, também é **software de aplicação** voltado à produção de diagramas, esboços e conteúdo visual. Essas categorias descrevem dimensões diferentes e não precisam ser tratadas como mutuamente exclusivas.

A presença do pacote `@excalidraw/excalidraw` acrescenta a perspectiva de **componente de software reutilizável**, incorporável a outras aplicações React. Não se afirma que o projeto seja software embarcado, de tempo real, de sistema operacional ou que todas as funcionalidades da aplicação estejam presentes na biblioteca. A aplicação hospedada inclui capacidades de persistência e colaboração que não se confundem com as funcionalidades básicas do componente npm.

## 3. Classificação segundo a IEEE 1062: COTS, MOTS e FD

A classificação depende do **objeto e da modalidade de aquisição/uso**. Os termos são aplicados aqui como categorias de análise, sem sugerir que uma licença open source determine, por si só, uma classificação de aquisição:

| Modalidade | Aplicação ao caso | Justificativa |
| :--- | :--- | :--- |
| **COTS** (*Commercial Off-The-Shelf*) | **Aproximação funcional** para adoção da aplicação e consumo do pacote distribuído sem alteração do código-fonte | O produto está disponível, reutilizável e pode ser empregado como fornecido. O termo **commercial** tem conotação de aquisição: por ser software aberto, não cabe declarar enquadramento contratual formal sem examinar o contexto de aquisição. |
| **MOTS** (*Modified Off-The-Shelf*) | **Possibilidade condicionada** a modificações do código-fonte do Excalidraw para atender necessidades próprias | Integrar a API pública ou configurar a biblioteca **não implica**, por si só, modificar o produto. Há MOTS quando a organização altera o software adquirido/adotado. |
| **FD** (*Fully Developed*) | **Não descreve a adoção do produto preexistente pela equipe** | Só seria aplicável a uma solução integralmente desenvolvida para o demandante, ou a um novo produto construído desde o início. |

**Conclusão contextual:** para esta avaliação, o Excalidraw é um **produto de prateleira preexistente, open source, com aplicação e biblioteca**. Considera-se o uso *as-is* próximo ao cenário COTS; alterações no código poderiam configurar MOTS. A ambiguidade entre aplicação completa e componente reutilizável está explicitada, sem atribuir a ambos os mesmos requisitos de integração e operação.

## 4. Roteiro de caracterização do produto

| Pergunta da aula | Resposta fundamentada | Evidência e ressalva |
| :--- | :--- | :--- |
| **Que funções executa?** | Criação/edição de cenas em canvas; inserção de formas, texto, desenho livre, setas e imagens; desfazer/refazer; biblioteca de elementos; importação/exportação; na aplicação web, colaboração e salvamento local. | [README](https://github.com/excalidraw/excalidraw/blob/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/README.md) distingue recursos do editor e recursos adicionais de excalidraw.com. |
| **Quais janelas ou interfaces?** | Editor visual no navegador, barras e menus, diálogos de importação/exportação e integração por componente React. | [`packages/excalidraw/components/`](https://github.com/excalidraw/excalidraw/tree/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/packages/excalidraw/components). Não se estabelece contagem fixa de janelas, que depende da versão e do estado da interface. |
| **Quem usa?** | Pessoas criando desenhos, estudantes, docentes, profissionais de produto, equipes colaborativas, desenvolvedores integradores e mantenedores/contribuidores. | Perspectivas detalhadas em [Partes interessadas](./interessados.md). |
| **Qual conhecimento é exigido?** | Uso básico de interface gráfica para o editor; conhecimento de React/JavaScript e gestão de dependências para integrar a biblioteca; conhecimento de Node/Yarn/TypeScript para desenvolver o monorepo. | [`packages/excalidraw/README.md`](https://github.com/excalidraw/excalidraw/blob/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/packages/excalidraw/README.md). |
| **Qual massa de dados é manipulada?** | Cenas com elementos, estado da aplicação e recursos binários (p.ex., imagens). Os desenhos podem ser serializados em `.excalidraw` (JSON) e exportados em formatos de imagem. | [`packages/excalidraw/data/json.ts`](https://github.com/excalidraw/excalidraw/blob/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/packages/excalidraw/data/json.ts); **nenhuma carga representativa ou volume típico foi medido nesta fase**. |
| **Requisitos de hardware?** | Dispositivo com navegador que suporte as APIs Web requeridas; tela e entradas apropriadas para manipular canvas. **Não foi identificada especificação oficial de RAM/CPU mínima que possa ser afirmada para todos os cenários**. | Compatibilidade e desempenho real precisam de ambiente e cargas de teste definidos nas próximas fases. |
| **Requisitos de software?** | Para usuário final, navegador compatível; para integração, React/React DOM e dependências do pacote; para desenvolvimento do repositório, Node.js **≥ 18** e **Yarn 1.22.22** declarados no manifesto raiz. | [`package.json` do monorepo](https://github.com/excalidraw/excalidraw/blob/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/package.json), [`excalidraw-app/package.json`](https://github.com/excalidraw/excalidraw/blob/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/excalidraw-app/package.json) e [manifesto da biblioteca](https://github.com/excalidraw/excalidraw/blob/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/packages/excalidraw/package.json). |

## 5. Estrutura, módulos e responsabilidades

O projeto é um **monorepo com workspaces** (`excalidraw-app`, `packages/*`, `examples/*`). Os pacotes citados são identificáveis no commit de referência, mas isso **não significa** que todos sejam publicados separadamente ou tenham API estável.

| Diretório/componente | Responsabilidade observável | Interfaces ou evidência |
| :--- | :--- | :--- |
| `excalidraw-app/` | Aplicação web: composição da interface, mecanismos de colaboração, armazenamento local, integrações e configuração de build. | `App.tsx`, `index.tsx`, `collab/`, `data/`, `vite.config.mts`. |
| `packages/excalidraw/` | Editor React reutilizável, componentes de UI, cena, ações, renderização e APIs de importação/exportação. | `index.tsx`, `components/`, `data/`, `scene/`, `renderer/` e `package.json`. |
| `packages/element/` | Operações e estruturas de elementos geométricos da cena. | `packages/element/src/` e seu manifesto. |
| `packages/math/`, `packages/common/`, `packages/utils/` | Rotinas de cálculo, tipos/utilitários e funcionalidades compartilhadas. | Diretórios e manifestos em `packages/`. |
| `packages/fractional-indexing/`, `packages/laser-pointer/` | Funcionalidades de apoio específicas, como ordenação e ponteiro. | Diretórios e manifestos em `packages/`. |
| `examples/` | Exemplos de integração e uso, úteis para testar reusabilidade. | Workspaces declarados no `package.json` raiz. |
| `excalidraw-app/collab/` | Coordenação da sessão colaborativa e comunicação em tempo real. | `Collab.tsx`, `Portal.tsx`; dependências de `socket.io-client`. |
| `excalidraw-app/data/` | Armazenamento local, persistência e comunicação com serviços remotos. | `LocalData.ts`, `firebase.ts`, `localStorage.ts`, `FileManager.ts`. |
| `.github/workflows/`, configurações e testes | CI, checagens, testes automatizados e ferramentas de análise de código. | `vitest.config.mts`, `tsconfig.json`, scripts `test:code`, `test:typecheck`, `test:app`. |

### 5.1 Diagrama de contexto e arquitetura

![Diagrama de arquitetura do Excalidraw: o navegador acessa a aplicação web, que utiliza a biblioteca React de editor; o editor utiliza pacotes comuns, de elementos e matemática; a aplicação lida separadamente com armazenamento local e serviços de colaboração externos.](../images/arquitetura-excalidraw.png)

*Figura 1 — Visão lógica simplificada dos componentes no commit de referência. As setas representam dependências ou interações conceituais, não o mapa completo de importações de código.*

A biblioteca permite incorporar o editor em **outra aplicação React**, que deve prover contexto de execução e interface conforme a API do pacote. A colaboração e determinados fluxos de persistência pertencem à **aplicação** e usam serviços externos; não devem ser atribuídos automaticamente à distribuição npm.

### 5.2 Interfaces e dependências

- **Interface humana:** canvas, ferramentas, menus, diálogos e controles para mouse, toque e teclado conforme o ambiente.
- **Interface de integração:** o pacote npm expõe o componente React `Excalidraw`, tipos e utilitários; a integração exige o CSS do pacote e um contêiner com altura definida ([guia oficial](https://github.com/excalidraw/excalidraw/blob/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/packages/excalidraw/README.md)).
- **Persistência local:** [`LocalData.ts`](https://github.com/excalidraw/excalidraw/blob/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/excalidraw-app/data/LocalData.ts) usa armazenamento do navegador; políticas de quota, privacidade e comportamento offline dependem do navegador e do contexto de execução.
- **Comunicação colaborativa:** [`Collab.tsx`](https://github.com/excalidraw/excalidraw/blob/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/excalidraw-app/collab/Collab.tsx) coordena a colaboração; [`firebase.ts`](https://github.com/excalidraw/excalidraw/blob/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/excalidraw-app/data/firebase.ts) implementa interações de armazenamento remoto. Serviços externos não estão integralmente cobertos pelo código do cliente inspecionado.
- **Empacotamento e ambiente:** o monorepo utiliza Yarn Workspaces; o pacote npm informa dependências React por `peerDependencies`; a aplicação usa Vite, e a distribuição web usa as APIs suportadas pelo navegador.

## 6. Restrições e implicações para a avaliação

| Aspecto | O que é possível avaliar com as evidências disponíveis | Limite e tratamento |
| :--- | :--- | :--- |
| **Manutenibilidade** | Modularidade, organização de workspaces, dependências declaradas, regras de lint/tipagem, arquivos de testes e histórico Git. | Isso não prova, isoladamente, baixo esforço real para manutenção nem cobertura funcional efetiva. |
| **Confiabilidade** | Implementações de recuperação, persistência, gerenciamento de erros, PWA e estratégias de colaboração descritas no código. | Inspeção estática **não comprova** disponibilidade de produção, ausência de perda de dados ou tolerância real a falhas. Testes controlados exigem protocolo e ambiente próprios. |
| **Flexibilidade** | Compatibilidade declarada, API pública, instruções de instalação, workspaces e mecanismos de importação/exportação. | Declarações de suporte não equivalem a testes em todos os browsers, hardwares e cargas. Escalabilidade requer cenários e medições reproduzíveis. |

A seleção dos objetos, do nível de profundidade e das exclusões está formalizada em [Escopo, profundidade e objetos de avaliação](./escopo-avaliacao.md); os requisitos rastreáveis estão em [Requisitos de avaliação](./requisitos-avaliacao.md). Nenhuma dessas observações deve ser apresentada como **resultado medido** antes de especificar e executar as métricas nas Fases 2 a 4.

## 7. Fontes e rastreabilidade

Fontes oficiais, todas referidas ao commit `e1b7aacb356a492aa1e0fc6eb57b8896124027f0`:

1. [README e documentação do projeto](https://github.com/excalidraw/excalidraw/blob/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/README.md).
2. [Manifesto raiz e workspaces](https://github.com/excalidraw/excalidraw/blob/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/package.json).
3. [Manifesto e API da biblioteca](https://github.com/excalidraw/excalidraw/blob/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/packages/excalidraw/package.json).
4. [Aplicação, colaboração e dados](https://github.com/excalidraw/excalidraw/tree/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/excalidraw-app).
5. AULA A07 QSW1 PROC AVAL PRODUTO.pdf, páginas 10 a 13 (critérios da disciplina sobre tipo e descrição do produto); **documento interno da disciplina, conforme a Issue #10**.

## Histórico de versões

| Versão | Data | Descrição | Autor | Revisão |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 18/10/2026 | Caracterização do produto, classificação Pressman/IEEE 1062 e arquitetura de referência | [Davi Pierre](https://github.com/DaviPierre) | |
| 1.1 | 20/10/2026 | Diagrama de arquitetura redesenhado no Excalidraw e publicado em PNG ([arquivo editável](../images/arquitetura-excalidraw.excalidraw)) | [Christopher Paraizo](https://github.com/wChrstphr) | |
