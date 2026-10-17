# Política de Contribuição — QS1 2026-2 T02, Grupo Karen Jones

Este documento define o fluxo de trabalho no repositório **2026-2_T02_KAREN_JONES**, que reúne a documentação (GitPage), os dados e os artefatos de gestão da avaliação de qualidade do Excalidraw.

O objetivo é garantir organização, revisão entre pares, rastreabilidade entre issues, Pull Requests e critérios de avaliação, e registro confiável dos dados de gestão (PSM/CID).

## Índice

1. [Visão Geral](#1-visão-geral)
2. [Branches](#2-branches)
3. [Issues](#3-issues)
4. [Padrão de Nomes de Branch](#4-padrão-de-nomes-de-branch)
5. [Padrão de Commits](#5-padrão-de-commits)
6. [Pull Requests](#6-pull-requests)
7. [Uso de IA](#7-uso-de-ia)
8. [Dados, Evidências e Atas](#8-dados-evidências-e-atas)
9. [Deploy do GitPage](#9-deploy-do-gitpage)
10. [Releases](#10-releases)
11. [Definição de Pronto](#11-definição-de-pronto)
12. [Boas Práticas Gerais](#12-boas-práticas-gerais)
13. [Para quem está aprendendo Git](#13-para-quem-está-aprendendo-git)
14. [Resumo](#14-resumo)

## 1. Visão Geral

**Ninguém deve trabalhar diretamente na branch `main`.**

Toda tarefa começa com uma issue. Cada integrante cria uma branch para a issue, faz os commits nela e abre um Pull Request para revisão e merge na `main`.

```text
issue → branch a partir da main → commits → PR → revisão → merge na main → deploy automático do GitPage
```

## 2. Branches

- **main** — Branch principal. Representa a versão publicada no GitPage; cada merge dispara o deploy.
- **gh-pages** — Gerada automaticamente pela GitHub Action de deploy. **Não editar manualmente** e não usar como base de branches.

Não há branch `dev`: o produto do repositório é documentação, e a revisão no PR, junto com o build local (seção 6), cumpre o papel de validação.

## 3. Issues

Toda tarefa precisa de uma issue **antes** de começar o trabalho. As issues são criadas pelo formulário **Tarefa**.

Ao criar a issue, preencha:

- **Milestone** da fase (`Fase 1` a `Fase 4`);
- **Uma ou duas labels de tipo** (tabela abaixo) e a **label do subgrupo** (`subgrupo-F1F3` ou `subgrupo-F2F4`);
- **Prazo** e **Depende de** (issues que precisam terminar antes, ex.: `#9 (Propósito da avaliação)`, ou "Nenhuma");
- **Estimativa (h)**, **Critério de pronto** e, quando houver, **Critérios da rubrica atendidos** (códigos em [`.github/criterios-avaliacao.md`](.github/criterios-avaliacao.md));
- **Referências**: documentos de aula ou de avaliação que justificam a tarefa, sempre com nome do arquivo e página (ex.: `AULA 08 QSW1 GQM.pdf, p. 24`). Os PDFs ficam no Moodle e não são versionados no repositório;
- **Responsável** (assignee) e **Revisor**.

| Label | Uso |
| :--- | :--- |
| `documentacao` | Página de conteúdo do GitPage |
| `estudo` | Pesquisa de método ou norma antes de aplicá-lo |
| `analise` | Investigação do código ou da arquitetura do Excalidraw |
| `especificacao` | Definição usada nas fases seguintes (GQM, critérios de julgamento) |
| `medicao` | Coleta de dados e execução de ferramentas |
| `verificacao` | Revisão de entregas ou conferência com a rubrica |
| `diagrama` | Produção de figuras e diagramas |
| `artigo` | Seções do artigo em LaTeX |
| `gestao` | PSM/CID, atas, configuração do repositório |
| `gitpage` | Estrutura do site (rodapé, navegação, links) |
| `melhoria` | Ação de melhoria da Fase 4 |
| `retroativa` | Trabalho já realizado e registrado depois |

**Ao fechar a issue, edite o corpo e preencha "Horas reais (h)"**, informando as horas por pessoa quando houver mais de um responsável. Esses dados alimentam as métricas PSM/CID e a tabela de contribuição do artigo.

## 4. Padrão de Nomes de Branch

**Convenção:** `<tipo>/<área>-<descrição-curta>`

**Tipos:**

- `docs/*` → conteúdo de documentação ou do artigo
- `feat/*` → nova funcionalidade ou página estrutural do site
- `fix/*` → correção de conteúdo, link ou erro no site
- `chore/*` → configuração, dependências, gestão do repositório

**Áreas:** `f1` | `f2` | `f3` | `f4` | `artigo` | `gestao` | `site`

**Exemplos:**

- `docs/f1-proposito-avaliacao`
- `docs/f2-estudo-gqm`
- `docs/artigo-referencial-teorico`
- `fix/site-links-quebrados`
- `feat/site-rodape-versao`
- `chore/gestao-setup-issues`

**Regras:** letras minúsculas, sem acentos, palavras separadas por hífen, área logo após o tipo, nome curto. Evite nomes genéricos como `teste`, `mudancas` ou `branch-fulano`.

### Como criar a branch

```bash
git switch main
git pull origin main
git switch -c docs/f1-minha-tarefa
```

## 5. Padrão de Commits

**Estrutura:** `<tipo>: <descrição curta>`

**Tipos:**

- `docs` → conteúdo de documentação ou do artigo
- `feat` → nova funcionalidade ou página estrutural do site
- `fix` → correção de conteúdo, link ou erro
- `chore` → configuração, dependências, gestão
- `ci` → workflows do GitHub Actions
- `data` → dados brutos ou consolidados da avaliação (Fase 4)

**Exemplos:**

- `docs: adicionar propósito da avaliação`
- `docs: incluir matriz de priorização das características`
- `fix: corrigir grafia de manutenibilidade`
- `chore: adicionar formulário de issue`
- `ci: adicionar verificação de build nos PRs`
- `data: adicionar resultado da cobertura de testes`

### Autoria

- **Cada integrante faz os próprios commits e abre os próprios PRs.** Não suba trabalho de outra pessoa no seu nome: a contribuição individual é medida pelo histórico do Git.
- Cada integrante deve ter, ao longo do projeto, pelo menos uma issue com código (ex.: script de métricas PSM/CID, coleta automatizada de métricas, ação de melhoria).

### Boas práticas

- Verbo no infinitivo: `adicionar`, `corrigir`, `atualizar`.
- Evitar mensagens genéricas como *ajustes*, *update*, *alterações*, *agora vai*.
- Commits pequenos, sem misturar assuntos distintos.

## 6. Pull Requests

- Sempre abrir PR para a `main`; nada de push direto.
- Todo PR precisa de **pelo menos 1 aprovação** de quem não é autor; de preferência o revisor indicado na issue.
- Rodar `npm run build` localmente antes de pedir revisão: o build falha com links quebrados.
- Resolver conflitos antes de solicitar revisão.
- Usar `Closes #N` na descrição para fechar a issue no merge.
- Se não existe issue para o trabalho, criar a issue antes de abrir o PR.
- A descrição segue o modelo do repositório (preenchido automaticamente ao abrir o PR), incluindo a **declaração de uso de IA**.

**Título do PR:** `[<ÁREA>-<NÚMERO DA ISSUE>] <tipo>: <descrição objetiva>`

O número é o da issue no GitHub (numeração única do repositório). A área indica a qual parte do projeto a issue pertence.

**Exemplos:**

- `[F1-12] docs: adicionar propósito da avaliação`
- `[F2-20] docs: definir objetivos GQM`
- `[ARTIGO-31] docs: escrever referencial teórico`
- `[SITE-8] feat: adicionar versão e data no rodapé`
- `[GESTAO-3] chore: adicionar formulário de issue e mapa de critérios`

## 7. Uso de IA

Os critérios F1-C10, F2-C9 e AG-C3 avaliam a declaração e a revisão do uso de IA. Por isso:

- Declare no PR **qual ferramenta** foi usada, **para qual tarefa** e **como o conteúdo foi conferido ou ajustado**.
- Não cole texto gerado sem revisão; adapte ao contexto do Excalidraw e confira fatos e referências.
- Citações literais vão entre aspas, com fonte.
- **Sem emojis, figurinhas ou ícones** no GitPage e no artigo.

As declarações dos PRs serão consolidadas na declaração de uso de IA do artigo.

## 8. Dados, Evidências e Atas

- **Atas de reunião** ficam em `docs/gestao/atas/`, a partir do modelo `_modelo-ata.md`, com o nome `AAAA-MM-DD-assunto.md`.
- **Dados brutos e consolidados** da avaliação ficam no repositório, junto com os procedimentos de tratamento e cálculo, de modo que qualquer resultado do artigo possa ser verificado.
- **Entrevistas** só são gravadas com consentimento dos participantes. Dados de participantes devem ser anonimizados antes de serem versionados.

## 9. Deploy do GitPage

- O GitPage é publicado pela GitHub Action `.github/workflows/deploy.yml` a cada merge na `main` que altere o site.
- Não editar a branch `gh-pages` manualmente.
- Após o merge, confira se a página publicada está correta.

## 10. Releases

Cada entrega tem uma release com tag no `main`:

- `v1.0-E1` — Entrega 1 (Fases 1 e 2)
- `v2.0-E2` — Entrega 2 (Fases 3 e 4)

A release identifica a versão submetida no Moodle e é citada no artigo. O PDF do artigo é anexado à release e **não é versionado** no repositório: o fonte fica em `artigo/` e o PDF é gerado a partir dele.

## 11. Definição de Pronto

Uma issue só está **pronta** quando:

1. O **Pull Request** foi aberto seguindo este guia (título com área e número da issue, descrição completa).
2. Houve **revisão aprovada** de pelo menos uma pessoa que não seja a autora.
3. O **build local** (`npm run build`) passou, quando o PR altera o site.
4. Os itens do **Critério de pronto** da issue foram conferidos.
5. Os **critérios da rubrica** indicados na issue foram conferidos com [`.github/criterios-avaliacao.md`](.github/criterios-avaliacao.md).
6. As **Horas reais (h)** foram preenchidas na issue.
7. A **issue foi fechada** após o merge (via `Closes #N` ou manualmente, com referência ao PR).

## 12. Boas Práticas Gerais

- Branches curtas e PRs pequenos, fáceis de revisar.
- Atualizar a branch com a `main` com frequência para reduzir conflitos.
- Não alterar o trabalho de outra pessoa sem conversar com ela.
- Revisar com respeito: o comentário explica o problema e, quando possível, sugere uma solução.

## 13. Para quem está aprendendo Git

**Não tenha medo de perguntar.** Se aparecer um erro ou você não souber qual comando usar, peça ajuda antes de executar comandos que possam apagar ou sobrescrever o trabalho de outras pessoas.

`git reset --hard`, `git push --force` e exclusão de branches não devem ser usados sem orientação de alguém do grupo.

## 14. Resumo

- **main** = versão publicada no GitPage; **gh-pages** = deploy automático, não editar.
- **Fluxo:** issue → branch da main → PR (mín. 1 aprovação) → merge → deploy.
- **Branch:** `<tipo>/<área>-<descrição>`, com tipo `docs`, `feat`, `fix` ou `chore` e área `f1`–`f4`, `artigo`, `gestao` ou `site`.
- **Commit:** `tipo: descrição`.
- **PR:** `[ÁREA-NÚMERO] tipo: descrição`, com `Closes #N` e declaração de uso de IA.
- **Issue:** milestone, labels, estimativa ao abrir e horas reais ao fechar.
