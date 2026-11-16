# Massa de dados para avaliação (Fase 03)

Arquivos de teste usados na medição das métricas de Confiabilidade (G2) e Flexibilidade (G3) durante a Fase 04.

Todos os arquivos são gerados a partir do script `scripts/gerar_massa_dados.py`, para que qualquer pessoa consiga recriar a mesma base de dados.

---

## 1. Cena de referência (`cena_referencia.excalidraw`)

Contém um elemento de cada um dos 10 tipos definidos na Fase 02: retângulo, elipse, losango, seta, linha, desenho livre, texto solto, texto dentro de forma, imagem e moldura (*frame*).

Essa cena padronizada é usada em quatro métricas:
- [M2.4.1](../../docs/fase-02/gqm-confiabilidade.md#m241-proporção-de-cenários-de-fechamento-com-restauração-do-desenho): restauração do desenho após fechamento ou queda do navegador.
- [M2.4.2](../../docs/fase-02/gqm-confiabilidade.md#m242-proporção-de-arquivos-reabertos-sem-perda): reabertura de arquivos de versões anteriores.
- [M3.4.2](../../docs/fase-02/gqm-flexibilidade.md#m342-proporção-de-elementos-preservados-na-exportação-e-reimportação): elementos preservados após exportar e reimportar em `.excalidraw`, PNG e SVG.
- [M3.4.3](../../docs/fase-02/gqm-flexibilidade.md#m343-proporção-dos-campos-do-formato-excalidraw-documentados): proporção dos campos do arquivo documentados na especificação.

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
- [M3.2.1](../../docs/fase-02/gqm-flexibilidade.md#m321-tempo-de-abertura-por-tamanho-de-cena): tempo de abertura de cada cena.
- [M3.2.2](../../docs/fase-02/gqm-flexibilidade.md#m322-taxa-de-quadros-durante-a-edição-por-tamanho-de-cena): taxa de quadros (FPS) ao arrastar uma seleção de 50 elementos.
- [M3.2.3](../../docs/fase-02/gqm-flexibilidade.md#m323-tamanho-máximo-de-cena-salva-e-exportada): maior cena que salva e exporta em PNG e SVG sem travar o navegador.

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

Conjunto de 9 arquivos usados em [M2.3.1](../../docs/fase-02/gqm-confiabilidade.md#m231-proporção-de-arquivos-inválidos-tratados-com-mensagem) para verificar se o editor trata erros de arquivo exibindo mensagem ao usuário e continua funcionando sem travar.

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

## 4. Conjunto de reabertura (`reabertura/`)

Conjunto fixo de 7 entradas da [M2.4.2](../../docs/fase-02/gqm-confiabilidade.md#m242-proporção-de-arquivos-reabertos-sem-perda). O uso de cada entrada na coleta segue a [instrução de G2 para a M2.4.2](../../docs/fase-03/instrucoes-g2-confiabilidade.md#m242--reabertura-dos-sete-arquivos-sem-perda).

Os casos c2 a c5 são a cena de referência aberta e salva pela interface de cada versão antiga, construída a partir da marcação (*tag*) do repositório do Excalidraw. O script só aciona a interface e nunca escreve esses arquivos, e o campo `source` de cada um traz o endereço da versão que o salvou. Os casos c6 e c7 são os PNGs de exemplo do commit avaliado, sem alteração de bytes. A cena incorporada em cada PNG foi extraída para `c6_referencia.excalidraw` e `c7_referencia.excalidraw`, que servem de referência na comparação no lugar dos pixels da prévia.

**Tabela: Casos do conjunto de reabertura**

| Caso | Arquivo | Origem | Versão | Node.js |
| :-: | :--- | :--- | :-: | :-: |
| c1 | [`../cena_referencia.excalidraw`](./cena_referencia.excalidraw) | Gerado por `scripts/gerar_massa_dados.py` | `e1b7aacb` | |
| c2 | `c2_v0.15.0.excalidraw` | Salvo pela interface, com o `Dockerfile` da tag | `v0.15.0` | v14.21.3 |
| c3 | `c3_v0.16.4.excalidraw` | Salvo pela interface, com `Dockerfile` alternativo `node:18` | `v0.16.4` | v18.20.8 |
| c4 | `c4_v0.17.6.excalidraw` | Salvo pela interface, com `Dockerfile` alternativo `node:18` | `v0.17.6` | v18.20.8 |
| c5 | `c5_v0.18.0.excalidraw` | Salvo pela interface, com o `Dockerfile` da tag | `v0.18.0` | v18.20.8 |
| c6 | `c6_test_embedded_v1.png` | Fixture `test_embedded_v1.png` do commit avaliado | `e1b7aacb` | |
| c7 | `c7_smiley_embedded_v2.png` | Fixture `smiley_embedded_v2.png` do commit avaliado | `e1b7aacb` | |

Fonte: [Christopher Paraizo](https://github.com/wChrstphr), 2026.

As tags `v0.16.4` e `v0.17.6` não constroem com o próprio `Dockerfile`, porque o `.dockerignore` delas exclui arquivos que a construção exige. Nesses casos o script usa uma imagem `node:18`, que atende ao campo `engines` das duas versões.

O [`manifesto.csv`](./reabertura/manifesto.csv) registra, por caso, o SHA-256 do arquivo, a quantidade de elementos da referência e do arquivo salvo, os identificadores ausentes e as propriedades alteradas. As incompatibilidades encontradas foram:

- `v0.15.0` (c2): não salva a moldura `ref_frame_01`, porque a versão não tem o tipo `frame`, e altera `width` e `height` de `ref_text_solto_01` e `x`, `width` e `height` de `ref_bound_text_01` ao recalcular o texto.
- `v0.16.4`, `v0.17.6` e `v0.18.0` (c3 a c5): preservam os 10 elementos da referência.

A entrada c2 continua no conjunto com a perda registrada, e o total permanece em 7 entradas.

---

## 5. Como recriar os arquivos

Para recriar todos os arquivos e rodar a checagem automática, execute na raiz do repositório:

```bash
python scripts/gerar_massa_dados.py --verificar
```

Comandos para recriar apenas uma parte:

- Só a cena de referência: `python scripts/gerar_massa_dados.py --so-referencia`.
- Só as cenas de escala: `python scripts/gerar_massa_dados.py --so-escala`.
- Só os arquivos inválidos: `python scripts/gerar_massa_dados.py --so-invalidos`.
- Só os PNGs de c6 e c7 e as cenas extraídas deles: `python scripts/gerar_massa_dados.py --so-reabertura-png`.

Os arquivos de c2 a c5 e o manifesto são recriados por `scripts/gerar_massa_versoes_antigas.py`, que exige Docker e Playwright com Firefox:

```bash
pip install -r scripts/requirements.txt
python -m playwright install firefox
python scripts/gerar_massa_versoes_antigas.py
```

Para cada versão, o script clona a tag numa pasta fora do repositório (`--work-dir`, padrão `~/.cache/karen-jones/excalidraw-versoes`), constrói a imagem Docker, serve a aplicação numa porta própria (3011 a 3014), abre a cena de referência pelo menu e salva pelo comando de salvar em arquivo. A construção é lenta, então é possível processar uma versão por vez:

- Uma versão: `python scripts/gerar_massa_versoes_antigas.py --versao v0.18.0`.
- Manter a versão no ar para inspeção manual: `python scripts/gerar_massa_versoes_antigas.py --versao v0.18.0 --so-servir`.
- Só regenerar o manifesto a partir dos arquivos já salvos: `python scripts/gerar_massa_versoes_antigas.py --so-manifesto`.

O `--verificar` confere a presença das 7 entradas, das cenas extraídas e do manifesto, e se o SHA-256 de cada arquivo bate com o manifesto, sem regenerar c2 a c5.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 08/11/2026 | Documentação da massa de dados de G2 e G3 | [Gabriel Santos](https://github.com/gabriel-nitro) | |
| 1.1 | 15/11/2026 | Inclusão do conjunto de reabertura da M2.4.2 e dos comandos para recriá-lo | [Christopher Paraizo](https://github.com/wChrstphr) | |
