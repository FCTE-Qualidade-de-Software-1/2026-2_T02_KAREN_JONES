# Massa de dados para avaliação (Fase 03)

Arquivos de teste usados na medição das métricas de Confiabilidade (G2) e Flexibilidade (G3) durante a Fase 04.

Todos os arquivos são gerados a partir do script `scripts/gerar_massa_dados.py`, para que qualquer pessoa consiga recriar a mesma base de dados.

---

## 1. Cena de referência (`cena_referencia.excalidraw`)

Contém um elemento de cada um dos 10 tipos definidos na Fase 02: retângulo, elipse, losango, seta, linha, desenho livre, texto solto, texto dentro de forma, imagem e moldura (*frame*).

Essa cena padronizada é usada em quatro métricas:
- [M2.4.1](../../docs/fase-02/gqm-confiabilidade.md#m241--proporção-de-cenários-de-fechamento-com-restauração-do-desenho): restauração do desenho após fechamento ou queda do navegador;
- [M2.4.2](../../docs/fase-02/gqm-confiabilidade.md#m242--proporção-de-arquivos-reabertos-sem-perda): reabertura de arquivos de versões anteriores;
- [M3.4.2](../../docs/fase-02/gqm-flexibilidade.md#m342--proporção-de-elementos-preservados-na-exportação-e-reimportação): elementos preservados após exportar e reimportar em `.excalidraw`, PNG e SVG;
- [M3.4.3](../../docs/fase-02/gqm-flexibilidade.md#m343--proporção-dos-campos-do-formato-excalidraw-documentados): proporção dos campos do arquivo documentados na especificação.

### Elementos da cena

| Identificador (`id`) | Tipo (`type`) | Descrição |
| :--- | :--- | :--- |
| `ref_frame_01` | `frame` | Moldura que agrupa os elementos da cena |
| `ref_text_solto_01` | `text` | Texto solto com o título da cena |
| `ref_rect_01` | `rectangle` | Retângulo com cantos arredondados e cor azul |
| `ref_bound_text_01` | `text` | Texto vinculado dentro do retângulo (`ref_rect_01`) |
| `ref_ellipse_01` | `ellipse` | Elipse com preenchimento verde |
| `ref_diamond_01` | `diamond` | Losango com preenchimento amarelo |
| `ref_arrow_01` | `arrow` | Seta com ponta triangular |
| `ref_line_01` | `line` | Linha com três pontos e traço tracejado |
| `ref_freedraw_01` | `freedraw` | Traçado livre feito à mão com variação de pressão |
| `ref_image_01` | `image` | Imagem raster em PNG registrada no campo `files` do arquivo |

---

## 2. Cenas de escala

Quatro arquivos gerados com 100, 1.000, 5.000 e 10.000 elementos para testar a escalabilidade do editor:
- [M3.2.1](../../docs/fase-02/gqm-flexibilidade.md#m321--tempo-de-abertura-por-tamanho-de-cena): tempo de abertura de cada cena;
- [M3.2.2](../../docs/fase-02/gqm-flexibilidade.md#m322--taxa-de-quadros-durante-a-edição-por-tamanho-de-cena): taxa de quadros (FPS) ao arrastar uma seleção de 50 elementos;
- [M3.2.3](../../docs/fase-02/gqm-flexibilidade.md#m323--tamanho-máximo-de-cena-salva-e-exportada): maior cena que salva e exporta em PNG e SVG sem travar o navegador.

### Proporção dos elementos

Todas as cenas seguem a proporção definida na Fase 02: **40% retângulos, 20% elipses, 20% setas e 20% textos**. Os elementos são organizados em grade para que não fiquem sobrepostos.

| Arquivo | Total | Retângulos (40%) | Elipses (20%) | Setas (20%) | Textos (20%) | Grade |
| :--- | :-: | :-: | :-: | :-: | :-: | :--- |
| `cena_100.excalidraw` | 100 | 40 | 20 | 20 | 20 | 10 colunas × 10 linhas |
| `cena_1000.excalidraw` | 1.000 | 400 | 200 | 200 | 200 | 40 colunas × 25 linhas |
| `cena_5000.excalidraw` | 5.000 | 2.000 | 1.000 | 1.000 | 1.000 | 100 colunas × 50 linhas |
| `cena_10000.excalidraw` | 10.000 | 4.000 | 2.000 | 2.000 | 2.000 | 100 colunas × 100 linhas |

---

## 3. Arquivos inválidos (`invalidos/`)

Conjunto de 9 arquivos usados em [M2.3.1](../../docs/fase-02/gqm-confiabilidade.md#m231--proporção-de-arquivos-inválidos-tratados-com-mensagem) para verificar se o editor trata erros de arquivo exibindo mensagem ao usuário e continua funcionando sem travar.

| Arquivo | Defeito introduzido | O que a aplicação deve fazer |
| :--- | :--- | :--- |
| `invalido_01_vazio.excalidraw` | Arquivo vazio com 0 bytes | Exibir mensagem de arquivo vazio ou inválido sem quebrar a página |
| `invalido_02_json_malformado.excalidraw` | JSON com erro de sintaxe (chaves e colchetes não fechados) | Tratar o erro de leitura do JSON e avisar o usuário |
| `invalido_03_sem_campo_type.excalidraw` | JSON válido, mas sem a chave `type` | Rejeitar o arquivo por falta do identificador do formato |
| `invalido_04_type_desconhecido.excalidraw` | Campo `type` com valor não suportado | Avisar que o tipo de arquivo não é reconhecido |
| `invalido_05_elementos_sem_campos_obrigatorios.excalidraw` | Elementos sem propriedades obrigatórias (`id`, `type`, coordenadas) | Identificar que o elemento está incompleto sem travar o editor |
| `invalido_06_coordenadas_nao_numericas.excalidraw` | Posição e dimensões com texto ou `null` no lugar de números | Descartar ou recusar as coordenadas inválidas sem erro no canvas |
| `invalido_07_binario_renomeado.excalidraw` | Arquivo binário arbitrário salvo com extensão `.excalidraw` | Tratar a falha na leitura de texto UTF-8 e exibir mensagem |
| `invalido_08_png_sem_desenho.png` | Imagem PNG comum sem dados do Excalidraw incorporados | Ao tentar abrir pelo menu, avisar que a imagem não contém um desenho editável |
| `invalido_09_truncado_no_meio.excalidraw` | Arquivo `.excalidraw` cortado no meio da lista de elementos | Avisar que o arquivo está corrompido ou incompleto |

---

## 4. Como recriar os arquivos

Para recriar todos os arquivos e rodar a checagem automática, execute na raiz do repositório:

```bash
python scripts/gerar_massa_dados.py --verificar
```

Comandos para recriar apenas uma parte:

- Só a cena de referência: `python scripts/gerar_massa_dados.py --so-referencia`
- Só as cenas de escala: `python scripts/gerar_massa_dados.py --so-escala`
- Só os arquivos inválidos: `python scripts/gerar_massa_dados.py --so-invalidos`

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 08/11/2026 | Documentação da massa de dados de G2 e G3 | [Gabriel Santos](https://github.com/gabriel-nitro) | |
