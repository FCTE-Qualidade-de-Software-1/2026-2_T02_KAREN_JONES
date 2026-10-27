---
sidebar_position: 2
title: Abstraction Sheets dos Objetivos
description: Abstraction sheets dos objetivos de Manutenibilidade, Confiabilidade e Flexibilidade, com as métricas candidatas, as hipóteses de baseline e os fatores que podem influenciar as medições
---

# Abstraction sheets dos objetivos

Os [objetivos de medição](./estrutura-gqm.md#3-objetivos-de-medição) dizem o que se quer entender sobre o Excalidraw. Antes de escrever as questões e escolher as métricas, o GQM recomenda registrar o que as pessoas envolvidas já sabem e esperam sobre cada objetivo. A ferramenta usada para isso é a *abstraction sheet* (AULA 08, p. 28 e 29).

Esta página apresenta uma *abstraction sheet* para cada objetivo: [G1](./estrutura-gqm.md#g1-manutenibilidade) (Manutenibilidade), [G2](./estrutura-gqm.md#g2-confiabilidade) (Confiabilidade) e [G3](./estrutura-gqm.md#g3-flexibilidade-antiga-portabilidade) (Flexibilidade). As hipóteses registradas aqui são a base das hipóteses de cada questão, e os fatores de variação orientam a interpretação dos resultados nas fases seguintes. As questões, hipóteses e métricas que saíram delas estão nas páginas de [G1](./gqm-manutenibilidade.md), [G2](./gqm-confiabilidade.md) e [G3](./gqm-flexibilidade.md).

---

## 1. Estrutura de uma abstraction sheet

O cabeçalho repete o objeto, o propósito, o foco da qualidade e o ponto de vista do objetivo. O corpo tem quatro quadrantes, preenchidos na ordem abaixo (AULA 08, p. 29):

| Ordem | Quadrante | Pergunta que responde |
| :---: | :--- | :--- |
| 1º | **Foco de qualidade** | Quais métricas são possíveis para medir o objeto em relação ao foco de qualidade? |
| 2º | **Hipóteses de baseline** | O que se sabe sobre essas métricas e quais resultados se esperam? As expectativas ficam registradas como *baseline*. |
| 3º | **Fatores de variação** | Quais fatores do ambiente podem influenciar as métricas? |
| 4º | **Impacto nas hipóteses de baseline** | Como esses fatores influenciam as medições e que dependência existe entre eles e as métricas? |

As hipóteses podem ser valores individuais ou ideias comparativas, como "os X mais" ou "os piores" (AULA 08, p. 31). Nesta página, as hipóteses são comparativas sempre que a equipe não tem base para estimar um valor antes da medição. A AULA 08 traz um exemplo preenchido para o foco de Confiabilidade (p. 30), com hipóteses dos dois tipos: uma distribuição de falhas em percentuais e a ordem dos módulos que terão mais defeitos. Esse exemplo serviu de modelo para o formato.

---

## 2. Como as abstraction sheets foram preenchidas

A aula recomenda conduzir entrevistas individuais com a equipe do projeto avaliado (AULA 08, p. 28). Como os mantenedores do Excalidraw não estão disponíveis para entrevistas, a própria equipe avaliadora preencheu as *abstraction sheets*, assumindo o ponto de vista dos interessados de cada objetivo.

As três *abstraction sheets* foram preenchidas do zero, em conjunto, na [reunião de 19/10/2026](../gestao/atas/2026-10-19-reuniao-gqm.md) dos integrantes responsáveis pela Fase 02. A base foi a [descrição do produto](../fase-01/descricao-produto.md) e os [requisitos de avaliação](../fase-01/requisitos-avaliacao.md) da Fase 01. Cada quadrante foi discutido até ser considerado suficientemente completo (AULA 08, p. 31).

As métricas listadas no foco de qualidade são **candidatas**. A seleção final, com uma a três métricas por questão ([estrutura das questões](./estrutura-gqm.md#4-estrutura-das-questões)), é feita no detalhamento de cada objetivo, junto com a ficha de cada métrica, nas páginas de [G1](./gqm-manutenibilidade.md), [G2](./gqm-confiabilidade.md) e [G3](./gqm-flexibilidade.md). As diferenças entre o que foi registrado aqui e o que foi detalhado nessas páginas estão na [seção 7](#7-ajustes-feitos-no-detalhamento-do-gqm).

---

## 3. G1: Manutenibilidade

| Objeto | Propósito | Foco da qualidade | Ponto de vista |
| :--- | :--- | :--- | :--- |
| Código-fonte do Excalidraw (biblioteca, aplicação web e pacotes auxiliares), testes, documentação para desenvolvedores e histórico de alterações | Entender | [Manutenibilidade](../fase-01/modelo-de-qualidade.md#manutenabilidade) | Mantenedores e contribuidores do projeto |

### 1º Foco de qualidade

| Subcaracterística | Métricas candidatas |
| :--- | :--- |
| Modularidade | Número de ciclos de dependência entre pacotes; número de importações que violam a direção esperada (por exemplo, a biblioteca importando código da aplicação web); acoplamento aferente e eferente de cada pacote. |
| Reusabilidade | Número de dependências de React ou do navegador nos pacotes auxiliares de matemática e utilitários; proporção de itens da interface pública da biblioteca que estão documentados. |
| Analisabilidade | Complexidade ciclomática por função; tamanho dos arquivos em linhas de código; presença de guias de contribuição e de arquitetura; ferramentas de lint, formatação e verificação de tipos executadas automaticamente. |
| Modificabilidade | Número de arquivos alterados por contribuição aceita; número de arquivos acima de um limite de tamanho ou de complexidade. |
| Testabilidade | Razão entre arquivos de teste e arquivos de produção; cobertura de testes por pacote; níveis de teste presentes (unitário, integração, ponta a ponta); execução dos testes a cada alteração proposta. |

### 2º Hipóteses de baseline

- **Modularidade:** não há ciclos de dependência entre os pacotes, e a biblioteca não importa código da aplicação web. O pacote da biblioteca é o que mais recebe dependências dos demais.
- **Reusabilidade:** os pacotes de matemática e utilitários não dependem de React nem de recursos do navegador e podem ser usados isoladamente. A interface pública da biblioteca é documentada, mas parte das opções avançadas só é descrita nos tipos do código.
- **Analisabilidade:** a maior parte das funções tem complexidade baixa, mas a complexidade e o tamanho se concentram em poucos arquivos. O componente principal do editor deve ser o arquivo mais extenso e complexo do projeto. Lint, formatação e verificação de tipos são executados automaticamente.
- **Modificabilidade:** a maioria das contribuições altera poucos arquivos. Os arquivos mais extensos são também os mais alterados, o que torna as mudanças neles mais arriscadas.
- **Testabilidade:** a lógica da biblioteca tem mais testes do que a aplicação web. Predominam testes unitários e de integração, e os testes rodam em toda alteração proposta.

### 3º Fatores de variação

- **Modelo de contribuição aberto:** muitos contribuidores externos e um grupo pequeno de mantenedores que revisam e aprovam as alterações.
- **Ferramentas obrigatórias no fluxo de desenvolvimento:** TypeScript, lint e testes automatizados que precisam passar antes da integração.
- **Ritmo de entrega de funcionalidades:** demanda por novas funcionalidades no editor e na aplicação web.
- **Ferramenta e configuração de medição:** o que é contado como código de produção, código de teste, código gerado ou dependência externa.

### 4º Impacto nas hipóteses de baseline

- A revisão concentrada em poucos mantenedores tende a preservar a direção das dependências entre pacotes, tornando ciclos raros. Por outro lado, é mais fácil acrescentar código a um componente existente do que criar um novo, o que faz os arquivos centrais crescerem.
- As ferramentas obrigatórias reduzem a variação de estilo e melhoram a analisabilidade, mas não reduzem a complexidade das funções.
- Um ritmo alto de entregas aumenta o número de alterações nos arquivos centrais e pode reduzir a proporção de código coberto por testes.
- Tamanho, complexidade e razão de testes dependem da configuração da ferramenta. Se código gerado, testes e dependências não forem separados, os valores ficam distorcidos. Por isso, a configuração de cada ferramenta será registrada na ficha da métrica.

---

## 4. G2: Confiabilidade

| Objeto | Propósito | Foco da qualidade | Ponto de vista |
| :--- | :--- | :--- | :--- |
| Editor, aplicação web, mecanismos de colaboração e de salvamento no navegador e histórico de defeitos relatados | Entender | [Confiabilidade](../fase-01/modelo-de-qualidade.md#confiabilidade) | Usuários finais |

### 1º Foco de qualidade

| Subcaracterística | Métricas candidatas |
| :--- | :--- |
| Ausência de falhas | Número de defeitos relatados e corrigidos em um período; tempo até a correção de um defeito; distribuição dos defeitos por área do produto; verificações automáticas obrigatórias antes da integração. |
| Disponibilidade | Presença de *service worker* e de manifesto de aplicação instalável (PWA); proporção das funcionalidades essenciais do editor que funcionam sem conexão. |
| Tolerância a falhas | Pontos de tratamento de erro na abertura de arquivos e no carregamento de dados salvos; proporção de casos de arquivo inválido tratados com mensagem ao usuário; dependência do editor local em relação ao código de colaboração. |
| Recuperabilidade | Intervalo do salvamento automático; tipos de dado restaurados ao reabrir a aplicação; existência de rotinas que convertem arquivos de versões antigas; ações que podem ser desfeitas e refeitas. |

### 2º Hipóteses de baseline

- **Ausência de falhas:** o volume de defeitos relatados é alto, compatível com um projeto muito usado, e a maior parte dos defeitos corrigidos é fechada em poucas semanas. Colaboração, edição de texto e exportação concentram mais defeitos do que o desenho de formas básicas. Toda alteração proposta passa por verificações automáticas.
- **Disponibilidade:** depois do primeiro carregamento, o editor funciona sem conexão. A colaboração em tempo real e o compartilhamento por link não funcionam sem conexão.
- **Tolerância a falhas:** arquivos inválidos ou corrompidos são recusados com uma mensagem, sem travar o editor. Se a sessão de colaboração cair, o desenho local continua editável.
- **Recuperabilidade:** ao reabrir a aplicação, o último desenho é restaurado do armazenamento do navegador. Arquivos de versões antigas abrem nas versões atuais. Desfazer e refazer cobrem as ações de edição do próprio usuário, mas não necessariamente as alterações feitas por outros participantes da colaboração.

### 3º Fatores de variação

- **Navegador e suas políticas de armazenamento:** limite de espaço, navegação privada e limpeza automática de dados.
- **Condições de rede:** conexão instável ou ausente e indisponibilidade do servidor de colaboração.
- **Tamanho do desenho:** número de elementos e imagens incorporadas.
- **Forma como a comunidade registra defeitos:** relatos duplicados, sem classificação ou classificados de forma inconsistente.
- **Análise sem acesso aos servidores de produção:** a avaliação observa o código, a configuração e a aplicação executada em ambiente de teste local, e não o comportamento do serviço em uso.

### 4º Impacto nas hipóteses de baseline

- A classificação inconsistente dos relatos pode aumentar ou reduzir a contagem de defeitos. As métricas de ausência de falhas precisam de um critério explícito para decidir o que conta como defeito.
- As políticas do navegador podem impedir a restauração automática mesmo com o mecanismo correto no código. A avaliação verifica a existência e o funcionamento do mecanismo, não a garantia de restauração em qualquer navegador.
- Desenhos grandes aumentam a chance de atingir o limite de armazenamento, o que afeta a recuperabilidade e liga este objetivo à escalabilidade do G3.
- Sem acesso à produção, disponibilidade e tolerância a falhas são avaliadas pela presença dos mecanismos e por testes controlados. Os resultados indicam capacidade, não comportamento observado em uso real.

---

## 5. G3: Flexibilidade

| Objeto | Propósito | Foco da qualidade | Ponto de vista |
| :--- | :--- | :--- | :--- |
| Biblioteca `@excalidraw/excalidraw` e aplicação web, incluindo a interface pública da biblioteca, as instruções de instalação e os formatos de exportação | Entender | [Flexibilidade](../fase-01/modelo-de-qualidade.md#flexibilidade) | Desenvolvedores que integram a biblioteca e equipes de implantação e operação |

### 1º Foco de qualidade

| Subcaracterística | Métricas candidatas |
| :--- | :--- |
| Adaptabilidade | Navegadores e versões declarados como suportados; versões de React aceitas pela biblioteca; existência de instruções para frameworks com renderização no servidor; tratamento de entrada por toque e caneta. |
| Escalabilidade | Tempo para abrir, mover e exportar desenhos com quantidades crescentes de elementos, em ambiente controlado; maior desenho que pode ser aberto e salvo sem travar a aplicação. |
| Instalabilidade | Número de passos para instalar a biblioteca; pré-requisitos declarados (versões de ferramentas); sucesso na construção da imagem Docker; proporção dos passos documentados que podem ser reproduzidos sem ajustes. |
| Substituibilidade | Formatos de exportação disponíveis; existência de documentação do formato `.excalidraw`; proporção do conteúdo preservado ao exportar e reimportar. |

### 2º Hipóteses de baseline

- **Adaptabilidade:** a aplicação funciona nas versões recentes dos principais navegadores, mas não em navegadores antigos. A biblioteca aceita mais de uma versão principal de React e precisa ser carregada apenas no navegador quando usada em frameworks com renderização no servidor. O editor aceita toque e caneta.
- **Escalabilidade:** o editor continua utilizável com algumas centenas de elementos, e o desempenho cai de forma perceptível com milhares. Exportar um desenho grande é mais lento do que abri-lo.
- **Instalabilidade:** a biblioteca é instalada com um único comando dos gerenciadores de pacotes usuais. A imagem Docker é construída sem passos manuais adicionais, e as instruções de execução local são suficientes, desde que as versões de ferramentas exigidas sejam respeitadas.
- **Substituibilidade:** o desenho pode ser exportado em `.excalidraw`, PNG e SVG, e PNG e SVG podem guardar os dados do desenho para reimportação. O formato `.excalidraw` é legível (texto em JSON), mas não tem uma especificação formal publicada.

### 3º Fatores de variação

- **Hardware e navegador** usados nos testes de desempenho.
- **Versões das ferramentas** do ambiente de construção, como Node.js e o gerenciador de pacotes.
- **Evolução do ecossistema React** e dos empacotadores usados pelos integradores.
- **Conteúdo dos desenhos de teste:** tipos de elementos, textos e imagens incorporadas.

### 4º Impacto nas hipóteses de baseline

- Medidas de desempenho só são comparáveis quando feitas no mesmo hardware e no mesmo navegador. O ambiente de teste será fixado e registrado.
- Uma construção pode falhar por causa da versão de uma ferramenta, e não por um problema do produto. As versões usadas serão registradas, e falhas desse tipo serão distinguidas das demais.
- Mudanças no ecossistema React podem tornar desatualizadas as versões declaradas como compatíveis. A avaliação considera o que está declarado na versão avaliada.
- Imagens incorporadas aumentam o tamanho do desenho mais do que o número de elementos. Os desenhos de teste terão composição definida, para que o efeito de cada fator possa ser separado.

---

## 6. Uso das abstraction sheets nas próximas etapas

- **Hipóteses das questões:** cada hipótese de *baseline* dá origem à hipótese da questão da mesma subcaracterística. Onde a hipótese da questão difere da de *baseline*, a diferença e o motivo estão na [seção 7](#7-ajustes-feitos-no-detalhamento-do-gqm).
- **Seleção das métricas:** as métricas candidatas são filtradas pelas características desejáveis (AULA 08, p. 41) e pela possibilidade de coleta na versão avaliada (AULA 08, p. 42). As métricas que não vieram de uma candidata também estão na [seção 7](#7-ajustes-feitos-no-detalhamento-do-gqm).
- **Análise dos resultados:** os fatores de variação e seus impactos servem de guia para interpretar as medições (AULA 08, p. 31). Um resultado diferente do esperado é examinado à luz desses fatores antes de ser atribuído ao produto.

---

## 7. Ajustes feitos no detalhamento do GQM

A aula recomenda preencher a *abstraction sheet* de forma iterativa (AULA 08, p. 31). Os quadrantes das seções 3 a 5 são os aprovados na [reunião de 19/10/2026](../gestao/atas/2026-10-19-reuniao-gqm.md) e foram mantidos como registro dela. Ao escrever as questões, hipóteses e métricas de cada objetivo, algumas hipóteses foram refinadas e algumas métricas foram acrescentadas. Esta seção registra essas diferenças, para que cada hipótese e cada métrica possa ser rastreada até a *abstraction sheet*.

### 7.1 Hipóteses

As hipóteses de G3 ([Q3.1 a Q3.4](./gqm-flexibilidade.md)) são iguais às de *baseline* e não aparecem na tabela.

| Questão | Hipótese de *baseline* | Hipótese da questão | Motivo |
| :--- | :--- | :--- | :--- |
| [Q1.1](./gqm-manutenibilidade.md#3-q11--modularidade) | Não há ciclos entre os pacotes, e a biblioteca não importa código da aplicação web. | Não há ciclos **em tempo de execução**, e **nenhum pacote** importa código da aplicação web. | [M1.1.1](./gqm-manutenibilidade.md#m111--ciclos-de-dependência-entre-pacotes) conta só dependências em tempo de execução, e [M1.1.2](./gqm-manutenibilidade.md#m112--importações-que-violam-a-direção-declarada) verifica a direção declarada para todos os pacotes, e não só para a biblioteca. |
| [Q1.2](./gqm-manutenibilidade.md#4-q12--reusabilidade) | Os pacotes de base podem ser usados isoladamente; parte das **opções avançadas** só aparece nos tipos. | Sem "podem ser usados isoladamente"; parte das **propriedades públicas** só aparece nos tipos. | [M1.2.1](./gqm-manutenibilidade.md#m121--arquivos-de-pacotes-de-base-com-dependência-de-react-ou-do-navegador) mede a dependência de React e do navegador, e não o uso isolado. [M1.2.2](./gqm-manutenibilidade.md#m122--proporção-de-propriedades-públicas-documentadas) conta propriedades de `ExcalidrawProps`, e não há critério objetivo para separar opções avançadas das demais. |
| [Q1.3](./gqm-manutenibilidade.md#5-q13--analisabilidade) | O componente principal do editor é o arquivo **mais extenso e complexo** do projeto. | A complexidade alta se concentra em poucos arquivos, **principalmente** no componente principal do editor; acrescenta a documentação para desenvolvedores. | O tamanho dos arquivos passou para Q1.4 ([M1.4.2](./gqm-manutenibilidade.md#m142--arquivos-de-produção-extensos)). A documentação entrou porque [M1.3.2](./gqm-manutenibilidade.md#m132--cobertura-da-documentação-para-desenvolvedores) a mede. |
| [Q1.4](./gqm-manutenibilidade.md#6-q14--modificabilidade) | Os arquivos mais extensos são **também os mais alterados**. | Há **poucos** arquivos muito extensos, alterados por uma **parte relevante** das contribuições. | [M1.4.3](./gqm-manutenibilidade.md#m143--proporção-de-contribuições-que-alteram-arquivos-extensos) mede a parte das contribuições que passa pelos arquivos extensos, e não uma ordenação dos arquivos mais alterados. |
| [Q1.5](./gqm-manutenibilidade.md#7-q15--testabilidade) | A biblioteca tem **mais testes** do que a aplicação web. | A biblioteca tem **cobertura** maior do que a aplicação web. | [M1.5.1](./gqm-manutenibilidade.md#m151--cobertura-de-linhas-por-pacote) mede a cobertura de linhas, que não depende do tamanho de cada pacote, como dependeria a contagem de testes. |
| [Q2.1](./gqm-confiabilidade.md#3-q21--ausência-de-falhas) | O **volume de defeitos** relatados é alto; colaboração, texto e exportação **concentram mais defeitos**. | As **correções** são parte relevante das contribuições integradas; toda contribuição passa por verificações automáticas **e por revisão**. | A classificação dos relatos é inconsistente (fator de variação da seção 4), então [M2.1.1](./gqm-confiabilidade.md#m211--proporção-de-correções-entre-as-contribuições-integradas) usa as correções integradas, cujo tipo é verificado pelo próprio projeto. Pelo mesmo motivo, a distribuição por área não foi selecionada. A revisão entrou com [M2.1.3](./gqm-confiabilidade.md#m213--proporção-de-contribuições-revisadas-antes-da-integração). |
| [Q2.2](./gqm-confiabilidade.md#4-q22--disponibilidade) | O editor funciona sem conexão; colaboração e link não. | Acrescenta: o editor local carrega **poucos recursos externos, nenhum indispensável**. | Entrou com [M2.2.2](./gqm-confiabilidade.md#m222--origens-externas-necessárias-para-o-editor-local), que responde ao RQ-CONF-04 da [Fase 01](../fase-01/requisitos-avaliacao.md#3-requisitos-de-confiabilidade). |
| [Q2.3](./gqm-confiabilidade.md#5-q23--tolerância-a-falhas) | Se a colaboração cair, o desenho local continua editável. | Acrescenta: **o usuário é avisado**. | [M2.3.2](./gqm-confiabilidade.md#m232--continuidade-do-editor-após-falha-da-colaboração) inclui o aviso de falta de conexão entre as verificações. |
| [Q2.4](./gqm-confiabilidade.md#6-q24--recuperabilidade) | O último desenho é restaurado; arquivos **antigos** abrem; desfazer **não necessariamente** cobre as alterações de outros participantes. | Acrescenta **o fechamento inesperado** e os arquivos da **versão atual**; retira a ressalva sobre outros participantes. | [M2.4.1](./gqm-confiabilidade.md#m241--proporção-de-cenários-de-fechamento-com-restauração-do-desenho) testa cenários de fechamento, inclusive o inesperado, e [M2.4.2](./gqm-confiabilidade.md#m242--proporção-de-arquivos-reabertos-sem-perda) inclui arquivos da versão atual. [M2.4.3](./gqm-confiabilidade.md#m243--cobertura-de-desfazer-e-refazer) testa só as ações do próprio usuário, e por isso a ressalva saiu da hipótese. |

### 7.2 Métricas sem candidata correspondente

| Métrica | Candidata mais próxima | Motivo |
| :--- | :--- | :--- |
| [M1.4.3](./gqm-manutenibilidade.md#m143--proporção-de-contribuições-que-alteram-arquivos-extensos) | Nenhuma | Responde à parte da hipótese de Modificabilidade sobre os arquivos extensos serem os mais alterados, que nenhuma candidata media. |
| [M2.1.3](./gqm-confiabilidade.md#m213--proporção-de-contribuições-revisadas-antes-da-integração) | Verificações automáticas obrigatórias antes da integração | As verificações automáticas já são medidas em G1 ([M1.3.3](./gqm-manutenibilidade.md#m133--verificações-estáticas-executadas-automaticamente) e [M1.5.3](./gqm-manutenibilidade.md#m153--proporção-de-contribuições-com-testes-executados-antes-da-integração)). Em G2, mede-se a outra barreira antes da integração: a revisão por outra pessoa. |
| [M2.2.2](./gqm-confiabilidade.md#m222--origens-externas-necessárias-para-o-editor-local) | Nenhuma | Responde ao RQ-CONF-04, que nenhuma candidata cobria. |
| [M3.3.1](./gqm-flexibilidade.md#m331--proporção-de-operações-de-pacote-bem-sucedidas) | Número de passos para instalar a biblioteca | Além de contar se a instalação exige um único comando, mede se instalar, atualizar e remover terminam sem erro. |

---

## 8. Limitações

1. **Expectativas da equipe avaliadora.** As hipóteses refletem o que a equipe espera ao assumir o ponto de vista dos interessados, e não a opinião de mantenedores, integradores ou usuários reais ([limitações do método](./estrutura-gqm.md#6-limitações-do-método-nesta-avaliação)).
2. **Preenchimento em conjunto.** A aula recomenda entrevistas individuais, para que uma pessoa não influencie a outra (AULA 08, p. 28). As *abstraction sheets* foram preenchidas em reunião, então as hipóteses registram o consenso do grupo, e não as expectativas individuais de cada integrante.
3. **Conhecimento prévio limitado.** A equipe conhece o Excalidraw pela análise feita na Fase 01, e não por experiência de desenvolvimento no projeto. Por isso, a maior parte das hipóteses é comparativa, e não numérica.
4. **Fatores não controláveis.** Fatores como a forma de registro de defeitos pela comunidade e as políticas dos navegadores não podem ser controlados pela equipe, apenas registrados e considerados na análise.

---

## Referências

- AULA 08 QSW1 GQM. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Páginas 28 a 31, 41 e 42.
- BASILI, V. R.; CALDIERA, G.; ROMBACH, H. D. The Goal Question Metric Approach. In: *Encyclopedia of Software Engineering*. Wiley, 1994. Disponível em: [https://www.cs.umd.edu/~mvz/handouts/gqm.pdf](https://www.cs.umd.edu/~mvz/handouts/gqm.pdf).
- ISO/IEC 25010:2023. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model*.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 19/10/2026 | Criação das abstraction sheets dos objetivos G1, G2 e G3 | [Christopher Paraizo](https://github.com/wChrstphr) | [Luiz Henrique Soares](https://github.com/luizh-gsoares) |
| 1.1 | 27/10/2026 | Troca dos travessões dos títulos; links para os objetivos, o modelo de qualidade e as páginas de cada objetivo; citação literal da p. 31; seção 7 com as diferenças entre as *abstraction sheets* e o GQM detalhado; limitação do preenchimento em conjunto; fator de variação alinhado aos testes em ambiente local | [Christopher Paraizo](https://github.com/wChrstphr) | |
