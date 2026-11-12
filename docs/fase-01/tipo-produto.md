---
sidebar_position: 3
title: Tipo de Produto
description: Identificação da versão avaliada e classificação do Excalidraw segundo Pressman e a IEEE 1062, com o roteiro de caracterização da aula
---

import Link from '@docusaurus/Link';

# Tipo de produto

## Introdução

Identificar o tipo de produto é uma das três atividades da fase de estabelecer os requisitos da avaliação [[1, p. 4]](#ref-1). Esta página identifica a versão do Excalidraw avaliada e classifica o produto pelas duas classificações apresentadas na aula, a de Pressman e a da IEEE 1062 [[1, p. 11]](#ref-1). A organização interna do produto, as interfaces e o diagrama de arquitetura estão em [Descrição e arquitetura do produto](./descricao-produto.md).

## Metodologia

A classificação compara o Excalidraw com as categorias das tabelas da aula [[1, p. 12 e 13]](#ref-1), e o roteiro de caracterização responde às perguntas de descrição geral do produto [[1, p. 10]](#ref-1). Cada resposta foi conferida no repositório oficial, no commit `e1b7aac` de 18/10/2026 [[2]](#ref-2). O commit, e não o nome da branch nem a versão de um pacote npm, é a linha de base reprodutível da avaliação.

---

## 1. Identificação e versão analisada

<p className="tabela-titulo">Tabela 1: Identificação do produto</p>

| Campo | Identificação |
| :--- | :--- |
| Produto | **Excalidraw**, editor visual de quadro branco em estilo de esboço, com uma aplicação web e uma biblioteca React reutilizável |
| Repositório de referência | [excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) |
| Licença | MIT, conforme `LICENSE` do projeto oficial |
| Versão de referência para a análise estrutural | Commit [`e1b7aacb356a492aa1e0fc6eb57b8896124027f0`](https://github.com/excalidraw/excalidraw/tree/e1b7aacb356a492aa1e0fc6eb57b8896124027f0) da branch `master`, datado de **18/10/2026** |
| Aplicação | [`excalidraw-app/`](https://github.com/excalidraw/excalidraw/tree/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/excalidraw-app) |
| Biblioteca | [`packages/excalidraw/`](https://github.com/excalidraw/excalidraw/tree/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/packages/excalidraw), pacote npm `@excalidraw/excalidraw` |
| Stack principal | TypeScript, React, Vite, Yarn Workspaces e Vitest (conforme os manifestos e arquivos de configuração do commit analisado) |

<p className="tabela-fonte">Fonte: [Davi Pierre](https://github.com/DaviPierre), 2026.</p>

## 2. Classificação segundo Pressman

A tabela de Pressman apresentada na aula não traz uma categoria própria para aplicações web [[1, p. 12]](#ref-1). Entre as categorias da tabela, o Excalidraw se aproxima de **software de computador pessoal**, que reúne editores de texto, planilhas e outras ferramentas de produção usadas pelo usuário final, embora rode no navegador. Não se enquadra como software básico, de tempo real, comercial, científico, embarcado ou de inteligência artificial.

A biblioteca `@excalidraw/excalidraw` acrescenta outra perspectiva: a de **componente reutilizável**, incorporado a outras aplicações React. A colaboração e parte da persistência pertencem à aplicação web e não ao pacote npm ([descrição do produto](./descricao-produto.md#2-estrutura-de-módulos-e-pacotes-do-monorepo)).

## 3. Classificação segundo a IEEE 1062: COTS, MOTS e FD

A classificação depende de como o produto é adquirido e usado [[1, p. 13]](#ref-1). Os termos são aplicados como categorias de análise, sem supor que a licença aberta determine sozinha a classificação.

<p className="tabela-titulo">Tabela 2: Classificação segundo a IEEE 1062</p>

| Modalidade | Aplicação ao caso | Justificativa |
| :--- | :--- | :--- |
| **COTS** (*Commercial Off-The-Shelf*) | **Aproximação funcional** para adoção da aplicação e consumo do pacote distribuído sem alteração do código-fonte | O produto está disponível, reutilizável e pode ser empregado como fornecido. O termo **commercial** tem conotação de aquisição: por ser software aberto, não cabe declarar enquadramento contratual formal sem examinar o contexto de aquisição. |
| **MOTS** (*Modified Off-The-Shelf*) | **Possibilidade condicionada** a modificações do código-fonte do Excalidraw para atender necessidades próprias | Integrar a API pública ou configurar a biblioteca **não implica**, por si só, modificar o produto. Há MOTS quando a organização altera o software adquirido/adotado. |
| **FD** (*Fully Developed*) | **Não descreve a adoção do produto preexistente pela equipe** | Só seria aplicável a uma solução integralmente desenvolvida para o demandante, ou a um novo produto construído desde o início. |

<p className="tabela-fonte">Fonte: adaptada de Ramos [[1, p. 13]](#ref-1), com a aplicação ao caso por [Davi Pierre](https://github.com/DaviPierre), 2026.</p>

**Conclusão:** para esta avaliação, o Excalidraw é um produto preexistente de código aberto, com aplicação e biblioteca. O uso sem alterações se aproxima do cenário COTS, e alterações no código configurariam MOTS.

## 4. Roteiro de caracterização do produto

<p className="tabela-titulo">Tabela 3: Roteiro de caracterização do produto</p>

| Pergunta da aula | Resposta fundamentada | Evidência e ressalva |
| :--- | :--- | :--- |
| **Que funções executa?** | Criação/edição de cenas em canvas, inserção de formas, texto, desenho livre, setas e imagens, desfazer/refazer, biblioteca de elementos, importação/exportação, na aplicação web, colaboração e salvamento local. | [README](https://github.com/excalidraw/excalidraw/blob/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/README.md) distingue recursos do editor e recursos adicionais de excalidraw.com. |
| **Quais janelas ou interfaces?** | Editor visual no navegador, barras e menus, diálogos de importação/exportação e integração por componente React. | [`packages/excalidraw/components/`](https://github.com/excalidraw/excalidraw/tree/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/packages/excalidraw/components). Não se estabelece contagem fixa de janelas, que depende da versão e do estado da interface. |
| **Quem usa?** | Pessoas criando desenhos, estudantes, docentes, profissionais de produto, equipes colaborativas, desenvolvedores integradores e mantenedores/contribuidores. | Perspectivas detalhadas em [Partes interessadas](./interessados.md). |
| **Qual conhecimento é exigido?** | Uso básico de interface gráfica para o editor, conhecimento de React/JavaScript e gestão de dependências para integrar a biblioteca, conhecimento de Node/Yarn/TypeScript para desenvolver o monorepo. | [`packages/excalidraw/README.md`](https://github.com/excalidraw/excalidraw/blob/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/packages/excalidraw/README.md). |
| **Qual massa de dados é manipulada?** | Cenas com elementos, estado da aplicação e recursos binários (p.ex., imagens). Os desenhos podem ser serializados em `.excalidraw` (JSON) e exportados em formatos de imagem. | [`packages/excalidraw/data/json.ts`](https://github.com/excalidraw/excalidraw/blob/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/packages/excalidraw/data/json.ts), **nenhuma carga representativa ou volume típico foi medido nesta fase**. |
| **Requisitos de hardware?** | Dispositivo com navegador que suporte as APIs Web requeridas, tela e entradas apropriadas para manipular canvas. **Não foi identificada especificação oficial de RAM/CPU mínima que possa ser afirmada para todos os cenários**. | Compatibilidade e desempenho real precisam de ambiente e cargas de teste definidos nas próximas fases. |
| **Requisitos de software?** | Para usuário final, navegador compatível, para integração, React/React DOM e dependências do pacote, para desenvolvimento do repositório, Node.js **≥ 18** e **Yarn 1.22.22** declarados no manifesto raiz. | [`package.json` do monorepo](https://github.com/excalidraw/excalidraw/blob/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/package.json), [`excalidraw-app/package.json`](https://github.com/excalidraw/excalidraw/blob/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/excalidraw-app/package.json) e [manifesto da biblioteca](https://github.com/excalidraw/excalidraw/blob/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/packages/excalidraw/package.json). |

<p className="tabela-fonte">Fonte: [Davi Pierre](https://github.com/DaviPierre), 2026, a partir das perguntas de Ramos [[1, p. 10]](#ref-1).</p>

Nenhuma dessas respostas é resultado medido. A seleção dos objetos e a profundidade da avaliação estão em [Escopo e objetos de avaliação](./escopo-avaliacao.md), e os requisitos, em [Requisitos de avaliação](./requisitos-avaliacao.md).

---

## Referências

> <Link id="ref-1">1.</Link> RAMOS, Cristiane Soares. **AULA A07 QSW1 PROC AVAL PRODUTO**. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Páginas 4 e 10 a 13. Disponível no Moodle da disciplina.
>
> <Link id="ref-2">2.</Link> EXCALIDRAW. Repositório oficial, commit `e1b7aac` de 18/10/2026. Disponível em: [https://github.com/excalidraw/excalidraw/tree/e1b7aacb356a492aa1e0fc6eb57b8896124027f0](https://github.com/excalidraw/excalidraw/tree/e1b7aacb356a492aa1e0fc6eb57b8896124027f0). Acesso em: 10 nov. 2026.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 18/10/2026 | Caracterização do produto, classificação Pressman/IEEE 1062 e arquitetura de referência | [Davi Pierre](https://github.com/DaviPierre) | |
| 1.1 | 20/10/2026 | Diagrama de arquitetura redesenhado no Excalidraw e publicado em PNG ([arquivo editável](../images/arquitetura-excalidraw.excalidraw)) | [Christopher Paraizo](https://github.com/wChrstphr) | |
| 1.2 | 10/11/2026 | Introdução e Metodologia, classificação de Pressman alinhada à tabela da aula, que não tem categoria para aplicações web, tabelas com título e fonte, referências numeradas e estrutura, interfaces, diagrama e restrições movidos para a descrição do produto, que já os trazia | [Christopher Paraizo](https://github.com/wChrstphr) | [Davi Pierre](https://github.com/DaviPierre) |
