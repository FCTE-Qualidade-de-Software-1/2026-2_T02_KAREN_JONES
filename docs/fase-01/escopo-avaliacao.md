---
sidebar_position: 8
title: Escopo, Profundidade e Objetos de Avaliação
description: Delimitação dos objetos, da profundidade e dos limites de validade da avaliação do Excalidraw
---

import Link from '@docusaurus/Link';

# Escopo, profundidade e objetos de avaliação

## Introdução

A análise de requisitos define a profundidade, a abrangência, o relacionamento com outras avaliações e os objetos a serem avaliados [[1, p. 7]](#ref-1). Esta página delimita o que a avaliação do Excalidraw examina, o que fica de fora, com que profundidade cada característica é tratada e quais limites de validade os resultados terão.

## Metodologia

Os objetos foram identificados no repositório oficial, no commit `e1b7aac` de 18/10/2026 [[2]](#ref-2), a partir da arquitetura descrita em [Descrição e arquitetura do produto](./descricao-produto.md). Cada objeto foi ligado às características do [modelo de qualidade](./modelo-de-qualidade.md) [[3]](#ref-3) e aos [requisitos de avaliação](./requisitos-avaliacao.md). As exclusões registram o que a equipe não consegue observar a partir do repositório público.

---

## 1. Linha de base

A equipe Karen Jones é [requisitante e avaliadora independente](./proposito-avaliacao.md#3-requisitante-da-avaliação), sem acesso privilegiado aos sistemas internos de operação do produto. A avaliação considera o Excalidraw nas suas duas formas de distribuição: aplicação web e componente React reutilizável. A linha de base é o commit [`e1b7aac`](https://github.com/excalidraw/excalidraw/tree/e1b7aacb356a492aa1e0fc6eb57b8896124027f0) da branch `master`, em que a biblioteca `@excalidraw/excalidraw` está na versão 0.18.0. O número do pacote não identifica sozinho a aplicação hospedada, por isso a avaliação se refere ao commit ([identificação completa](./tipo-produto.md#1-identificação-e-versão-analisada)).

O commit permite repetir a inspeção do **código-fonte**, mas resultados que dependem de serviços externos ou de configurações de produção podem não ser reproduzíveis apenas por essa referência. As conclusões distinguem evidência de código, evidência de teste e inferência.

## 2. Objetos e fronteiras da avaliação

Os **objetos** são partes concretas do produto e artefatos usados como fontes de evidência. As **características** são dimensões de qualidade que serão investigadas nesses objetos.

<p className="tabela-titulo">Tabela 1: Objetos e fronteiras da avaliação</p>

| Objeto de avaliação | Identificação no commit fixado | Características relacionadas | Inclusão e justificativa |
| :--- | :--- | :--- | :--- |
| **O1: Editor e biblioteca React** | `packages/excalidraw/`, `package.json`, entradas públicas, `components/`, `scene/`, `renderer/`, `data/` | Manutenibilidade, Confiabilidade e Flexibilidade | Núcleo reutilizável para análise de arquitetura, API e serialização. |
| **O2: Aplicação web** | `excalidraw-app/`, `App.tsx`, `index.tsx`, `vite.config.mts` | Confiabilidade, Flexibilidade e Manutenibilidade | Permite inspecionar como o editor é usado e disponibilizado ao usuário. |
| **O3: Colaboração e persistência cliente** | `excalidraw-app/collab/`, `excalidraw-app/data/` | Confiabilidade | Contém lógica observável de sessões, salvamento, restauração e integração. Só o **cliente** faz parte da análise de código. |
| **O4: Pacotes reutilizáveis** | `packages/element/`, `packages/common/`, `packages/math/`, `packages/utils/` e demais workspaces | Manutenibilidade e Flexibilidade | Permitem verificar fronteiras, responsabilidades e reuso entre módulos. |
| **O5: Build, qualidade e documentação** | `package.json`, `tsconfig.json`, `vitest.config.mts`, `.github/workflows/`, `dev-docs/`, `examples/`, arquivos de testes | Manutenibilidade e Flexibilidade | Registram contratos de integração, pré-requisitos, procedimentos automatizados e evidências documentais. |
| **O6: Histórico público de evolução** | Commits, Issues, Pull Requests e releases do repositório, delimitados por janela histórica | Manutenibilidade e Confiabilidade | Subsidia métricas de manutenção e de tratamento de defeitos, com a janela histórica definida na [Fase 02](../fase-02/gqm-manutenibilidade.md#2-convenções-de-coleta). |

<p className="tabela-fonte">Fonte: [Davi Pierre](https://github.com/DaviPierre), 2026.</p>

**Fronteira principal:** no âmbito de O1 a O5, inclui-se o código **versionado no commit de referência**, suas configurações, testes e documentação. O6 é uma fonte histórica e requer critério temporal próprio. **Não** se deve misturar eventos posteriores ao commit com métricas de uma versão congelada sem declarar essa diferença.

## 3. O que está dentro do escopo

<p className="tabela-titulo">Tabela 2: Características, abordagem e profundidade</p>

| Característica (ISO/IEC 25010:2023) | Subcaracterísticas | Abordagem prevista e evidências | Profundidade inicial |
| :--- | :--- | :--- | :--- |
| **Manutenibilidade** | Modularidade, Reusabilidade, Analisabilidade, Modificabilidade, Testabilidade | Inspeção dos diretórios/workspaces, dependências e APIs, scripts de lint e tipagem, testes e workflows, e análise de histórico quando houver método de amostragem explícito. | **Intermediária:** evidência estática estruturada, com possibilidade de medidas automatizadas após definição operacional. |
| **Confiabilidade** | Ausência de falhas, Disponibilidade, Tolerância a falhas, Recuperabilidade | Análise de código cliente de persistência, erros, PWA, colaboração e recuperação, seguida de projeto de testes controlados com condições/rede/arquivos definidos. | **Exploratória na Fase 01:** identificar mecanismos, sem alegar desempenho ou disponibilidade medidos. |
| **Flexibilidade** | Adaptabilidade, Escalabilidade, Instalabilidade, Substituibilidade | Inspeção da API React, manifestos e instruções de build, compatibilidade declarada, exportação/importação e cenários de volume crescente a planejar. | **Intermediária na documentação**, exploratória para desempenho e compatibilidade real até existirem ensaios. |

<p className="tabela-fonte">Fonte: [Davi Pierre](https://github.com/DaviPierre), 2026.</p>

**Critério de profundidade:** a avaliação dará maior cobertura ao que é verificável por artefatos públicos e passível de repetição por uma equipe acadêmica. Investigações que exijam carga de produção, contas privadas, métricas de servidor ou dispositivos indisponíveis ficam limitadas a hipóteses e propostas de medição, não a conclusões empíricas.

## 4. O que está fora do escopo (e por quê)

<p className="tabela-titulo">Tabela 3: Exclusões do escopo</p>

| Exclusão | Justificativa técnica/metodológica | Consequência para as conclusões |
| :--- | :--- | :--- |
| **Servidores e bancos de dados gerenciados de produção** e sua configuração privada | O repositório público expõe lógica de cliente, mas não garante acesso a toda a arquitetura implantada, logs, SLAs ou configurações operacionais. | Não é possível afirmar disponibilidade de serviço, tolerância a falhas ponta a ponta ou integridade real sob falhas de infraestrutura. |
| **Auditoria de segurança, proteção de dados e conformidade** | São dimensões relevantes, mas não estão entre as três características escolhidas, nem há recursos para perícia especializada. | Referências a criptografia no código **não equivalem** a certificação de segurança. |
| **Medições de produção em escala real** (usuários simultâneos, latência de serviços, indicadores de SLA) | Não há acesso controlado a infraestrutura e telemetria representativa. | Resultados de escalabilidade ou confiabilidade em produção não poderão ser generalizados a partir de inspeção de código. |
| **Cobertura de todas as combinações de browsers, dispositivos e acessibilidade** | Matriz de compatibilidade combinatória extensa e infraestrutura física limitada. | Pode-se documentar suporte **declarado** e testar amostras definidas nas fases seguintes, não certificar compatibilidade universal. |
| **Código interno de bibliotecas terceirizadas** | Dependências externas não integram o produto-fonte avaliado e exigiriam escopo próprio. | Vulnerabilidades ou defeitos nessas dependências não são exaustivamente auditados. |
| **Demais características de qualidade** (além de Manutenibilidade, Confiabilidade e Flexibilidade) | A equipe priorizou três características rastreáveis a interessados e artefatos, considerando prazo e capacidade. | O resultado não representa a qualidade total do Excalidraw segundo todas as nove características. |
| **Componentes comerciais de Excalidraw+ e integrações privadas** | Não são necessários para o recorte da aplicação open source e podem não possuir código público auditável. | As conclusões valem para o produto aberto/objeto versionado e não para ofertas comerciais adicionais. |
| **Versões futuras, forks e instalações modificadas** | O objeto técnico é um snapshot fixo. | Uma mudança posterior de código, dependências ou implantação exige reavaliação. |

<p className="tabela-fonte">Fonte: [Davi Pierre](https://github.com/DaviPierre), 2026.</p>

## 5. Profundidade, procedimento e limites operacionais

A análise está organizada em **três níveis** que não devem ser confundidos:

1. **Inventário documental e arquitetural (Fase 01):** identificar objetos, responsabilidades, interfaces, interessados, fronteiras, versão e potenciais fontes de evidência. **Este documento conclui a delimitação, não o julgamento de qualidade.**
2. **Especificação verificável (Fase 02):** converter os [requisitos de avaliação](./requisitos-avaliacao.md) em questões e métricas do [Plano GQM](../fase-02/plano-gqm.md), definir procedimento, ferramentas, amostra, unidade, critérios e condição de teste.
3. **Coleta e julgamento (Fases 03 e 04):** planejar execução em ambiente controlado, coletar medidas, registrar condições, confrontar os critérios e interpretar limitações. Um teste futuro **não** deve ser descrito aqui como se já tivesse sido executado.

### 5.1 Aplicação por característica

- **Manutenibilidade:** inspeção de artefatos versionados é viável, mas o impacto de manutenção real depende de histórico contextualizado. Não se infere diretamente tempo médio de correção a partir de contagens brutas de PRs.
- **Confiabilidade:** implementação de salvamento, mecanismos de tratamento de erros e configuração PWA podem ser **inspecionadas**. Afirmações sobre recuperação após falhas ou funcionamento offline exigem testes de falha/reabertura com resultados registrados.
- **Flexibilidade:** contratos React e dependências permitem estudar **instalabilidade** e **adaptabilidade declarada**. Testes de diferentes navegadores, tamanho de cena e integração por aplicações hospedeiras deverão ser reprodutíveis, delimitando versões e recursos de hardware.

## 6. Matriz de rastreabilidade entre objetos e requisitos

A Tabela 4 não substitui o [Plano GQM](../fase-02/plano-gqm.md#6-rastreabilidade-com-a-fase-01). Ela liga os objetos à [tabela de requisitos](./requisitos-avaliacao.md) e ao [modelo de qualidade](./modelo-de-qualidade.md).

<p className="tabela-titulo">Tabela 4: Objetos e requisitos de avaliação</p>

| Objeto | Requisitos de avaliação pertinentes | Evidências iniciais |
| :--- | :--- | :--- |
| O1, O4, O5 | [RQ-MAN-01 a RQ-MAN-13](./requisitos-avaliacao.md#2-requisitos-de-manutenibilidade) | Diretórios, dependências, exportações públicas, testes e CI |
| O2, O3, O5, O6 | [RQ-CONF-01 a RQ-CONF-11](./requisitos-avaliacao.md#3-requisitos-de-confiabilidade) | Código de colaboração e persistência, configuração PWA, controle de qualidade e histórico público |
| O1, O2, O5 | [RQ-FLEX-01 a RQ-FLEX-12](./requisitos-avaliacao.md#4-requisitos-de-flexibilidade) | `package.json`, `Dockerfile`, exemplos, API, serialização e manifestos de navegador |

<p className="tabela-fonte">Fonte: [Davi Pierre](https://github.com/DaviPierre), 2026.</p>

As perguntas identificam o **que deverá ser verificado**. A presença de código ou de uma dependência **não é resposta positiva automática** a um requisito.

## 7. Validade e ameaças aos resultados

1. **Validade temporal:** os mecanismos descritos correspondem ao commit fixado, e indicadores extraídos do GitHub em outras datas devem documentar a janela de coleta.
2. **Validade externa:** um subconjunto de browsers e cargas sintéticas não representa todos os dispositivos nem o comportamento de produção.
3. **Validade de construto:** quantidade de testes, alterações ou dependências não equivale diretamente a cobertura, facilidade de manutenção ou confiabilidade, e cada métrica requer justificativa.
4. **Validade interna:** falhas ou acertos podem decorrer do ambiente (rede, cache, armazenamento disponível e serviços externos), por isso as condições são registradas e os fatores, isolados.
5. **Visibilidade:** inspecionar somente repositório público não revela configuração de produção, disponibilidade real ou políticas de operação.
6. **Reprodutibilidade:** registrar SHA, versões de Node, Yarn e navegador, comandos, dados de entrada e limites de recursos em futuras coletas.

As observações sobre arquitetura estão em [Descrição e arquitetura do produto](./descricao-produto.md), e os interessados que justificam o recorte, em [Partes interessadas](./interessados.md).

## Referências

> <Link id="ref-1">1.</Link> RAMOS, Cristiane Soares. **AULA A07 QSW1 PROC AVAL PRODUTO**. Material da disciplina de Qualidade de Software 1, FCTE/UnB, 2026. Páginas 7 e 8. Disponível no Moodle da disciplina.
>
> <Link id="ref-2">2.</Link> EXCALIDRAW. Repositório oficial, commit `e1b7aac` de 18/10/2026, com o [README](https://github.com/excalidraw/excalidraw/blob/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/README.md), o [manifesto raiz](https://github.com/excalidraw/excalidraw/blob/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/package.json) e o [manifesto da biblioteca](https://github.com/excalidraw/excalidraw/blob/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/packages/excalidraw/package.json). Disponível em: [https://github.com/excalidraw/excalidraw/tree/e1b7aacb356a492aa1e0fc6eb57b8896124027f0](https://github.com/excalidraw/excalidraw/tree/e1b7aacb356a492aa1e0fc6eb57b8896124027f0). Acesso em: 10 nov. 2026.
>
> <Link id="ref-3">3.</Link> ISO/IEC 25010:2023. *Systems and software engineering: Systems and software Quality Requirements and Evaluation (SQuaRE): Product quality model*.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 18/10/2026 | Formalização dos objetos, fronteiras, profundidade e limites de validade | [Davi Pierre](https://github.com/DaviPierre) | |
| 1.1 | 10/11/2026 | Introdução e Metodologia, linha de base resumida com link à identificação do produto, códigos de objeto sem travessão, janela histórica ligada à Fase 02, faixas de requisitos com links, link de arquitetura apontado para a descrição do produto, tabelas com título e fonte e referências numeradas | [Christopher Paraizo](https://github.com/wChrstphr) | [Davi Pierre](https://github.com/DaviPierre) |
