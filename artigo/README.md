# Artigo

O workflow `.github/workflows/latex.yml` compila `main.tex` com `pdflatex` a
cada pull request que altere `artigo/**` e publica o PDF como o artefato
`artigo-pdf` da execucao. Se o arquivo principal mudar (por exemplo, ao adotar
o modelo SBC), atualize `root_file` e o caminho do artefato no workflow.

O PDF e gerado pelo workflow e nao deve ser versionado. Para testar manualmente
no GitHub, use **Actions > Build LaTeX article > Run workflow**.
