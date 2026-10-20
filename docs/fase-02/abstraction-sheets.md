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

As hipóteses podem ser valores ou comparações, como "os módulos com mais defeitos" ou "o pior caso" (AULA 08, p. 31). Nesta página, as hipóteses são comparativas sempre que a equipe não tem base para estimar um valor antes da medição. A AULA 08 traz um exemplo preenchido para o foco de Confiabilidade (p. 30), que serviu de modelo para o formato.

---

## 2. Como as abstraction sheets foram preenchidas

A aula recomenda conduzir entrevistas individuais com a equipe do projeto avaliado (AULA 08, p. 28). Como os mantenedores do Excalidraw não estão disponíveis para entrevistas, a própria equipe avaliadora preencheu as *abstraction sheets*, assumindo o ponto de vista dos interessados de cada objetivo.

As três *abstraction sheets* foram preenchidas do zero, em conjunto, na [reunião de 19/10/2026](../gestao/atas/2026-10-19-reuniao-gqm.md) dos integrantes responsáveis pela Fase 02. A base foi a [descrição do produto](../fase-01/descricao-produto.md) e os [requisitos de avaliação](../fase-01/requisitos-avaliacao.md) da Fase 01. Cada quadrante foi discutido até ser considerado suficientemente completo (AULA 08, p. 31).

As métricas listadas no foco de qualidade são **candidatas**. A seleção final, com uma a três métricas por questão, é feita no detalhamento de cada objetivo, junto com a ficha de cada métrica ([estrutura das questões](./estrutura-gqm.md#4-estrutura-das-questões)).

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

- **Ausência de falhas:** o volume de defeitos relatados é alto, compatível com um projeto muito usado, e a maior parte dos defeitos corrigidos é fechada em poucas semanas. Colaboração, edição de texto e exportação concentram mais defeitos do que o desenho de formas básicas. Toda alteração proposta passa por verificações automáticas.
- **Disponibilidade:** depois do primeiro carregamento, o editor funciona sem conexão. A colaboração em tempo real e o compartilhamento por link não funcionam sem conexão.
- **Tolerância a falhas:** arquivos inválidos ou corrompidos são recusados com uma mensagem, sem travar o editor. Se a sessão de colaboração cair, o desenho local continua editável.
- **Recuperabilidade:** ao reabrir a aplicação, o último desenho é restaurado do armazenamento do navegador. Arquivos de versões antigas abrem nas versões atuais. Desfazer e refazer cobrem as ações de edição do próprio usuário, mas não necessariamente as alterações feitas por outros participantes da colaboração.

### 3º Fatores de variação

- **Navegador e suas políticas de armazenamento:** limite de espaço, navegação privada e limpeza automática de dados.
- **Condições de rede:** conexão instável ou ausente e indisponibilidade do servidor de colaboração.
- **Tamanho do desenho:** número de elementos e imagens incorporadas.
- **Forma como a comunidade registra defeitos:** relatos duplicados, sem classificação ou classificados de forma inconsistente.
- **Análise sem acesso aos servidores de produção:** a avaliação observa o código e a configuração, e não o comportamento do serviço em uso.

### 4º Impacto nas hipóteses de baseline

- A classificação inconsistente dos relatos pode aumentar ou reduzir a contagem de defeitos. As métricas de ausência de falhas precisam de um critério explícito para decidir o que conta como defeito.
- As políticas do navegador podem impedir a restauração automática mesmo com o mecanismo correto no código. A avaliação verifica a existência e o funcionamento do mecanismo, não a garantia de restauração em qualquer navegador.
- Desenhos grandes aumentam a chance de atingir o limite de armazenamento, o que afeta a recuperabilidade e liga este objetivo à escalabilidade do G3.
- Sem acesso à produção, disponibilidade e tolerância a falhas são avaliadas pela presença dos mecanismos e por testes controlados. Os resultados indicam capacidade, não comportamento observado em uso real.

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

- **Hipóteses das questões:** cada hipótese de *baseline* dá origem à hipótese da questão da mesma subcaracterística.
- **Seleção das métricas:** as métricas candidatas são filtradas pelas características desejáveis (AULA 08, p. 41) e pela possibilidade de coleta na versão avaliada (AULA 08, p. 42).
- **Análise dos resultados:** os fatores de variação e seus impactos servem de guia para interpretar as medições (AULA 08, p. 31). Um resultado diferente do esperado é examinado à luz desses fatores antes de ser atribuído ao produto.

---

## 7. Limitações

1. **Expectativas da equipe avaliadora.** As hipóteses refletem o que a equipe espera ao assumir o ponto de vista dos interessados, e não a opinião de mantenedores, integradores ou usuários reais ([limitações do método](./estrutura-gqm.md#6-limitações-do-método-nesta-avaliação)).
2. **Conhecimento prévio limitado.** A equipe conhece o Excalidraw pela análise feita na Fase 01, e não por experiência de desenvolvimento no projeto. Por isso, a maior parte das hipóteses é comparativa, e não numérica.
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
