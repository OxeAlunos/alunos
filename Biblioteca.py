from Livro import Livro
from OBJLivro import OBJLivro
from Usuario import Usuario

class Biblioteca:

    def __init__(self):
        self.livros = []
        
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
    
    def BuscarLivrosEmprestadosDeCadaUsusario(self, livro: OBJLivro):
        livro.emprestados = not livro.disponivel
        Usuario.__init__()
        
    def adicionarLivro(self, livro: OBJLivro):
        self.livros.append(Livro(livro.nome, livro.autor, livro.genero, livro.disponivel, livro.expiracao, livro.isbn))
        return 'livro adicionado com sucesso'
    
    def atualizarDisponibilidadeDevolução(self, livro: OBJLivro):
        self.disponibilidade = not livro.disponivel
    