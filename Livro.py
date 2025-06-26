class Livro:
    def __init__(self, autor, nome, genero):
        self.autor = autor
        self.nome = nome
        self.genero = genero





    def __str__(self):
        return f"Livro:   {self.nome}, Autor: {self.autor}, Genero: {self.genero}"