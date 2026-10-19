# Priorização das Características

## Objetivo e Método

A seleção das características que serão avaliadas não foi feita por preferência da equipe. Ela adota um método estruturado em duas etapas, para que cada escolha possa ser rastreada até os interessados mapeados na Fase 01 e para que os *trade-offs* fiquem explícitos.

1. **Ênfase de 1 a 5:** A equipe, no papel de requisitante, atribui a cada característica uma ênfase calculada a partir da matriz de interessados.
2. **Matriz impacto×risco:** A ênfase da etapa 1 é usada como impacto e cruzada com o risco de a característica apresentar problemas no Excalidraw. O cruzamento sustenta a seleção final e a discussão dos *trade-offs*.

A escala de ênfase segue:
**1** nenhum interesse, **2** baixo interesse, **3** médio interesse, **4** largo interesse e **5** grande interesse

> **Aviso:** A Capacidade de Interação (denominada Usabilidade na edição de 2011) não entra na priorização por regra da atividade. Por isso, ela não recebe nota nas tabelas abaixo.

---

## Etapa 1 — Ênfase de 1 a 5 a partir dos Interessados

### Regra de Cálculo

Para cada característica, cada um dos sete grupos de interessados da matriz de prioridades recebe uma classificação, convertida em pontos:

| Classificação | Pontos |
| :--- | :---: |
| **Principal (P)** — atende diretamente os interesses do grupo | 2 |
| **Secundário (S)** — relevância indireta | 1 |
| **Não Aplicável (–)** — periférica ou não aplicável | 0 |

A soma varia de 0 a 14 pontos. A ênfase é obtida por interpolação linear e arredondada segundo a fórmula:

**Ênfase = 1 + 4 * (Pontos / 14)**

### Matriz de Interessados × Características

Legenda dos grupos: **UF** (Usuários Finais) · **DP** (Desenvolvedores do Projeto) · **MA** (Mantenedores) · **CO** (Contribuidores Open Source) · **IN** (Integradores da Biblioteca npm) · **OP** (Equipes de Implantação e Operação) · **QA** (Equipes de Qualidade).

| Característica | UF | DP | MA | CO | IN | OP | QA | Pontos | Ênfase |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Confiabilidade** | P | S | P | S | S | S | P | **10** | **4** (Largo) |
| **Manutenibilidade** | – | P | P | P | S | – | P | **9** | **4** (Largo) |
| **Flexibilidade** | S | – | S | S | P | P | S | **8** | **3** (Médio) |
| Adequação Funcional | P | – | – | – | S | – | S | 4 | 2 (Baixo) |
| Eficiência de Desempenho | P | – | – | – | S | S | – | 4 | 2 (Baixo) |
| Compatibilidade | S | – | – | – | P | S | – | 4 | 2 (Baixo) |
| Segurança | S | – | S | – | – | S | – | 3 | 2 (Baixo) |
| Segurança de Proteção (*Safety*) | – | – | – | – | – | – | – | 0 | 1 (Nenhum) |
| Capacidade de Interação | — | — | — | — | — | — | — | — | *Fora da seleção* |

### Justificativa pelos Interessados

* **Confiabilidade (4):** Prioridade principal para os usuários finais (dependem de o trabalho ser salvo e recuperado), para os mantenedores e para as equipes de qualidade.
* **Manutenibilidade (4):** Prioridade principal para quem altera o código: desenvolvedores, mantenedores, contribuidores externos e equipes de qualidade.
* **Flexibilidade (3):** Prioridade principal de dois grupos (integradores da biblioteca npm e equipes de operação), com relevância secundária para outros quatro.
* **Adequação Funcional, Eficiência de Desempenho e Compatibilidade (2):** Cada uma possui um grupo principal e relevância secundária reduzida.
* **Segurança (2):** Relevante de forma indireta para usuários finais, mantenedores e operação, sem ser prioridade principal.
* **Segurança de Proteção (1):** Não há risco físico associado ao uso de um editor de desenhos.

---

## Etapa 2 — Matriz Impacto × Risco

### Definições

* **Impacto (1 a 5):** A ênfase obtida na etapa 1 (o quanto importa para os interessados).
* **Risco (1 a 5):** A probabilidade de a característica apresentar problemas no Excalidraw, estimada a partir do perfil do produto.
* **Prioridade:** **Impacto × Risco**.

### Estimativa de Risco e Prioridade

| Característica | Impacto | Risco | Impacto × Risco | Base da Estimativa de Risco |
| :--- | :---: | :---: | :---: | :--- |
| **Confiabilidade** | 4 | 4 | **16** | Edição colaborativa em tempo real, sincronização via WebSocket e modo offline (PWA) criam múltiplos pontos de falha. |
| **Manutenibilidade** | 4 | 3 | **12** | Monorepo com contribuições externas frequentes. Integração contínua, ESLint e TypeScript atenuam o risco. |
| **Flexibilidade** | 3 | 3 | **9** | O produto é aplicação web e biblioteca npm, precisando rodar em vários navegadores e ambientes React. |
| Eficiência de Desempenho | 2 | 4 | 8 | Editor baseado em canvas com desenhos que podem ter elevado volume de elementos. |
| Segurança | 2 | 3 | 6 | Existe sessão colaborativa, mas operando majoritariamente client-side. |
| Adequação Funcional | 2 | 2 | 4 | Ferramenta amplamente utilizada, com funções essenciais bem consolidadas. |
| Compatibilidade | 2 | 2 | 4 | Interoperabilidade focada nos formatos de exportação (.excalidraw, PNG, SVG). |
| Segurança de Proteção | 1 | 1 | 1 | Não há risco físico associado ao uso da ferramenta. |

### Matriz Impacto × Risco

| Risco \ Impacto | Baixo (1–2) | Médio (3) | Alto (4–5) |
| :--- | :--- | :--- | :--- |
| **Alto (4–5)** | Eficiência de Desempenho (8) | — | **Confiabilidade (16)** |
| **Médio (3)** | Segurança (6) | **Flexibilidade (9)** | **Manutenibilidade (12)** |
| **Baixo (1–2)** | Adequação Funcional (4), Compatibilidade (4), *Safety* (1) | — | — |

---

## Seleção Resultante

As três características com maior prioridade nas duas etapas foram selecionadas: **Confiabilidade (16)**, **Manutenibilidade (12)** e **Flexibilidade (9)**. O corte é visível na etapa 1, onde elas são as únicas com ênfase igual ou superior a 3.

---

## Trade-offs

1. **Confiabilidade e Manutenibilidade têm a mesma ênfase (4):** Atendem a públicos distintos (usuários finais vs. quem altera o código). O risco coloca Confiabilidade à frente (16 vs. 12), mas a equipe decidiu avaliar ambas com a mesma profundidade.
2. **Flexibilidade entra apesar da menor ênfase (3):** Atende aos integradores da biblioteca npm e equipes de operação, grupos que as outras duas características atendem pouco.
3. **Eficiência de Desempenho fica de fora apesar do risco alto:** O risco estimado é alto (4), mas o impacto é baixo (2). A perda é parcialmente compensada porque o desempenho com múltiplos elementos é avaliado dentro de Escalabilidade.
4. **Segurança não é avaliada:** Sua prioridade (6) é inferior à das três selecionadas, sem ser o foco principal de nenhum grupo.
5. **Usabilidade fica fora por regra da atividade:** É uma limitação reconhecida da avaliação.

---

## Referências

* AULA A07 QSW1 PROC AVAL PRODUTO. Material da disciplina de Qualidade de Software 1, UnB, slide 9.
* ISO/IEC 25010:2023. *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — Product quality model*.
* Documento de interessados da Fase 01 deste projeto.

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| 0.1 | 18/10/2026 | Criação do documento de priorização das características | [Letícia Santos](https://github.com/LeticiaSantosss) | |