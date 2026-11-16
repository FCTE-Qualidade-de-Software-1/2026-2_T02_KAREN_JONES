---
sidebar_position: 10
title: Oportunidades de melhoria
description: Proposta de pontos de melhoria de G1 e G3, pontos de atenção de G3, critérios de priorização, ação proposta, critério de sucesso e avaliação do tamanho da mudança
---

import Link from '@docusaurus/Link';

# Oportunidades de melhoria

## Introdução

A avaliação deve terminar com oportunidades de melhoria baseadas nas métricas e nos julgamentos, e com pelo menos uma ação executada, justificada pelas evidências [[1, p. 3]](#ref-1). Na interpretação do GQM, é a equipe que traduz as conclusões em ações [[2, p. 60]](#ref-2). Esta página lista os pontos de melhoria de [G1](./resultados-g1-manutenibilidade.md) e [G3](./resultados-g3-flexibilidade.md) e propõe a ação a executar. É uma proposta para a decisão conjunta da equipe, prevista no [plano de análise](../fase-03/plano-analise.md#6-interpretação-e-revisão), e a versão final da página registra a escolha.

A ação proposta é documentar as propriedades públicas da biblioteca que estão sem documentação ([M1.2.2](../fase-02/gqm-manutenibilidade.md#m122-proporção-de-propriedades-públicas-documentadas)). É a única oportunidade pequena que muda o julgamento de uma característica: com ela, a manutenibilidade passa a atender.

## Metodologia

As oportunidades são as métricas nos níveis `-` e `--`, que a [regra dos pontos de melhoria](../fase-02/pontuacao-julgamento.md#73-pontos-de-melhoria) registra com a questão e a subcaracterística afetadas. Cada uma foi comparada por três critérios:

- **Efeito no julgamento:** se levar a métrica para o nível seguinte, ou ao necessário, muda o julgamento da característica, calculado pela [agregação](../fase-02/pontuacao-julgamento.md#6-agregação-da-métrica-à-característica) e pelo [julgamento](../fase-02/pontuacao-julgamento.md#71-julgamento-de-cada-característica) da Fase 02.
- **Tamanho da mudança:** se cabe em um *pull request* pequeno ou exige discutir antes com os mantenedores, como o guia de contribuição do Excalidraw pede para mudanças grandes [[3]](#ref-3).
- **Medição antes e depois:** se a métrica pode ser medida de novo na base do *pull request*, pelo mesmo procedimento da ficha, dentro do prazo da avaliação.

Os tipos de ação seguem a especificação do trabalho: protótipo de alta fidelidade, modificação no código, templates técnicos ou processo de desenvolvimento [[1, p. 3]](#ref-1). As oportunidades de [G2](../fase-02/gqm-confiabilidade.md) entram na versão 1.1 desta página, depois da [análise de G2](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/116).

---

## 1. Oportunidades

<p className="tabela-titulo">Tabela 1: Pontos de melhoria de G1 e G3</p>

| Métrica | Valor e nível | Questão | Efeito no julgamento | Tamanho | Medição antes e depois |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [M1.2.2](../fase-02/gqm-manutenibilidade.md#m122-proporção-de-propriedades-públicas-documentadas) | 57,69% `-` | Q1.2 Reusabilidade | Com 80% ou mais, G1 passa a atender | Pequeno: só documentação | Sim, com o mesmo formulário |
| [M1.2.1](../fase-02/gqm-manutenibilidade.md#m121-arquivos-de-pacotes-de-base-com-dependência-de-react-ou-do-navegador) | 69,07% `--` | Q1.2 Reusabilidade | Com 20% ou menos, G1 passa a atender | Grande: tirar a dependência do navegador de 48 dos 67 arquivos | Sim, com o script de cálculo |
| [M1.1.1](../fase-02/gqm-manutenibilidade.md#m111-ciclos-de-dependência-entre-pacotes) | 4 pares `-` | Q1.1 Modularidade | Nenhum, porque Q1.2 continua em `--` | Grande: muda a divisão entre pacotes | Sim, com o script de cálculo |
| [M1.3.1](../fase-02/gqm-manutenibilidade.md#m131-perfil-de-risco-de-complexidade-das-funções) | 6,54% em risco muito alto `--` | Q1.3 Analisabilidade | Nenhum, porque Q1.2 continua em `--` | Grande: refatorar as funções mais complexas | Sim, com o ESLint |
| [M1.4.3](../fase-02/gqm-manutenibilidade.md#m143-proporção-de-contribuições-que-alteram-arquivos-extensos) | 65,75% `--` | Q1.4 Modificabilidade | Nenhum, porque Q1.2 continua em `--` | Grande: dividir os arquivos extensos | Não: depende de seis meses de contribuições futuras |
| [M3.4.3](../fase-02/gqm-flexibilidade.md#m343-proporção-dos-campos-do-formato-excalidraw-documentados) | 26,9% `-` | Q3.4 Substituibilidade | Nenhum, porque G3 já atende | Grande: esquema do formato, verificação na CI e documentação | Sim, com a conferência dos campos |
| [M3.3.1](../fase-02/gqm-flexibilidade.md#m331-proporção-de-operações-de-pacote-bem-sucedidas) | 33,3% `-` | Q3.3 Instalabilidade | Nenhum, porque G3 já atende | Médio: o pacote depende de `@excalidraw/common`, que não é publicado, e a análise de G3 aponta a publicação sincronizada dos subpacotes | Sim, repetindo as operações de pacote |

<p className="tabela-fonte">Fonte: [Christopher Paraizo](https://github.com/wChrstphr), 2026.</p>

Os valores de G1 estão em [`niveis.csv`](../../dados/fase-04/consolidados/niveis.csv) e os de G3 em [`G3_metricas_consolidadas.csv`](../../dados/fase-04/consolidados/G3_metricas_consolidadas.csv). G1 não atende só porque [Q1.2](./resultados-g1-manutenibilidade.md#2-q12-reusabilidade) está no nível `--`, com média 1,5. Por isso, só as duas métricas de Q1.2 mudam o julgamento. As demais melhorariam o nível da sua questão, mas não o de G1 nem o de G3.

### 1.1 Pontos de atenção de G3

A [análise de G3](./resultados-g3-flexibilidade.md#6-pontos-de-melhoria-e-de-atenção) registrou também três métricas no nível `o` ou acima, fora da regra dos pontos de melhoria. Elas não mudam o julgamento de G3, mas entram na decisão da equipe:

<p className="tabela-titulo">Tabela 2: Pontos de atenção de G3</p>

| Métrica | Valor e nível | Caminho apontado na análise de G3 | Tamanho |
| :--- | :--- | :--- | :--- |
| [M3.3.2](../fase-02/gqm-flexibilidade.md#m332-proporção-de-passos-documentados-reproduzidos-sem-ajuste) | 85,7% `+` | Trocar `docker-compose up --build -d` por `docker compose up --build -d` no guia `development.mdx`. Com isso, M3.3.2 chega a 100% `++` e Q3.3 a média 4,0 | Pequeno: uma linha de documentação, ainda presente no ramo principal em 15/11/2026 |
| [M3.1.2](../fase-02/gqm-flexibilidade.md#m312-proporção-de-ambientes-de-integração-com-sucesso) | 66,7% `o` | Adotar o React 19 ou isolar a biblioteca no cliente (`ssr: false`) no Next.js com React 17 e 18 | Grande: muda o build do pacote ou as versões de React aceitas |
| [M3.2.2](../fase-02/gqm-flexibilidade.md#m322-taxa-de-quadros-durante-a-edição-por-tamanho-de-cena) | 52 FPS `o` | Particionamento espacial ou virtualização da área visível para cenas acima de 5.000 elementos | Grande: muda o motor de renderização |

<p className="tabela-fonte">Fonte: [Maria Eduarda](https://github.com/eduarda-ogomes), 2026.</p>

---

## 2. Ação proposta

**Ação:** documentar as propriedades de `ExcalidrawProps`, a interface pública do componente da biblioteca, que não têm documentação. São 22 de 52, por exemplo `initialState`, `onMount`, `onExport` e `aiEnabled`. A lista completa está em [`M1.2.2_propriedades.csv`](../../dados/fase-04/brutos/M1.2.2_propriedades.csv).

**Tipo:** templates técnicos, que a especificação indica quando o problema é ausência ou fragilidade da documentação [[1, p. 3]](#ref-1). A ação propõe um modelo de entrada para documentar uma propriedade, com tipo, valor padrão, descrição e exemplo. Esse modelo é aplicado às propriedades sem documentação em um *pull request* para o Excalidraw e fica disponível para as próximas propriedades.

**Justificativa:** M1.2.2 vale 57,69% (30 de 52), no nível `-`. Com mais 12 propriedades documentadas, o valor chega a 80,77% (42 de 52), no nível `+`. Q1.2 passa então para média 2,5, nível `-`, e G1 para média 3,1, nível `o`, sem nenhuma questão em `--`. Pelo [julgamento](../fase-02/pontuacao-julgamento.md#71-julgamento-de-cada-característica), G1 passa a **atender**. Com 20 propriedades, M1.2.2 chega ao nível `++` e Q1.2 ao nível `o`. M1.2.1 teria o mesmo efeito, mas exigiria uma mudança grande na arquitetura dos pacotes.

A lacuna continua no ramo principal do Excalidraw. Em 15/11/2026, pelo menos 19 das 22 propriedades não aparecem nas páginas de `dev-docs/docs/@excalidraw/excalidraw/api/props/`.

---

## 3. Critério de sucesso

Se escolhida, a ação dá certo se M1.2.2, medida de novo na base do *pull request*, chegar a **80% ou mais**, o valor em que G1 passa a atender. A meta é 100%. A nova medição segue o procedimento da [ficha de M1.2.2](../fase-02/gqm-manutenibilidade.md#m122-proporção-de-propriedades-públicas-documentadas) e conta de novo as propriedades de `ExcalidrawProps`, porque `packages/excalidraw/types.ts` mudou depois do fim da janela de coleta. O resultado registra que essa base é diferente do commit avaliado (`e1b7aac`).

---

## 4. Tamanho da mudança

A mudança altera só a documentação, nas páginas de propriedades da API, sem tocar no código. O guia de contribuição do Excalidraw pede uma issue antes só para mudanças grandes e aceita alterações apenas de documentação com o prefixo `docs` no título [[3]](#ref-3). Por isso, a ação é tratada como um *pull request* pequeno, sem issue prévia. Depois da decisão da equipe, a execução é feita na [execução da ação de melhoria](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/119), que registra o resultado nesta página.

---

## 5. Segunda recomendação

Como alternativa para a decisão da equipe, fica a ação proposta por Maria Eduarda na coleta de G3 para [M3.4.3](../fase-02/gqm-flexibilidade.md#m343-proporção-dos-campos-do-formato-excalidraw-documentados). Ela tem três partes:

1. Documentar em `dev-docs/docs/codebase/json-schema.mdx` os 38 campos sem documentação listados em [`M3.4.3_conferencia_campos.csv`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.3_conferencia_campos.csv). O exemplo da página ainda resume os elementos com `/* ...other element properties */` no ramo principal em 15/11/2026.
2. Criar o esquema formal `packages/excalidraw/schema/excalidraw.schema.json`, em JSON Schema, que o repositório ainda não tem.
3. Verificar na CI que um campo novo nos tipos do TypeScript atualiza o esquema.

Só a primeira parte já leva M3.4.3 de 26,9% para 100%, no nível `++`. Q3.4 passa de 3,7 para 4,7, e G3 de 3,9 para 4,1, que continua no nível `+`. O esquema e a verificação na CI mantêm a documentação em dia depois da mudança.

Ela não é a primeira proposta por dois motivos. G3 já atende, e a mudança completa é grande, porque cria um arquivo novo no repositório e uma verificação automática. Por isso, exigiria discutir antes com os mantenedores [[3]](#ref-3). Se a equipe preferir uma ação em G3 que caiba em um *pull request* pequeno, a primeira parte, sozinha, cumpre esse papel.

---

## Referências

> <Link id="ref-1">1.</Link> RAMOS, Cristiane Soares. **2026-2 Trabalho final completo v1**. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Página 3. Disponível no Moodle da disciplina.
>
> <Link id="ref-2">2.</Link> RAMOS, Cristiane Soares. **AULA 08 QSW1 GQM**. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Página 60. Disponível no Moodle da disciplina.
>
> <Link id="ref-3">3.</Link> EXCALIDRAW. Contributing. *Excalidraw developer docs*. Seções "Contributing" e "Title". Disponível em: [https://docs.excalidraw.com/docs/introduction/contributing](https://docs.excalidraw.com/docs/introduction/contributing). Acesso em: 15 nov. 2026.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 15/11/2026 | Criação da proposta de oportunidades de G1 e G3, dos pontos de atenção de G3 levantados por Maria Eduarda, da ação proposta, do critério de sucesso e da avaliação do tamanho | [Christopher Paraizo](https://github.com/wChrstphr) | |
