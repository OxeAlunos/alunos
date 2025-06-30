from fastapi import FastAPI
from Biblioteca import Biblioteca
from OBJLivro import OBJLivro
from Livro import Livro
import pandas as pd


app = FastAPI()
bib = Biblioteca()

@app.get('/')
def mainRoute():
    return 'rota principal'

@app.get('/livros')
def listarLivros() -> list[OBJLivro]:
    return bib.listarLivros()

@app.post("/livros/adicionar")
def adicionarLivro(livro: OBJLivro):
    return bib.adicionarLivro(livro)

@app.post('/livro/nome')
def listar_por_nome(nome: str):
    return bib.buscarTitulo()

@app.post('/livro/autor')
def listar_por_autor(aut: str):
    return bib.buscarAutor(aut)

@app.post('/livro/isbn')
def listar_por_isbn(isbn: int):
    return bib.buscarIsbn(isbn)


@app.put('/livro/emprestar')
def emprestarLivro():
    return bib.emprestarLivro(bib.livros[0])

@app.put('/livro/devolver')
def devolverLivro():
    # nessa rota deve haver uma página com uma lista dos livros emprestados, né?
    return bib.devolverLivro(bib.livros[0])