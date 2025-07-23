import pandas as pd
from pandas import DataFrame
from main.OBJLivro import OBJLivro 
from main.Livro import Livro
from main.Usuario import Usuario
from main.Endereco import Endereco

import datetime as dtm

path = "./dados.xlsx"
books_sheet = 'Livros'
users_sheet = 'Usuarios'
lendings_sheet = 'Emprestimos'
devolutions_sheet = 'Devolucoes'

booksDF = pd.read_excel(path, books_sheet)
usersDF = pd.read_excel(path, users_sheet)
lendingsDF = pd.read_excel(path, lendings_sheet)
devolutionsDF = pd.read_excel(path, devolutions_sheet)

def add_book(livro):
    new_entry = pd.DataFrame(data={
        'nome': [livro.nome],
        'autor': [livro.autor],
        'genero': [livro.genero], 
        'isbn': [livro.isbn]
        })
    
    global booksDF
    global path
    booksDF = pd.concat([booksDF, new_entry], ignore_index=True)
    save_data_to_excel()
    # booksDF.to_excel(path,books_sheet)

def add_user(usuario: Usuario):
    new_entry = pd.DataFrame(data={
        'nome': [usuario.nome],
        'idade': [usuario.idade],
        'cpf': [usuario.cpf], 
        'email': [usuario.email],
        'telefone': [usuario.telefone],
        'endereco': [usuario.endereco]
        })
    
    global usersDF
    global path
    usersDF = pd.concat([usersDF, new_entry], ignore_index=True)
    save_data_to_excel()

def register_lending(livro, usuario):
    new_entry = {
        'nome do livro': [livro.nome],
        'nome do usuario': [usuario.nome],
        'data de emprestimo': [dtm.datetime] 
    }
    return
def register_devolution(livro):
    return

def save_data_to_excel():
    with pd.ExcelWriter(path) as writer:  
        booksDF.to_excel(writer, books_sheet, index=False)
        usersDF.to_excel(writer, users_sheet, index=False)
        lendingsDF.to_excel(writer, lendings_sheet, index=False)
        devolutionsDF.to_excel(writer, devolutions_sheet, index=False)

def list_books():
    
    
    print(booksDF)
    # return booksDF

def list_users():
    print(usersDF)

def list_lendings():
    print(usersDF)

def list_devolutions():
    print(usersDF)

if __name__ == '__main__':
   li = Livro('aaadw','adawd','awdawd','awdawd','1234567890123','2001')
   add_book(li)
   list_books()

   us = Usuario('abc',123,'12345678901','abcde@gmail.com','1212341234','rua1')
   add_user(us)
   list_users()

    # booksDF = booksDF.drop(booksDF.index)
    # booksDF = booksDF.drop(columns= booksDF.columns)
    # salvarDadosNoExcel()
    # listarLivros()
