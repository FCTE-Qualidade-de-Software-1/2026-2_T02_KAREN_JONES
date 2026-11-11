---
sidebar_position: 9
title: Requisitos de Avaliação
description: Requisitos do Excalidraw por característica e subcaracterística da ISO/IEC 25010:2023
---

import Link from '@docusaurus/Link';

# Requisitos de Avaliação do Excalidraw

## Introdução

A análise de requisitos define os requisitos de qualidade do produto a partir dos objetivos da avaliação, que traduzem o interesse do requisitante [[1, p. 7]](#ref-1). Esta página reúne os requisitos de avaliação do Excalidraw, isto é, as perguntas que as fases seguintes precisam responder, organizadas pelas características e subcaracterísticas da ISO/IEC 25010:2023 [[2]](#ref-2).

## Metodologia

Cada requisito foi escrito como pergunta verificável a partir de uma subcaracterística do [modelo de qualidade](./modelo-de-qualidade.md), com a interpretação para o Excalidraw que o modelo registra e as necessidades dos grupos mapeados em [Partes interessadas](./interessados.md). A profundidade e os objetos a que cada requisito se aplica estão em [Escopo e objetos de avaliação](./escopo-avaliacao.md).

---

## 1. Como ler os requisitos

Cada requisito tem um identificador (`RQ-MAN`, `RQ-CONF` ou `RQ-FLEX`, seguido de número) e a subcaracterística a que se liga. Os interessados principais de cada subcaracterística estão na [rastreabilidade do modelo de qualidade](./modelo-de-qualidade.md#rastreabilidade-entre-subcaracterísticas-interessados-e-artefatos), e as questões e métricas que respondem a cada requisito, na [rastreabilidade do Plano GQM](../fase-02/plano-gqm.md#6-rastreabilidade-com-a-fase-01).

---

## 2. Requisitos de Manutenibilidade

Requisitos ligados à Manutenibilidade, organizados pelas subcaracterísticas Modularidade, Reusabilidade, Analisabilidade, Modificabilidade e Testabilidade.

<p className="tabela-titulo">Tabela 1: Requisitos de Manutenibilidade</p>

| ID | Requisito (pergunta a responder) | Subcaracterística |
| :--- | :--- | :--- |
| **RQ-MAN-01** | Existem limites claros entre a aplicação (`excalidraw-app/`) e a biblioteca (`packages/excalidraw/`)? | Modularidade |
| **RQ-MAN-02** | As dependências entre os pacotes seguem direção consistente, sem ciclos e sem pacotes de base dependendo de pacotes de nível superior? | Modularidade |
| **RQ-MAN-03** | Cada pacote tem responsabilidade coesa e baixo nível de dependência desnecessária em relação aos demais? | Modularidade |
| **RQ-MAN-04** | Os componentes podem ser reutilizados em outros contextos, inclusive pacotes menores (matemática e utilitários) de forma isolada? | Reusabilidade |
| **RQ-MAN-05** | A interface pública da biblioteca (propriedades e callbacks) está documentada e separada dos detalhes internos? | Reusabilidade |
| **RQ-MAN-06** | O código pode ser compreendido com facilidade, e é possível identificar com clareza as partes responsáveis por cada funcionalidade? | Analisabilidade |
| **RQ-MAN-07** | O projeto documenta convenções de código, arquitetura e formas de contribuir? | Analisabilidade |
| **RQ-MAN-08** | Existem ferramentas de lint, formatação e verificação de tipos integradas ao fluxo de desenvolvimento? | Analisabilidade |
| **RQ-MAN-09** | Alterações podem ser feitas sem impacto excessivo em componentes não relacionados (alcance das mudanças nos commits e pull requests)? | Modificabilidade |
| **RQ-MAN-10** | Há arquivos ou funções que concentram responsabilidades demais e dificultam alterações? | Modificabilidade |
| **RQ-MAN-11** | O sistema apresenta condições adequadas para testes automatizados, incluindo teste de componentes de forma isolada? | Testabilidade |
| **RQ-MAN-12** | Os testes cobrem diferentes níveis (unitário, integração e, quando houver, ponta a ponta)? | Testabilidade |
| **RQ-MAN-13** | Os testes são executados automaticamente a cada alteração proposta? | Testabilidade |

<p className="tabela-fonte">Fonte: [Letícia Santos](https://github.com/LeticiaSantosss), 2026.</p>

---

## 3. Requisitos de Confiabilidade

Requisitos ligados à Confiabilidade, organizados pelas subcaracterísticas Ausência de falhas, Disponibilidade, Tolerância a falhas e Recuperabilidade.

<p className="tabela-titulo">Tabela 2: Requisitos de Confiabilidade</p>

| ID | Requisito (pergunta a responder) | Subcaracterística |
| :--- | :--- | :--- |
| **RQ-CONF-01** | Verificações automáticas (tipos, lint e testes) e revisão de código atuam antes da integração das alterações, reduzindo falhas e regressões? | Ausência de falhas |
| **RQ-CONF-02** | Os defeitos relatados são registrados, classificados e tratados de forma organizada? | Ausência de falhas |
| **RQ-CONF-03** | O editor continua utilizável sem conexão após o primeiro carregamento (PWA)? | Disponibilidade |
| **RQ-CONF-04** | O editor local funciona sem depender de sessão colaborativa ou de recursos carregados remotamente em tempo de execução? | Disponibilidade |
| **RQ-CONF-05** | O editor mantém as funcionalidades essenciais diante de problemas de conectividade, com falhas de serviços externos isoladas das funcionalidades locais? | Tolerância a falhas |
| **RQ-CONF-06** | O editor local continua funcionando quando uma sessão de colaboração falha ou é encerrada? | Tolerância a falhas |
| **RQ-CONF-07** | Arquivos inválidos ou corrompidos são tratados sem comprometer a aplicação, com mensagens que informem a falha e orientem a próxima ação? | Tolerância a falhas |
| **RQ-CONF-08** | O último estado do desenho é restaurado automaticamente ao reabrir a aplicação, inclusive após fechamento inesperado? | Recuperabilidade |
| **RQ-CONF-09** | O software permite armazenar e recuperar os desenhos, reabrindo trabalhos salvos em arquivos `.excalidraw`? | Recuperabilidade |
| **RQ-CONF-10** | Arquivos criados em versões anteriores continuam podendo ser abertos nas versões atuais? | Recuperabilidade |
| **RQ-CONF-11** | O usuário consegue desfazer e refazer ações? | Recuperabilidade |

<p className="tabela-fonte">Fonte: [Letícia Santos](https://github.com/LeticiaSantosss), 2026.</p>

---

## 4. Requisitos de Flexibilidade

Requisitos ligados à Flexibilidade (Portabilidade na edição de 2011 da norma), organizados pelas subcaracterísticas Adaptabilidade, Escalabilidade, Instalabilidade e Substituibilidade.

<p className="tabela-titulo">Tabela 3: Requisitos de Flexibilidade</p>

| ID | Requisito (pergunta a responder) | Subcaracterística |
| :--- | :--- | :--- |
| **RQ-FLEX-01** | A aplicação pode ser utilizada em diferentes navegadores? Quais navegadores e versões são declarados como suportados e quais APIs web específicas são exigidas? | Adaptabilidade |
| **RQ-FLEX-02** | A biblioteca pode ser integrada em diferentes versões e ambientes React, inclusive com renderização no servidor (SSR) e diferentes empacotadores? | Adaptabilidade |
| **RQ-FLEX-03** | O produto apresenta dependências específicas que dificultam sua utilização em determinados ambientes? | Adaptabilidade |
| **RQ-FLEX-04** | O editor é utilizável em dispositivos móveis e com entrada por toque ou caneta? | Adaptabilidade |
| **RQ-FLEX-05** | O editor mantém desempenho utilizável (abertura, movimentação e edição de elementos) quando o número de elementos do desenho cresce? | Escalabilidade |
| **RQ-FLEX-06** | Desenhos grandes continuam podendo ser abertos, salvos e exportados sem travar a aplicação? | Escalabilidade |
| **RQ-FLEX-07** | A biblioteca pode ser instalada, atualizada e removida por mecanismos convencionais do ecossistema JavaScript? | Instalabilidade |
| **RQ-FLEX-08** | A aplicação pode ser construída e implantada em diferentes ambientes, e quais pré-requisitos (versões de ferramentas) são exigidos? | Instalabilidade |
| **RQ-FLEX-09** | O suporte a Docker facilita a implantação? | Instalabilidade |
| **RQ-FLEX-10** | As instruções de instalação e execução (local e Docker) estão documentadas e são reproduzíveis? | Instalabilidade |
| **RQ-FLEX-11** | Os dados produzidos pelo sistema podem ser exportados para formatos utilizáveis fora da aplicação (`.excalidraw`, PNG e SVG)? | Substituibilidade |
| **RQ-FLEX-12** | Os formatos exportados são abertos, documentados e permitem reimportar o conteúdo sem perda relevante? | Substituibilidade |

<p className="tabela-fonte">Fonte: [Letícia Santos](https://github.com/LeticiaSantosss), 2026.</p>

---

## Referências

> <Link id="ref-1">1.</Link> RAMOS, Cristiane Soares. **AULA A07 QSW1 PROC AVAL PRODUTO**. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Página 7. Disponível no Moodle da disciplina.
>
> <Link id="ref-2">2.</Link> ISO/IEC 25010:2023. *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): Product quality model*.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 15/10/2026 | Primeira versão dos requisitos de avaliação de Manutenibilidade, Confiabilidade e Flexibilidade (ISO/IEC 25010:2023) | [Letícia Santos](https://github.com/LeticiaSantosss) | [Gabriel Monteiro](https://github.com/GabrielSMonteiro) |
| 1.1 | 18/10/2026 | Harmonização da terminologia Maturidade e padronização do frontmatter | [Gabriel Monteiro](https://github.com/GabrielSMonteiro) | [Maria Eduarda](https://github.com/eduarda-ogomes) |
| 1.2 | 10/11/2026 | Introdução e Metodologia, subcaracterística Ausência de falhas adotada como na edição de 2023, nome da característica na edição de 2011 corrigido para Portabilidade, links para a rastreabilidade do modelo e do Plano GQM, tabelas com título e fonte e referências | [Christopher Paraizo](https://github.com/wChrstphr) | [Letícia Santos](https://github.com/LeticiaSantosss) |
