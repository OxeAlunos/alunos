class Livro:
    def __init__(self, autor, nome, genero, disponibilidade, expiracao='', isbn="",):
        #Expiração do Livro
        if genero == 'escolar' and not expiracao:
            raise ValueError("O livro é escolar porém não foi colocado uma expiração")
        
        
        self.autor = autor
        self.nome = nome
        self.genero = genero
        self.expiracao = expiracao
        self.disponivel = disponibilidade
        self.isbn = isbn

        #Livro ISBN, ISBN = int e string_isbn = string, converte int(isbn) para string(string_isbn)
        string_isbn = str(isbn)
        tamanho = len(string_isbn)
        if isbn == '':
            print(f'O ISbn é: {string_isbn}')
            pass
        elif isbn != '' and tamanho < 13:
            raise ValueError("O ISBN está errado e/ou imcompleto")
        elif isbn != '' and tamanho == 13:
            pass
        else:
            raise ValueError("O ISBN está errado e/ou imcompleto")
        
    def __str__(self):
        return f"Livro:{self.nome}, Autor: {self.autor}, Genero: {self.genero},ISBN: {self.isbn}, Expiração : {self.expiracao}"
    
livro = Livro('1984', 'George Owell', 'Ficção', 1234567890123
 , '') 
#livro.verifcar_caracter()
print(livro.isbn)
  

#Fazer a Expiração do Livro, caso o Livro seja do genêro escolar
#O isbn não é obrigatório, neste tópico ele se comporta que nem a expiração
#Fazer uma verificação da quantidade de caracteres (tem que ser 13 caracteres)
#o isbn vai ser do tipo int e para a verificação fazer a conversão para str