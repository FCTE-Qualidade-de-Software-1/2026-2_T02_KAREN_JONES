---
sidebar_position: 10
title: ODS e a Avaliação
description: Relação entre a avaliação do Excalidraw e os Objetivos de Desenvolvimento Sustentável da Agenda 2030
---

import Link from '@docusaurus/Link';

# Objetivos de Desenvolvimento Sustentável

## Introdução

Os Objetivos de Desenvolvimento Sustentável (ODS) fazem parte da Agenda 2030 da ONU, aprovada em 2015. São 17 objetivos globais, cada um com metas específicas, que tratam de temas como pobreza, educação, inovação, desigualdade e meio ambiente [[1]](#ref-1). Esta página indica os ODS pertinentes ao Excalidraw e mostra como as características avaliadas se relacionam com eles.

## Metodologia

A equipe partiu do perfil do Excalidraw, uma ferramenta de código aberto, gratuita, colaborativa e voltada para diagramação, e selecionou os ODS com relação direta a esse perfil. Para cada ODS, as metas foram conferidas no texto oficial da ONU [[1]](#ref-1) e ligadas às subcaracterísticas do [modelo de qualidade](./modelo-de-qualidade.md) que ajudam a verificá-las. Os indicadores citados são propostos pela equipe e não fazem parte dos indicadores oficiais da Agenda 2030.

---

## 1. ODS selecionados

A Tabela 1 resume os três ODS selecionados.

<p className="tabela-titulo">Tabela 1: ODS selecionados</p>

| ODS | Nome | Relação com o Excalidraw |
|---|---|---|
| 4 | Educação de Qualidade | Ferramenta gratuita usada em contextos educacionais |
| 9 | Indústria, Inovação e Infraestrutura | Software livre que promove inovação e acesso a tecnologia |
| 10 | Redução das Desigualdades | Ferramenta acessível que reduz barreiras de acesso |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>

## 2. ODS 4: Educação de Qualidade

**Objetivo:** Assegurar a educação inclusiva, equitativa e de qualidade, e promover oportunidades de aprendizagem ao longo da vida para todos.

### Por que se aplica ao Excalidraw

O Excalidraw é usado por professores, estudantes e instrutores como ferramenta de apoio ao ensino. Por ser gratuito e funcionar direto no navegador, sem necessidade de instalação ou cadastro, qualquer pessoa com acesso à internet pode usá-lo em aulas, apresentações e atividades colaborativas. Isso reduz a barreira de acesso a ferramentas de diagramação, que muitas vezes são pagas ou exigem licenças institucionais.

A funcionalidade de colaboração em tempo real também facilita dinâmicas de sala de aula, trabalhos em grupo e orientações remotas.

### Metas e indicadores relacionados

<p className="tabela-titulo">Tabela 2: Metas do ODS 4 relacionadas à avaliação</p>

| Meta | Descrição | Relação com a avaliação |
|---|---|---|
| 4.3 | Assegurar igualdade de acesso para todos à educação técnica, profissional e superior de qualidade, a custos acessíveis | O Excalidraw é gratuito e acessível via navegador, eliminando custos de licença para estudantes e instituições. A avaliação de Flexibilidade (Instalabilidade e Adaptabilidade) verifica se o software funciona em diferentes ambientes e dispositivos, o que afeta diretamente esse acesso. |
| 4.4 | Aumentar o número de jovens e adultos com competências técnicas e profissionais relevantes | Ferramentas de diagramação como o Excalidraw apoiam o desenvolvimento de habilidades de modelagem, design e comunicação visual. A avaliação de Confiabilidade garante que o uso em contextos educacionais seja estável e sem perda de trabalho. |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>

**Indicador proposto pela equipe:** proporção de estudantes e professores com acesso a ferramentas digitais de apoio ao ensino. A avaliação de Flexibilidade (Adaptabilidade e Instalabilidade) verifica se o Excalidraw atende a essa necessidade ao funcionar em navegadores, dispositivos móveis e diferentes sistemas operacionais.

## 3. ODS 9: Indústria, Inovação e Infraestrutura

**Objetivo:** Construir infraestruturas resilientes, promover a industrialização inclusiva e sustentável, e fomentar a inovação.

### Por que se aplica ao Excalidraw

O Excalidraw é um projeto de código aberto que representa um exemplo de inovação tecnológica colaborativa. A arquitetura do projeto (monorepo com aplicação web e biblioteca npm separada) permite que outros desenvolvedores integrem o editor em suas próprias aplicações, ampliando o alcance da ferramenta e fomentando novas soluções.

Além disso, o modelo open source reduz as barreiras para o desenvolvimento de infraestrutura digital: equipes e organizações podem hospedar suas próprias instâncias do Excalidraw, adaptando-o às suas necessidades sem custos de licença.

### Metas e indicadores relacionados

<p className="tabela-titulo">Tabela 3: Metas do ODS 9 relacionadas à avaliação</p>

| Meta | Descrição | Relação com a avaliação |
|---|---|---|
| 9.5 | Fortalecer a pesquisa científica e a capacidade tecnológica, incentivando a inovação | O Excalidraw é mantido por uma comunidade aberta que contribui com código, testes e documentação. A avaliação de Manutenibilidade (Modularidade, Testabilidade e Analisabilidade) verifica se a estrutura do projeto facilita ou dificulta essas contribuições. |
| 9.b | Apoiar o desenvolvimento de tecnologia, pesquisa e inovação nos países em desenvolvimento | Ferramentas gratuitas e de código aberto reduzem a dependência de software proprietário. A avaliação de Flexibilidade (Instalabilidade) verifica se é viável instalar e manter o Excalidraw em diferentes ambientes. |
| 9.c | Aumentar o acesso às tecnologias da informação e comunicação e fornecer acesso universal à internet nos países menos desenvolvidos | O Excalidraw funciona como PWA (Progressive Web App) e tem suporte a funcionamento offline, o que é relevante em contextos com conectividade limitada. A avaliação de Confiabilidade (Disponibilidade) analisa esse aspecto. |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>

**Indicador proposto pela equipe:** número de contribuições externas e facilidade de integração da biblioteca. As métricas de Manutenibilidade e Flexibilidade do [Plano GQM](../fase-02/plano-gqm.md) ajudam a mensurar a facilidade com que novos desenvolvedores podem inovar a partir do código existente.

## 4. ODS 10: Redução das Desigualdades

**Objetivo:** Reduzir a desigualdade dentro dos países e entre eles.

### Por que se aplica ao Excalidraw

Ferramentas de produtividade e colaboração pagas criam uma barreira para estudantes, profissionais e organizações com recursos limitados. O Excalidraw, por ser gratuito e open source, permite que qualquer pessoa tenha acesso ao mesmo nível de funcionalidade sem restrições financeiras.

A capacidade de exportar dados em formatos abertos (.excalidraw, PNG, SVG) também evita o aprisionamento em uma plataforma, garantindo que os usuários tenham liberdade para migrar seus dados caso necessário.

### Metas e indicadores relacionados

<p className="tabela-titulo">Tabela 4: Metas do ODS 10 relacionadas à avaliação</p>

| Meta | Descrição | Relação com a avaliação |
|---|---|---|
| 10.2 | Até 2030, empoderar e promover a inclusão social, econômica e política de todos, independentemente de condição | Ferramentas acessíveis e gratuitas promovem a inclusão digital. A avaliação de Flexibilidade (Adaptabilidade) verifica se o Excalidraw funciona em dispositivos mais simples, telas pequenas e com entrada por toque, o que importa para o acesso de quem não tem equipamentos sofisticados. |
| 10.3 | Garantir igualdade de oportunidades e reduzir desigualdades de resultados | A avaliação de Flexibilidade (Substituibilidade) analisa se os formatos de exportação do Excalidraw são abertos e documentados, evitando que os dados dos usuários fiquem presos na ferramenta. |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>

**Indicador proposto pela equipe:** acessibilidade da ferramenta em diferentes contextos socioeconômicos. A avaliação de Flexibilidade, ao verificar adaptabilidade a dispositivos variados e formatos abertos de exportação, contribui para entender se o Excalidraw de fato atende a públicos diversos.

## 5. Relação entre os ODS e as características avaliadas

A Tabela 5 resume como cada ODS se conecta às três características avaliadas.

<p className="tabela-titulo">Tabela 5: Relação entre os ODS e as características avaliadas</p>

| ODS | Manutenibilidade | Confiabilidade | Flexibilidade |
|---|---|---|---|
| 4 (Educação) | Código bem organizado facilita contribuições de desenvolvedores que queiram adaptar o Excalidraw para contextos educacionais | Estabilidade e recuperação de dados são essenciais para uso em sala de aula | Funcionamento em navegadores diversos, dispositivos móveis e ambientes com restrições garante o acesso |
| 9 (Inovação) | Modularidade e testabilidade determinam a viabilidade de contribuição e inovação pela comunidade | A ausência de falhas, sustentada pelo processo de desenvolvimento, reforça a confiança da comunidade no projeto | Instalabilidade e adaptabilidade permitem que organizações hospedem e customizem suas instâncias |
| 10 (Desigualdades) | Analisabilidade e documentação baixam a barreira de entrada para novos contribuidores, inclusive de países em desenvolvimento | Disponibilidade offline é relevante para contextos com conectividade limitada | Exportação em formatos abertos e suporte a dispositivos variados garantem acesso sem restrições |

<p className="tabela-fonte">Fonte: [Gabriel Monteiro](https://github.com/GabrielSMonteiro), 2026.</p>

---

## Referências

> <Link id="ref-1">1.</Link> NAÇÕES UNIDAS BRASIL. **Objetivos de Desenvolvimento Sustentável**. Agenda 2030, com os 17 objetivos e suas metas. Disponível em: [https://brasil.un.org/pt-br/sdgs](https://brasil.un.org/pt-br/sdgs). Acesso em: 10 nov. 2026.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 18/10/2026 | Criação do documento de ODS relacionados à avaliação do Excalidraw | [Gabriel Monteiro](https://github.com/GabrielSMonteiro) | [Maria Eduarda](https://github.com/eduarda-ogomes) |
| 1.1 | 10/11/2026 | Introdução e Metodologia, retirada da citação ao critério da disciplina, retirada da meta 4.a, que trata de instalações físicas de ensino, indicadores identificados como propostos pela equipe, subcaracterística Ausência de falhas adotada, tabelas com título e fonte e referência à ONU numerada | [Christopher Paraizo](https://github.com/wChrstphr) | [Gabriel Monteiro](https://github.com/GabrielSMonteiro) |
