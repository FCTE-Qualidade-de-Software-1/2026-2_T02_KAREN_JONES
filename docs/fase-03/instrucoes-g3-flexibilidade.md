---
sidebar_position: 4
title: Instruções para o avaliador — Flexibilidade (G3)
description: Procedimento passo a passo para obtenção das 12 métricas do objetivo G3 (Flexibilidade) na Fase 04, com pré-condições, comandos exatos, saídas esperadas, cálculo, formulários e arquivos de dados brutos.
---

# Instruções para o avaliador — Flexibilidade (G3)

Este documento descreve o passo a passo para a coleta das 12 métricas do objetivo **G3 — Flexibilidade** na Fase 04. As instruções cobrem as quatro questões do GQM (Adaptabilidade, Escalabilidade, Instalabilidade e Substituibilidade), com pré-condições, comandos exatos, saídas esperadas, modo de cálculo e armazenamento dos dados brutos.

O roteiro atende aos critérios **F3-C1** (repetibilidade das instruções) e **F3-C8** (consistência entre Fases 02 e 03), permitindo que qualquer membro da equipe ou avaliador independente execute os passos sob o mesmo ambiente de [Recursos e ambiente](./recursos-ambiente.md) e chegue aos mesmos resultados.

---

## 1. Visão geral das métricas de G3

A tabela abaixo resume as 12 métricas de Flexibilidade divididas pelas quatro questões do [GQM de Flexibilidade](../fase-02/gqm-flexibilidade.md), indicando o tipo de coleta, o link para a respectiva ficha na Fase 02 e o link para a sua faixa de pontuação em [Níveis de pontuação e critérios de julgamento](../fase-02/pontuacao-julgamento.md).

| Métrica | Nome da métrica | Questão | Tipo de coleta | Ficha na Fase 02 | Níveis de pontuação |
| :--- | :--- | :---: | :--- | :---: | :---: |
| **M3.1.1** | Cobertura de usuários pelos navegadores declarados | Q3.1 | Automatizada (CLI) | [Ficha M3.1.1](../fase-02/gqm-flexibilidade.md#m311--cobertura-de-usuários-pelos-navegadores-declarados) | [Pontuação M3.1.1](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3) |
| **M3.1.2** | Proporção de ambientes de integração com sucesso | Q3.1 | Mista (Script + Build) | [Ficha M3.1.2](../fase-02/gqm-flexibilidade.md#m312--proporção-de-ambientes-de-integração-com-sucesso) | [Pontuação M3.1.2](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3) |
| **M3.1.3** | Proporção de ações de edição por toque e caneta | Q3.1 | Manual roteirizada | [Ficha M3.1.3](../fase-02/gqm-flexibilidade.md#m313--proporção-de-ações-de-edição-que-funcionam-por-toque-e-caneta) | [Pontuação M3.1.3](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3) |
| **M3.2.1** | Tempo de abertura por tamanho de cena | Q3.2 | Ferramenta DevTools | [Ficha M3.2.1](../fase-02/gqm-flexibilidade.md#m321--tempo-de-abertura-por-tamanho-de-cena) | [Pontuação M3.2.1](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3) |
| **M3.2.2** | Taxa de quadros durante a edição por tamanho de cena | Q3.2 | Ferramenta DevTools | [Ficha M3.2.2](../fase-02/gqm-flexibilidade.md#m322--taxa-de-quadros-durante-a-edição-por-tamanho-de-cena) | [Pontuação M3.2.2](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3) |
| **M3.2.3** | Tamanho máximo de cena salva e exportada | Q3.2 | Manual roteirizada | [Ficha M3.2.3](../fase-02/gqm-flexibilidade.md#m323--tamanho-máximo-de-cena-salva-e-exportada) | [Pontuação M3.2.3](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3) |
| **M3.3.1** | Proporção de operações de pacote bem-sucedidas | Q3.3 | Automatizada (Script) | [Ficha M3.3.1](../fase-02/gqm-flexibilidade.md#m331--proporção-de-operações-de-pacote-bem-sucedidas) | [Pontuação M3.3.1](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3) |
| **M3.3.2** | Proporção de passos documentados reproduzidos sem ajuste | Q3.3 | Manual roteirizada | [Ficha M3.3.2](../fase-02/gqm-flexibilidade.md#m332--proporção-de-passos-documentados-reproduzidos-sem-ajuste) | [Pontuação M3.3.2](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3) |
| **M3.3.3** | Implantação com Docker | Q3.3 | Automatizada (CLI) | [Ficha M3.3.3](../fase-02/gqm-flexibilidade.md#m333--implantação-com-docker) | [Pontuação M3.3.3](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3) |
| **M3.4.1** | Formatos de exportação abertos disponíveis | Q3.4 | Inspeção de interface | [Ficha M3.4.1](../fase-02/gqm-flexibilidade.md#m341--formatos-de-exportação-abertos-disponíveis) | [Pontuação M3.4.1](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3) |
| **M3.4.2** | Proporção de elementos preservados na reimportação | Q3.4 | Mista (UI + Script) | [Ficha M3.4.2](../fase-02/gqm-flexibilidade.md#m342--proporção-de-elementos-preservados-na-exportação-e-reimportação) | [Pontuação M3.4.2](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3) |
| **M3.4.3** | Proporção dos campos de `.excalidraw` documentados | Q3.4 | Automatizada (Script) | [Ficha M3.4.3](../fase-02/gqm-flexibilidade.md#m343--proporção-dos-campos-do-formato-excalidraw-documentados) | [Pontuação M3.4.3](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3) |

---

## 2. Diretrizes gerais para a execução da avaliação

### 2.1 Repositório e commit avaliado

A coleta da Fase 04 parte do repositório oficial do Excalidraw no commit fixado no [escopo da avaliação](../fase-01/escopo-avaliacao.md):

```bash
git clone https://github.com/excalidraw/excalidraw.git
cd excalidraw
git checkout e1b7aacb356a492aa1e0fc6eb57b8896124027f0
git rev-parse --short HEAD
```

O comando deve imprimir `e1b7aac`. Se imprimir outro valor, a coleta não deve começar.

### 2.2 Local e padrão de nomenclatura dos dados brutos

Todos os artefatos brutos resultantes da medição (arquivos de log, planilhas CSV, saídas de comandos, capturas e gravações de vídeo) devem ser armazenados sob o diretório:

```text
dados/fase-04/brutos/
```

Os arquivos seguem a convenção `M<código>_<identificador-curto>.<extensão>`. Exemplo: `M3.1.1_cobertura_browserslist.txt`.

### 2.3 Política obrigatória de gravação de tela para testes no navegador

Conforme exigido pelo critério **F4-C2**, todo teste manual ou medição interativa executada no navegador ou em dispositivo móvel exige gravação contínua da tela:

1. **Ferramenta de gravação no computador:** OBS Studio ou SimpleScreenRecorder no Linux/Windows, gravando a área inteira da tela onde a aplicação está sendo operada, com o relógio do sistema visível.
2. **Ferramenta no dispositivo móvel:** Recurso nativo de gravação de tela do sistema operacional (iOS ou Android).
3. **Padrão de nome do vídeo:** `dados/fase-04/brutos/M<código>_gravacao_<acao>.mp4`.
4. Os vídeos devem ser versionados junto às evidências no repositório da disciplina ou vinculados no relatório técnico caso excedam o limite de tamanho do Git (com hash SHA-256 e link de armazenamento em nuvem registrado).

### 2.4 Fatores de variação a registrar em toda coleta

Para cada execução, o avaliador deve preencher o cabeçalho de contexto contendo os fatores de variação:

- **Data e hora:** início e término da medição.
- **Avaliador:** nome completo e usuário no GitHub.
- **Identificação da máquina:** processador, memória RAM e placa de vídeo.
- **Sistema operacional:** nome e versão exata (`uname -a` ou `winver`).
- **Navegador:** nome e versão completa (ex.: Google Chrome 130.0.6723.70).
- **Ambiente de execução:** local com Docker, Node.js nativo ou dispositivo móvel.
- **Rede:** status da conexão (online ou offline).

---

## 3. Instruções detalhadas por métrica

### 3.1 Adaptabilidade (Q3.1)

#### M3.1.1 — Cobertura de usuários pelos navegadores declarados

- **Questão respondida:** Q3.1 (Adaptabilidade).
- **Hipótese:** H3.1.1 (Confirmada se cobertura ≥ 80%).
- **Links:** [Ficha da métrica](../fase-02/gqm-flexibilidade.md#m311--cobertura-de-usuários-pelos-navegadores-declarados) | [Faixa de pontuação](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3).

##### Pré-condições
1. Repositório no commit `e1b7aac`.
2. Node.js instalado (versão ≥ 18.0.0).
3. Terminal com acesso à internet para consulta à base global do Browserslist.

##### Passo a passo
1. Abra o terminal no diretório do aplicativo web:
   ```bash
   cd excalidraw/excalidraw-app
   ```
2. Verifique a consulta declarada no campo `browserslist.production` do arquivo `package.json`:
   ```bash
   node -e "console.log(require('./package.json').browserslist.production)"
   ```
3. Execute o comando oficial do Browserslist para calcular a cobertura populacional global:
   ```bash
   npx browserslist --coverage=global
   ```
4. Liste os navegadores suportados e os excluídos explicitamente:
   ```bash
   npx browserslist
   ```
5. Registre a versão exata do Browserslist e do pacote de dados `caniuse-lite`:
   ```bash
   npx browserslist --version
   npm list caniuse-lite
   ```

##### Saída esperada
O terminal deve imprimir uma mensagem similar a:
```text
These browsers account for 85.4% of all users globally:
  and_chr 129
  chrome 130
  ...
```

##### Cálculo do valor
O valor da métrica é a porcentagem informada diretamente na linha `These browsers account for X% of all users globally`.

##### Arquivo de dados brutos
Salve a saída completa dos comandos em:
- `dados/fase-04/brutos/M3.1.1_cobertura_browserslist.txt`

---

#### M3.1.2 — Proporção de ambientes de integração com sucesso

- **Questão respondida:** Q3.1 (Adaptabilidade).
- **Hipótese:** H3.1.2 (Confirmada se = 6 de 6 combinações).
- **Links:** [Ficha da métrica](../fase-02/gqm-flexibilidade.md#m312--proporção-de-ambientes-de-integração-com-sucesso) | [Faixa de pontuação](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3).

##### Pré-condições
1. Biblioteca `@excalidraw/excalidraw` empacotada localmente via `yarn build:packages` e `npm pack` dentro de `packages/excalidraw`, gerando o arquivo `excalidraw-excalidraw-0.17.6.tgz`.
2. Ambiente limpo (Node.js 24 via Docker ou ambiente isolado na máquina).

##### Matriz de 6 combinações
1. Combinação 1: React 17 + Vite
2. Combinação 2: React 18 + Vite
3. Combinação 3: React 19 + Vite
4. Combinação 4: React 17 + Next.js
5. Combinação 5: React 18 + Next.js
6. Combinação 6: React 19 + Next.js

##### Passo a passo para cada combinação com Vite
1. Crie um projeto mínimo Vite:
   ```bash
   npm create vite@latest app-vite-react -- --template react-ts
   cd app-vite-react
   ```
2. Instale a versão de React correspondente (exemplo para React 18):
   ```bash
   npm install react@18 react-dom@18
   ```
3. Instale o pacote local avaliado:
   ```bash
   npm install /caminho/absoluto/excalidraw-excalidraw-0.17.6.tgz
   ```
4. Edite `src/App.tsx` para importar e renderizar o Excalidraw com tamanho fixo:
   ```tsx
   import { Excalidraw } from "@excalidraw/excalidraw";
   export default function App() {
     return <div style={{ height: "500px", width: "100%" }}><Excalidraw /></div>;
   }
   ```
5. Execute a construção e inicialize o servidor de pré-visualização:
   ```bash
   npm run build
   npm run preview
   ```
6. Abra o navegador em `http://localhost:4173`, verifique o console do desenvolvedor e tente desenhar um retângulo.

##### Passo a passo para cada combinação com Next.js
1. Crie o projeto Next.js com TypeScript:
   ```bash
   npx create-next-app@latest app-next --typescript --eslint --no-tailwind --app --no-src-dir --import-alias "@/*"
   cd app-next
   ```
2. Instale o pacote local e a versão desejada de React.
3. Conforme documentado no guia de integração (`examples/with-nextjs`), o Excalidraw acessa APIs do navegador e exige importação dinâmica no lado do cliente:
   ```tsx
   "use client";
   import dynamic from "next/dynamic";
   const Excalidraw = dynamic(
     async () => (await import("@excalidraw/excalidraw")).Excalidraw,
     { ssr: false }
   );
   export default function Page() {
     return <div style={{ height: "500px", width: "100%" }}><Excalidraw /></div>;
   }
   ```
4. Execute `npm run build` e `npm run start`. Abra no navegador e verifique o desenho.

##### Critério de sucesso de cada combinação
Uma combinação é considerada bem-sucedida se e somente se:
- A compilação (`build`) terminar com código de saída 0;
- A página carregar sem exceções não tratadas no console;
- For possível desenhar uma forma geométrica no canvas.

##### Cálculo do valor
Proporção = (combinações com sucesso ÷ 6) × 100.

##### Arquivos de dados brutos
- Tabela resumo preenchida: `dados/fase-04/brutos/M3.1.2_matriz_integracao.csv`
- Logs de compilação: `dados/fase-04/brutos/M3.1.2_build_logs.zip`
- Capturas de tela do editor em funcionamento em cada projeto: `dados/fase-04/brutos/M3.1.2_evidencia_ambiente.png`

---

#### M3.1.3 — Proporção de ações de edição por toque e caneta

- **Questão respondida:** Q3.1 (Adaptabilidade).
- **Hipótese:** H3.1.3 (Confirmada se = 10 de 10 ações por toque).
- **Links:** [Ficha da métrica](../fase-02/gqm-flexibilidade.md#m313--proporção-de-ações-de-edição-que-funcionam-por-toque-e-caneta) | [Faixa de pontuação](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3).

##### Pré-condições
1. Aplicação Excalidraw de produção em execução (`http://ip-do-servidor:3000`).
2. Dispositivo móvel com tela de toque conectado à mesma rede local.
3. Gravação de tela do dispositivo ativada desde o início do roteiro.

##### Roteiro das 10 ações padronizadas
Execute sequencialmente as seguintes ações, primeiro usando o dedo e depois usando a caneta (se disponível no aparelho):

1. **Criar uma forma:** selecionar a ferramenta de retângulo na barra superior e arrastar o dedo na tela até criar o objeto.
2. **Desenhar à mão livre:** selecionar a ferramenta de desenho livre (*freedraw*) e traçar uma curva contínua.
3. **Selecionar um elemento:** tocar sobre o retângulo desenhado no passo 1 e confirmar o aparecimento da caixa delimitadora com alças.
4. **Mover um elemento:** tocar e arrastar o elemento selecionado para outra posição na tela.
5. **Redimensionar um elemento:** tocar em uma das alças de canto da caixa delimitadora e arrastar para alterar o tamanho.
6. **Aproximar e afastar com pinça (*pinch-to-zoom*):** usar dois dedos em movimento de pinça para ampliar e reduzir o zoom da tela.
7. **Deslocar a tela com dois dedos (*pan*):** arrastar dois dedos simultaneamente pelo canvas para navegar pela cena.
8. **Escrever texto com teclado virtual:** tocar na ferramenta de texto, tocar no canvas para abrir o teclado virtual nativo, digitar a palavra "Teste" e confirmar.
9. **Desfazer:** tocar no botão de seta para a esquerda (desfazer) na barra de ferramentas inferior e confirmar o desfazimento da última ação.
10. **Abrir o menu principal:** tocar no ícone de menu superior esquerdo (menu hambúrguer) e verificar a abertura do painel lateral de opções.

##### Formulário de coleta manual
O avaliador deve preencher a tabela a seguir durante o teste:

```csv
Acao,Dedo (Sucesso/Falha),Caneta (Sucesso/Falha),Observacoes
1. Criar forma,,,
2. Desenhar livre,,,
3. Selecionar elemento,,,
4. Mover elemento,,,
5. Redimensionar elemento,,,
6. Zoom com pinca,,,
7. Deslocar tela (pan),,,
8. Texto com teclado virtual,,,
9. Desfazer,,,
10. Abrir menu,,,
```

##### Cálculo do valor
Proporção (Toque) = (ações com sucesso pelo toque ÷ 10) × 100.
Se houver caneta, calcule também a proporção para a caneta. A pontuação final da métrica será a média entre as duas formas de entrada.

##### Arquivos de dados brutos
- Formulário preenchido: `dados/fase-04/brutos/M3.1.3_formulario_toque_caneta.csv`
- Vídeos de gravação de tela: `dados/fase-04/brutos/M3.1.3_gravacao_toque.mp4` e `dados/fase-04/brutos/M3.1.3_gravacao_caneta.mp4`

---

### 3.2 Escalabilidade (Q3.2)

As métricas de escalabilidade avaliam o comportamento do editor sob diferentes volumes de elementos, utilizando as quatro **cenas de escala** (100, 1.000, 5.000 e 10.000 elementos com proporção fixa de 40% retângulos, 20% elipses, 20% setas e 20% textos dispostos em grade).

Os arquivos ficam em `dados/fase-03/massa-de-dados/` (`cena_100.excalidraw`, `cena_1000.excalidraw`, `cena_5000.excalidraw` e `cena_10000.excalidraw`). Caso não estejam presentes, o avaliador pode recriá-los com o script gerador a partir da raiz do repositório:

```bash
python scripts/gerar_massa_dados.py --so-escala
```

#### M3.2.1 — Tempo de abertura por tamanho de cena

- **Questão respondida:** Q3.2 (Escalabilidade).
- **Hipótese:** H3.2.1 (Confirmada se tempo na cena de 1.000 elementos for ≤ 1 s).
- **Links:** [Ficha da métrica](../fase-02/gqm-flexibilidade.md#m321--tempo-de-abertura-por-tamanho-de-cena) | [Faixa de pontuação](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3).

##### Pré-condições
1. Aplicação executando localmente em contêiner de produção (`http://localhost:3000`).
2. Google Chrome de versão fixa em perfil limpo e sem extensões de terceiros ativas.
3. Computador conectado à tomada elétrica com plano de energia em alto desempenho.
4. Cenas de escala disponíveis em `dados/fase-03/massa-de-dados/` (`cena_100.excalidraw`, `cena_1000.excalidraw`, `cena_5000.excalidraw` e `cena_10000.excalidraw`).

##### Passo a passo para cada cena
Para cada uma das 4 cenas, realize 5 repetições seguindo este ciclo:

1. Abra a aba do navegador em `http://localhost:3000`.
2. Abra as Ferramentas do Desenvolvedor (F12) e acesse a aba **Performance**.
3. Abra o console (aba Console) e limpe os dados locais:
   ```javascript
   localStorage.clear();
   sessionStorage.clear();
   ```
4. Recarregue a página com bypass de cache: pressione `Ctrl + Shift + R`.
5. Na aba **Performance**, clique no botão circular **Record** (ou `Ctrl + E`) para iniciar a gravação do perfil de desempenho.
6. Arraste e solte o arquivo da cena correspondente (localizado em `dados/fase-03/massa-de-dados/cena_<tamanho>.excalidraw`, ex.: `dados/fase-03/massa-de-dados/cena_1000.excalidraw`) diretamente sobre a área do canvas do editor.
7. Aguarde a conclusão visual da renderização de todos os elementos na tela.
8. Clique no botão **Stop** no painel de gravação do DevTools.
9. No gráfico temporal (*timeline*), identifique a duração do processo desde o evento `drop` do arquivo até a finalização da última tarefa longa (*Long Task*) de renderização ou commit do DOM.
10. Anote a duração em segundos com duas casas decimais no formulário de medição.
11. Exporte o arquivo de rastreamento do Chrome clicando com botão direito na timeline e selecionando **Save profile...**.

##### Cálculo do valor
Para cada uma das quatro cenas:
1. Ordene os tempos das 5 repetições e selecione o terceiro valor (mediana).
2. O resultado é a curva de medianas: `[T_100, T_1000, T_5000, T_10000]`.
3. Pontue cada mediana segundo as faixas de M3.2.1 e calcule a média das pontuações.

##### Arquivos de dados brutos
- Tabela com todas as 20 medições e medianas: `dados/fase-04/brutos/M3.2.1_tempos_abertura.csv`
- Arquivos de perfil do DevTools exportados: `dados/fase-04/brutos/M3.2.1_trace_cena_<elementos>_rep<1..5>.json`
- Gravação de tela do teste: `dados/fase-04/brutos/M3.2.1_gravacao_abertura.mp4`

---

#### M3.2.2 — Taxa de quadros durante a edição por tamanho de cena

- **Questão respondida:** Q3.2 (Escalabilidade).
- **Hipótese:** H3.2.2 (Confirmada se taxa na cena de 1.000 elementos for ≥ 48 FPS).
- **Links:** [Ficha da métrica](../fase-02/gqm-flexibilidade.md#m322--taxa-de-quadros-durante-a-edição-por-tamanho-de-cena) | [Faixa de pontuação](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3).

##### Pré-condições
1. Mesmas pré-condições de hardware e ambiente limpo de M3.2.1.
2. Monitor com taxa de atualização padrão de 60 Hz.
3. Painel de renderização do DevTools acessível via menu de três pontos → **More tools** → **Rendering** → marcar **Frame Rendering Stats** para exibição do FPS em tempo real no canto superior direito.

##### Passo a passo para cada cena
Para cada uma das 4 cenas (100, 1.000, 5.000 e 10.000 elementos), realize 5 repetições de 10 segundos:

1. Carregue o arquivo da cena no editor arrastando-o a partir de `dados/fase-03/massa-de-dados/cena_<tamanho>.excalidraw`.
2. Selecione uma amostra contígua de 50 elementos desenhando um retângulo de seleção ao redor deles (a disposição em grade regular facilita a seleção em bloco).
3. Abra a aba **Performance** do DevTools.
4. Inicie a gravação no DevTools (botão **Record**).
5. Durante exatamente 10 segundos (acompanhados por cronômetro na tela), execute o roteiro de movimentação contínua:
   - Segure o clique sobre a seleção de 50 elementos e arraste-os continuamente em trajetória circular ampla;
   - Alterne a cada 3 segundos com navegação panorâmica (*pan*), segurando a barra de espaço e movimentando o cursor pela tela.
6. Pare a gravação no painel de desempenho.
7. Analise a seção **Frames** no relatório gerado pelo DevTools e registre a taxa média de quadros por segundo (*Frames Per Second*) observada durante os 10 segundos de interação contínua.
8. Exporte o perfil do Chrome (*Save profile...*).

##### Cálculo do valor
1. Para cada cena, tome a mediana das 5 repetições de FPS: FPS_mediana.
2. Calcule o percentual em relação à meta de 60 FPS:
   Aderência FPS = (FPS mediana ÷ 60) × 100.
3. Converta cada valor em nível ordinal conforme a tabela de pontuação e calcule a média das 4 cenas.

##### Arquivos de dados brutos
- Tabela com as taxas de quadros registradas: `dados/fase-04/brutos/M3.2.2_fps_edicao.csv`
- Perfis exportados: `dados/fase-04/brutos/M3.2.2_trace_fps_cena_<elementos>_rep<1..5>.json`
- Gravação de tela com o medidor de FPS visível: `dados/fase-04/brutos/M3.2.2_gravacao_fps.mp4`

---

#### M3.2.3 — Tamanho máximo de cena salva e exportada

- **Questão respondida:** Q3.2 (Escalabilidade).
- **Hipótese:** H3.2.3 (Confirmada se maior cena salva e exportada for ≥ 5.000 elementos).
- **Links:** [Ficha da métrica](../fase-02/gqm-flexibilidade.md#m323--tamanho-máximo-de-cena-salva-e-exportada) | [Faixa de pontuação](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3).

##### Pré-condições
1. Aplicação em execução no navegador em perfil limpo.
2. Cenas de escala disponíveis em `dados/fase-03/massa-de-dados/` (`cena_100.excalidraw`, `cena_1000.excalidraw`, `cena_5000.excalidraw` e `cena_10000.excalidraw`).
3. Cronômetro digital visível durante a gravação de tela.

##### Passo a passo
Na ordem crescente de tamanho (100, 1.000, 5.000 e 10.000 elementos):

1. Abra a cena no editor arrastando o arquivo correspondente de `dados/fase-03/massa-de-dados/` (ex.: `cena_100.excalidraw`).
2. **Operação 1 — Salvar arquivo:**
   - Clique no menu principal (canto superior esquerdo) → **Salvar no disco** (formato `.excalidraw`);
   - Inicie o cronômetro no momento do clique e encerre quando o download for concluído na barra do navegador;
   - Anote o tempo e se houve travamento.
3. **Operação 2 — Exportar PNG:**
   - Pressione `Ctrl + Shift + E` (ou menu → **Exportar imagem**);
   - Mantenha a escala padrão de 1x com fundo e clique no botão **PNG**;
   - Cronometre o tempo até a conclusão do download.
4. **Operação 3 — Exportar SVG:**
   - No diálogo de exportação, clique no botão **SVG**;
   - Cronometre o tempo até a conclusão do download.
5. **Critério de reprovação da cena:**
   - A cena é considerada reprovada se qualquer uma das 3 operações demorar mais de 30 segundos, se a aba do navegador falhar (*crash*) ou se o navegador exibir o alerta do sistema "A página não está respondendo".
6. Se a cena atual for aprovada nas 3 operações, avance para a próxima cena de escala. Se reprovar em qualquer operação, interrompa o teste.

##### Cálculo do valor
O valor da métrica é a quantidade de elementos da maior cena em que as três operações terminaram com sucesso em até 30 segundos (100, 1.000, 5.000 ou 10.000 elementos; se nenhuma passar de 100, o valor é 0).

##### Arquivos de dados brutos
- Tabela de tempos e status por operação: `dados/fase-04/brutos/M3.2.3_tamanho_maximo_salvamento.csv`
- Gravação de tela de todo o teste de estresse: `dados/fase-04/brutos/M3.2.3_gravacao_exportacao.mp4`

---

### 3.3 Instalabilidade (Q3.3)

#### M3.3.1 — Proporção de operações de pacote bem-sucedidas

- **Questão respondida:** Q3.3 (Instalabilidade).
- **Hipótese:** H3.3.1 (Confirmada se = 9 de 9 operações).
- **Links:** [Ficha da métrica](../fase-02/gqm-flexibilidade.md#m331--proporção-de-operações-de-pacote-bem-sucedidas) | [Faixa de pontuação](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3).

##### Pré-condições
1. Pacote avaliado `.tgz` gerado a partir do commit `e1b7aac`.
2. Ambiente limpo em contêiner oficial:
   ```bash
   docker run --rm -it node:24@sha256:8530f76a96d88820d288761f022e318970dda93d01536919fbc16076b7983e63 bash
   ```
3. No contêiner, copie o arquivo `.tgz` avaliado para `/tmp/excalidraw.tgz`.

##### As 9 operações avaliadas
A matriz avalia 3 gerenciadores de pacotes (`npm`, `yarn` v1, `pnpm`) contra 3 operações essenciais:
1. **Instalação:** instalar o pacote avaliado em projeto React 18 vazio.
2. **Atualização:** instalar a versão prévia publicada no npm (`0.17.6`) e atualizar em seguida para o pacote avaliado local.
3. **Remoção:** desinstalar o pacote `@excalidraw/excalidraw` do projeto.

##### Passo a passo para cada gerenciador

###### Cenário A: NPM
```bash
# 1. Instalação
mkdir /teste-npm && cd /teste-npm
npm init -y
npm install react@18 react-dom@18
npm install /tmp/excalidraw.tgz
# Verifica se compila/resolve
node -e "require('@excalidraw/excalidraw')"

# 2. Atualização
mkdir /teste-npm-upgrade && cd /teste-npm-upgrade
npm init -y
npm install react@18 react-dom@18 @excalidraw/excalidraw@0.17.6
npm install /tmp/excalidraw.tgz
node -e "require('@excalidraw/excalidraw')"

# 3. Remoção
npm uninstall @excalidraw/excalidraw
node -e "try { require('@excalidraw/excalidraw'); process.exit(1); } catch (e) { process.exit(0); }"
```

###### Cenário B: Yarn (v1.22.22)
```bash
# 1. Instalação
mkdir /teste-yarn && cd /teste-yarn
yarn init -y
yarn add react@18 react-dom@18
yarn add file:/tmp/excalidraw.tgz
node -e "require('@excalidraw/excalidraw')"

# 2. Atualização
mkdir /teste-yarn-upgrade && cd /teste-yarn-upgrade
yarn init -y
yarn add react@18 react-dom@18 @excalidraw/excalidraw@0.17.6
yarn add file:/tmp/excalidraw.tgz
node -e "require('@excalidraw/excalidraw')"

# 3. Remoção
yarn remove @excalidraw/excalidraw
node -e "try { require('@excalidraw/excalidraw'); process.exit(1); } catch (e) { process.exit(0); }"
```

###### Cenário C: PNPM
```bash
corepack enable && corepack prepare pnpm@latest --activate

# 1. Instalação
mkdir /teste-pnpm && cd /teste-pnpm
pnpm init
pnpm add react@18 react-dom@18
pnpm add /tmp/excalidraw.tgz
node -e "require('@excalidraw/excalidraw')"

# 2. Atualização
mkdir /teste-pnpm-upgrade && cd /teste-pnpm-upgrade
pnpm init
pnpm add react@18 react-dom@18 @excalidraw/excalidraw@0.17.6
pnpm add /tmp/excalidraw.tgz
node -e "require('@excalidraw/excalidraw')"

# 3. Remoção
pnpm remove @excalidraw/excalidraw
node -e "try { require('@excalidraw/excalidraw'); process.exit(1); } catch (e) { process.exit(0); }"
```

##### Critério de sucesso
Uma operação tem sucesso se terminar com código de saída 0 e sem avisos de dependência corrompida no `package.json`.

##### Cálculo do valor
Proporção = (operações com sucesso ÷ 9) × 100.

##### Arquivos de dados brutos
- Registro de log de terminal: `dados/fase-04/brutos/M3.3.1_log_operacoes_pacote.txt`
- Tabela resumo das 9 operações: `dados/fase-04/brutos/M3.3.1_resultados_pacote.csv`

---

#### M3.3.2 — Proporção de passos documentados reproduzidos sem ajuste

- **Questão respondida:** Q3.3 (Instalabilidade).
- **Hipótese:** H3.3.2 (Confirmada se ≥ 95% dos passos forem executados sem ajuste).
- **Links:** [Ficha da métrica](../fase-02/gqm-flexibilidade.md#m332--proporção-de-passos-documentados-reproduzidos-sem-ajuste) | [Faixa de pontuação](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3).

##### Pré-condições
1. Ambiente limpo em máquina Linux ou contêiner limpo sem dependências de compilação previamente configuradas.
2. Guias oficiais do commit `e1b7aac`: `README.md` e `dev-docs/docs/introduction/development.mdx`.

##### Lista dos passos documentados para execução local
O avaliador deve extrair a sequência exata de comandos descrita no guia oficial:

- **Via 1: Execução nativa com Node.js e Yarn:**
  - Passo 1: `git clone https://github.com/excalidraw/excalidraw.git`
  - Passo 2: `cd excalidraw`
  - Passo 3: `yarn`
  - Passo 4: `yarn start`
  - Passo 5: Acesso ao navegador no endereço impresso (`http://localhost:3000`).
- **Via 2: Execução com Docker Compose:**
  - Passo 6: `docker compose up` (ou `docker-compose up`, conforme estiver escrito no guia)
  - Passo 7: Acesso ao navegador em `http://localhost:3000`.

##### Procedimento de execução
1. Execute cada passo na ordem estrita em que aparece na documentação.
2. Não insira nenhuma flag, variável de ambiente ou comando intermediário não citado no documento.
3. Se o comando terminar com sucesso e cumprir a finalidade descrita, classifique como **"Sem ajuste"**.
4. Se o comando falhar (código diferente de 0, erro de dependência, falta de ferramenta do sistema operacional), registre como **"Com ajuste"** e anote:
   - A mensagem de erro original;
   - O comando corretivo ou ajuste manual necessário para contornar a falha e prosseguir;
   - Se o ajuste decorre de um pré-requisito omitido na documentação.

##### Cálculo do valor
Proporção = (passos reproduzidos sem ajuste ÷ total de passos testados) × 100.

##### Arquivos de dados brutos
- Registro textual de execução de todos os passos: `dados/fase-04/brutos/M3.3.2_log_reproducao_passos.txt`
- Tabela com passos, status e justificativa de ajustes: `dados/fase-04/brutos/M3.3.2_passos_ajustes.csv`

---

#### M3.3.3 — Implantação com Docker

- **Questão respondida:** Q3.3 (Instalabilidade).
- **Hipótese:** H3.3.3 (Confirmada se = 4 de 4 verificações aprovadas).
- **Links:** [Ficha da métrica](../fase-02/gqm-flexibilidade.md#m333--implantação-com-docker) | [Faixa de pontuação](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3).

##### Pré-condições
1. Docker Engine e CLI instalados na máquina do avaliador.
2. Repositório no commit `e1b7aac`, contendo `Dockerfile` e `docker-compose.yml` originais.
3. Nenhuma outra aplicação utilizando a porta 3000 no host.

##### Passo a passo das 4 verificações

###### Verificação 1: Construção da imagem Docker
Execute a compilação a partir do `Dockerfile` da raiz sem parâmetros adicionais, cronometrando a execução:
```bash
time docker build -t excalidraw-avaliacao .
```
- **Critério de sucesso:** O comando deve retornar código de saída 0 e a imagem `excalidraw-avaliacao` deve constar na saída de `docker images`.

###### Verificação 2: Inicialização do contêiner
Inicie o contêiner mapeando a porta 3000 do host para a porta 80 do contêiner (onde o nginx roda):
```bash
docker run -d --name excalidraw-avaliacao-teste -p 3000:80 excalidraw-avaliacao
```
- **Critério de sucesso:** O contêiner deve ser criado e mantido no estado executando (`Up`) na listagem de `docker ps`.

###### Verificação 3: Verificação de saúde (*healthcheck*)
O `Dockerfile` declara uma instrução `HEALTHCHECK`. Aguarde 35 segundos (tempo de inicialização e intervalo da checagem) e inspecione o estado:
```bash
docker inspect --format='{{json .State.Health.Status}}' excalidraw-avaliacao-teste
```
- **Critério de sucesso:** A saída do comando deve ser exatamente `"healthy"`.

###### Verificação 4: Acesso e operação no editor
Abra o navegador em `http://localhost:3000`:
- **Critério de sucesso:** A página deve carregar o editor completamente e permitir desenhar um elemento gráfico (ex.: um losango), sem erros visíveis ou de console.

##### Finalização e limpeza
Após registrar as evidências, remova o contêiner de teste:
```bash
docker rm -f excalidraw-avaliacao-teste
```

##### Cálculo do valor
Proporção = (verificações aprovadas ÷ 4) × 100.

##### Arquivos de dados brutos
- Log da construção e execução do Docker: `dados/fase-04/brutos/M3.3.3_docker_deploy.log`
- Captura de tela do editor em execução no navegador: `dados/fase-04/brutos/M3.3.3_editor_docker.png`
- Tabela de conferência das 4 verificações: `dados/fase-04/brutos/M3.3.3_verificacoes_docker.csv`

---

### 3.4 Substituibilidade (Q3.4)

#### M3.4.1 — Formatos de exportação abertos disponíveis

- **Questão respondida:** Q3.4 (Substituibilidade).
- **Hipótese:** H3.4.1 (Confirmada se ≥ 3 formatos abertos).
- **Links:** [Ficha da métrica](../fase-02/gqm-flexibilidade.md#m341--formatos-de-exportação-abertos-disponíveis) | [Faixa de pontuação](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3).

##### Pré-condições
1. Aplicação web em execução local ou ambiente de teste.
2. Acesso ao código-fonte da biblioteca em `packages/excalidraw/scene/export.ts`.

##### Passo a passo
1. Acesse o editor no navegador e crie um desenho simples com uma forma e um texto.
2. Inspecione o menu principal superior esquerdo e o diálogo de exportação (`Ctrl + Shift + E`).
3. Identifique todos os formatos de exportação/salvamento diretamente oferecidos pela interface:
   - Formato de documento nativo: `.excalidraw` (estrutura JSON aberta);
   - Formatos gráficos de exportação: PNG (Portable Network Graphics) e SVG (Scalable Vector Graphics).
4. Verifique no código-fonte em `packages/excalidraw/scene/export.ts` as funções públicas fornecidas para desenvolvedores:
   - `exportToCanvas`
   - `exportToBlob`
   - `exportToSvg`
5. Para cada formato identificado, verifique se atende ao conceito de formato aberto: possuir especificação técnica pública (W3C para PNG e SVG, ECMA-404 para JSON), independente de fornecedor único e que viabilize a leitura por ferramentas de terceiros sem cobrança de royalties.

##### Cálculo do valor
Contagem direta da quantidade de formatos abertos oferecidos pelo software (número inteiro).

##### Arquivos de dados brutos
- Captura de tela do modal de exportação: `dados/fase-04/brutos/M3.4.1_dialogo_exportacao.png`
- Tabela com formatos identificados, tipo MIME e especificação aberta de referência: `dados/fase-04/brutos/M3.4.1_catalogo_formatos.csv`

---

#### M3.4.2 — Proporção de elementos preservados na exportação e reimportação

- **Questão respondida:** Q3.4 (Substituibilidade).
- **Hipótese:** H3.4.2 (Confirmada se ≥ 95% de preservação em cada formato).
- **Links:** [Ficha da métrica](../fase-02/gqm-flexibilidade.md#m342--proporção-de-elementos-preservados-na-exportação-e-reimportação) | [Faixa de pontuação](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3).

##### Pré-condições
1. Aplicação web em execução.
2. Arquivo da **cena de referência** em `dados/fase-03/massa-de-dados/cena_referencia.excalidraw`, gerado por `scripts/gerar_massa_dados.py` (ou com `python scripts/gerar_massa_dados.py --so-referencia`), contendo os 10 tipos de elementos da Fase 02 (retângulo, elipse, losango, seta, linha, desenho livre, texto solto, texto dentro de forma, imagem e moldura).
3. Script automatizado de conferência de integridade de elementos (`scripts/compara_elementos.py`).

##### Passo a passo
1. Abra o arquivo `dados/fase-03/massa-de-dados/cena_referencia.excalidraw` no editor do Excalidraw.
2. **Exportação nos 3 formatos suportados:**
   - **Arquivo 1:** Menu → **Salvar no disco** → salva como `export_referencia.excalidraw`.
   - **Arquivo 2:** `Ctrl + Shift + E` → certifique-se de que a opção de embutir metadados da cena esteja marcada (*Embed scene data*) → exporte como `export_referencia.png`.
   - **Arquivo 3:** `Ctrl + Shift + E` → certifique-se de que a opção de embutir metadados da cena esteja marcada (*Embed scene data*) → exporte como `export_referencia.svg`.
3. **Reimportação e salvamento:**
   - Limpe o editor (`Ctrl + A` → `Delete`).
   - Arraste `export_referencia.excalidraw` para o editor. Salve a cena reaberta como `reimport_excalidraw.excalidraw`.
   - Limpe o editor. Arraste `export_referencia.png` para o editor. Salve a cena resultante como `reimport_png.excalidraw`.
   - Limpe o editor. Arraste `export_referencia.svg` para o editor. Salve a cena resultante como `reimport_svg.excalidraw`.
   - Mova os três arquivos salvos para `dados/fase-04/brutos/`.
4. **Comparação automatizada:**
   Execute o script de conferência comparando a cena original contra cada uma das três cenas reimportadas:
   ```bash
   python scripts/compara_elementos.py \
     --original dados/fase-03/massa-de-dados/cena_referencia.excalidraw \
     --reimportados \
       dados/fase-04/brutos/reimport_excalidraw.excalidraw \
       dados/fase-04/brutos/reimport_png.excalidraw \
       dados/fase-04/brutos/reimport_svg.excalidraw
   ```
5. **Critério de elemento preservado:**
   Um elemento é considerado íntegro se mantiver idênticos: tipo (`type`), coordenadas e dimensões (`x, y, width, height` com tolerância de arredondamento de até 0,01 pixel), estilo visual (`strokeColor, backgroundColor, fillStyle, strokeWidth`) e conteúdo textual (`text`).

##### Cálculo do valor
Para cada um dos 3 formatos:
Preservação = (elementos preservados ÷ total de elementos da cena original) × 100.

A pontuação final da métrica em [Níveis de pontuação](../fase-02/pontuacao-julgamento.md) é a média aritmética das pontuações dos três formatos.

##### Arquivos de dados brutos
- Pacote com os arquivos exportados e reimportados: `dados/fase-04/brutos/M3.4.2_arquivos_reimportados.zip`
- Relatório em formato JSON detalhando elementos comparados: `dados/fase-04/brutos/M3.4.2_relatorio_preservacao.json`
- Tabela resumo das proporções por formato: `dados/fase-04/brutos/M3.4.2_preservacao_formatos.csv`
- Gravação de tela do ciclo de exportação e reimportação: `dados/fase-04/brutos/M3.4.2_gravacao_reimportacao.mp4`

---

#### M3.4.3 — Proporção dos campos do formato `.excalidraw` documentados

- **Questão respondida:** Q3.4 (Substituibilidade).
- **Hipótese:** H3.4.3 (Confirmada se < 60% dos campos estiverem documentados).
- **Links:** [Ficha da métrica](../fase-02/gqm-flexibilidade.md#m343--proporção-dos-campos-do-formato-excalidraw-documentados) | [Faixa de pontuação](../fase-02/pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3).

##### Pré-condições
1. Arquivo `cena_referencia.excalidraw` em `dados/fase-03/massa-de-dados/cena_referencia.excalidraw`.
2. Arquivo de documentação técnica do formato: `dev-docs/docs/codebase/json-schema.mdx` no commit avaliado.

##### Passo a passo
1. Execute o comando extrator para listar todas as chaves contidas no JSON (nível raiz, `appState` e todas as propriedades que aparecem em qualquer objeto da lista `elements`):
   ```bash
   node -e "
     const fs = require('fs');
     const data = JSON.parse(fs.readFileSync('dados/fase-03/massa-de-dados/cena_referencia.excalidraw', 'utf8'));
     const rootKeys = Object.keys(data);
     const elementKeys = new Set();
     (data.elements || []).forEach(el => Object.keys(el).forEach(k => elementKeys.add(k)));
     const appStateKeys = data.appState ? Object.keys(data.appState) : [];
     const total = Array.from(new Set([...rootKeys, ...elementKeys, ...appStateKeys])).sort();
     fs.mkdirSync('dados/fase-04/brutos', { recursive: true });
     fs.writeFileSync('dados/fase-04/brutos/M3.4.3_campos_encontrados.json', JSON.stringify(total, null, 2));
     console.log('Total de campos distintos encontrados:', total.length);
   "
   ```
2. Abra o arquivo de documentação do formato (`dev-docs/docs/codebase/json-schema.mdx`).
3. Para cada campo listado em `M3.4.3_campos_encontrados.json`, verifique se o termo está citado com sua descrição ou tipo correspondente no documento.
4. Classifique cada campo na planilha como "Documentado" ou "Não documentado".
5. Verifique se existe no repositório um esquema formal validável por máquina (arquivo JSON Schema `.json`).

##### Cálculo do valor
Proporção = (campos documentados ÷ total de campos distintos encontrados) × 100.

##### Arquivos de dados brutos
- Lista JSON de campos extraídos da cena real: `dados/fase-04/brutos/M3.4.3_campos_encontrados.json`
- Planilha de auditoria campo a campo: `dados/fase-04/brutos/M3.4.3_conferencia_campos.csv`
- Log do script de extração: `dados/fase-04/brutos/M3.4.3_extracao_campos.log`

---

## 4. Formulário padrão de coleta manual para o avaliador

Para as medições manuais ou que envolvem interface de usuário (M3.1.2, M3.1.3, M3.2.1, M3.2.2, M3.2.3, M3.3.2, M3.4.1 e M3.4.2), o avaliador deve preencher e anexar o formulário padronizado abaixo junto ao repositório de dados brutos da Fase 04:

```markdown
# Formulário de Coleta Manual — Fase 04

- **Código da Métrica:** M3.X.X
- **Nome da Métrica:** [Nome da métrica]
- **Data e Hora de Início:** AAAA-MM-DD HH:MM
- **Data e Hora de Término:** AAAA-MM-DD HH:MM
- **Avaliador Responsável:** Nome Completo (@usuarioGithub)
- **Máquina / Dispositivo:** [Modelo, processador, memória RAM]
- **Sistema Operacional:** [Ex.: Ubuntu 24.04 LTS / Windows 11 23H2 / iPadOS 17.5]
- **Navegador e Versão:** [Ex.: Google Chrome 130.0.6723.70 (64 bits)]
- **Condições de Rede:** [Conectado via cabo / Wi-Fi / Modo Offline]
- **Perfil do Navegador:** [Perfil limpo, sem extensões, cache e storage limpos]
- **Arquivo de Gravação de Tela:** dados/fase-04/brutos/M3.X.X_gravacao_...mp4
- **Arquivos de Dados Brutos Gerados:**
  - dados/fase-04/brutos/M3.X.X_...
- **Desvios ou Observações do Método:** [Nenhum / Descrever qualquer eventualidade]
- **Valor Medido Obtido:** [Valor numérico e unidade]
- **Assinatura do Avaliador:** [Nome do avaliador]
```

---

## 5. Rastreabilidade com os critérios da rubrica

| Critério da rubrica | Exigência da rubrica | Atendimento nesta página |
| :--- | :--- | :--- |
| **F3-C1** | Definição clara, precisa e repetível das instruções para o avaliador | Todos os procedimentos detalham pré-condições, comandos exatos copiáveis, saídas esperadas, métodos de cálculo e formulários de identificação. |
| **F3-C8** | Consistência entre as Fases 02 e 03 | Cada uma das 12 métricas preserva exatamente as fórmulas, definições operacionais, hipóteses e escalas fixadas em `docs/fase-02/gqm-flexibilidade.md` e `docs/fase-02/pontuacao-julgamento.md`. |
| **F4-C2** | Repositório de dados brutos e evidências | Especificação explícita de caminhos e nomes de arquivos sob `dados/fase-04/brutos/`, além de vídeos obrigatórios para todas as coletas no navegador. |

---

## Referências

- AULA A07 QSW1 PROC AVAL PRODUTO. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Páginas 18, 19 e 20.
- AULA 08 QSW1 GQM. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Páginas 38, 45, 49, 50 e 51.
- 2026-2 Trabalho final completo v1. Projeto final da disciplina, 05/10/2026. Critérios F3-C1, F3-C8, F4-C1 e F4-C2.
- ISO/IEC 25040:2011. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Evaluation process*.
- Repositório oficial do Excalidraw no commit `e1b7aac` de 18/10/2026.
- [GQM de Flexibilidade (G3)](../fase-02/gqm-flexibilidade.md).
- [Níveis de pontuação e critérios de julgamento](../fase-02/pontuacao-julgamento.md).

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 07/11/2026 | Elaboração do roteiro de instruções das métricas do objetivo G3 (Flexibilidade) | [Gabriel Monteiro](https://github.com/GabrielSMonteiro) | [Letícia Santos](https://github.com/LeticiaSantosss) |
| 1.1 | 08/11/2026 | Alinhamento dos caminhos da massa de dados e comandos de geração com scripts/gerar_massa_dados.py | [Gabriel Monteiro](https://github.com/GabrielSMonteiro) | [Gabriel Santos](https://github.com/gabriel-nitro) |
