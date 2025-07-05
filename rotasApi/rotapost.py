from rotasApi.rotaget import bib
from OBJLivro import OBJLivro
from fastapi import APIRouter

router = APIRouter()

@router.post("/livros/adicionar")
def adicionarLivro(livro: OBJLivro):
    return bib.adicionarLivro(livro)

# de POST para GET: POST retornava método not allowed 


