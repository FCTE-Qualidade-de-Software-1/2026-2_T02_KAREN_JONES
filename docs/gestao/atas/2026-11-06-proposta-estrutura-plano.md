---
title: "Ata: 06/11/2026 (Proposta da estrutura do plano da Fase 3)"
description: Apresentação e validação da proposta de estrutura do plano de avaliação da Fase 03 (Issue #94).
---

# Ata da reunião: 06/11/2026

| Campo | Valor |
| :--- | :--- |
| **Data e horário** | 06/11/2026, assíncrono (sem horário fixo) |
| **Local** | Remoto assíncrono (apresentação em vídeo dos slides) |
| **Fase** | Fase 03: Projetar a avaliação |
| **Redator(a)** | Letícia de Carvalho |
| **Gravação** | Não houve gravação de reunião; a proposta foi apresentada em vídeo com os slides |

## Participantes

- [x] Christopher
- [x] Davi Pierre
- [x] Gabriel Monteiro
- [x] Letícia de Carvalho
- [x] Luiz Henrique Soares
- [x] Maria Eduarda

Todos os integrantes assistiram à apresentação e deram o ok.

## Pauta

1. Escopo quantitativo: do GQM ao plano operacional.
2. Arquitetura documental: quem especifica cada parte do plano.
3. Exemplo executável da métrica M3.2.1 (tempo de abertura por tamanho de cena).
4. Como os dados viram um julgamento (escala ordinal e regras de agregação).
5. Sequência de execução, pendências da Fase 02 para a 03 e aceite da Issue #94.

## Discussão

- **Escopo:** G1 (Manutenibilidade) com 14 métricas e 5 questões, G2 (Confiabilidade) com 10 métricas e 4 questões, e G3 (Flexibilidade) com 12 métricas e 4 questões. Esses dados foram fixados na Fase 02 e não serão redefinidos na execução. A referência reproduzível é o commit e1b7aac, de 18/10/2026.
- **Arquitetura documental:** o plano é dividido em seis blocos, cada um ligado a uma issue e a um responsável: método (`metodo-avaliacao.md`, #95), recursos e ambiente (`recursos-ambiente.md`, #96), roteiros (`instrucoes-g1/g2/g3.md`, #98 a #100), análise (`plano-analise.md`, #101), tempos (`cronograma-avaliacao.md`, #102) e rastreio (`visao-geral.md` + `_category_.json`, #104). A massa de dados e os scripts são artefatos de apoio (#97).
- **Exemplo executável (M3.2.1):** entradas padronizadas de 100, 1.000, 5.000 e 10.000 elementos; cada cena é aberta 5 vezes, mede-se o tempo de abertura em ms, calcula-se a mediana por tamanho e registram-se navegador, hardware e logs. As evidências vão para `dados/fase-04/brutos/`.
- **Análise:** dado bruto, métrica, questão e depois G1/G2/G3, com escala ordinal de 1 a 5. As regras de agregação são: sem arredondamento intermediário, empate exato em 0,5 arredonda para baixo, e mais de 50% de métricas ausentes torna o resultado inconclusivo.
- **Pendências da Fase 02 para a 03:** versões, máquinas, Docker e dispositivo touch/pen; cena de referência e cenas de escala com arquivos inválidos; evidências, gravação de tela e critérios objetivos; divergência entre "Portabilidade" e "Flexibilidade".

## Decisões

| # | Decisão | Justificativa |
| :--- | :--- | :--- |
| 1 | Validar a arquitetura documental do plano e os responsáveis por cada parte. | Critério de aceite da Issue #94; todos os integrantes assistiram à proposta e aprovaram. |

## Encaminhamentos

Os prazos abaixo são os marcos previstos na proposta.

| Tarefa | Responsável | Prazo | Issue |
| :--- | :--- | :--- | :--- |
| Especificar o método de avaliação | [Davi Pierre](https://github.com/DaviPierre) | 06/11/2026 | #95 |
| Especificar recursos e ambiente | [Leticia Santos](https://github.com/LeticiaSantosss)| 05/11/2026| #96 |
| Montar a massa de dados e os scripts de apoio | [Gabriel Monteiro](https://github.com/GabrielSMonteiro)| 06/11/2026 | #97 |
| Escrever as instruções de avaliação de G1, G2 e G3 | [Davi Pierre](https://github.com/DaviPierre), [Leticia Santos](https://github.com/LeticiaSantosss) e [Gabriel Monteiro](https://github.com/GabrielSMonteiro)| 07/11/2026 | #98, #99 e #100 |
| Especificar o plano de análise | [Christopher](https://github.com/wChrstphr) | 06/11/2026 | #101 |
| Montar o cronograma de avaliação | [Leticia Santos](https://github.com/LeticiaSantosss) | 06/11/2026 | #102 |
| Executar o piloto independente das instruções | [Maria Eduarda](https://github.com/eduarda-ogomes)| 08/11/2026 | #103 |
| Montar a rastreabilidade | [Davi Pierre](https://github.com/DaviPierre) | 08/11/2026 | #104 |