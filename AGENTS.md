# Instruções para agentes

## Escrita da documentação

- **Critérios de avaliação orientam o trabalho, não o texto.** Use os critérios do trabalho final para fazer o melhor conteúdo possível, mas não escreva que uma página "atende ao critério X" nem cite códigos como F2-C5.
- **Sem seção "Objetivos" com tabela de objetivo e seção.** Ela ocupa espaço sem acrescentar conteúdo.
- **Regra 80/20.** Cada página traz só o mais importante para o leitor. Corte repetições, explicações sobre a própria página e detalhes operacionais.
- **Tom acadêmico e profissional.** Texto direto e objetivo, com afirmações ligadas às fontes.
- **Sem travessão nem ponto e vírgula.** Use dois-pontos, vírgula, "e" ou divida a frase. Itens de lista terminam com ponto.
- **Linkar em vez de repetir.** Antes de escrever uma regra, procure se ela já existe em outra página (fichas do GQM, níveis de pontuação, Plano GQM, instruções do avaliador). Se existir, aponte para a seção exata em vez de copiar fórmulas, faixas ou tabelas.
- **Cada conteúdo na sua fase.** Uma página de plano não traz quadros a preencher com resultados. Confira nas issues da fase seguinte onde cada conteúdo será publicado.
- **Alinhar com as issues.** Caminhos de arquivos, pastas e scripts citados numa página seguem o que as issues já definem (por exemplo, `dados/fase-04/brutos/` e `consolidados/`). Se houver divergência, resolva antes de escrever.
- **Fidelidade às fontes.** Parafraseie sem acrescentar o que a fonte não diz e não afirme mais do que as páginas do repositório sustentam. Exemplos com dados inventados são marcados como fictícios.

## Formato das páginas

- **Introdução e Metodologia** abrem a página, em texto corrido. O objetivo da página cabe numa frase da introdução.
- **Citações** no formato `[[1, p. 46]](#ref-1)`, com a referência em `> <Link id="ref-1">1.</Link> ...` e `import Link from '@docusaurus/Link';` no topo.
- **Tabelas** com `<p className="tabela-titulo">Tabela N: ...</p>` acima e `<p className="tabela-fonte">Fonte: ...</p>` abaixo. Tabela da equipe: `Fonte: [Christopher Paraizo](https://github.com/wChrstphr), 2026.`, ou o nome do autor no mesmo formato.
- **Histórico de versões** com o autor no formato acima e a coluna Revisor(es) vazia.

## Links e verificação

- **Âncoras:** títulos repetidos numa página (como "2º Hipóteses de baseline") ganham sufixo no Docusaurus. Prefira linkar a seção de nível acima, que é única.
- **Build:** `npm run build` deve passar antes do commit. Ele falha com link quebrado, mas não com âncora quebrada, que precisa ser conferida à parte.

## Git

- Branch nova a partir de `origin/main`, sem `main` como upstream, para que um `git push` não vá direto para a `main`.
- Mensagens de commit `docs: <verbo no infinitivo> ...`, em português, sem linhas de coautoria.
