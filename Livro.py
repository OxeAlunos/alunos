class Livro:
    def __init__(self, autor, nome, genero, disponibilidade, expiracao=''):
        #Expiração do Livro
        if genero == 'escolar' and not expiracao:
            raise ValueError("O livro é escolar porém não foi colocado uma expiração")
        
        self.autor = autor
        self.nome = nome
        self.genero = genero
        self.expiracao = expiracao
        self.disponivel = disponibilidade

        
      

    
    
    
    def __str__(self):
        return f"Livro:{self.nome}, Autor: {self.autor}, Genero: {self.genero}, Expiração : {self.expiracao}"
    
#livro = Livro('1984', 'George Owell', 'Ficção', " ") 
#print(livro)  
#mensagem = livro.expirar(expiracao = "001 ")
#print(mensagem)
#Fazer a Expiração do Livro, caso o Livro seja do genêro escolar