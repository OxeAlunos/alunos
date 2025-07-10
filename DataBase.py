import pandas as pd
from pandas import DataFrame
from OBJLivro import OBJLivro 
from Livro import Livro


path = "./dados.xlsx"
books_sheet = 'Livros'
users_sheet = 'Usuarios'
lendings_sheet = 'Emprestimos'
devolutions_sheet = 'Devolucoes'

bdf = pd.read_excel(path, books_sheet)
udf = pd.read_excel(path, users_sheet)
ldf = pd.read_excel(path, lendings_sheet)
ddf = pd.read_excel(path, devolutions_sheet)

def adicionarLivro(livro):
    novo_registro = pd.DataFrame(data={
        'nome': [livro.nome],
        'autor': [livro.autor],
        'genero': [livro.genero], 
        'isbn': [livro.isbn]
        })
    
    global bdf
    global path
    bdf = pd.concat([bdf, novo_registro], ignore_index=True)
    salvarDadosNoExcel()
    # bdf.to_excel(path,books_sheet)

def salvarDadosNoExcel():
    with pd.ExcelWriter(path) as writer:  
        bdf.to_excel(writer, books_sheet, index=False)
        udf.to_excel(writer, users_sheet, index=False)
        ldf.to_excel(writer, lendings_sheet, index=False)
        ddf.to_excel(writer, devolutions_sheet, index=False)

def listarLivros():
    print(bdf)
    # return bdf

def listarEmprestimos():
    return


if __name__ == '__main__':
   li = Livro('aaadw','adawd','awdawd','awdawd','1234567890123','2001')
   adicionarLivro(li)
   listarLivros()

    # bdf = bdf.drop(bdf.index)
    # bdf = bdf.drop(columns= bdf.columns)
    # salvarDadosNoExcel()
    # listarLivros()
