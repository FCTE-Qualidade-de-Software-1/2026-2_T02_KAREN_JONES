# Artigo

O artigo usa o modelo para publicação de artigos da Sociedade Brasileira de
Computação (SBC), como permite a Premissa 7 da especificação do trabalho
("2026-2 Trabalho final completo v1.pdf", p. 1). Os arquivos `sbc-template.sty`
(versão de 2017) e `sbc.bst` são cópias sem alteração dos arquivos do modelo
LaTeX da SBC, também disponível no Overleaf como
[SBC Conferences Template](https://www.overleaf.com/latex/templates/sbc-conferences-template/blbxwjwzdngr).

| Arquivo | Conteúdo |
| :--- | :--- |
| `main.tex` | Texto do artigo |
| `bibliography.bib` | Referências, formatadas pelo estilo `sbc.bst` |
| `figura-*.pdf` | Figuras do artigo |
| `contribuicao-e-ia.md` | Rascunho dos apêndices de contribuição e de uso de IA |

## Como compilar

```bash
cd artigo
latexmk -pdf main.tex
```

O `latexmk` roda o `pdflatex` e o `bibtex` quantas vezes forem necessárias.

O workflow `.github/workflows/latex.yml` compila `main.tex` a cada pull request
que altere `artigo/**` e publica o PDF como o artefato `artigo-pdf` da execução.
Para rodar manualmente no GitHub, use **Actions > Build LaTeX article > Run
workflow**. O PDF é gerado pelo workflow e não deve ser versionado.

## Observação sobre o preâmbulo

O `babel` é carregado antes do `sbc-template`. Com o `hyperref` carregado, o
bloco final do `sbc-template.sty` executa `\makeatother` no fim do preâmbulo, e
isso quebra o código do `babel` registrado depois dele.
