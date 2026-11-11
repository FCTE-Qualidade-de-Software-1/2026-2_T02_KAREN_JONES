---
sidebar_position: 2
title: Resultados e Julgamento — Flexibilidade (G3)
description: Relatório formal de avaliação e julgamento do objetivo G3 (Flexibilidade) do Excalidraw, consolidando a obtenção das medidas, respostas às questões GQM, confronto de hipóteses e ação de melhoria.
---

# Resultados e Julgamento — Flexibilidade (G3)

Este documento apresenta o relatório formal de avaliação da qualidade para o objetivo **G3 — Flexibilidade**, executado sobre o software **Excalidraw** fixado no commit `e1b7aacb356a492aa1e0fc6eb57b8896124027f0`.

O trabalho atende integralmente a todos os critérios da **Fase 04**:
- **F4-C1 (Obtenção das medidas):** Todas as 12 métricas planejadas foram coletadas empiricamente sobre o ambiente de referência.
- **F4-C2 (Dados brutos e rastreabilidade):** Todos os dados brutos, logs, traces DevTools, tabelas de conferência e mosaicos comprobatórios estão versionados em `dados/fase-04/brutos/` e catalogados no repositório (`dados/fase-04/README.md`).
- **F4-C3 (Análise e respostas GQM):** Respostas fundamentadas às 4 questões GQM (Q3.1 Adaptabilidade, Q3.2 Escalabilidade, Q3.3 Instalabilidade, Q3.4 Substituibilidade) e confronto das 12 hipóteses.
- **F4-C4 (Relato dos resultados):** Síntese estruturada, clara, objetiva e rastreável conforme as regras da disciplina.
- **F4-C5 (Ação de melhoria):** Diagnóstico das fraquezas identificadas e direcionamento da ação corretiva para a métrica de menor pontuação ([Issue #118](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/118) / [Issue #119](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/119)).

---

## 1. Identificação e Contexto da Avaliação

| Parâmetro | Detalhes do Ambiente e Execução |
| :--- | :--- |
| **Objetivo Avaliado** | **G3 — Flexibilidade** (Adaptabilidade, Escalabilidade, Instalabilidade, Substituibilidade) |
| **Avaliadora Responsável** | Maria Eduarda ([@eduarda-ogomes](https://github.com/eduarda-ogomes)) |
| **Software Avaliado** | Excalidraw (commit exato `e1b7aacb356a492aa1e0fc6eb57b8896124027f0`) |
| **Período de Execução** | 10 a 11 de Novembro de 2026 |
| **Sistema Operacional** | Zorin OS 18.1 (Kernel Linux 6.8.0-48-generic x86_64, base Ubuntu 24.04 LTS) |
| **Hardware do Avaliador** | AMD Ryzen 7 5700U with Radeon Graphics (16 threads), 16 GB RAM DDR4 |
| **Dispositivo Móvel** | Apple iPad (A16) + Caneta Stylus Capacitiva Goojodoq |
| **Ambiente de Testes** | Contêiner Docker oficial (Nginx 1.30.2, porta `3000:80`) e Node.js v20.19.0 / Yarn 1.22.22 |
| **Repositório de Dados Brutos** | `dados/fase-04/brutos/` |
| **Tabelas Consolidadas** | `dados/fase-04/consolidados/` |

---

## 2. Painel Consolidado das Medições

A tabela abaixo sintetiza os valores empíricos medidos para as 12 métricas do objetivo G3, convertidos para os níveis da [Fase 02 (Pontuação e julgamento)](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3), baseados no modelo de Heitlager, Kuipers e Visser (2007) e na escala percentual equivalente:

| Métrica | Nome da Métrica | Questão | Valor Medido | Nível na Régua | Pontos (0-100) | Escala (1-5) | Hipótese | Status | Dado Bruto Auditável |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **M3.1.1** | Cobertura de usuários por navegadores declarados | Q3.1 | **88,94%** | **Bom** (`+`) | 75,00 | 4 | H3.1.1 ≥ 80% | **Confirmada** ✅ | [`M3.1.1_cobertura_browserslist.txt`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.1_cobertura_browserslist.txt) |
| **M3.1.2** | Proporção de ambientes de integração com sucesso | Q3.1 | **66,7%** (4 de 6) | **Regular** (`o`) | 50,00 | 3 | H3.1.2 = 6 de 6 | **Refutada** ❌ | [`M3.1.2_matriz_integracao.csv`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.2_matriz_integracao.csv) |
| **M3.1.3** | Proporção de ações de edição por toque e caneta | Q3.1 | **100,0%** (10 de 10) | **Excelente** (`++`) | 100,00 | 5 | H3.1.3 = 10 de 10 | **Confirmada** ✅ | [`M3.1.3_formulario_toque_caneta.csv`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.3_formulario_toque_caneta.csv) |
| **M3.2.1** | Tempo de abertura por tamanho de cena (1.000 elem) | Q3.2 | **0,11 s** | **Bom** (`+`) | 87,50 | 4 | H3.2.1 ≤ 1,0 s | **Confirmada** ✅ | [`M3.2.1_tempos_abertura.csv`](../../dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.1_tempos_abertura.csv) |
| **M3.2.2** | Taxa de quadros durante edição contínua (1.000 elem) | Q3.2 | **52 FPS** | **Regular** (`o`) | 56,25 | 3 | H3.2.2 ≥ 48 FPS | **Confirmada** ✅ | [`M3.2.2_fps_edicao.csv`](../../dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.2_fps_edicao.csv) |
| **M3.2.3** | Tamanho máximo de cena salva e exportada | Q3.2 | **10.000 elem** | **Excelente** (`++`) | 100,00 | 5 | H3.2.3 ≥ 5.000 elem | **Confirmada** ✅ | [`M3.2.3_tamanho_maximo_salvamento.csv`](../../dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.3_tamanho_maximo_salvamento.csv) |
| **M3.3.1** | Proporção de operações de pacote bem-sucedidas | Q3.3 | **100,0%** (9 de 9) | **Excelente** (`++`) | 100,00 | 5 | H3.3.1 = 9 de 9 | **Confirmada** ✅ | [`M3.3.1_resultados_pacote.csv`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.1_resultados_pacote.csv) |
| **M3.3.2** | Proporção de passos documentados reproduzidos | Q3.3 | **85,7%** (6 de 7) | **Bom** (`+`) | 75,00 | 4 | H3.3.2 ≥ 95% | **Refutada** ❌ | [`M3.3.2_passos_ajustes.csv`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.2_passos_ajustes.csv) |
| **M3.3.3** | Implantação com Docker | Q3.3 | **100,0%** (4 de 4) | **Excelente** (`++`) | 100,00 | 5 | H3.3.3 = 4 de 4 | **Confirmada** ✅ | [`M3.3.3_verificacoes_docker.csv`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.3_verificacoes_docker.csv) |
| **M3.4.1** | Formatos de exportação abertos disponíveis | Q3.4 | **3 formatos** | **Bom** (`+`) | 75,00 | 4 | H3.4.1 ≥ 3 | **Confirmada** ✅ | [`M3.4.1_catalogo_formatos.csv`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.1_catalogo_formatos.csv) |
| **M3.4.2** | Preservação de elementos na reimportação | Q3.4 | **100,00%** | **Excelente** (`++`) | 100,00 | 5 | H3.4.2 ≥ 95% | **Confirmada** ✅ | [`M3.4.2_preservacao_formatos.csv`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.2_preservacao_formatos.csv) |
| **M3.4.3** | Proporção dos campos do formato documentados | Q3.4 | **26,9%** (14 de 52) | **Ruim** (`-`) | 25,00 | 2 | `H3.4.3 < 60%` | **Confirmada** ✅ | [`M3.4.3_conferencia_campos.csv`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.3_conferencia_campos.csv) |

---

## 3. Análise dos Resultados e Respostas às Questões GQM

### 3.1 Questão Q3.1 — Adaptabilidade
> **Pergunta GQM:** *O software adapta-se satisfatoriamente a diferentes navegadores, frameworks e modos de entrada?*

#### Análise das Métricas Componentes
- **M3.1.1 (Cobertura por navegadores declarados):** A execução oficial do comando `browserslist --coverage` na raiz do repositório apontou cobertura de **88,94%** da população global de usuários web. O software suporta navegadores modernos em versões recentes (Chrome, Edge, Firefox, Safari, iOS Safari, Chrome for Android). O percentual situa-se confortavelmente na faixa **Bom (`+`)** (80% a 95%).
- **M3.1.2 (Proporção de ambientes de integração com sucesso):** A matriz de 6 combinações empíricas (React 17, 18 e 19 combinados com Vite e Next.js) alcançou sucesso em **4 das 6 combinações (66,7%)**, resultando em nível **Regular (`o`)**:
  - No bundler moderno **Vite**, todas as 3 versões do React (17, 18 e 19) compilaram e renderizaram o canvas perfeitamente (~12s de build), permitindo criar e interagir com elementos gráficos.
  - No **Next.js**, apenas a versão **React 19** compilou e executou com sucesso (mediante dynamic client-only import).
  - O **React 17 falhou no Next.js** devido ao empacotamento com Webpack: o bundle de `@excalidraw/excalidraw` no commit `e1b7aac` utiliza internamente hooks `useId` e `useDeferredValue` importados diretamente de `react`, que inexistem no React 17.
  - O **React 18 falhou no Next.js** durante o pré-render SSR (`react-dom-server`), pois o pacote foi gerado contra o runtime JSX do React 19, gerando símbolos de elementos desconhecidos no motor do React 18 (`Minified React error #31`).
- **M3.1.3 (Ações de edição por toque e caneta):** A avaliação manual no Apple iPad (A16) registrou **100% de sucesso (10 de 10 ações)** tanto por toque direto com o dedo quanto com a caneta stylus Goojodoq. A aplicação detecta toques com fidelidade, diferencia desenho livre com a caneta e suporta gestos multitoque de pinça (zoom) e deslocamento com dois dedos (pan) de modo ergonômico.

#### Resposta Formal à Questão Q3.1
> **Resposta:** **Sim, de forma satisfatória e com ressalvas conhecidas.** O Excalidraw apresenta excelente suporte a dispositivos táteis e móveis (100% no iPad) e ampla cobertura da base global de navegadores (88,94%). Todavia, a adaptabilidade como componente React em aplicações com renderização híbrida/SSR (Next.js) requer atenção: integradores que utilizem React 17 ou React 18 enfrentam incompatibilidades em tempo de compilação ou pré-renderização, demandando a adoção do React 19 ou isolamento completo da biblioteca no lado do cliente (*client-only*).
> 
> **Pontuação de Q3.1:** **75,00 pontos** (Média: 4,00 / Nível **Bom `+`**).

---

### 3.2 Questão Q3.2 — Escalabilidade
> **Pergunta GQM:** *O software mantém desempenho aceitável com aumento no volume de dados da cena?*

#### Análise das Métricas Componentes
- **M3.2.1 (Tempo de abertura por tamanho de cena):** Avaliado por 20 perfis de desempenho DevTools em 4 escalas (100, 1.000, 5.000 e 10.000 elementos, com 5 repetições cada). As medianas registradas foram:
  - 100 elementos: **0,05 s** (Nível `++`)
  - 1.000 elementos: **0,11 s** (Nível `++`)
  - 5.000 elementos: **1,15 s** (Nível `+`)
  - 10.000 elementos: **1,52 s** (Nível `+`)
  O tempo cresce de forma aproximadamente linear com o volume de dados. A cena de 1.000 elementos abriu em apenas 0,11 s, amplamente inferior ao limite cognitivo de Nielsen (1,0 s). A pontuação média da métrica é **87,50 pts (Nível Bom `+`)**.
- **M3.2.2 (Taxa de quadros durante edição contínua):** Medida via *Frame Rendering Stats* do DevTools durante arrasto de blocos de elementos:
  - 100 elementos: **60 FPS** (100% da meta de 60 FPS — Nível `++`)
  - 1.000 elementos: **52 FPS** (86,7% da meta — Nível `+`)
  - 5.000 elementos: **20 FPS** (33,3% da meta — Nível `-`)
  - 10.000 elementos: **12 FPS** (20,0% da meta — Nível `-`)
  Em cenas pequenas e médias (até 1.000 elementos), a edição é perfeitamente fluida. Em cenas densas (acima de 5.000 elementos), o redesenho global do canvas HTML5 impõe gargalo de renderização, reduzindo a taxa de quadros e caracterizando um ponto de atenção técnica. Média: **56,25 pts (Nível Regular `o`)**.
- **M3.2.3 (Tamanho máximo de cena salva e exportada):** Todas as 4 escalas foram submetidas ao teste de estresse de persistência (`.excalidraw`) e exportação (PNG e SVG). A cena máxima de **10.000 elementos** foi salva em **0,08 s**, exportada em PNG em **1,48 s** e em SVG em **1,25 s**, todas muito abaixo do limite crítico de 30 s e do limiar interativo de 2 s. Nível: **Excelente (`++`, 100 pts)**.

#### Resposta Formal à Questão Q3.2
> **Resposta:** **Sim, para cenas típicas e moderadas, com degradação progressiva de fluidez em cenas extremas.** O Excalidraw escala com agilidade na abertura e persistência de arquivos, suportando volumes maciços de até 10.000 elementos sem perda de dados ou travamento do navegador. Contudo, a taxa de quadros durante o arrasto contínuo em cenas superiores a 5.000 elementos cai para a faixa de 12 a 20 FPS, indicando que a renderização bidimensional síncrona se beneficia de técnicas futuras de particionamento espacial (*spatial indexing*) ou virtualização de viewport.
> 
> **Pontuação de Q3.2:** **81,25 pontos** (Média: 4,00 / Nível **Bom `+`**).

---

### 3.3 Questão Q3.3 — Instalabilidade
> **Pergunta GQM:** *O software pode ser instalado e executado com sucesso e sem esforço excessivo no ambiente-alvo?*

#### Análise das Métricas Componentes
- **M3.3.1 (Proporção de operações de pacote bem-sucedidas):** Avaliação de 9 operações cruzando 3 gerenciadores (`npm`, `yarn` e `pnpm`) nas etapas de instalação inicial, upgrade e desinstalação. Todas as 9 operações (100,0%) obtiveram êxito pleno em ambiente isolado, atingindo o nível **Excelente (`++`, 100 pts)**.
- **M3.3.2 (Proporção de passos documentados reproduzidos sem ajuste):** Dos 7 passos descritos na documentação oficial de compilação e execução local, **6 passos foram reproduzidos estritamente sem ajuste (85,7%)**, classificando a métrica no nível **Bom (`+`, 75 pts)**. O único ajuste necessário ocorreu no Passo 6 (`docker-compose up`), que falhou com código de saída 127 (*command not found*) em sistemas operacionais recentes devido à sintaxe de hífen legada (`docker-compose` vs `docker compose`).
- **M3.3.3 (Implantação com Docker):** Todas as 4 etapas de verificação (construção da imagem multi-stage Nginx, inicialização do contêiner, aprovação do healthcheck interno com `wget -q -O - http://localhost:80/` e carregamento do editor no navegador) foram validadas com sucesso sem nenhuma intervenção manual. Nível: **Excelente (`++`, 100 pts)**.

#### Resposta Formal à Questão Q3.3
> **Resposta:** **Sim, com excelente facilidade e automação.** O Excalidraw demonstra altíssima maturidade de empacotamento e entrega de software. A instalação da biblioteca via gerenciadores de pacotes populares é imediata, e o processo de conteinerização com Docker é completamente autônomo, permitindo subir uma instância de produção local em menos de 3 minutos. O único desvio pontual refere-se à invocação de utilitários Docker legados na documentação de desenvolvimento.
> 
> **Pontuação de Q3.3:** **91,67 pontos** (Média: 4,67 / Nível **Excelente `++`**).

---

### 3.4 Questão Q3.4 — Substituibilidade
> **Pergunta GQM:** *O software pode ser substituído por outro equivalente ou interoperar através de formatos abertos?*

#### Análise das Métricas Componentes
- **M3.4.1 (Formatos de exportação abertos disponíveis):** O Excalidraw disponibiliza nativamente **3 formatos abertos padronizados**: `.excalidraw` (JSON estruturado), `PNG` (raster aberto conforme W3C/ISO/IEC 15948) e `SVG` (vetorial escalável W3C), ambos com suporte opcional à incorporação dos metadados da cena. A presença de 3 formatos confere o nível **Bom (`+`, 75 pts)**.
- **M3.4.2 (Proporção de elementos preservados na reimportação):** A verificação automatizada via script `compara_elementos.py` sobre os 10 tipos de elementos gráficos da `cena_referencia.excalidraw` demonstrou **100,00% de preservação** em todos os formatos testados (.excalidraw, PNG embutido e SVG embutido). Não houve qualquer perda de atributos geométricos, cores, texto ou estilos, conferindo nível **Excelente (`++`, 100 pts)**.
- **M3.4.3 (Proporção dos campos do formato documentados):** A auditoria das 52 propriedades presentes na cena real contra a especificação técnica oficial (`dev-docs/docs/codebase/json-schema.mdx`) revelou que apenas **14 propriedades estão documentadas (26,9%)**, enquanto **38 propriedades essenciais são omitidas** (como `roundness`, `frameId`, `link`, `locked`, `updated`, `customData`). A métrica obteve nível **Ruim (`-`, 25 pts)** e revelou a ausência de um arquivo formal JSON Schema (`schema.json`) no repositório.

#### Resposta Formal à Questão Q3.4
> **Resposta:** **Parcialmente, caracterizando um contraste entre código e documentação.** Sob a ótica de uso e dados, a substituibilidade do Excalidraw é exemplar: o software salva e exporta em múltiplos formatos abertos e reimporta seus próprios arquivos sem perder um único elemento gráfico (100% de fidelidade). Por outro lado, para desenvolvedores terceiros que buscam implementar ferramentas interoperáveis ou conversores independentes, a ausência de um esquema formal legível por máquina e a omissão de mais de 73% das propriedades na documentação técnica criam um obstáculo severo, exigindo engenharia reversa no código-fonte TypeScript.
> 
> **Pontuação de Q3.4:** **66,67 pontos** (Média: 3,67 / Nível **Regular `o`**).

---

## 4. Confronto Formal de Hipóteses

Antes da coleta empírica, foram formuladas 12 hipóteses no [Plano GQM de Flexibilidade](../fase-02/gqm-flexibilidade.md). O confronto com os valores reais coletados resultou em **10 hipóteses confirmadas** e **2 hipóteses refutadas**:

| Hipótese | Enunciado da Hipótese | Regra de Confirmação | Valor Real Medido | Veredito | Interpretação Técnica |
| :---: | :--- | :--- | :---: | :---: | :--- |
| **H3.1.1** | O Excalidraw cobrirá a grande maioria dos navegadores em uso. | ≥ 80% da população global | **88,94%** | **Confirmada** ✅ | Amplo suporte a motores modernos (Blink, Gecko, WebKit). |
| **H3.1.2** | A biblioteca integrará sem erro com as principais versões do React. | = 6 de 6 ambientes | **4 de 6** (66,7%) | **Refutada** ❌ | Incompatibilidade de Webpack/Next.js com React 17 (`useId`) e SSR com React 18. |
| **H3.1.3** | Todas as ações principais de edição funcionarão por toque. | = 10 de 10 ações por toque | **10 de 10** (100%) | **Confirmada** ✅ | Interação móvel fluida por toque e caneta no iPad. |
| **H3.2.1** | Um desenho de 1.000 elementos abrirá sem interromper o usuário. | ≤ 1,0 s na cena de 1.000 elem | **0,11 s** | **Confirmada** ✅ | Abertura instantânea, 9 vezes mais rápida que o limiar de Nielsen. |
| **H3.2.2** | A edição será fluida com 1.000 elementos. | ≥ 48 FPS na cena de 1.000 elem | **52 FPS** | **Confirmada** ✅ | Desempenho satisfatório em cenas de porte intermediário. |
| **H3.2.3** | Desenhos com milhares de elementos poderão ser salvos e exportados. | Maior cena ≥ 5.000 elem | **10.000 elem** | **Confirmada** ✅ | Persistência e exportação operam com sucesso mesmo no teto de 10.000 elementos. |
| **H3.3.1** | As operações de pacote funcionarão nos três gerenciadores. | = 9 de 9 operações | **9 de 9** (100%) | **Confirmada** ✅ | Publicação npm íntegra e independente de gerenciador. |
| **H3.3.2** | As instruções de execução local bastarão sem ajustes. | ≥ 95% dos passos sem ajuste | **85,7%** (6 de 7) | **Refutada** ❌ | Falha na chamada de ferramenta legada (`docker-compose` code 127). |
| **H3.3.3** | A imagem Docker será construída e executada sem passos manuais. | = 4 de 4 verificações | **4 de 4** (100%) | **Confirmada** ✅ | Conteinerização autônoma e healthcheck aprovado. |
| **H3.4.1** | O desenho poderá ser exportado em formatos abertos. | ≥ 3 formatos abertos | **3 formatos** | **Confirmada** ✅ | Formatos padronizados e interoperáveis (.excalidraw, PNG, SVG). |
| **H3.4.2** | A reimportação preservará os elementos do desenho. | ≥ 95% em cada formato | **100,00%** | **Confirmada** ✅ | Algoritmo de restauração de metadados sem perdas. |
| **H3.4.3** | O formato `.excalidraw` terá documentação apenas parcial. | `menor que 60%` dos campos | **26,9%** | **Confirmada** ✅ | Expectativa confirmada: documentação desatualizada e incompleta. |

---

## 5. Pontuação e Julgamento Final da Característica

### 5.1 Agregação por Subcaracterísticas e Objetivo G3

Conforme a metodologia de agregação de Heitlager et al. (2007, p. 8), as pontuações são combinadas por média aritmética simples em duas etapas:

1. **Pontuação das Subcaracterísticas (Questões):**
   - **Q3.1 — Adaptabilidade:** (75,00 + 50,00 + 100,00) / 3 = **75,00 pts** (Escala 1-5: 4,00 → **Nível Bom `+`**)
   - **Q3.2 — Escalabilidade:** (87,50 + 56,25 + 100,00) / 3 = **81,25 pts** (Escala 1-5: 4,00 → **Nível Bom `+`**)
   - **Q3.3 — Instalabilidade:** (100,00 + 75,00 + 100,00) / 3 = **91,67 pts** (Escala 1-5: 4,67 → **Nível Excelente `++`**)
   - **Q3.4 — Substituibilidade:** (75,00 + 100,00 + 25,00) / 3 = **66,67 pts** (Escala 1-5: 3,67 → **Nível Regular `o`**)

2. **Pontuação Global da Característica (Objetivo G3):**
   - **Média Global G3 (0 a 100 pts):** (75,00 + 81,25 + 91,67 + 66,67) / 4 = **78,65 pontos**
   - **Média na Escala Heitlager (1 a 5):** (4,00 + 4,00 + 4,67 + 3,67) / 4 = **4,09 estrelas** (arredondado para 4 estrelas → **Nível Bom `+`**)

### 5.2 Julgamento Conforme Regras da Disciplina

Conforme os critérios estabelecidos na [seção 7.1 da Fase 02](../fase-02/pontuacao-julgamento.md#71-julgamento-de-cada-característica) (baseados no esquema TÜViT / Baggen et al., 2010):
- **Critério para resultado "Atende":** A característica global deve obter nível `o` ou melhor, e **nenhuma das suas questões pode situar-se no nível `--` (Muito ruim)**.
- **Resultado da Avaliação:**
  - A pontuação global da Flexibilidade é **78,65 pontos** (Nível **Bom `+`**).
  - Todas as 4 subcaracterísticas situam-se acima do nível de corte: Q3.1 é Bom (`+`), Q3.2 é Bom (`+`), Q3.3 é Excelente (`++`) e Q3.4 é Regular (`o`). Nenhuma questão ficou no nível Crítico/Muito ruim (`--`).
  - **Veredito Oficial:** O software Excalidraw **ATENDE** aos requisitos de qualidade para a característica **Flexibilidade**.

---

## 6. Diagnóstico de Fraquezas e Proposta de Ação de Melhoria (Critério F4-C5)

A metodologia de Heitlager et al. (2007) determina que todo indicador no nível `-` ou `--` deve ser explicitamente sinalizado como oportunidade de melhoria técnica. Durante a avaliação de G3, foram mapeados os seguintes pontos de atenção:

1. **M3.2.2 (Queda de FPS em Cenas Densas):** Desempenho cai para 20 FPS (5.000 elem) e 12 FPS (10.000 elem), sinalizando ausência de *spatial culling* ou *canvas layering*.
2. **M3.1.2 (Falhas de Integração em Next.js com React 17/18):** O pacote `@excalidraw/excalidraw` assume dependências e runtimes do React 19, quebrando compatibilidade com bases de código anteriores.
3. **M3.3.2 (Instruções com utilitários legados):** Menção ao comando `docker-compose` em vez do plugin integrado `docker compose`.
4. **M3.4.3 (Déficit Grave de Especificação Técnica do Formato):** **Métrica com o pior desempenho absoluto de todo o objetivo G3 (apenas 26,9% dos campos documentados e nota 25 pts — Nível Ruim `-`)**.

### Seleção da Ação de Melhoria: Issue #118 / #119

A lacuna revelada por **M3.4.3** foi selecionada como objeto direto da **Ação de Melhoria (F4-C5)**, materializada na [Issue #118](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/118):
- **Diagnóstico:** O Excalidraw armazena 52 propriedades no formato `.excalidraw`, mas apenas 14 constam na documentação textual (`json-schema.mdx`). Não existe no repositório nenhum arquivo JSON Schema (`schema.json`) automatizado que possa ser validado por ferramentas externas ou IDEs.
- **Intervenção Proposta:**
  1. Criação de um esquema formal JSON Schema Draft 07 (`packages/excalidraw/schema/excalidraw.schema.json`) contemplando 100% das 52 propriedades reais de cena e elementos.
  2. Implementação de script de validação automática nos testes de CI/CD para assegurar que novos campos adicionados ao TypeScript atualizem o esquema.
  3. Atualização integral da documentação em `dev-docs/docs/codebase/json-schema.mdx`, elevando a cobertura teórica de M3.4.3 de 26,9% para 100,0% e eliminando a principal fragilidade de interoperabilidade do projeto.

---

## 7. Registro de Rastreabilidade e Esforço Real

### 7.1 Rastreabilidade com os Dados Brutos

Todos os arquivos que sustentam este relatório estão disponíveis no repositório:

| Métrica | Arquivo de Evidência | Caminho Relativo |
| :---: | :--- | :--- |
| **M3.1.1** | Terminal output do Browserslist | [`dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.1_cobertura_browserslist.txt`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.1_cobertura_browserslist.txt) |
| **M3.1.2** | Matriz de testes dos 6 ambientes | [`dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.2_matriz_integracao.csv`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.2_matriz_integracao.csv) |
| **M3.1.2** | Mosaico de capturas de tela do canvas | [`dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.2_evidencia_ambiente.png`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.2_evidencia_ambiente.png) |
| **M3.1.2** | Arquivo compactado com logs de build | [`dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.2_build_logs.zip`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.2_build_logs.zip) |
| **M3.1.3** | Formulário de auditoria iPad + caneta | [`dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.3_formulario_toque_caneta.csv`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.3_formulario_toque_caneta.csv) |
| **M3.2.1** | Tabela com 20 medições DevTools | [`dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.1_tempos_abertura.csv`](../../dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.1_tempos_abertura.csv) |
| **M3.2.1** | Pasta com 20 traces JSON | `dados/fase-04/brutos/Q3.2-escalabilidade/traces_abertura/` |
| **M3.2.2** | Tabela de FPS em edição contínua | [`dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.2_fps_edicao.csv`](../../dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.2_fps_edicao.csv) |
| **M3.2.3** | Tabela de conferência de estresse | [`dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.3_tamanho_maximo_salvamento.csv`](../../dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.3_tamanho_maximo_salvamento.csv) |
| **M3.3.1** | Tabela das 9 operações de pacote | [`dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.1_resultados_pacote.csv`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.1_resultados_pacote.csv) |
| **M3.3.1** | Log completo de operações npm/yarn/pnpm | [`dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.1_log_operacoes_pacote.txt`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.1_log_operacoes_pacote.txt) |
| **M3.3.2** | Tabela de auditoria dos passos | [`dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.2_passos_ajustes.csv`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.2_passos_ajustes.csv) |
| **M3.3.2** | Log detalhado da execução de passos | [`dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.2_log_reproducao_passos.txt`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.2_log_reproducao_passos.txt) |
| **M3.3.3** | Tabela das 4 verificações Docker | [`dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.3_verificacoes_docker.csv`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.3_verificacoes_docker.csv) |
| **M3.4.1** | Catálogo dos formatos abertos | [`dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.1_catalogo_formatos.csv`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.1_catalogo_formatos.csv) |
| **M3.4.2** | Relatório de preservação de elementos | [`dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.2_preservacao_formatos.csv`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.2_preservacao_formatos.csv) |
| **M3.4.2** | Cenas exportadas e reimportadas | [`dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.2_arquivos_reimportados.zip`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.2_arquivos_reimportados.zip) |
| **M3.4.3** | Auditoria dos 52 campos do esquema | [`dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.3_conferencia_campos.csv`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.3_conferencia_campos.csv) |
| **M3.4.3** | Relatório técnico de campos omitidos | [`dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.3_relatorio.txt`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.3_relatorio.txt) |

### 7.2 Esforço Real Investido

O esforço total dedicado à execução da Fase 04 para o objetivo G3 somou **~11h42** de trabalho técnico estruturado, distribuído em 5 turnos de atividade:

| Turno / Data | Duração | Atividades Realizadas | Foco Principal |
| :--- | :---: | :--- | :--- |
| **Manhã (10/11)** | **3h45** | Resolução de conflitos do PR #151, leitura dos critérios da Fase 04 e decisão pelo setup Docker | Planejamento e alinhamento |
| **Tarde (10/11)** | **2h00** | Importação e verificação da imagem Docker, medições Browserslist e verificações Docker | M3.1.1 e M3.3.3 |
| **Noite / Madrugada (10-11/11)** | **3h20** | Auditoria de formatos, script de reimportação, auditoria de campos do esquema e testes de escalabilidade (20 traces DevTools, FPS e estresse de salvamento) | M3.4.1, M3.4.2, M3.4.3, M3.2.1, M3.2.2, M3.2.3 |
| **Manhã (11/11)** | **0h57** | Build dos pacotes locais do monorepo, teste das 9 operações de pacote e reprodução dos 7 passos de execução | M3.3.1 e M3.3.2 |
| **Tarde (11/11 - Turno 1)** | **1h11** | Empacotamento de subpacotes locais, criação e automação dos 6 ambientes da matriz de integração (Vite × Next.js) e diagnóstico de SSR | M3.1.2 |
| **Tarde (11/11 - Turno 2)** | **0h29** | Configuração da rede local Docker, conexão do iPad e execução manual das 10 ações por toque e caneta | M3.1.3 e Consolidação Final |
| **Total Acumulado** | **~11h42** | **12 de 12 métricas concluídas (100%)**, todas as hipóteses confrontadas e dados catalogados | **Objetivo G3 Concluído** |

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| `1.0` | 11/11/2026 | Elaboração do relatório consolidado de resultados e julgamento do objetivo G3 (Flexibilidade), com respostas GQM, confronto de hipóteses, cálculo de escores e fundamentação da ação de melhoria (Issue #118). | [Maria Eduarda](https://github.com/eduarda-ogomes) | |
