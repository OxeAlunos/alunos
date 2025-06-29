from Livro import Livro

class Biblioteca:

    def __init__(self):
        self.livros = []
        
    def vizualizarDados(self, livro: Livro):
        print(livro.autor, livro.nome, livro.genero, livro.disponivel)
        return f'{livro.autor}, {livro.nome}, {livro.genero}, {livro.disponivel}'

        
    def adicionarLivro(self):
        return 'adicionar livros'
    
    def emprestarLivro(self, livro: Livro):
        if livro.disponivel == True:
            livro.disponivel = False
            print("livro emprestado!")
            return 'livro emprestado!'

    def devolverLivro(self, livro: Livro):
        if livro.disponivel == False:
            livro.disponivel = True
            print("Livro devolvido!")
            return 'livro devolvido'
            
    def listarLivros(self):
        livrosListados = []
        for chave, valor in enumerate(self.livros):
            valor: Livro
            
            dadosLivros = {'autor': valor.autor, 'nome': valor.nome, 'genero': valor.genero,'expiracao': valor.expiracao}
            
            livrosListados.append(dadosLivros)
        return livrosListados
    
    def buscarAutor(self):
        return 'buscando por autor'
    
    def buscarTitulo(self):
        return 'buscando por titulo'
    

