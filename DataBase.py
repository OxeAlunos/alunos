import pandas as pd
from pandas import DataFrame
from OBJLivro import OBJLivro 
from Livro import Livro

class DataBase:

    def __init__(self):        
        
        self.path = "C:/Users/aluno_pnd/Desktop/alunos/dados.xlsx"

        self.books_sheet = 'Livros'
        self.users_sheet = 'Usuarios'
        self.lendings_sheet = 'Emprestimos'
        self.devolutions_sheet = 'Devolucao'

        self.bdf = pd.read_excel(self.path, self.books_sheet)
        self.udf = pd.read_excel(self.path, self.users_sheet)
        self.ldf = pd.read_excel(self.path, self.lendings_sheet)
        self.ddf = pd.read_excel(self.path, self.devolutions_sheet)

    def adicionarLivro(self, livro: OBJLivro, dataFrame: DataFrame):
        novo_registro = {
            'nome': livro.nome,
            'autor': livro.autor,
            'genero': livro.genero, 
            'expiracao': livro.expiracao, 
            'disponivel': livro.disponivel,
            'isbn': livro.isbn
            }
        
        novo_bdf = pd.DataFrame([novo_registro])
        df = pd.concat([dataFrame, novo_bdf])
        return df



    def listarLivros(self):
        print(self.bdf)
        # return bdf

    def listarEmprestimos():
        return


 