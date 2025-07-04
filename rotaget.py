from main import app, bib 


@app.get('/')
def mainRoute():
    return 'rota principal'

@app.get('/livros')
def listarLivros():
    # return bib.listarLivros()
    return bib.livros


@app.get('/livro/autor')
def listar_por_autor(aut: str):
    return bib.buscarAutor(aut)

@app.get('/livro/nome')
def listar_por_nome(nome: str):
    return bib.buscarTitulo(nome)

@app.get('/livro/isbn')
def listar_por_isbn(isbn: str):
    return bib.buscarIsbn(isbn)

