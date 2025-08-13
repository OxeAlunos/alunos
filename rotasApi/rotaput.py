from rotasApi.rotaget import bib
from fastapi import APIRouter

router = APIRouter()

@router.put('/livro/emprestar')
def emprestarLivro():
    return bib.emprestarLivro(bib.livros[0])

@router.put('/livro/devolver')
def devolverLivro():
    # nessa rota deve haver uma página com uma lista dos livros emprestados, né?
    return bib.devolverLivro(bib.livros[0])