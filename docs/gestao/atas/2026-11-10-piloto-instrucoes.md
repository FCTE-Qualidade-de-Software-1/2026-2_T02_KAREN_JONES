---
title: "Ata: 10/11/2026 (Piloto das Instruções da Fase 3)"
description: Reunião do subgrupo F2/F4 para execução do teste piloto dos procedimentos de avaliação e homologação dos comandos de preparação de ambiente da Fase 03.
---

# Ata da reunião: 10/11/2026

| Campo | Valor |
| :--- | :--- |
| **Data e horário** | 10/11/2026, 14h00 às 15h30 |
| **Local** | Remoto (Discord) |
| **Fase** | Fase 03: Projetar a avaliação |
| **Redator(a)** | [Maria Eduarda](https://github.com/eduarda-ogomes) |
| **Gravação** | Não houve |

## Participantes

- [x] Christopher Paraizo
- [ ] Davi Pierre
- [ ] Gabriel Monteiro
- [ ] Letícia de Carvalho
- [x] Luiz Henrique Soares
- [x] Maria Eduarda

Sessão técnica do subgrupo F2/F4 para execução e validação do teste piloto das instruções da Fase 03.

## Pauta

1. Execução do teste piloto do plano de avaliação conforme a Issue #103.
2. Verificação prática dos comandos de preparação e configuração de ambiente descritos na Issue #96.
3. Identificação de obstáculos, omissões nas instruções textuais e encaminhamento dos ajustes necessários antes do início da Fase 04.

## Discussão

- **Execução do Piloto de Procedimentos:** Maria Eduarda, integrante do subgrupo F2/F4 que não redigiu as instruções de G1 e G2, seguiu os passos das instruções de avaliação para verificar se as orientações eram autossuficientes e reproduzíveis sem conhecimento tácito não documentado.
- **Validação do Ambiente e Docker:** Os comandos de conteinerização oficial da Issue #96 foram executados no Zorin OS (Linux). A imagem Docker de produção `excalidraw-avaliacao` foi gerada via `docker build -t excalidraw-avaliacao .` e o contêiner subiu na porta 3000:80 com verificação de integridade aprovada, validando a infraestrutura de referência para as coletas.
- **Obstáculo 1 (Sintaxe legada de Docker Compose):** Durante a reprodução do Passo 6 de execução local documentada, a invocação de `docker-compose up` falhou com código 127 (command not found) em distribuições Linux modernas com Docker Engine v2. Foi constatada a necessidade de orientar o uso do comando moderno `docker compose up` sem hífen nas instruções e relatórios.
- **Obstáculo 2 (Conflitos de Dependências e Cobertura em G1):** Christopher e Luiz relataram que o pacote `cmdtest` do Ubuntu interfere com o utilitário Yarn, e que o comando de cobertura do Vitest exige a variável `CI=true` para encerramento síncrono dos testes sem travar o terminal.
- **Obstáculo 3 (Alocação de Portas):** Luiz Henrique registrou que em seu ambiente de testes a porta padrão 3000 estava em uso por outro processo, sendo necessário parametrizar o mapeamento para a porta 3001, mantendo a documentação do desvio nos fatores de variação.

## Decisões

| # | Decisão | Justificativa |
| :--- | :--- | :--- |
| 1 | Homologar a preparação conteinerizada via Docker como pronta para a Fase 04. | O contêiner de referência subiu com integridade e serviu o editor de forma autônoma na porta 3000. |
| 2 | Incorporar a orientação sobre `docker compose` nas instruções e relatórios. | Evitar falhas de comando não encontrado para avaliadores em sistemas com Docker Engine v2. |
| 3 | Padronizar a flag `CI=true` nos scripts e testes automatizados de G1. | Garantir o encerramento do processo do Vitest após a geração da matriz de cobertura. |
| 4 | Autorizar a abertura da Fase 04 e o início das coletas empíricas de G3 (Flexibilidade). | Os roteiros e o ambiente de Flexibilidade foram plenamente validados no piloto. |

## Encaminhamentos

| Tarefa | Responsável | Prazo | Issue |
| :--- | :--- | :--- | :--- |
| Registrar os ambientes no repositório de medidas da Fase 04 | Luiz Henrique e Maria Eduarda | 10/11/2026 | #110 |
| Iniciar a coleta das métricas de G3 (Flexibilidade) | Maria Eduarda | 10/11/2026 | #113 |
| Iniciar a coleta das métricas de G1 (Manutenibilidade) | Christopher | 11/11/2026 | #111 |
| Iniciar a coleta das métricas de G2 (Confiabilidade) | Luiz Henrique | 11/11/2026 | #112 |

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| :---: | :---: | :--- | :--- | :--- |
| `1.0` | 10/11/2026 | Registro da ata de reunião do teste piloto das instruções de avaliação da Fase 03 | [Maria Eduarda](https://github.com/eduarda-ogomes) | [Christopher Paraizo](https://github.com/wChrstphr) |
