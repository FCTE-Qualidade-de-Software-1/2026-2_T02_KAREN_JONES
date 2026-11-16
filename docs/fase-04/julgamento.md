---
sidebar_position: 5
title: "Julgamento Final e Relações entre Características"
description: Julgamento consolidado de G1, G2 e G3, coerência com o propósito da Fase 01, relações entre características com evidências e limitações, limites de validade e conclusão ligada à ação de melhoria.
---

import Link from '@docusaurus/Link';

# Julgamento Final e Relações entre Características

## Introdução

Esta página consolida o julgamento final da qualidade do Excalidraw (commit `e1b7aacb356a492aa1e0fc6eb57b8896124027f0`) a partir dos resultados obtidos em Manutenibilidade (G1), Confiabilidade (G2) e Flexibilidade (G3), com o objetivo de aplicar os critérios da Fase 02, verificar a coerência com o propósito da Fase 01, discutir as relações entre as características e encaminhar as conclusões com a ação de melhoria selecionada.

## Metodologia

O julgamento aplica diretamente a regra de agregação em duas etapas e a condição de atendimento definidas nos [níveis de pontuação e critérios de julgamento](../fase-02/pontuacao-julgamento.md#6-agregação-da-métrica-à-característica), baseadas em Heitlager, Kuipers e Visser [[1, p. 8]](#ref-1) e em Baggen, Schill e Visser [[2, p. 3]](#ref-2). Conforme o método adotado, não se calcula uma nota única para o produto, mantendo o julgamento por característica para preservar a rastreabilidade até as subcaracterísticas e métricas [[1, p. 8]](#ref-1). Os valores de G1 partem dos consolidados da [#115](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/pull/173), os de G2 partem da análise da [#116](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/pull/176) e os de G3 partem do relatório de [resultados de Flexibilidade](./resultados-g3-flexibilidade.md), integrados com a proposta de melhoria da [#118](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/pull/175).

---

## 1. Julgamento por Característica e Síntese do Produto

A Tabela 1 reúne as médias por questão, o nível obtido em cada característica e o julgamento final segundo o critério da Fase 02 (nível `o` ou melhor na característica e nenhuma questão em `--`).

<p className="tabela-titulo">Tabela 1: Julgamento consolidado das três características avaliadas</p>

| Característica (Objetivo) | Questões e Médias (1 a 5) | Média Geral | Nível | Julgamento | Condição Determinante |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Manutenibilidade (G1)** | Q1.1 (`3,3`, `o`), Q1.2 (`1,5`, `--`), Q1.3 (`3,0`, `o`), Q1.4 (`3,0`, `o`), Q1.5 (`3,7`, `+`) | **2,9** | `o` | **Não atende** | Possui questão no nível `--` (Q1.2: Reusabilidade) |
| **Confiabilidade (G2)** | Q2.1 (`3,0`, `o`), Q2.2 (`4,5`, `+`), Q2.3 (`4,0`, `+`), Q2.4 (`4,0`, `+`) | **3,9** | `+` | **Atende** | Nível `+` e menor questão em `o` (Q2.1) |
| **Flexibilidade (G3)** | Q3.1 (`4,0`, `+`), Q3.2 (`4,3`, `+`), Q3.3 (`3,7`, `+`), Q3.4 (`3,7`, `+`) | **3,9** | `+` | **Atende** | Nível `+` e todas as questões em `+` |

<p className="tabela-fonte">Fonte: [Luiz Henrique Soares](https://github.com/luizh-gsoares), 2026.</p>

**Síntese do produto:** Seguindo a regra de não colapsar as características em um número único [[1, p. 8]](#ref-1), o Excalidraw **atende** aos critérios de qualidade sob a ótica de uso e interoperabilidade (Confiabilidade e Flexibilidade no nível `+`), mas **não atende** em Manutenibilidade devido ao bloqueio da subcaracterística de Reusabilidade (`Q1.2` em `--`), provocado pelo alto acoplamento dos pacotes de base com React e navegador (`M1.2.1` em `69,07%`, `--`) e pela documentação parcial da interface pública (`M1.2.2` em `57,69%`, `-`).

---

## 2. Coerência com o Propósito, o Uso Pretendido e o Requisitante

Na Fase 01, a equipe Karen Jones assumiu o papel de **requisitante** como equipe independente de garantia da qualidade (QA), com o objetivo declarado de **indicar pontos para melhoria no produto**, sem finalidade de certificação ou comparação com concorrentes, conforme o [propósito da avaliação](../fase-01/proposito-avaliacao.md#2-objetivo-da-avaliação). A Tabela 2 mostra como os resultados obtidos atendem diretamente às decisões previstas naquele documento.

<p className="tabela-titulo">Tabela 2: Coerência dos resultados com o uso pretendido e decisões apoiadas</p>

| Decisão Prevista na Fase 01 | Parte Interessada | Evidência Entregue pelos Resultados da Fase 04 |
| :--- | :--- | :--- |
| Priorizar refatorações no código | Mantenedores do projeto | Mapeamento de 4 pares de pacotes em ciclo (`M1.1.1`), `69,07%` de dependência de React/navegador nos pacotes de base (`M1.2.1`), `6,54%` de código em complexidade muito alta (`M1.3.1`) e `65,75%` de PRs alterando arquivos extensos (`M1.4.3`). |
| Escolher onde contribuir | Contribuidores externos | Identificação de `55,48%` dos PRs sem aprovação de terceiro (`M2.1.3`), lacunas de validação para entradas JSON malformadas (`M2.3.1`) e `73,1%` dos campos do formato `.excalidraw` sem documentação (`M3.4.3`). |
| Adotar ou manter o uso da ferramenta | Equipes e organizações | Confirmação de uso *offline* completo (`10/10` em `M2.2.1`), zero domínios externos indispensáveis (`M2.2.2`), tolerância à queda de colaboração (`5/5` em `M2.3.2`), reabertura fiel desde a `v0.15.0` (`7/7` em `M2.4.2`) e suporte a toque/caneta (`10/10` em `M3.1.3`). |
| Escolher a ação de melhoria da Fase 04 | Equipe avaliadora | Comparação objetiva das métricas em `-` e `--` que levou à seleção da documentação de `ExcalidrawProps` (`M1.2.2`) na [#118](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/pull/175), por ser a única intervenção pequena capaz de fazer G1 atender. |
| Avaliar a execução do método SQuaRE | Professores e equipe | Rastreabilidade ponta a ponta entre requisitos da Fase 01, fichas GQM e réguas da Fase 02, instruções da Fase 03 e evidências brutas e consolidadas da Fase 04. |

<p className="tabela-fonte">Fonte: [Luiz Henrique Soares](https://github.com/luizh-gsoares), 2026.</p>

---

## 3. Relações entre as Características

A análise conjunta das três características revela convergências sustentadas pelas medições empíricas e casos em que os dados não autorizam estabelecer relação causal.

### 3.1 Relações sustentadas por evidências

- **Manutenibilidade (`Q1.1`, `Q1.2`) e Flexibilidade (`Q3.1`, `Q3.3`):** o acoplamento estrutural medido em G1 aparece refletido nos atritos de integração e empacotamento medidos em G3. Em Manutenibilidade, foram encontrados `4` pares de pacotes em ciclo (`M1.1.1`, `-`) e `69,07%` dos arquivos de base dependentes de React ou do navegador (`M1.2.1`, `--`). Em Flexibilidade, o empacotamento local do pacote falhou na instalação e atualização em todos os três gerenciadores (`M3.3.1`, `33,3%`, `-`) por dependência não resolvida do subpacote interno `@excalidraw/common`, e a integração com Next.js falhou no React 17 e no React 18 (`M3.1.2`, `66,7%`, `o`) por acoplamento ao *runtime* e aos *hooks* do React 19.
- **Manutenibilidade (`Q1.2`), Flexibilidade (`Q3.4`) e Confiabilidade (`Q2.3`):** a deficiência documental da interface pública em G1 (`M1.2.2` em `57,69%`, `-`) converge com a omissão de `38` dos `52` campos do formato `.excalidraw` na documentação técnica em G3 (`M3.4.3` em `26,9%`, `-`) e com a ausência de um esquema JSON formal (`schema.json`). Na execução, essa falta de especificação formal acompanha a falha de validação de entrada em G2 (`M2.3.1` em `77,78%`, `o`): arquivos JSON sintaticamente válidos, mas com campos obrigatórios ausentes (`invalido_05`) ou coordenadas não numéricas (`invalido_06`), passam sem mensagem de erro e chegam a causar tela branca ao desenhar.
- **Confiabilidade (`Q2.4`) e Flexibilidade (`Q3.4`):** as duas características convergem positivamente na consistência de serialização do formato `.excalidraw`. Tanto a reimportação entre formatos abertos em G3 (`M3.4.2`, `100,0%`, `++`) quanto a reabertura de arquivos de versões anteriores (`v0.15.0` a `v0.18.0`) e PNGs embutidos em G2 (`M2.4.2`, `7/7`, `++`) preservaram integralmente os elementos esperados.
- **Manutenibilidade (`Q1.5`) e Confiabilidade (`Q2.1`):** G1 registra `99,12%` dos PRs com execuções automáticas antes da integração (`M1.5.3`, `++`) e `76,74%` de cobertura de linhas (`M1.5.1`, `o`). Em G2, porém, apenas `44,52%` dos PRs tiveram revisão humana `APPROVED` de terceiro (`M2.1.3`, `-`), e `51,37%` das contribuições integradas na janela foram correções (`M2.1.1`, `o`), com `62` de `75` concentradas no escopo `editor`. Isso indica que a automação de CI elevada convive com alta proporção de correções e baixa revisão humana obrigatória.

### 3.2 Limitações das relações e casos sem relação estabelecida

- **Recortes distintos de PRs:** as métricas de histórico em G1 (`M1.4.1`, `M1.4.3`, `M1.5.3`) e em G2 (`M2.1.1` a `M2.1.3`) consultam a mesma janela de seis meses, mas aplicam filtros e exclusões próprios (por exemplo, exclusão de robôs e traduções em `M2.1.1`/`M2.1.3` e recorte de PRs com *issue* vinculada em `M2.1.2`). Por isso, a coexistência entre `99,12%` de CI e `51,37%` de correções mostra associação descritiva no processo, não causalidade isolada.
- **Desempenho em cena densa (`M3.2.1`, `M3.2.2`) e Confiabilidade (`Q2.1`–`Q2.4`):** os dados não permitem estabelecer relação entre a queda de fluidez acima de `5.000` elementos (`20` FPS e `12` FPS em `M3.2.2`) e a ausência de falhas ou recuperabilidade em G2, pois as medições de G2 usaram cenas de referência pequenas (`10` elementos) e as medições de G3 não testaram perda de estado ou erro sob estresse de volume.
- **Uso *offline* (`M2.2.1`) e acoplamento de pacotes (`M1.2.1`):** a dependência elevada de APIs do navegador nos pacotes de base prejudica a reusabilidade em ambientes sem DOM (`Q1.2`), mas não prejudica a disponibilidade *offline* na aplicação web (`M2.2.1`, `10/10`), que justamente se apoia em recursos do navegador (*service worker* e armazenamento local). Trata-se de objetivos distintos entre integradores de biblioteca e usuários finais da aplicação web.

---

## 4. Limites de Validade dos Resultados

Conforme registrado na [seção 8 dos critérios da Fase 02](../fase-02/pontuacao-julgamento.md#8-limitações) e nos relatórios de coleta da Fase 04, a validade das conclusões está sujeita aos seguintes limites:

- **Validade temporal:** as medições estáticas e dinâmicas retratam exclusivamente o commit `e1b7aac` (18/10/2026), e as métricas de processo cobrem a janela histórica de 18/04/2026 a 18/10/2026. Evoluções posteriores no repositório oficial podem alterar os valores.
- **Validade de calibração das faixas:** as faixas de Heitlager, Kuipers e Visser usadas foram as publicadas originalmente em 2007 [[1, p. 6-7]](#ref-1), sem recalibração para projetos em TypeScript, e foram reaproveitadas para proporções desejáveis e indesejáveis de G2 e G3, além de limites próprios da equipe em métricas sem referência publicada.
- **Validade de amostragem e rastreabilidade:** em `M2.1.2`, apenas `20` de `75` PRs `fix` (`26,67%`) possuíam vínculo explícito com relato (`closingIssuesReferences`), restringindo a mediana de `7,26` dias a esse subconjunto rastreável. Em `M2.4.2`, o arquivo histórico da `v0.15.0` continha `9` elementos por incompatibilidade prévia daquela versão com o tipo *frame*.
- **Validade de ambiente de teste:** houve desvios operacionais registrados nas coletas manuais (Mozilla Firefox `160.0` em vez de `159.0.1` e contêiner em `127.0.0.1:3001` em G2; uso do Chrome DevTools em `M3.2.1` e `M3.2.2` em G3), sem alteração das regras de cálculo.

---

## 5. Conclusões e Encaminhamento da Ação de Melhoria

A avaliação mostra que o Excalidraw entrega uma experiência confiável e flexível ao usuário final (`G2` e `G3` em `+`, ambas **atendendo**), com destaque para operação *offline*, tolerância à queda de colaboração, reabertura fiel de versões anteriores, suporte a toque/caneta e escalabilidade de persistência. Contudo, o produto **não atende** em Manutenibilidade (`G1` em `o`, `2,9` pontos) por causa da nota `--` em Reusabilidade (`Q1.2`, média `1,5`), além de apresentar pontos de melhoria pontuais em revisão de código (`M2.1.3`), empacotamento local (`M3.3.1`) e documentação do esquema JSON (`M3.4.3`).

Em coerência com o objetivo da Fase 01 de indicar e executar uma melhoria viável dentro do prazo da avaliação, a equipe selecionou na [#118](https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/pull/175) a ação proposta sobre **M1.2.2 (Proporção de propriedades públicas documentadas)**:

- **Ação escolhida (`#118` / `#119`):** criar um modelo técnico padrão (tipo, valor padrão, descrição e exemplo) e documentar as propriedades públicas de `ExcalidrawProps` que estão sem documentação (atualmente `30` de `52` documentadas, `57,69%`, nível `-`).
- **Impacto esperado no julgamento:** ao documentar ao menos `12` das `22` propriedades faltantes, `M1.2.2` sobe para `80,77%` (`+`, 4 pontos), elevando `Q1.2` de `1,5` (`--`) para `2,5` (`-`) e fazendo a média de **G1** subir para `3,1` (`o`) sem nenhuma questão em `--`, o que muda o julgamento da Manutenibilidade de **Não atende** para **Atende**.

---

## Referências

> <Link id="ref-1">1.</Link> HEITLAGER, I.; KUIPERS, T.; VISSER, J. A Practical Model for Measuring Maintainability. In: *6th International Conference on the Quality of Information and Communications Technology (QUATIC 2007)*. IEEE, 2007. p. 30-39. Páginas 5 a 8 da versão dos autores. Disponível em: [https://www.di.uminho.pt/~joost/publications/HeitlagerKuipersVisser-Quatic2007.pdf](https://www.di.uminho.pt/~joost/publications/HeitlagerKuipersVisser-Quatic2007.pdf). Acesso em: 16 nov. 2026.
>
> <Link id="ref-2">2.</Link> BAGGEN, R.; SCHILL, K.; VISSER, J. Standardized Code Quality Benchmarking for Improving Software Maintainability. In: *4th International Workshop on Software Quality and Maintainability (SQM 2010)*, 2010. Página 3. Disponível em: [https://webarchive.di.uminho.pt/wiki.di.uminho.pt/twiki/pub/Personal/Joost/PublicationList/SQM2010-StandardizedCodeQuality.pdf](https://webarchive.di.uminho.pt/wiki.di.uminho.pt/twiki/pub/Personal/Joost/PublicationList/SQM2010-StandardizedCodeQuality.pdf). Acesso em: 16 nov. 2026.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| `1.0` | 16/11/2026 | Consolidação do julgamento final de G1, G2 e G3, coerência com a Fase 01, relações entre características, limites de validade e encaminhamento da ação da #118 | [Luiz Henrique Soares](https://github.com/luizh-gsoares) | |
