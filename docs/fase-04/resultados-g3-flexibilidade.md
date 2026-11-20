---
sidebar_position: 3
title: "Resultados e julgamento: Flexibilidade (G3)"
description: Relatório formal de avaliação e julgamento do objetivo G3 (Flexibilidade) do Excalidraw, consolidando a obtenção das medidas, as descobertas técnicas da coleta, as respostas às questões GQM, o confronto de hipóteses e os pontos de melhoria.
---

import Link from '@docusaurus/Link';

# Resultados e julgamento: Flexibilidade (G3)

## Introdução

Este documento apresenta o relatório formal de avaliação da qualidade para o objetivo G3 (Flexibilidade), executado sobre o software Excalidraw fixado no commit `e1b7aacb356a492aa1e0fc6eb57b8896124027f0`. A página reúne os resultados e as descobertas técnicas da coleta, responde às questões do GQM, confronta as hipóteses e emite o julgamento da característica.

## Metodologia

A avaliação seguiu o método Goal-Question-Metric (GQM) estruturado na Fase 02, em consonância com o modelo de qualidade de software ISO/IEC 25010:2023 e a sistemática de agregação de Heitlager, Kuipers e Visser [[1, p. 8]](#ref-1). A coleta empírica envolveu doze métricas distribuídas em quatro subcaracterísticas: Adaptabilidade, Escalabilidade, Instalabilidade e Substituibilidade. Os dados brutos foram obtidos por meio de testes automatizados, perfis de desempenho gravados no painel Performance do navegador, execução conteinerizada em Docker e testes manuais de ergonomia em dispositivo móvel. As fraquezas mapeadas durante o processo foram registradas como pontos de melhoria e de atenção, que alimentam as [oportunidades de melhoria](./melhorias.md).

---

## 1. Identificação e contexto da avaliação

<p className="tabela-titulo">Tabela 1: Parâmetros do ambiente e contexto da execução</p>

| Parâmetro | Detalhes do ambiente e da execução |
| :--- | :--- |
| **Objetivo avaliado** | G3: Flexibilidade (Adaptabilidade, Escalabilidade, Instalabilidade, Substituibilidade) |
| **Avaliadora responsável** | Maria Eduarda ([@eduarda-ogomes](https://github.com/eduarda-ogomes)) |
| **Software avaliado** | Excalidraw (commit exato `e1b7aacb356a492aa1e0fc6eb57b8896124027f0`) |
| **Período de execução** | 10 a 11 de novembro de 2026 |
| **Sistema operacional** | Zorin OS 18.1 (Kernel Linux 7.0.0-34-generic x86_64, base Ubuntu 24.04 LTS) |
| **Hardware da avaliadora** | AMD Ryzen 7 5700U with Radeon Graphics, 10 GB de RAM utilizáveis (16 GB instalados) |
| **Dispositivo móvel** | Apple iPad (A16) e Caneta Stylus Capacitiva Goojodoq |
| **Ambiente de testes** | Contêiner Docker oficial (Nginx 1.30.2, porta `3000:80`) e Node.js 24.16.0 com Yarn 1.22.22 |
| **Navegador** | Google Chrome em [M3.2.1](../fase-02/gqm-flexibilidade.md#m321-tempo-de-abertura-por-tamanho-de-cena) e [M3.2.2](../fase-02/gqm-flexibilidade.md#m322-taxa-de-quadros-durante-a-edição-por-tamanho-de-cena), versão não registrada (ver [desvios](#11-desvios-das-instruções)) |
| **Repositório de dados brutos** | `dados/fase-04/brutos/` |
| **Tabelas consolidadas** | `dados/fase-04/consolidados/` |

<p className="tabela-fonte">Fonte: [Maria Eduarda](https://github.com/eduarda-ogomes), 2026.</p>

### 1.1 Desvios das instruções

Os [recursos e ambiente](../fase-03/recursos-ambiente.md#3-máquinas-dos-responsáveis-pela-coleta) fixam o Mozilla Firefox 159.0.1 para todos os testes no navegador. As medições de [M3.2.1](../fase-02/gqm-flexibilidade.md#m321-tempo-de-abertura-por-tamanho-de-cena) e [M3.2.2](../fase-02/gqm-flexibilidade.md#m322-taxa-de-quadros-durante-a-edição-por-tamanho-de-cena) usaram o Google Chrome: os traces de abertura (`traces_abertura/`) foram gravados pelo DevTools do Chrome, e as observações de [`M3.2.1_tempos_abertura.csv`](../../dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.1_tempos_abertura.csv) citam o Chrome. A versão do navegador não foi registrada nos dados brutos nem nos metadados dos traces. Por isso, os tempos e as taxas de quadros de [Q3.2](../fase-02/gqm-flexibilidade.md#4-q32-escalabilidade) não são comparáveis a uma medição no navegador fixado, como prevê o [4º quadrante da abstraction sheet de G3](../fase-02/abstraction-sheets.md#4-g3-flexibilidade).

A coleta de [M3.1.2](../fase-02/gqm-flexibilidade.md#m312-proporção-de-ambientes-de-integração-com-sucesso) divergiu das [instruções do avaliador](../fase-03/instrucoes-g3-flexibilidade.md#22-m312-proporção-de-ambientes-de-integração-com-sucesso) em quatro pontos, conforme os [logs de build](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.2_build_logs.zip):

- O pacote instalado foi o tarball 0.18.0 gerado pelo commit avaliado, o mesmo registrado no [log de M3.3.1](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.1_log_operacoes_pacote.txt), e não o 0.17.6 citado nas instruções.
- A Comb4 (React 17) usou o Next.js 12.3.4.
- A Comb5 (React 18) usou o Next.js 14.2.15.
- A Comb6 (React 19) usou o exemplo `examples/with-nextjs` do monorepo, com Next.js 14.1.4, em vez de um projeto criado com `create-next-app`.

---

## 2. Painel consolidado das medições

A tabela abaixo sintetiza os valores empíricos medidos para as doze métricas do objetivo G3, convertidos para os níveis da [Fase 02 (Pontuação e julgamento)](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3), baseados no modelo de Heitlager, Kuipers e Visser [[1, p. 8]](#ref-1) na escala de 1 a 5 pontos:

<p className="tabela-titulo">Tabela 2: Painel consolidado das medições de flexibilidade (G3)</p>

| Métrica | Nome da métrica | Questão | Valor medido | Nível na régua | Escala (1 a 5) | Hipótese | Status | Dado bruto auditável |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **[M3.1.1](../fase-02/gqm-flexibilidade.md#m311-cobertura-de-usuários-pelos-navegadores-declarados)** | Cobertura de usuários por navegadores declarados | [Q3.1](../fase-02/gqm-flexibilidade.md#3-q31-adaptabilidade) | **88,94%** | **Bom** (`+`) | 4,00 | [H3.1.1](../fase-02/gqm-flexibilidade.md#3-q31-adaptabilidade) ≥ 80% | **Confirmada** | [`M3.1.1_cobertura_browserslist.txt`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.1_cobertura_browserslist.txt) |
| **[M3.1.2](../fase-02/gqm-flexibilidade.md#m312-proporção-de-ambientes-de-integração-com-sucesso)** | Proporção de ambientes de integração com sucesso | [Q3.1](../fase-02/gqm-flexibilidade.md#3-q31-adaptabilidade) | **83,3%** (5 de 6) | **Bom** (`+`) | 4,00 | [H3.1.2](../fase-02/gqm-flexibilidade.md#3-q31-adaptabilidade) = 6 de 6 | **Refutada** | [`M3.1.2_matriz_integracao.csv`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.2_matriz_integracao.csv) |
| **[M3.1.3](../fase-02/gqm-flexibilidade.md#m313-proporção-de-ações-de-edição-que-funcionam-por-toque-e-caneta)** | Proporção de ações de edição por toque e caneta | [Q3.1](../fase-02/gqm-flexibilidade.md#3-q31-adaptabilidade) | **100,0%** (10 de 10) | **Excelente** (`++`) | 5,00 | [H3.1.3](../fase-02/gqm-flexibilidade.md#3-q31-adaptabilidade) = 10 de 10 | **Confirmada** | [`M3.1.3_formulario_toque_caneta.csv`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.3_formulario_toque_caneta.csv) |
| **[M3.2.1](../fase-02/gqm-flexibilidade.md#m321-tempo-de-abertura-por-tamanho-de-cena)** | Tempo de abertura por tamanho de cena | [Q3.2](../fase-02/gqm-flexibilidade.md#4-q32-escalabilidade) | Medianas: 0,05 s, **0,11 s**, 1,15 s e 1,52 s (100, 1.000, 5.000 e 10.000 elem) | **Bom** (`+`), média das 4 cenas | 4,50 | [H3.2.1](../fase-02/gqm-flexibilidade.md#4-q32-escalabilidade) ≤ 1,0 s (1.000 elem) | **Confirmada** | [`M3.2.1_tempos_abertura.csv`](../../dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.1_tempos_abertura.csv) |
| **[M3.2.2](../fase-02/gqm-flexibilidade.md#m322-taxa-de-quadros-durante-a-edição-por-tamanho-de-cena)** | Taxa de quadros durante edição contínua | [Q3.2](../fase-02/gqm-flexibilidade.md#4-q32-escalabilidade) | Medianas: 60, **52**, 20 e 12 FPS (100, 1.000, 5.000 e 10.000 elem) | **Regular** (`o`), média das 4 cenas | 3,25 | [H3.2.2](../fase-02/gqm-flexibilidade.md#4-q32-escalabilidade) ≥ 48 FPS (1.000 elem) | **Confirmada** | [`M3.2.2_fps_edicao.csv`](../../dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.2_fps_edicao.csv) |
| **[M3.2.3](../fase-02/gqm-flexibilidade.md#m323-tamanho-máximo-de-cena-salva-e-exportada)** | Tamanho máximo de cena salva e exportada | [Q3.2](../fase-02/gqm-flexibilidade.md#4-q32-escalabilidade) | **10.000 elem** | **Excelente** (`++`) | 5,00 | [H3.2.3](../fase-02/gqm-flexibilidade.md#4-q32-escalabilidade) ≥ 5.000 elem | **Confirmada** | [`M3.2.3_tamanho_maximo_salvamento.csv`](../../dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.3_tamanho_maximo_salvamento.csv) |
| **[M3.3.1](../fase-02/gqm-flexibilidade.md#m331-proporção-de-operações-de-pacote-bem-sucedidas)** | Proporção de operações de pacote bem-sucedidas | [Q3.3](../fase-02/gqm-flexibilidade.md#5-q33-instalabilidade) | **33,3%** (3 de 9) | **Ruim** (`-`) | 2,00 | [H3.3.1](../fase-02/gqm-flexibilidade.md#5-q33-instalabilidade) = 9 de 9 | **Refutada** | [`M3.3.1_resultados_pacote.csv`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.1_resultados_pacote.csv) |
| **[M3.3.2](../fase-02/gqm-flexibilidade.md#m332-proporção-de-passos-documentados-reproduzidos-sem-ajuste)** | Proporção de passos documentados reproduzidos | [Q3.3](../fase-02/gqm-flexibilidade.md#5-q33-instalabilidade) | **85,7%** (6 de 7) | **Bom** (`+`) | 4,00 | [H3.3.2](../fase-02/gqm-flexibilidade.md#5-q33-instalabilidade) ≥ 95% | **Refutada** | [`M3.3.2_passos_ajustes.csv`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.2_passos_ajustes.csv) |
| **[M3.3.3](../fase-02/gqm-flexibilidade.md#m333-implantação-com-docker)** | Implantação com Docker | [Q3.3](../fase-02/gqm-flexibilidade.md#5-q33-instalabilidade) | **100,0%** (4 de 4) | **Excelente** (`++`) | 5,00 | [H3.3.3](../fase-02/gqm-flexibilidade.md#5-q33-instalabilidade) = 4 de 4 | **Confirmada** | [`M3.3.3_verificacoes_docker.csv`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.3_verificacoes_docker.csv) |
| **[M3.4.1](../fase-02/gqm-flexibilidade.md#m341-formatos-de-exportação-abertos-disponíveis)** | Formatos de exportação abertos disponíveis | [Q3.4](../fase-02/gqm-flexibilidade.md#6-q34-substituibilidade) | **3 formatos** | **Bom** (`+`) | 4,00 | [H3.4.1](../fase-02/gqm-flexibilidade.md#6-q34-substituibilidade) ≥ 3 | **Confirmada** | [`M3.4.1_catalogo_formatos.csv`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.1_catalogo_formatos.csv) |
| **[M3.4.2](../fase-02/gqm-flexibilidade.md#m342-proporção-de-elementos-preservados-na-exportação-e-reimportação)** | Preservação de elementos na reimportação | [Q3.4](../fase-02/gqm-flexibilidade.md#6-q34-substituibilidade) | **100,00%** | **Excelente** (`++`) | 5,00 | [H3.4.2](../fase-02/gqm-flexibilidade.md#6-q34-substituibilidade) ≥ 95% | **Confirmada** | [`M3.4.2_preservacao_formatos.csv`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.2_preservacao_formatos.csv) |
| **[M3.4.3](../fase-02/gqm-flexibilidade.md#m343-proporção-dos-campos-do-formato-excalidraw-documentados)** | Proporção dos campos do formato documentados | [Q3.4](../fase-02/gqm-flexibilidade.md#6-q34-substituibilidade) | **26,9%** (14 de 52) | **Ruim** (`-`) | 2,00 | [H3.4.3](../fase-02/gqm-flexibilidade.md#6-q34-substituibilidade) < 60% | **Confirmada** | [`M3.4.3_conferencia_campos.csv`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.3_conferencia_campos.csv) |

<p className="tabela-fonte">Fonte: [Maria Eduarda](https://github.com/eduarda-ogomes), 2026.</p>

---

## 3. Análise dos resultados e respostas às questões GQM

### 3.1 Questão Q3.1: Adaptabilidade

> **Pergunta do GQM:** *O software adapta-se satisfatoriamente a diferentes navegadores, frameworks e modos de entrada?*

#### Análise das métricas componentes

- **[M3.1.1](../fase-02/gqm-flexibilidade.md#m311-cobertura-de-usuários-pelos-navegadores-declarados) (Cobertura por navegadores declarados):** A execução do comando `browserslist --coverage` na pasta `excalidraw-app`, conforme as [instruções](../fase-03/instrucoes-g3-flexibilidade.md#21-m311-cobertura-de-usuários-pelos-navegadores-declarados), apontou cobertura de **88,94%** da população global de usuários web. O software suporta navegadores modernos em versões recentes (Chrome, Edge, Firefox, Safari, iOS Safari, Chrome for Android). A regra de produção declarada em `excalidraw-app/package.json` parte de `>0.2%` e `not dead` e exclui de forma explícita navegadores obsoletos, como IE 11 e anteriores, Opera Mini, Safari anterior ao 12, Edge anterior ao 79 e Chrome anterior ao 70. Esse descarte evita polyfills legados no pacote. O percentual fica na faixa **Bom (`+`)** (80% a 95%).
- **[M3.1.2](../fase-02/gqm-flexibilidade.md#m312-proporção-de-ambientes-de-integração-com-sucesso) (Proporção de ambientes de integração com sucesso):** A matriz de seis combinações empíricas (React 17, 18 e 19 combinados com Vite e Next.js) alcançou sucesso em **5 das 6 combinações (83,3%)**, resultando em nível **Bom (`+`)**:
  - No Vite 5.4.11, as três versões do React (17.0.2, 18.2.0 e 19.0.0) compilaram com código de saída 0 em cerca de 12 segundos. O servidor de pré-visualização respondeu com HTTP 200, o canvas carregou sem exceções não tratadas e foi possível desenhar formas, com validação automatizada via Puppeteer-core.
  - No Next.js, o React 18 (Next.js 14.2.15) e o React 19 (Next.js 14.1.4) compilaram com sucesso. O React 19 rodou no exemplo oficial do monorepo (`examples/with-nextjs`), com build de 65 s, com importação dinâmica sem SSR (`dynamic(..., { ssr: false })`) e fontes estáticas na pasta pública.
  - O React 17 falhou no Next.js 12 durante a compilação com Webpack. Embora o `package.json` do `@excalidraw/excalidraw` declare compatibilidade com React 17, 18 e 19, o pacote no commit `e1b7aac` importa os hooks `useId` e `useDeferredValue` diretamente de `react`, e eles inexistem no React 17.
  - O React 18 no Next.js 14.2.15 conta como sucesso: o [log de build](../../dados/fase-04/brutos/Q3.1-adaptabilidade/build_logs/comb5_react18_next_build.log) termina com a compilação e a geração das páginas estáticas (2 de 2) sem erro. O CSV registrava falha em tempo de execução (`Minified React error #31`) que não aparece no log anexado. Prevaleceu a evidência do log.
  - A importação direta com `require('@excalidraw/excalidraw')` no Node.js falha com `ReferenceError: document is not defined`. O pacote depende do DOM do navegador, por isso a desativação de SSR é obrigatória em frameworks com renderização no servidor.
- **[M3.1.3](../fase-02/gqm-flexibilidade.md#m313-proporção-de-ações-de-edição-que-funcionam-por-toque-e-caneta) (Ações de edição por toque e caneta):** A avaliação manual no Apple iPad (A16) registrou **100% de sucesso (10 de 10 ações)** tanto por toque direto com o dedo quanto com a caneta stylus Goojodoq. O iPad acessou o contêiner oficial pela rede local. A aplicação detecta toques com fidelidade, diferencia desenho livre com a caneta e suporta gestos multitoque de pinça (zoom) sem travamentos. Com a ferramenta de seleção ativa, o arraste com um dedo é reservado à seleção por caixa, e o deslocamento da tela exige dois dedos. Com a ferramenta Mão, um dedo basta. O uso híbrido, desenhando com a caneta e navegando com os dedos, alterna sem atraso perceptível.

#### Resposta formal à questão Q3.1

> **Resposta:** **Sim, de forma satisfatória e com ressalvas conhecidas.** O Excalidraw apresenta excelente suporte a dispositivos táteis e móveis (100% no iPad) e ampla cobertura da base global de navegadores (88,94%). Todavia, a adaptabilidade como componente React em aplicações com renderização híbrida ou SSR (Next.js) requer atenção. Integradores que utilizem React 17 no Next.js enfrentam incompatibilidade em tempo de compilação, porque o pacote importa hooks que essa versão não tem. O isolamento da biblioteca no lado do cliente (`ssr: false`) é necessário pela dependência do DOM, mas não corrige a ausência dos hooks no React 17.
> 
> **Pontuação de [Q3.1](../fase-02/gqm-flexibilidade.md#3-q31-adaptabilidade):** Média de **4,3 pontos** (Nível **Bom `+`**).

---

### 3.2 Questão Q3.2: Escalabilidade

> **Pergunta do GQM:** *O software mantém desempenho aceitável com aumento no volume de dados da cena?*

#### Análise das métricas componentes

- **[M3.2.1](../fase-02/gqm-flexibilidade.md#m321-tempo-de-abertura-por-tamanho-de-cena) (Tempo de abertura por tamanho de cena):** Avaliado por 20 perfis de desempenho DevTools em 4 escalas (100, 1.000, 5.000 e 10.000 elementos, com 5 repetições cada). As medianas registradas foram:
  - 100 elementos: **0,05 s** (Nível `++`).
  - 1.000 elementos: **0,11 s** (Nível `++`).
  - 5.000 elementos: **1,15 s** (Nível `+`).
  - 10.000 elementos: **1,52 s** (Nível `+`).

  O tempo não cresce na mesma proporção do volume: sobe cerca de 10 vezes de 1.000 para 5.000 elementos (de 0,11 s para 1,15 s) e cerca de 1,3 vez de 5.000 para 10.000 elementos (de 1,15 s para 1,52 s). A cena de 1.000 elementos abriu em apenas 0,11 s, abaixo do limite de 1 s em que o raciocínio do usuário não é interrompido [[2]](#ref-2). A cena de 10.000 elementos, um arquivo de 5,2 MB, estabilizou em 1,52 s, abaixo da meta de 2 s do modelo RAIL [[3]](#ref-3). A pontuação média da métrica é **4,50 pontos (Nível Bom `+`)**.
- **[M3.2.2](../fase-02/gqm-flexibilidade.md#m322-taxa-de-quadros-durante-a-edição-por-tamanho-de-cena) (Taxa de quadros durante edição contínua):** Medida via Frame Rendering Stats do DevTools durante arrasto de blocos de elementos:
  - 100 elementos: **60 FPS** (100% da meta de 60 FPS do modelo RAIL [[3]](#ref-3), Nível `++`).
  - 1.000 elementos: **52 FPS** (86,7% da meta, Nível `+`), com oscilação entre 46 e 58 FPS.
  - 5.000 elementos: **20 FPS** (33,3% da meta, Nível `-`).
  - 10.000 elementos: **12 FPS** (20,0% da meta, Nível `-`).

  Até 1.000 elementos, a mediana fica em 52 FPS ou mais, acima do limiar de 48 FPS da hipótese, com oscilação entre 46 e 58 FPS nessa cena. Em cenas densas (acima de 5.000 elementos), o redesenho global do canvas HTML5 impõe gargalo de renderização, reduzindo a taxa de quadros e caracterizando um ponto de atenção técnica. Mesmo nessas cenas, não houve congelamento da aba, travamento do processo ou fechamento do navegador. Média: **3,25 pontos (Nível Regular `o`)**.
- **[M3.2.3](../fase-02/gqm-flexibilidade.md#m323-tamanho-máximo-de-cena-salva-e-exportada) (Tamanho máximo de cena salva e exportada):** Todas as 4 escalas foram submetidas ao teste de estresse de persistência (`.excalidraw`) e exportação (PNG e SVG). A cena máxima de **10.000 elementos** foi salva em **0,80 s**, exportada em PNG em **1,20 s** e em SVG em **0,70 s**, todas muito abaixo do limite crítico de 30 s e do limiar interativo de 2 s. Nível: **Excelente (`++`, 5,00 pontos)**.

#### Resposta formal à questão Q3.2

> **Resposta:** **Sim, para cenas típicas e moderadas, com degradação progressiva de fluidez em cenas extremas.** O Excalidraw escala com agilidade na abertura e persistência de arquivos, salvando e exportando cenas de até 10.000 elementos sem travamento do navegador. A integridade dos elementos salvos não foi verificada em [M3.2.3](../fase-02/gqm-flexibilidade.md#m323-tamanho-máximo-de-cena-salva-e-exportada). Contudo, a taxa de quadros durante o arrasto contínuo em cenas superiores a 5.000 elementos cai para a faixa de 12 a 20 FPS, indicando que a renderização bidimensional síncrona se beneficia de técnicas futuras de particionamento espacial (spatial indexing) ou virtualização de viewport.
> 
> **Pontuação de [Q3.2](../fase-02/gqm-flexibilidade.md#4-q32-escalabilidade):** Média de **4,3 pontos** (Nível **Bom `+`**).

---

### 3.3 Questão Q3.3: Instalabilidade

> **Pergunta do GQM:** *O software pode ser instalado e executado com sucesso e sem esforço excessivo no ambiente-alvo?*

#### Análise das métricas componentes

- **[M3.3.1](../fase-02/gqm-flexibilidade.md#m331-proporção-de-operações-de-pacote-bem-sucedidas) (Proporção de operações de pacote bem-sucedidas):** Avaliação de 9 operações cruzando 3 gerenciadores (`npm`, `yarn` e `pnpm`) nas etapas de instalação inicial, upgrade e desinstalação a partir do tarball local gerado no monorepo (`@excalidraw/excalidraw-0.18.0.tgz`). Na [tabela de resultados](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.1_resultados_pacote.csv), a coluna `Status_Tarball_Local` registra falha na instalação e na atualização e sucesso nas três remoções. No [log](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.1_log_operacoes_pacote.txt), o npm falha com `ETARGET`, porque o pacote depende de `@excalidraw/common@0.18.0`, subpacote interno não publicado no registro. Com 3 operações bem-sucedidas em 9 avaliadas (**33,3%**), a métrica atinge o nível **Ruim (`-`, 2,00 pontos)** e refuta a hipótese [H3.3.1](../fase-02/gqm-flexibilidade.md#5-q33-instalabilidade).

  A nota tem uma limitação. O log só registra as três operações do npm com o tarball local, e suas linhas dizem "Falha" ao lado de descrições de sucesso, como "Desinstalação limpa confirmada sem resíduos". O registro do Yarn para logo no início, quando o Corepack baixa o Yarn 4.14.1, e não o 1.22.22 previsto nas [instruções](../fase-03/instrucoes-g3-flexibilidade.md#41-m331-proporção-de-operações-de-pacote-bem-sucedidas). Não há log do pnpm nem das operações pelo registro público, que a coluna `Status_Registro_Oficial` marca como sucesso nas nove operações. A nota usa a coluna `Status_Tarball_Local` porque as instruções avaliam o pacote gerado no commit avaliado, instalado a partir do tarball local. Assim, as falhas de instalação e atualização no Yarn e no pnpm vêm só da tabela, sem log que as comprove.
- **[M3.3.2](../fase-02/gqm-flexibilidade.md#m332-proporção-de-passos-documentados-reproduzidos-sem-ajuste) (Proporção de passos documentados reproduzidos sem ajuste):** Dos 7 passos descritos na documentação oficial de compilação e execução local, **6 passos foram reproduzidos estritamente sem ajuste (85,7%)**, classificando a métrica no nível **Bom (`+`, 4,00 pontos)**. Na via nativa, `yarn` instalou as dependências e configurou os githooks do Husky com código 0 em 346 s, e `yarn start` inicializou o Vite em **1,09 s**, respondendo com HTTP 200. O único ajuste ocorreu no Passo 6: o guia `development.mdx` documenta `docker-compose up --build -d`, com a sintaxe de hífen legada. Com o Docker Compose v2, que é um plugin do Docker e não instala o binário `docker-compose`, o comando falhou com código de saída 127 (command not found) e precisou ser trocado por `docker compose up`. A falta do `docker-compose` v1 é um fator de variação de versão de ferramenta, caso previsto no [4º quadrante da abstraction sheet de G3](../fase-02/abstraction-sheets.md#4-g3-flexibilidade): a falha vem do ambiente de construção, e não do código do produto. O passo conta como ajuste mesmo assim, porque a [ficha de M3.3.2](../fase-02/gqm-flexibilidade.md#m332-proporção-de-passos-documentados-reproduzidos-sem-ajuste) só aceita como reproduzido o passo que funciona sem nenhuma ação não escrita no guia.
- **[M3.3.3](../fase-02/gqm-flexibilidade.md#m333-implantação-com-docker) (Implantação com Docker):** Todas as 4 etapas de verificação (construção da imagem multi-stage Nginx, inicialização do contêiner, aprovação do healthcheck interno com `wget -q -O - http://localhost:80/` e carregamento do editor no navegador) foram validadas com sucesso sem nenhuma intervenção manual. O servidor Nginx interno torna a execução independente das configurações do hospedeiro, o que atende ao requisito [RQ-FLEX-09](../fase-01/requisitos-avaliacao.md#4-requisitos-de-flexibilidade). Nível: **Excelente (`++`, 5,00 pontos)**.

#### Resposta formal à questão Q3.3

> **Resposta:** **Sim, com boa facilidade geral e ressalvas no consumo de pacotes locais.** O Excalidraw demonstra alta maturidade na conteinerização com Docker, permitindo disponibilizar uma instância de produção local sem intervenção manual. O ambiente nativo também compila com agilidade. Por outro lado, o empacotamento local do monorepo expõe acoplamento entre subpacotes internos, exigindo publicação sincronizada para evitar inconsistências em gerenciadores de dependências, além de apontar a necessidade de modernização das instruções de Docker Compose na documentação.
> 
> **Pontuação de [Q3.3](../fase-02/gqm-flexibilidade.md#5-q33-instalabilidade):** Média de **3,7 pontos** (Nível **Bom `+`**).

---

### 3.4 Questão Q3.4: Substituibilidade

> **Pergunta do GQM:** *O software pode ser substituído por outro equivalente ou interoperar através de formatos abertos?*

#### Análise das métricas componentes

- **[M3.4.1](../fase-02/gqm-flexibilidade.md#m341-formatos-de-exportação-abertos-disponíveis) (Formatos de exportação abertos disponíveis):** O Excalidraw disponibiliza nativamente **3 formatos abertos padronizados**: `.excalidraw` (JSON estruturado), `PNG` (raster aberto conforme W3C e ISO/IEC 15948) e `SVG` (vetorial escalável W3C), todos com suporte opcional à incorporação dos metadados da cena. A presença de 3 formatos confere o nível **Bom (`+`, 4,00 pontos)**.
- **[M3.4.2](../fase-02/gqm-flexibilidade.md#m342-proporção-de-elementos-preservados-na-exportação-e-reimportação) (Proporção de elementos preservados na reimportação):** A verificação automatizada via script `compara_elementos.py` sobre os 10 tipos de elementos gráficos da `cena_referencia.excalidraw` demonstrou **100,00% de preservação** em todos os formatos testados (.excalidraw, PNG embutido e SVG embutido). O mecanismo que embute os metadados da cena no PNG e no SVG preservou tipos, coordenadas (`x`, `y`, `width`, `height`), estilos (`strokeColor`, `backgroundColor`, `fillStyle`, `strokeWidth`) e textos sem desvio, conferindo nível **Excelente (`++`, 5,00 pontos)**.
- **[M3.4.3](../fase-02/gqm-flexibilidade.md#m343-proporção-dos-campos-do-formato-excalidraw-documentados) (Proporção dos campos do formato documentados):** A auditoria das 52 propriedades presentes na cena real contra a especificação técnica oficial (`dev-docs/docs/codebase/json-schema.mdx`) revelou que apenas **14 propriedades estão documentadas (26,9%)**, enquanto **38 propriedades não são documentadas**. Entre elas estão campos de controle interno, como `seed` e `versionNonce`, e campos de conteúdo, como `strokeColor`, `roundness`, `roughness`, `fontSize`, `opacity`, `boundElements`, `frameId`, `isDeleted`, `link`, `locked` e `updated`. O exemplo da documentação resume as propriedades dos elementos com o comentário `/* ...other element properties */`. A métrica obteve nível **Ruim (`-`, 2,00 pontos)** e revelou a ausência de um arquivo formal JSON Schema (`schema.json`) no repositório, o que fragiliza o requisito [RQ-FLEX-12](../fase-01/requisitos-avaliacao.md#4-requisitos-de-flexibilidade).

#### Resposta formal à questão Q3.4

> **Resposta:** **Parcialmente, caracterizando um contraste entre código e documentação.** Sob a ótica de uso e dados, a substituibilidade do Excalidraw é alta: o software salva e exporta em múltiplos formatos abertos e reimporta seus próprios arquivos sem perder um único elemento gráfico (100% de fidelidade). Por outro lado, para desenvolvedores terceiros que buscam implementar ferramentas interoperáveis ou conversores independentes, a ausência de um esquema formal legível por máquina e a omissão de mais de 73% das propriedades na documentação técnica obrigam quem integra a ler o código-fonte TypeScript para entender o formato.
> 
> **Pontuação de [Q3.4](../fase-02/gqm-flexibilidade.md#6-q34-substituibilidade):** Média de **3,7 pontos** (Nível **Bom `+`**).

---

## 4. Confronto formal de hipóteses

Antes da coleta empírica, foram formuladas doze hipóteses no [Plano GQM de Flexibilidade](../fase-02/gqm-flexibilidade.md). O confronto com os valores reais coletados resultou em **9 hipóteses confirmadas** e **3 hipóteses refutadas**:

<p className="tabela-titulo">Tabela 3: Confronto formal de hipóteses do objetivo G3</p>

| Hipótese | Enunciado da hipótese | Regra de confirmação | Valor medido | Veredito | Interpretação técnica |
| :---: | :--- | :--- | :---: | :---: | :--- |
| **[H3.1.1](../fase-02/gqm-flexibilidade.md#3-q31-adaptabilidade)** | Os navegadores declarados cobrirão a maior parte dos usuários. | ≥ 80% da população global | **88,94%** | **Confirmada** | Amplo suporte a motores modernos (Blink, Gecko, WebKit). |
| **[H3.1.2](../fase-02/gqm-flexibilidade.md#3-q31-adaptabilidade)** | A biblioteca funcionará com React 17, 18 e 19, em Vite e em Next.js. | = 6 de 6 ambientes | **5 de 6** (83,3%) | **Refutada** | Incompatibilidade do Next.js 12 com React 17 (`useId` e `useDeferredValue`). |
| **[H3.1.3](../fase-02/gqm-flexibilidade.md#3-q31-adaptabilidade)** | O editor aceitará toque nas ações de edição. | = 10 de 10 ações por toque | **10 de 10** (100%) | **Confirmada** | Interação móvel fluida por toque e caneta no iPad. |
| **[H3.2.1](../fase-02/gqm-flexibilidade.md#4-q32-escalabilidade)** | Um desenho de 1.000 elementos abrirá sem interromper o usuário. | ≤ 1,0 s na cena de 1.000 elem | **0,11 s** | **Confirmada** | Abertura bem abaixo do limite de 1 s de Nielsen [[2]](#ref-2). |
| **[H3.2.2](../fase-02/gqm-flexibilidade.md#4-q32-escalabilidade)** | A edição será fluida com 1.000 elementos. | ≥ 48 FPS na cena de 1.000 elem | **52 FPS** | **Confirmada** | Desempenho satisfatório em cenas de porte intermediário. |
| **[H3.2.3](../fase-02/gqm-flexibilidade.md#4-q32-escalabilidade)** | Desenhos com milhares de elementos poderão ser salvos e exportados. | Maior cena ≥ 5.000 elem | **10.000 elem** | **Confirmada** | Persistência e exportação operam com sucesso no teto de 10.000 elementos. |
| **[H3.3.1](../fase-02/gqm-flexibilidade.md#5-q33-instalabilidade)** | A biblioteca será instalada e removida sem erro pelos gerenciadores de pacotes. | = 9 de 9 operações | **3 de 9** (33,3%) | **Refutada** | Erro de resolução de dependência de workspace (`@excalidraw/common`) em tarball local. |
| **[H3.3.2](../fase-02/gqm-flexibilidade.md#5-q33-instalabilidade)** | As instruções de execução local bastarão, com as versões de ferramentas exigidas. | ≥ 95% dos passos sem ajuste | **85,7%** (6 de 7) | **Refutada** | Falha na invocação de ferramenta legada (`docker-compose` com código 127), fator de variação de versão de ferramenta previsto na abstraction sheet. |
| **[H3.3.3](../fase-02/gqm-flexibilidade.md#5-q33-instalabilidade)** | A imagem Docker será construída e executada sem passos manuais. | = 4 de 4 verificações | **4 de 4** (100%) | **Confirmada** | Conteinerização autônoma e healthcheck aprovado. |
| **[H3.4.1](../fase-02/gqm-flexibilidade.md#6-q34-substituibilidade)** | O desenho poderá ser exportado em formatos abertos. | ≥ 3 formatos abertos | **3 formatos** | **Confirmada** | Formatos padronizados e interoperáveis (.excalidraw, PNG, SVG). |
| **[H3.4.2](../fase-02/gqm-flexibilidade.md#6-q34-substituibilidade)** | A reimportação preservará os elementos do desenho. | ≥ 95% em cada formato | **100,00%** | **Confirmada** | Algoritmo de restauração de metadados sem perda de atributos. |
| **[H3.4.3](../fase-02/gqm-flexibilidade.md#6-q34-substituibilidade)** | O formato `.excalidraw` terá documentação apenas parcial. | Menor que 60% dos campos | **26,9%** | **Confirmada** | Confirmação empírica da defasagem documental do esquema de dados. |

<p className="tabela-fonte">Fonte: [Maria Eduarda](https://github.com/eduarda-ogomes), 2026.</p>

---

## 5. Pontuação e julgamento final da característica

### 5.1 Agregação por subcaracterísticas e objetivo G3

As pontuações seguem a [regra de agregação da Fase 02](../fase-02/pontuacao-julgamento.md#6-agregação-da-métrica-à-característica), baseada em Heitlager, Kuipers e Visser [[1, p. 8]](#ref-1).

<p className="tabela-titulo">Tabela 4: Pontuação das questões e do objetivo G3</p>

| Questão | Pontos das métricas | Média | Nível |
| :--- | :--- | :---: | :---: |
| [Q3.1](../fase-02/gqm-flexibilidade.md#3-q31-adaptabilidade): Adaptabilidade | 4,00, 4,00 e 5,00 | 4,3 | `+` |
| [Q3.2](../fase-02/gqm-flexibilidade.md#4-q32-escalabilidade): Escalabilidade | 4,50, 3,25 e 5,00 | 4,3 | `+` |
| [Q3.3](../fase-02/gqm-flexibilidade.md#5-q33-instalabilidade): Instalabilidade | 2,00, 4,00 e 5,00 | 3,7 | `+` |
| [Q3.4](../fase-02/gqm-flexibilidade.md#6-q34-substituibilidade): Substituibilidade | 4,00, 5,00 e 2,00 | 3,7 | `+` |
| **G3: Flexibilidade** | Média das quatro questões, sem arredondá-las antes | **4,0** | **`+`** |

<p className="tabela-fonte">Fonte: [Maria Eduarda](https://github.com/eduarda-ogomes), 2026.</p>

### 5.2 Julgamento

Pelos [critérios de julgamento da Fase 02](../fase-02/pontuacao-julgamento.md#71-julgamento-de-cada-característica), a Flexibilidade **atende**: a característica está no nível `+`, e nenhuma das quatro questões está no nível `--`.

---

## 6. Pontos de melhoria e de atenção

Pela [regra de pontos de melhoria da Fase 02](../fase-02/pontuacao-julgamento.md#73-pontos-de-melhoria), toda métrica no nível `-` ou `--` é registrada como ponto de melhoria. Os itens 1 e 2 são esses pontos. Os itens 3 a 5 estão no nível `o` ou acima e foram registrados como pontos de atenção:

1. **[M3.4.3](../fase-02/gqm-flexibilidade.md#m343-proporção-dos-campos-do-formato-excalidraw-documentados) ([Q3.4](../fase-02/gqm-flexibilidade.md#6-q34-substituibilidade) Substituibilidade, déficit de especificação técnica do formato):** Apenas 26,9% dos campos documentados, com pontuação 2,00 (Nível Ruim `-`).
2. **[M3.3.1](../fase-02/gqm-flexibilidade.md#m331-proporção-de-operações-de-pacote-bem-sucedidas) ([Q3.3](../fase-02/gqm-flexibilidade.md#5-q33-instalabilidade) Instalabilidade, inconsistência na instalação local de pacotes):** Falha na resolução do subpacote `@excalidraw/common` via tarball isolado, com a limitação de evidência descrita na [análise de Q3.3](#33-questão-q33-instalabilidade), atingindo 33,3% de sucesso e pontuação 2,00 (Nível Ruim `-`).
3. **[M3.1.2](../fase-02/gqm-flexibilidade.md#m312-proporção-de-ambientes-de-integração-com-sucesso) ([Q3.1](../fase-02/gqm-flexibilidade.md#3-q31-adaptabilidade) Adaptabilidade, falha de integração em Next.js com React 17):** O pacote compilado importa hooks ausentes no React 17, com pontuação 4,00 (Nível Bom `+`).
4. **[M3.2.2](../fase-02/gqm-flexibilidade.md#m322-taxa-de-quadros-durante-a-edição-por-tamanho-de-cena) ([Q3.2](../fase-02/gqm-flexibilidade.md#4-q32-escalabilidade) Escalabilidade, queda da taxa de quadros em cenas densas):** Desempenho cai para 20 FPS (5.000 elementos) e 12 FPS (10.000 elementos), atingindo pontuação 3,25 (Nível Regular `o`).
5. **[M3.3.2](../fase-02/gqm-flexibilidade.md#m332-proporção-de-passos-documentados-reproduzidos-sem-ajuste) ([Q3.3](../fase-02/gqm-flexibilidade.md#5-q33-instalabilidade) Instalabilidade, instruções com utilitários legados):** Menção ao comando `docker-compose` em vez do comando `docker compose`.

As ações propostas para esses pontos, com a priorização entre G1 e G3, estão nas [oportunidades de melhoria](./melhorias.md).

---

## 7. Registro de rastreabilidade com os dados brutos

Todos os arquivos que sustentam este relatório estão disponíveis no repositório:

<p className="tabela-titulo">Tabela 5: Rastreabilidade entre métricas e dados brutos auditáveis</p>

| Métrica | Arquivo de evidência | Caminho relativo |
| :---: | :--- | :--- |
| **[M3.1.1](../fase-02/gqm-flexibilidade.md#m311-cobertura-de-usuários-pelos-navegadores-declarados)** | Terminal output do Browserslist | [`dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.1_cobertura_browserslist.txt`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.1_cobertura_browserslist.txt) |
| **[M3.1.2](../fase-02/gqm-flexibilidade.md#m312-proporção-de-ambientes-de-integração-com-sucesso)** | Matriz de testes dos 6 ambientes | [`dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.2_matriz_integracao.csv`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.2_matriz_integracao.csv) |
| **[M3.1.2](../fase-02/gqm-flexibilidade.md#m312-proporção-de-ambientes-de-integração-com-sucesso)** | Mosaico de capturas de tela do canvas | [`dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.2_evidencia_ambiente.png`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.2_evidencia_ambiente.png) |
| **[M3.1.2](../fase-02/gqm-flexibilidade.md#m312-proporção-de-ambientes-de-integração-com-sucesso)** | Arquivo compactado com logs de build | [`dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.2_build_logs.zip`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.2_build_logs.zip) |
| **[M3.1.3](../fase-02/gqm-flexibilidade.md#m313-proporção-de-ações-de-edição-que-funcionam-por-toque-e-caneta)** | Formulário de auditoria iPad e caneta | [`dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.3_formulario_toque_caneta.csv`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.3_formulario_toque_caneta.csv) |
| **[M3.1.3](../fase-02/gqm-flexibilidade.md#m313-proporção-de-ações-de-edição-que-funcionam-por-toque-e-caneta)** | Gravação de tela por toque no iPad | [`dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.3_gravacao_toque.mp4`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.3_gravacao_toque.mp4) |
| **[M3.1.3](../fase-02/gqm-flexibilidade.md#m313-proporção-de-ações-de-edição-que-funcionam-por-toque-e-caneta)** | Gravação de tela com stylus no iPad | [`dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.3_gravacao_caneta.mp4`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.3_gravacao_caneta.mp4) |
| **[M3.2.1](../fase-02/gqm-flexibilidade.md#m321-tempo-de-abertura-por-tamanho-de-cena)** | Tabela com 20 medições DevTools | [`dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.1_tempos_abertura.csv`](../../dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.1_tempos_abertura.csv) |
| **[M3.2.1](../fase-02/gqm-flexibilidade.md#m321-tempo-de-abertura-por-tamanho-de-cena)** | Pasta com 20 traces JSON | `dados/fase-04/brutos/Q3.2-escalabilidade/traces_abertura/` |
| **[M3.2.2](../fase-02/gqm-flexibilidade.md#m322-taxa-de-quadros-durante-a-edição-por-tamanho-de-cena)** | Tabela de FPS em edição contínua | [`dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.2_fps_edicao.csv`](../../dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.2_fps_edicao.csv) |
| **[M3.2.3](../fase-02/gqm-flexibilidade.md#m323-tamanho-máximo-de-cena-salva-e-exportada)** | Tabela de conferência de estresse | [`dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.3_tamanho_maximo_salvamento.csv`](../../dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.3_tamanho_maximo_salvamento.csv) |
| **[M3.3.1](../fase-02/gqm-flexibilidade.md#m331-proporção-de-operações-de-pacote-bem-sucedidas)** | Tabela das 9 operações de pacote | [`dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.1_resultados_pacote.csv`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.1_resultados_pacote.csv) |
| **[M3.3.1](../fase-02/gqm-flexibilidade.md#m331-proporção-de-operações-de-pacote-bem-sucedidas)** | Log de operações npm, yarn e pnpm | [`dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.1_log_operacoes_pacote.txt`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.1_log_operacoes_pacote.txt) |
| **[M3.3.2](../fase-02/gqm-flexibilidade.md#m332-proporção-de-passos-documentados-reproduzidos-sem-ajuste)** | Tabela de auditoria dos passos | [`dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.2_passos_ajustes.csv`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.2_passos_ajustes.csv) |
| **[M3.3.2](../fase-02/gqm-flexibilidade.md#m332-proporção-de-passos-documentados-reproduzidos-sem-ajuste)** | Log detalhado da execução de passos | [`dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.2_log_reproducao_passos.txt`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.2_log_reproducao_passos.txt) |
| **[M3.3.3](../fase-02/gqm-flexibilidade.md#m333-implantação-com-docker)** | Tabela das 4 verificações Docker | [`dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.3_verificacoes_docker.csv`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.3_verificacoes_docker.csv) |
| **[M3.4.1](../fase-02/gqm-flexibilidade.md#m341-formatos-de-exportação-abertos-disponíveis)** | Catálogo dos formatos abertos | [`dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.1_catalogo_formatos.csv`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.1_catalogo_formatos.csv) |
| **[M3.4.2](../fase-02/gqm-flexibilidade.md#m342-proporção-de-elementos-preservados-na-exportação-e-reimportação)** | Relatório de preservação de elementos | [`dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.2_preservacao_formatos.csv`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.2_preservacao_formatos.csv) |
| **[M3.4.2](../fase-02/gqm-flexibilidade.md#m342-proporção-de-elementos-preservados-na-exportação-e-reimportação)** | Cenas exportadas e reimportadas | [`dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.2_arquivos_reimportados.zip`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.2_arquivos_reimportados.zip) |
| **[M3.4.3](../fase-02/gqm-flexibilidade.md#m343-proporção-dos-campos-do-formato-excalidraw-documentados)** | Auditoria dos 52 campos do esquema | [`dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.3_conferencia_campos.csv`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.3_conferencia_campos.csv) |
| **[M3.4.3](../fase-02/gqm-flexibilidade.md#m343-proporção-dos-campos-do-formato-excalidraw-documentados)** | Relatório técnico de campos omitidos | [`dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.3_relatorio.txt`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.3_relatorio.txt) |

<p className="tabela-fonte">Fonte: [Maria Eduarda](https://github.com/eduarda-ogomes), 2026.</p>

---

## 8. Referências

> <Link id="ref-1">1.</Link> HEITLAGER, Ilja, KUIPERS, Tobias e VISSER, Joost. A practical model for measuring maintainability. In: **6th International Conference on the Quality of Information and Communications Technology (QUATIC 2007)**. IEEE, 2007. p. 30-39. Página 8 da versão dos autores. Disponível em: [https://www.di.uminho.pt/~joost/publications/HeitlagerKuipersVisser-Quatic2007.pdf](https://www.di.uminho.pt/~joost/publications/HeitlagerKuipersVisser-Quatic2007.pdf). Acesso em: 11 nov. 2026.

> <Link id="ref-2">2.</Link> NIELSEN, J. *Usability Engineering*. Academic Press, 1993. Capítulo 5. Trecho disponível em: [https://www.nngroup.com/articles/response-times-3-important-limits/](https://www.nngroup.com/articles/response-times-3-important-limits/). Acesso em: 06 nov. 2026.

> <Link id="ref-3">3.</Link> GOOGLE. Measure performance with the RAIL model. *web.dev*, atualizado em 10/06/2020. Seções "Load" e "Animation". Disponível em: [https://web.dev/articles/rail](https://web.dev/articles/rail). Acesso em: 06 nov. 2026.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| `1.0` | 11/11/2026 | Elaboração do relatório consolidado de resultados e julgamento do objetivo G3 (Flexibilidade). | [Maria Eduarda](https://github.com/eduarda-ogomes) | |
| `1.1` | 11/11/2026 | Correção do ambiente registrado, do texto de M3.3.1 e da apresentação da agregação e do julgamento, conforme a revisão da PR. | [Christopher Paraizo](https://github.com/wChrstphr) | |
| `1.2` | 15/11/2026 | Fusão com a página Insights e Descobertas de G3, com os detalhes técnicos levados à análise de cada questão, e troca da seleção da ação por um link para as oportunidades de melhoria. | [Christopher Paraizo](https://github.com/wChrstphr) | |
| `1.3` | 17/11/2026 | Correção da resposta de Q3.1, que tratava o isolamento no cliente como alternativa às falhas de hooks e de runtime JSX, conforme a revisão do PR. | [Christopher Paraizo](https://github.com/wChrstphr) | |
| `1.4` | 18/11/2026 | Revisão de coerência e cross-links: M3.1.2 recalculada com a Comb5 como sucesso e afirmações de desempenho ajustadas aos dados | [Christopher Paraizo](https://github.com/wChrstphr) | |
