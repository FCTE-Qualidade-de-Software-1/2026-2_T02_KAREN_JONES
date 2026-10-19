---
sidebar_position: 6
title: Níveis de Pontuação e Critérios de Julgamento
description: Faixas de pontuação das 36 métricas de G1, G2 e G3 e regras para interpretar os resultados, da métrica até a característica
---

# Níveis de pontuação e critérios de julgamento

As páginas de [Manutenibilidade](./gqm-manutenibilidade.md), [Confiabilidade](./gqm-confiabilidade.md) e [Flexibilidade](./gqm-flexibilidade.md) definem o que será medido. Esta página define **como cada resultado será classificado e interpretado**, para que o resultado não dependa da opinião de quem mede (AULA A07, p. 17). Ela cobre as 36 métricas dos três objetivos: 14 de G1, 10 de G2 e 12 de G3.

O caminho de interpretação tem quatro passos, do dado até a característica: a **métrica** recebe uma pontuação, a **questão** reúne as pontuações das suas métricas, a **subcaracterística** assume a nota da sua questão e a **característica** reúne as notas das suas subcaracterísticas (AULA A07, p. 16 e 17).

---

## 1. Escala de pontuação

Toda métrica é pontuada na mesma escala de 0 a 3. A pontuação mede o **nível de qualidade observado**: quanto maior, melhor.

| Pontuação | Nível | Significado |
| :---: | :--- | :--- |
| 3 | Plenamente satisfatório | O resultado atende ao que se espera de um projeto maduro nesse aspecto. |
| 2 | Satisfatório | O resultado atende, com pequenas lacunas. |
| 1 | Parcialmente satisfatório | O resultado atende só em parte e há lacunas relevantes. |
| 0 | Insatisfatório | O resultado não atende ao que se espera. |

A pontuação é independente da hipótese. A hipótese de cada questão é a resposta esperada antes da medição (AULA 08, p. 34) e é julgada à parte, na seção 4.3. Uma hipótese pode ser refutada por um resultado bom, e uma hipótese pode ser confirmada por um resultado ruim. Registrar as duas coisas separadamente mantém a pontuação comparável entre métricas.

### 1.1 Regras comuns às faixas

- **Limites inclusivos.** O limite indicado pertence à faixa em que aparece. Por exemplo, "80 a 99%" inclui 80% e 99%.
- **Arredondamento.** Percentuais são arredondados para o inteiro mais próximo antes de ser comparados com a faixa. Medianas e médias usam uma casa decimal.
- **Valor bruto sempre registrado.** Cada resultado é guardado com o valor medido, a pontuação e o nível. A pontuação resume, mas não substitui o valor.
- **Denominadores pequenos.** Quando uma métrica percentual tem até 10 itens (por exemplo, uma lista de 5 verificações), cada item que falha muda a faixa. O número de itens é registrado junto com o resultado para o leitor poder avaliar o peso de cada falha.
- **Faixas congeladas.** As faixas abaixo foram definidas antes de qualquer coleta e não são alteradas depois de a coleta começar. Uma mudança exige nova versão desta página, com justificativa no histórico de versões.

### 1.2 Faixas-padrão

Duas faixas se repetem em várias métricas e recebem um nome para simplificar as tabelas.

| Faixa | 3 | 2 | 1 | 0 | Usada quando |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **P** (padrão) | 100% | 80 a 99% | 50 a 79% | abaixo de 50% | A hipótese espera 100%: cada caso que falha é uma função que o usuário ou o integrador perde. |
| **R** (processo) | 95% ou mais | 80 a 94% | 50 a 79% | abaixo de 50% | A hipótese espera um valor próximo de 100%, mas a métrica mede prática de processo, em que pequenas exceções são normais. |

---

## 2. Como foram escolhidas as faixas

Nenhuma norma ou aula define faixas numéricas para o Excalidraw, e a literatura só fixa um limite pontual em poucos casos. Por isso a coluna **Base** das tabelas da seção 3 indica a origem de cada faixa:

- **H**: derivada da hipótese da questão ou da abstraction sheet, que já descreve o valor esperado (por exemplo, "100%", "nenhum ciclo", "poucas semanas").
- **L**: apoiada em uma referência da literatura, citada ao lado.
- **C**: convenção da equipe, escolhida para separar resultados de forma graduada quando nem a hipótese nem a literatura fixam um valor. As faixas C são o ponto mais sujeito a discussão e devem ser revisadas pela equipe antes da Fase 03.

As faixas têm quatro níveis para que cada resultado seja separado de forma graduada, e não apenas aprovado ou reprovado.

---

## 3. Níveis de pontuação por métrica

### 3.1 G1 — Manutenibilidade

#### Q1.1 — Modularidade

| Métrica | 3 | 2 | 1 | 0 | Base |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **M1.1.1** Ciclos entre pacotes (pares) | 0 | 1 | 2 a 3 | 4 ou mais | H (hipótese: nenhum ciclo); C |
| **M1.1.2** Importações contra a direção declarada | 0 | 1 a 5 | 6 a 20 | mais de 20 | H (hipótese: nenhuma violação); C |
| **M1.1.3** Violações do princípio das dependências estáveis (pacote estável que depende de um pacote mais instável, a partir de Ca, Ce e *I*) | 0 | 1 | 2 a 3 | 4 ou mais | L (Martin, 2002); C |

#### Q1.2 — Reusabilidade

| Métrica | 3 | 2 | 1 | 0 | Base |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **M1.2.1** Arquivos dependentes de React ou do navegador, pior caso entre `math` e `utils` (proporção dos arquivos de produção do pacote) | 0 arquivo | até 5% | 6 a 20% | mais de 20% | H (hipótese: nenhum em `math` e `utils`); C |
| **M1.2.2** Propriedades públicas documentadas | 90% ou mais | 75 a 89% | 50 a 74% | abaixo de 50% | C |

#### Q1.3 — Analisabilidade

| Métrica | 3 | 2 | 1 | 0 | Base |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **M1.3.1** Funções com complexidade ciclomática maior que 10 | até 5% | 6 a 10% | 11 a 20% | mais de 20% | L (limite 10: McCabe, 1976); C |
| **M1.3.2** Tópicos de documentação presentes (de 4) | 4 | 3 | 2 | 0 ou 1 | H (hipótese: ao menos os tópicos 1 e 2) |
| **M1.3.3** Verificações estáticas automáticas (de 3) | 3 | 2 | 1 | 0 | H (hipótese: 3) |

#### Q1.4 — Modificabilidade

| Métrica | 3 | 2 | 1 | 0 | Base |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **M1.4.1** Mediana de arquivos de produção por contribuição | até 3 | 4 a 5 | 6 a 10 | mais de 10 | C |
| **M1.4.2** Arquivos de produção com mais de 1.000 linhas | 0 | 1 a 5 | 6 a 15 | mais de 15 | H (hipótese: poucos arquivos); C |
| **M1.4.3** Contribuições que alteram arquivos extensos | até 10% | 11 a 25% | 26 a 50% | mais de 50% | C |

#### Q1.5 — Testabilidade

| Métrica | 3 | 2 | 1 | 0 | Base |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **M1.5.1** Cobertura de linhas do código de produção (total, com o valor de cada pacote registrado) | 80% ou mais | 60 a 79% | 40 a 59% | abaixo de 40% | C; os limites mínimos de `vitest.config.mts` são registrados como referência |
| **M1.5.2** Distribuição dos testes por nível | três níveis presentes e testes unitários e de integração somam 60% ou mais | três níveis presentes, mas unitários e de integração somam menos de 60% | dois níveis presentes | um nível ou nenhum | H (hipótese: predominam unitários e de integração); C |
| **M1.5.3** Contribuições com testes executados antes da integração | faixa R | faixa R | faixa R | faixa R | H (hipótese: 100% ou próximo); ver faixa R |

### 3.2 G2 — Confiabilidade

#### Q2.1 — Ausência de falhas

| Métrica | 3 | 2 | 1 | 0 | Base |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **M2.1.1** Correções entre as contribuições integradas | 25% ou mais | 15 a 24% | 5 a 14% | abaixo de 5% | H (hipótese: parte relevante); C. A métrica mostra o esforço dedicado a corrigir defeitos, e não quantos defeitos existem. |
| **M2.1.2** Mediana do tempo entre o relato e a correção | até 14 dias | 15 a 28 dias | 29 a 90 dias | mais de 90 dias | H (hipótese: poucas semanas); C |
| **M2.1.3** Contribuições revisadas antes da integração | faixa R | faixa R | faixa R | faixa R | H (hipótese: 100% ou próximo); ver faixa R |

#### Q2.2 — Disponibilidade

| Métrica | 3 | 2 | 1 | 0 | Base |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **M2.2.1** Funções essenciais disponíveis sem conexão | faixa P | faixa P | faixa P | faixa P | H (hipótese: 100%); ver faixa P |
| **M2.2.2** Domínios externos necessários para o editor local | nenhum indispensável e até 3 domínios | nenhum indispensável e 4 ou mais domínios | 1 indispensável | 2 ou mais indispensáveis | H (hipótese: poucos e nenhum indispensável); C |

#### Q2.3 — Tolerância a falhas

| Métrica | 3 | 2 | 1 | 0 | Base |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **M2.3.1** Arquivos inválidos tratados com mensagem | faixa P | faixa P | faixa P | faixa P | H (hipótese: 100%); ver faixa P |
| **M2.3.2** Verificações que passam quando a colaboração é interrompida | faixa P | faixa P | faixa P | faixa P | H (hipótese: verificações 1 a 4 passam); ver faixa P |

#### Q2.4 — Recuperabilidade

| Métrica | 3 | 2 | 1 | 0 | Base |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **M2.4.1** Cenários de fechamento com restauração do desenho | faixa P | faixa P | faixa P | faixa P | H (hipótese: 100%); ver faixa P |
| **M2.4.2** Arquivos reabertos sem perda | faixa P | faixa P | faixa P | faixa P | H (hipótese: 100%); ver faixa P |
| **M2.4.3** Cobertura de desfazer e refazer | faixa P | faixa P | faixa P | faixa P | H (hipótese: 100%); ver faixa P |

### 3.3 G3 — Flexibilidade

#### Q3.1 — Adaptabilidade

| Métrica | 3 | 2 | 1 | 0 | Base |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **M3.1.1** Cobertura de usuários pelos navegadores declarados | 90% ou mais | 80 a 89% | 60 a 79% | abaixo de 60% | H (hipótese: versões recentes dos principais navegadores); C |
| **M3.1.2** Ambientes de integração com sucesso (6 combinações) | faixa P | faixa P | faixa P | faixa P | H (hipótese: 6 de 6); ver faixa P |
| **M3.1.3** Ações de edição que funcionam por toque e caneta | faixa P | faixa P | faixa P | faixa P | H (hipótese: 100%); ver faixa P |

#### Q3.2 — Escalabilidade

As métricas M3.2.1 e M3.2.2 são pontuadas na cena de **1.000 elementos**, porque a hipótese da questão fixa esse ponto como o limite de uso confortável. Os valores das demais cenas (100, 5.000 e 10.000 elementos) são registrados para mostrar a forma da curva e não entram na pontuação.

| Métrica | 3 | 2 | 1 | 0 | Base |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **M3.2.1** Tempo de abertura da cena de 1.000 elementos | até 2 s | mais de 2 e até 5 s | mais de 5 e até 10 s | mais de 10 s | L (limites de tempo de resposta de Nielsen, 1993: 1 s mantém o fluxo de pensamento e 10 s é o limite da atenção); C |
| **M3.2.2** Quadros por segundo na cena de 1.000 elementos | 50 ou mais | 30 a 49 | 15 a 29 | abaixo de 15 | C |
| **M3.2.3** Maior cena salva e exportada | 10.000 elementos | 5.000 elementos | 1.000 elementos | 100 elementos ou menos | H (hipótese: desempenho cai com milhares); C |

#### Q3.3 — Instalabilidade

| Métrica | 3 | 2 | 1 | 0 | Base |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **M3.3.1** Operações de pacote bem-sucedidas | faixa P | faixa P | faixa P | faixa P | H (hipótese: 100%); ver faixa P |
| **M3.3.2** Passos documentados reproduzidos sem ajuste | faixa P | faixa P | faixa P | faixa P | H (hipótese: todos); ver faixa P |
| **M3.3.3** Implantação com Docker (verificações que passam) | faixa P | faixa P | faixa P | faixa P | H (hipótese: 100%); ver faixa P |

#### Q3.4 — Substituibilidade

| Métrica | 3 | 2 | 1 | 0 | Base |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **M3.4.1** Formatos de exportação abertos | 3 ou mais | 2 | 1 | 0 | H (hipótese: `.excalidraw`, PNG e SVG) |
| **M3.4.2** Elementos preservados na exportação e reimportação (menor valor entre os formatos que permitem reimportação) | faixa P | faixa P | faixa P | faixa P | H (a hipótese espera que PNG e SVG guardem os dados); ver faixa P |
| **M3.4.3** Campos do formato `.excalidraw` documentados | 90% ou mais | 70 a 89% | 40 a 69% | abaixo de 40% | H (hipótese: sem especificação formal publicada); C |

Nas linhas que citam a faixa P ou R, as faixas são as da seção 1.2.

---

## 4. Critérios de julgamento

### 4.1 Da métrica à questão

A pontuação de uma questão é a **média aritmética simples** das pontuações das suas métricas, com uma casa decimal. Todas as métricas têm o mesmo peso, porque as abstraction sheets não ordenam as métricas por importância e atribuir pesos sem esse critério introduziria uma escolha sem base.

Se uma métrica não puder ser coletada (por exemplo, por falta de dado ou de ferramenta), ela sai da média e o motivo é registrado. Se mais da metade das métricas de uma questão ficar sem coleta, a questão é classificada como **não avaliada**, e não recebe nota.

### 4.2 Da questão à característica

Cada questão cobre uma subcaracterística. Portanto, **a nota da subcaracterística é a nota da sua questão**. A nota da característica é a média aritmética simples das notas das suas subcaracterísticas.

Os resultados de G1, G2 e G3 são apresentados **separadamente**. Não existe nota global do Excalidraw, porque os objetivos têm propósitos e pontos de vista diferentes (mantenedores, usuários e integradores), e somá-los misturaria escalas que não se comparam.

A nota de uma questão ou de uma característica é convertida em conceito por esta tabela:

| Nota | Conceito |
| :---: | :--- |
| 2,5 a 3,0 | Atende plenamente |
| 1,5 a 2,4 | Atende |
| 0,5 a 1,4 | Atende parcialmente |
| 0,0 a 0,4 | Não atende |

**Regra de alerta.** A média pode esconder um problema grave em uma subcaracterística. Por isso, toda subcaracterística com nota **abaixo de 1,0** é destacada no relatório com o seu conceito, mesmo que a característica tenha conceito mais alto. O relatório informa também quais métricas puxaram a nota para baixo.

### 4.3 Julgamento da hipótese

Cada hipótese é julgada contra o **critério de interpretação** de cada métrica da questão, descrito nas páginas de G1, G2 e G3:

| Situação | Hipótese |
| :--- | :--- |
| Todas as métricas coletadas confirmam o critério | Confirmada |
| Pelo menos metade das métricas confirma o critério | Parcialmente confirmada |
| Menos da metade confirma o critério | Refutada |

Uma hipótese refutada não é um resultado ruim para a avaliação: ela mostra que o Excalidraw se comporta diferente do esperado, e isso é registrado com o valor medido.

### 4.4 Exemplo ilustrativo

O exemplo abaixo usa números **inventados** para mostrar o cálculo. Ele não é um resultado da avaliação.

| Passo | Cálculo | Resultado |
| :--- | :--- | :---: |
| M1.3.1 = 8% | faixa 6 a 10% | 2 |
| M1.3.2 = 3 tópicos | 3 tópicos | 2 |
| M1.3.3 = 3 verificações | 3 verificações | 3 |
| **Q1.3 (Analisabilidade)** | (2 + 2 + 3) ÷ 3 | 2,3 (Atende) |
| Outras subcaracterísticas de G1 | Q1.1 = 3,0; Q1.2 = 1,5; Q1.4 = 1,0; Q1.5 = 2,0 | |
| **G1 (Manutenibilidade)** | (3,0 + 1,5 + 2,3 + 1,0 + 2,0) ÷ 5 | 1,96, ou 2,0 (Atende) |

Nesse exemplo, Q1.4 (nota 1,0) não aciona o alerta, que exige nota abaixo de 1,0. Se ela fosse 0,9, seria destacada no relatório.

---

## 5. Limitações

1. **Faixas C são propostas da equipe.** Elas separam resultados de forma graduada, mas não vêm de um padrão externo. Por isso ficam registradas como C e foram congeladas antes da coleta.
2. **Pesos iguais.** A média simples trata todas as métricas como igualmente importantes. A Fase 03 pode decidir ponderar, mas isso exigiria uma justificativa que as abstraction sheets não dão hoje.
3. **Valores de referência de desempenho.** As faixas de M3.2.1 e M3.2.2 dependem da máquina e do navegador usados na coleta. O ambiente de medição é registrado no Plano de Medição da Fase 03 e vale para todas as cenas.
4. **Faixas por proporção em listas curtas.** A faixa P tem passos grandes quando a lista tem poucos itens (seção 1.1).

---

## Referências

- AULA 08 QSW1 GQM. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Página 34.
- AULA A07 QSW1 PROC AVAL PRODUTO. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Páginas 16 e 17.
- Especificação do trabalho final da disciplina de Qualidade de Software 1 (2026-2 Trabalho final completo v1). Página 5, critério F2-C5.
- MARTIN, R. C. *Agile Software Development: Principles, Patterns, and Practices*. Prentice Hall, 2002.
- McCABE, T. J. A Complexity Measure. *IEEE Transactions on Software Engineering*, v. SE-2, n. 4, p. 308–320, 1976.
- NIELSEN, J. *Usability Engineering*. Morgan Kaufmann, 1993. Capítulo 5, limites de tempo de resposta.
- ISO/IEC 25010:2023. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model*.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 19/10/2026 | Criação dos níveis de pontuação e dos critérios de julgamento de G1, G2 e G3 | [Luiz Henrique Soares](https://github.com/luizh-gsoares) | [Christopher Paraizo](https://github.com/wChrstphr) |
