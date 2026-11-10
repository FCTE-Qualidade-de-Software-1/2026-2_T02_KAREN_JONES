---
sidebar_position: 1
title: Visão Geral da Fase 01
description: O que estamos definindo nesta primeira fase da avaliação de qualidade do Excalidraw
---

import Link from '@docusaurus/Link';

# Fase 01: Requisitos de Avaliação

## Introdução

A avaliação do Excalidraw segue o processo de avaliação de produto da ISO/IEC 25040 [[2]](#ref-2), apresentado na aula em quatro fases [[1, p. 4]](#ref-1). A Fase 01 estabelece os requisitos da avaliação: o que precisa estar definido antes de escolher métricas ou coletar dados [[1, p. 3]](#ref-1). Nela se decide por que avaliar, o que avaliar, para quem e com quais características de qualidade.

## Metodologia

A fase segue as três atividades que a aula atribui a ela: estabelecer o propósito da avaliação, identificar o tipo de produto e especificar o modelo de qualidade [[1, p. 4]](#ref-1). O propósito parte da necessidade de quem solicita a avaliação e considera os pontos de vista dos usuários do produto [[1, p. 5]](#ref-1). A análise de requisitos define a profundidade, a abrangência e os objetos avaliados [[1, p. 7]](#ref-1), e as características são priorizadas pela ênfase de 1 a 5 dada pelos interessados [[1, p. 9]](#ref-1). Nenhuma métrica é coletada nesta fase.

---

## Documentos desta fase

A Tabela 1 segue a ordem de leitura: do propósito e do produto aos interessados, e destes às características, ao escopo e aos requisitos.

<p className="tabela-titulo">Tabela 1: Documentos da Fase 01</p>

| Documento | Conteúdo |
| :--- | :--- |
| [Propósito da avaliação](./proposito-avaliacao.md) | Por que o Excalidraw foi escolhido, quem solicita a avaliação e como os resultados serão usados |
| [Tipo de produto](./tipo-produto.md) | Identificação da versão avaliada, classificação segundo Pressman e a IEEE 1062 e roteiro de caracterização |
| [Descrição e arquitetura do produto](./descricao-produto.md) | Organização em monorepo, diagrama de contexto e arquitetura e interfaces externas |
| [Partes interessadas](./interessados.md) | Usuários, desenvolvedores, mantenedores, contribuidores, integradores e equipe avaliadora, com matriz de prioridades |
| [Priorização das características](./priorizacao-caracteristicas.md) | Ênfase de 1 a 5 e matriz de impacto e risco para escolher as características da ISO/IEC 25010:2023 |
| [Modelo de qualidade](./modelo-de-qualidade.md) | Manutenibilidade, Confiabilidade e Flexibilidade, com as subcaracterísticas interpretadas para o Excalidraw e as adaptações ao contexto |
| [Escopo e objetos de avaliação](./escopo-avaliacao.md) | Objetos O1 a O6, profundidade, fronteiras e limites de validade da avaliação |
| [Requisitos de avaliação](./requisitos-avaliacao.md) | Requisitos RQ-MAN, RQ-CONF e RQ-FLEX por subcaracterística |
| [ODS e a avaliação](./ods.md) | Relação do produto com os ODS 4, 9 e 10 da Agenda 2030 |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>

## Relação com a Fase 02

O propósito e os interessados orientam a priorização e o modelo de qualidade. O tipo de produto e a descrição técnica delimitam o escopo e os requisitos. Na [Fase 02](../fase-02/visao-geral.md), cada característica do modelo vira um [objetivo de medição](../fase-02/estrutura-gqm.md#3-objetivos-de-medição), e os requisitos de cada subcaracterística são reunidos numa questão.

---

## Referências

> <Link id="ref-1">1.</Link> RAMOS, Cristiane Soares. **AULA A07 QSW1 PROC AVAL PRODUTO**. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Páginas 3 a 5, 7 e 9. Disponível no Moodle da disciplina.
>
> <Link id="ref-2">2.</Link> ISO/IEC 25040. *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): Evaluation process*.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 18/10/2026 | Estruturação da visão geral da Fase 1 e links de navegação | [Gabriel Monteiro](https://github.com/GabrielSMonteiro) | [Maria Eduarda](https://github.com/eduarda-ogomes) |
| 1.1 | 19/10/2026 | Adição das referências cruzadas | [Letícia Santos](https://github.com/LeticiaSantosss) | [Gabriel Monteiro](https://github.com/GabrielSMonteiro) |
| 1.2 | 19/10/2026 | Referência cruzada para a Fase 02 | [Luiz Henrique Soares](https://github.com/luizh-gsoares) | [Christopher](https://github.com/wChrstphr) |
| 1.3 | 10/11/2026 | Título sem travessão, Introdução e Metodologia com citações à AULA A07, tabela de documentos com título e fonte e descrições alinhadas ao conteúdo revisado das páginas, relação com a Fase 02 em um parágrafo e referências numeradas | [Christopher Paraizo](https://github.com/wChrstphr) | [Gabriel Monteiro](https://github.com/GabrielSMonteiro) |
