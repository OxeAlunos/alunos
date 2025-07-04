from fastapi import FastAPI
from Biblioteca import Biblioteca
from DataBase import DataBase
from OBJLivro import OBJLivro
from Livro import Livro
import rotaget
import rotapost
import rotaput


app = FastAPI()
bib = Biblioteca()
db = DataBase()
