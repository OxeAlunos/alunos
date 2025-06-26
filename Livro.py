class Livro:
    def __init__(self, autor, nome, genero, disponibilidade):
        self.autor = autor
        self.nome = nome
        self.genero = genero
        self.disponibilidade = disponibilidade





    def __str__(self):
        return f"Livro:   {self.nome}, Autor: {self.autor}, Genero: {self.genero}"