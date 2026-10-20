---
sidebar_position: 1
title: Método GQM e Objetivos de Medição
description: Como o método GQM é aplicado na especificação da avaliação do Excalidraw e quais objetivos de medição derivam das prioridades da Fase 01
---

# Método GQM e objetivos de medição

A avaliação do Excalidraw segue o processo da ISO/IEC 25040, organizado em quatro fases: estabelecer os requisitos da avaliação, especificar a avaliação, projetar a avaliação e executá-la. A Fase 01 definiu por que avaliar, o que avaliar e quais características de qualidade priorizar.

A Fase 02, descrita aqui, especifica a avaliação: define o que será medido em cada parte do produto, com detalhe suficiente para que outra pessoa possa repetir a avaliação e chegar aos mesmos resultados (AULA A07, p. 15). Nela, as subcaracterísticas escolhidas na Fase 01 são desdobradas em atributos que possam ser medidos e pontuados (AULA A07, p. 16), e são definidos os critérios para interpretar as medições (AULA A07, p. 17).

Para fazer esse desdobramento, a avaliação usa o método *Goal–Question–Metric* (GQM). Esta página resume o método, mostra como ele foi adaptado ao contexto da avaliação e apresenta os três objetivos de medição que guiam o restante da Fase 02.

---

## 1. O que é o GQM

O GQM foi proposto por Victor Basili e parte de um princípio simples: **mede-se para algum fim** (AULA 08, p. 6). Em vez de começar pela lista de métricas disponíveis, começa-se pelo objetivo da medição e só então se decide o que coletar. A estrutura tem três níveis (AULA 08, p. 8):

| Nível | Elemento | Papel nesta avaliação |
| :--- | :--- | :--- |
| Conceitual | **Objetivo** (*Goal*) | O que se quer entender sobre o Excalidraw, sob qual foco de qualidade e do ponto de vista de quem. |
| Operacional | **Questão** (*Question*) | Perguntas cujas respostas dizem se o objetivo foi atendido. Para cada questão, elabora-se uma hipótese, que é a resposta esperada (AULA 08, p. 34). |
| Quantitativo | **Métrica** (*Metric*) | Dados coletados para responder cada questão de forma objetiva. |

A interpretação percorre o caminho inverso: as métricas respondem às questões, e as respostas às questões dizem se o objetivo foi alcançado (AULA 08, p. 7).

A aula admite questões sem hipótese quando não for possível formulá-la (AULA 08, p. 31). Nesta avaliação, todas as questões terão hipótese, para que cada resultado possa ser comparado com uma expectativa definida antes da medição.

---

## 2. Como as etapas do GQM foram adaptadas

A aula apresenta oito etapas para a definição do GQM (AULA 08, p. 21). A tabela mostra como cada uma é aplicada nesta avaliação e em que fase o resultado é entregue.

| Etapa (AULA 08, p. 21) | Como é aplicada | Fase |
| :--- | :--- | :---: |
| Definir objetivos de medição (p. 22 e 24) | Um objetivo por característica selecionada, no template da aula (seção 3 desta página). | 02 |
| Rever ou produzir modelos de processo (p. 27) | Na aula, essa etapa analisa o processo de desenvolvimento para ver onde as medições podem ser feitas. Como aqui o objeto medido é um produto, esse papel é cumprido pela [descrição do produto](../fase-01/descricao-produto.md) e pelas partes do Excalidraw delimitadas no [escopo](../fase-01/escopo-avaliacao.md). | 02 |
| Conduzir entrevistas GQM (p. 28) | Os mantenedores do Excalidraw não estão disponíveis para entrevistas. A equipe avaliadora preenche, em reunião, uma *abstraction sheet* por objetivo, assumindo o ponto de vista dos interessados mapeados na Fase 01 (ver limitações na seção 6). | 02 |
| Definir e rever questões e hipóteses (p. 33 a 35) | Uma questão por subcaracterística, reunindo os requisitos de avaliação da Fase 01 (seção 4). Cada questão recebe uma hipótese. | 02 |
| Definir métricas (p. 38) | Métricas documentadas em uma ficha padronizada (seção 5), escolhidas pelas características desejáveis apresentadas na p. 41. | 02 |
| Verificar métricas (p. 42) | Conferir se cada métrica pode ser coletada na versão avaliada do código, com as ferramentas disponíveis. | 02 |
| Produzir planos (p. 43 a 46) | Plano GQM na Fase 02. Plano de Medição e Plano de Análise na Fase 03, junto com o plano de avaliação (AULA A07, p. 18 e 19). | 02 e 03 |
| Rever planos (p. 47) | Cada artefato é revisado por outro integrante da equipe antes de ser publicado. | 02 e 03 |

### Divisão entre as Fases 02 e 03

| Artefato | Conteúdo (AULA 08) | Fase |
| :--- | :--- | :---: |
| **Plano GQM** | Objetivos, questões, métricas e hipóteses; diretrizes de interpretação; definição dos procedimentos de coleta (p. 44). | 02 |
| *Abstraction sheets* | Foco de qualidade, fatores de variação, hipóteses de *baseline* e impacto dos fatores (p. 29). | 02 |
| Níveis de pontuação e critérios de julgamento | Como cada resultado de medição é classificado (AULA A07, p. 17). | 02 |
| **Plano de Medição** | Faixas de valores, responsável, momento, meio e ferramenta de coleta de cada métrica (p. 45). | 03 |
| **Plano de Análise** | Processamento dos dados, forma de apresentação e comparação com as hipóteses (p. 46). | 03 |

A aula inclui no Plano GQM a definição dos procedimentos de coleta e a elaboração dos planos de medição e de análise (AULA 08, p. 44). Na Fase 02, o procedimento de coleta de cada métrica já é registrado na ficha da métrica (seção 5). O detalhamento operacional (responsável, momento, ferramentas e formulários) fica para o Plano de Medição, e a simulação da interpretação, para o Plano de Análise. Os dois são produzidos na Fase 03, que é quando o processo da ISO/IEC 25040 elabora o plano de avaliação (AULA A07, p. 18 e 19).

---

## 3. Objetivos de medição

Os objetivos seguem o template da aula (AULA 08, p. 24). Cada um corresponde a uma característica selecionada na [priorização](../fase-01/priorizacao-caracteristicas.md), e o ponto de vista é o dos interessados para os quais a característica é prioridade principal na [matriz de prioridades](../fase-01/interessados.md#matriz-de-prioridades).

No template da aula, o ponto de vista é o da pessoa que mede o objeto, ou seja, quem deseja a avaliação (AULA 08, p. 24). Nesta avaliação não há um cliente externo: a própria equipe solicita e executa a avaliação, atuando como uma equipe de garantia da qualidade independente do projeto Excalidraw. Se o ponto de vista fosse o da equipe, os três objetivos teriam o mesmo ponto de vista e não mostrariam para quem cada característica importa. Por isso, a equipe mede, mas adota o ponto de vista dos interessados mapeados na Fase 01. Assim, o foco de qualidade e o ponto de vista de cada objetivo derivam diretamente das prioridades da Fase 01.

O propósito escolhido é **entender**. A equipe não mantém o Excalidraw e não pode alterar o produto, então mede para caracterizá-lo. Essa caracterização serve ao objetivo da avaliação definido no [propósito](../fase-01/proposito-avaliacao.md), que é indicar pontos para melhoria no produto. As ações de melhoria ficam para a Fase 04.

O contexto é o mesmo nos três objetivos: o código-fonte público do Excalidraw na versão de 18/10/2026, identificada no [escopo](../fase-01/escopo-avaliacao.md), analisado sem execução em ambiente de produção.

### G1 — Manutenibilidade

| Campo do template | Valor |
| :--- | :--- |
| Analisar | o código-fonte do Excalidraw (biblioteca, aplicação web e pacotes auxiliares), seus testes, sua documentação para desenvolvedores e o histórico público de alterações |
| para o propósito de | entender |
| com respeito a | Manutenibilidade: modularidade, reusabilidade, analisabilidade, modificabilidade e testabilidade |
| do ponto de vista de | mantenedores e contribuidores do projeto |
| no contexto de | código-fonte público na versão de 18/10/2026, avaliado por equipe independente |

**Origem na Fase 01:** ênfase 4 e prioridade 12 (impacto × risco). É prioridade principal para desenvolvedores, mantenedores, contribuidores e equipes de qualidade.

### G2 — Confiabilidade

| Campo do template | Valor |
| :--- | :--- |
| Analisar | o editor, a aplicação web e os mecanismos de colaboração e de salvamento no navegador, além do histórico público de defeitos relatados |
| para o propósito de | entender |
| com respeito a | Confiabilidade: ausência de falhas (Maturidade, na edição de 2011), disponibilidade, tolerância a falhas e recuperabilidade |
| do ponto de vista de | usuários finais |
| no contexto de | código-fonte público na versão de 18/10/2026, avaliado por equipe independente, sem acesso aos servidores de produção |

**Origem na Fase 01:** ênfase 4 e maior prioridade da seleção (16). É prioridade principal para usuários finais, mantenedores e equipes de qualidade. O ponto de vista é o do usuário final porque é quem perde trabalho quando a confiabilidade falha.

### G3 — Flexibilidade (antiga Portabilidade)

Na ISO/IEC 25010:2023, adotada desde a Fase 01, a Portabilidade da edição de 2011 passou a se chamar Flexibilidade e ganhou a subcaracterística Escalabilidade. As demais (adaptabilidade, instalabilidade e substituibilidade) continuam as mesmas.

| Campo do template | Valor |
| :--- | :--- |
| Analisar | a biblioteca `@excalidraw/excalidraw` e a aplicação web, incluindo a interface pública da biblioteca, as instruções de instalação e os formatos de exportação |
| para o propósito de | entender |
| com respeito a | Flexibilidade: adaptabilidade, escalabilidade, instalabilidade e substituibilidade |
| do ponto de vista de | desenvolvedores que integram a biblioteca em seus sistemas e equipes de implantação e operação |
| no contexto de | código-fonte público na versão de 18/10/2026, avaliado por equipe independente |

**Origem na Fase 01:** ênfase 3 e prioridade 9. É prioridade principal para integradores e equipes de operação, grupos que as outras duas características atendem pouco.

---

## 4. Estrutura das questões

Cada objetivo terá **uma questão por subcaracterística**, porque as subcaracterísticas são os atributos que compõem o foco de qualidade de cada objetivo. Cada questão reúne os [requisitos de avaliação](../fase-01/requisitos-avaliacao.md) da Fase 01 ligados à mesma subcaracterística, de modo que toda questão pode ser rastreada até um requisito. A redação final das questões e de suas hipóteses será apresentada no Plano GQM.

| Objetivo | Questão | Subcaracterística | Requisitos de avaliação reunidos |
| :--- | :--- | :--- | :--- |
| G1 | Q1.1 | Modularidade | RQ-MAN-01 a RQ-MAN-03 |
| G1 | Q1.2 | Reusabilidade | RQ-MAN-04 e RQ-MAN-05 |
| G1 | Q1.3 | Analisabilidade | RQ-MAN-06 a RQ-MAN-08 |
| G1 | Q1.4 | Modificabilidade | RQ-MAN-09 e RQ-MAN-10 |
| G1 | Q1.5 | Testabilidade | RQ-MAN-11 a RQ-MAN-13 |
| G2 | Q2.1 | Ausência de falhas (Maturidade, na edição de 2011) | RQ-CONF-01 e RQ-CONF-02 |
| G2 | Q2.2 | Disponibilidade | RQ-CONF-03 e RQ-CONF-04 |
| G2 | Q2.3 | Tolerância a falhas | RQ-CONF-05 a RQ-CONF-07 |
| G2 | Q2.4 | Recuperabilidade | RQ-CONF-08 a RQ-CONF-11 |
| G3 | Q3.1 | Adaptabilidade | RQ-FLEX-01 a RQ-FLEX-04 |
| G3 | Q3.2 | Escalabilidade | RQ-FLEX-05 e RQ-FLEX-06 |
| G3 | Q3.3 | Instalabilidade | RQ-FLEX-07 a RQ-FLEX-10 |
| G3 | Q3.4 | Substituibilidade | RQ-FLEX-11 e RQ-FLEX-12 |

Ao todo, são 3 objetivos, 13 questões e 36 requisitos de avaliação. Para manter a avaliação viável, a meta é de **uma a três métricas por questão**. Uma questão não deve ser apenas uma métrica escrita em forma de pergunta: ela precisa caracterizar o objeto em relação ao foco de qualidade, e as métricas é que a respondem (AULA 08, p. 33 e 34).

Antes de seguir para as métricas, cada questão passa pela revisão proposta na aula: respondendo a questão, é possível concluir algo sobre o objetivo? A hipótese ajuda a analisar o resultado? (AULA 08, p. 35).

---

## 5. Ficha de cada métrica

Cada métrica será documentada com os campos abaixo. Os cinco primeiros garantem que qualquer pessoa consiga calcular a métrica e interpretar o resultado da mesma forma. Os dois últimos ligam a métrica à questão que ela responde e justificam sua escolha.

| Campo | Descrição | Fonte |
| :--- | :--- | :--- |
| Definição | O que a métrica mede, sem ambiguidade. | AULA 08, p. 4 |
| Procedimento de cálculo | Fórmula, unidade e escala. | Especificação do trabalho, p. 1 |
| Fonte dos dados | Parte do produto e artefato de onde o dado sai. | Especificação do trabalho, p. 1 |
| Procedimento de coleta | Como o dado é obtido: ferramenta, comando ou inspeção. | Especificação do trabalho, p. 1 |
| Critério de interpretação | Como o valor é lido em relação à hipótese da questão. | Especificação do trabalho, p. 1 |
| Questão respondida | Identificador da questão (ex.: Q1.1). | AULA 08, p. 38 |
| Características desejáveis | Justificativa de simplicidade, consistência e objetividade, facilidade de coleta, robustez, validade e independência da linguagem de programação. | AULA 08, p. 41 |

Depois das fichas, serão definidos os níveis de pontuação e os critérios de julgamento de todas as métricas, para que cada resultado possa ser classificado sem depender da opinião de quem mede (AULA A07, p. 17).

---

## 6. Limitações do método nesta avaliação

1. **Sem entrevistas com os mantenedores do Excalidraw.** A aula recomenda entrevistas individuais (AULA 08, p. 28). Como não há acesso aos mantenedores, as *abstraction sheets* são preenchidas pela própria equipe avaliadora, que assume o ponto de vista dos interessados. As hipóteses refletem a expectativa da equipe, e não a dos interessados reais.
2. **Análise predominantemente estática.** Disponibilidade, tolerância a falhas e recuperabilidade são observáveis principalmente com o sistema em funcionamento. Na Fase 01 ficou definido que elas serão investigadas pela leitura do código e da configuração, com poder preditivo limitado ([modelo de qualidade](../fase-01/modelo-de-qualidade.md)).
3. **Versão fixa do código.** As medições sobre o código referem-se à versão de 18/10/2026. Dados que dependem do histórico do projeto, como defeitos relatados e alterações feitas ao longo do tempo, precisam de um período de análise próprio, que será definido no Plano de Medição.

---

## Referências

- AULA 08 QSW1 GQM. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Páginas 4, 6 a 8, 21, 22, 24, 27 a 29, 31, 33 a 35, 38, 41 a 47.
- AULA A07 QSW1 PROC AVAL PRODUTO. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Páginas 15 a 19.
- Especificação do trabalho final da disciplina de Qualidade de Software 1 (2026-2 Trabalho final completo v1). Página 1, premissa 2.
- BASILI, V. R.; CALDIERA, G.; ROMBACH, H. D. The Goal Question Metric Approach. In: *Encyclopedia of Software Engineering*. Wiley, 1994.
- ISO/IEC 25010:2023. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model*.
- ISO/IEC 25040. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Evaluation process*.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 19/10/2026 | Criação do documento com o método GQM, os objetivos de medição e a estrutura das questões | [Christopher Paraizo](https://github.com/wChrstphr) | [Luiz Henrique Soares](https://github.com/luizh-gsoares) |
