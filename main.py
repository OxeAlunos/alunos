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


# Recurso -> Um local onde podemos pegar algo

# Como que faz GET
@app.get('/livros')
def listarLivros():
    return bib.livros

# Utiliza a ? + o nome dos parametros ex: isbn=1234567890123
# Pode colocar + do que um
@app.get('/livros/isbn')
def buscarPorISBN(isbn: str):
    return bib.buscarIsbn(isbn)
    #faz algo

#GET POR PARAMETRO -> Ele já pega o que vem após 
@app.get("/livros/{isbn}")
def read_item(isbn):
    return bib.buscarIsbn(isbn)

#---------------------------------------------------------------------- #


@app.delete('livros/{isbn}')
def deletarLivro(isbn):
    # um loop | pegaria o indice do livro | e usaria o self.livros.pop(indice)
    # self.livros.remove()
    return bib.deletarLivro(isbn)

# --------------------------------------------------------------------- #

from pydantic import BaseModel

class ObjLivro(BaseModel):
    nome: str
    isbn: str
    autor: str
    genero: str

@app.post("/livro/adicionar")
def adicionarLivro(livro: OBJLivro):
    return bib.adicionarLivro(livro)


# -------------------------------------------------------------------- #
from pydantic import BaseModel

class ObjLivro(BaseModel):
    nome: str
    isbn: str
    autor: str
    genero: str

@app.put('livros/')
def atualizarLivro(li: OBJLivro):
    # percorreria a lista dos livros
    for livro in self.livros:
    # acharia o livro que tem o isbn igual
        if livro.isbn == li.isbn:
    # depois atualizaria os dados
            livro.isbn = li.isbn
            livro.nome = li.nome
            livro.autor = li.autor
            livro.genero = li.genero
    # e retornava o livro com os dados atualizados
            return livro
    return bib.atualizarLivro(livro)





# --------------------------------------------------------------- #



@app.post('/livro/autor')
def listar_por_autor(aut: str):
    return bib.buscarAutor(aut)

@app.post('/livro/nome')
def listar_por_nome(nome: str):
    return bib.buscarTitulo(nome)

@app.post('/livro/isbn')
def listar_por_isbn(isbn: str):
    return bib.buscarIsbn(isbn)


@app.put('/livro/emprestar')
def emprestarLivro():
    return bib.emprestarLivro(bib.livros[0])

@app.put('/livro/devolver')
def devolverLivro():
    # nessa rota deve haver uma página com uma lista dos livros emprestados, né?
    return bib.devolverLivro(bib.livros[0])