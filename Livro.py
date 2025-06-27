class Livro:
    def __init__(self, autor, nome, genero, expiracao):
        self.autor = autor
        self.nome = nome
        self.genero = genero
        self.expiracao = expiracao
      

    def expirar(self, expiracao, genero):
        if genero == "escolar":
            return 'Digite a Expiração do livro'
        else:
           pass
    
    
    def __str__(self):
        return f"Livro:   {self.nome}, Autor: {self.autor}, Genero: {self.genero}, Expiração : {self.expiracao}"
    
livro = Livro('1984', 'George Owell', 'Ficção', "001 ") 
print(livro)  
mensagem = livro.expirar(expiracao = "001 ")
print(mensagem)
#Fazer a Expiração do Livro, caso o Livro seja do genêro escolar