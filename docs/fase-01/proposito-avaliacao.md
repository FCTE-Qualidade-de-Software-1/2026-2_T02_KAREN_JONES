---
sidebar_position: 2
title: Propósito da Avaliação
description: Propósito, objetivos, requisitante, beneficiários e decisões apoiadas pela avaliação do Excalidraw
---

# Propósito da Avaliação

## 1. Identificação do produto

A primeira etapa do processo de avaliação da ISO/IEC 25040 consiste em identificar claramente o software a ser avaliado e seu contexto:

| Campo | Descrição |
|---|---|
| Produto | Excalidraw |
| Versão avaliada | Código do repositório principal (commit e tag serão fixados no início da Fase 02) |
| Domínio | Ferramenta web de quadro branco virtual para diagramação e colaboração |
| Licença | MIT (código aberto) |
| Repositório | [github.com/excalidraw/excalidraw](https://github.com/excalidraw/excalidraw) |
| Tecnologias | TypeScript, React, monorepo com aplicação web e pacote npm |

## 2. Por que avaliar o Excalidraw

O Excalidraw é amplamente utilizado por desenvolvedores, estudantes e equipes de tecnologia para desenhar diagramas e colaborar em tempo real. Apesar de ter uma comunidade muito ativa e milhares de usuários diários, não encontramos avaliações formais de qualidade do projeto baseadas em normas reconhecidas, como a família ISO/IEC 25000 (SQuaRE).

O fato de ser um projeto open source com repositório aberto torna o Excalidraw propício para este estudo. Temos acesso completo ao código-fonte, histórico de commits, pull requests, issues e rotinas de integração contínua (CI).

Vale destacar que esta avaliação não busca emitir certificação nem fazer auditoria formal. Trata-se de um diagnóstico acadêmico para identificar o que o projeto tem de positivo e quais pontos merecem atenção na arquitetura e na implementação.

## 3. Objetivo da avaliação

Seguindo os tipos de objetivos apresentados na norma ISO/IEC 25040 e na Aula 07 da disciplina, o objetivo principal desta avaliação é:

**Indicar pontos para melhoria no produto.**

Para cumprir esse objetivo, definimos as seguintes metas específicas:

1. Diagnosticar a qualidade atual do Excalidraw nas características Manutenabilidade, Confiabilidade e Flexibilidade (ISO/IEC 25010:2023), utilizando análise estática e inspeção dos artefatos do repositório.
2. Identificar boas práticas e pontos fortes já consolidados no código e nos fluxos de desenvolvimento.
3. Mapear pontos fracos e dívida técnica, como componentes excessivamente complexos, acoplamento indevido ou lacunas em testes.
4. Propor melhorias práticas para a aplicação ao final do trabalho, incluindo o desenvolvimento de um protótipo de alta fidelidade para demonstrar soluções de usabilidade, interface e fluxo para o site.
5. Produzir um relatório final rastreável, conectando cada constatação aos requisitos e às métricas da norma.

### O que fica fora do escopo

Para manter o trabalho viável dentro do semestre letivo, delimitamos algumas restrições:
- Não faremos comparações de desempenho com ferramentas comerciais concorrentes.
- Não emitiremos certificado de conformidade técnica.
- As demais características da ISO/IEC 25010:2023 (Adequação Funcional, Desempenho, Compatibilidade, Usabilidade, Segurança e Proteção) não serão medidas, focando o esforço nas três escolhidas.

## 4. Requisitante da avaliação

De acordo com a ISO/IEC 25040, toda avaliação precisa declarar seu requisitante. Como não há um cliente externo solicitando este estudo, a equipe Karen Jones se declara como a própria requisitante da avaliação, assumindo o papel de equipe de QA independente.

Isso significa que:
- Não fazemos parte do time de mantenedores ou desenvolvedores oficiais do Excalidraw.
- Não temos relação comercial ou institucional com os criadores do software.
- A condução do trabalho é autônoma, pautada nos critérios da norma e nas orientações da disciplina de Qualidade de Software 1 (FCTE/UnB).

Essa postura independente é importante porque permite avaliar o projeto de maneira imparcial, sem os vieses de quem desenvolve a ferramenta no dia a dia.

| Campo | Descrição |
|---|---|
| Requisitante | Equipe Karen Jones |
| Papel | Equipe de garantia da qualidade (QA) independente |
| Contexto | Disciplina de Qualidade de Software 1 (FCTE/UnB, 2º semestre de 2026) |
| Objetivo declarado | Indicar pontos para melhoria no produto |

## 5. Partes interessadas e beneficiários

Mesmo sendo uma iniciativa acadêmica sem contratação externa, as conclusões da avaliação podem beneficiar diferentes grupos envolvidos com o ecossistema do Excalidraw:

| Beneficiário | Como os resultados ajudam |
|---|---|
| Mantenedores do Excalidraw | Recebem um diagnóstico externo sobre a organização dos pacotes, acoplamento e cobertura de testes, ajudando a planejar refatorações. |
| Contribuidores open source | Passam a ter visibilidade sobre quais módulos têm maior dívida técnica ou precisam de mais testes, direcionando melhor novos pull requests. |
| Integradores da biblioteca | Encontram dados sobre estabilidade da API, empacotamento, facilidade de instalação e suporte a diferentes versões do React. |
| Usuários e organizações | Obtêm informações confiáveis sobre disponibilidade offline, estabilidade da persistência dos arquivos e compatibilidade entre versões. |
| Equipe avaliadora (Karen Jones) | Aplica os conceitos teóricos e as etapas da ISO/IEC 25040 em um produto real de grande escala. |
| Docentes da disciplina | Têm um projeto prático e documentado para verificar o domínio das normas SQuaRE pela equipe. |

Para mais detalhes sobre as necessidades de cada grupo e o cruzamento com as subcaracterísticas do projeto, consulte o documento de [Partes Interessadas](./interessados.md).

## 6. Decisões apoiadas pela avaliação

Uma avaliação de qualidade é útil quando serve de subsídio para decisões reais. A tabela abaixo relaciona as decisões técnicas e organizacionais que o relatório pretende apoiar, quem é responsável por tomá-las e como os dados levantados contribuem:

| Decisão | Quem decide | Como a avaliação apoia |
|---|---|---|
| Priorizar refatorações no código | Mantenedores do projeto | Aponta arquivos e módulos com alto acoplamento, dependências circulares ou baixa cobertura de testes. |
| Escolher onde contribuir | Contribuidores externos | Identifica partes da base de código que necessitam de mais testes, tipagem ou melhorias de documentação. |
| Adotar ou manter o uso da ferramenta | Equipes e organizações | Apresenta dados sobre tolerância a falhas, funcionamento offline e independência de serviços externos. |
| Implementar melhorias no produto e no site | Equipe avaliadora e comunidade | Fornece evidências para guiar a criação de protótipos de alta fidelidade e propostas de redesign de interface. |
| Avaliar a execução do método SQuaRE | Professores e equipe | Permite checar a conformidade das fases com as normas ISO/IEC 25010, 25023 e 25040. |

## 7. Uso pretendido dos resultados

Os resultados obtidos serão utilizados da seguinte forma:

1. Ficarão publicados abertamente neste site de documentação como relatório técnico acadêmico.
2. Manterão rastreabilidade direta entre os requisitos definidos, as métricas coletadas na Fase 02 e as conclusões finais.
3. Poderão ser compartilhados com os mantenedores do repositório oficial do Excalidraw como contribuição comunitária.
4. Servirão de base para a elaboração de propostas concretas de melhoria para o site, incluindo um protótipo de alta fidelidade focado em usabilidade e experiência do usuário, se for viável e necessário.

Os resultados não serão utilizados para ranqueamento contra outros softwares, nem possuem valor de auditoria contábil, contratual ou certificação comercial.

## 8. Normas e referências

| Referência | Aplicação no projeto |
|---|---|
| ISO/IEC 25010:2023 | Modelo de qualidade de produto de software (definição das características e subcaracterísticas). |
| ISO/IEC 25040:2011 | Processo de avaliação de produto de software em quatro fases. |
| ISO/IEC 25023:2016 | Catálogo de métricas de qualidade interna e externa (aplicado a partir da Fase 02). |
| Aula A07 (FCTE/UnB) | Processo de avaliação de produto de software: tipos de requisitante, objetivos e roteiro da avaliação. |

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| `1.0` | 18/10/2026 | Elaboração inicial do documento de propósito da avaliação, atendendo aos critérios F1-C1 e F1-C2 | [Gabriel Monteiro](https://github.com/GabrielSMonteiro) | |