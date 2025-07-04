from main import app,bib


@app.put('/livro/emprestar')
def emprestarLivro():
    return bib.emprestarLivro(bib.livros[0])

@app.put('/livro/devolver')
def devolverLivro():
    # nessa rota deve haver uma página com uma lista dos livros emprestados, né?
    return bib.devolverLivro(bib.livros[0])