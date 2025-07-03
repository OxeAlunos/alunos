from Livro import Livro
from OBJLivro import OBJLivro

class Biblioteca:

    def __init__(self):
        self.livrosPadrao = [
            Livro('josé','a casa', 'terror', True, None , '1234567890123'),
            Livro('kaleb','sense life', 'ação', True, None,'1234567890123'),
            Livro('curió','dicas de mat', 'educação', True, '3', '1234567890123')
        ]
        self.livros = []
        # self.livros.append(self.livrosPadrao)
        self.livros.extend(self.livrosPadrao)
        
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
    
    # faz basicamente a mesmo coisa que os métodos de busca
    # def vizualizarDados(self, livro: Livro):
    #     print(f'{livro.autor}, {livro.nome}, {livro.genero}, {livro.disponivel}, {livro.expiracao}, {livro.isbn}')
    #     return f'dados do requerido livro:' \
    #         f'{livro.autor}, {livro.nome}, {livro.genero}, ' \
    #         f'{livro.disponivel}, {livro.expiracao}, {livro.isbn}'
    
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
    
    def buscarIsbn(self, isbn:str):
           
        listIsbn: list[Livro] = []
        
        for li in self.livros:
            li: Livro
            if li.isbn == isbn:
                listIsbn.append(li)    

        return listIsbn
        
    def adicionarLivro(self, livro: OBJLivro):
        self.livros.append(Livro(livro.nome, livro.autor, livro.genero, livro.disponivel, livro.expiracao, livro.isbn))
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
            
    

