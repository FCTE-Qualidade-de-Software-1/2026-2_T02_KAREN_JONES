---
sidebar_position: 4
title: GQM de Confiabilidade (G2)
description: Questões, hipóteses e métricas do objetivo de medição G2, que avalia a confiabilidade do editor e da aplicação web do Excalidraw
---

# GQM de Confiabilidade (G2)

Esta página detalha o objetivo G2, definido em [Método GQM e objetivos de medição](./estrutura-gqm.md#g2--confiabilidade). Para cada subcaracterística de Confiabilidade há uma questão, a hipótese da questão e as métricas que a respondem.

| Campo do template | Valor |
| :--- | :--- |
| Analisar | o editor, a aplicação web e os mecanismos de colaboração e de salvamento no navegador, além do histórico público de defeitos relatados |
| para o propósito de | entender |
| com respeito a | Confiabilidade: ausência de falhas (Maturidade, na edição de 2011), disponibilidade, tolerância a falhas e recuperabilidade |
| do ponto de vista de | usuários finais |
| no contexto de | código-fonte público na versão de 18/10/2026, avaliado por equipe independente, sem acesso aos servidores de produção |

As questões caracterizam o produto em relação a cada subcaracterística (AULA 08, p. 33 e 34). As hipóteses partem da [abstraction sheet de G2](./abstraction-sheets.md#4-g2--confiabilidade), como a aula permite (AULA 08, p. 34). As métricas respondem às questões de forma quantitativa (AULA 08, p. 38). Os níveis de pontuação e os critérios de julgamento de cada métrica são definidos em uma página própria da Fase 02.

---

## 1. Visão geral

| Questão | Subcaracterística | Requisitos da Fase 01 | Métricas |
| :--- | :--- | :--- | :--- |
| Q2.1 | Ausência de falhas | RQ-CONF-01 e RQ-CONF-02 | M2.1.1, M2.1.2, M2.1.3 |
| Q2.2 | Disponibilidade | RQ-CONF-03 e RQ-CONF-04 | M2.2.1, M2.2.2 |
| Q2.3 | Tolerância a falhas | RQ-CONF-05 a RQ-CONF-07 | M2.3.1, M2.3.2 |
| Q2.4 | Recuperabilidade | RQ-CONF-08 a RQ-CONF-11 | M2.4.1, M2.4.2, M2.4.3 |

Os requisitos estão em [Requisitos da avaliação](../fase-01/requisitos-avaliacao.md). A seção 7 mostra qual métrica atende cada requisito.

---

## 2. Convenções de coleta

As definições abaixo valem para todas as métricas de G2 e evitam que pessoas diferentes contem ou testem coisas diferentes.

- **Versão avaliada:** commit `e1b7aac` do repositório oficial, de 18/10/2026, identificado no [escopo](../fase-01/escopo-avaliacao.md).
- **Janela histórica:** contribuições integradas e relatos abertos entre 18/04/2026 e 18/10/2026, os seis meses que antecedem a versão avaliada. A janela delimita os dados de histórico do projeto (objeto O6 do escopo).
- **Contribuição integrada:** *pull request* aceito (*merged*) no ramo principal do repositório.
- **Correção:** contribuição integrada cujo título começa com o tipo `fix`. O próprio Excalidraw exige que todo título de *pull request* comece com um tipo padronizado (`feat`, `fix`, `docs`, `refactor` e outros), verificado automaticamente pelo fluxo `semantic-pr-title.yml`. Esse padrão é usado porque a maior parte dos relatos de defeito no repositório não recebe rótulo, o que tornaria a contagem por rótulo pouco confiável.
- **Ambiente de teste:** a aplicação web construída a partir da versão avaliada, executada localmente com a configuração de produção do repositório, em um navegador de versão fixa. O ambiente exato (máquina, sistema operacional, navegador e versões) é definido no plano de avaliação da Fase 03 e registrado em cada coleta.
- **Cena de referência:** desenho padronizado usado nos testes, com ao menos um elemento de cada tipo principal: retângulo, elipse, losango, seta, linha, desenho livre, texto, texto dentro de forma, imagem e moldura (*frame*).

Os fatores que podem influenciar os resultados também são registrados junto com cada coleta (AULA 08, p. 38): o commit avaliado, a janela histórica, o navegador e sua versão, e o estado da rede durante os testes. Esses fatores foram levantados na abstraction sheet de G2.

---

## 3. Q2.1 — Ausência de falhas

**Questão:** O projeto evita que falhas cheguem ao usuário e trata de forma organizada os defeitos que chegam?

**Requisitos:** RQ-CONF-01 (verificações automáticas e revisão antes da integração) e RQ-CONF-02 (registro, classificação e tratamento dos defeitos).

**Hipótese:** as correções são uma parte relevante das contribuições integradas, compatível com um projeto muito usado. Os defeitos relatados são corrigidos em poucas semanas. Toda contribuição passa por verificações automáticas e por revisão de outra pessoa antes da integração.

### M2.1.1 — Proporção de correções entre as contribuições integradas

| Campo | Descrição |
| :--- | :--- |
| Definição | Percentual das contribuições integradas na janela histórica que são correções de defeitos. |
| Procedimento de cálculo | (correções integradas na janela ÷ contribuições integradas na janela) × 100. Também é registrada a distribuição das correções pelo escopo indicado no título (por exemplo, `fix(editor)` ou `fix(app)`). Unidade: percentual. Escala: 0 a 100. |
| Fonte dos dados | Histórico de *pull requests* do repositório oficial no GitHub. |
| Procedimento de coleta | Busca da API do GitHub (`gh api search/issues`) com os filtros `is:pr is:merged` e o intervalo da janela, separando as correções pelo tipo `fix` no início do título. Contribuições automáticas de atualização de dependências e de traduções são excluídas. |
| Critério de interpretação | Confirma a hipótese se o percentual for relevante. O resultado mostra quanto do esforço do projeto vai para corrigir defeitos em vez de criar funcionalidades. Ele não mede quantos defeitos existem, só quantos foram corrigidos. |
| Questão respondida | Q2.1 |
| Características desejáveis | Simples (uma razão). Objetiva, porque o tipo da contribuição é verificado automaticamente pelo próprio projeto. Fácil de coletar pela API. Robusta, porque permite comparar janelas diferentes. |

### M2.1.2 — Mediana do tempo entre o relato e a correção

| Campo | Descrição |
| :--- | :--- |
| Definição | Mediana do tempo entre a abertura de um relato de defeito e a integração da correção que o encerra, para as correções integradas na janela histórica. |
| Procedimento de cálculo | Para cada correção integrada na janela que declara encerrar um relato (*closing issue reference* do GitHub), calcular a diferença em dias entre a data de integração da correção e a data de abertura do relato. Calcular a mediana. Também é registrada a proporção das correções que declaram encerrar um relato. Unidade: dias. Escala: absoluta. |
| Fonte dos dados | Histórico de *pull requests* e de *issues* do repositório oficial no GitHub. |
| Procedimento de coleta | API GraphQL do GitHub (`gh api graphql`), campo `closingIssuesReferences` de cada correção, com a data de abertura de cada relato ligado. |
| Critério de interpretação | Confirma a hipótese se a mediana for de poucas semanas. Medianas longas indicam que o usuário convive mais tempo com o defeito. Se poucas correções estiverem ligadas a relatos, o resultado vale só para essa parte e isso é registrado. |
| Questão respondida | Q2.1 |
| Características desejáveis | Objetiva, porque as datas vêm do registro do GitHub. Robusta a valores extremos, por usar a mediana. Fácil de coletar automaticamente. Válida para o tratamento dos defeitos (RQ-CONF-02). |

### M2.1.3 — Proporção de contribuições revisadas antes da integração

| Campo | Descrição |
| :--- | :--- |
| Definição | Percentual das contribuições integradas na janela histórica que receberam pelo menos uma aprovação de revisão de uma pessoa diferente do autor. |
| Procedimento de cálculo | (contribuições com ao menos uma revisão aprovada por outra pessoa ÷ contribuições integradas na janela) × 100. Unidade: percentual. Escala: 0 a 100. |
| Fonte dos dados | Revisões registradas em cada *pull request* do repositório oficial no GitHub; fluxos de `.github/workflows/` disparados por `pull_request`. |
| Procedimento de coleta | API GraphQL do GitHub, campo `reviews` com estado `APPROVED` de cada contribuição, comparando o autor da revisão com o autor da contribuição. As verificações automáticas são as mesmas medidas no objetivo de Manutenibilidade e não são contadas de novo aqui. |
| Critério de interpretação | Confirma a hipótese se o valor for 100% ou próximo disso. Contribuições integradas sem revisão dependem só das verificações automáticas para evitar falhas. |
| Questão respondida | Q2.1 |
| Características desejáveis | Simples. Objetiva, porque usa o registro de revisões do GitHub. Fácil de coletar automaticamente. Válida para RQ-CONF-01. |

---

## 4. Q2.2 — Disponibilidade

**Questão:** O editor continua disponível para o usuário sem conexão e sem depender de serviços externos?

**Requisitos:** RQ-CONF-03 (uso sem conexão após o primeiro carregamento) e RQ-CONF-04 (independência de colaboração e de recursos remotos).

**Hipótese:** depois do primeiro carregamento, o editor funciona sem conexão. A colaboração em tempo real e o compartilhamento por link não funcionam sem conexão. O editor local carrega poucos recursos de servidores externos, e nenhum deles é indispensável para desenhar.

### M2.2.1 — Proporção de funções essenciais disponíveis sem conexão

| Campo | Descrição |
| :--- | :--- |
| Definição | Percentual de uma lista fixa de funções essenciais do editor que funcionam sem conexão, depois de um primeiro carregamento com conexão. |
| Procedimento de cálculo | Lista de funções verificadas: (1) recarregar a página; (2) criar formas; (3) escrever texto; (4) mover e redimensionar elementos; (5) desfazer e refazer; (6) salvar em arquivo `.excalidraw`; (7) abrir um arquivo `.excalidraw`; (8) exportar em PNG; (9) exportar em SVG; (10) exibir o texto com a fonte padrão. Calcular (funções que funcionam ÷ 10) × 100. Unidade: percentual. Escala: 0 a 100. |
| Fonte dos dados | Aplicação web em execução no ambiente de teste; configuração do *service worker* em `excalidraw-app/vite.config.mts`. |
| Procedimento de coleta | Abrir a aplicação com conexão, aguardar o registro do *service worker*, desligar a rede pelo modo *offline* das ferramentas do navegador e executar a lista na ordem, registrando cada item como funciona ou não funciona, com captura de tela. |
| Critério de interpretação | Confirma a hipótese se o valor for 100%. Cada função que falha é um caso em que o usuário perde acesso ao editor sem conexão. |
| Questão respondida | Q2.2 |
| Características desejáveis | Simples. Objetiva, porque a lista é fixa e cada item tem resultado binário com evidência. Válida, porque testa o comportamento, e não só a presença da configuração. Robusta, porque pode ser repetida em outros navegadores. |

### M2.2.2 — Origens externas necessárias para o editor local

| Campo | Descrição |
| :--- | :--- |
| Definição | Número de domínios diferentes do da aplicação dos quais o editor carrega recursos ao ser aberto sem sessão de colaboração. Também é registrado quantos desses recursos são indispensáveis para desenhar. |
| Procedimento de cálculo | Contar os domínios externos no registro de requisições da abertura do editor. Para cada domínio, bloquear suas requisições e verificar se o editor ainda permite criar formas e texto; se não permitir, o domínio é indispensável. Unidade: domínios. Escala: absoluta. |
| Fonte dos dados | Registro de rede (arquivo HAR) do navegador no ambiente de teste. |
| Procedimento de coleta | Abrir o editor com o cache vazio, exportar o registro de rede das ferramentas do navegador e listar os domínios. Repetir a abertura com cada domínio bloqueado pela opção de bloqueio de requisições do navegador. |
| Critério de interpretação | Confirma a hipótese se houver poucos domínios externos e nenhum indispensável. Cada domínio indispensável é um serviço cuja queda deixa o editor indisponível. |
| Questão respondida | Q2.2 |
| Características desejáveis | Objetiva, porque os domínios saem do registro do navegador. Fácil de coletar com ferramentas do próprio navegador. Válida para RQ-CONF-04. |

---

## 5. Q2.3 — Tolerância a falhas

**Questão:** O editor continua funcionando quando recebe dados inválidos ou quando a conexão com a colaboração falha?

**Requisitos:** RQ-CONF-05 (funcionalidades essenciais diante de problemas de conectividade), RQ-CONF-06 (editor local após falha da colaboração) e RQ-CONF-07 (arquivos inválidos ou corrompidos).

**Hipótese:** arquivos inválidos ou corrompidos são recusados com uma mensagem, sem travar o editor. Se a sessão de colaboração cair, o desenho local continua editável e o usuário é avisado.

### M2.3.1 — Proporção de arquivos inválidos tratados com mensagem

| Campo | Descrição |
| :--- | :--- |
| Definição | Percentual de casos de uma lista fixa de arquivos inválidos ou corrompidos em que o editor exibe uma mensagem de erro e continua utilizável. |
| Procedimento de cálculo | Lista de casos: (1) arquivo vazio com extensão `.excalidraw`; (2) JSON com erro de sintaxe; (3) JSON válido sem o campo `type`; (4) campo `type` com valor desconhecido; (5) lista de elementos com campos obrigatórios ausentes; (6) elemento com coordenadas não numéricas; (7) arquivo binário qualquer renomeado para `.excalidraw`; (8) imagem PNG sem desenho incorporado; (9) arquivo `.excalidraw` truncado no meio. Um caso é tratado se o editor mostra uma mensagem e, em seguida, ainda permite criar formas sem recarregar a página. Calcular (casos tratados ÷ 9) × 100. Unidade: percentual. Escala: 0 a 100. |
| Fonte dos dados | Aplicação web no ambiente de teste; arquivos de teste preparados pela equipe e guardados no repositório da avaliação. |
| Procedimento de coleta | Abrir cada arquivo pelo menu de abertura e, em outra rodada, arrastando o arquivo para o editor. Registrar a mensagem exibida (ou a ausência dela) e se o editor continua utilizável, com captura de tela. |
| Critério de interpretação | Confirma a hipótese se o valor for 100%. Cada caso não tratado é uma forma de o usuário travar o editor ou perder o trabalho em andamento. |
| Questão respondida | Q2.3 |
| Características desejáveis | Objetiva e consistente, porque os arquivos são fixos e o critério de tratamento é definido antes do teste. Robusta, porque os mesmos arquivos servem para outras versões. Válida para RQ-CONF-07. |

### M2.3.2 — Continuidade do editor após falha da colaboração

| Campo | Descrição |
| :--- | :--- |
| Definição | Percentual de uma lista fixa de verificações que passam quando a conexão de uma sessão de colaboração é interrompida. |
| Procedimento de cálculo | Com uma sessão de colaboração ativa entre duas janelas, interromper a rede de uma delas e verificar: (1) o desenho continua na tela; (2) é possível criar e editar elementos; (3) o usuário recebe aviso de que está sem conexão; (4) é possível salvar o desenho em arquivo; (5) ao restabelecer a rede, as alterações feitas sem conexão aparecem na outra janela. Calcular (verificações que passam ÷ 5) × 100. Unidade: percentual. Escala: 0 a 100. |
| Fonte dos dados | Aplicação web no ambiente de teste, conectada ao servidor de colaboração configurado na versão avaliada; código de colaboração em `excalidraw-app/collab/`. |
| Procedimento de coleta | Teste manual roteirizado, repetido três vezes, com o modo *offline* das ferramentas do navegador para interromper a rede. Cada verificação passa se passar nas três repetições. |
| Critério de interpretação | Confirma a hipótese se as verificações 1 a 4 passarem. A verificação 5 mostra se o trabalho feito durante a falha é preservado na sessão compartilhada. |
| Questão respondida | Q2.3 |
| Características desejáveis | Objetiva, porque cada verificação tem resultado binário definido antes do teste. Robusta, por exigir três repetições. Válida para RQ-CONF-05 e RQ-CONF-06. |

---

## 6. Q2.4 — Recuperabilidade

**Questão:** O usuário recupera seu trabalho depois de fechar a aplicação, de reabrir arquivos antigos ou de cometer um erro de edição?

**Requisitos:** RQ-CONF-08 (restauração automática do último estado), RQ-CONF-09 (salvar e reabrir arquivos), RQ-CONF-10 (arquivos de versões anteriores) e RQ-CONF-11 (desfazer e refazer).

**Hipótese:** ao reabrir a aplicação, o último desenho é restaurado, inclusive depois de um fechamento inesperado. Arquivos salvos na versão atual e em versões anteriores são reabertos sem perda. Desfazer e refazer cobrem as ações de edição do próprio usuário.

### M2.4.1 — Proporção de cenários de fechamento com restauração do desenho

| Campo | Descrição |
| :--- | :--- |
| Definição | Percentual de cenários de fechamento em que a cena de referência é restaurada por completo ao reabrir a aplicação. |
| Procedimento de cálculo | Cenários: (1) recarregar a página; (2) fechar a aba e abrir de novo; (3) fechar o navegador normalmente; (4) encerrar o processo do navegador pelo sistema operacional, um segundo depois da última edição. Um cenário passa se todos os elementos da cena de referência voltarem com as mesmas propriedades. Calcular (cenários que passam ÷ 4) × 100. Unidade: percentual. Escala: 0 a 100. |
| Fonte dos dados | Aplicação web no ambiente de teste; armazenamento do navegador; código de salvamento local em `excalidraw-app/data/LocalData.ts`. |
| Procedimento de coleta | Montar a cena de referência, executar cada cenário e comparar a cena reaberta com a original exportando ambas em `.excalidraw` e comparando os elementos com um script. |
| Critério de interpretação | Confirma a hipótese se o valor for 100%. Cada cenário que falha é uma situação em que o usuário perde trabalho sem ter salvo um arquivo. |
| Questão respondida | Q2.4 |
| Características desejáveis | Objetiva, porque a comparação entre as cenas é feita por script. Válida para RQ-CONF-08. Robusta, porque os cenários podem ser repetidos em outros navegadores. |

### M2.4.2 — Proporção de arquivos reabertos sem perda

| Campo | Descrição |
| :--- | :--- |
| Definição | Percentual de arquivos de um conjunto de teste que a versão avaliada abre sem perder elementos ou propriedades. |
| Procedimento de cálculo | Conjunto de teste: a cena de referência salva em `.excalidraw` pela versão avaliada e pelas versões publicadas v0.15.0, v0.16.4, v0.17.6 e v0.18.0, mais as imagens com desenho incorporado que o próprio repositório usa como exemplo (`test_embedded_v1.png` e `smiley_embedded_v2.png`). Um arquivo é reaberto sem perda se todos os elementos aparecem com tipo, posição, tamanho e texto iguais aos do original. Calcular (arquivos reabertos sem perda ÷ arquivos do conjunto) × 100. Unidade: percentual. Escala: 0 a 100. |
| Fonte dos dados | Aplicação web das versões citadas, construída a partir das marcações (*tags*) do repositório; arquivos de exemplo em `packages/excalidraw/tests/fixtures/`. |
| Procedimento de coleta | Gerar os arquivos em cada versão anterior, abri-los na versão avaliada e comparar os elementos com um script. |
| Critério de interpretação | Confirma a hipótese se o valor for 100%. Cada arquivo com perda indica um desenho antigo que o usuário não consegue recuperar como foi salvo. |
| Questão respondida | Q2.4 |
| Características desejáveis | Objetiva, porque a comparação é feita por script sobre um conjunto fixo. Robusta, porque o conjunto pode crescer com novas versões. Válida para RQ-CONF-09 e RQ-CONF-10. |

### M2.4.3 — Cobertura de desfazer e refazer

| Campo | Descrição |
| :--- | :--- |
| Definição | Percentual de uma lista fixa de tipos de ação que podem ser desfeitos e refeitos, voltando exatamente ao estado anterior e ao posterior. |
| Procedimento de cálculo | Tipos de ação: (1) criar elemento; (2) apagar elemento; (3) mover; (4) redimensionar; (5) girar; (6) mudar cor ou estilo; (7) editar texto; (8) agrupar e desagrupar; (9) mudar a ordem de sobreposição; (10) ligar uma seta a uma forma. Uma ação passa se, depois de desfazer, a cena volta ao estado anterior e, depois de refazer, volta ao estado posterior. Calcular (ações que passam ÷ 10) × 100. Unidade: percentual. Escala: 0 a 100. |
| Fonte dos dados | Aplicação web no ambiente de teste; código do histórico de edição em `packages/excalidraw/history.ts`. |
| Procedimento de coleta | Teste manual roteirizado, exportando a cena antes da ação, depois da ação, depois de desfazer e depois de refazer, e comparando as exportações com um script. |
| Critério de interpretação | Confirma a hipótese se o valor for 100%. Cada tipo de ação que não pode ser desfeito é um erro do usuário que não tem volta. |
| Questão respondida | Q2.4 |
| Características desejáveis | Simples. Objetiva, porque a comparação é feita por script. Válida para RQ-CONF-11. Robusta, porque a lista pode ser repetida em outras versões. |

---

## 7. Rastreabilidade com a Fase 01

| Requisito | Subcaracterística | Questão | Métricas |
| :--- | :--- | :--- | :--- |
| RQ-CONF-01 | Ausência de falhas | Q2.1 | M2.1.3 |
| RQ-CONF-02 | Ausência de falhas | Q2.1 | M2.1.1, M2.1.2 |
| RQ-CONF-03 | Disponibilidade | Q2.2 | M2.2.1 |
| RQ-CONF-04 | Disponibilidade | Q2.2 | M2.2.2 |
| RQ-CONF-05 | Tolerância a falhas | Q2.3 | M2.3.2 |
| RQ-CONF-06 | Tolerância a falhas | Q2.3 | M2.3.2 |
| RQ-CONF-07 | Tolerância a falhas | Q2.3 | M2.3.1 |
| RQ-CONF-08 | Recuperabilidade | Q2.4 | M2.4.1 |
| RQ-CONF-09 | Recuperabilidade | Q2.4 | M2.4.2 |
| RQ-CONF-10 | Recuperabilidade | Q2.4 | M2.4.2 |
| RQ-CONF-11 | Recuperabilidade | Q2.4 | M2.4.3 |

Todos os 11 requisitos de Confiabilidade da Fase 01 são atendidos por pelo menos uma métrica.

---

## 8. Verificação das métricas

A aula pede verificar se as métricas podem ser coletadas e se são consistentes com as questões e o objetivo (AULA 08, p. 42). A equipe fez essa verificação no código da versão avaliada e no repositório oficial, sem registrar valores, porque a medição propriamente dita pertence à Fase 04.

| Métrica | O que foi verificado |
| :--- | :--- |
| M2.1.1 | O fluxo `semantic-pr-title.yml` exige o tipo no título de toda contribuição, e a busca da API do GitHub retorna as contribuições integradas na janela, filtráveis pelo tipo `fix`. Foi verificado também que nenhum relato aberto na janela recebeu o rótulo `bug`, o que confirmou a decisão de não contar defeitos por rótulo. |
| M2.1.2 e M2.1.3 | A API GraphQL do GitHub retorna, para cada contribuição, os relatos que ela encerra e as revisões aprovadas. |
| M2.2.1 | A aplicação registra um *service worker* (plugin `vite-plugin-pwa` em `excalidraw-app/vite.config.mts`) com regras de cache para os arquivos da aplicação e para as fontes. O teste depende da execução da aplicação no ambiente de teste. |
| M2.2.2 | O registro de rede e o bloqueio de requisições são recursos padrão das ferramentas de desenvolvedor dos navegadores. |
| M2.3.1 | O código de abertura de arquivos (`packages/excalidraw/data/blob.ts`) lança erros para arquivos inválidos, e a interface tem mensagens para esses casos, como "Couldn't load invalid file". |
| M2.3.2 | O código de colaboração (`excalidraw-app/collab/Collab.tsx`) acompanha o estado de conexão do navegador, e a configuração de produção aponta para um servidor de colaboração público. |
| M2.4.1 | O salvamento local está em `excalidraw-app/data/LocalData.ts`, com intervalo de 300 ms definido em `excalidraw-app/app_constants.ts`. |
| M2.4.2 | As marcações das versões v0.15.0, v0.16.4, v0.17.6 e v0.18.0 existem no repositório oficial, e os arquivos de exemplo com desenho incorporado estão em `packages/excalidraw/tests/fixtures/`. |
| M2.4.3 | O histórico de edição está implementado em `packages/excalidraw/history.ts` e tem testes próprios (`history.test.tsx`). |

---

## Referências

- AULA 08 QSW1 GQM. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Páginas 33, 34, 38 e 42.
- Especificação do trabalho final da disciplina de Qualidade de Software 1 (2026-2 Trabalho final completo v1). Página 1, premissa 2.
- ISO/IEC 25010:2023. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model*.
- Excalidraw. Repositório oficial, commit `e1b7aac` de 18/10/2026. Disponível em: https://github.com/excalidraw/excalidraw/tree/e1b7aacb356a492aa1e0fc6eb57b8896124027f0.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 19/10/2026 | Criação das questões, hipóteses e métricas do objetivo G2 | [Christopher Paraizo](https://github.com/wChrstphr) | [Luiz Henrique Soares](https://github.com/luizh-gsoares), [Maria Eduarda](https://github.com/eduarda-ogomes) |
