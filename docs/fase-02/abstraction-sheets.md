---
sidebar_position: 2
title: Abstraction Sheets dos Objetivos
description: Abstraction sheets dos objetivos de Manutenibilidade, Confiabilidade e Flexibilidade, com as métricas candidatas, as hipóteses de baseline e os fatores que podem influenciar as medições
---

# Abstraction sheets dos objetivos

Os [objetivos de medição](./estrutura-gqm.md#3-objetivos-de-medição) dizem o que se quer entender sobre o Excalidraw. Antes de escrever as questões e escolher as métricas, o GQM recomenda registrar o que as pessoas envolvidas já sabem e esperam sobre cada objetivo. A ferramenta usada para isso é a *abstraction sheet* (AULA 08, p. 28 e 29).

Esta página apresenta uma *abstraction sheet* para cada objetivo: G1 (Manutenibilidade), G2 (Confiabilidade) e G3 (Flexibilidade). As hipóteses registradas aqui são a base das hipóteses de cada questão, e os fatores de variação orientam a interpretação dos resultados nas fases seguintes.

---

## 1. Estrutura de uma abstraction sheet

O cabeçalho repete o objeto, o propósito, o foco da qualidade e o ponto de vista do objetivo. O corpo tem quatro quadrantes, preenchidos na ordem abaixo (AULA 08, p. 29):

| Ordem | Quadrante | Pergunta que responde |
| :---: | :--- | :--- |
| 1º | **Foco de qualidade** | Quais métricas são possíveis para medir o objeto em relação ao foco de qualidade? |
| 2º | **Hipóteses de baseline** | O que se sabe sobre essas métricas e quais resultados se esperam? As expectativas ficam registradas como *baseline*. |
| 3º | **Fatores de variação** | Quais fatores do ambiente podem influenciar as métricas? |
| 4º | **Impacto nas hipóteses de baseline** | Como esses fatores influenciam as medições e que dependência existe entre eles e as métricas? |

As hipóteses podem ser valores ou comparações, como "os módulos com mais defeitos" ou "o pior caso" (AULA 08, p. 31). Nesta página, cada hipótese tem uma única afirmação, ligada a uma métrica, e uma regra que diz quando ela é confirmada. Quando a equipe não tem base para estimar um valor, a hipótese é comparativa. A AULA 08 traz um exemplo preenchido para o foco de Confiabilidade (p. 30), que serviu de modelo para o formato.

---

## 2. Como as abstraction sheets foram preenchidas

A aula recomenda conduzir entrevistas individuais com a equipe do projeto avaliado (AULA 08, p. 28). Como os mantenedores do Excalidraw não estão disponíveis para entrevistas, a própria equipe avaliadora preencheu as *abstraction sheets*, assumindo o ponto de vista dos interessados de cada objetivo.

As três *abstraction sheets* foram preenchidas do zero, em conjunto, na [reunião de 19/10/2026](../gestao/atas/2026-10-19-reuniao-gqm.md) dos integrantes responsáveis pela Fase 02. A base foi a [descrição do produto](../fase-01/descricao-produto.md) e os [requisitos de avaliação](../fase-01/requisitos-avaliacao.md) da Fase 01. Cada quadrante foi discutido até ser considerado suficientemente completo (AULA 08, p. 31).

O quadrante 2º foi refeito na versão 1.1, depois da escolha das métricas, para que cada hipótese tenha uma única afirmação verificável por uma métrica. As métricas listadas no foco de qualidade são **candidatas**. A seleção final, com uma a três métricas por questão, é feita no detalhamento de cada objetivo, junto com a ficha de cada métrica ([estrutura das questões](./estrutura-gqm.md#4-estrutura-das-questões)).

---

## 3. G1 — Manutenibilidade

| Objeto | Propósito | Foco da qualidade | Ponto de vista |
| :--- | :--- | :--- | :--- |
| Código-fonte do Excalidraw (biblioteca, aplicação web e pacotes auxiliares), testes, documentação para desenvolvedores e histórico de alterações | Entender | Manutenibilidade | Mantenedores e contribuidores do projeto |

### 1º Foco de qualidade

| Subcaracterística | Métricas candidatas |
| :--- | :--- |
| Modularidade | Número de ciclos de dependência entre pacotes; número de importações que violam a direção esperada (por exemplo, a biblioteca importando código da aplicação web); acoplamento aferente e eferente de cada pacote. |
| Reusabilidade | Número de dependências de React ou do navegador nos pacotes auxiliares de matemática e utilitários; proporção de itens da interface pública da biblioteca que estão documentados. |
| Analisabilidade | Complexidade ciclomática por função; tamanho dos arquivos em linhas de código; presença de guias de contribuição e de arquitetura; ferramentas de lint, formatação e verificação de tipos executadas automaticamente. |
| Modificabilidade | Número de arquivos alterados por contribuição aceita; número de arquivos acima de um limite de tamanho ou de complexidade. |
| Testabilidade | Razão entre arquivos de teste e arquivos de produção; cobertura de testes por pacote; níveis de teste presentes (unitário, integração, ponta a ponta); execução dos testes a cada alteração proposta. |

### 2º Hipóteses de baseline

Cada hipótese tem uma única afirmação e uma regra de confirmação. O limite da regra coincide com uma fronteira das [faixas de pontuação](./pontuacao-julgamento.md#3-níveis-das-métricas-de-manutenibilidade-g1) da métrica ou vem da própria definição da métrica. São as mesmas hipóteses das questões, como a aula permite (AULA 08, p. 34), e o quadrante 4º indica o fator que justifica cada uma.

| Subcaracterística | Hipótese | Enunciado | Confirmada se o valor medido for |
| :--- | :--- | :--- | :--- |
| Modularidade | [H1.1.1](./gqm-manutenibilidade.md#3-q11--modularidade) | Não haverá ciclos de dependência entre os pacotes. | = 0 pares em ciclo |
| Modularidade | [H1.1.2](./gqm-manutenibilidade.md#3-q11--modularidade) | As importações entre pacotes seguirão a direção declarada pelo projeto. | = 0 importações em desacordo |
| Modularidade | [H1.1.3](./gqm-manutenibilidade.md#3-q11--modularidade) | A biblioteca `excalidraw` será o pacote que mais recebe dependências. | *Ca* da biblioteca > *Ca* de cada outro pacote |
| Reusabilidade | [H1.2.1](./gqm-manutenibilidade.md#4-q12--reusabilidade) | Os pacotes `math` e `utils` não dependerão de React nem do navegador. | = 0 arquivos em `math` e `utils` |
| Reusabilidade | [H1.2.2](./gqm-manutenibilidade.md#4-q12--reusabilidade) | A documentação cobrirá a maior parte das propriedades públicas, sem cobrir todas. | ≥ 80% e < 100% |
| Analisabilidade | [H1.3.1](./gqm-manutenibilidade.md#5-q13--analisabilidade) | Haverá funções de complexidade muito alta no código. | > 0% das linhas em funções com complexidade acima de 50 |
| Analisabilidade | [H1.3.2](./gqm-manutenibilidade.md#5-q13--analisabilidade) | A documentação para desenvolvedores cobrirá a contribuição e a preparação do ambiente. | tópicos (1) e (2) presentes |
| Analisabilidade | [H1.3.3](./gqm-manutenibilidade.md#5-q13--analisabilidade) | Lint, formatação e tipos serão verificados automaticamente. | = 3 de 3 |
| Modificabilidade | [H1.4.1](./gqm-manutenibilidade.md#6-q14--modificabilidade) | A maioria das contribuições alterará poucos arquivos de produção. | mediana ≤ 4 arquivos |
| Modificabilidade | [H1.4.2](./gqm-manutenibilidade.md#6-q14--modificabilidade) | Poucos arquivos de produção serão extensos. | ≤ 5% dos arquivos com mais de 1.000 linhas |
| Modificabilidade | [H1.4.3](./gqm-manutenibilidade.md#6-q14--modificabilidade) | Os arquivos extensos serão alterados com frequência. | > 10% das contribuições |
| Testabilidade | [H1.5.1](./gqm-manutenibilidade.md#7-q15--testabilidade) | A biblioteca terá cobertura de testes maior que a da aplicação web. | cobertura da biblioteca > cobertura da aplicação web |
| Testabilidade | [H1.5.2](./gqm-manutenibilidade.md#7-q15--testabilidade) | Testes unitários e de integração serão a maior parte dos arquivos de teste. | > 50% dos arquivos de teste, somados |
| Testabilidade | [H1.5.3](./gqm-manutenibilidade.md#7-q15--testabilidade) | Os testes rodarão em toda contribuição antes da integração. | ≥ 95% |

### 3º Fatores de variação

- **Modelo de contribuição aberto:** muitos contribuidores externos e um grupo pequeno de mantenedores que revisam e aprovam as alterações.
- **Ferramentas obrigatórias no fluxo de desenvolvimento:** TypeScript, lint e testes automatizados que precisam passar antes da integração.
- **Ritmo de entrega de funcionalidades:** demanda por novas funcionalidades no editor e na aplicação web.
- **Ferramenta e configuração de medição:** o que é contado como código de produção, código de teste, código gerado ou dependência externa.

### 4º Impacto nas hipóteses de baseline

- A revisão concentrada em poucos mantenedores tende a preservar a direção das dependências entre pacotes e a manter os pacotes de base livres de React e do navegador. Por isso se esperam pacotes sem ciclos, importações na direção declarada e a biblioteca no centro das dependências ([H1.1.1](./gqm-manutenibilidade.md#3-q11--modularidade), [H1.1.2](./gqm-manutenibilidade.md#3-q11--modularidade), [H1.1.3](./gqm-manutenibilidade.md#3-q11--modularidade) e [H1.2.1](./gqm-manutenibilidade.md#4-q12--reusabilidade)).
- O modelo de contribuição aberto exige que quem chega consiga preparar o ambiente e enviar uma alteração sem ajuda, o que favorece o guia de contribuição e as contribuições pequenas ([H1.3.2](./gqm-manutenibilidade.md#5-q13--analisabilidade) e [H1.4.1](./gqm-manutenibilidade.md#6-q14--modificabilidade)).
- É mais fácil acrescentar código a um componente existente do que criar um novo, o que faz os arquivos centrais crescerem e concentrarem funções complexas e alterações ([H1.3.1](./gqm-manutenibilidade.md#5-q13--analisabilidade), [H1.4.2](./gqm-manutenibilidade.md#6-q14--modificabilidade) e [H1.4.3](./gqm-manutenibilidade.md#6-q14--modificabilidade)).
- As ferramentas obrigatórias reduzem a variação de estilo e fazem lint, tipos e testes rodarem em cada contribuição, mas não reduzem a complexidade das funções. O executor de testes do projeto, o Vitest, favorece testes unitários e de integração ([H1.3.3](./gqm-manutenibilidade.md#5-q13--analisabilidade), [H1.5.2](./gqm-manutenibilidade.md#7-q15--testabilidade) e [H1.5.3](./gqm-manutenibilidade.md#7-q15--testabilidade)).
- Um ritmo alto de entregas aumenta o número de alterações nos arquivos centrais e faz a documentação da interface pública e os testes da aplicação web ficarem para trás ([H1.2.2](./gqm-manutenibilidade.md#4-q12--reusabilidade), [H1.4.3](./gqm-manutenibilidade.md#6-q14--modificabilidade) e [H1.5.1](./gqm-manutenibilidade.md#7-q15--testabilidade)).
- Tamanho, complexidade e razão de testes dependem da configuração da ferramenta. Se código gerado, testes e dependências não forem separados, os valores ficam distorcidos, o que afeta a leitura de [H1.3.1](./gqm-manutenibilidade.md#5-q13--analisabilidade), [H1.4.2](./gqm-manutenibilidade.md#6-q14--modificabilidade), [H1.5.1](./gqm-manutenibilidade.md#7-q15--testabilidade) e [H1.5.2](./gqm-manutenibilidade.md#7-q15--testabilidade). Por isso, a configuração de cada ferramenta será registrada na ficha da métrica.

---

## 4. G2 — Confiabilidade

| Objeto | Propósito | Foco da qualidade | Ponto de vista |
| :--- | :--- | :--- | :--- |
| Editor, aplicação web, mecanismos de colaboração e de salvamento no navegador e histórico de defeitos relatados | Entender | Confiabilidade | Usuários finais |

### 1º Foco de qualidade

| Subcaracterística | Métricas candidatas |
| :--- | :--- |
| Ausência de falhas | Número de defeitos relatados e corrigidos em um período; tempo até a correção de um defeito; distribuição dos defeitos por área do produto; verificações automáticas obrigatórias antes da integração. |
| Disponibilidade | Presença de *service worker* e de manifesto de aplicação instalável (PWA); proporção das funcionalidades essenciais do editor que funcionam sem conexão. |
| Tolerância a falhas | Pontos de tratamento de erro na abertura de arquivos e no carregamento de dados salvos; proporção de casos de arquivo inválido tratados com mensagem ao usuário; dependência do editor local em relação ao código de colaboração. |
| Recuperabilidade | Intervalo do salvamento automático; tipos de dado restaurados ao reabrir a aplicação; existência de rotinas que convertem arquivos de versões antigas; ações que podem ser desfeitas e refeitas. |

### 2º Hipóteses de baseline

Cada hipótese tem uma única afirmação e uma regra de confirmação. O limite da regra coincide com uma fronteira das [faixas de pontuação](./pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2) da métrica ou vem da própria definição da métrica. São as mesmas hipóteses das questões, como a aula permite (AULA 08, p. 34), e o quadrante 4º indica o fator que justifica cada uma.

| Subcaracterística | Hipótese | Enunciado | Confirmada se o valor medido for |
| :--- | :--- | :--- | :--- |
| Ausência de falhas | [H2.1.1](./gqm-confiabilidade.md#3-q21--ausência-de-falhas) | As correções serão uma parte relevante das contribuições integradas. | ≥ 20% |
| Ausência de falhas | [H2.1.2](./gqm-confiabilidade.md#3-q21--ausência-de-falhas) | Os defeitos relatados serão corrigidos em poucas semanas. | mediana ≤ 30 dias |
| Ausência de falhas | [H2.1.3](./gqm-confiabilidade.md#3-q21--ausência-de-falhas) | Toda contribuição terá revisão aprovada por outra pessoa antes da integração. | ≥ 95% |
| Disponibilidade | [H2.2.1](./gqm-confiabilidade.md#4-q22--disponibilidade) | O editor funcionará sem conexão depois do primeiro carregamento. | = 10 de 10 funções |
| Disponibilidade | [H2.2.2](./gqm-confiabilidade.md#4-q22--disponibilidade) | Nenhum serviço externo será indispensável para desenhar. | = 0 domínios indispensáveis |
| Tolerância a falhas | [H2.3.1](./gqm-confiabilidade.md#5-q23--tolerância-a-falhas) | Arquivos inválidos serão recusados com mensagem, sem travar o editor. | = 9 de 9 casos |
| Tolerância a falhas | [H2.3.2](./gqm-confiabilidade.md#5-q23--tolerância-a-falhas) | O desenho local continuará editável se a colaboração cair. | verificações 1 a 4 aprovadas |
| Recuperabilidade | [H2.4.1](./gqm-confiabilidade.md#6-q24--recuperabilidade) | O último desenho será restaurado ao reabrir a aplicação, mesmo após fechamento inesperado. | = 4 de 4 cenários |
| Recuperabilidade | [H2.4.2](./gqm-confiabilidade.md#6-q24--recuperabilidade) | Arquivos da versão atual e de versões anteriores reabrirão sem perda. | = 7 de 7 arquivos |
| Recuperabilidade | [H2.4.3](./gqm-confiabilidade.md#6-q24--recuperabilidade) | Desfazer e refazer cobrirão as ações de edição do usuário. | = 10 de 10 ações |

### 3º Fatores de variação

- **Regras de integração do repositório:** verificações automáticas e revisão exigidas antes de cada integração.
- **Navegador e suas políticas de armazenamento:** limite de espaço, navegação privada e limpeza automática de dados.
- **Condições de rede:** conexão instável ou ausente e indisponibilidade do servidor de colaboração.
- **Tamanho do desenho:** número de elementos e imagens incorporadas.
- **Forma como a comunidade registra defeitos:** relatos duplicados, sem classificação ou classificados de forma inconsistente.
- **Análise sem acesso aos servidores de produção:** a avaliação observa o código e a configuração, e não o comportamento do serviço em uso.

### 4º Impacto nas hipóteses de baseline

- As regras de integração do repositório exigem verificações automáticas e revisão antes de cada integração, por isso se espera revisão aprovada em quase toda contribuição ([H2.1.3](./gqm-confiabilidade.md#3-q21--ausência-de-falhas)).
- Em um projeto muito usado, o volume de relatos é alto, o que faz as correções serem parte relevante das contribuições e mantém os mantenedores atentos a defeitos recentes ([H2.1.1](./gqm-confiabilidade.md#3-q21--ausência-de-falhas) e [H2.1.2](./gqm-confiabilidade.md#3-q21--ausência-de-falhas)). A classificação inconsistente dos relatos pode aumentar ou reduzir essas contagens, por isso as métricas de ausência de falhas precisam de um critério explícito para decidir o que conta como defeito.
- Sem acesso à produção, disponibilidade e tolerância a falhas são avaliadas pela presença dos mecanismos e por testes controlados. O *service worker* da aplicação instalável (PWA) está configurado em `excalidraw-app/vite.config.mts`, e a abertura de arquivos acontece toda no navegador, sem servidor que filtre arquivos inválidos. Por isso se espera que o editor funcione sem conexão e trate ele mesmo os arquivos inválidos ([H2.2.1](./gqm-confiabilidade.md#4-q22--disponibilidade) e [H2.3.1](./gqm-confiabilidade.md#5-q23--tolerância-a-falhas)). Os resultados indicam capacidade, não comportamento observado em uso real.
- A colaboração é a única parte do editor que depende de um servidor. Por isso se espera que nenhum serviço externo seja indispensável para desenhar e que a queda da colaboração preserve o editor local, mas não necessariamente a sincronização, que fica fora da regra de [H2.3.2](./gqm-confiabilidade.md#5-q23--tolerância-a-falhas) ([H2.2.2](./gqm-confiabilidade.md#4-q22--disponibilidade) e [H2.3.2](./gqm-confiabilidade.md#5-q23--tolerância-a-falhas)).
- As políticas do navegador podem impedir a restauração automática mesmo com o mecanismo correto no código. A avaliação usa um navegador fixo, fora da navegação privada, e verifica a existência e o funcionamento do mecanismo, não a garantia de restauração em qualquer navegador ([H2.4.1](./gqm-confiabilidade.md#6-q24--recuperabilidade)).
- Desenhos grandes e imagens incorporadas aumentam a chance de atingir o limite de armazenamento e de falhar a reabertura de arquivos, o que afeta [H2.4.1](./gqm-confiabilidade.md#6-q24--recuperabilidade) e [H2.4.2](./gqm-confiabilidade.md#6-q24--recuperabilidade) e liga este objetivo à escalabilidade do G3. Como o formato `.excalidraw` é usado há várias versões publicadas, espera-se que o projeto mantenha a conversão de arquivos antigos e que eles reabram sem perda ([H2.4.2](./gqm-confiabilidade.md#6-q24--recuperabilidade)).
- Em uma sessão colaborativa, as alterações feitas por outros participantes podem não entrar no histórico de desfazer. Por isso [H2.4.3](./gqm-confiabilidade.md#6-q24--recuperabilidade) trata só das ações do próprio usuário, com a colaboração desligada.

---

## 5. G3 — Flexibilidade

| Objeto | Propósito | Foco da qualidade | Ponto de vista |
| :--- | :--- | :--- | :--- |
| Biblioteca `@excalidraw/excalidraw` e aplicação web, incluindo a interface pública da biblioteca, as instruções de instalação e os formatos de exportação | Entender | Flexibilidade | Desenvolvedores que integram a biblioteca e equipes de implantação e operação |

### 1º Foco de qualidade

| Subcaracterística | Métricas candidatas |
| :--- | :--- |
| Adaptabilidade | Navegadores e versões declarados como suportados; versões de React aceitas pela biblioteca; existência de instruções para frameworks com renderização no servidor; tratamento de entrada por toque e caneta. |
| Escalabilidade | Tempo para abrir, mover e exportar desenhos com quantidades crescentes de elementos, em ambiente controlado; maior desenho que pode ser aberto e salvo sem travar a aplicação. |
| Instalabilidade | Número de passos para instalar a biblioteca; pré-requisitos declarados (versões de ferramentas); sucesso na construção da imagem Docker; proporção dos passos documentados que podem ser reproduzidos sem ajustes. |
| Substituibilidade | Formatos de exportação disponíveis; existência de documentação do formato `.excalidraw`; proporção do conteúdo preservado ao exportar e reimportar. |

### 2º Hipóteses de baseline

Cada hipótese tem uma única afirmação e uma regra de confirmação. O limite da regra coincide com uma fronteira das [faixas de pontuação](./pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3) da métrica ou vem da própria definição da métrica. São as mesmas hipóteses das questões, como a aula permite (AULA 08, p. 34), e o quadrante 4º indica o fator que justifica cada uma.

| Subcaracterística | Hipótese | Enunciado | Confirmada se o valor medido for |
| :--- | :--- | :--- | :--- |
| Adaptabilidade | [H3.1.1](./gqm-flexibilidade.md#3-q31--adaptabilidade) | Os navegadores declarados cobrirão a maior parte dos usuários. | ≥ 80% |
| Adaptabilidade | [H3.1.2](./gqm-flexibilidade.md#3-q31--adaptabilidade) | A biblioteca funcionará com React 17, 18 e 19, em Vite e em Next.js. | = 6 de 6 combinações |
| Adaptabilidade | [H3.1.3](./gqm-flexibilidade.md#3-q31--adaptabilidade) | O editor aceitará toque nas ações de edição. | = 10 de 10 ações |
| Escalabilidade | [H3.2.1](./gqm-flexibilidade.md#4-q32--escalabilidade) | Um desenho de 1.000 elementos abrirá sem interromper o usuário. | ≤ 1 s na cena de 1.000 elementos |
| Escalabilidade | [H3.2.2](./gqm-flexibilidade.md#4-q32--escalabilidade) | A edição será fluida com 1.000 elementos. | ≥ 48 quadros por segundo na cena de 1.000 elementos |
| Escalabilidade | [H3.2.3](./gqm-flexibilidade.md#4-q32--escalabilidade) | Desenhos com milhares de elementos poderão ser salvos e exportados. | maior cena ≥ 5.000 elementos |
| Instalabilidade | [H3.3.1](./gqm-flexibilidade.md#5-q33--instalabilidade) | A biblioteca será instalada e removida sem erro pelos gerenciadores de pacotes. | = 9 de 9 operações |
| Instalabilidade | [H3.3.2](./gqm-flexibilidade.md#5-q33--instalabilidade) | As instruções de execução local bastarão, com as versões de ferramentas exigidas. | ≥ 95% dos passos sem ajuste |
| Instalabilidade | [H3.3.3](./gqm-flexibilidade.md#5-q33--instalabilidade) | A imagem Docker será construída e executada sem passos manuais. | = 4 de 4 verificações |
| Substituibilidade | [H3.4.1](./gqm-flexibilidade.md#6-q34--substituibilidade) | O desenho poderá ser exportado em formatos abertos. | ≥ 3 formatos |
| Substituibilidade | [H3.4.2](./gqm-flexibilidade.md#6-q34--substituibilidade) | A reimportação preservará os elementos do desenho. | ≥ 95% em cada formato |
| Substituibilidade | [H3.4.3](./gqm-flexibilidade.md#6-q34--substituibilidade) | O formato `.excalidraw` terá documentação apenas parcial. | < 60% dos campos documentados |

### 3º Fatores de variação

- **Hardware e navegador** usados nos testes de desempenho.
- **Versões das ferramentas** do ambiente de construção, como Node.js e o gerenciador de pacotes.
- **Evolução do ecossistema React** e dos empacotadores usados pelos integradores.
- **Conteúdo dos desenhos de teste:** tipos de elementos, textos e imagens incorporadas.

### 4º Impacto nas hipóteses de baseline

- Medidas de desempenho e de entrada por toque só são comparáveis quando feitas no mesmo hardware e no mesmo navegador. O ambiente de teste será fixado e registrado ([H3.1.3](./gqm-flexibilidade.md#3-q31--adaptabilidade), [H3.2.1](./gqm-flexibilidade.md#4-q32--escalabilidade) e [H3.2.2](./gqm-flexibilidade.md#4-q32--escalabilidade)).
- Uma construção pode falhar por causa da versão de uma ferramenta, e não por um problema do produto. As versões usadas serão registradas, e falhas desse tipo serão distinguidas das demais ([H3.3.1](./gqm-flexibilidade.md#5-q33--instalabilidade), [H3.3.2](./gqm-flexibilidade.md#5-q33--instalabilidade) e [H3.3.3](./gqm-flexibilidade.md#5-q33--instalabilidade)).
- Mudanças no ecossistema React e na lista de navegadores podem tornar desatualizadas as versões declaradas como compatíveis. A avaliação considera o que está declarado na versão avaliada ([H3.1.1](./gqm-flexibilidade.md#3-q31--adaptabilidade) e [H3.1.2](./gqm-flexibilidade.md#3-q31--adaptabilidade)).
- Imagens incorporadas aumentam o tamanho do desenho mais do que o número de elementos. Os desenhos de teste terão composição definida, para que o efeito de cada fator possa ser separado ([H3.2.3](./gqm-flexibilidade.md#4-q32--escalabilidade) e [H3.4.2](./gqm-flexibilidade.md#6-q34--substituibilidade)).
- Os formatos de exportação e a falta de uma especificação publicada do formato `.excalidraw` já são visíveis no repositório no commit `e1b7aac`. Por isso [H3.4.1](./gqm-flexibilidade.md#6-q34--substituibilidade) e [H3.4.3](./gqm-flexibilidade.md#6-q34--substituibilidade) se apoiam no que se vê no código, e não em um fator de variação.

---

## 6. Uso das abstraction sheets nas próximas etapas

- **Hipóteses das questões:** as hipóteses de *baseline* são as mesmas das questões da mesma subcaracterística, com os mesmos códigos ([H1.1.1](./gqm-manutenibilidade.md#3-q11--modularidade), [H1.1.2](./gqm-manutenibilidade.md#3-q11--modularidade) etc.).
- **Seleção das métricas:** as métricas candidatas são filtradas pelas características desejáveis (AULA 08, p. 41) e pela possibilidade de coleta na versão avaliada (AULA 08, p. 42).
- **Análise dos resultados:** os fatores de variação e seus impactos servem de guia para interpretar as medições (AULA 08, p. 31). Um resultado diferente do esperado é examinado à luz desses fatores antes de ser atribuído ao produto.

---

## 7. Limitações

1. **Expectativas da equipe avaliadora.** As hipóteses refletem o que a equipe espera ao assumir o ponto de vista dos interessados, e não a opinião de mantenedores, integradores ou usuários reais ([limitações do método](./estrutura-gqm.md#6-limitações-do-método-nesta-avaliação)).
2. **Conhecimento prévio limitado.** A equipe conhece o Excalidraw pela análise feita na Fase 01, e não por experiência de desenvolvimento no projeto. Por isso, os limites das regras de confirmação vêm das faixas de pontuação já definidas, e não de valores estimados pela equipe.
3. **Fatores não controláveis.** Fatores como a forma de registro de defeitos pela comunidade e as políticas dos navegadores não podem ser controlados pela equipe, apenas registrados e considerados na análise.

---

## Referências

- AULA 08 QSW1 GQM. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Páginas 28 a 31, 41 e 42.
- BASILI, V. R.; CALDIERA, G.; ROMBACH, H. D. The Goal Question Metric Approach. In: *Encyclopedia of Software Engineering*. Wiley, 1994.
- ISO/IEC 25010:2023. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model*.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 19/10/2026 | Criação das abstraction sheets dos objetivos G1, G2 e G3 | [Christopher Paraizo](https://github.com/wChrstphr) | [Luiz Henrique Soares](https://github.com/luizh-gsoares) |
| 1.1 | 30/10/2026 | Hipóteses de baseline refeitas: uma por métrica, com uma única afirmação e regra de confirmação. Impactos passam a citar as hipóteses afetadas, e G2 ganha o fator de regras de integração | [Christopher Paraizo](https://github.com/wChrstphr) | |
