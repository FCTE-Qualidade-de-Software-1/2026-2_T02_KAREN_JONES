# Massa de Dados para Avaliação (Fase 03)

Este diretório contém a massa de dados padronizada necessária para a execução das medições dos objetivos de qualidade **G2 (Confiabilidade)** e **G3 (Flexibilidade)** durante a Fase 04, atendendo aos critérios de avaliação **F3-C2** (especificação e justificativa da massa de dados) e **F3-C8** (consistência entre as Fases 02 e 03).

Todos os artefatos aqui armazenados são gerados de forma reproduzível e determinística pelo script versionado [`scripts/gerar_massa_dados.py`](../../scripts/gerar_massa_dados.py), permitindo que qualquer avaliador recrie integralmente o ambiente de dados de teste.

---

## 1. Estrutura do Diretório

```text
dados/fase-03/massa-de-dados/
├── README.md                      # Esta documentação técnica
├── cena_referencia.excalidraw     # Cena canônica com os 10 tipos essenciais de elementos
├── cena_100.excalidraw            # Cena de escala com 100 elementos (40/20/20/20)
├── cena_1000.excalidraw           # Cena de escala com 1.000 elementos (40/20/20/20)
├── cena_5000.excalidraw           # Cena de escala com 5.000 elementos (40/20/20/20)
├── cena_10000.excalidraw          # Cena de escala com 10.000 elementos (40/20/20/20)
└── invalidos/                     # Conjunto de 9 arquivos inválidos para M2.3.1
    ├── invalido_01_vazio.excalidraw
    ├── invalido_02_json_malformado.excalidraw
    ├── invalido_03_sem_campo_type.excalidraw
    ├── invalido_04_type_desconhecido.excalidraw
    ├── invalido_05_elementos_sem_campos_obrigatorios.excalidraw
    ├── invalido_06_coordenadas_nao_numericas.excalidraw
    ├── invalido_07_binario_renomeado.excalidraw
    ├── invalido_08_png_sem_desenho.png
    └── invalido_09_truncado_no_meio.excalidraw
```

---

## 2. Cena de Referência (`cena_referencia.excalidraw`)

A cena de referência consolida em um único arquivo todos os tipos primitivos de elementos manipulados pelo Excalidraw, servindo de base para os testes de restauração de sessão ([M2.4.1](../../docs/fase-02/gqm-confiabilidade.md#m241--proporção-de-cenários-de-fechamento-com-restauração-do-desenho)), compatibilidade retroativa e abertura sem perda ([M2.4.2](../../docs/fase-02/gqm-confiabilidade.md#m242--proporção-de-arquivos-reabertos-sem-perda)), fidelidade de exportação e reimportação ([M3.4.2](../../docs/fase-02/gqm-flexibilidade.md#m342--proporção-de-elementos-preservados-na-exportação-e-reimportação)) e cobertura documental do formato ([M3.4.3](../../docs/fase-02/gqm-flexibilidade.md#m343--proporção-dos-campos-do-formato-excalidraw-documentados)).

### Elementos Contidos na Cena

| # | Identificador (`id`) | Tipo (`type`) | Descrição do Elemento | Características Específicas |
| :-: | :--- | :--- | :--- | :--- |
| 1 | `ref_frame_01` | `frame` | Moldura estrutural | Delimita a prancheta de avaliação (`1100 × 680 px`), traço tracejado (`#868e96`). Agrupa os demais elementos via `frameId`. |
| 2 | `ref_text_solto_01` | `text` | Texto independente | Rótulo de título posicionado no topo (`fontSize: 20`, alinhamento à esquerda, `containerId: null`). |
| 3 | `ref_rect_01` | `rectangle` | Retângulo arredondado | Borda azul (`#1971c2`), preenchimento sólido (`#d0ebff`), cantos arredondados (`roundness: type 3`). Contém vínculo em `boundElements`. |
| 4 | `ref_bound_text_01` | `text` | Texto contido em forma (*bound text*) | Texto interno ao retângulo (`containerId: "ref_rect_01"`), centralizado vertical e horizontalmente. |
| 5 | `ref_ellipse_01` | `ellipse` | Elipse | Forma elíptica verde (`#2b8a3e`), preenchimento sólido (`#d3f9d8`), dimensões `180 × 110 px`. |
| 6 | `ref_diamond_01` | `diamond` | Losango de decisão | Vértices simétricos amarelos/laranja (`#e67700`), preenchimento `#fff3bf`, dimensões `160 × 120 px`. |
| 7 | `ref_arrow_01` | `arrow` | Seta direcional | Vetor linear horizontal de 180 px (`#c92a2a`) com ponta triangular (`endArrowhead: "arrow"`). |
| 8 | `ref_line_01` | `line` | Linha poligonal | Linha com três pontos de ancoragem `[0,0]`, `[120,40]`, `[240,0]`, estilo tracejado cinza (`#495057`). |
| 9 | `ref_freedraw_01` | `freedraw` | Traço livre à mão (*pencil*) | Curva com 5 coordenadas vetoriais, espessura e sensibilidade à pressão simulada (`pressures` e `simulatePressure: true`). |
| 10 | `ref_image_01` | `image` | Imagem raster incorporada | Elemento de imagem vinculado à entrada `file_ref_logo_fcte` registrada no dicionário de arquivos raiz `files` (PNG 1×1 em base64). |

---

## 3. Cenas de Escala (`cena_100`, `cena_1000`, `cena_5000`, `cena_10000.excalidraw`)

As cenas de escala fornecem cargas de trabalho crescentes e padronizadas para avaliar o comportamento do motor de renderização do Excalidraw sob estresse nas métricas de escalabilidade:
- [M3.2.1](../../docs/fase-02/gqm-flexibilidade.md#m321--tempo-de-abertura-por-tamanho-de-cena): Tempo de abertura por tamanho de cena;
- [M3.2.2](../../docs/fase-02/gqm-flexibilidade.md#m322--taxa-de-quadros-durante-a-edição-por-tamanho-de-cena): Taxa de quadros (FPS) durante manipulação em tela;
- [M3.2.3](../../docs/fase-02/gqm-flexibilidade.md#m323--tamanho-máximo-de-cena-salva-e-exportada): Limite máximo de elementos suportados para persistência e exportação.

### Distribuição e Proporção Fixa dos Elementos

Todas as cenas de escala seguem rigorosamente a proporção canônica fixada na Fase 02: **40% de retângulos**, **20% de elipses**, **20% de setas** e **20% de textos**.

| Arquivo | Total de Elementos | Retângulos (40%) | Elipses (20%) | Setas (20%) | Textos (20%) | Arranjo Espacial em Grade |
| :--- | :-: | :-: | :-: | :-: | :-: | :--- |
| `cena_100.excalidraw` | 100 | 40 | 20 | 20 | 20 | Grade 10 × 10 (passo 160 × 120 px) |
| `cena_1000.excalidraw` | 1.000 | 400 | 200 | 200 | 200 | Grade 40 × 25 (passo 160 × 120 px) |
| `cena_5000.excalidraw` | 5.000 | 2.000 | 1.000 | 1.000 | 1.000 | Grade 100 × 50 (passo 160 × 120 px) |
| `cena_10000.excalidraw` | 10.000 | 4.000 | 2.000 | 2.000 | 2.000 | Grade 100 × 100 (passo 160 × 120 px) |

Cada elemento possui identificador único determinístico (`scale_<N>_<ID>`), sementes pseudoaleatórias fixadas (`seed`, `versionNonce`) para garantir renderização consistente das arestas ásperas (*roughness*), e coordenadas geométricas que evitam sobreposição total, facilitando a seleção em lote de 50 elementos exigida por M3.2.2.

---

## 4. Conjunto de Arquivos Inválidos (`invalidos/`)

Este subconjunto implementa os 9 cenários de teste exigidos pela métrica [M2.3.1](../../docs/fase-02/gqm-confiabilidade.md#m231--proporção-de-arquivos-inválidos-tratados-com-mensagem) (Proporção de arquivos inválidos tratados com mensagem), avaliando a robustez do software ao receber entradas corrompidas ou adversárias.

| Nome do Arquivo | Tipo / Extensão | Defeito Intencional Inserido | Comportamento Esperado no Editor |
| :--- | :--- | :--- | :--- |
| `invalido_01_vazio.excalidraw` | Texto (`.excalidraw`) | Arquivo com tamanho zero bytes (vazio). | Exibir aviso de erro de arquivo vazio ou inválido, sem lançar exceção não capturada nem congelar o canvas. |
| `invalido_02_json_malformado.excalidraw` | Texto (`.excalidraw`) | Erro de sintaxe JSON: chaves e colchetes não fechados e vírgula solta. | Capturar a falha do analisador sintático (`JSON.parse`), alertando sobre formato corrompido sem derrubar a aplicação. |
| `invalido_03_sem_campo_type.excalidraw` | JSON (`.excalidraw`) | JSON estruturalmente íntegro, mas omitindo a propriedade obrigatória `type`. | Rejeitar a carga por ausência do discriminador de tipo do documento com mensagem orientativa. |
| `invalido_04_type_desconhecido.excalidraw` | JSON (`.excalidraw`) | O campo `type` possui o valor `"formato_desconhecido_exemplo"` em vez de `"excalidraw"`. | Identificar incompatibilidade de tipo de arquivo e notificar formato não suportado. |
| `invalido_05_elementos_sem_campos_obrigatorios.excalidraw` | JSON (`.excalidraw`) | Objetos no array `elements` sem propriedades essenciais (`id`, `type`, `x`, `y`, `width`, `height`). | Validar o esquema de cada elemento, alertar a inconsistência estrutural e preservar a prancheta utilizável. |
| `invalido_06_coordenadas_nao_numericas.excalidraw` | JSON (`.excalidraw`) | Campos de posição e dimensões contendo valores não numéricos (`x: "coordenada_invalida_string"`, `y: null`, `height: false`). | Sanitizar ou recusar as coordenadas corrompidas antes do cálculo vetorial, impedindo travamento por `NaN`. |
| `invalido_07_binario_renomeado.excalidraw` | Binário (`.excalidraw`) | Conteúdo binário arbitrário (cabeçalho executável ELF e bytes não-UTF-8) com extensão `.excalidraw`. | Tratar a falha de decodificação de texto, informando que o arquivo é binário ou não legível. |
| `invalido_08_png_sem_desenho.png` | Binário (`.png`) | Imagem raster PNG padrão (1×1 px) sem os metadados de chunk `tEXt`/`zTXt` contendo a cena Excalidraw. | Ao tentar abrir a imagem via menu de abertura de arquivo, notificar que o arquivo não contém um desenho editável incorporado. |
| `invalido_09_truncado_no_meio.excalidraw` | Texto (`.excalidraw`) | Arquivo JSON legítimo cortado bruscamente na metade da payload de elementos (simulando corte de rede ou falha de E/S). | Identificar terminação inesperada do arquivo (fim de arquivo prematuro) e exibir mensagem de recuperação/erro. |

---

## 5. Como Recriar e Validar os Arquivos

A geração de toda a massa de dados é 100% automatizada e não requer dependências externas além do interpretador Python (versão 3.8 ou superior).

### 5.1 Recriar Todos os Arquivos e Executar Validação Estrutural

A partir da raiz do repositório, execute:

```bash
python scripts/gerar_massa_dados.py --verificar
```

A rotina irá:
1. Gerar a cena canônica `cena_referencia.excalidraw`;
2. Gerar as 4 cenas de escala (`cena_100`, `cena_1000`, `cena_5000` e `cena_10000.excalidraw`);
3. Gerar os 9 arquivos inválidos no subdiretório `invalidos/`;
4. Validar o esquema JSON, verificar a presença dos 10 tipos de elementos na cena de referência, conferir a proporção exata nas 4 cenas de escala e atestar a integridade do conjunto inválido.

### 5.2 Comandos para Recriação Seletiva

Caso deseje recriar apenas um subconjunto de dados específico:

- **Apenas a cena de referência:**
  ```bash
  python scripts/gerar_massa_dados.py --so-referencia
  ```

- **Apenas as cenas de escala (100 a 10.000 elementos):**
  ```bash
  python scripts/gerar_massa_dados.py --so-escala
  ```

- **Apenas os arquivos de teste de falha (M2.3.1):**
  ```bash
  python scripts/gerar_massa_dados.py --so-invalidos
  ```

- **Especificar outro diretório de saída:**
  ```bash
  python scripts/gerar_massa_dados.py --output-dir caminho/personalizado/
  ```

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 08/11/2026 | Criação da massa de dados completa para G2 e G3 (cena de referência, cenas de escala e arquivos inválidos) e script gerador | [Gabriel Santos](https://github.com/gabriel-nitro) | |
