from fastapi import FastAPI
from Biblioteca import Biblioteca
from OBJLivro import OBJLivro
from Livro import Livro
import rotaget
import rotapost
import rotaput


app = FastAPI()
bib = Biblioteca()

