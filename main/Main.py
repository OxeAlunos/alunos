from fastapi import FastAPI
from main.Biblioteca import Biblioteca
from main.DataBase import DataBase
from rotasApi import rotaget
from rotasApi import rotapost
from rotasApi import rotaput

app = FastAPI()
db = DataBase()

app.include_router(rotaget.router)
app.include_router(rotapost.router)
app.include_router(rotaput.router)