---
sidebar_position: 1
title: Visão Geral da Fase 01
description: O que estamos definindo nesta primeira fase da avaliação de qualidade do Excalidraw
---

# Fase 01 — Requisitos de Avaliação

Antes de sair medindo qualquer coisa, a norma ISO/IEC 25040 pede que a gente pare e responda algumas perguntas básicas: *por que estamos fazendo essa avaliação? O que exatamente vamos avaliar? Quem se interessa pelos resultados? E quais aspectos de qualidade fazem sentido investigar?*

Essa primeira fase existe exatamente para isso. Não vamos coletar métricas ainda, nem executar ferramentas de análise — o foco agora é montar a base sobre a qual o restante do projeto vai se apoiar.

---

## O que vamos definir aqui

A Fase 01 está organizada nas seguintes entregas e documentos de referência:

1. **[Propósito da avaliação](./proposito-avaliacao.md)** — por que escolhemos o Excalidraw, quem solicita a avaliação, quem se beneficia dos resultados e como eles serão usados.
2. **[Tipo de produto e arquitetura](./tipo-produto.md)** — classificação segundo Pressman e IEEE 1062 (COTS/MOTS/FD), roteiro de caracterização e visão lógica dos componentes.
3. **[Descrição e arquitetura do produto](./descricao-produto.md)** — caracterização técnica detalhada, organização em monorepo, diagrama de contexto/arquitetura, interfaces externas e implicações para a avaliação.
4. **[Partes interessadas](./interessados.md)** — quem são as pessoas afetadas pelos resultados: usuários, desenvolvedores, mantenedores, contribuidores externos, integradores da biblioteca e equipe avaliadora, com matriz de prioridades e critérios de sucesso.
5. **[Priorização das características](./priorizacao-caracteristicas.md)** — método em duas etapas (ênfase e matriz impacto × risco) para a seleção formal das características da ISO/IEC 25010:2023.
6. **[Modelo de qualidade](./modelo-de-qualidade.md)** — características e subcaracterísticas da ISO/IEC 25010:2023 selecionadas: Manutenibilidade, Confiabilidade e Flexibilidade, com justificativas, adaptações e limites de validade.
7. **[Escopo e objetos de avaliação](./escopo-avaliacao.md)** — delimitação dos objetos concretos (O1 a O6), profundidade e fronteiras operacionais da avaliação.
8. **[Requisitos de avaliação](./requisitos-avaliacao.md)** — catálogo de requisitos técnicos e perguntas a responder formuladas por característica e subcaracterística.
9. **[ODS e a Avaliação](./ods.md)** — relação do software com os Objetivos de Desenvolvimento Sustentável da Agenda 2030 (ODS 4, 9 e 10).

---

## Documentos desta fase

Os documentos de cada item acima estão nesta seção e estruturam o relatório de requisitos de avaliação da Fase 01. Os [requisitos de avaliação](./requisitos-avaliacao.md) detalham as perguntas rastreáveis para as etapas seguintes.

---

## Referências Cruzadas

* Os objetivos e o público mapeados em [Propósito da avaliação](./proposito-avaliacao.md) e [Partes interessadas](./interessados.md) orientam a [Priorização das Características](./priorizacao-caracteristicas.md) e o [Modelo de qualidade](./modelo-de-qualidade.md).
* A estrutura técnica apresentada em [Tipo de produto e arquitetura](./tipo-produto.md) e [Descrição e arquitetura do produto](./descricao-produto.md) define a delimitação em [Escopo e objetos de avaliação](./escopo-avaliacao.md) e os critérios em [Requisitos de avaliação](./requisitos-avaliacao.md).
* Os requisitos de avaliação desta fase alimentam a [Fase 02 — Especificação da Avaliação](../fase-02/visao-geral.md), em que cada característica vira um objetivo de medição com questões, hipóteses e métricas.
* As implicações sociais do projeto são abordadas em [ODS e a Avaliação](./ods.md).

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 18/10/2026 | Estruturação da visão geral da Fase 1 e links de navegação | [Gabriel Monteiro](https://github.com/GabrielSMonteiro) | [Maria Eduarda](https://github.com/eduarda-ogomes) |
| 1.1 | 19/10/2026 | Adição das referências cruzadas | [Letícia Santos](https://github.com/LeticiaSantosss) | [Gabriel Monteiro](https://github.com/GabrielSMonteiro) |
| 1.2 | 19/10/2026 | Referência cruzada para a Fase 02 | [Luiz Henrique Soares](https://github.com/luizh-gsoares) | [Christopher](https://github.com/wChrstphr) |