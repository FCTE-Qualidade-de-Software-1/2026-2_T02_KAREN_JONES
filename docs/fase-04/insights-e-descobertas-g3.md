---
sidebar_position: 1
title: Insights e Descobertas Preliminares — Flexibilidade (G3)
description: Relatório analítico preliminar da coleta empírica das métricas do objetivo G3 (Flexibilidade) no Excalidraw, consolidando dados brutos, hipóteses confirmadas, diagnósticos técnicos e oportunidades de melhoria.
---

# Insights e Descobertas Preliminares — Flexibilidade (G3)

Este documento consolida os resultados, análises empíricas e descobertas obtidas durante a execução inicial da **Fase 04** para o objetivo **G3 — Flexibilidade**, conduzida pela avaliadora responsável Maria Eduarda sobre a versão de referência do Excalidraw (commit `e1b7aacb356a492aa1e0fc6eb57b8896124027f0`).

A coleta atende aos critérios **F4-C1** (obtenção das medidas), **F4-C2** (rastreabilidade aos dados brutos) e **F4-C3** (análise e respostas GQM), fundamentando também as discussões para o **Ponto de Controle 2** e a seleção da **Ação de Melhoria** (critério **F4-C5** / [Issue #118](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/118)).

---

## 1. Contexto e Ambiente de Execução

As medições foram conduzidas estritamente sob as condições de contorno fixadas na [Fase 03 (Recursos e ambiente)](../fase-03/recursos-ambiente.md):

| Parâmetro | Configuração Efetiva Registrada |
| :--- | :--- |
| **Avaliadora Responsável** | Maria Eduarda ([@eduarda-ogomes](https://github.com/eduarda-ogomes)) |
| **Data da Coleta** | 10 de Novembro de 2026 |
| **Software Avaliado** | Excalidraw (commit exato `e1b7aac`) |
| **Sistema Operacional** | Zorin OS 18.1 (Kernel Linux x86_64, base Ubuntu 24.04 LTS / Noble) |
| **Processador** | AMD Ryzen 7 5700U with Radeon Graphics |
| **Memória RAM** | 10 GB utilizáveis (16 GB físicos instalados) |
| **Ambiente de Execução** | Contêiner Docker oficial (base Nginx 1.30.2) em `http://localhost:3000` |
| **Repositório de Dados Brutos** | `dados/fase-04/brutos/` |

---

## 2. Painel Consolidado das Métricas Coletadas

Até o presente momento, **todas as 12 métricas de G3 (100% do objetivo de Flexibilidade)** foram integralmente coletadas, auditadas e confrontadas com as hipóteses e réguas da [Fase 02 (Pontuação e julgamento)](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3):

| Métrica | Nome da Métrica | Questão | Valor Medido | Nível na Régua | Hipótese GQM | Status da Hipótese |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **M3.1.1** | Cobertura de usuários pelos navegadores declarados | Q3.1 | **88,94%** | **Bom** (75 pts) | H3.1.1 ≥ 80% | **Confirmada** ✅ |
| **M3.1.2** | Proporção de ambientes de integração com sucesso | Q3.1 | **66,7%** (4 de 6) | **Regular** (50 pts) | H3.1.2 = 6 de 6 | **Refutada** ❌ |
| **M3.1.3** | Proporção de ações de edição por toque e caneta | Q3.1 | **100,0%** (10 de 10) | **Excelente** (100 pts) | H3.1.3 = 10 de 10 | **Confirmada** ✅ |
| **M3.2.1** | Tempo de abertura por tamanho de cena | Q3.2 | **0,11 s** (1.000 elem) | **Bom** (87,5 pts) | H3.2.1 ≤ 1,0 s | **Confirmada** ✅ |
| **M3.2.2** | Taxa de quadros durante a edição por tamanho de cena | Q3.2 | **52 FPS** (1.000 elem) | **Regular** (56,25 pts) | H3.2.2 ≥ 48 FPS | **Confirmada** ✅ |
| **M3.2.3** | Tamanho máximo de cena salva e exportada | Q3.2 | **10.000 elem** | **Excelente** (100 pts) | H3.2.3 ≥ 5.000 elem | **Confirmada** ✅ |
| **M3.3.1** | Proporção de operações de pacote bem-sucedidas | Q3.3 | **100,0%** (9 de 9) | **Excelente** (100 pts) | H3.3.1 = 9 de 9 | **Confirmada** ✅ |
| **M3.3.2** | Proporção de passos documentados reproduzidos | Q3.3 | **85,7%** (6 de 7) | **Bom** (75 pts) | H3.3.2 ≥ 95% | **Refutada** ❌ |
| **M3.3.3** | Implantação com Docker | Q3.3 | **100,0%** (4 de 4) | **Excelente** (100 pts) | H3.3.3 = 4 de 4 | **Confirmada** ✅ |
| **M3.4.1** | Formatos de exportação abertos disponíveis | Q3.4 | **3 formatos** | **Bom** (75 pts) | H3.4.1 ≥ 3 | **Confirmada** ✅ |
| **M3.4.2** | Proporção de elementos preservados na reimportação | Q3.4 | **100,00%** | **Excelente** (100 pts) | H3.4.2 ≥ 95% | **Confirmada** ✅ |
| **M3.4.3** | Proporção dos campos do formato documentados | Q3.4 | **26,9%** (14 de 52) | **Ruim** (25 pts) | H3.4.3 < 60% | **Confirmada** ✅ |

---

## 3. Principais Insights e Descobertas Técnicas

### 💡 Insight 1: O Contraste entre a Robustez do Código e a Fragilidade da Documentação (Substituibilidade — Q3.4)

A análise cruzada entre as métricas **M3.4.2** e **M3.4.3** revelou uma discrepância técnica profunda no ecossistema do Excalidraw:

1. **Excelência no Motor de Serialização (M3.4.2 = 100%):**
   - O teste prático de ciclo de vida (exportação da `cena_referencia.excalidraw` contendo todos os 10 tipos de elementos gráficos da Fase 02 para `.excalidraw`, `.png` e `.svg`, seguido de reabertura e comparação matemática via `scripts/compara_elementos.py`) resultou em **preservação perfeita de 100% dos elementos**.
   - O mecanismo de embutir metadados da cena em imagens PNG e vetores SVG (*Embed scene data*) provou-se altamente confiável: tipos, coordenadas espaciais (`x`, `y`, `width`, `height`), estilos visuais (`strokeColor`, `backgroundColor`, `fillStyle`, `strokeWidth`) e textos foram preservados com **zero pixel de desvio e zero perda de informação**.
2. **Defasagem Crítica na Documentação Externa (M3.4.3 = 26,9%):**
   - Em contraste direto com a fidelidade do software, a especificação técnica pública oferecida aos desenvolvedores terceiros em `dev-docs/docs/codebase/json-schema.mdx` revelou-se extremamente superficial.
   - De **52 propriedades reais** gravadas pelo editor no arquivo de desenho, apenas **14 propriedades** estão descritas no documento.
   - Os mantenedores do projeto explicitamente omitiram as propriedades dos elementos gráficos no exemplo da documentação com o comentário de código:
     ```json
     {
       "id": "pologsyG-tAraPgiN9xP9b",
       "type": "rectangle",
       "x": 928,
       "y": 319,
       "width": 134,
       "height": 90
       /* ...other element properties */
     }
     ```
   - Propriedades vitais para a renderização do desenho — como `strokeColor`, `roundness`, `roughness`, `fontSize`, `opacity`, `frameId`, `boundElements` e `isDeleted` — **não constam na documentação oficial**, forçando desenvolvedores externos a inspecionar o código-fonte em TypeScript para compreender o formato.
   - Além disso, a auditoria constatou a **ausência total de um arquivo formal JSON Schema (`.json`)** validável por máquina no repositório.

---

### 💡 Insight 2: A Oportunidade Central para a Ação de Melhoria da Fase 04 (Critério F4-C5)

A comprovação empírica do nível **Crítico** em M3.4.3 oferece à equipe a melhor justificativa técnica para a **Ação de Melhoria** exigida pelas [Issues #118](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/118) e [#119](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/119):

* **Problema Diagnosticado:** Violação do princípio de transparência de formato aberto em conformidade com o requisito `RQ-FLEX-12`. Usuários e ferramentas externas enfrentam barreiras de interoperabilidade devido a 38 campos não documentados (apenas 26,9% de cobertura).
* **Proposta de Melhoria:**
  1. Redigir a complementação da documentação técnica dos elementos em `dev-docs/docs/codebase/json-schema.mdx`, detalhando os 38 campos identificados pela auditoria.
  2. Implementar um arquivo formal `packages/excalidraw/schema.json` contendo o JSON Schema canônico do formato `.excalidraw`.
* **Impacto Mensurável:** A implementação desta ação de melhoria elevará a métrica M3.4.3 de **26,9% (Nível Crítico)** para **100,0% (Nível Excelente)**, gerando impacto direto no indicador de Substituibilidade de G3.

---

### 💡 Insight 3: Ampla Cobertura Populacional sem Inflação de Polyfills (Adaptabilidade — Q3.1)

A métrica **M3.1.1** atingiu **88,94% de cobertura global**, garantindo o nível **Bom**:

* A regra de produção declarada em `excalidraw-app/package.json` equilibra modernidade e compatibilidade:
  ```json
  [
    ">0.2%",
    "not dead",
    "not ie <= 11",
    "not op_mini all",
    "not safari < 12",
    "not kaios <= 2.5",
    "not edge < 79",
    "not chrome < 70",
    "not and_uc < 13",
    "not samsung < 10"
  ]
  ```
* O descarte intencional de navegadores obsoletos (IE 11, Safari legado, Opera Mini) evita o aumento desnecessário do tamanho do pacote (*bundle size*) com *polyfills* legados, enquanto assegura funcionamento para a quase totalidade dos navegadores modernos móveis e desktop.

---

### 💡 Insight 4: Alta Reprodutibilidade na Esteira Docker (Instalabilidade — Q3.3)

A execução da métrica **M3.3.3** comprovou a facilidade de implantação do software em infraestrutura isolada:

* O contêiner de produção construído a partir do `Dockerfile` oficial executou sem ajustes, subiu com sucesso na porta `3000:80` e atingiu o estado `"healthy"` na checagem nativa de integridade em menos de 15 segundos.
* A entrega através de servidor Nginx interno garante independência completa de configurações do ambiente hospedeiro, validando o requisito `RQ-FLEX-09`.

### 💡 Insight 5: Desempenho e Degradação Graciosa sob Escala Extrema (Escalabilidade — Q3.2)

A medição empírica das três métricas da questão **Q3.2** revelou o comportamento do motor de renderização do Excalidraw sob estresse progressivo de volume de dados:

1. **Tempo de Abertura (M3.2.1):**
   - O tempo de carga da cena com 1.000 elementos atingiu mediana de **0,11 s**, confirmando com ampla folga a hipótese **H3.2.1 ≤ 1,0 s** (nível Excelente).
   - Sob 10.000 elementos (um arquivo massivo de 5,2 MB), o tempo de estabilização completa foi de apenas **1,52 s**, mantendo-se na faixa de conforto cognitivo humano definida por Nielsen (1993) e pelo modelo RAIL (inferior a 2 segundos).
2. **Taxa de Quadros em Edição Contínua (M3.2.2):**
   - Com 100 elementos, o editor fixa cravado no limite do monitor a **60 FPS** (100% de fluidez).
   - Na cena de 1.000 elementos, a taxa oscila entre 46 e 58 FPS, obtendo mediana de **52 FPS** e confirmando a hipótese **H3.2.2 ≥ 48 FPS** (nível Bom).
   - Sob 5.000 elementos (mediana de **20 FPS**) e 10.000 elementos (**12 FPS**), a aplicação apresenta degradação graciosa: o redesenho sofre redução de taxa de quadros (*dropped frames*), mas não ocorre congelamento da aba (*freeze*), travamento (*hang*) ou fechamento inesperado do navegador (*crash*).
3. **Persistência e Exportação sob Carga Máxima (M3.2.3):**
   - Todas as 4 escalas de cena completaram com sucesso as três operações (salvamento no disco em `.excalidraw`, exportação em PNG e exportação em SVG) em tempos inferiores a 2 segundos, muito abaixo do teto de tolerância de 30 segundos.
   - O tamanho máximo suportado atingiu **10.000 elementos**, confirmando a hipótese **H3.2.3 ≥ 5.000 elementos** e alcançando a pontuação máxima de **100 pontos (Excelente)**.

### 💡 Insight 6: Auditoria de Instalabilidade, Dependências de Monorepo e Obsolescência Documental (Instalabilidade — Q3.3)

A execução das métricas **M3.3.1** e **M3.3.2** complementou os dados da esteira Docker (M3.3.3), finalizando a avaliação de toda a questão **Q3.3**:

1. **Reprodutibilidade dos Passos Documentados (M3.3.2):**
   - Na via nativa (Node.js e Yarn), a clonagem, instalação de dependências e inicialização do servidor de desenvolvimento ocorreram de forma impecável: `yarn` instalou todas as dependências e configurou os *git hooks* do Husky com código 0 em 346s, e `yarn start` inicializou o Vite em apenas **1,09 s** respondendo com `HTTP/1.1 200 OK`.
   - Na via com Docker Compose, detectou-se uma incompatibilidade documental crítica: o guia `development.mdx` documenta a sintaxe legada `docker-compose up --build -d` (com hífen). Em distribuições modernas com Docker Engine v2 (como o Ubuntu/Zorin OS avaliado), o binário Python standalone não existe, gerando `command not found` (código 127) e exigindo ajuste corretivo para o plugin moderno `docker compose up`.
   - Com 6 de 7 passos bem-sucedidos sem ajuste (**85,7%**), a métrica atinge o **Nível Bom (75 pontos)**, mas **REFUTA a hipótese H3.3.2 (≥ 95%)** devido à defasagem da instrução de compose.
2. **Ciclo de Vida de Pacotes em Gerenciadores (M3.3.1):**
   - O teste comparativo nos 3 gerenciadores (`npm`, `yarn` v1 e `pnpm`) revelou que a distribuição estável pública (`@excalidraw/excalidraw@0.17.6`) cumpre 100% das 9 operações de instalação, atualização e desinstalação.
   - Contudo, a geração de tarball local a partir do commit de desenvolvimento (`excalidraw-excalidraw-0.18.0.tgz`, 31 MB) expõe um forte acoplamento com subpacotes internos do monorepo (`@excalidraw/common` e `@excalidraw/math`), os quais requerem publicação coordenada para permitir consumo isolado fora do monorepo via npm padrão.
   - Além disso, a execução de `require('@excalidraw/excalidraw')` direto no Node.js confirma que a biblioteca depende estritamente do DOM do navegador (`ReferenceError: document is not defined`), exigindo desativação de renderização no servidor (`ssr: false`) ao ser integrada em frameworks modernos como Next.js.


---

### 💡 Insight 7: Desafios de Compatibilidade em Frameworks SSR e Transição React 19 (Adaptabilidade — Q3.1 / M3.1.2)

A avaliação da métrica **M3.1.2** sobre as **6 combinações** de ecossistema (React 17, 18 e 19 cruzados com Vite e Next.js) revelou um contraste marcante entre empacotadores tradicionais e frameworks modernos com renderização no servidor:

1. **Robustez Plena sob Empacotador Vite (3 de 3 Sucessos):**
   - No Vite 5.4.11, as 3 versões de React (**React 17.0.2**, **React 18.2.0** e **React 19.0.0**) compilaram com código de saída 0 em tempo médio de **~12,1 s**.
   - Em todas as 3 variantes, o servidor de pré-visualização serviu a aplicação com HTTP 200, o canvas carregou sem exceções não tratadas e foi possível desenhar formas geométricas (retângulos com painel de propriedades) com validação automatizada via Puppeteer-core.
2. **Fragilidade Estrutural em Frameworks SSR (Next.js — 1 de 3 Sucessos):**
   - **React 17 + Next.js 12:** Falha crítica na compilação do Webpack (`next build`). Embora o `package.json` do `@excalidraw/excalidraw` declare formalmente compatibilidade com `"react": "^17.0.2 || ^18.2.0 || ^19.0.0"`, os arquivos JavaScript transcompilados do pacote realizam importações nomeadas dos hooks `useId` e `useDeferredValue` diretamente de `'react'`. Como esses hooks só foram criados no React 18, o Webpack acusa `Attempted import error` e encerra a compilação com código de erro 1.
   - **React 18 + Next.js 14:** Falha durante a etapa de pré-renderização estática (`prerender page /`). A versão do Excalidraw no commit avaliado (`e1b7aac`) foi migrada internamente para compilar seu JSX sob a especificação do React 19 (emissão de metadados de nó com símbolos do React 19). Quando empacotado junto ao React 18 no Next.js, o motor de SSR do React 18 rejeita os elementos com o erro `Minified React error #31 (Objects are not valid as a React child / symbol mismatch)` e acusa `ReferenceError: e is not defined` na invocação de logs estáticos.
   - **React 19 + Next.js 14:** Sucesso total comprovado no exemplo oficial do monorepo (`examples/with-nextjs`). O build completou em 65s via importação dinâmica com desativação de SSR (`dynamic(..., { ssr: false })`) e injeção de fontes estáticas na pasta pública, permitindo renderização perfeita do canvas e desenho de formas geométricas.
3. **Julgamento e Hipótese:**
   - Com **4 de 6 combinações bem-sucedidas (66,7%)**, a métrica atinge o nível **Regular (50 pontos)**.
   - A hipótese **H3.1.2 (= 6 de 6 combinações) é REFUTADA** ❌, demonstrando que integradores terceiros enfrentam barreiras severas e precisam aplicar adaptações consideráveis caso operem fora do ecossistema React 19 / Vite.


---

### 💡 Insight 8: Fluidez e Fidelidade na Interação por Toque e Stylus em Dispositivos Móveis (Adaptabilidade — Q3.1 / M3.1.3)

A execução da métrica **M3.1.3** encerrou a coleta de dados de Adaptabilidade (Q3.1) e de todo o objetivo G3, através de testes empíricos controlados conduzidos diretamente no hardware físico de referência (**Apple iPad A16**) conectado via Wi-Fi ao contêiner oficial do Excalidraw (`http://192.168.1.24:3000`), avaliando a entrada direta com o **dedo** e com **caneta capacitiva stylus (Goojodoq)**:

1. **Eficiência Multimodal e Desempenho com Dedo (10 de 10 Ações Aprovadas — 100%):**
   - O canvas respondeu de forma fluida a toques diretos para criação de formas, traçado à mão livre, seleção, arraste e redimensionamento de elementos.
   - O gesto de pinça (*pinch-to-zoom*) demonstrou resposta instantânea de ampliação e redução de escala sem travamentos ou quebras visuais.
   - **Comportamento de UX na Ação 7 (Deslocar tela / pan):** A avaliadora identificou um comportamento ergonômico intencional do Excalidraw: quando a ferramenta de seleção (setinha) está ativa, o arraste com um único dedo é reservado para seleção por caixa elástica (*marquee selection*), exigindo o toque simultâneo de 2 dedos para ativar o *pan*; ao ativar a ferramenta Mão (*hand tool*), o deslocamento da tela ocorre diretamente com apenas 1 dedo, simplificando a navegação.
2. **Precisão com Caneta Stylus Goojodoq (10 de 10 Ações Aprovadas — 100%):**
   - A caneta stylus apresentou alta precisão na ponta ativa, traçando desenhos livres e posicionando alças de redimensionamento sem latência perceptível.
   - A interação híbrida (desenhar com a ponta da caneta enquanto realiza navegação na tela com os dedos) operou de forma transparente, permitindo alternância instantânea entre escrita/desenho e gestos multitouch de navegação.
3. **Julgamento e Hipótese:**
   - Com **100,0% de sucesso** em ambas as vias de entrada (dedo e caneta), a métrica atinge o nível **Excelente (100 pontos)**.
   - A hipótese **H3.1.3 (= 10 de 10 ações) é CONFIRMADA** ✅, comprovando a maturidade ergonômica da interface do Excalidraw para dispositivos móveis e tablets.

---

## 4. Rastreabilidade com os Dados Brutos

Todos os dados brutos gerados durante estas coletas estão versionados e auditáveis na pasta `dados/fase-04/brutos/`:

| Métrica | Arquivo de Dado Bruto | Finalidade da Evidência |
| :---: | :--- | :--- |
| **M3.1.1** | [`M3.1.1_cobertura_browserslist.txt`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.1_cobertura_browserslist.txt) | Saída de terminal com a cobertura populacional e lista de navegadores. |
| **M3.1.2** | [`M3.1.2_matriz_integracao.csv`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.2_matriz_integracao.csv) | Tabela detalhada dos 6 ambientes com status de build, runtime, desenho e diagnóstico. |
| **M3.1.2** | [`M3.1.2_build_logs.zip`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.2_build_logs.zip) | Arquivo compactado com os logs brutos completos de instalação e compilação dos 6 projetos. |
| **M3.1.2** | [`M3.1.2_evidencia_ambiente.png`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.2_evidencia_ambiente.png) | Mosaico comprobatório com capturas de tela do canvas e desenho nos 4 ambientes aprovados. |
| **M3.1.3** | [`M3.1.3_formulario_toque_caneta.csv`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.3_formulario_toque_caneta.csv) | Formulário empírico preenchido com a auditoria das 10 ações por toque e caneta no iPad. |
| **M3.1.3** | [`M3.1.3_gravacao_toque.mp4`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.3_gravacao_toque.mp4) | Gravação de tela (8,4 MB) da execução das 10 ações por toque com o dedo no iPad. |
| **M3.1.3** | [`M3.1.3_gravacao_caneta.mp4`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.3_gravacao_caneta.mp4) | Gravação de tela (4,7 MB) da execução das 10 ações com a caneta stylus Goojodoq no iPad. |
| **M3.2.1** | [`M3.2.1_tempos_abertura.csv`](../../dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.1_tempos_abertura.csv) | Tabela com as 20 medições e 4 medianas do tempo de abertura no DevTools. |
| **M3.2.1** | `Q3.2-escalabilidade/traces_abertura/` | 20 arquivos JSON de perfil DevTools exportados com traces de renderização. |
| **M3.2.2** | [`M3.2.2_fps_edicao.csv`](../../dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.2_fps_edicao.csv) | Taxas de quadros medidas via Frame Rendering Stats sob as 4 escalas de cena. |
| **M3.2.3** | [`M3.2.3_tamanho_maximo_salvamento.csv`](../../dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.3_tamanho_maximo_salvamento.csv) | Tabela de conferência do teste de estresse de salvamento e exportação até 10.000 elementos. |
| **M3.3.1** | [`M3.3.1_log_operacoes_pacote.txt`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.1_log_operacoes_pacote.txt) | Log detalhado da execução de instalação, atualização e desinstalação via npm, yarn e pnpm. |
| **M3.3.1** | [`M3.3.1_resultados_pacote.csv`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.1_resultados_pacote.csv) | Tabela comparativa das 9 operações de pacote por gerenciador (cenário público e local). |
| **M3.3.2** | [`M3.3.2_log_reproducao_passos.txt`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.2_log_reproducao_passos.txt) | Registro textual da auditoria dos 7 passos documentados de compilação e execução local. |
| **M3.3.2** | [`M3.3.2_passos_ajustes.csv`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.2_passos_ajustes.csv) | Tabela dos 7 passos documentados com classificação (sem ajuste vs com ajuste) e justificativas. |
| **M3.3.3** | [`M3.3.3_verificacoes_docker.csv`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.3_verificacoes_docker.csv) | Tabela de conferência das 4 verificações de deploy, container e healthcheck. |
| **M3.4.1** | [`M3.4.1_catalogo_formatos.csv`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.1_catalogo_formatos.csv) | Catálogo formal dos formatos abertos com MIME types e especificações W3C/ECMA. |
| **M3.4.2** | [`M3.4.2_preservacao_formatos.csv`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.2_preservacao_formatos.csv) | Resumo das taxas de preservação de elementos por formato. |
| **M3.4.2** | [`M3.4.2_relatorio_preservacao.json`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.2_relatorio_preservacao.json) | Relatório técnico JSON elemento a elemento gerado por `compara_elementos.py`. |
| **M3.4.2** | [`M3.4.2_arquivos_reimportados.zip`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.2_arquivos_reimportados.zip) | Pacote ZIP contendo as 6 cenas (originais exportadas e reimportadas salvas). |
| **M3.4.3** | [`M3.4.3_campos_encontrados.json`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.3_campos_encontrados.json) | Lista das 52 propriedades extraídas da cena real. |
| **M3.4.3** | [`M3.4.3_conferencia_campos.csv`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.3_conferencia_campos.csv) | Auditoria campo a campo classificando cada propriedade como documentada ou omitida. |
| **M3.4.3** | [`M3.4.3_relatorio.txt`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.3_relatorio.txt) | Resumo textual com o percentual final e lista de campos pendentes. |

---

## 5. Registro de Esforço e Tempo de Execução

Conforme as diretrizes de rastreabilidade e gestão da qualidade, a tabela a seguir consolida o esforço real investido pela avaliadora ao longo do processo de medição empírica:

| Turno / Período | Horário Aprox. | Duração | Atividades Realizadas (Decisão & Execução) | Métricas / Entregas Associadas |
| :--- | :---: | :---: | :--- | :--- |
| **Manhã (10/11)** | 09:00 – 12:45 | **3h45** | • Análise e resolução de conflitos no PR #151 (adaptação do script PSM e dados brutos do GitHub).<br />• Alinhamento do plano de medição da Fase 04 (Issue #113 — G3 Flexibilidade).<br />• Leitura detalhada das instruções de avaliação, critérios de julgamento e faixas de pontuação.<br />• Decisão arquitetural de priorizar a execução via contêiner oficial Docker para garantir reprodutibilidade e ambiente limpo. | PR #151 (Merge main)<br />Setup inicial F4 |
| **Tarde (10/11)** | 14:30 – 16:30 | **2h00** | • Recepção e importação da imagem Docker do Excalidraw (`excalidraw-avaliacao`).<br />• Instanciação e verificação de integridade do contêiner na porta 3000:80.<br />• Criação da estrutura de pastas em `dados/fase-04/brutos/` e templates de coleta.<br />• Execução dos comandos CLI do Browserslist e auditoria das 4 etapas de implantação Docker. | **M3.1.1** (Browserslist)<br />**M3.3.3** (Docker) |
| **Noite / Madrugada (10-11/11)** | 21:00 – 00:20 | **3h20** | • Auditoria dos formatos abertos e testes de reimportação com conferência via `compara_elementos.py`.<br />• Extração e auditoria campo a campo do JSON Schema oficial (identificação da lacuna de documentação).<br />• Definição da Ação de Melhoria (F4-C5) para documentação formal do esquema do Excalidraw.<br />• Reorganização completa da pasta de dados brutos por questões GQM (`Q3.1` a `Q3.4`).<br />• Execução das medições de escalabilidade: 20 perfis de rastreamento no DevTools (tempo de abertura), testes de salvamento/exportação até 10.000 elementos e medição empírica de FPS com *Frame Rendering Stats*. | **M3.4.1** (Formatos)<br />**M3.4.2** (Preservação)<br />**M3.4.3** (Esquema)<br />**M3.2.1** (Abertura)<br />**M3.2.2** (FPS)<br />**M3.2.3** (Exportação) |
| **Manhã (11/11)** | 11:38 – 12:35 | **0h57** | • Compilação local dos pacotes do monorepo (`yarn build:packages`) e geração do tarball `@excalidraw/excalidraw` (31 MB).<br />• Auditoria da execução nativa do servidor Vite (1,09s de inicialização e HTTP 200).<br />• Identificação e diagnóstico do comando legado `docker-compose` gerando código 127 vs `docker compose`.<br />• Teste das 9 operações de pacote nos 3 gerenciadores (`npm`, `yarn`, `pnpm`) e análise de acoplamento de monorepo. | **M3.3.1** (Operações pacote)<br />**M3.3.2** (Passos documentados) |
| **Tarde (11/11 - Turno 1)** | 12:40 – 13:51 | **1h11** | • Criação e empacotamento dos subpacotes locais (common, math, element, fractional-indexing).<br />• Configuração dos 6 ambientes de integração cruzando Vite e Next.js com React 17, 18 e 19.<br />• Execução de builds, identificação dos erros estruturais de compilação Webpack (React 17) e prerender SSR (React 18).<br />• Automação de testes de renderização com Puppeteer-core, validação de desenho de retângulos e geração do mosaico comprobatório. | **M3.1.2** (Matriz de integração) |
| **Tarde (11/11 - Turno 2)** | 13:56 – 14:25 | **0h29** | • Inicialização da instância Docker oficial e disponibilização na rede local (`192.168.1.24:3000`).<br />• Conexão do iPad (A16) e execução manual roteirizada das 10 ações por toque e caneta stylus Goojodoq.<br />• Registro das observações de interação multimodal e preenchimento da planilha de dados brutos.<br />• Conclusão de 100% da coleta das métricas do objetivo G3. | **M3.1.3** (Toque e caneta)<br />Consolidação de G3 |
| **Total Acumulado** | — | **~11h42** | **12 de 12 métricas concluídas (100% do objetivo G3)**, 20 traces DevTools, 7 planilhas CSV, pacote ZIP de logs de build e relatórios técnicos versionados. | **G3 — 12 métricas** |

---

## 6. Próximos Passos da Avaliação

Com **100% das 12 métricas de G3 integralmente coletadas**, as próximas etapas para conclusão da [Issue #113](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/113) são:

1. **Elaboração do Relatório Consolidado:** redigir o documento formal `docs/fase-04/resultados-g3-flexibilidade.md`, consolidando as respostas às 4 questões GQM (Q3.1, Q3.2, Q3.3, Q3.4), a pontuação global do objetivo e o confronto das hipóteses.
2. **Atualização das Tabelas Consolidadas:** preencher as planilhas consolidadas em `dados/fase-04/consolidados/`.
3. **Abertura do Pull Request:** submeter as evidências e o relatório da Fase 04 para revisão dos pares e do professor.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| `1.0` | 10/11/2026 | Consolidação dos dados brutos, diagnósticos técnicos e insights preliminares das métricas M3.1.1, M3.3.3, M3.4.1, M3.4.2 e M3.4.3 de G3 | [Maria Eduarda](https://github.com/eduarda-ogomes) | |
| `1.1` | 11/11/2026 | Inclusão dos resultados e insights de Escalabilidade (M3.2.1, M3.2.2 e M3.2.3), organização das pastas por questão GQM e rastreabilidade dos traces | [Maria Eduarda](https://github.com/eduarda-ogomes) | |
| `1.2` | 11/11/2026 | Registro de esforço e detalhamento temporal por turnos (decisão, planejamento e execução empírica) | [Maria Eduarda](https://github.com/eduarda-ogomes) | |
| `1.3` | 11/11/2026 | Inclusão dos resultados e insights de Instalabilidade (M3.3.1 e M3.3.2) e atualização do esforço acumulado para 10 métricas | [Maria Eduarda](https://github.com/eduarda-ogomes) | |
| `1.4` | 11/11/2026 | Inclusão dos resultados e diagnóstico técnico de Adaptabilidade em Integração (M3.1.2), mosaico de evidências e esforço acumulado de 11 métricas (91,7%) | [Maria Eduarda](https://github.com/eduarda-ogomes) | |
| `1.5` | 11/11/2026 | Conclusão integral da coleta das 12 métricas de G3 (100%), inclusão dos resultados de M3.1.3 (iPad A16 + Goojodoq) e consolidação do esforço final (~11h42) | [Maria Eduarda](https://github.com/eduarda-ogomes) | |
