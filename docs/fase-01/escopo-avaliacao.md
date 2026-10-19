---
sidebar_position: 4
title: Escopo, Profundidade e Objetos de Avaliação
description: Delimitação dos objetos, da profundidade e dos limites de validade da avaliação do Excalidraw
---

# Escopo, profundidade e objetos de avaliação

## 1. Identificação, propósito e linha de base

A avaliação conduzida pelo **Grupo Karen Jones**, no contexto da disciplina de Qualidade de Software 1 da FCTE/UnB, considera o **Excalidraw** em suas duas formas de disponibilização: aplicação web e componente reutilizável React. A equipe é **requisitante e avaliadora acadêmica independente**, sem acesso privilegiado aos sistemas internos de operação do produto.

- **Produto:** Excalidraw; repositório oficial: [github.com/excalidraw/excalidraw](https://github.com/excalidraw/excalidraw).
- **Branch de origem:** `master`.
- **Commit analisado:** [`e1b7aacb356a492aa1e0fc6eb57b8896124027f0`](https://github.com/excalidraw/excalidraw/tree/e1b7aacb356a492aa1e0fc6eb57b8896124027f0), de **18/10/2026**.
- **Pacote da biblioteca nesse commit:** `@excalidraw/excalidraw`, com versão **0.18.0** no respectivo `package.json`; **não** se presume que o número do pacote identifique toda a aplicação hospedada.
- **Base normativa:** ISO/IEC 25010:**2023**, família SQuaRE, com foco em **Manutenibilidade, Confiabilidade e Flexibilidade**.
- **Objetivo de uso dos resultados:** identificar evidências de qualidade, lacunas, limitações e oportunidades de melhoria, subsidiando a especificação GQM, o planejamento e a execução futura da avaliação.

A referência ao commit permite repetir a inspeção do **código-fonte**; resultados operacionais dependentes de serviços externos ou configurações de produção podem não ser reproduzíveis apenas por essa referência. As conclusões deverão distinguir evidência de código, teste e inferência.

## 2. Objetos e fronteiras da avaliação

Os **objetos** são partes concretas do produto e artefatos usados como fontes de evidência. As **características** são dimensões de qualidade que serão investigadas nesses objetos.

| Objeto de avaliação | Identificação no commit fixado | Características relacionadas | Inclusão e justificativa |
| :--- | :--- | :--- | :--- |
| **O1 — Editor e biblioteca React** | `packages/excalidraw/`, `package.json`, entradas públicas, `components/`, `scene/`, `renderer/`, `data/` | Manutenibilidade, Confiabilidade e Flexibilidade | Núcleo reutilizável para análise de arquitetura, API e serialização. |
| **O2 — Aplicação web** | `excalidraw-app/`, `App.tsx`, `index.tsx`, `vite.config.mts` | Confiabilidade, Flexibilidade e Manutenibilidade | Permite inspecionar como o editor é usado e disponibilizado ao usuário. |
| **O3 — Colaboração e persistência cliente** | `excalidraw-app/collab/`, `excalidraw-app/data/` | Confiabilidade | Contém lógica observável de sessões, salvamento, restauração e integração; só o **cliente** faz parte da análise de código. |
| **O4 — Pacotes reutilizáveis** | `packages/element/`, `packages/common/`, `packages/math/`, `packages/utils/` e demais workspaces | Manutenibilidade e Flexibilidade | Permitem verificar fronteiras, responsabilidades e reuso entre módulos. |
| **O5 — Build, qualidade e documentação** | `package.json`, `tsconfig.json`, `vitest.config.mts`, `.github/workflows/`, `dev-docs/`, `examples/`, arquivos de testes | Manutenibilidade e Flexibilidade | Registram contratos de integração, pré-requisitos, procedimentos automatizados e evidências documentais. |
| **O6 — Histórico público de evolução** | Commits, Issues, Pull Requests e releases do repositório, delimitados por janela explicitada no plano de medição | Manutenibilidade e Confiabilidade | Pode subsidiar métricas de manutenção e tratamento de defeitos; a janela e a coleta ainda deverão ser especificadas. |

**Fronteira principal:** no âmbito de O1 a O5, inclui-se o código **versionado no commit de referência**, suas configurações, testes e documentação. O6 é uma fonte histórica e requer critério temporal próprio; **não** se deve misturar eventos posteriores ao commit com métricas de uma versão congelada sem declarar essa diferença.

## 3. O que está dentro do escopo

| Característica (ISO/IEC 25010:2023) | Subcaracterísticas | Abordagem prevista e evidências | Profundidade inicial |
| :--- | :--- | :--- | :--- |
| **Manutenibilidade** | Modularidade, Reusabilidade, Analisabilidade, Modificabilidade, Testabilidade | Inspeção dos diretórios/workspaces, dependências e APIs; scripts de lint/tipagem, testes e workflows; análise de histórico quando houver método de amostragem explícito. | **Intermediária:** evidência estática estruturada, com possibilidade de medidas automatizadas após definição operacional. |
| **Confiabilidade** | Ausência de falhas, Disponibilidade, Tolerância a falhas, Recuperabilidade | Análise de código cliente de persistência, erros, PWA, colaboração e recuperação; posterior projeto de testes controlados com condições/rede/arquivos definidos. | **Exploratória na Fase 1:** identificar mecanismos, sem alegar desempenho ou disponibilidade medidos. |
| **Flexibilidade** | Adaptabilidade, Escalabilidade, Instalabilidade, Substituibilidade | Inspeção da API React, manifestos e instruções de build, compatibilidade declarada, exportação/importação e cenários de volume crescente a planejar. | **Intermediária na documentação**, exploratória para desempenho e compatibilidade real até existirem ensaios. |

**Critério de profundidade:** a avaliação dará maior cobertura ao que é verificável por artefatos públicos e passível de repetição por uma equipe acadêmica. Investigações que exijam carga de produção, contas privadas, métricas de servidor ou dispositivos indisponíveis ficam limitadas a hipóteses e propostas de medição, não a conclusões empíricas.

## 4. O que está fora do escopo (e por quê)

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

## 5. Profundidade, procedimento e limites operacionais

A análise está organizada em **três níveis** que não devem ser confundidos:

1. **Inventário documental e arquitetural (Fase 1):** identificar objetos, responsabilidades, interfaces, interessados, fronteiras, versão e potenciais fontes de evidência. **Este documento conclui a delimitação, não o julgamento de qualidade.**
2. **Especificação verificável (Fase 2):** converter requisitos do documento [Requisitos de avaliação](./requisitos-avaliacao.md) em perguntas e métricas GQM, definir procedimento, ferramentas, amostra, unidade, critérios e condição de teste.
3. **Coleta e julgamento (Fases 3 e 4):** planejar execução em ambiente controlado, coletar medidas, registrar condições, confrontar os critérios e interpretar limitações. Um teste futuro **não** deve ser descrito aqui como se já tivesse sido executado.

### 5.1 Aplicação por característica

- **Manutenibilidade:** inspeção de artefatos versionados é viável; impacto de manutenção real depende de histórico contextualizado. Não se infere diretamente tempo médio de correção a partir de contagens brutas de PRs.
- **Confiabilidade:** implementação de salvamento, mecanismos de tratamento de erros e configuração PWA podem ser **inspecionadas**. Afirmações sobre recuperação após falhas ou funcionamento offline exigem testes de falha/reabertura com resultados registrados.
- **Flexibilidade:** contratos React e dependências permitem estudar **instalabilidade** e **adaptabilidade declarada**. Testes de diferentes navegadores, tamanho de cena e integração por aplicações hospedeiras deverão ser reprodutíveis, delimitando versões e recursos de hardware.

## 6. Matriz de rastreabilidade (objetos × requisitos)

A tabela não substitui o Plano GQM. Ela liga os objetos à [tabela de requisitos](./requisitos-avaliacao.md) e ao [modelo de qualidade](./modelo-de-qualidade.md).

| Objeto | Requisitos de avaliação pertinentes | Evidências iniciais |
| :--- | :--- | :--- |
| O1, O4, O5 | `RQ-MAN-01` a `RQ-MAN-13` | Diretórios, dependências, exportações públicas, testes e CI |
| O2, O3, O5, O6 | `RQ-CONF-01` a `RQ-CONF-11` | Código de colaboração/persistência, configuração PWA, controle de qualidade e histórico público |
| O1, O2, O5 | `RQ-FLEX-01` a `RQ-FLEX-12` | `package.json`, `Dockerfile`, exemplos, API, serialização e manifestos de navegador |

As perguntas identificam o **que deverá ser verificado**; presença de código ou de uma dependência **não é resposta positiva automática** a um requisito.

## 7. Validade e ameaças aos resultados

1. **Validade temporal:** os mecanismos descritos correspondem ao commit fixado; indicadores extraídos do GitHub em outras datas devem documentar a janela de coleta.
2. **Validade externa:** um subconjunto de browsers e cargas sintéticas não representa todos os dispositivos nem o comportamento de produção.
3. **Validade de construto:** quantidade de testes, alterações ou dependências não equivale diretamente a cobertura, facilidade de manutenção ou confiabilidade; cada métrica requer justificativa.
4. **Validade interna:** falhas ou acertos podem decorrer do ambiente (rede, cache, armazenamento disponível e serviços externos); registrar as condições e isolar fatores.
5. **Visibilidade:** inspecionar somente repositório público não revela configuração de produção, disponibilidade real ou políticas de operação.
6. **Reprodutibilidade:** registrar SHA, versões de Node/Yarn/navegador, comandos, dados de entrada e limites de recursos em futuras coletas.

As observações sobre arquitetura são detalhadas em [Tipo de produto e arquitetura](./tipo-produto.md), e os interessados que justificam o recorte estão em [Mapeamento de interessados](./interessados.md).

## 8. Referências

- [Excalidraw — snapshot oficial do código (`e1b7aac`)](https://github.com/excalidraw/excalidraw/tree/e1b7aacb356a492aa1e0fc6eb57b8896124027f0).
- [README do Excalidraw](https://github.com/excalidraw/excalidraw/blob/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/README.md); [manifesto raiz](https://github.com/excalidraw/excalidraw/blob/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/package.json); [manifesto da biblioteca](https://github.com/excalidraw/excalidraw/blob/e1b7aacb356a492aa1e0fc6eb57b8896124027f0/packages/excalidraw/package.json).
- ISO/IEC 25010:2023 — modelo de qualidade de produto da família SQuaRE (conforme documento da disciplina).
- AULA A07 QSW1 PROC AVAL PRODUTO.pdf, páginas 7 e 8 (profundidade, abrangência, objetos e versão; material da disciplina referenciado na Issue #13).

## Histórico de versões

| Versão | Data | Descrição | Autor | Revisão |
| :---: | :---: | :--- | :--- | :--- |
| 1.0 | 18/10/2026 | Formalização dos objetos, fronteiras, profundidade e limites de validade | [Davi Pierre](https://github.com/DaviPierre) | |
