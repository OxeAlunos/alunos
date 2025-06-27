class Livro:
    def __init__(self, autor, nome, genero, disponibilidade):
        self.autor = autor
        self.nome = nome
        self.genero = genero
        self.disponibilidade = disponibilidade
        self.lista = []

    def expirar_livro(self, genero, expiracao):
        self.expiracao = expiracao
        super().__init__(genero)
        if genero == 'Escolar':

    def salvar_livro(self,):
        




    def __str__(self):
        return f"Livro:   {self.nome}, Autor: {self.autor}, Genero: {self.genero}"
    
#Precisa colocar a expiração no caso de livros escolares
#tem que fazer uma condição em que: se o livro for escolar, tem que colocar a expiração. Se não for, não pedir.