---
sidebar_position: 1
title: Método GQM e Objetivos de Medição
description: Como o método GQM é aplicado na especificação da avaliação do Excalidraw e quais objetivos de medição derivam das prioridades da Fase 01
---

import Link from '@docusaurus/Link';

# Método GQM e objetivos de medição

## Introdução

A avaliação do Excalidraw segue o processo de avaliação da [ISO/IEC 25040](#ref-6), apresentado na aula em quatro fases: estabelecer os requisitos da avaliação, especificar a avaliação, projetar a avaliação e executá-la [[2, p. 4]](#ref-2). A [Fase 01](../fase-01/visao-geral.md) definiu por que avaliar, o que avaliar e quais características de qualidade priorizar.

A Fase 02 especifica a avaliação: define o que será medido, com detalhe suficiente para que a avaliação seja repetível e reprodutível [[2, p. 15]](#ref-2). As subcaracterísticas escolhidas na Fase 01 são desdobradas em atributos que possam ser medidos e pontuados [[2, p. 16]](#ref-2), e são definidos os critérios para interpretar as medições [[2, p. 17]](#ref-2).

Para esse desdobramento, a avaliação usa o método *Goal–Question–Metric* (GQM). Esta página resume o método, mostra como ele foi adaptado e apresenta os três objetivos de medição. O detalhamento está nas [abstraction sheets](./abstraction-sheets.md), nas páginas de [G1](./gqm-manutenibilidade.md), [G2](./gqm-confiabilidade.md) e [G3](./gqm-flexibilidade.md), nos [níveis de pontuação e critérios de julgamento](./pontuacao-julgamento.md) e no [Plano GQM](./plano-gqm.md).

## Metodologia

O método foi montado a partir das etapas de definição do GQM apresentadas na AULA 08 [[1, p. 21]](#ref-1) e das atividades da fase de especificação apresentadas na AULA A07 [[2, p. 4]](#ref-2). Cada etapa foi comparada com o contexto da avaliação, em que não há acesso à equipe do Excalidraw, e adaptada quando necessário. Os objetivos de medição foram escritos no template da aula a partir das características e dos interessados priorizados na [Fase 01](../fase-01/priorizacao-caracteristicas.md), e as questões, a partir dos [requisitos de avaliação](../fase-01/requisitos-avaliacao.md).

---

## 1. O que é o GQM

O GQM foi definido por Victor Basili [[4]](#ref-4) e parte de um princípio simples: **mede-se para algum fim** [[1, p. 6]](#ref-1). Em vez de começar pela lista de métricas disponíveis, começa-se pelo objetivo da medição e só então se decide o que coletar. A estrutura tem três níveis [[1, p. 8]](#ref-1):

<p className="tabela-titulo">Tabela 1: Níveis do GQM</p>

| Nível | Elemento | Papel nesta avaliação |
| :--- | :--- | :--- |
| Conceitual | **Objetivo** (*Goal*) | O que se quer entender sobre o Excalidraw, sob qual foco de qualidade e do ponto de vista de quem. |
| Operacional | **Questão** (*Question*) | Perguntas cujas respostas dizem se o objetivo foi atendido. Para cada questão, as respostas esperadas são elaboradas como hipóteses [[1, p. 34]](#ref-1). |
| Quantitativo | **Métrica** (*Metric*) | Dados coletados para responder cada questão de forma objetiva. |

<p className="tabela-fonte">Fonte: adaptada de Ramos [[1, p. 8]](#ref-1).</p>

A interpretação percorre o caminho inverso: as métricas respondem às questões, e as respostas às questões dizem se o objetivo foi alcançado [[1, p. 7]](#ref-1).

Nesta avaliação, os objetivos são identificados por G1, G2 e G3 (de *goal*). As questões de cada objetivo recebem o número do objetivo seguido de um número sequencial (Q1.1 é a primeira questão de G1), e as métricas recebem o número da questão seguido de outro número sequencial (M1.1.1 é a primeira métrica de Q1.1).

A aula admite que nem sempre é possível definir hipóteses, e elas podem ser valores ou comparações [[1, p. 31]](#ref-1). Nesta avaliação, todas as questões têm hipóteses, uma por métrica, para que cada resultado possa ser comparado com uma expectativa definida antes da medição. Cada hipótese tem uma única afirmação e uma regra de confirmação, cujo limite vem das [faixas de pontuação](./pontuacao-julgamento.md#2-como-as-faixas-foram-definidas) da métrica ou da própria definição da métrica.

---

## 2. Como as etapas do GQM foram adaptadas

A aula apresenta oito etapas para a definição do GQM [[1, p. 21]](#ref-1). A Tabela 2 mostra como cada uma é aplicada nesta avaliação e em que fase o resultado é entregue.

<p className="tabela-titulo">Tabela 2: Etapas do GQM nesta avaliação</p>

| Etapa | Como é aplicada | Fase |
| :--- | :--- | :---: |
| Definir objetivos de medição [[1, p. 22 e 24]](#ref-1) | Um objetivo por característica selecionada, no template da aula ([seção 3](#3-objetivos-de-medição) desta página). | 02 |
| Rever ou produzir modelos de processo [[1, p. 27]](#ref-1) | Na aula, essa etapa analisa o processo de desenvolvimento para ver onde as medições podem ser feitas. Como aqui o objeto medido é um produto, esse papel é cumprido pela [descrição do produto](../fase-01/descricao-produto.md) e pelas partes do Excalidraw delimitadas no [escopo](../fase-01/escopo-avaliacao.md). | 02 |
| Conduzir entrevistas GQM [[1, p. 28]](#ref-1) | Os mantenedores do Excalidraw não estão disponíveis para entrevistas. A equipe avaliadora preenche, em reunião, uma *abstraction sheet* por objetivo, assumindo o ponto de vista dos interessados mapeados na Fase 01. A *abstraction sheet* é o quadro que registra as métricas possíveis, as expectativas sobre elas (hipóteses de *baseline*) e os fatores que podem influenciar os resultados [[1, p. 29]](#ref-1). As três estão em [Abstraction sheets dos objetivos](./abstraction-sheets.md), e as limitações dessa adaptação, na [seção 6](#6-limitações-do-método-nesta-avaliação). | 02 |
| Definir e rever questões e hipóteses [[1, p. 33 a 35]](#ref-1) | Uma questão por subcaracterística, reunindo os requisitos de avaliação da Fase 01 ([seção 4](#4-estrutura-das-questões)). Cada questão recebe uma hipótese por métrica. | 02 |
| Definir métricas [[1, p. 38]](#ref-1) | Métricas documentadas em uma ficha padronizada ([seção 5](#5-ficha-de-cada-métrica)), escolhidas pelas características desejáveis apresentadas na aula [[1, p. 41]](#ref-1). | 02 |
| Verificar métricas [[1, p. 42]](#ref-1) | Conferir a consistência e a completude entre objetivos, questões e métricas, e se cada métrica pode ser coletada na versão avaliada do código, com as ferramentas disponíveis. O resultado está nas seções de rastreabilidade e de verificação das métricas de cada página de objetivo. | 02 |
| Produzir planos [[1, p. 43 a 46]](#ref-1) | [Plano GQM](./plano-gqm.md) na Fase 02. Plano de Medição e Plano de Análise na Fase 03, junto com o plano de avaliação [[2, p. 18 e 19]](#ref-2). | 02 e 03 |
| Rever planos [[1, p. 47]](#ref-1) | A aula prevê avaliar os planos com os membros da equipe do projeto medido e aprová-los. Como não há acesso à equipe do Excalidraw, cada artefato é revisado e aprovado por outro integrante da equipe avaliadora antes de ser publicado. | 02 e 03 |

<p className="tabela-fonte">Fonte: adaptada de Ramos [[1, p. 21 a 47]](#ref-1).</p>

### Divisão entre as Fases 02 e 03

<p className="tabela-titulo">Tabela 3: Artefatos do GQM em cada fase</p>

| Artefato | Conteúdo | Fase |
| :--- | :--- | :---: |
| [**Plano GQM**](./plano-gqm.md) | Objetivos, questões, métricas e hipóteses, com as diretrizes de interpretação [[1, p. 44]](#ref-1). | 02 |
| [*Abstraction sheets*](./abstraction-sheets.md) | Foco de qualidade, fatores de variação, hipóteses de *baseline* e impacto dos fatores [[1, p. 29]](#ref-1). | 02 |
| [Níveis de pontuação e critérios de julgamento](./pontuacao-julgamento.md) | Como cada resultado de medição é classificado [[2, p. 17]](#ref-2). | 02 |
| **Plano de Medição** | Faixa de valores possíveis de cada medida, responsável, momento, meio e ferramenta de coleta de cada métrica [[1, p. 45]](#ref-1). A faixa de valores possíveis é a escala da medida, como 0 a 100 para um percentual, e não se confunde com as faixas dos níveis de pontuação, definidas na Fase 02. | 03 |
| **Plano de Análise** | Processamento dos dados, forma de apresentação e comparação com as hipóteses [[1, p. 46]](#ref-1). | 03 |

<p className="tabela-fonte">Fonte: adaptada de Ramos [[1, p. 29, 44 a 46]](#ref-1) e [[2, p. 17]](#ref-2).</p>

O Plano GQM é a base para definir os procedimentos de coleta e para elaborar os planos de medição e de análise [[1, p. 44]](#ref-1). Na Fase 02, o procedimento de coleta de cada métrica já é registrado na sua ficha ([seção 5](#5-ficha-de-cada-métrica)). O detalhamento operacional fica para os dois planos, produzidos na Fase 03, quando o processo de avaliação elabora o plano de avaliação [[2, p. 18]](#ref-2).

---

## 3. Objetivos de medição

Os objetivos seguem o template da aula [[1, p. 24]](#ref-1). Cada um corresponde a uma característica selecionada na [priorização](../fase-01/priorizacao-caracteristicas.md), e o ponto de vista é o dos interessados para os quais a característica é prioridade principal na [matriz de prioridades](../fase-01/interessados.md#matriz-de-prioridades).

No template da aula, o ponto de vista é o da pessoa que mede o objeto, ou seja, quem deseja a avaliação [[1, p. 24]](#ref-1). Nesta avaliação não há um cliente externo: a própria equipe solicita e executa a avaliação, atuando como uma equipe de garantia da qualidade independente do projeto Excalidraw. Se o ponto de vista fosse o da equipe, os três objetivos teriam o mesmo ponto de vista e não mostrariam para quem cada característica importa. Por isso, a equipe mede, mas adota o ponto de vista dos interessados mapeados na Fase 01. Assim, o foco de qualidade e o ponto de vista de cada objetivo derivam diretamente das prioridades da Fase 01.

O propósito escolhido é **entender**. A equipe não mantém o Excalidraw e não pode alterar o produto, então mede para caracterizá-lo. Essa caracterização serve ao objetivo da avaliação definido no [propósito](../fase-01/proposito-avaliacao.md), que é indicar pontos para melhoria no produto. As ações de melhoria ficam para a Fase 04.

O contexto é o mesmo nos três objetivos: o código-fonte público do Excalidraw na versão de 18/10/2026, identificada no [escopo](../fase-01/escopo-avaliacao.md). A equipe analisa esse código, o histórico público do repositório e a aplicação construída a partir dessa versão e executada em ambiente de teste local, sem acesso aos servidores de produção.

A origem de cada objetivo na Fase 01 é dada pela [ênfase](../fase-01/priorizacao-caracteristicas.md#etapa-1-ênfase-de-1-a-5-a-partir-dos-interessados), de 1 a 5, e pela [prioridade](../fase-01/priorizacao-caracteristicas.md#estimativa-de-risco-e-prioridade), que é o produto da ênfase pelo risco.

### G1: Manutenibilidade

<p className="tabela-titulo">Tabela 4: Objetivo G1: Manutenibilidade</p>

| Campo do template | Valor |
| :--- | :--- |
| Analisar | o código-fonte do Excalidraw (biblioteca, aplicação web e pacotes auxiliares), seus testes, sua documentação para desenvolvedores e o histórico público de alterações |
| para o propósito de | entender |
| com respeito a | Manutenibilidade: modularidade, reusabilidade, analisabilidade, modificabilidade e testabilidade |
| do ponto de vista de | mantenedores e contribuidores do projeto |
| no contexto de | código-fonte público na versão de 18/10/2026, avaliado por equipe independente |

<p className="tabela-fonte">Fonte: adaptada do template de Ramos [[1, p. 24]](#ref-1).</p>

**Origem na Fase 01:** ênfase 4 e prioridade 12 (impacto × risco). É prioridade principal para desenvolvedores, mantenedores, contribuidores e equipes de qualidade.

### G2: Confiabilidade

<p className="tabela-titulo">Tabela 5: Objetivo G2: Confiabilidade</p>

| Campo do template | Valor |
| :--- | :--- |
| Analisar | o editor, a aplicação web e os mecanismos de colaboração e de salvamento no navegador, além do histórico público de defeitos relatados |
| para o propósito de | entender |
| com respeito a | Confiabilidade: ausência de falhas, disponibilidade, tolerância a falhas e recuperabilidade |
| do ponto de vista de | usuários finais |
| no contexto de | código-fonte público na versão de 18/10/2026, avaliado por equipe independente, sem acesso aos servidores de produção |

<p className="tabela-fonte">Fonte: adaptada do template de Ramos [[1, p. 24]](#ref-1).</p>

**Origem na Fase 01:** ênfase 4 e maior prioridade da seleção (16). É prioridade principal para usuários finais, mantenedores e equipes de qualidade. O ponto de vista é o do usuário final porque é quem perde trabalho quando a confiabilidade falha.

### G3: Flexibilidade (antiga Portabilidade)

Na ISO/IEC 25010:2023 [[5]](#ref-5), adotada desde a Fase 01 no [modelo de qualidade](../fase-01/modelo-de-qualidade.md), a Portabilidade da edição de 2011 passou a se chamar Flexibilidade e ganhou a subcaracterística Escalabilidade. As demais (adaptabilidade, instalabilidade e substituibilidade) continuam as mesmas.

<p className="tabela-titulo">Tabela 6: Objetivo G3: Flexibilidade</p>

| Campo do template | Valor |
| :--- | :--- |
| Analisar | a biblioteca `@excalidraw/excalidraw` e a aplicação web, incluindo a interface pública da biblioteca, as instruções de instalação e os formatos de exportação |
| para o propósito de | entender |
| com respeito a | Flexibilidade: adaptabilidade, escalabilidade, instalabilidade e substituibilidade |
| do ponto de vista de | desenvolvedores que integram a biblioteca em seus sistemas e equipes de implantação e operação |
| no contexto de | código-fonte público na versão de 18/10/2026, avaliado por equipe independente |

<p className="tabela-fonte">Fonte: adaptada do template de Ramos [[1, p. 24]](#ref-1).</p>

**Origem na Fase 01:** ênfase 3 e prioridade 9. É prioridade principal para integradores e equipes de operação, grupos que as outras duas características atendem pouco.

---

## 4. Estrutura das questões

Cada objetivo tem **uma questão por subcaracterística**, porque as subcaracterísticas são os atributos que compõem o foco de qualidade de cada objetivo. Cada questão reúne os [requisitos de avaliação](../fase-01/requisitos-avaliacao.md) da Fase 01 ligados à mesma subcaracterística, de modo que toda questão pode ser rastreada até um requisito. A Tabela 7 mostra o texto de cada questão. As hipóteses e as métricas de cada uma estão na página do objetivo, aberta pelo link do código da questão.

<p className="tabela-titulo">Tabela 7: Questões de cada objetivo</p>

| Objetivo | Questão | Subcaracterística | Requisitos de avaliação reunidos |
| :--- | :--- | :--- | :--- |
| G1 | [Q1.1](./gqm-manutenibilidade.md#3-q11-modularidade): Em que medida o código está dividido em pacotes independentes, com dependências em uma única direção? | Modularidade | [RQ-MAN-01 a RQ-MAN-03](../fase-01/requisitos-avaliacao.md#2-requisitos-de-manutenibilidade) |
| G1 | [Q1.2](./gqm-manutenibilidade.md#4-q12-reusabilidade): Os pacotes podem ser usados fora do editor, e a interface pública da biblioteca está documentada para quem vai reutilizá-la? | Reusabilidade | [RQ-MAN-04 e RQ-MAN-05](../fase-01/requisitos-avaliacao.md#2-requisitos-de-manutenibilidade) |
| G1 | [Q1.3](./gqm-manutenibilidade.md#5-q13-analisabilidade): O código pode ser entendido com facilidade, com apoio de documentação e de verificações automáticas? | Analisabilidade | [RQ-MAN-06 a RQ-MAN-08](../fase-01/requisitos-avaliacao.md#2-requisitos-de-manutenibilidade) |
| G1 | [Q1.4](./gqm-manutenibilidade.md#6-q14-modificabilidade): As alterações no código ficam restritas a poucas partes, ou tendem a se espalhar e a passar por arquivos que concentram responsabilidades demais? | Modificabilidade | [RQ-MAN-09 e RQ-MAN-10](../fase-01/requisitos-avaliacao.md#2-requisitos-de-manutenibilidade) |
| G1 | [Q1.5](./gqm-manutenibilidade.md#7-q15-testabilidade): O código pode ser verificado por testes automatizados, em diferentes níveis, executados a cada alteração? | Testabilidade | [RQ-MAN-11 a RQ-MAN-13](../fase-01/requisitos-avaliacao.md#2-requisitos-de-manutenibilidade) |
| G2 | [Q2.1](./gqm-confiabilidade.md#3-q21-ausência-de-falhas): O projeto evita que falhas cheguem ao usuário e trata de forma organizada os defeitos que chegam? | Ausência de falhas | [RQ-CONF-01 e RQ-CONF-02](../fase-01/requisitos-avaliacao.md#3-requisitos-de-confiabilidade) |
| G2 | [Q2.2](./gqm-confiabilidade.md#4-q22-disponibilidade): O editor continua disponível para o usuário sem conexão e sem depender de serviços externos? | Disponibilidade | [RQ-CONF-03 e RQ-CONF-04](../fase-01/requisitos-avaliacao.md#3-requisitos-de-confiabilidade) |
| G2 | [Q2.3](./gqm-confiabilidade.md#5-q23-tolerância-a-falhas): O editor continua funcionando quando recebe dados inválidos ou quando a conexão com a colaboração falha? | Tolerância a falhas | [RQ-CONF-05 a RQ-CONF-07](../fase-01/requisitos-avaliacao.md#3-requisitos-de-confiabilidade) |
| G2 | [Q2.4](./gqm-confiabilidade.md#6-q24-recuperabilidade): O usuário recupera seu trabalho depois de fechar a aplicação, de reabrir arquivos antigos ou de cometer um erro de edição? | Recuperabilidade | [RQ-CONF-08 a RQ-CONF-11](../fase-01/requisitos-avaliacao.md#3-requisitos-de-confiabilidade) |
| G3 | [Q3.1](./gqm-flexibilidade.md#3-q31-adaptabilidade): O Excalidraw pode ser usado em diferentes navegadores, dispositivos e ambientes de integração sem adaptações no código? | Adaptabilidade | [RQ-FLEX-01 a RQ-FLEX-04](../fase-01/requisitos-avaliacao.md#4-requisitos-de-flexibilidade) |
| G3 | [Q3.2](./gqm-flexibilidade.md#4-q32-escalabilidade): O editor continua utilizável quando o desenho cresce? | Escalabilidade | [RQ-FLEX-05 e RQ-FLEX-06](../fase-01/requisitos-avaliacao.md#4-requisitos-de-flexibilidade) |
| G3 | [Q3.3](./gqm-flexibilidade.md#5-q33-instalabilidade): A biblioteca e a aplicação podem ser instaladas, construídas e implantadas seguindo apenas a documentação, em ambientes diferentes? | Instalabilidade | [RQ-FLEX-07 a RQ-FLEX-10](../fase-01/requisitos-avaliacao.md#4-requisitos-de-flexibilidade) |
| G3 | [Q3.4](./gqm-flexibilidade.md#6-q34-substituibilidade): Os desenhos feitos no Excalidraw podem ser levados para outras ferramentas, em formatos abertos e sem perda de conteúdo? | Substituibilidade | [RQ-FLEX-11 e RQ-FLEX-12](../fase-01/requisitos-avaliacao.md#4-requisitos-de-flexibilidade) |

<p className="tabela-fonte">Fonte: [Christopher Paraizo](https://github.com/wChrstphr), 2026.</p>

Ao todo, são 3 objetivos, 13 questões e 36 requisitos de avaliação. Para manter a avaliação viável, a meta é de **uma a três métricas por questão**. Uma questão não deve ser apenas uma métrica escrita em forma de pergunta: ela precisa caracterizar o objeto em relação ao foco de qualidade, e as métricas é que a respondem [[1, p. 33 e 34]](#ref-1).

Antes de seguir para as métricas, cada questão passa pela revisão proposta na aula: respondendo a questão, é possível concluir algo sobre o objetivo? As hipóteses ajudam a analisar o resultado [[1, p. 35]](#ref-1)?

---

## 5. Ficha de cada métrica

Cada métrica é documentada com os campos abaixo. Os cinco primeiros garantem que qualquer pessoa consiga calcular a métrica e interpretar o resultado da mesma forma. Os dois últimos ligam a métrica à questão que ela responde e justificam sua escolha.

<p className="tabela-titulo">Tabela 8: Campos da ficha de cada métrica</p>

| Campo | Descrição | Fonte |
| :--- | :--- | :--- |
| Definição | O que a métrica mede, sem ambiguidade. | [[1, p. 4]](#ref-1) |
| Procedimento de cálculo | Fórmula, unidade e escala. | [[3, p. 1]](#ref-3) |
| Fonte dos dados | Parte do produto e artefato de onde o dado sai. | [[3, p. 1]](#ref-3) |
| Procedimento de coleta | Como o dado é obtido: ferramenta, comando ou inspeção. | [[3, p. 1]](#ref-3) |
| Critério de interpretação | Regra que confirma ou refuta a hipótese ligada à métrica e como o valor é lido. | [[3, p. 1]](#ref-3) |
| Questão respondida | Identificador da questão (ex.: Q1.1). | [[1, p. 38]](#ref-1) |
| Características desejáveis | Justificativa de simplicidade, consistência e objetividade, facilidade de coleta, robustez, validade e independência da linguagem de programação. | [[1, p. 41]](#ref-1) |

<p className="tabela-fonte">Fonte: [Christopher Paraizo](https://github.com/wChrstphr), 2026.</p>

Depois das fichas, os níveis de pontuação e os critérios de julgamento de todas as métricas são definidos em [Níveis de pontuação e critérios de julgamento](./pontuacao-julgamento.md), para que cada resultado seja interpretado por critérios estabelecidos antes da medição [[2, p. 17]](#ref-2).

---

## 6. Limitações do método nesta avaliação

1. **Sem entrevistas com os mantenedores do Excalidraw.** A aula recomenda entrevistas individuais [[1, p. 28]](#ref-1). Como não há acesso aos mantenedores, as [*abstraction sheets*](./abstraction-sheets.md) são preenchidas pela própria equipe avaliadora, que assume o ponto de vista dos interessados. As hipóteses refletem a expectativa da equipe, e não a dos interessados reais.
2. **Sem acesso ao ambiente de produção.** Disponibilidade, tolerância a falhas e recuperabilidade são observáveis principalmente com o sistema em funcionamento. Na Fase 01, ficou previsto investigá-las pela leitura do código e da configuração, com poder preditivo limitado ([modelo de qualidade](../fase-01/modelo-de-qualidade.md)). Na Fase 02, a equipe passou a medi-las também com testes controlados na aplicação construída a partir da versão avaliada e executada localmente, como descrito nas convenções de coleta de [G2](./gqm-confiabilidade.md#2-convenções-de-coleta) e de [G3](./gqm-flexibilidade.md#2-convenções-de-coleta). Os resultados mostram o comportamento do produto nesse ambiente de teste, e não o do serviço `excalidraw.com` em uso real.
3. **Versão fixa do código.** As medições sobre o código referem-se à versão de 18/10/2026. Dados que dependem do histórico do projeto, como defeitos relatados e alterações feitas ao longo do tempo, usam uma janela histórica própria: de 18/04/2026 a 18/10/2026, os seis meses que antecedem a versão avaliada, definida nas convenções de coleta de [G1](./gqm-manutenibilidade.md#2-convenções-de-coleta) e de [G2](./gqm-confiabilidade.md#2-convenções-de-coleta).

---

## Referências

> <Link id="ref-1">1.</Link> RAMOS, Cristiane Soares. **AULA 08 QSW1 GQM**. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Páginas 4, 6 a 8, 21, 22, 24, 27 a 29, 31, 33 a 35, 38 e 41 a 47. Disponível no Moodle da disciplina.
>
> <Link id="ref-2">2.</Link> RAMOS, Cristiane Soares. **AULA A07 QSW1 PROC AVAL PRODUTO**. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Páginas 4 e 15 a 19. Disponível no Moodle da disciplina.
>
> <Link id="ref-3">3.</Link> **2026-2 Trabalho final completo v1**. Especificação do trabalho final de Qualidade de Software 1, FCTE/UnB, 2026. Página 1, premissa 2. Disponível no Moodle da disciplina.
>
> <Link id="ref-4">4.</Link> BASILI, V. R.; CALDIERA, G.; ROMBACH, H. D. The Goal Question Metric Approach. In: *Encyclopedia of Software Engineering*. Wiley, 1994. Disponível em: [https://www.cs.umd.edu/~mvz/handouts/gqm.pdf](https://www.cs.umd.edu/~mvz/handouts/gqm.pdf). Acesso em: 08 nov. 2026.
>
> <Link id="ref-5">5.</Link> ISO/IEC 25010:2023. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model*.
>
> <Link id="ref-6">6.</Link> ISO/IEC 25040. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Evaluation process*.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 19/10/2026 | Criação do documento com o método GQM, os objetivos de medição e a estrutura das questões | [Christopher Paraizo](https://github.com/wChrstphr) | [Luiz Henrique Soares](https://github.com/luizh-gsoares) |
| 1.1 | 26/10/2026 | Troca dos travessões dos títulos dos objetivos, texto das questões e links para as páginas de cada objetivo, para os requisitos da Fase 01 e para as demais páginas da Fase 02, explicação dos códigos G, Q e M e da *abstraction sheet*, adaptação da revisão dos planos, limitações alinhadas aos testes em ambiente local e à janela histórica | [Christopher Paraizo](https://github.com/wChrstphr) | |
| 1.2 | 30/10/2026 | Hipóteses passam a ser uma por métrica, com uma única afirmação e regra de confirmação | [Christopher Paraizo](https://github.com/wChrstphr) | |
| 1.3 | 10/11/2026 | Introdução e metodologia sem numeração, tabelas numeradas, com título e fonte, referências numeradas e ligadas às citações, correção do conteúdo do Plano GQM, que é base para os procedimentos de coleta, e não os contém, critérios de julgamento descritos como definidos antes da medição | [Christopher Paraizo](https://github.com/wChrstphr) | |
