from main import app, bib
from OBJLivro import OBJLivro

@app.post("/livros/adicionar")
def adicionarLivro(livro: OBJLivro):
    return bib.adicionarLivro(livro)

# de POST para GET: POST retornava método not allowed 


