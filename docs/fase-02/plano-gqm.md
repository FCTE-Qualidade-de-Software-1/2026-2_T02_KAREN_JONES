---
sidebar_position: 7
title: Plano GQM
description: Plano GQM da avaliação do Excalidraw, com os diagramas da hierarquia de objetivos, questões e métricas de G1, G2 e G3, as hipóteses, as diretrizes de interpretação e a rastreabilidade com a Fase 01
---

# Plano GQM

O Plano GQM reúne em um só lugar os objetivos, as questões, as métricas e as hipóteses da medição, junto com as diretrizes para interpretar os resultados. Ele é a base para definir os procedimentos de coleta e para elaborar os planos de medição e de análise (AULA 08, p. 44).

Esta página não cria nenhum item novo. Ela consolida o que foi definido nas demais páginas da Fase 02:

- os objetivos G1, G2 e G3 vêm dos [objetivos de medição](./estrutura-gqm.md#3-objetivos-de-medição);
- as questões, as hipóteses e as fichas das métricas vêm das páginas de [Manutenibilidade (G1)](./gqm-manutenibilidade.md), [Confiabilidade (G2)](./gqm-confiabilidade.md) e [Flexibilidade (G3)](./gqm-flexibilidade.md);
- as diretrizes de interpretação vêm dos [níveis de pontuação e critérios de julgamento](./pontuacao-julgamento.md).

Os planos de medição e de análise ficam para a Fase 03, como registrado na [divisão entre as Fases 02 e 03](./estrutura-gqm.md#divisão-entre-as-fases-02-e-03).

---

## 1. Como ler os diagramas

O GQM é uma hierarquia de três níveis (AULA 08, p. 8):

| Nível | Elemento | O que representa nesta avaliação |
| :--- | :--- | :--- |
| Conceitual | Objetivo | Uma característica de qualidade da ISO/IEC 25010 escolhida na Fase 01, analisada do ponto de vista dos seus interessados principais. |
| Operacional | Questão | Uma subcaracterística da característica do objetivo. Cada questão caracteriza o produto em relação a ela. |
| Quantitativo | Métrica | Um dado coletado do produto que ajuda a responder a questão. |

*Tabela 1: Níveis do GQM (AULA 08, p. 8).*

A hierarquia é construída de cima para baixo e lida de baixo para cima. Na **definição**, cada objetivo é refinado em questões, e cada questão em métricas. Na **interpretação**, o caminho é o inverso: os valores das métricas respondem às questões, e as respostas das questões são usadas para concluir sobre o objetivo (AULA 08, p. 7 e 8).

As [Figuras 1](#2-g1-manutenibilidade), [2](#3-g2-confiabilidade) e [3](#4-g3-flexibilidade) seguem a mesma legenda:

- **Faixas horizontais:** os três níveis da Tabela 1. A faixa de cima é o nível conceitual, a do meio é o operacional e a de baixo é o quantitativo.
- **Caixa escura no alto:** o objetivo, com a característica avaliada, o propósito, o objeto e o ponto de vista. O texto completo de cada objetivo está nos [objetivos de medição](./estrutura-gqm.md#3-objetivos-de-medição).
- **Caixas escuras do meio:** as questões, com o código e a subcaracterística correspondente.
- **Caixas claras de baixo:** as métricas, com o código e o nome. Cada métrica fica abaixo da questão que responde.
- **Linhas:** ligam cada elemento ao elemento de nível superior que ele detalha.
- **Setas à direita:** o sentido da definição (para baixo) e o da interpretação (para cima).
- **Cores:** azul para G1, verde para G2 e laranja para G3, as mesmas do [modelo de qualidade](../fase-01/modelo-de-qualidade.md#representação-gráfica-do-modelo) da Fase 01.

Os três diagramas foram desenhados no próprio Excalidraw, o produto avaliado. Para editar um deles, abra o arquivo correspondente ([`gqm-g1.excalidraw`](../images/gqm-g1.excalidraw), [`gqm-g2.excalidraw`](../images/gqm-g2.excalidraw) ou [`gqm-g3.excalidraw`](../images/gqm-g3.excalidraw)) em [excalidraw.com](https://excalidraw.com/) e exporte o PNG de novo com a opção de incluir a cena ativada. O PNG publicado também guarda a cena, então pode ser aberto direto no editor.

Os códigos seguem a posição na hierarquia. Q1.3 é a terceira questão de G1, e M1.3.2 é a segunda métrica de Q1.3. A Tabela 2 resume o tamanho de cada objetivo.

| Objetivo | Característica | Questões | Métricas | Detalhamento |
| :--- | :--- | :---: | :---: | :--- |
| G1 | Manutenibilidade | 5 | 14 | [GQM de Manutenibilidade](./gqm-manutenibilidade.md) |
| G2 | Confiabilidade | 4 | 10 | [GQM de Confiabilidade](./gqm-confiabilidade.md) |
| G3 | Flexibilidade | 4 | 12 | [GQM de Flexibilidade](./gqm-flexibilidade.md) |
| **Total** | | **13** | **36** | |

*Tabela 2: Quantidade de questões e de métricas por objetivo.*

---

## 2. G1: Manutenibilidade

**Objetivo:** analisar o código-fonte do Excalidraw (biblioteca, aplicação web e pacotes auxiliares), seus testes, sua documentação para desenvolvedores e o histórico público de alterações, para o propósito de entender, com respeito à Manutenibilidade, do ponto de vista de mantenedores e contribuidores do projeto ([G1 nos objetivos de medição](./estrutura-gqm.md#g1--manutenibilidade)).

[![Diagrama em três níveis. Nível conceitual: objetivo G1, entender a manutenibilidade do código-fonte, dos testes e do histórico do ponto de vista de mantenedores e contribuidores do projeto. Nível operacional: 5 questões, uma por subcaracterística. Nível quantitativo: 14 métricas. Q1.1 (Modularidade) é respondida por M1.1.1, M1.1.2, M1.1.3. Q1.2 (Reusabilidade) é respondida por M1.2.1, M1.2.2. Q1.3 (Analisabilidade) é respondida por M1.3.1, M1.3.2, M1.3.3. Q1.4 (Modificabilidade) é respondida por M1.4.1, M1.4.2, M1.4.3. Q1.5 (Testabilidade) é respondida por M1.5.1, M1.5.2, M1.5.3.](../images/gqm-g1.png)](../images/gqm-g1.png)

*Figura 1: Hierarquia GQM do objetivo G1 (Manutenibilidade), com 5 questões e 14 métricas. Clique na figura para abri-la em tamanho real.*

A [Figura 1](#2-g1-manutenibilidade) mostra a hierarquia completa de G1. A Tabela 3 traz a pergunta e a hipótese de cada questão. A ficha de cada métrica, com definição, cálculo, fonte, coleta e critério de interpretação, está no link do código da métrica.

| Questão | Pergunta | Hipótese | Métricas |
| :--- | :--- | :--- | :--- |
| [Q1.1](./gqm-manutenibilidade.md#3-q11--modularidade) Modularidade | Em que medida o código está dividido em pacotes independentes, com dependências em uma única direção? | não há ciclos de dependência em tempo de execução entre os pacotes, e nenhum pacote importa código da aplicação web. A biblioteca `excalidraw` é o pacote que mais recebe dependências dos demais. | [M1.1.1](./gqm-manutenibilidade.md#m111--ciclos-de-dependência-entre-pacotes) Ciclos de dependência entre pacotes<br/>[M1.1.2](./gqm-manutenibilidade.md#m112--importações-que-violam-a-direção-declarada) Importações que violam a direção declarada<br/>[M1.1.3](./gqm-manutenibilidade.md#m113--acoplamento-e-instabilidade-de-cada-pacote) Acoplamento e instabilidade de cada pacote |
| [Q1.2](./gqm-manutenibilidade.md#4-q12--reusabilidade) Reusabilidade | Os pacotes podem ser usados fora do editor, e a interface pública da biblioteca está documentada para quem vai reutilizá-la? | os pacotes `math` e `utils` não dependem de React nem de recursos do navegador. A maior parte das propriedades públicas da biblioteca está documentada, mas parte delas só aparece nos tipos do código. | [M1.2.1](./gqm-manutenibilidade.md#m121--arquivos-de-pacotes-de-base-com-dependência-de-react-ou-do-navegador) Arquivos de pacotes de base com dependência de React ou do navegador<br/>[M1.2.2](./gqm-manutenibilidade.md#m122--proporção-de-propriedades-públicas-documentadas) Proporção de propriedades públicas documentadas |
| [Q1.3](./gqm-manutenibilidade.md#5-q13--analisabilidade) Analisabilidade | O código pode ser entendido com facilidade, com apoio de documentação e de verificações automáticas? | a maior parte das funções tem complexidade baixa, e as de complexidade alta se concentram em poucos arquivos, principalmente no componente principal do editor. A documentação para desenvolvedores cobre a contribuição e a preparação do ambiente. Lint, formatação e verificação de tipos são executados automaticamente. | [M1.3.1](./gqm-manutenibilidade.md#m131--perfil-de-risco-de-complexidade-das-funções) Perfil de risco de complexidade das funções<br/>[M1.3.2](./gqm-manutenibilidade.md#m132--cobertura-da-documentação-para-desenvolvedores) Cobertura da documentação para desenvolvedores<br/>[M1.3.3](./gqm-manutenibilidade.md#m133--verificações-estáticas-executadas-automaticamente) Verificações estáticas executadas automaticamente |
| [Q1.4](./gqm-manutenibilidade.md#6-q14--modificabilidade) Modificabilidade | As alterações no código ficam restritas a poucas partes, ou tendem a se espalhar e a passar por arquivos que concentram responsabilidades demais? | a maioria das contribuições altera poucos arquivos. Há poucos arquivos muito extensos, mas eles são alterados por uma parte relevante das contribuições, o que torna essas alterações mais arriscadas. | [M1.4.1](./gqm-manutenibilidade.md#m141--mediana-de-arquivos-de-produção-alterados-por-contribuição) Mediana de arquivos de produção alterados por contribuição<br/>[M1.4.2](./gqm-manutenibilidade.md#m142--arquivos-de-produção-extensos) Arquivos de produção extensos<br/>[M1.4.3](./gqm-manutenibilidade.md#m143--proporção-de-contribuições-que-alteram-arquivos-extensos) Proporção de contribuições que alteram arquivos extensos |
| [Q1.5](./gqm-manutenibilidade.md#7-q15--testabilidade) Testabilidade | O código pode ser verificado por testes automatizados, em diferentes níveis, executados a cada alteração? | a biblioteca tem cobertura de testes maior do que a aplicação web. Predominam testes unitários e de integração. Os testes rodam em toda contribuição antes da integração. | [M1.5.1](./gqm-manutenibilidade.md#m151--cobertura-de-linhas-por-pacote) Cobertura de linhas por pacote<br/>[M1.5.2](./gqm-manutenibilidade.md#m152--distribuição-dos-testes-por-nível) Distribuição dos testes por nível<br/>[M1.5.3](./gqm-manutenibilidade.md#m153--proporção-de-contribuições-com-testes-executados-antes-da-integração) Proporção de contribuições com testes executados antes da integração |

*Tabela 3: Questões, hipóteses e métricas de G1.*

---

## 3. G2: Confiabilidade

**Objetivo:** analisar o editor, a aplicação web e os mecanismos de colaboração e de salvamento no navegador, além do histórico público de defeitos relatados, para o propósito de entender, com respeito à Confiabilidade, do ponto de vista de usuários finais ([G2 nos objetivos de medição](./estrutura-gqm.md#g2--confiabilidade)).

[![Diagrama em três níveis. Nível conceitual: objetivo G2, entender a confiabilidade do editor, da colaboração e do salvamento do ponto de vista de usuários finais. Nível operacional: 4 questões, uma por subcaracterística. Nível quantitativo: 10 métricas. Q2.1 (Ausência de falhas) é respondida por M2.1.1, M2.1.2, M2.1.3. Q2.2 (Disponibilidade) é respondida por M2.2.1, M2.2.2. Q2.3 (Tolerância a falhas) é respondida por M2.3.1, M2.3.2. Q2.4 (Recuperabilidade) é respondida por M2.4.1, M2.4.2, M2.4.3.](../images/gqm-g2.png)](../images/gqm-g2.png)

*Figura 2: Hierarquia GQM do objetivo G2 (Confiabilidade), com 4 questões e 10 métricas. Clique na figura para abri-la em tamanho real.*

A [Figura 2](#3-g2-confiabilidade) mostra a hierarquia completa de G2, e a Tabela 4 detalha cada questão. A subcaracterística Ausência de falhas corresponde à Maturidade da edição de 2011 da norma, nome usado na Fase 01.

| Questão | Pergunta | Hipótese | Métricas |
| :--- | :--- | :--- | :--- |
| [Q2.1](./gqm-confiabilidade.md#3-q21--ausência-de-falhas) Ausência de falhas | O projeto evita que falhas cheguem ao usuário e trata de forma organizada os defeitos que chegam? | as correções são uma parte relevante das contribuições integradas, compatível com um projeto muito usado. Os defeitos relatados são corrigidos em poucas semanas. Toda contribuição passa por verificações automáticas e por revisão de outra pessoa antes da integração. | [M2.1.1](./gqm-confiabilidade.md#m211--proporção-de-correções-entre-as-contribuições-integradas) Proporção de correções entre as contribuições integradas<br/>[M2.1.2](./gqm-confiabilidade.md#m212--mediana-do-tempo-entre-o-relato-e-a-correção) Mediana do tempo entre o relato e a correção<br/>[M2.1.3](./gqm-confiabilidade.md#m213--proporção-de-contribuições-revisadas-antes-da-integração) Proporção de contribuições revisadas antes da integração |
| [Q2.2](./gqm-confiabilidade.md#4-q22--disponibilidade) Disponibilidade | O editor continua disponível para o usuário sem conexão e sem depender de serviços externos? | depois do primeiro carregamento, o editor funciona sem conexão. A colaboração em tempo real e o compartilhamento por link não funcionam sem conexão. O editor local carrega poucos recursos de servidores externos, e nenhum deles é indispensável para desenhar. | [M2.2.1](./gqm-confiabilidade.md#m221--proporção-de-funções-essenciais-disponíveis-sem-conexão) Proporção de funções essenciais disponíveis sem conexão<br/>[M2.2.2](./gqm-confiabilidade.md#m222--origens-externas-necessárias-para-o-editor-local) Origens externas necessárias para o editor local |
| [Q2.3](./gqm-confiabilidade.md#5-q23--tolerância-a-falhas) Tolerância a falhas | O editor continua funcionando quando recebe dados inválidos ou quando a conexão com a colaboração falha? | arquivos inválidos ou corrompidos são recusados com uma mensagem, sem travar o editor. Se a sessão de colaboração cair, o desenho local continua editável e o usuário é avisado. | [M2.3.1](./gqm-confiabilidade.md#m231--proporção-de-arquivos-inválidos-tratados-com-mensagem) Proporção de arquivos inválidos tratados com mensagem<br/>[M2.3.2](./gqm-confiabilidade.md#m232--continuidade-do-editor-após-falha-da-colaboração) Continuidade do editor após falha da colaboração |
| [Q2.4](./gqm-confiabilidade.md#6-q24--recuperabilidade) Recuperabilidade | O usuário recupera seu trabalho depois de fechar a aplicação, de reabrir arquivos antigos ou de cometer um erro de edição? | ao reabrir a aplicação, o último desenho é restaurado, inclusive depois de um fechamento inesperado. Arquivos salvos na versão atual e em versões anteriores são reabertos sem perda. Desfazer e refazer cobrem as ações de edição do próprio usuário. | [M2.4.1](./gqm-confiabilidade.md#m241--proporção-de-cenários-de-fechamento-com-restauração-do-desenho) Proporção de cenários de fechamento com restauração do desenho<br/>[M2.4.2](./gqm-confiabilidade.md#m242--proporção-de-arquivos-reabertos-sem-perda) Proporção de arquivos reabertos sem perda<br/>[M2.4.3](./gqm-confiabilidade.md#m243--cobertura-de-desfazer-e-refazer) Cobertura de desfazer e refazer |

*Tabela 4: Questões, hipóteses e métricas de G2.*

---

## 4. G3: Flexibilidade

**Objetivo:** analisar a biblioteca `@excalidraw/excalidraw` e a aplicação web, incluindo a interface pública da biblioteca, as instruções de instalação e os formatos de exportação, para o propósito de entender, com respeito à Flexibilidade, do ponto de vista de desenvolvedores que integram a biblioteca em seus sistemas e de equipes de implantação e operação ([G3 nos objetivos de medição](./estrutura-gqm.md#g3--flexibilidade-antiga-portabilidade)).

[![Diagrama em três níveis. Nível conceitual: objetivo G3, entender a flexibilidade da biblioteca e da aplicação web do ponto de vista de integradores e equipes de implantação e operação. Nível operacional: 4 questões, uma por subcaracterística. Nível quantitativo: 12 métricas. Q3.1 (Adaptabilidade) é respondida por M3.1.1, M3.1.2, M3.1.3. Q3.2 (Escalabilidade) é respondida por M3.2.1, M3.2.2, M3.2.3. Q3.3 (Instalabilidade) é respondida por M3.3.1, M3.3.2, M3.3.3. Q3.4 (Substituibilidade) é respondida por M3.4.1, M3.4.2, M3.4.3.](../images/gqm-g3.png)](../images/gqm-g3.png)

*Figura 3: Hierarquia GQM do objetivo G3 (Flexibilidade), com 4 questões e 12 métricas. Clique na figura para abri-la em tamanho real.*

A [Figura 3](#4-g3-flexibilidade) mostra a hierarquia completa de G3, e a Tabela 5 detalha cada questão.

| Questão | Pergunta | Hipótese | Métricas |
| :--- | :--- | :--- | :--- |
| [Q3.1](./gqm-flexibilidade.md#3-q31--adaptabilidade) Adaptabilidade | O Excalidraw pode ser usado em diferentes navegadores, dispositivos e ambientes de integração sem adaptações no código? | a aplicação funciona nas versões recentes dos principais navegadores, mas não em navegadores antigos. A biblioteca aceita mais de uma versão principal de React e precisa ser carregada apenas no navegador quando usada em frameworks com renderização no servidor. O editor aceita toque e caneta. | [M3.1.1](./gqm-flexibilidade.md#m311--cobertura-de-usuários-pelos-navegadores-declarados) Cobertura de usuários pelos navegadores declarados<br/>[M3.1.2](./gqm-flexibilidade.md#m312--proporção-de-ambientes-de-integração-com-sucesso) Proporção de ambientes de integração com sucesso<br/>[M3.1.3](./gqm-flexibilidade.md#m313--proporção-de-ações-de-edição-que-funcionam-por-toque-e-caneta) Proporção de ações de edição que funcionam por toque e caneta |
| [Q3.2](./gqm-flexibilidade.md#4-q32--escalabilidade) Escalabilidade | O editor continua utilizável quando o desenho cresce? | o editor continua utilizável com algumas centenas de elementos, e o desempenho cai de forma perceptível com milhares. Exportar um desenho grande é mais lento do que abri-lo. | [M3.2.1](./gqm-flexibilidade.md#m321--tempo-de-abertura-por-tamanho-de-cena) Tempo de abertura por tamanho de cena<br/>[M3.2.2](./gqm-flexibilidade.md#m322--taxa-de-quadros-durante-a-edição-por-tamanho-de-cena) Taxa de quadros durante a edição por tamanho de cena<br/>[M3.2.3](./gqm-flexibilidade.md#m323--tamanho-máximo-de-cena-salva-e-exportada) Tamanho máximo de cena salva e exportada |
| [Q3.3](./gqm-flexibilidade.md#5-q33--instalabilidade) Instalabilidade | A biblioteca e a aplicação podem ser instaladas, construídas e implantadas seguindo apenas a documentação, em ambientes diferentes? | a biblioteca é instalada com um único comando dos gerenciadores de pacotes usuais. A imagem Docker é construída sem passos manuais adicionais, e as instruções de execução local são suficientes, desde que as versões de ferramentas exigidas sejam respeitadas. | [M3.3.1](./gqm-flexibilidade.md#m331--proporção-de-operações-de-pacote-bem-sucedidas) Proporção de operações de pacote bem-sucedidas<br/>[M3.3.2](./gqm-flexibilidade.md#m332--proporção-de-passos-documentados-reproduzidos-sem-ajuste) Proporção de passos documentados reproduzidos sem ajuste<br/>[M3.3.3](./gqm-flexibilidade.md#m333--implantação-com-docker) Implantação com Docker |
| [Q3.4](./gqm-flexibilidade.md#6-q34--substituibilidade) Substituibilidade | Os desenhos feitos no Excalidraw podem ser levados para outras ferramentas, em formatos abertos e sem perda de conteúdo? | o desenho pode ser exportado em `.excalidraw`, PNG e SVG, e PNG e SVG podem guardar os dados do desenho para reimportação. O formato `.excalidraw` é legível (texto em JSON), mas não tem uma especificação formal publicada. | [M3.4.1](./gqm-flexibilidade.md#m341--formatos-de-exportação-abertos-disponíveis) Formatos de exportação abertos disponíveis<br/>[M3.4.2](./gqm-flexibilidade.md#m342--proporção-de-elementos-preservados-na-exportação-e-reimportação) Proporção de elementos preservados na exportação e reimportação<br/>[M3.4.3](./gqm-flexibilidade.md#m343--proporção-dos-campos-do-formato-excalidraw-documentados) Proporção dos campos do formato `.excalidraw` documentados |

*Tabela 5: Questões, hipóteses e métricas de G3.*

---

## 5. Diretrizes de interpretação

As hipóteses ajudam a interpretar os resultados (AULA 08, p. 34). Cada resultado é lido de duas formas independentes, definidas antes da coleta:

1. **Hipótese.** O valor da métrica confirma ou refuta a hipótese da questão, segundo o critério de interpretação da ficha da métrica. As hipóteses estão nas Tabelas 3, 4 e 5 e vieram das hipóteses de baseline das [abstraction sheets](./abstraction-sheets.md).
2. **Nível de pontuação.** O valor da métrica é convertido em um dos cinco níveis da [escala de pontuação](./pontuacao-julgamento.md#1-escala-de-pontuação), pelas faixas de [G1](./pontuacao-julgamento.md#3-níveis-das-métricas-de-manutenibilidade-g1), [G2](./pontuacao-julgamento.md#4-níveis-das-métricas-de-confiabilidade-g2) e [G3](./pontuacao-julgamento.md#5-níveis-das-métricas-de-flexibilidade-g3).

A interpretação segue o sentido de baixo para cima das figuras:

| Passo | Nível do GQM | O que é feito | Regra |
| :---: | :--- | :--- | :--- |
| 1 | Quantitativo | Cada métrica recebe um nível de pontuação e confirma ou refuta a sua hipótese. | [Seções 3 a 5](./pontuacao-julgamento.md#3-níveis-das-métricas-de-manutenibilidade-g1) e [seção 7.2](./pontuacao-julgamento.md#72-hipóteses) da página de pontuação |
| 2 | Operacional | A questão recebe a média dos níveis das suas métricas. | [Seção 6](./pontuacao-julgamento.md#6-agregação-da-métrica-à-característica) da página de pontuação |
| 3 | Conceitual | A característica do objetivo recebe a média das suas questões e é julgada como *atende*, *não atende* ou *inconclusiva*. | [Seção 7.1](./pontuacao-julgamento.md#71-julgamento-de-cada-característica) da página de pontuação |
| 4 | Todos | Métricas nos dois piores níveis viram pontos de melhoria, rastreáveis até a questão e a subcaracterística. | [Seção 7.3](./pontuacao-julgamento.md#73-pontos-de-melhoria) da página de pontuação |

*Tabela 6: Passos da interpretação, do nível quantitativo ao conceitual.*

Se uma métrica não puder ser coletada, a regra das [métricas não coletadas](./pontuacao-julgamento.md#61-métricas-não-coletadas) define como a questão e a característica são tratadas.

---

## 6. Rastreabilidade com a Fase 01

A Tabela 7 liga cada questão à subcaracterística, aos interessados e aos requisitos de avaliação da Fase 01 de onde ela veio. Os interessados principais são os da [rastreabilidade do modelo de qualidade](../fase-01/modelo-de-qualidade.md#rastreabilidade-entre-subcaracterísticas-interessados-e-artefatos). Os requisitos são os da [estrutura das questões](./estrutura-gqm.md#4-estrutura-das-questões). A ligação de cada requisito com as métricas está na seção de rastreabilidade de [G1](./gqm-manutenibilidade.md#8-rastreabilidade-com-a-fase-01), [G2](./gqm-confiabilidade.md#7-rastreabilidade-com-a-fase-01) e [G3](./gqm-flexibilidade.md#7-rastreabilidade-com-a-fase-01).

| Característica (Fase 01) | Subcaracterística | Interessados principais | Requisitos de avaliação | Questão | Métricas |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [Manutenibilidade](../fase-01/modelo-de-qualidade.md#manutenabilidade) | Modularidade | [Desenvolvedores](../fase-01/interessados.md#2-desenvolvedores-do-projeto); [Mantenedores](../fase-01/interessados.md#3-mantenedores) | [RQ-MAN-01 a 03](../fase-01/requisitos-avaliacao.md#2-requisitos-de-manutenibilidade) | [Q1.1](./gqm-manutenibilidade.md#3-q11--modularidade) | [M1.1.1](./gqm-manutenibilidade.md#m111--ciclos-de-dependência-entre-pacotes), [M1.1.2](./gqm-manutenibilidade.md#m112--importações-que-violam-a-direção-declarada), [M1.1.3](./gqm-manutenibilidade.md#m113--acoplamento-e-instabilidade-de-cada-pacote) |
| [Manutenibilidade](../fase-01/modelo-de-qualidade.md#manutenabilidade) | Reusabilidade | [Integradores](../fase-01/interessados.md#5-desenvolvedores-que-integram-a-biblioteca) | [RQ-MAN-04 e 05](../fase-01/requisitos-avaliacao.md#2-requisitos-de-manutenibilidade) | [Q1.2](./gqm-manutenibilidade.md#4-q12--reusabilidade) | [M1.2.1](./gqm-manutenibilidade.md#m121--arquivos-de-pacotes-de-base-com-dependência-de-react-ou-do-navegador), [M1.2.2](./gqm-manutenibilidade.md#m122--proporção-de-propriedades-públicas-documentadas) |
| [Manutenibilidade](../fase-01/modelo-de-qualidade.md#manutenabilidade) | Analisabilidade | [Contribuidores](../fase-01/interessados.md#4-contribuidores-open-source); [Desenvolvedores](../fase-01/interessados.md#2-desenvolvedores-do-projeto) | [RQ-MAN-06 a 08](../fase-01/requisitos-avaliacao.md#2-requisitos-de-manutenibilidade) | [Q1.3](./gqm-manutenibilidade.md#5-q13--analisabilidade) | [M1.3.1](./gqm-manutenibilidade.md#m131--perfil-de-risco-de-complexidade-das-funções), [M1.3.2](./gqm-manutenibilidade.md#m132--cobertura-da-documentação-para-desenvolvedores), [M1.3.3](./gqm-manutenibilidade.md#m133--verificações-estáticas-executadas-automaticamente) |
| [Manutenibilidade](../fase-01/modelo-de-qualidade.md#manutenabilidade) | Modificabilidade | [Desenvolvedores](../fase-01/interessados.md#2-desenvolvedores-do-projeto); [Mantenedores](../fase-01/interessados.md#3-mantenedores) | [RQ-MAN-09 e 10](../fase-01/requisitos-avaliacao.md#2-requisitos-de-manutenibilidade) | [Q1.4](./gqm-manutenibilidade.md#6-q14--modificabilidade) | [M1.4.1](./gqm-manutenibilidade.md#m141--mediana-de-arquivos-de-produção-alterados-por-contribuição), [M1.4.2](./gqm-manutenibilidade.md#m142--arquivos-de-produção-extensos), [M1.4.3](./gqm-manutenibilidade.md#m143--proporção-de-contribuições-que-alteram-arquivos-extensos) |
| [Manutenibilidade](../fase-01/modelo-de-qualidade.md#manutenabilidade) | Testabilidade | [Equipes de qualidade](../fase-01/interessados.md#7-equipes-de-qualidade); [Mantenedores](../fase-01/interessados.md#3-mantenedores) | [RQ-MAN-11 a 13](../fase-01/requisitos-avaliacao.md#2-requisitos-de-manutenibilidade) | [Q1.5](./gqm-manutenibilidade.md#7-q15--testabilidade) | [M1.5.1](./gqm-manutenibilidade.md#m151--cobertura-de-linhas-por-pacote), [M1.5.2](./gqm-manutenibilidade.md#m152--distribuição-dos-testes-por-nível), [M1.5.3](./gqm-manutenibilidade.md#m153--proporção-de-contribuições-com-testes-executados-antes-da-integração) |
| [Confiabilidade](../fase-01/modelo-de-qualidade.md#confiabilidade) | Ausência de falhas (Maturidade na Fase 01) | [Mantenedores](../fase-01/interessados.md#3-mantenedores); [Equipes de qualidade](../fase-01/interessados.md#7-equipes-de-qualidade) | [RQ-CONF-01 e 02](../fase-01/requisitos-avaliacao.md#3-requisitos-de-confiabilidade) | [Q2.1](./gqm-confiabilidade.md#3-q21--ausência-de-falhas) | [M2.1.1](./gqm-confiabilidade.md#m211--proporção-de-correções-entre-as-contribuições-integradas), [M2.1.2](./gqm-confiabilidade.md#m212--mediana-do-tempo-entre-o-relato-e-a-correção), [M2.1.3](./gqm-confiabilidade.md#m213--proporção-de-contribuições-revisadas-antes-da-integração) |
| [Confiabilidade](../fase-01/modelo-de-qualidade.md#confiabilidade) | Disponibilidade | [Usuários finais](../fase-01/interessados.md#1-usuários-finais); [Equipes de operação](../fase-01/interessados.md#6-equipes-de-implantação-e-operação) | [RQ-CONF-03 e 04](../fase-01/requisitos-avaliacao.md#3-requisitos-de-confiabilidade) | [Q2.2](./gqm-confiabilidade.md#4-q22--disponibilidade) | [M2.2.1](./gqm-confiabilidade.md#m221--proporção-de-funções-essenciais-disponíveis-sem-conexão), [M2.2.2](./gqm-confiabilidade.md#m222--origens-externas-necessárias-para-o-editor-local) |
| [Confiabilidade](../fase-01/modelo-de-qualidade.md#confiabilidade) | Tolerância a falhas | [Usuários finais](../fase-01/interessados.md#1-usuários-finais) | [RQ-CONF-05 a 07](../fase-01/requisitos-avaliacao.md#3-requisitos-de-confiabilidade) | [Q2.3](./gqm-confiabilidade.md#5-q23--tolerância-a-falhas) | [M2.3.1](./gqm-confiabilidade.md#m231--proporção-de-arquivos-inválidos-tratados-com-mensagem), [M2.3.2](./gqm-confiabilidade.md#m232--continuidade-do-editor-após-falha-da-colaboração) |
| [Confiabilidade](../fase-01/modelo-de-qualidade.md#confiabilidade) | Recuperabilidade | [Usuários finais](../fase-01/interessados.md#1-usuários-finais) | [RQ-CONF-08 a 11](../fase-01/requisitos-avaliacao.md#3-requisitos-de-confiabilidade) | [Q2.4](./gqm-confiabilidade.md#6-q24--recuperabilidade) | [M2.4.1](./gqm-confiabilidade.md#m241--proporção-de-cenários-de-fechamento-com-restauração-do-desenho), [M2.4.2](./gqm-confiabilidade.md#m242--proporção-de-arquivos-reabertos-sem-perda), [M2.4.3](./gqm-confiabilidade.md#m243--cobertura-de-desfazer-e-refazer) |
| [Flexibilidade](../fase-01/modelo-de-qualidade.md#flexibilidade) | Adaptabilidade | [Usuários finais](../fase-01/interessados.md#1-usuários-finais); [Integradores](../fase-01/interessados.md#5-desenvolvedores-que-integram-a-biblioteca) | [RQ-FLEX-01 a 04](../fase-01/requisitos-avaliacao.md#4-requisitos-de-flexibilidade) | [Q3.1](./gqm-flexibilidade.md#3-q31--adaptabilidade) | [M3.1.1](./gqm-flexibilidade.md#m311--cobertura-de-usuários-pelos-navegadores-declarados), [M3.1.2](./gqm-flexibilidade.md#m312--proporção-de-ambientes-de-integração-com-sucesso), [M3.1.3](./gqm-flexibilidade.md#m313--proporção-de-ações-de-edição-que-funcionam-por-toque-e-caneta) |
| [Flexibilidade](../fase-01/modelo-de-qualidade.md#flexibilidade) | Escalabilidade | [Integradores](../fase-01/interessados.md#5-desenvolvedores-que-integram-a-biblioteca); [Equipes de operação](../fase-01/interessados.md#6-equipes-de-implantação-e-operação) | [RQ-FLEX-05 e 06](../fase-01/requisitos-avaliacao.md#4-requisitos-de-flexibilidade) | [Q3.2](./gqm-flexibilidade.md#4-q32--escalabilidade) | [M3.2.1](./gqm-flexibilidade.md#m321--tempo-de-abertura-por-tamanho-de-cena), [M3.2.2](./gqm-flexibilidade.md#m322--taxa-de-quadros-durante-a-edição-por-tamanho-de-cena), [M3.2.3](./gqm-flexibilidade.md#m323--tamanho-máximo-de-cena-salva-e-exportada) |
| [Flexibilidade](../fase-01/modelo-de-qualidade.md#flexibilidade) | Instalabilidade | [Integradores](../fase-01/interessados.md#5-desenvolvedores-que-integram-a-biblioteca); [Equipes de operação](../fase-01/interessados.md#6-equipes-de-implantação-e-operação); [Contribuidores](../fase-01/interessados.md#4-contribuidores-open-source) | [RQ-FLEX-07 a 10](../fase-01/requisitos-avaliacao.md#4-requisitos-de-flexibilidade) | [Q3.3](./gqm-flexibilidade.md#5-q33--instalabilidade) | [M3.3.1](./gqm-flexibilidade.md#m331--proporção-de-operações-de-pacote-bem-sucedidas), [M3.3.2](./gqm-flexibilidade.md#m332--proporção-de-passos-documentados-reproduzidos-sem-ajuste), [M3.3.3](./gqm-flexibilidade.md#m333--implantação-com-docker) |
| [Flexibilidade](../fase-01/modelo-de-qualidade.md#flexibilidade) | Substituibilidade | [Usuários finais](../fase-01/interessados.md#1-usuários-finais); [Integradores](../fase-01/interessados.md#5-desenvolvedores-que-integram-a-biblioteca) | [RQ-FLEX-11 e 12](../fase-01/requisitos-avaliacao.md#4-requisitos-de-flexibilidade) | [Q3.4](./gqm-flexibilidade.md#6-q34--substituibilidade) | [M3.4.1](./gqm-flexibilidade.md#m341--formatos-de-exportação-abertos-disponíveis), [M3.4.2](./gqm-flexibilidade.md#m342--proporção-de-elementos-preservados-na-exportação-e-reimportação), [M3.4.3](./gqm-flexibilidade.md#m343--proporção-dos-campos-do-formato-excalidraw-documentados) |

*Tabela 7: Rastreabilidade entre a Fase 01 e o Plano GQM.*

Todas as 13 subcaracterísticas do [modelo de qualidade](../fase-01/modelo-de-qualidade.md) têm uma questão, e todos os 36 requisitos de avaliação da Fase 01 são cobertos por pelo menos uma métrica. A Fase 01 usa o nome Maturidade, da edição de 2011 da norma, para a subcaracterística que a Fase 02 chama de Ausência de falhas.

---

## 7. Uso do plano nas próximas fases

Na Fase 03, o Plano GQM é a base de dois outros planos (AULA 08, p. 45 e 46):

- o **Plano de Medição**, que define o responsável pela coleta de cada métrica, o momento da coleta e o meio usado (formulário ou ferramenta), a partir dos procedimentos de coleta das fichas das métricas;
- o **Plano de Análise**, que simula a interpretação antes de a medição começar, seguindo as diretrizes da [seção 5](#5-diretrizes-de-interpretação), e define como os resultados serão apresentados em tabelas e gráficos.

Os planos devem ser avaliados com os membros da equipe e aprovados (AULA 08, p. 47). Se a revisão alterar alguma questão, hipótese ou métrica, a alteração deve ser feita na página de origem e repetida nesta página e nas figuras, com registro no histórico de versões das duas páginas.

---

## Referências

- AULA 08 QSW1 GQM. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Páginas 7, 8, 34, 44, 45, 46 e 47.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 19/10/2026 | Criação do Plano GQM, com os diagramas da hierarquia de G1, G2 e G3, as diretrizes de interpretação e a rastreabilidade com a Fase 01 | [Christopher Paraizo](https://github.com/wChrstphr) | |
| 1.1 | 20/10/2026 | Diagramas de G1, G2 e G3 refeitos no Excalidraw e publicados em PNG, com os arquivos editáveis `.excalidraw` | [Christopher Paraizo](https://github.com/wChrstphr) | |
