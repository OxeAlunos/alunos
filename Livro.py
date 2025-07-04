class Livro:
    def __init__(self, nome, autor, genero, editora, isbn='', ano_publicacao=''):
        #Verificação da Expiração do Livro
        expiracao = ''
        if genero.lower() == 'escolar' and not ano_publicacao:
            raise ValueError("O livro é escolar porém não foi colocado o seu ano.")
        
            
        
        #Verificação do ISBN o Livro:
        if isbn.isalpha():
            return False
        if isbn != '' and len(isbn) < 13 or len(isbn) < 13:
            raise ValueError("O ISBN está errado e/ou imcompleto")
        
        #Verificação do Ano de Publicação:
        if ano_publicacao.isalpha():
            return False
        


        self.autor = autor
        self.nome = nome
        self.genero = genero
        self.editora = editora
        self.isbn = isbn
        
        #Validade da Expiração do Livro
        self.ano_publicacao = ano_publicacao
        if genero.lower() == 'escolar':
            expiracao = int(self.ano_publicacao) + 4
        self.expiracao = expiracao    
        
        #o self.ano_publicacao está na linha 29
        #o self.ano_expiracao está na linha 32


            
        
        
    def __str__(self):

        return f"Livro:{self.nome}, Autor: {self.autor}, Genero: {self.genero}, Editora: {self.editora}, ISBN: {self.isbn},Ano de Publicação : {self.ano_publicacao}, Expiração : {self.expiracao}"
    
livro = Livro('1984', 'George Owell', 'Ficção', 'Principis', '1234567890123', '1984')
livro2 = Livro('Boiologia', 'Dr.Chpatim', 'Escolar', '2+2=5', '0123456789101', '2020') 
print(f'{livro} \n {livro2}')


  

#Fazer a Expiração do Livro, caso o Livro seja do genêro escolar
#O isbn não é obrigatório, neste tópico ele se comporta que nem a expiração
#Fazer uma verificação da quantidade de caracteres (tem que ser 13 caracteres)
#o isbn vai ser do tipo str e para a verificação utilizar o isalpha para conferir se tem letra
#ano_expiração = o ano que o livro foi criado, expiração = a expiração do livro (validade)
#a expiração do livro é o ano da expiração + 4
#Verificar se tem o ano de Publicação