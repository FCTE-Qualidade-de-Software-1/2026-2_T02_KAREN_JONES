---
sidebar_position: 2
title: "Resultados e Julgamento: Flexibilidade (G3)"
description: Relatório formal de avaliação e julgamento do objetivo G3 (Flexibilidade) do Excalidraw, consolidando a obtenção das medidas, respostas às questões GQM, confronto de hipóteses e ação de melhoria.
---

import Link from '@docusaurus/Link';

# Resultados e Julgamento: Flexibilidade (G3)

## Introdução

Este documento apresenta o relatório formal de avaliação da qualidade para o objetivo G3 (Flexibilidade), executado sobre o software Excalidraw fixado no commit `e1b7aacb356a492aa1e0fc6eb57b8896124027f0`. O propósito deste artefato é sintetizar os resultados empíricos obtidos na coleta de dados, responder fundamentadamente às questões formuladas pelo modelo GQM, confrontar as hipóteses estabelecidas e emitir o julgamento formal da característica com base nas normas de engenharia de software e nos critérios da disciplina.

## Metodologia

A avaliação seguiu o método Goal-Question-Metric (GQM) estruturado na Fase 02, em consonância com o modelo de qualidade de software ISO/IEC 25010:2011 e a sistemática de agregação de Heitlager, Kuipers e Visser [[1, p. 8]](#ref-1). A coleta empírica envolveu doze métricas distribuídas em quatro subcaracterísticas: Adaptabilidade, Escalabilidade, Instalabilidade e Substituibilidade. Os dados brutos foram obtidos por meio de testes automatizados, perfis de desempenho via Chrome DevTools, execução conteinerizada em Docker e testes manuais de ergonomia em dispositivo móvel. Com base nas fraquezas mapeadas durante o processo, foi delineada uma intervenção de engenharia de software para tratamento de não conformidades.

---

## 1. Identificação e Contexto da Avaliação

<p className="tabela-titulo">Tabela 1: Parâmetros do ambiente e contexto da execução</p>

| Parâmetro | Detalhes do Ambiente e Execução |
| :--- | :--- |
| **Objetivo Avaliado** | G3: Flexibilidade (Adaptabilidade, Escalabilidade, Instalabilidade, Substituibilidade) |
| **Avaliadora Responsável** | Maria Eduarda ([@eduarda-ogomes](https://github.com/eduarda-ogomes)) |
| **Software Avaliado** | Excalidraw (commit exato `e1b7aacb356a492aa1e0fc6eb57b8896124027f0`) |
| **Período de Execução** | 10 a 11 de Novembro de 2026 |
| **Sistema Operacional** | Zorin OS 18.1 (Kernel Linux 6.8.0-48-generic x86_64, base Ubuntu 24.04 LTS) |
| **Hardware do Avaliador** | AMD Ryzen 7 5700U with Radeon Graphics (16 threads), 16 GB RAM DDR4 |
| **Dispositivo Móvel** | Apple iPad (A16) e Caneta Stylus Capacitiva Goojodoq |
| **Ambiente de Testes** | Contêiner Docker oficial (Nginx 1.30.2, porta `3000:80`) e Node.js v20.19.0 com Yarn 1.22.22 |
| **Repositório de Dados Brutos** | `dados/fase-04/brutos/` |
| **Tabelas Consolidadas** | `dados/fase-04/consolidados/` |

<p className="tabela-fonte">Fonte: Elaborado pela autora, 2026.</p>

---

## 2. Painel Consolidado das Medições

A tabela abaixo sintetiza os valores empíricos medidos para as doze métricas do objetivo G3, convertidos para os níveis da [Fase 02 (Pontuação e julgamento)](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3), baseados no modelo de Heitlager, Kuipers e Visser [[1, p. 8]](#ref-1) na escala de 1 a 5 pontos:

<p className="tabela-titulo">Tabela 2: Painel consolidado das medições de flexibilidade (G3)</p>

| Métrica | Nome da Métrica | Questão | Valor Medido | Nível na Régua | Escala (1 a 5) | Hipótese | Status | Dado Bruto Auditável |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **M3.1.1** | Cobertura de usuários por navegadores declarados | Q3.1 | **88,94%** | **Bom** (`+`) | 4,00 | H3.1.1 ≥ 80% | **Confirmada** | [`M3.1.1_cobertura_browserslist.txt`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.1_cobertura_browserslist.txt) |
| **M3.1.2** | Proporção de ambientes de integração com sucesso | Q3.1 | **66,7%** (4 de 6) | **Regular** (`o`) | 3,00 | H3.1.2 = 6 de 6 | **Refutada** | [`M3.1.2_matriz_integracao.csv`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.2_matriz_integracao.csv) |
| **M3.1.3** | Proporção de ações de edição por toque e caneta | Q3.1 | **100,0%** (10 de 10) | **Excelente** (`++`) | 5,00 | H3.1.3 = 10 de 10 | **Confirmada** | [`M3.1.3_formulario_toque_caneta.csv`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.3_formulario_toque_caneta.csv) |
| **M3.2.1** | Tempo de abertura por tamanho de cena (1.000 elem) | Q3.2 | **0,11 s** | **Bom** (`+`) | 4,50 | H3.2.1 ≤ 1,0 s | **Confirmada** | [`M3.2.1_tempos_abertura.csv`](../../dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.1_tempos_abertura.csv) |
| **M3.2.2** | Taxa de quadros durante edição contínua (1.000 elem) | Q3.2 | **52 FPS** | **Regular** (`o`) | 3,25 | H3.2.2 ≥ 48 FPS | **Confirmada** | [`M3.2.2_fps_edicao.csv`](../../dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.2_fps_edicao.csv) |
| **M3.2.3** | Tamanho máximo de cena salva e exportada | Q3.2 | **10.000 elem** | **Excelente** (`++`) | 5,00 | H3.2.3 ≥ 5.000 elem | **Confirmada** | [`M3.2.3_tamanho_maximo_salvamento.csv`](../../dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.3_tamanho_maximo_salvamento.csv) |
| **M3.3.1** | Proporção de operações de pacote bem-sucedidas | Q3.3 | **33,3%** (3 de 9) | **Ruim** (`-`) | 2,00 | H3.3.1 = 9 de 9 | **Refutada** | [`M3.3.1_resultados_pacote.csv`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.1_resultados_pacote.csv) |
| **M3.3.2** | Proporção de passos documentados reproduzidos | Q3.3 | **85,7%** (6 de 7) | **Bom** (`+`) | 4,00 | H3.3.2 ≥ 95% | **Refutada** | [`M3.3.2_passos_ajustes.csv`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.2_passos_ajustes.csv) |
| **M3.3.3** | Implantação com Docker | Q3.3 | **100,0%** (4 de 4) | **Excelente** (`++`) | 5,00 | H3.3.3 = 4 de 4 | **Confirmada** | [`M3.3.3_verificacoes_docker.csv`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.3_verificacoes_docker.csv) |
| **M3.4.1** | Formatos de exportação abertos disponíveis | Q3.4 | **3 formatos** | **Bom** (`+`) | 4,00 | H3.4.1 ≥ 3 | **Confirmada** | [`M3.4.1_catalogo_formatos.csv`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.1_catalogo_formatos.csv) |
| **M3.4.2** | Preservação de elementos na reimportação | Q3.4 | **100,00%** | **Excelente** (`++`) | 5,00 | H3.4.2 ≥ 95% | **Confirmada** | [`M3.4.2_preservacao_formatos.csv`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.2_preservacao_formatos.csv) |
| **M3.4.3** | Proporção dos campos do formato documentados | Q3.4 | **26,9%** (14 de 52) | **Ruim** (`-`) | 2,00 | H3.4.3 < 60% | **Confirmada** | [`M3.4.3_conferencia_campos.csv`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.3_conferencia_campos.csv) |

<p className="tabela-fonte">Fonte: Elaborado pela autora, 2026.</p>

---

## 3. Análise dos Resultados e Respostas às Questões GQM

### 3.1 Questão Q3.1: Adaptabilidade

> **Pergunta GQM:** *O software adapta-se satisfatoriamente a diferentes navegadores, frameworks e modos de entrada?*

#### Análise das Métricas Componentes

- **M3.1.1 (Cobertura por navegadores declarados):** A execução oficial do comando `browserslist --coverage` na raiz do repositório apontou cobertura de **88,94%** da população global de usuários web. O software suporta navegadores modernos em versões recentes (Chrome, Edge, Firefox, Safari, iOS Safari, Chrome for Android). O percentual situa-se confortavelmente na faixa **Bom (`+`)** (80% a 95%).
- **M3.1.2 (Proporção de ambientes de integração com sucesso):** A matriz de seis combinações empíricas (React 17, 18 e 19 combinados com Vite e Next.js) alcançou sucesso em **4 das 6 combinações (66,7%)**, resultando em nível **Regular (`o`)**:
  - No empacotador Vite, todas as três versões do React (17, 18 e 19) compilaram e renderizaram o canvas perfeitamente (cerca de 12 segundos de build), permitindo criar e interagir com elementos gráficos.
  - No Next.js, apenas a versão React 19 compilou e executou com sucesso, mediante dynamic client-only import.
  - O React 17 falhou no Next.js devido ao empacotamento com Webpack, pois o pacote `@excalidraw/excalidraw` no commit `e1b7aac` utiliza internamente hooks `useId` e `useDeferredValue` importados diretamente de `react`, que inexistem no React 17.
  - O React 18 falhou no Next.js durante o pré-render SSR (`react-dom-server`), pois o pacote foi gerado contra o runtime JSX do React 19, gerando símbolos de elementos desconhecidos no motor do React 18 (`Minified React error #31`).
- **M3.1.3 (Ações de edição por toque e caneta):** A avaliação manual no Apple iPad (A16) registrou **100% de sucesso (10 de 10 ações)** tanto por toque direto com o dedo quanto com a caneta stylus Goojodoq. A aplicação detecta toques com fidelidade, diferencia desenho livre com a caneta e suporta gestos multitoque de pinça (zoom) e deslocamento com dois dedos (pan) de modo ergonômico.

#### Resposta Formal à Questão Q3.1

> **Resposta:** **Sim, de forma satisfatória e com ressalvas conhecidas.** O Excalidraw apresenta excelente suporte a dispositivos táteis e móveis (100% no iPad) e ampla cobertura da base global de navegadores (88,94%). Todavia, a adaptabilidade como componente React em aplicações com renderização híbrida ou SSR (Next.js) requer atenção. Integradores que utilizem React 17 ou React 18 enfrentam incompatibilidades em tempo de compilação ou pré-renderização, demandando a adoção do React 19 ou isolamento completo da biblioteca no lado do cliente (client-only).
> 
> **Pontuação de Q3.1:** Média de **4,00 pontos** (Nível **Bom `+`**).

---

### 3.2 Questão Q3.2: Escalabilidade

> **Pergunta GQM:** *O software mantém desempenho aceitável com aumento no volume de dados da cena?*

#### Análise das Métricas Componentes

- **M3.2.1 (Tempo de abertura por tamanho de cena):** Avaliado por 20 perfis de desempenho DevTools em 4 escalas (100, 1.000, 5.000 e 10.000 elementos, com 5 repetições cada). As medianas registradas foram:
  - 100 elementos: **0,05 s** (Nível `++`)
  - 1.000 elementos: **0,11 s** (Nível `++`)
  - 5.000 elementos: **1,15 s** (Nível `+`)
  - 10.000 elementos: **1,52 s** (Nível `+`)
  O tempo cresce de forma aproximadamente linear com o volume de dados. A cena de 1.000 elementos abriu em apenas 0,11 s, amplamente inferior ao limite cognitivo de Nielsen (1,0 s). A pontuação média da métrica é **4,50 pontos (Nível Bom `+`)**.
- **M3.2.2 (Taxa de quadros durante edição contínua):** Medida via Frame Rendering Stats do DevTools durante arrasto de blocos de elementos:
  - 100 elementos: **60 FPS** (100% da meta de 60 FPS, Nível `++`)
  - 1.000 elementos: **52 FPS** (86,7% da meta, Nível `+`)
  - 5.000 elementos: **20 FPS** (33,3% da meta, Nível `-`)
  - 10.000 elementos: **12 FPS** (20,0% da meta, Nível `-`)
  Em cenas pequenas e médias (até 1.000 elementos), a edição é perfeitamente fluida. Em cenas densas (acima de 5.000 elementos), o redesenho global do canvas HTML5 impõe gargalo de renderização, reduzindo a taxa de quadros e caracterizando um ponto de atenção técnica. Média: **3,25 pontos (Nível Regular `o`)**.
- **M3.2.3 (Tamanho máximo de cena salva e exportada):** Todas as 4 escalas foram submetidas ao teste de estresse de persistência (`.excalidraw`) e exportação (PNG e SVG). A cena máxima de **10.000 elementos** foi salva em **0,80 s**, exportada em PNG em **1,20 s** e em SVG em **0,70 s**, todas muito abaixo do limite crítico de 30 s e do limiar interativo de 2 s. Nível: **Excelente (`++`, 5,00 pontos)**.

#### Resposta Formal à Questão Q3.2

> **Resposta:** **Sim, para cenas típicas e moderadas, com degradação progressiva de fluidez em cenas extremas.** O Excalidraw escala com agilidade na abertura e persistência de arquivos, suportando volumes maciços de até 10.000 elementos sem perda de dados ou travamento do navegador. Contudo, a taxa de quadros durante o arrasto contínuo em cenas superiores a 5.000 elementos cai para a faixa de 12 a 20 FPS, indicando que a renderização bidimensional síncrona se beneficia de técnicas futuras de particionamento espacial (spatial indexing) ou virtualização de viewport.
> 
> **Pontuação de Q3.2:** Média de **4,25 pontos** (Nível **Bom `+`**).

---

### 3.3 Questão Q3.3: Instalabilidade

> **Pergunta GQM:** *O software pode ser instalado e executado com sucesso e sem esforço excessivo no ambiente-alvo?*

#### Análise das Métricas Componentes

- **M3.3.1 (Proporção de operações de pacote bem-sucedidas):** Avaliação de 9 operações cruzando 3 gerenciadores (`npm`, `yarn` e `pnpm`) nas etapas de instalação inicial, upgrade e desinstalação a partir do tarball local gerado no monorepo (`@excalidraw/excalidraw-0.18.0.tgz`). A instalação inicial obteve êxito nos três gerenciadores (3 de 3). No entanto, as operações de upgrade falharam devido à dependência interna não publicada `@excalidraw/common` com código `ETARGET`, inviabilizando também a conclusão limpa da desinstalação subsequente. Com 3 operações bem-sucedidas em 9 avaliadas (**33,3%**), a métrica atinge o nível **Ruim (`-`, 2,00 pontos)** e refuta a hipótese H3.3.1.
- **M3.3.2 (Proporção de passos documentados reproduzidos sem ajuste):** Dos 7 passos descritos na documentação oficial de compilação e execução local, **6 passos foram reproduzidos estritamente sem ajuste (85,7%)**, classificando a métrica no nível **Bom (`+`, 4,00 pontos)**. O único ajuste necessário ocorreu no Passo 6 (`docker-compose up`), que falhou com código de saída 127 (command not found) em sistemas operacionais recentes devido à sintaxe de hífen legada (`docker-compose` em vez de `docker compose`).
- **M3.3.3 (Implantação com Docker):** Todas as 4 etapas de verificação (construção da imagem multi-stage Nginx, inicialização do contêiner, aprovação do healthcheck interno com `wget -q -O - http://localhost:80/` e carregamento do editor no navegador) foram validadas com sucesso sem nenhuma intervenção manual. Nível: **Excelente (`++`, 5,00 pontos)**.

#### Resposta Formal à Questão Q3.3

> **Resposta:** **Sim, com boa facilidade geral e ressalvas no consumo de pacotes locais.** O Excalidraw demonstra alta maturidade na conteinerização com Docker, permitindo disponibilizar uma instância de produção local em menos de três minutos de forma totalmente automatizada. O ambiente nativo também compila com agilidade. Por outro lado, o empacotamento local do monorepo expõe acoplamento entre subpacotes internos, exigindo publicação sincronizada para evitar inconsistências em gerenciadores de dependências, além de apontar a necessidade de modernização das instruções de Docker Compose na documentação.
> 
> **Pontuação de Q3.3:** Média de **3,67 pontos** (Nível **Bom `+`**).

---

### 3.4 Questão Q3.4: Substituibilidade

> **Pergunta GQM:** *O software pode ser substituído por outro equivalente ou interoperar através de formatos abertos?*

#### Análise das Métricas Componentes

- **M3.4.1 (Formatos de exportação abertos disponíveis):** O Excalidraw disponibiliza nativamente **3 formatos abertos padronizados**: `.excalidraw` (JSON estruturado), `PNG` (raster aberto conforme W3C e ISO/IEC 15948) e `SVG` (vetorial escalável W3C), todos com suporte opcional à incorporação dos metadados da cena. A presença de 3 formatos confere o nível **Bom (`+`, 4,00 pontos)**.
- **M3.4.2 (Proporção de elementos preservados na reimportação):** A verificação automatizada via script `compara_elementos.py` sobre os 10 tipos de elementos gráficos da `cena_referencia.excalidraw` demonstrou **100,00% de preservação** em todos os formatos testados (.excalidraw, PNG embutido e SVG embutido). Não houve qualquer perda de atributos geométricos, cores, texto ou estilos, conferindo nível **Excelente (`++`, 5,00 pontos)**.
- **M3.4.3 (Proporção dos campos do formato documentados):** A auditoria das 52 propriedades presentes na cena real contra a especificação técnica oficial (`dev-docs/docs/codebase/json-schema.mdx`) revelou que apenas **14 propriedades estão documentadas (26,9%)**, enquanto **38 propriedades essenciais são omitidas**, tais como `roundness`, `roughness`, `boundElements`, `frameId`, `link`, `locked` e `updated`. A métrica obteve nível **Ruim (`-`, 2,00 pontos)** e revelou a ausência de um arquivo formal JSON Schema (`schema.json`) no repositório.

#### Resposta Formal à Questão Q3.4

> **Resposta:** **Parcialmente, caracterizando um contraste entre código e documentação.** Sob a ótica de uso e dados, a substituibilidade do Excalidraw é exemplar: o software salva e exporta em múltiplos formatos abertos e reimporta seus próprios arquivos sem perder um único elemento gráfico (100% de fidelidade). Por outro lado, para desenvolvedores terceiros que buscam implementar ferramentas interoperáveis ou conversores independentes, a ausência de um esquema formal legível por máquina e a omissão de mais de 73% das propriedades na documentação técnica criam um obstáculo severo, exigindo engenharia reversa no código-fonte TypeScript.
> 
> **Pontuação de Q3.4:** Média de **3,67 pontos** (Nível **Bom `+`**).

---

## 4. Confronto Formal de Hipóteses

Antes da coleta empírica, foram formuladas doze hipóteses no [Plano GQM de Flexibilidade](../fase-02/gqm-flexibilidade.md). O confronto com os valores reais coletados resultou em **9 hipóteses confirmadas** e **3 hipóteses refutadas**:

<p className="tabela-titulo">Tabela 3: Confronto formal de hipóteses do objetivo G3</p>

| Hipótese | Enunciado da Hipótese | Regra de Confirmação | Valor Real Medido | Veredito | Interpretação Técnica |
| :---: | :--- | :--- | :---: | :---: | :--- |
| **H3.1.1** | O Excalidraw cobrirá a grande maioria dos navegadores em uso. | ≥ 80% da população global | **88,94%** | **Confirmada** | Amplo suporte a motores modernos (Blink, Gecko, WebKit). |
| **H3.1.2** | A biblioteca integrará sem erro com as principais versões do React. | = 6 de 6 ambientes | **4 de 6** (66,7%) | **Refutada** | Incompatibilidade de Webpack e Next.js com React 17 (`useId`) e SSR com React 18. |
| **H3.1.3** | Todas as ações principais de edição funcionarão por toque. | = 10 de 10 ações por toque | **10 de 10** (100%) | **Confirmada** | Interação móvel fluida por toque e caneta no iPad. |
| **H3.2.1** | Um desenho de 1.000 elementos abrirá sem interromper o usuário. | ≤ 1,0 s na cena de 1.000 elem | **0,11 s** | **Confirmada** | Abertura instantânea, amplamente inferior ao limiar de Nielsen. |
| **H3.2.2** | A edição será fluida com 1.000 elementos. | ≥ 48 FPS na cena de 1.000 elem | **52 FPS** | **Confirmada** | Desempenho satisfatório em cenas de porte intermediário. |
| **H3.2.3** | Desenhos com milhares de elementos poderão ser salvos e exportados. | Maior cena ≥ 5.000 elem | **10.000 elem** | **Confirmada** | Persistência e exportação operam com sucesso no teto de 10.000 elementos. |
| **H3.3.1** | As operações de pacote funcionarão nos três gerenciadores. | = 9 de 9 operações | **3 de 9** (33,3%) | **Refutada** | Erro de resolução de dependência de workspace (`@excalidraw/common`) em tarball local. |
| **H3.3.2** | As instruções de execução local bastarão sem ajustes. | ≥ 95% dos passos sem ajuste | **85,7%** (6 de 7) | **Refutada** | Falha na invocação de ferramenta legada (`docker-compose` com código 127). |
| **H3.3.3** | A imagem Docker será construída e executada sem passos manuais. | = 4 de 4 verificações | **4 de 4** (100%) | **Confirmada** | Conteinerização autônoma e healthcheck aprovado. |
| **H3.4.1** | O desenho poderá ser exportado em formatos abertos. | ≥ 3 formatos abertos | **3 formatos** | **Confirmada** | Formatos padronizados e interoperáveis (.excalidraw, PNG, SVG). |
| **H3.4.2** | A reimportação preservará os elementos do desenho. | ≥ 95% em cada formato | **100,00%** | **Confirmada** | Algoritmo de restauração de metadados sem perda de atributos. |
| **H3.4.3** | O formato `.excalidraw` terá documentação apenas parcial. | Menor que 60% dos campos | **26,9%** | **Confirmada** | Confirmação empírica da defasagem documental do esquema de dados. |

<p className="tabela-fonte">Fonte: Elaborado pela autora, 2026.</p>

---

## 5. Pontuação e Julgamento Final da Característica

### 5.1 Agregação por Subcaracterísticas e Objetivo G3

Conforme a metodologia de agregação de Heitlager, Kuipers e Visser [[1, p. 8]](#ref-1), as pontuações são combinadas por média aritmética simples na escala de 1 a 5 pontos:

1. **Pontuação das Subcaracterísticas (Questões GQM):**
   - **Q3.1: Adaptabilidade:** (4,00 + 3,00 + 5,00) / 3 = **4,00 pontos** (Nível **Bom `+`**)
   - **Q3.2: Escalabilidade:** (4,50 + 3,25 + 5,00) / 3 = **4,25 pontos** (Nível **Bom `+`**)
   - **Q3.3: Instalabilidade:** (2,00 + 4,00 + 5,00) / 3 = **3,67 pontos** (Nível **Bom `+`**)
   - **Q3.4: Substituibilidade:** (4,00 + 5,00 + 2,00) / 3 = **3,67 pontos** (Nível **Bom `+`**)

2. **Pontuação Global da Característica (Objetivo G3):**
   - **Média Global na Escala Heitlager (1 a 5):** (4,00 + 4,25 + 3,67 + 3,67) / 4 = **3,90 estrelas** (arredondado para 4 estrelas, Nível **Bom `+`**)

### 5.2 Julgamento Conforme Regras da Disciplina

Conforme os critérios estabelecidos na [seção 7.1 da Fase 02](../fase-02/pontuacao-julgamento.md#71-julgamento-de-cada-característica) (baseados no esquema TÜViT e Baggen et al., 2010):
- **Critério para resultado "Atende":** A característica global deve obter nível `o` ou superior (média igual ou maior que 3,0), e nenhuma das suas questões pode situar-se no nível `--` (Muito ruim, inferior a 2,0).
- **Resultado da Avaliação:**
  - A pontuação global da Flexibilidade é **3,90 pontos** (Nível **Bom `+`**).
  - Todas as 4 subcaracterísticas situam-se no nível Bom (`+`), com notas entre 3,67 e 4,25 pontos. Nenhuma subcaracterística obteve conceito Crítico ou Muito Ruim (`--`).
  - **Veredito Oficial:** O software Excalidraw **ATENDE** aos requisitos de qualidade para a característica **Flexibilidade**.

---

## 6. Diagnóstico de Fraquezas e Proposta de Ação de Melhoria

A sistemática de avaliação de qualidade determina que todo indicador no nível `-` ou `--` deve ser explicitamente sinalizado como oportunidade de melhoria técnica. Durante a avaliação de G3, foram mapeados os seguintes pontos de atenção:

1. **M3.4.3 (Déficit de Especificação Técnica do Formato):** Apenas 26,9% dos campos documentados, com pontuação 2,00 (Nível Ruim `-`).
2. **M3.3.1 (Inconsistência em Instalação Local de Pacotes):** Falha na resolução do subpacote `@excalidraw/common` via tarball isolado, atingindo 33,3% de sucesso e pontuação 2,00 (Nível Ruim `-`).
3. **M3.1.2 (Falhas de Integração em Next.js com React 17 e 18):** Incompatibilidade de hooks e símbolos SSR no pacote compilado, atingindo pontuação 3,00 (Nível Regular `o`).
4. **M3.2.2 (Queda de Taxa de Quadros em Cenas Densas):** Desempenho cai para 20 FPS (5.000 elementos) e 12 FPS (10.000 elementos), atingindo pontuação 3,25 (Nível Regular `o`).
5. **M3.3.2 (Instruções com Utilitários Legados):** Menção ao comando `docker-compose` em vez do comando `docker compose`.

### Seleção da Ação de Melhoria: Issue #118 e #119

A lacuna revelada por **M3.4.3** foi selecionada como objeto direto da intervenção corretiva, materializada na [Issue #118](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/118):
- **Diagnóstico:** O Excalidraw armazena 52 propriedades no formato `.excalidraw`, mas apenas 14 constam na documentação textual (`json-schema.mdx`). Não existe no repositório nenhum arquivo JSON Schema (`schema.json`) automatizado que possa ser validado por ferramentas externas ou IDEs.
- **Intervenção Proposta:**
  1. Criação de um esquema formal JSON Schema Draft 07 (`packages/excalidraw/schema/excalidraw.schema.json`) contemplando a totalidade das 52 propriedades reais de cena e elementos.
  2. Implementação de script de validação automática nos testes de CI/CD para assegurar que novos campos adicionados ao TypeScript atualizem o esquema.
  3. Atualização integral da documentação em `dev-docs/docs/codebase/json-schema.mdx`, elevando a cobertura de M3.4.3 de 26,9% para 100,0% e eliminando a principal fragilidade de interoperabilidade do projeto.

---

## 7. Registro de Rastreabilidade e Esforço Real

### 7.1 Rastreabilidade com os Dados Brutos

Todos os arquivos que sustentam este relatório estão disponíveis no repositório:

<p className="tabela-titulo">Tabela 4: Rastreabilidade entre métricas e dados brutos auditáveis</p>

| Métrica | Arquivo de Evidência | Caminho Relativo |
| :---: | :--- | :--- |
| **M3.1.1** | Terminal output do Browserslist | [`dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.1_cobertura_browserslist.txt`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.1_cobertura_browserslist.txt) |
| **M3.1.2** | Matriz de testes dos 6 ambientes | [`dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.2_matriz_integracao.csv`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.2_matriz_integracao.csv) |
| **M3.1.2** | Mosaico de capturas de tela do canvas | [`dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.2_evidencia_ambiente.png`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.2_evidencia_ambiente.png) |
| **M3.1.2** | Arquivo compactado com logs de build | [`dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.2_build_logs.zip`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.2_build_logs.zip) |
| **M3.1.3** | Formulário de auditoria iPad e caneta | [`dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.3_formulario_toque_caneta.csv`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.3_formulario_toque_caneta.csv) |
| **M3.1.3** | Gravação de tela por toque no iPad | [`dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.3_gravacao_toque.mp4`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.3_gravacao_toque.mp4) |
| **M3.1.3** | Gravação de tela com stylus no iPad | [`dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.3_gravacao_caneta.mp4`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.3_gravacao_caneta.mp4) |
| **M3.2.1** | Tabela com 20 medições DevTools | [`dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.1_tempos_abertura.csv`](../../dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.1_tempos_abertura.csv) |
| **M3.2.1** | Pasta com 20 traces JSON | `dados/fase-04/brutos/Q3.2-escalabilidade/traces_abertura/` |
| **M3.2.2** | Tabela de FPS em edição contínua | [`dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.2_fps_edicao.csv`](../../dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.2_fps_edicao.csv) |
| **M3.2.3** | Tabela de conferência de estresse | [`dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.3_tamanho_maximo_salvamento.csv`](../../dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.3_tamanho_maximo_salvamento.csv) |
| **M3.3.1** | Tabela das 9 operações de pacote | [`dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.1_resultados_pacote.csv`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.1_resultados_pacote.csv) |
| **M3.3.1** | Log de operações npm, yarn e pnpm | [`dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.1_log_operacoes_pacote.txt`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.1_log_operacoes_pacote.txt) |
| **M3.3.2** | Tabela de auditoria dos passos | [`dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.2_passos_ajustes.csv`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.2_passos_ajustes.csv) |
| **M3.3.2** | Log detalhado da execução de passos | [`dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.2_log_reproducao_passos.txt`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.2_log_reproducao_passos.txt) |
| **M3.3.3** | Tabela das 4 verificações Docker | [`dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.3_verificacoes_docker.csv`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.3_verificacoes_docker.csv) |
| **M3.4.1** | Catálogo dos formatos abertos | [`dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.1_catalogo_formatos.csv`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.1_catalogo_formatos.csv) |
| **M3.4.2** | Relatório de preservação de elementos | [`dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.2_preservacao_formatos.csv`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.2_preservacao_formatos.csv) |
| **M3.4.2** | Cenas exportadas e reimportadas | [`dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.2_arquivos_reimportados.zip`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.2_arquivos_reimportados.zip) |
| **M3.4.3** | Auditoria dos 52 campos do esquema | [`dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.3_conferencia_campos.csv`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.3_conferencia_campos.csv) |
| **M3.4.3** | Relatório técnico de campos omitidos | [`dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.3_relatorio.txt`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.3_relatorio.txt) |

<p className="tabela-fonte">Fonte: Elaborado pela autora, 2026.</p>

### 7.2 Esforço Real Investido

O esforço total dedicado à execução da Fase 04 para o objetivo G3 somou aproximadamente 11 horas e 42 minutos de trabalho técnico estruturado, distribuído em 6 turnos de atividade:

<p className="tabela-titulo">Tabela 5: Distribuição do esforço real investido na Fase 04</p>

| Turno e Data | Duração | Atividades Realizadas | Foco Principal |
| :--- | :---: | :--- | :--- |
| **Manhã (10/11)** | **3h45** | Resolução de conflitos do PR #151, leitura dos critérios da Fase 04 e decisão pelo setup Docker | Planejamento e alinhamento |
| **Tarde (10/11)** | **2h00** | Importação e verificação da imagem Docker, medições Browserslist e verificações Docker | M3.1.1 e M3.3.3 |
| **Noite e Madrugada (10-11/11)** | **3h20** | Auditoria de formatos, script de reimportação, auditoria de campos do esquema e testes de escalabilidade (20 traces DevTools, FPS e estresse de salvamento) | M3.4.1, M3.4.2, M3.4.3, M3.2.1, M3.2.2 e M3.2.3 |
| **Manhã (11/11)** | **0h57** | Build dos pacotes locais do monorepo, teste das 9 operações de pacote e reprodução dos 7 passos de execução | M3.3.1 e M3.3.2 |
| **Tarde (11/11, Turno 1)** | **1h11** | Empacotamento de subpacotes locais, criação e automação dos 6 ambientes da matriz de integração (Vite e Next.js) e diagnóstico de SSR | M3.1.2 |
| **Tarde (11/11, Turno 2)** | **0h29** | Configuração da rede local Docker, conexão do iPad e execução manual das 10 ações por toque e caneta | M3.1.3 e Consolidação Final |
| **Total Acumulado** | **11h42** | 12 de 12 métricas concluídas (100%), todas as hipóteses confrontadas e dados catalogados | Conclusão do Objetivo G3 |

<p className="tabela-fonte">Fonte: Elaborado pela autora, 2026.</p>

---

## 8. Referências Bibliográficas

> <Link id="ref-1">1.</Link> HEITLAGER, Ilja; KUIPERS, Tobias; VISSER, Joost. A practical model for measuring maintainability. In: **6th International Conference on the Quality of Information and Communications Technology (QUATIC 2007)**. IEEE, 2007. p. 30–39.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| `1.0` | 11/11/2026 | Elaboração do relatório consolidado de resultados e julgamento do objetivo G3 (Flexibilidade). | [Maria Eduarda](https://github.com/eduarda-ogomes) | |
