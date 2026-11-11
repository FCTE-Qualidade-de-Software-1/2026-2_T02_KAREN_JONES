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

Até o presente momento, **5 métricas de G3** foram integralmente coletadas, auditadas e confrontadas com as hipóteses e réguas da [Fase 02 (Pontuação e julgamento)](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3):

| Métrica | Nome da Métrica | Questão | Valor Medido | Nível na Régua | Hipótese GQM | Status da Hipótese |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **M3.1.1** | Cobertura de usuários pelos navegadores declarados | Q3.1 | **88,94%** | **Bom** (75 pts) | H3.1.1 ≥ 80% | **Confirmada** ✅ |
| **M3.3.3** | Implantação com Docker | Q3.3 | **100,0%** (4 de 4) | **Excelente** (100 pts) | H3.3.3 = 4 de 4 | **Confirmada** ✅ |
| **M3.4.1** | Formatos de exportação abertos disponíveis | Q3.4 | **3 formatos** | **Excelente** (100 pts) | H3.4.1 ≥ 3 | **Confirmada** ✅ |
| **M3.4.2** | Proporção de elementos preservados na reimportação | Q3.4 | **100,00%** | **Excelente** (100 pts) | H3.4.2 ≥ 95% | **Confirmada** ✅ |
| **M3.4.3** | Proporção dos campos do formato documentados | Q3.4 | **26,9%** (14 de 52) | **Crítico** (0 pts) | H3.4.3 < 60% | **Confirmada** ✅ |

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

---

## 4. Rastreabilidade com os Dados Brutos

Todos os dados brutos gerados durante estas coletas estão versionados e auditáveis na pasta `dados/fase-04/brutos/`:

| Métrica | Arquivo de Dado Bruto | Finalidade da Evidência |
| :---: | :--- | :--- |
| **M3.1.1** | [`M3.1.1_cobertura_browserslist.txt`](../../dados/fase-04/brutos/M3.1.1_cobertura_browserslist.txt) | Saída de terminal com a cobertura populacional e lista de navegadores. |
| **M3.3.3** | [`M3.3.3_verificacoes_docker.csv`](../../dados/fase-04/brutos/M3.3.3_verificacoes_docker.csv) | Tabela de conferência das 4 verificações de deploy, container e healthcheck. |
| **M3.4.1** | [`M3.4.1_catalogo_formatos.csv`](../../dados/fase-04/brutos/M3.4.1_catalogo_formatos.csv) | Catálogo formal dos formatos abertos com MIME types e especificações W3C/ECMA. |
| **M3.4.2** | [`M3.4.2_preservacao_formatos.csv`](../../dados/fase-04/brutos/M3.4.2_preservacao_formatos.csv) | Resumo das taxas de preservação de elementos por formato. |
| **M3.4.2** | [`M3.4.2_relatorio_preservacao.json`](../../dados/fase-04/brutos/M3.4.2_relatorio_preservacao.json) | Relatório técnico JSON elemento a elemento gerado por `scripts/compara_elementos.py`. |
| **M3.4.2** | [`M3.4.2_arquivos_reimportados.zip`](../../dados/fase-04/brutos/M3.4.2_arquivos_reimportados.zip) | Pacote ZIP contendo as 6 cenas (originais exportadas e reimportadas salvas). |
| **M3.4.3** | [`M3.4.3_campos_encontrados.json`](../../dados/fase-04/brutos/M3.4.3_campos_encontrados.json) | Lista das 52 propriedades extraídas da cena real. |
| **M3.4.3** | [`M3.4.3_conferencia_campos.csv`](../../dados/fase-04/brutos/M3.4.3_conferencia_campos.csv) | Auditoria campo a campo classificando cada propriedade como documentada ou omitida. |
| **M3.4.3** | [`M3.4.3_relatorio.txt`](../../dados/fase-04/brutos/M3.4.3_relatorio.txt) | Resumo textual com o percentual final e lista de campos pendentes. |

---

## 5. Próximos Passos da Coleta

Com as 5 primeiras métricas consolidadas, o plano de ação segue para as medições restantes:

1. **Escalabilidade (M3.2.1, M3.2.2 e M3.2.3):**
   - Medição do tempo de abertura (em segundos) e da taxa de quadros (FPS) sob estresse progressivo utilizando as cenas padronizadas de 100, 1.000, 5.000 e 10.000 elementos via Chrome DevTools.
   - Verificação do tamanho máximo de cena salva e exportada em até 30 segundos.
2. **Adaptabilidade em Dispositivo Móvel (M3.1.3):**
   - Execução do roteiro de 10 ações por toque e caneta stylus no iPad (A16) com gravação de tela contínua.
3. **Instalabilidade e Integração (M3.1.2, M3.3.1 e M3.3.2):**
   - Teste de empacotamento da biblioteca em projetos mínimos e verificação dos passos documentados de compilação local.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| `1.0` | 10/11/2026 | Consolidação dos dados brutos, diagnósticos técnicos e insights preliminares das métricas M3.1.1, M3.3.3, M3.4.1, M3.4.2 e M3.4.3 de G3 | [Maria Eduarda](https://github.com/eduarda-ogomes) | |
