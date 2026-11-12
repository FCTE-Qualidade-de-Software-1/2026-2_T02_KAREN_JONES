---
sidebar_position: 2
title: Propósito da Avaliação
description: Propósito, objetivos, requisitante, beneficiários e decisões apoiadas pela avaliação do Excalidraw
---

import Link from '@docusaurus/Link';

# Propósito da Avaliação

## Introdução

Estabelecer o propósito é a primeira atividade da fase de requisitos da avaliação da ISO/IEC 25040 [[1, p. 4]](#ref-1). O objetivo e os requisitos da avaliação dependem da necessidade de quem a solicita [[1, p. 5]](#ref-1). Esta página declara por que o Excalidraw é avaliado, o objetivo da avaliação, quem a requisita, quem se beneficia dos resultados e que decisões eles apoiam. O produto, no commit `e1b7aac` do repositório oficial, está identificado em [Tipo de produto](./tipo-produto.md#1-identificação-e-versão-analisada).

## Metodologia

O objetivo foi escolhido entre as opções do roteiro da aula [[1, p. 8]](#ref-1), e o requisitante foi definido a partir dos tipos de solicitante apresentados na mesma aula [[1, p. 6]](#ref-1). As características avaliadas seguem o modelo da ISO/IEC 25010:2023 [[2]](#ref-2), e as métricas da Fase 02 partem do catálogo da ISO/IEC 25023 [[3]](#ref-3).

---

## 1. Por que avaliar o Excalidraw

O Excalidraw é usado por desenvolvedores, estudantes e equipes de tecnologia para desenhar diagramas e colaborar em tempo real. Apesar da comunidade ativa, a equipe não encontrou avaliações formais de qualidade do projeto baseadas na família ISO/IEC 25000 (SQuaRE).

Por ser um projeto de código aberto, o Excalidraw oferece acesso ao código-fonte, ao histórico de commits, aos pull requests, às issues e às rotinas de integração contínua (CI). A avaliação não busca emitir certificação nem fazer auditoria formal. Trata-se de um diagnóstico acadêmico para identificar os pontos fortes do projeto e os que merecem atenção na arquitetura e na implementação.

## 2. Objetivo da avaliação

Entre os objetivos listados no roteiro da aula [[1, p. 8]](#ref-1), o desta avaliação é **indicar pontos para melhoria no produto**. Ele se desdobra em cinco metas:

1. Diagnosticar a qualidade atual do Excalidraw em Manutenibilidade, Confiabilidade e Flexibilidade [[2]](#ref-2), com análise estática e inspeção dos artefatos do repositório.
2. Identificar boas práticas e pontos fortes já consolidados no código e nos fluxos de desenvolvimento.
3. Mapear pontos fracos e dívida técnica, como componentes excessivamente complexos, acoplamento indevido ou lacunas em testes.
4. Executar ao menos uma ação de melhoria na Fase 04: uma modificação no código, para problemas técnicos como os de confiabilidade, ou um protótipo de alta fidelidade, se o problema encontrado for de interface ou fluxo de navegação [[4, p. 3]](#ref-4).
5. Produzir um relatório final rastreável, que ligue cada constatação aos requisitos e às métricas.

A escolha das três características está em [Priorização das características](./priorizacao-caracteristicas.md). Ficam fora da avaliação a comparação de desempenho com ferramentas concorrentes, a emissão de certificado de conformidade e a medição das demais características da ISO/IEC 25010:2023. Os limites de cada objeto avaliado estão em [Escopo e objetos de avaliação](./escopo-avaliacao.md).

## 3. Requisitante da avaliação

Entre os solicitantes apresentados na aula estão equipes de desenvolvimento, vendedores, compradores, usuários, a comunidade de software e laboratórios de avaliação [[1, p. 6]](#ref-1). Como nenhum cliente externo solicitou este estudo, a equipe Karen Jones se declara a própria requisitante e assume o papel de equipe de garantia da qualidade (QA) independente. A equipe não faz parte dos mantenedores do Excalidraw nem tem relação comercial ou institucional com seus criadores, o que reduz o viés de quem desenvolve a ferramenta.

<p className="tabela-titulo">Tabela 1: Requisitante da avaliação</p>

| Campo | Descrição |
|---|---|
| Requisitante | Equipe Karen Jones |
| Papel | Equipe de garantia da qualidade (QA) independente |
| Contexto | Disciplina de Qualidade de Software 1 (FCTE/UnB, 2º semestre de 2026) |
| Objetivo declarado | Indicar pontos para melhoria no produto |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>

## 4. Partes interessadas e beneficiários

Mesmo sem contratação externa, as conclusões podem beneficiar diferentes grupos do ecossistema do Excalidraw. As necessidades de cada grupo e sua relação com as subcaracterísticas estão em [Partes interessadas](./interessados.md).

<p className="tabela-titulo">Tabela 2: Beneficiários dos resultados</p>

| Beneficiário | Como os resultados ajudam |
|---|---|
| Mantenedores do Excalidraw | Recebem um diagnóstico externo sobre a organização dos pacotes, acoplamento e cobertura de testes, ajudando a planejar refatorações. |
| Contribuidores open source | Passam a ter visibilidade sobre quais módulos têm maior dívida técnica ou precisam de mais testes, direcionando melhor novos pull requests. |
| Integradores da biblioteca | Encontram dados sobre estabilidade da API, empacotamento, facilidade de instalação e suporte a diferentes versões do React. |
| Usuários e organizações | Obtêm informações confiáveis sobre disponibilidade offline, estabilidade da persistência dos arquivos e compatibilidade entre versões. |
| Equipe avaliadora (Karen Jones) | Aplica os conceitos teóricos e as etapas da ISO/IEC 25040 em um produto real de grande escala. |
| Docentes da disciplina | Têm um projeto prático e documentado para verificar o domínio das normas SQuaRE pela equipe. |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>

## 5. Decisões apoiadas pela avaliação

<p className="tabela-titulo">Tabela 3: Decisões apoiadas pela avaliação</p>

| Decisão | Quem decide | Como a avaliação apoia |
|---|---|---|
| Priorizar refatorações no código | Mantenedores do projeto | Aponta arquivos e módulos com alto acoplamento, dependências circulares ou baixa cobertura de testes. |
| Escolher onde contribuir | Contribuidores externos | Identifica partes da base de código que necessitam de mais testes, tipagem ou melhorias de documentação. |
| Adotar ou manter o uso da ferramenta | Equipes e organizações | Apresenta dados sobre tolerância a falhas, funcionamento offline e independência de serviços externos. |
| Escolher a ação de melhoria da Fase 04 | Equipe avaliadora | Indica o problema de maior impacto e se a ação deve ser uma modificação no código ou um protótipo de alta fidelidade. |
| Avaliar a execução do método SQuaRE | Professores e equipe | Permite checar a conformidade das fases com as normas ISO/IEC 25010, 25023 e 25040. |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>

## 6. Uso pretendido dos resultados

Os resultados ficarão publicados neste site como relatório técnico acadêmico, com rastreabilidade entre os requisitos, as métricas da [Fase 02](../fase-02/plano-gqm.md) e as conclusões finais. Poderão ser compartilhados com os mantenedores do Excalidraw como contribuição comunitária e servirão de base para a ação de melhoria da Fase 04. Não serão usados para ranquear o Excalidraw contra outros softwares nem têm valor de auditoria ou certificação.

---

## Referências

> <Link id="ref-1">1.</Link> RAMOS, Cristiane Soares. **AULA A07 QSW1 PROC AVAL PRODUTO**. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Páginas 4 a 6 e 8. Disponível no Moodle da disciplina.
>
> <Link id="ref-2">2.</Link> ISO/IEC 25010:2023. *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): Product quality model*.
>
> <Link id="ref-3">3.</Link> ISO/IEC 25023:2016. *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): Measurement of system and software product quality*.
>
> <Link id="ref-4">4.</Link> **2026-2 Trabalho final completo v1**. Especificação do trabalho final de Qualidade de Software 1, FCTE/UnB, 2026. Página 3. Disponível no Moodle da disciplina.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 18/10/2026 | Elaboração inicial do documento de propósito da avaliação | [Gabriel Monteiro](https://github.com/GabrielSMonteiro) | [Maria Eduarda](https://github.com/eduarda-ogomes) |
| 1.1 | 10/11/2026 | Introdução e Metodologia, retirada da citação ao critério da disciplina, identificação do produto substituída por link ao tipo de produto com o commit avaliado, meta do protótipo alinhada à ação de melhoria da Fase 04, tabelas com título e fonte e normas convertidas em referências numeradas | [Christopher Paraizo](https://github.com/wChrstphr) | [Gabriel Monteiro](https://github.com/GabrielSMonteiro) |
