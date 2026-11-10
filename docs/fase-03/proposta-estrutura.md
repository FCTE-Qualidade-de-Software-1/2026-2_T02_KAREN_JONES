---
title: Proposta de estrutura e organização do plano de avaliação — Fase 03
sidebar_position: 1
description: Estudo do processo de projetar a avaliação e distribuição dos planos GQM de medição e análise; issue 94.
---

# Proposta de estrutura e organização do plano de avaliação — Fase 03


## 1. Objetivo e fundamentos

A Fase 03 do processo de avaliação de produto (ISO/IEC 25040) responde à pergunta **como, com quais recursos, por quem e quando as medidas especificadas serão coletadas e analisadas?** O produto esperado é um plano que permita a um avaliador independente executar a avaliação de forma repetível e reprodutível. Por isso, a documentação deve explicitar: **método de avaliação**, **instruções ao avaliador**, **recursos e ambiente**, **massa de dados**, **cronograma**, **plano de medição** e **plano de análise**.

A proposta é desdobrar o plano em páginas especializadas, em vez de criar um único documento longo. O [Plano GQM](../fase-02/plano-gqm.md) e as fichas da Fase 02 permanecem como fonte canônica de definições, fórmulas, hipóteses e faixas. A Fase 03 acrescenta os procedimentos operacionais; não modifica retroativamente a Fase 02 para acomodar resultados observados.

### Linha de base já fixada

| Decisão consolidada | Origem | Implicação para a Fase 03 |
| :--- | :--- | :--- |
| Produto: Excalidraw, commit `e1b7aacb356a492aa1e0fc6eb57b8896124027f0`, 18/10/2026 | [Escopo da Fase 01](../fase-01/escopo-avaliacao.md) | Fazer checkout do commit em todas as medições de código e testes; documentar eventuais serviços externos. |
| Histórico de PRs/relatos: 18/04/2026 a 18/10/2026 | Convenções de coleta dos GQM | Usar a mesma janela em todas as métricas históricas que a especificam. |
| G1: Manutenibilidade, 5 questões, 14 métricas | [GQM G1](../fase-02/gqm-manutenibilidade.md) | Produzir 14 procedimentos em `instrucoes-g1-manutenibilidade.md`. |
| G2: Confiabilidade, 4 questões, 10 métricas | [GQM G2](../fase-02/gqm-confiabilidade.md) | Produzir dez procedimentos em `instrucoes-g2-confiabilidade.md`. |
| G3: Flexibilidade, 4 questões, 12 métricas | [GQM G3](../fase-02/gqm-flexibilidade.md) | Produzir 12 procedimentos em `instrucoes-g3-flexibilidade.md`. |
| Cinco níveis: `++` (5), `+` (4), `o` (3), `-` (2), `--` (1); agregação e julgamento previamente fixados | [Pontuação e julgamento](../fase-02/pontuacao-julgamento.md) | Não recalibrar faixas após a coleta; aplicar as regras já publicadas. |

**Cobertura total:** três objetivos, 13 questões e 36 métricas, conforme o [Plano GQM](../fase-02/plano-gqm.md).

## 2. Estrutura proposta em `docs/fase-03/`

| Página / artefato | Conteúdo mínimo | Issue | Responsável |
| :--- | :--- | :---: | :--- |
| `_category_.json` | Rótulo, ordem e navegação da Fase 03 no Docusaurus. | #104 | Davi Pierre |
| `visao-geral.md` | Objetivo e limites da fase, índice do plano, estado dos documentos, rastreabilidade **das 36 métricas** com definição da Fase 02, método, instrução, recurso e pontuação. | #104 | Davi Pierre |
| `metodo-avaliacao.md` | Matriz completa com ID, método, fonte, instrumento/ferramenta, justificativa técnica e relação com cada faixa de pontuação; distinguir análise estática, histórico, testes, inspeção e desempenho. | #95 | Davi Pierre |
| `recursos-ambiente.md` | Máquinas e hardware, sistema operacional, navegador, Node.js, gerenciadores, versões de ferramentas, contêiner limpo, conhecimentos exigidos, redes, gravação de tela e recursos de acessibilidade/touch/pen. | #96 | Letícia de Carvalho |
| `instrucoes-g1-manutenibilidade.md` | Procedimentos para **14 métricas** de G1, desde pré-condições e comandos até fórmula, saída esperada, dados brutos e fatores de variação. | #98 | Davi Pierre |
| `instrucoes-g2-confiabilidade.md` | Procedimentos para **10 métricas** de G2; formulários e gravações nos testes manuais, tratamento das falhas, identificação do coletor e evidências. | #99 | Letícia de Carvalho |
| `instrucoes-g3-flexibilidade.md` | Procedimentos para **12 métricas** de G3; integrações, execução local, performance, toque/caneta, Docker e exportação/importação. | #100 | Gabriel Monteiro |
| `plano-analise.md` | Processamento dos dados, fórmulas, pontuação, tratamento de ausências, arredondamento, hipóteses, gráficos/tabelas para as 13 questões e conclusões por objetivo. | #101 | Christopher Paraizo |
| `cronograma-avaliacao.md` | Marco de cada atividade, responsável por cada métrica, data de coleta, disponibilidade dos recursos, conferência, piloto, análise e folga antes da entrega. | #102 | Letícia de Carvalho |

### Artefatos de apoio ligados à Fase 03

| Local | Finalidade | Issue |
| :--- | :--- | :---: |
| `dados/fase-03/massa-de-dados/` | Cena de referência `.excalidraw`, quatro cenas de escala, entradas inválidas e README de reprodução. | #97 |
| `scripts/` | Gerador determinístico das cenas e utilitários de apoio, versionados com instruções de execução. | #97 |
| `docs/gestao/atas/` | Ata da apresentação da proposta (#94) e ata do piloto, incluindo obstáculos e correções (#103). | #94 e #103 |
| `dados/fase-04/brutos/` e `dados/fase-04/consolidados/` | Destino da coleta e da consolidação; estrutura e README operacional previstos na #110. | #110 |
| `docs/intro.md` e navegação do site | Indicação da fase atual, links publicados e rodapé. | #105 |

**Decisão de arquitetura proposta:** o **Plano de Medição** é um artefato lógico distribuído entre `metodo-avaliacao.md`, `recursos-ambiente.md`, `instrucoes-g*.md` e `cronograma-avaliacao.md`, com índice e rastreabilidade em `visao-geral.md`. O **Plano de Análise** fica concentrado em `plano-analise.md`, referenciando as regras já fixadas na Fase 02. Não duplicar fichas e tabelas inteiras da Fase 02.

## 3. Distribuição do conteúdo do Plano de Medição (GQM, Aula 08, p. 45)

| Item a definir/registrar | Página responsável | Regra para evitar ambiguidade |
| :--- | :--- | :--- |
| Objetivos, questões, hipóteses, métricas, unidades, população e fontes de dados | [Plano GQM da Fase 02](../fase-02/plano-gqm.md) e fichas G1/G2/G3, referenciados por `visao-geral.md` | A Fase 02 é a fonte de verdade; IDs e fórmulas não são alterados durante a coleta. |
| O que será observado e qual método/instrumento será utilizado | `metodo-avaliacao.md` | Uma linha por métrica, com justificativa adequada ao tipo de dado e ao limiar de pontuação. |
| Ferramentas, versões, hardware, sistema, navegador, rede e requisitos de conhecimento | `recursos-ambiente.md` | Registrar as versões exatas e o ambiente efetivamente utilizado. |
| Como coletar: passos, filtros, comandos, entradas, formulário, saída e armazenamento | `instrucoes-g1-manutenibilidade.md`, `instrucoes-g2-confiabilidade.md`, `instrucoes-g3-flexibilidade.md` | Um roteiro executável por métrica, incluindo ID, nome do arquivo bruto e fatores de variação. |
| Quem coleta, quando coleta e precedências | `cronograma-avaliacao.md` | Toda métrica recebe um responsável e uma janela de coleta. |
| Dados de referência e entradas controladas | `recursos-ambiente.md` + `dados/fase-03/massa-de-dados/` | Registrar composição, quantidade, reprodutibilidade e identidade/hash dos arquivos. |
| Conferência da aplicação dos roteiros | Piloto #103 e verificação de dados #114 | Avaliador não autor executa uma métrica por objetivo; registrar correções antes da coleta oficial. |

**Campos mínimos propostos para todo registro bruto:** ID da métrica; data/hora e fuso; coletor; objeto/commit ou janela histórica; máquina/OS; ferramenta e versão; navegador e estado da rede quando aplicável; entrada/execução; evidência (CSV/JSON/log/vídeo); valor bruto; observações/desvios. Um padrão de nome para os arquivos deve ser acordado entre as issues #98–#100 e #110 (exemplo **sujeito a aprovação**: `dados/fase-04/brutos/M1.1.1_20261110.json`).

## 4. Distribuição do Plano de Análise (GQM, Aula 08, p. 46)

| Item do plano | Documento | Especificação necessária |
| :--- | :--- | :--- |
| Entrada bruta e processamento de cada métrica | `plano-analise.md`, com referência às fichas da Fase 02 | Fonte, filtros, transformações, fórmula, escala, unidade, arredondamento e saída consolidada. |
| Pontuação de cada valor medido | [Pontuação e julgamento da Fase 02](../fase-02/pontuacao-julgamento.md), aplicada no `plano-analise.md` | `++=5`, `+=4`, `o=3`, `-=2`, `--=1`, preservando os intervalos já fixados. |
| Agregação e dados ausentes | `plano-analise.md` | Média aritmética das métricas por questão; depois média das questões por característica, sem arredondamento intermediário; em empate de 0,5, arredondar para baixo; justificar exclusões; característica inconclusiva com mais de 50% das métricas ausentes. |
| Verificação das hipóteses | `plano-analise.md`, referenciando as hipóteses individuais de G1/G2/G3 | Registrar confirmação/refutação **separadamente** do nível ordinal, usando os limiares já definidos. |
| Apresentação dos resultados | `plano-analise.md` | Tabela por métrica (bruto, valor, hipótese, nível, fonte), painel/gráfico por cada uma das 13 questões e quadro-resumo por característica. |
| Critérios finais de julgamento | `plano-analise.md` + documento de pontuação da Fase 02 | “Atende”: nível `o` ou melhor e nenhuma questão `--`; “Não atende” nos demais casos avaliáveis com nível ruim ou questão `--`; “Inconclusiva” na condição de dados ausentes. |
| Rastreabilidade e checagem independente | `visao-geral.md` + #114 | Manter o encadeamento dado bruto → métrica → questão → objetivo → conclusão e evidência verificável. |

**Não antecipar resultados na Fase 03.** O plano especifica o tratamento e a forma de apresentação antes de as métricas serem coletadas; os valores, gráficos populados e julgamentos ficam para a Fase 04.

## 5. Pendências da Fase 02 a resolver na Fase 03

| Pendência ou risco concreto | Evidência/impacto | Encaminhamento |
| :--- | :--- | :--- |
| Ambiente de teste não fixado por completo | As seções 2 de G2 e G3 remetem à Fase 03 para hardware, OS, navegador, versões e rede. | #96: registrar modelos de máquinas, CPU/RAM, OS, navegador/versão, Node.js, Yarn/npm/pnpm e os comandos de preparação. |
| Ambiente limpo reproduzível | G3 prevê testes de instalação em contêiner/VM sem pré-requisitos implícitos. | #96: fixar imagem Docker/VM, pacotes e procedimento de limpeza. |
| Dependência de hardware em desempenho | M3.2.1 e M3.2.2 variam conforme dispositivo e carga. | #96: executar ambas somente na máquina da Maria Eduarda e registrar fatores de variação. |
| Cena de referência | G2 e G3 exigem retângulo, elipse, losango, seta, linha, desenho livre, texto, texto em forma, imagem e moldura. | #97: gerar e versionar cena única reutilizável com README. |
| Cenas de escala para desempenho | G3 especifica 100, 1.000, 5.000 e 10.000 elementos, em proporção 40/20/20/20. | #97: gerar de modo determinístico; guardar script, sementes, arquivos e composição. |
| Casos inválidos e formatos antigos | M2.3.1 e M2.4.2 exigem entradas controladas e identificáveis. | #97 e #99: catalogar entradas inválidas; #99 documentar origem e seleção de arquivos antigos. |
| Versões e parâmetros de ferramentas de inspeção | Comparabilidade de Madge, ESLint, cloc, Vitest/cobertura, API GitHub, navegadores e utilitários de medição. | #95 define método e #96 fixa ferramenta/versão/comandos. |
| Gravações e avaliação humana | Testes G2/G3 podem depender de interpretação de mensagens, restauração e sucesso da ação. | #96 define gravador; #99/#100 fornecem roteiro, formulário, vídeo e critério de aceitação; #114 verifica. |
| Dispositivo para toque e caneta | M3.1.3 demanda hardware e modelo registrados, não apenas simulação por mouse. | #96 fixa dispositivo; #100 define ações testadas e evidências. |
| Nomes/formatos dos dados e evidências | #98/#99/#100 requerem arquivos brutos rastreáveis; #110 organizará as pastas. | Alinhar convenção única, formatos e metadados antes da primeira coleta. |
| Reprodutibilidade dos procedimentos | Nenhum procedimento da Fase 03 foi testado ainda por avaliador independente. | #103 realiza piloto das três características e documenta correções antes da #110/#111–#113. |


## 6. Responsabilidades, dependências e cronograma de alto nível

| Data prevista | Atividade | Responsável / issue |
| :--- | :--- | :--- |
| 05/11/2026 | Apresentar e aprovar a arquitetura documental; registrar ata. | Davi Pierre — #94 |
| 05/11/2026 | Fixar recursos e máquinas de avaliação. | Letícia — #96 |
| 06/11/2026 | Definir método de todas as 36 métricas; massa de dados; plano de análise; cronograma. | Davi — #95; Gabriel — #97; Christopher — #101; Letícia — #102 |
| 07/11/2026 | Concluir procedimentos detalhados G1, G2, G3. | Davi — #98; Letícia — #99; Gabriel — #100 |
| 08/11/2026 | Piloto cruzado, visão geral/rastreabilidade, site e preparação da coleta. | Maria Eduarda — #103; Davi — #104; Gabriel — #105; Luiz — #110 |
| 10 a 12/11/2026 | Executar coleta G1, G2 e G3. | Christopher — #111; Luiz — #112; Maria Eduarda — #113 |
| 13/11/2026 | Conferir dados brutos, calcular consolidações e verificar evidências. | Davi — #114 |
| Até 15/11/2026 | Analisar medidas, preparar gráficos e apresentação. | Equipe — Fase 04 e PC2 |

**Dependência crítica:** #94 → #95 → #98/#99/#100 → #103 → coleta da Fase 04. Em paralelo: #96 (ambiente), #97 (massa de dados) e #101 (análise). A #104 depende das páginas efetivas de #95–#102 e consolida a rastreabilidade; não deve ser antecipada com links inexistentes.

## 7. Verificações de consistência e repetibilidade

Antes de aprovar cada documento da Fase 03, conferir:

1. Os **36 IDs** correspondem exatamente às fichas da Fase 02, sem métrica nova ou omitida.
2. Para cada métrica há fonte, fórmula/unidade, método, ferramenta/versão, procedimento, responsável, data, arquivo bruto e evidência.
3. As faixas, regras de agregação e hipóteses **não** são alteradas após observar resultados.
4. Regras de amostragem, exclusões e recortes históricos são explícitas; o commit avaliado é único.
5. Testes manuais possuem critérios observáveis e gravações; medições de desempenho usam máquina e condições fixas.
6. Uma pessoa que não redigiu as instruções consegue executar o piloto sem orientação verbal adicional; divergências geram revisão documentada.
7. `docs/fase-03/visao-geral.md` contém links válidos para cada ficha da Fase 02, procedimento, recurso, método e pontuação.


## Referências

- [Fase 01 — Escopo, profundidade e objetos](../fase-01/escopo-avaliacao.md).
- [Fase 02 — Visão geral](../fase-02/visao-geral.md).
- [Fase 02 — Plano GQM](../fase-02/plano-gqm.md).
- [Fase 02 — GQM de Manutenibilidade](../fase-02/gqm-manutenibilidade.md).
- [Fase 02 — GQM de Confiabilidade](../fase-02/gqm-confiabilidade.md).
- [Fase 02 — GQM de Flexibilidade](../fase-02/gqm-flexibilidade.md).
- [Fase 02 — Níveis de pontuação e critérios de julgamento](../fase-02/pontuacao-julgamento.md).
- *AULA A07 QSW1 PROC AVAL PRODUTO.pdf*, p. 15, 18–19 (conforme referências da issue #94).
- *AULA 08 QSW1 GQM.pdf*, p. 45–46 e 50 (conforme referências das issues #94 e #103).
- *2026-2 Trabalho final completo v1.pdf*, p. 7, critérios F3-C1 e F3-C8.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 05/11/2026 | Proposta inicial de estrutura, distribuição dos planos GQM e pendências operacionais da Fase 03 | [Davi Pierre](https://github.com/DaviPierre) |  |

