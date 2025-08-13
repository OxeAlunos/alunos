import pandas as pd
from pandas import DataFrame
from OBJLivro import OBJLivro 
from Livro import Livro
from usuario import Usuario
from endereco import Endereco


path = "./dados.xlsx"
books_sheet = 'Livros'
users_sheet = 'Usuarios'
lendings_sheet = 'Emprestimos'
devolutions_sheet = 'Devolucoes'

bdf = pd.read_excel(path, books_sheet)
udf = pd.read_excel(path, users_sheet)
ldf = pd.read_excel(path, lendings_sheet)
ddf = pd.read_excel(path, devolutions_sheet)

def add_book(livro):
    novo_registro = pd.DataFrame(data={
        'nome': [livro.nome],
        'autor': [livro.autor],
        'genero': [livro.genero], 
        'isbn': [livro.isbn]
        })
    
    global bdf
    global path
    bdf = pd.concat([bdf, novo_registro], ignore_index=True)
    save_data_to_excel()
    # bdf.to_excel(path,books_sheet)

def add_user(usuario: Usuario):
    novo_registro = pd.DataFrame(data={
        'nome': [usuario.nome],
        'idade': [usuario.idade],
        'cpf': [usuario.cpf], 
        'email': [usuario.email],
        'telefone': [usuario.telefone],
        'endereco': [usuario.endereco]
        })
    
    global udf
    global path
    udf = pd.concat([udf, novo_registro], ignore_index=True)
    save_data_to_excel()

def register_lending():
    return
def register_devolution():
    return

def save_data_to_excel():
    with pd.ExcelWriter(path) as writer:  
        bdf.to_excel(writer, books_sheet, index=False)
        udf.to_excel(writer, users_sheet, index=False)
        ldf.to_excel(writer, lendings_sheet, index=False)
        ddf.to_excel(writer, devolutions_sheet, index=False)

def list_books():
    print(bdf)
    # return bdf

def list_users():
    print(udf)

def list_lendings():
    print(udf)

def list_devolutions():
    print(udf)

if __name__ == '__main__':
   li = Livro('aaadw','adawd','awdawd','awdawd','1234567890123','2001')
   add_book(li)
   list_books()

   us = Usuario('abc',123,'12345678901','abcde@gmail.com','1212341234','rua1')
   add_user(us)
   list_users()

    # bdf = bdf.drop(bdf.index)
    # bdf = bdf.drop(columns= bdf.columns)
    # salvarDadosNoExcel()
    # listarLivros()
