class Livro:
    def __init__(self, autor, nome, genero, disponibilidade, isbn='não tem', expiracao=''):
        #Expiração do Livro
        if genero == 'escolar' and not expiracao:
            raise ValueError("O livro é escolar porém não foi colocado uma expiração")
        
        self.autor = autor
        self.nome = nome
        self.genero = genero
        self.expiracao = expiracao
        self.disponivel = disponibilidade
        self.isbn = isbn

        #Isbn do Livro
        string_isbn = str(isbn)
        tamanho = len(string_isbn)
        if isbn == 'não tem':
            pass
        elif isbn != 'não tem' and tamanho < 13:
            return ValueError("O ISBN está errado e/ou imcompleto")
        else:
            pass



        
      

    
    
    
    def __str__(self):
        return f"Livro:{self.nome}, Autor: {self.autor}, Genero: {self.genero},ISBN: {self.isbn} Expiração : {self.expiracao}"
    
#livro = Livro('1984', 'George Owell', 'Ficção', " ") 
#print(livro)  
#mensagem = livro.expirar(expiracao = "001 ")
#print(mensagem)
#Fazer a Expiração do Livro, caso o Livro seja do genêro escolar
#O isbn não é obrigatório, neste tópico ele se comporta que nem a expiração
#Fazer uma verificação da quantidade de caracteres (tem que ser 13 caracteres)
#o isbn vai ser do tipo int e para a verificação fazer a conversão para str