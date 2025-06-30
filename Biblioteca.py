from Livro import Livro
from OBJLivro import OBJLivro

class Biblioteca:

    def __init__(self):
        self.livrosPadrao = [
            Livro('josé','a casa', 'terror', True, '1234567890123', '1'),
            Livro('kaleb','sense life', 'ação', True, '1234567890123', '2'),
            Livro('curió','dicas de mat', 'educação', True, '1234567890123', '3')
        ]
        self.livros = []
        self.livros.append(self.livrosPadrao)
        
    def listarLivros(self):
        livrosListados = []
        for chave, valor in enumerate(self.livros):
            valor: Livro
            
            dadosLivros = {
                'autor': valor.autor,
                'nome': valor.nome,
                'genero': valor.genero,
                'expiracao': valor.expiracao,
                'isbn': valor.isbn,
                'disponibilidade': valor.disponivel
            }
            
            livrosListados.append(dadosLivros)
        return livrosListados
    
    def vizualizarDados(self, livro: Livro):
        print(livro.autor, livro.nome, livro.genero, livro.expiracao,livro.disponivel, livro.isbn)
        return f'{livro.autor}, {livro.nome}, {livro.genero}, {livro.disponivel}, {livro.expiracao}, {livro.isbn}'
    
    def buscarAutor(self, aut: str):
        
        listAut: list[Livro] = []

        for li in self.livros:
            li: Livro
            if li.autor == aut:
                listAut.append(li)

        return listAut
    
    def buscarTitulo(self, nome:str):
            
        listNome: list[Livro] = []

        for li in self.livros:
            li: Livro
            if li.nome == nome:
                listNome.append(li)    

        return listNome
    
    def buscarIsbn(self, isbn:int):
           
        listIsbn: list[Livro] = []
        
        for li in self.livros:
            li: Livro
            if li.isbn == isbn:
                listIsbn.append(li)    

        return listIsbn
        
    def adicionarLivro(self, livro: OBJLivro):
        self.livros.append(Livro(livro.nome, livro.autor, livro.genero, livro.expiracao, livro.disponivel, livro.isbn))
        return 'livro adicionado com sucesso'
    
    def emprestarLivro(self, livro: OBJLivro):
        if livro.disponivel == True:
            livro.disponivel = False
            print("livro emprestado!")
            return 'livro emprestado!'

    def devolverLivro(self, livro: OBJLivro):
        if livro.disponivel == False:
            livro.disponivel = True
            print("Livro devolvido!")
            return 'livro devolvido'
            
    

