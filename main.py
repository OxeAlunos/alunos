from fastapi import FastAPI
from Biblioteca import Biblioteca
from OBJLivro import OBJLivro
from Livro import Livro
# import pandas as pd


app = FastAPI()
bib = Biblioteca()

@app.get('/')
def mainRoute():
    return 'rota principal'

@app.get('/livros')
def listarLivros():
    # return bib.listarLivros()
    return bib.livros

@app.post("/livros/adicionar")
def adicionarLivro(livro: OBJLivro):
    return bib.adicionarLivro(livro)

# de POST para GET: POST retornava método not allowed 

@app.get('/livro/autor')
def listar_por_autor(aut: str):
    return bib.buscarAutor(aut)

@app.get('/livro/nome')
def listar_por_nome(nome: str):
    return bib.buscarTitulo(nome)

@app.get('/livro/isbn')
def listar_por_isbn(isbn: str):
    return bib.buscarIsbn(isbn)


@app.put('/livro/emprestar')
def emprestarLivro():
    return bib.emprestarLivro(bib.livros[0])

@app.put('/livro/devolver')
def devolverLivro():
    # nessa rota deve haver uma página com uma lista dos livros emprestados, né?
    return bib.devolverLivro(bib.livros[0])