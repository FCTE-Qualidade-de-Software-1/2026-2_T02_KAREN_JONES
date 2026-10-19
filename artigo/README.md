# Artigo

`placeholder.tex` e temporario: serve somente para verificar se o GitHub
Actions compila um documento LaTeX e publica o PDF como artefato. Ele nao e o
artigo da Entrega 1 nem usa o modelo SBC.

Quando o fonte oficial do Overleaf estiver nesta pasta, atualize
`.github/workflows/latex.yml` para apontar `root_file` ao arquivo principal do
artigo e renomeie o artefato para `artigo-pdf`. A compilacao deve entao ser
validada com o fonte e os recursos reais do artigo antes de considerar a issue
#33 concluida.

O PDF e gerado pelo workflow e nao deve ser versionado. Para testar manualmente
no GitHub, use **Actions > Build LaTeX article > Run workflow**.
