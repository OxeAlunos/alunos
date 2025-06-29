from fastapi import FastAPI
from Biblioteca import Biblioteca
from Livro import Livro
import pandas as pd


app = FastAPI()
bib = Biblioteca()

livroTeste1 = Livro('josé','a casa', 'terror', True)
bib.livros.append(livroTeste1)


@app.get('/')
def mainRoute():
    return 'rota principal'

@app.get('/emprestarLivro')
def emprestarLivro():
    return bib.emprestarLivro(bib.livros[0])

@app.get('/devolverLivro')
def devolverLivro():
    # nessa rota deve haver uma página com uma lista dos livros emprestados, né?
    return bib.devolverLivro(bib.livros[0])

@app.get('/listarLivros')
def listarLivros():
    return bib.listarLivros()

@app.post('/adicionarLivro')
def adicionarLivro():
    return bib.adicionarLivro()

@app.post('/buscarTitulo')
def buscarTitulo():
    return bib.buscarTitulo()

@app.post('/buscarAutor')
def buscarAutor():
    return bib.buscarAutor()
