---
sidebar_position: 1
title: "Insights e Descobertas: Flexibilidade (G3)"
description: Relatório analítico preliminar da coleta empírica das métricas do objetivo G3 (Flexibilidade) no Excalidraw, consolidando dados brutos, hipóteses confirmadas, diagnósticos técnicos e oportunidades de melhoria.
---

# Insights e Descobertas: Flexibilidade (G3)

## Introdução

Este documento consolida os resultados analíticos, diagnósticos empíricos e descobertas técnicas obtidas durante a execução da coleta de dados para o objetivo G3 (Flexibilidade), conduzida sobre a versão de referência do Excalidraw fixada no commit `e1b7aacb356a492aa1e0fc6eb57b8896124027f0`. O propósito deste artefato é apresentar uma visão analítica detalhada dos dados brutos, explorar o comportamento do software sob condições reais de uso e fornecer embasamento técnico para o planejamento das ações de melhoria da qualidade.

## Metodologia

A coleta empírica foi realizada segundo os procedimentos experimentais e de instrumentação delineados na Fase 03, estruturados sobre as doze métricas do modelo GQM de Flexibilidade. Foram aplicados testes automatizados de compilação e empacotamento, perfis de renderização e consumo temporal via Chrome DevTools, execução conteinerizada em ambiente isolado Docker e avaliação presencial de usabilidade tátil em tablet com caneta stylus. As fraquezas identificadas foram categorizadas tecnicamente para direcionar intervenções corretivas no código e na documentação do projeto.

---

## 1. Contexto e Ambiente de Execução

As medições foram conduzidas estritamente sob as condições de contorno fixadas na [Fase 03 (Recursos e ambiente)](../fase-03/recursos-ambiente.md):

<p className="tabela-titulo">Tabela 1: Parâmetros de configuração do ambiente de avaliação</p>

| Parâmetro | Configuração Efetiva Registrada |
| :--- | :--- |
| **Avaliadora Responsável** | Maria Eduarda ([@eduarda-ogomes](https://github.com/eduarda-ogomes)) |
| **Data da Coleta** | 10 a 11 de Novembro de 2026 |
| **Software Avaliado** | Excalidraw (commit exato `e1b7aacb356a492aa1e0fc6eb57b8896124027f0`) |
| **Sistema Operacional** | Zorin OS 18.1 (Kernel Linux x86_64, base Ubuntu 24.04 LTS) |
| **Processador** | AMD Ryzen 7 5700U with Radeon Graphics |
| **Memória RAM** | 10 GB utilizáveis (16 GB físicos instalados) |
| **Ambiente de Execução** | Contêiner Docker oficial (base Nginx 1.30.2) em `http://localhost:3000` |
| **Repositório de Dados Brutos** | `dados/fase-04/brutos/` |

<p className="tabela-fonte">Fonte: Elaborado pela autora, 2026.</p>

---

## 2. Painel Consolidado das Métricas Coletadas

Todas as 12 métricas de G3 (100% do objetivo de Flexibilidade) foram integralmente coletadas, auditadas e confrontadas com as hipóteses e réguas da [Fase 02 (Pontuação e julgamento)](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3):

<p className="tabela-titulo">Tabela 2: Painel consolidado das métricas coletadas de flexibilidade (G3)</p>

| Métrica | Nome da Métrica | Questão | Valor Medido | Nível na Régua | Hipótese GQM | Status da Hipótese |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **M3.1.1** | Cobertura de usuários pelos navegadores declarados | Q3.1 | **88,94%** | **Bom** (`+`, 4,00 pts) | H3.1.1 ≥ 80% | **Confirmada** |
| **M3.1.2** | Proporção de ambientes de integração com sucesso | Q3.1 | **66,7%** (4 de 6) | **Regular** (`o`, 3,00 pts) | H3.1.2 = 6 de 6 | **Refutada** |
| **M3.1.3** | Proporção de ações de edição por toque e caneta | Q3.1 | **100,0%** (10 de 10) | **Excelente** (`++`, 5,00 pts) | H3.1.3 = 10 de 10 | **Confirmada** |
| **M3.2.1** | Tempo de abertura por tamanho de cena | Q3.2 | **0,11 s** (1.000 elem) | **Bom** (`+`, 4,50 pts) | H3.2.1 ≤ 1,0 s | **Confirmada** |
| **M3.2.2** | Taxa de quadros durante a edição por tamanho de cena | Q3.2 | **52 FPS** (1.000 elem) | **Regular** (`o`, 3,25 pts) | H3.2.2 ≥ 48 FPS | **Confirmada** |
| **M3.2.3** | Tamanho máximo de cena salva e exportada | Q3.2 | **10.000 elem** | **Excelente** (`++`, 5,00 pts) | H3.2.3 ≥ 5.000 elem | **Confirmada** |
| **M3.3.1** | Proporção de operações de pacote bem-sucedidas | Q3.3 | **33,3%** (3 de 9) | **Ruim** (`-`, 2,00 pts) | H3.3.1 = 9 de 9 | **Refutada** |
| **M3.3.2** | Proporção de passos documentados reproduzidos | Q3.3 | **85,7%** (6 de 7) | **Bom** (`+`, 4,00 pts) | H3.3.2 ≥ 95% | **Refutada** |
| **M3.3.3** | Implantação com Docker | Q3.3 | **100,0%** (4 de 4) | **Excelente** (`++`, 5,00 pts) | H3.3.3 = 4 de 4 | **Confirmada** |
| **M3.4.1** | Formatos de exportação abertos disponíveis | Q3.4 | **3 formatos** | **Bom** (`+`, 4,00 pts) | H3.4.1 ≥ 3 | **Confirmada** |
| **M3.4.2** | Proporção de elementos preservados na reimportação | Q3.4 | **100,00%** | **Excelente** (`++`, 5,00 pts) | H3.4.2 ≥ 95% | **Confirmada** |
| **M3.4.3** | Proporção dos campos do formato documentados | Q3.4 | **26,9%** (14 de 52) | **Ruim** (`-`, 2,00 pts) | H3.4.3 < 60% | **Confirmada** |

<p className="tabela-fonte">Fonte: Elaborado pela autora, 2026.</p>

---

## 3. Principais Insights e Descobertas Técnicas

### 3.1 Contraste entre a robustez do código e a fragilidade da documentação (Substituibilidade: Q3.4)

A análise cruzada entre as métricas **M3.4.2** e **M3.4.3** revelou uma discrepância técnica profunda no ecossistema do Excalidraw:

1. **Excelência no Motor de Serialização (M3.4.2 = 100%):**
   - O teste prático de ciclo de vida (exportação da `cena_referencia.excalidraw` contendo todos os 10 tipos de elementos gráficos da Fase 02 para `.excalidraw`, `.png` e `.svg`, seguido de reabertura e comparação matemática via `scripts/compara_elementos.py`) resultou em **preservação perfeita de 100% dos elementos**.
   - O mecanismo de embutir metadados da cena em imagens PNG e vetores SVG provou ser altamente confiável. Tipos, coordenadas espaciais (`x`, `y`, `width`, `height`), estilos visuais (`strokeColor`, `backgroundColor`, `fillStyle`, `strokeWidth`) e textos foram preservados sem desvio métrico e sem perda de informação.
2. **Defasagem Crítica na Documentação Externa (M3.4.3 = 26,9%):**
   - Em contraste direto com a fidelidade do software, a especificação técnica pública oferecida aos desenvolvedores terceiros em `dev-docs/docs/codebase/json-schema.mdx` revelou-se superficial.
   - De **52 propriedades reais** gravadas pelo editor no arquivo de desenho, apenas **14 propriedades** estão descritas no documento.
   - Os mantenedores do projeto explicitamente omitiram as propriedades dos elementos gráficos no exemplo da documentação com o comentário de código `/* ...other element properties */`.
   - Propriedades vitais para a renderização do desenho, tais como `strokeColor`, `roundness`, `roughness`, `fontSize`, `opacity`, `frameId`, `boundElements` e `isDeleted`, não constam na documentação oficial, forçando desenvolvedores externos a inspecionar o código-fonte em TypeScript para compreender o formato.
   - Além disso, a auditoria constatou a ausência total de um arquivo formal JSON Schema (`schema.json`) validável por máquina no repositório.

---

### 3.2 Oportunidade central para a ação de melhoria (Substituibilidade: M3.4.3)

A comprovação empírica do nível Ruim em M3.4.3 oferece à equipe justificativa técnica direta para a ação de melhoria planejada nas [Issues #118](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/118) e [#119](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/119):

* **Problema Diagnosticado:** Violação do princípio de transparência de formato aberto em conformidade com o requisito `RQ-FLEX-12`. Usuários e ferramentas externas enfrentam barreiras de interoperabilidade devido a 38 campos não documentados (apenas 26,9% de cobertura).
* **Proposta de Melhoria:**
  1. Redigir a complementação da documentação técnica dos elementos em `dev-docs/docs/codebase/json-schema.mdx`, detalhando os 38 campos identificados pela auditoria.
  2. Implementar um arquivo formal `packages/excalidraw/schema/excalidraw.schema.json` contendo o JSON Schema canônico do formato `.excalidraw`.
* **Impacto Mensurável:** A implementação desta ação de melhoria elevará a métrica M3.4.3 de **26,9% (Nível Ruim)** para **100,0% (Nível Excelente)**, gerando impacto positivo direto no indicador de Substituibilidade de G3.

---

### 3.3 Ampla cobertura populacional sem inflação de dependências (Adaptabilidade: Q3.1)

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
* O descarte intencional de navegadores obsoletos (IE 11, Safari legado, Opera Mini) evita o aumento desnecessário do tamanho do pacote com polyfills legados, enquanto assegura funcionamento para a quase totalidade dos navegadores modernos móveis e desktop.

---

### 3.4 Alta reprodutibilidade na esteira Docker (Instalabilidade: Q3.3)

A execução da métrica **M3.3.3** comprovou a facilidade de implantação do software em infraestrutura isolada:

* O contêiner de produção construído a partir do `Dockerfile` oficial executou sem ajustes, subiu com sucesso na porta `3000:80` e atingiu o estado de integridade aprovada na checagem nativa em menos de 15 segundos.
* A entrega através de servidor Nginx interno garante independência completa de configurações do ambiente hospedeiro, validando o requisito `RQ-FLEX-09`.

---

### 3.5 Desempenho e degradação suave sob estresse de escala (Escalabilidade: Q3.2)

A medição empírica das três métricas da questão **Q3.2** revelou o comportamento do motor de renderização do Excalidraw sob estresse progressivo de volume de dados:

1. **Tempo de Abertura (M3.2.1):**
   - O tempo de carga da cena com 1.000 elementos atingiu mediana de **0,11 s**, confirmando com ampla folga a hipótese **H3.2.1 ≤ 1,0 s** (nível Bom, 4,50 pontos).
   - Sob 10.000 elementos (um arquivo de 5,2 MB), o tempo de estabilização completa foi de apenas **1,52 s**, mantendo-se na faixa de conforto cognitivo humano definida por Nielsen e pelo modelo RAIL (inferior a 2 segundos).
2. **Taxa de Quadros em Edição Contínua (M3.2.2):**
   - Com 100 elementos, o editor opera no limite do monitor a **60 FPS** (100% de fluidez).
   - Na cena de 1.000 elementos, a taxa oscila entre 46 e 58 FPS, obtendo mediana de **52 FPS** e confirmando a hipótese **H3.2.2 ≥ 48 FPS** (nível Regular, 3,25 pontos).
   - Sob 5.000 elementos (mediana de **20 FPS**) e 10.000 elementos (**12 FPS**), a aplicação apresenta degradação suave: o redesenho sofre redução de taxa de quadros, mas não ocorre congelamento da aba, travamento do processo ou fechamento inesperado do navegador.
3. **Persistência e Exportação sob Carga Máxima (M3.2.3):**
   - Todas as 4 escalas de cena completaram com sucesso as três operações (salvamento no disco em `.excalidraw` em 0,80 s, exportação em PNG em 1,20 s e exportação em SVG em 0,70 s), muito abaixo do teto de tolerância de 30 segundos.
   - O tamanho máximo suportado atingiu **10.000 elementos**, confirmando a hipótese **H3.2.3 ≥ 5.000 elementos** e alcançando a pontuação máxima de **5,00 pontos (Excelente)**.

---

### 3.6 Auditoria de instalabilidade e acoplamento em monorepo (Instalabilidade: Q3.3)

A execução das métricas **M3.3.1** e **M3.3.2** complementou os dados da esteira Docker (M3.3.3), finalizando a avaliação de toda a questão **Q3.3**:

1. **Reprodutibilidade dos Passos Documentados (M3.3.2):**
   - Na via nativa (Node.js e Yarn), a clonagem, instalação de dependências e inicialização do servidor de desenvolvimento ocorreram sem falhas. O comando `yarn` instalou todas as dependências e configurou os githooks do Husky com código 0 em 346s, e `yarn start` inicializou o Vite em apenas **1,09 s** respondendo com código HTTP 200.
   - Na via com Docker Compose, detectou-se uma incompatibilidade documental: o guia `development.mdx` documenta a sintaxe legada `docker-compose up --build -d` com hífen. Em distribuições modernas com Docker Engine v2 (como o Zorin OS avaliado), o binário Python standalone não existe nativamente, gerando código de erro 127 (command not found) e exigindo ajuste corretivo para o plugin moderno `docker compose up`.
   - Com 6 de 7 passos bem-sucedidos sem ajuste (**85,7%**), a métrica atinge o **Nível Bom (4,00 pontos)**, mas refuta a hipótese H3.3.2 (≥ 95%) devido à defasagem da instrução de compose.
2. **Ciclo de Vida de Pacotes em Gerenciadores (M3.3.1):**
   - No teste comparativo com os 3 gerenciadores (`npm`, `yarn` e `pnpm`) a partir do tarball local gerado no monorepo (`@excalidraw/excalidraw-0.18.0.tgz`), a instalação inicial foi concluída nos três gerenciadores.
   - No entanto, as operações de upgrade falharam devido a dependências internas de workspace não resolvidas (`@excalidraw/common` com código `ETARGET`), impedindo também a desinstalação subsequente de forma limpa.
   - Com 3 de 9 operações concluídas com êxito (**33,3%**), a métrica atinge o nível **Ruim (2,00 pontos)** e **refuta a hipótese H3.3.1**. Esse comportamento evidencia forte acoplamento entre os subpacotes do monorepo, que demandam publicação sincronizada no registro para consumo externo independente.
   - Adicionalmente, a execução de `require('@excalidraw/excalidraw')` direto no runtime Node.js confirma dependência estrita do DOM do navegador (`ReferenceError: document is not defined`), exigindo desativação de renderização no servidor (`ssr: false`) ao ser integrada em frameworks modernos como Next.js.

---

### 3.7 Desafios de compatibilidade em frameworks SSR e transição para React 19 (Adaptabilidade: Q3.1)

A avaliação da métrica **M3.1.2** sobre as **6 combinações** de ecossistema (React 17, 18 e 19 cruzados com Vite e Next.js) revelou um contraste marcante entre empacotadores tradicionais e frameworks modernos com renderização no servidor:

1. **Robustez Plena sob Empacotador Vite (3 de 3 Sucessos):**
   - No Vite 5.4.11, as 3 versões de React (**React 17.0.2**, **React 18.2.0** e **React 19.0.0**) compilaram com código de saída 0 em tempo médio de cerca de 12 segundos.
   - Em todas as 3 variantes, o servidor de pré-visualização serviu a aplicação com HTTP 200, o canvas carregou sem exceções não tratadas e foi possível desenhar formas geométricas (retângulos com painel de propriedades) com validação automatizada via Puppeteer-core.
2. **Fragilidade Estrutural em Frameworks SSR (Next.js, 1 de 3 Sucessos):**
   - **React 17 + Next.js 12:** Falha crítica na compilação do Webpack (`next build`). Embora o `package.json` do `@excalidraw/excalidraw` declare formalmente compatibilidade com React 17, 18 e 19, os arquivos JavaScript transcompilados do pacote realizam importações nomeadas dos hooks `useId` e `useDeferredValue` diretamente de `react`. Como esses hooks só foram criados no React 18, o Webpack acusa erro de importação e encerra a compilação com código de erro 1.
   - **React 18 + Next.js 14:** Falha durante a etapa de pré-renderização estática. A versão do Excalidraw no commit avaliado (`e1b7aac`) foi migrada internamente para compilar seu JSX sob a especificação do React 19. Quando empacotado junto ao React 18 no Next.js, o motor de SSR do React 18 rejeita os elementos com o erro `Minified React error #31` e acusa erro de referência na invocação de logs estáticos.
   - **React 19 + Next.js 14:** Sucesso total comprovado no exemplo oficial do monorepo (`examples/with-nextjs`). O build completou em 65s via importação dinâmica com desativação de SSR (`dynamic(..., { ssr: false })`) e injeção de fontes estáticas na pasta pública, permitindo renderização perfeita do canvas e desenho de formas geométricas.
3. **Julgamento e Hipótese:**
   - Com **4 de 6 combinações bem-sucedidas (66,7%)**, a métrica atinge o nível **Regular (3,00 pontos)**.
   - A hipótese **H3.1.2 (= 6 de 6 combinações) é refutada**, demonstrando que integradores terceiros enfrentam barreiras e precisam aplicar adaptações consideráveis caso operem fora do ecossistema React 19 com Vite.

---

### 3.8 Fluidez e fidelidade na interação por toque e stylus em dispositivos móveis (Adaptabilidade: Q3.1)

A execução da métrica **M3.1.3** encerrou a coleta de dados de Adaptabilidade (Q3.1) e de todo o objetivo G3, através de testes empíricos controlados conduzidos diretamente no hardware físico de referência (**Apple iPad A16**) conectado via rede sem fio ao contêiner oficial do Excalidraw (`http://192.168.1.24:3000`), avaliando a entrada direta com o dedo e com a caneta capacitiva stylus Goojodoq:

1. **Eficiência Multimodal e Desempenho com Dedo (10 de 10 Ações Aprovadas, 100%):**
   - O canvas respondeu de forma fluida a toques diretos para criação de formas, traçado à mão livre, seleção, arraste e redimensionamento de elementos.
   - O gesto de pinça para zoom demonstrou resposta instantânea de ampliação e redução de escala sem travamentos ou quebras visuais.
   - **Comportamento de usabilidade no deslocamento de tela:** Foi identificado um comportamento ergonômico intencional do Excalidraw. Quando a ferramenta de seleção está ativa, o arraste com um único dedo é reservado para seleção por caixa elástica, exigindo o toque simultâneo de dois dedos para ativar o deslocamento. Ao ativar a ferramenta Mão, o deslocamento da tela ocorre diretamente com apenas um dedo, simplificando a navegação.
2. **Precisão com Caneta Stylus Goojodoq (10 de 10 Ações Aprovadas, 100%):**
   - A caneta stylus apresentou alta precisão na ponta ativa, traçando desenhos livres e posicionando alças de redimensionamento sem latência perceptível.
   - A interação híbrida (desenhar com a ponta da caneta enquanto realiza navegação na tela com os dedos) operou de forma transparente, permitindo alternância instantânea entre escrita e gestos de navegação.
3. **Julgamento e Hipótese:**
   - Com **100,0% de sucesso** em ambas as vias de entrada (dedo e caneta), a métrica atinge o nível **Excelente (5,00 pontos)**.
   - A hipótese **H3.1.3 (= 10 de 10 ações) é confirmada**, comprovando a maturidade ergonômica da interface do Excalidraw para dispositivos móveis e tablets.

---

## 4. Rastreabilidade com os Dados Brutos

Todos os dados brutos gerados durante estas coletas estão versionados e auditáveis na pasta `dados/fase-04/brutos/`:

<p className="tabela-titulo">Tabela 3: Mapeamento de rastreabilidade com os dados brutos versionados</p>

| Métrica | Arquivo de Dado Bruto | Finalidade da Evidência |
| :---: | :--- | :--- |
| **M3.1.1** | [`M3.1.1_cobertura_browserslist.txt`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.1_cobertura_browserslist.txt) | Saída de terminal com a cobertura populacional e lista de navegadores. |
| **M3.1.2** | [`M3.1.2_matriz_integracao.csv`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.2_matriz_integracao.csv) | Tabela detalhada dos 6 ambientes com status de build, runtime, desenho e diagnóstico. |
| **M3.1.2** | [`M3.1.2_build_logs.zip`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.2_build_logs.zip) | Arquivo compactado com os logs brutos completos de instalação e compilação dos 6 projetos. |
| **M3.1.2** | [`M3.1.2_evidencia_ambiente.png`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.2_evidencia_ambiente.png) | Mosaico comprobatório com capturas de tela do canvas e desenho nos 4 ambientes aprovados. |
| **M3.1.3** | [`M3.1.3_formulario_toque_caneta.csv`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.3_formulario_toque_caneta.csv) | Formulário empírico preenchido com a auditoria das 10 ações por toque e caneta no iPad. |
| **M3.1.3** | [`M3.1.3_gravacao_toque.mp4`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.3_gravacao_toque.mp4) | Gravação de tela da execução das 10 ações por toque com o dedo no iPad. |
| **M3.1.3** | [`M3.1.3_gravacao_caneta.mp4`](../../dados/fase-04/brutos/Q3.1-adaptabilidade/M3.1.3_gravacao_caneta.mp4) | Gravação de tela da execução das 10 ações com a caneta stylus Goojodoq no iPad. |
| **M3.2.1** | [`M3.2.1_tempos_abertura.csv`](../../dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.1_tempos_abertura.csv) | Tabela com as 20 medições e 4 medianas do tempo de abertura no DevTools. |
| **M3.2.1** | `Q3.2-escalabilidade/traces_abertura/` | 20 arquivos JSON de perfil DevTools exportados com traces de renderização. |
| **M3.2.2** | [`M3.2.2_fps_edicao.csv`](../../dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.2_fps_edicao.csv) | Taxas de quadros medidas via Frame Rendering Stats sob as 4 escalas de cena. |
| **M3.2.3** | [`M3.2.3_tamanho_maximo_salvamento.csv`](../../dados/fase-04/brutos/Q3.2-escalabilidade/M3.2.3_tamanho_maximo_salvamento.csv) | Tabela de conferência do teste de estresse de salvamento e exportação até 10.000 elementos. |
| **M3.3.1** | [`M3.3.1_log_operacoes_pacote.txt`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.1_log_operacoes_pacote.txt) | Log detalhado da execução de operações de pacote via npm, yarn e pnpm. |
| **M3.3.1** | [`M3.3.1_resultados_pacote.csv`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.1_resultados_pacote.csv) | Tabela comparativa das 9 operações de pacote por gerenciador. |
| **M3.3.2** | [`M3.3.2_log_reproducao_passos.txt`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.2_log_reproducao_passos.txt) | Registro textual da auditoria dos 7 passos documentados de compilação e execução local. |
| **M3.3.2** | [`M3.3.2_passos_ajustes.csv`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.2_passos_ajustes.csv) | Tabela dos 7 passos documentados com classificação e justificativas. |
| **M3.3.3** | [`M3.3.3_verificacoes_docker.csv`](../../dados/fase-04/brutos/Q3.3-instalabilidade/M3.3.3_verificacoes_docker.csv) | Tabela de conferência das 4 verificações de deploy, container e healthcheck. |
| **M3.4.1** | [`M3.4.1_catalogo_formatos.csv`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.1_catalogo_formatos.csv) | Catálogo formal dos formatos abertos com MIME types e especificações W3C e ECMA. |
| **M3.4.2** | [`M3.4.2_preservacao_formatos.csv`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.2_preservacao_formatos.csv) | Resumo das taxas de preservação de elementos por formato. |
| **M3.4.2** | [`M3.4.2_relatorio_preservacao.json`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.2_relatorio_preservacao.json) | Relatório técnico JSON elemento a elemento gerado por `compara_elementos.py`. |
| **M3.4.2** | [`M3.4.2_arquivos_reimportados.zip`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.2_arquivos_reimportados.zip) | Pacote ZIP contendo as cenas originais exportadas e reimportadas salvas. |
| **M3.4.3** | [`M3.4.3_campos_encontrados.json`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.3_campos_encontrados.json) | Lista das 52 propriedades extraídas da cena real. |
| **M3.4.3** | [`M3.4.3_conferencia_campos.csv`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.3_conferencia_campos.csv) | Auditoria campo a campo classificando cada propriedade como documentada ou omitida. |
| **M3.4.3** | [`M3.4.3_relatorio.txt`](../../dados/fase-04/brutos/Q3.4-substituibilidade/M3.4.3_relatorio.txt) | Resumo textual com o percentual final e lista de campos pendentes. |

<p className="tabela-fonte">Fonte: Elaborado pela autora, 2026.</p>

---

## 5. Registro de Esforço e Tempo de Execução

Conforme as diretrizes de rastreabilidade e gestão da qualidade, a tabela a seguir consolida o esforço real investido pela avaliadora ao longo do processo de medição empírica:

<p className="tabela-titulo">Tabela 4: Distribuição do esforço real investido por turnos de trabalho</p>

| Turno e Período | Horário Aprox. | Duração | Atividades Realizadas (Decisão e Execução) | Métricas e Entregas Associadas |
| :--- | :---: | :---: | :--- | :--- |
| **Manhã (10/11)** | 09:00 às 12:45 | **3h45** | Resolução de conflitos no PR #151, alinhamento do plano de medição da Fase 04 (Issue #113), leitura detalhada das instruções de avaliação e decisão de priorizar a execução via contêiner oficial Docker para garantir reprodutibilidade. | PR #151 e setup inicial da Fase 04 |
| **Tarde (10/11)** | 14:30 às 16:30 | **2h00** | Recepção e importação da imagem Docker do Excalidraw, instanciação e verificação de integridade do contêiner na porta 3000:80, estruturação de pastas em dados brutos e execução dos comandos CLI do Browserslist e verificações Docker. | **M3.1.1** (Browserslist) e **M3.3.3** (Docker) |
| **Noite e Madrugada (10-11/11)** | 21:00 às 00:20 | **3h20** | Auditoria dos formatos abertos e testes de reimportação com script comparador, auditoria campo a campo do esquema de dados, planejamento da ação de melhoria de documentação, testes de escalabilidade no DevTools (20 traces), medição de FPS e teste de estresse até 10.000 elementos. | **M3.4.1**, **M3.4.2**, **M3.4.3**, **M3.2.1**, **M3.2.2** e **M3.2.3** |
| **Manhã (11/11)** | 11:38 às 12:35 | **0h57** | Compilação local dos pacotes do monorepo, teste das operações de pacote a partir do tarball local nos 3 gerenciadores, diagnóstico de resolução de workspace, execução nativa do servidor Vite e diagnóstico do comando legado docker-compose. | **M3.3.1** (Pacote) e **M3.3.2** (Passos documentados) |
| **Tarde (11/11, Turno 1)** | 12:40 às 13:51 | **1h11** | Empacotamento de subpacotes locais, criação e configuração dos 6 ambientes de integração cruzando Vite e Next.js com React 17, 18 e 19, diagnóstico de falhas de compilação Webpack e pré-renderização SSR, e automação de testes com Puppeteer gerando mosaico comprobatório. | **M3.1.2** (Matriz de integração) |
| **Tarde (11/11, Turno 2)** | 13:56 às 14:25 | **0h29** | Configuração da rede local Docker, conexão do iPad (A16) e execução manual roteirizada das 10 ações por toque e caneta stylus Goojodoq, preenchimento da planilha de auditoria e encerramento da coleta das 12 métricas de G3. | **M3.1.3** (Toque e caneta) e Consolidação de G3 |
| **Total Acumulado** | Total | **11h42** | Conclusão de 100% das 12 métricas do objetivo G3, 20 traces DevTools, 7 planilhas CSV, pacote ZIP de logs de build e relatórios técnicos versionados. | Conclusão do Objetivo G3 |

<p className="tabela-fonte">Fonte: Elaborado pela autora, 2026.</p>

---

## 6. Próximos Passos da Avaliação

Com **100% das doze métricas de G3 integralmente coletadas**, as próximas etapas para conclusão da [Issue #113](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/issues/113) são:

1. **Elaboração do Relatório Consolidado:** redigir o documento formal `docs/fase-04/resultados-g3-flexibilidade.md`, consolidando as respostas às 4 questões GQM (Q3.1, Q3.2, Q3.3, Q3.4), a pontuação global do objetivo e o confronto das hipóteses.
2. **Atualização das Tabelas Consolidadas:** preencher as planilhas consolidadas em `dados/fase-04/consolidados/`.
3. **Abertura do Pull Request:** submeter as evidências e o relatório da Fase 04 para revisão dos pares e do professor.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| `1.0` | 10/11/2026 | Consolidação dos dados brutos, diagnósticos técnicos e insights preliminares das métricas M3.1.1, M3.3.3, M3.4.1, M3.4.2 e M3.4.3 de G3. | [Maria Eduarda](https://github.com/eduarda-ogomes) | |
| `1.1` | 11/11/2026 | Inclusão dos resultados e insights de Escalabilidade (M3.2.1, M3.2.2 e M3.2.3), organização das pastas por questão GQM e rastreabilidade dos traces. | [Maria Eduarda](https://github.com/eduarda-ogomes) | |
| `1.2` | 11/11/2026 | Registro de esforço e detalhamento temporal por turnos de decisão, planejamento e execução empírica. | [Maria Eduarda](https://github.com/eduarda-ogomes) | |
| `1.3` | 11/11/2026 | Inclusão dos resultados e insights de Instalabilidade (M3.3.1 e M3.3.2) e atualização do esforço acumulado para 10 métricas. | [Maria Eduarda](https://github.com/eduarda-ogomes) | |
| `1.4` | 11/11/2026 | Inclusão dos resultados e diagnóstico técnico de Adaptabilidade em Integração (M3.1.2), mosaico de evidências e esforço acumulado de 11 métricas. | [Maria Eduarda](https://github.com/eduarda-ogomes) | |
| `1.5` | 11/11/2026 | Conclusão integral da coleta das 12 métricas de G3, inclusão dos resultados de M3.1.3 (iPad A16 e Goojodoq) e consolidação do esforço final de 11h42. | [Maria Eduarda](https://github.com/eduarda-ogomes) | |
