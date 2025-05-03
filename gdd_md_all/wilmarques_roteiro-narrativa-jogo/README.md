# Roteiro e Narrativa - Atividade prática

## Atividade

Nessa atividade, devemos criar um roteiro de um jogo, incluindo os elementos centrais da narrativa.

Além disso, devemos criar fluxogramas e iniciar o Game Design Document.

## Como gerar o arquivo final

Foram utilizados Mermaid CLI e Pandoc, ambos usando através do Docker.

> Exemplo usando arquivo `gdd.md`.

1. Renderizar os diagramas no arquivo `gdd.md` e referenciá-los no arquivo `gdd.md` gerado no diretório `dist`:

```bash
docker run --rm --volume "`pwd`:/data" -u `id -u`:`id -g` minlag/mermaid-cli -i gdd.md -o dist/gdd.md
```

Esse comando gerará um arquivo `gdd.md` no diretório `dist` referenciando novos arquivos com os diagramas renderizados.

Porém os nomes serão genéricos, como `gdd.md-1.svg`, `gdd.md-2.svg`, etc. Portanto é necessário renomear os arquivos para nomes mais significativos e alterar o arquivo `gdd.md` gerado no diretório `dist` para referenciar os novos nomes.

2. Gerar um arquivo em formato HTML a partir do arquivo `gdd.md` gerado no diretório `dist`:

```bash
docker run --rm --volume "`pwd`:/data" --user `id -u`:`id -g` pandoc/latex dist/gdd.md -o dist/gdd.html
```

3. Gerar o arquivo `gdd.pdf` a partir do arquivo `gdd.html` gerado no diretório `dist`:

Entre em algum navegador e abra o arquivo `gdd.html` gerado no diretório `dist`. Depois, imprima a página como PDF.

> Tentei utilizar Pandoc para esse passo, mas tive alguns problemas.
