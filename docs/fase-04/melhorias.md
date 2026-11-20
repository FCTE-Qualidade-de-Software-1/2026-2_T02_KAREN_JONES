---
sidebar_position: 10
title: Oportunidades de melhoria
description: Pontos de melhoria e de atenção de G1, G2 e G3, critérios de priorização, ações escolhidas, modelo de documentação de propriedade e resultado das ações
---

import Link from '@docusaurus/Link';

# Oportunidades de melhoria

## Introdução

A avaliação deve terminar com oportunidades de melhoria baseadas nas métricas e nos julgamentos, e com pelo menos uma ação executada, justificada pelas evidências [[1, p. 3]](#ref-1). Na interpretação do GQM, é a equipe que traduz as conclusões em ações [[2, p. 60]](#ref-2). Esta página lista os pontos de melhoria de [G1](./resultados-g1-manutenibilidade.md), [G2](./resultados-g2-confiabilidade.md) e [G3](./resultados-g3-flexibilidade.md) e registra as duas ações escolhidas pela equipe, conforme a [interpretação e revisão](../fase-03/plano-analise.md#6-interpretação-e-revisão) do plano de análise.

A primeira ação documenta as propriedades públicas da biblioteca que estão sem documentação ([M1.2.2](../fase-02/gqm-manutenibilidade.md#m122-proporção-de-propriedades-públicas-documentadas)). É a única oportunidade pequena que muda o julgamento de uma característica: com ela, a manutenibilidade passa a atender. A segunda corrige a importação de arquivos `.excalidraw` cujos elementos são todos inválidos ([M2.3.1](../fase-02/gqm-confiabilidade.md#m231-proporção-de-arquivos-inválidos-tratados-com-mensagem)), um problema de confiabilidade que chega ao usuário como cena vazia ou tela branca. As duas ações foram enviadas ao Excalidraw como *pull requests*, e o efeito medido está na [seção 5](#5-resultado-das-ações).

## Metodologia

As oportunidades são as métricas nos níveis `-` e `--`, que a [regra dos pontos de melhoria](../fase-02/pontuacao-julgamento.md#73-pontos-de-melhoria) registra com a questão e a subcaracterística afetadas. Os pontos de atenção apontados nas análises de G2 e G3, com métricas no nível `o` ou acima, também entraram na decisão. Cada oportunidade foi comparada por três critérios:

- **Efeito no julgamento:** se levar a métrica para o nível seguinte, ou ao necessário, muda o julgamento da característica, calculado pela [agregação](../fase-02/pontuacao-julgamento.md#6-agregação-da-métrica-à-característica) e pelo [julgamento](../fase-02/pontuacao-julgamento.md#71-julgamento-de-cada-característica) da Fase 02.
- **Tamanho da mudança:** se cabe em um *pull request* pequeno ou exige discutir antes com os mantenedores, como o guia de contribuição do Excalidraw pede para mudanças grandes [[3]](#ref-3).
- **Medição antes e depois:** se a métrica pode ser medida de novo na base do *pull request*, pelo mesmo procedimento da ficha, dentro do prazo da avaliação.

Os tipos de ação seguem a especificação do trabalho: protótipo de alta fidelidade, modificação no código, templates técnicos ou processo de desenvolvimento. A ação pode ser incorporada ao repositório do software ou apresentada como entrega técnica [[1, p. 3]](#ref-1).

---

## 1. Oportunidades

<p className="tabela-titulo">Tabela 1: Pontos de melhoria de G1, G2 e G3</p>

| Métrica | Valor e nível | Questão | Efeito no julgamento | Tamanho | Medição antes e depois |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [M1.2.2](../fase-02/gqm-manutenibilidade.md#m122-proporção-de-propriedades-públicas-documentadas) | 57,69% `-` | Q1.2 Reusabilidade | Com 80% ou mais, G1 passa a atender | Pequeno: só documentação | Sim, com o mesmo formulário |
| [M1.2.1](../fase-02/gqm-manutenibilidade.md#m121-arquivos-de-pacotes-de-base-com-dependência-de-react-ou-do-navegador) | 69,07% `--` | Q1.2 Reusabilidade | Com 20% ou menos, G1 passa a atender | Grande: tirar a dependência do navegador de 48 dos 67 arquivos | Sim, com o script de cálculo |
| [M1.1.1](../fase-02/gqm-manutenibilidade.md#m111-ciclos-de-dependência-entre-pacotes) | 4 pares `-` | Q1.1 Modularidade | Nenhum, porque Q1.2 continua em `--` | Grande: muda a divisão entre pacotes | Sim, com o script de cálculo |
| [M1.3.1](../fase-02/gqm-manutenibilidade.md#m131-perfil-de-risco-de-complexidade-das-funções) | 6,54% em risco muito alto `--` | Q1.3 Analisabilidade | Nenhum, porque Q1.2 continua em `--` | Grande: refatorar as funções mais complexas | Sim, com o ESLint |
| [M1.4.3](../fase-02/gqm-manutenibilidade.md#m143-proporção-de-contribuições-que-alteram-arquivos-extensos) | 65,75% `--` | Q1.4 Modificabilidade | Nenhum, porque Q1.2 continua em `--` | Grande: dividir os arquivos extensos | Não: depende de seis meses de contribuições futuras |
| [M2.1.3](../fase-02/gqm-confiabilidade.md#m213-proporção-de-contribuições-revisadas-antes-da-integração) | 44,52% `-` | Q2.1 Ausência de falhas | Nenhum, porque G2 já atende | Médio: exige que os mantenedores mudem a regra de integração do repositório | Não: depende de seis meses de contribuições futuras |
| [M3.4.3](../fase-02/gqm-flexibilidade.md#m343-proporção-dos-campos-do-formato-excalidraw-documentados) | 26,9% `-` | Q3.4 Substituibilidade | Nenhum, porque G3 já atende | Grande: esquema do formato, verificação na CI e documentação | Sim, com a conferência dos campos |
| [M3.3.1](../fase-02/gqm-flexibilidade.md#m331-proporção-de-operações-de-pacote-bem-sucedidas) | 33,3% `-` | Q3.3 Instalabilidade | Nenhum, porque G3 já atende | Médio: o pacote depende de `@excalidraw/common`, que não é publicado, e a análise de G3 aponta a publicação sincronizada dos subpacotes | Sim, repetindo as operações de pacote |

<p className="tabela-fonte">Fonte: [Christopher Paraizo](https://github.com/wChrstphr), 2026.</p>

Os valores de G1 estão em [`niveis.csv`](../../dados/fase-04/consolidados/niveis.csv), os de G2 em [`G2_metricas_consolidadas.csv`](../../dados/fase-04/consolidados/G2_metricas_consolidadas.csv) e os de G3 em [`G3_metricas_consolidadas.csv`](../../dados/fase-04/consolidados/G3_metricas_consolidadas.csv). G1 não atende só porque [Q1.2](./resultados-g1-manutenibilidade.md#2-q12-reusabilidade) está no nível `--`, com média 1,5. Por isso, só as duas métricas de Q1.2 mudam um julgamento. As demais melhorariam o nível da sua questão, mas G2 e G3 já atendem.

### 1.1 Pontos de atenção de G2

A [análise de G2](./resultados-g2-confiabilidade.md#5-agregação-e-julgamento-do-objetivo-g2) registrou também métricas no nível `o`, fora da regra dos pontos de melhoria:

<p className="tabela-titulo">Tabela 2: Pontos de atenção de G2</p>

| Métrica | Valor e nível | Caminho apontado na análise de G2 |
| :--- | :--- | :--- |
| [M2.3.1](../fase-02/gqm-confiabilidade.md#m231-proporção-de-arquivos-inválidos-tratados-com-mensagem) | 77,78% (7 de 9) `o` | Validar os campos dos elementos na importação de `.excalidraw`, para evitar a tela branca com coordenadas não numéricas (`invalido_06`) e a falha silenciosa com campos obrigatórios ausentes (`invalido_05`) |
| [M2.4.1](../fase-02/gqm-confiabilidade.md#m241-proporção-de-cenários-de-fechamento-com-restauração-do-desenho) | 75,0% `o` | Reduzir o atraso da gravação no armazenamento local, para diminuir a perda em encerramentos abruptos |
| [M2.1.1](../fase-02/gqm-confiabilidade.md#m211-proporção-de-correções-entre-as-contribuições-integradas) | 51,37% `o` | Ligar formalmente os *pull requests* de correção às *issues*, hoje feito em 26,67% deles |

<p className="tabela-fonte">Fonte: [Luiz Henrique Soares](https://github.com/luizh-gsoares), 2026.</p>

### 1.2 Pontos de atenção de G3

A [análise de G3](./resultados-g3-flexibilidade.md#6-pontos-de-melhoria-e-de-atenção) registrou três métricas no nível `o` ou acima:

<p className="tabela-titulo">Tabela 3: Pontos de atenção de G3</p>

| Métrica | Valor e nível | Caminho apontado na análise de G3 | Tamanho |
| :--- | :--- | :--- | :--- |
| [M3.3.2](../fase-02/gqm-flexibilidade.md#m332-proporção-de-passos-documentados-reproduzidos-sem-ajuste) | 85,7% `+` | Trocar `docker-compose up --build -d` por `docker compose up --build -d` no guia `development.mdx`. Com isso, M3.3.2 chega a 100% `++` e Q3.3 a média 4,0 | Pequeno: uma linha de documentação, mas numa página que não é mais publicada ([seção 4](#4-documentação-oficial-fora-do-repositório)) |
| [M3.1.2](../fase-02/gqm-flexibilidade.md#m312-proporção-de-ambientes-de-integração-com-sucesso) | 66,7% `o` | Alinhar o pacote às versões de React que ele declara aceitar, 17, 18 e 19: deixar de importar `useId` e `useDeferredValue`, ausentes no React 17, e de gerar o JSX só para o runtime do React 19, ou declarar apenas o React 19. Desativar o SSR (`ssr: false`) trata só a dependência do DOM e não corrige essas falhas | Grande: muda o build do pacote ou as versões de React aceitas |
| [M3.2.2](../fase-02/gqm-flexibilidade.md#m322-taxa-de-quadros-durante-a-edição-por-tamanho-de-cena) | 52 FPS `o` | Particionamento espacial ou virtualização da área visível para cenas acima de 5.000 elementos | Grande: muda o motor de renderização |

<p className="tabela-fonte">Fonte: [Maria Eduarda](https://github.com/eduarda-ogomes), 2026.</p>

---

## 2. Ações escolhidas

### 2.1 Documentar as propriedades de ExcalidrawProps (M1.2.2)

**Ação:** documentar as propriedades de `ExcalidrawProps`, a interface pública do componente da biblioteca, que não têm documentação. No commit avaliado eram 22 de 52, por exemplo `initialState`, `onMount`, `onExport` e `aiEnabled`, listadas em [`M1.2.2_propriedades.csv`](../../dados/fase-04/brutos/M1.2.2_propriedades.csv). No ramo principal, em 16/11/2026, a interface tem 53 propriedades, com a nova `renderEnvironment`, e as mesmas 30 documentadas (56,6%).

**Tipo:** templates técnicos, que a especificação indica quando o problema é ausência ou fragilidade da documentação [[1, p. 3]](#ref-1). A ação disponibiliza o [modelo de documentação de propriedade](#3-modelo-de-documentação-de-propriedade) e o aplica às propriedades sem documentação em um *pull request* para o Excalidraw, nas páginas de propriedades e, quando o comportamento não aparece no nome nem no tipo, em comentários JSDoc do tipo.

**Justificativa:** com 80% ou mais, M1.2.2 chega ao nível `+`. Q1.2 passa então para média 2,5, nível `-`, e G1 para média 3,1, nível `o`, sem nenhuma questão em `--`. Pelo [julgamento](../fase-02/pontuacao-julgamento.md#71-julgamento-de-cada-característica), G1 passa a **atender**. Com 95% ou mais, M1.2.2 chega ao nível `++` e Q1.2 ao nível `o`. M1.2.1 teria o mesmo efeito, mas exigiria uma mudança grande na arquitetura dos pacotes.

**Critério de sucesso:** M1.2.2, medida de novo na base do *pull request* pelo procedimento da [ficha](../fase-02/gqm-manutenibilidade.md#m122-proporção-de-propriedades-públicas-documentadas), chega a **80% ou mais**, com meta de 100%. As propriedades são contadas de novo, porque `packages/excalidraw/types.ts` mudou depois do commit avaliado (`e1b7aac`), e o resultado registra essa diferença de base.

### 2.2 Recusar na importação arquivos sem elementos válidos (M2.3.1)

**Ação:** fazer o editor mostrar a mensagem de arquivo inválido quando o arquivo `.excalidraw` tem elementos, mas nenhum deles sobrevive à restauração. Hoje a validação só confere o `type` do arquivo, a lista `elements` e o objeto `appState`. Elementos sem `type`, como os de `invalido_05`, são descartados em silêncio e a cena abre vazia. Coordenadas que não são números, como as de `invalido_06`, passam pela restauração, porque o valor padrão só substitui campos ausentes. A posição de rolagem vira um valor não numérico e a primeira forma desenhada deixa a tela branca.

**Tipo:** modificação no código, que a especificação indica para problemas técnicos objetivos, como confiabilidade [[1, p. 3]](#ref-1). A mudança fica em `packages/excalidraw/data/blob.ts`, reaproveita a mensagem que o editor já mostra para arquivos inválidos e leva um teste de interface.

**Justificativa:** M2.3.1 é o ponto de atenção de G2 com efeito mais direto no usuário. Ela não muda o julgamento, porque G2 já atende, mas leva Q2.3 de 4,0 para 4,5 com 8 de 9 arquivos tratados, ou para 5,0 com 9 de 9. A correção da geometria e da rolagem já está proposta por outro contribuidor nos *pull requests* abertos [#11990](https://github.com/excalidraw/excalidraw/pull/11990) e [#11991](https://github.com/excalidraw/excalidraw/pull/11991). Sem uma regra de recusa, porém, os dois arquivos continuam abrindo sem mensagem. A ação da equipe é só essa regra.

**Critério de sucesso:** `invalido_05` passa a ser tratado só com a regra da equipe, levando M2.3.1 a 8 de 9 (`+`). Numa base que junta a regra aos *pull requests* #11990 e #11991, M2.3.1 chega a **9 de 9** (`++`). A coleta repete o procedimento da [ficha](../fase-02/gqm-confiabilidade.md#m231-proporção-de-arquivos-inválidos-tratados-com-mensagem) com os mesmos nove arquivos, automatizada no navegador, e o resultado registra a mudança de procedimento e de base.

### 2.3 Oportunidades não escolhidas

A ação de [M3.4.3](../fase-02/gqm-flexibilidade.md#m343-proporção-dos-campos-do-formato-excalidraw-documentados), proposta por Maria Eduarda na coleta de G3, documentaria em `dev-docs/docs/codebase/json-schema.mdx` os 38 campos listados em [`M3.4.3_conferencia_campos.csv`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.3_conferencia_campos.csv), criaria o esquema formal `packages/excalidraw/schema/excalidraw.schema.json` e verificaria na CI que um campo novo nos tipos atualiza o esquema. Ela não foi escolhida porque G3 já atende, a mudança completa exigiria discutir antes com os mantenedores [[3]](#ref-3) e a parte de documentação cairia numa página que não é mais publicada. O esquema formal continua sendo a forma mais completa de evitar falhas como as de M2.3.1.

M2.1.3 depende de uma decisão de processo dos mantenedores e só poderia ser medida com seis meses de contribuições futuras.

---

## 3. Modelo de documentação de propriedade

Cada propriedade de `ExcalidrawProps` é documentada com quatro campos:

<p className="tabela-titulo">Tabela 4: Campos do modelo de documentação de propriedade</p>

| Campo | Conteúdo |
| :--- | :--- |
| Tipo | O tipo declarado em `ExcalidrawProps`, ou a assinatura da função para *callbacks*. |
| Valor padrão | O valor que o componente usa quando a propriedade é omitida. Só é preenchido quando o código define um. |
| Descrição | O propósito da propriedade e quando ela é lida, por exemplo só na montagem ou a cada renderização, tirados do código que a usa. |
| Exemplo | Um uso curto em JSX, quando o tipo sozinho não mostra como usar a propriedade. |

<p className="tabela-fonte">Fonte: [Christopher Paraizo](https://github.com/wChrstphr), 2026.</p>

O modelo é aplicado em dois lugares. Na documentação para desenvolvedores, cada propriedade ganha uma linha na tabela de `dev-docs/docs/@excalidraw/excalidraw/api/props/props.mdx`, com nome, tipo, valor padrão e descrição curta, e uma seção própria com a descrição completa. No código, ganha um comentário JSDoc em `packages/excalidraw/types.ts` só quando tem um comportamento que o nome e o tipo não mostram, para que o comentário não repita a declaração. O JSDoc vai para as definições de tipo publicadas no pacote e aparece no editor de quem integra a biblioteca. Para a propriedade `theme`, já documentada, o modelo fica assim:

```md
| [`theme`](#theme) | `"light"` &#124; `"dark"` | `"light"` | The theme of the Excalidraw component |
```

```ts
/**
 * The theme of the Excalidraw component. When supplied, it takes precedence
 * over `initialData.appState.theme`.
 * @default "light"
 * @example <Excalidraw theme="dark" />
 */
theme?: Theme;
```

---

## 4. Documentação oficial fora do repositório

A documentação para desenvolvedores do Excalidraw mudou para `plus.excalidraw.com/docs/sdk`. O `README.md` da pasta `dev-docs`, no ramo principal em 17/11/2026, avisa que todas as páginas antigas redirecionam para o endereço novo e que mudanças na pasta não são mais publicadas [[4]](#ref-4). O site novo não indica onde fica o seu código-fonte.

Isso não muda a medição de M1.2.2, cuja ficha conta as páginas da pasta `dev-docs`, mas limita o alcance da documentação escrita ali. A página de propriedades do site novo, consultada em 18/11/2026, também não lista propriedades como `className`, `initialState` e `onThemeChange` [[5]](#ref-5). Por isso o *pull request* de M1.2.2 se oferece para levar o conteúdo ao site novo, e as propriedades de comportamento menos óbvio ganham JSDoc, que chega a quem usa o pacote. A mesma limitação vale para as melhorias de M3.4.3 e de M3.3.2, que também mudam páginas da pasta `dev-docs`.

---

## 5. Resultado das ações

As duas medições usam como base o commit `9fbeaed` do ramo principal, de 17/11/2026, e não o commit avaliado `e1b7aac`, porque os *pull requests* precisam partir do código atual. Os dados brutos estão em [`acao-melhoria/`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/tree/main/dados/fase-04/brutos/acao-melhoria).

### 5.1 M1.2.2

O [*pull request* #12673](https://github.com/excalidraw/excalidraw/pull/12673) documenta as 23 propriedades que faltavam em `props.mdx` e acrescenta JSDoc a seis delas. As propriedades foram contadas de novo pelo procedimento da [ficha](../fase-02/gqm-manutenibilidade.md#m122-proporção-de-propriedades-públicas-documentadas), antes e depois da mudança:

<p className="tabela-titulo">Tabela 5: M1.2.2 antes e depois da ação</p>

| Medição | Commit | Documentadas | Valor e nível |
| :--- | :--- | :---: | :--- |
| Antes | `9fbeaed` | 30 de 53 | [56,6%](../../dados/fase-04/brutos/acao-melhoria/M1.2.2/M1.2.2_propriedades_antes.csv) `-` |
| Depois | `23cfe40` | 53 de 53 | [100%](../../dados/fase-04/brutos/acao-melhoria/M1.2.2/M1.2.2_propriedades_depois.csv) `++` |

<p className="tabela-fonte">Fonte: [Christopher Paraizo](https://github.com/wChrstphr), 2026.</p>

`onExcalidrawAPI` e `onPointerUp` continuam contadas como documentadas por páginas com outro nome, o mesmo julgamento da coleta original. Com M1.2.2 no nível `++`, Q1.2 passa para média (1 + 5) ÷ 2 = 3,0, nível `o`, e G1 para (3,3 + 3,0 + 3,0 + 3,0 + 3,7) ÷ 5 = 3,2, nível `o`, sem nenhuma questão em `--`. Pelo [julgamento](../fase-02/pontuacao-julgamento.md#71-julgamento-de-cada-característica), G1 passaria a **atender** com a mudança incorporada. O julgamento publicado em [resultados de G1](./resultados-g1-manutenibilidade.md) continua sendo o do commit avaliado. O critério de sucesso, 80% ou mais, foi atingido.

Na revisão das propriedades, a ação encontrou um defeito: `objectsSnapModeEnabled` está declarada em `ExcalidrawProps`, mas o componente não a repassa ao editor e ela não tem efeito. A documentação registra esse comportamento.

### 5.2 M2.3.1

O [*pull request* #12674](https://github.com/excalidraw/excalidraw/pull/12674) adiciona a regra e um teste com quatro casos. A coleta foi repetida em três versões do editor, todas no fork [`wChrstphr/excalidraw-fork`](https://github.com/wChrstphr/excalidraw-fork), com os mesmos nove arquivos inválidos:

<p className="tabela-titulo">Tabela 6: M2.3.1 nas três versões do editor</p>

| Versão | Commit | Casos tratados | Valor e nível |
| :--- | :--- | :---: | :--- |
| Base | `9fbeaed` | 6 de 9 | [66,67%](../../dados/fase-04/brutos/acao-melhoria/M2.3.1/antes/M2.3.1_casos.csv) `o` |
| Base com a regra | `adfc0f0` | 7 de 9 | [77,78%](../../dados/fase-04/brutos/acao-melhoria/M2.3.1/regra/M2.3.1_casos.csv) `o` |
| Base com a regra e os *pull requests* #11990 e #11991 | `a176e93` | 8 de 9 | [88,89%](../../dados/fase-04/brutos/acao-melhoria/M2.3.1/medicao/M2.3.1_casos.csv) `+` |

<p className="tabela-fonte">Fonte: [Christopher Paraizo](https://github.com/wChrstphr), 2026.</p>

Só com a regra, `invalido_05` passa a mostrar a mensagem de arquivo inválido. Com os dois *pull requests* de outro contribuidor, `invalido_06` também, em vez de deixar a tela branca ao inserir um texto. Q2.3 passa para média (4 + 5) ÷ 2 = 4,5, arredondada para o nível `+`, e G2 para (3,0 + 4,5 + 4,5 + 4,0) ÷ 4 = 4,0, nível `+`. O julgamento de G2 não muda, porque a característica já atende.

O critério de sucesso foi atingido em parte. `invalido_05` é tratado só com a regra, mas M2.3.1 chega a 8 de 9, e não a 9 de 9, por causa de `invalido_08`. Ao arrastar um PNG sem cena para o editor, o código insere o arquivo como imagem e não mostra mensagem. Esse comportamento é intencional e já existia no commit avaliado. A captura da coleta original, [`M2.3.1_invalido_08_arrastar.png`](../../dados/fase-04/brutos/Q2.3-tolerancia-a-falhas/M2.3.1_prints/M2.3.1_invalido_08_arrastar.png), mostra a mesma imagem inserida, embora a planilha registre uma mensagem. Pela ficha, o caso não é tratado. M2.3.1 no commit avaliado seria então 6 de 9, e não 7 de 9, no mesmo nível `o`, sem mudar Q2.3 nem o julgamento de G2.

A coleta seguiu o procedimento da [ficha](../fase-02/gqm-confiabilidade.md#m231-proporção-de-arquivos-inválidos-tratados-com-mensagem), com três desvios. Foi automatizada pelo script [`coleta_m231_playwright.py`](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/blob/main/scripts/coleta_m231_playwright.py), no Firefox 159.0 sem interface, com capturas de cada tentativa. O editor rodou no servidor de desenvolvimento, e não no contêiner Docker, para expor a cena ao script. Depois do retângulo, o script também insere um texto, porque é nesse passo que `invalido_06` deixa a tela branca, como na coleta original.

---

## Referências

> <Link id="ref-1">1.</Link> RAMOS, Cristiane Soares. **2026-2 Trabalho final completo v1**. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Página 3. Disponível no Moodle da disciplina.
>
> <Link id="ref-2">2.</Link> RAMOS, Cristiane Soares. **AULA 08 QSW1 GQM**. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Página 60. Disponível no Moodle da disciplina.
>
> <Link id="ref-3">3.</Link> EXCALIDRAW. Contributing. *Excalidraw SDK docs*. Disponível em: [https://plus.excalidraw.com/docs/sdk/contributing](https://plus.excalidraw.com/docs/sdk/contributing). Acesso em: 18 nov. 2026.
>
> <Link id="ref-4">4.</Link> EXCALIDRAW. dev-docs/README.md. *Repositório excalidraw/excalidraw*, commit `9fbeaed`. Disponível em: [https://github.com/excalidraw/excalidraw/blob/9fbeaed54aaad8dc06d32ba176a9bc20fb827109/dev-docs/README.md](https://github.com/excalidraw/excalidraw/blob/9fbeaed54aaad8dc06d32ba176a9bc20fb827109/dev-docs/README.md). Acesso em: 18 nov. 2026.
>
> <Link id="ref-5">5.</Link> EXCALIDRAW. Props. *Excalidraw SDK docs*. Disponível em: [https://plus.excalidraw.com/docs/sdk/excalidraw/api/props](https://plus.excalidraw.com/docs/sdk/excalidraw/api/props). Acesso em: 18 nov. 2026.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 15/11/2026 | Criação da proposta de oportunidades de G1 e G3, dos pontos de atenção de G3 levantados por Maria Eduarda, da ação proposta, do critério de sucesso e da avaliação do tamanho | [Christopher Paraizo](https://github.com/wChrstphr) | |
| 1.1 | 17/11/2026 | Correção da proposta para M3.1.2, que tratava a desativação do SSR como alternativa às falhas de hooks e de runtime JSX, conforme a revisão do PR | [Christopher Paraizo](https://github.com/wChrstphr) | |
| 1.2 | 18/11/2026 | Inclusão das oportunidades e dos pontos de atenção de G2, registro das duas ações escolhidas (M1.2.2 e M2.3.1) com critérios de sucesso, modelo de documentação de propriedade e nota sobre a mudança da documentação oficial | [Christopher Paraizo](https://github.com/wChrstphr) | |
| 1.3 | 18/11/2026 | Registro do resultado das duas ações, com os *pull requests* enviados ao Excalidraw, as medições antes e depois, o efeito nos julgamentos e a divergência de `invalido_08` na coleta original | [Christopher Paraizo](https://github.com/wChrstphr) | |
