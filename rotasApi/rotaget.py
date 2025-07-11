from fastapi import APIRouter
from main.Biblioteca import Biblioteca

bib = Biblioteca()

router = APIRouter()

@router.get('/')
def mainRoute():
    return 'rota principal'

@router.get('/livros')
def listarLivros():
    # return bib.listarLivros()
    return bib.livros


@router.get('/livro/autor')
def listar_por_autor(aut: str):
    return bib.buscarAutor(aut)

@router.get('/livro/nome')
def listar_por_nome(nome: str):
    return bib.buscarTitulo(nome)

@router.get('/livro/isbn')
def listar_por_isbn(isbn: str):
    return bib.buscarIsbn(isbn)

