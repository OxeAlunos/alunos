from pydantic import BaseModel

class OBJLivro(BaseModel):
    nome: str
    autor: str
    genero: str 
    expiracao: str
    disponivel: bool
    isbn: str