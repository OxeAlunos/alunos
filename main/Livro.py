class Livro:
    def __init__(self, nome, autor, genero, editora, isbn='', ano_publicacao=''):
        #Verificação da Expiração do Livro
        expiracao = ''
        if genero.lower() == 'escolar' and not ano_publicacao:
            raise ValueError("O livro é escolar porém não foi colocado o seu ano.")
        
        #Verificação do ISBN o Livro:
        if isbn is not None and isbn.isalpha():
            raise ValueError("O ISBN está errado e/ou imcompleto")
        if isbn is not None and len(isbn) < 13:
            raise ValueError("O ISBN está errado e/ou imcompleto")
        
        #Verificação do Ano de Publicação:
        if ano_publicacao.isalpha():
            raise ValueError("O ANO DE PUBLICAÇÃO está errado e/ou imcompleto")

        #Validade da Expiração do Livro
        self.ano_publicacao = ano_publicacao
        if genero.lower() == 'escolar':
            expiracao = int(self.ano_publicacao) + 4
        
            
        
        self.ano_expiracao = expiracao    
        self.autor = autor
        self.nome = nome
        self.genero = genero
        self.editora = editora
        self.isbn = isbn

        #Valores padrões e extras
        self.disponivel = True
        
        
        #o self.ano_publicacao está na linha 29
        #o self.ano_expiracao está na linha 32

    def __str__(self):
        return f"Livro:{self.nome}, Autor: {self.autor}, Genero: {self.genero}, Editora: {self.editora}, ISBN: {self.isbn},Ano de Publicação : {self.ano_publicacao}, Expiração : {self.expiracao}"

    

#Fazer a Expiração do Livro, caso o Livro seja do genêro escolar
#O isbn não é obrigatório, neste tópico ele se comporta que nem a expiração
#Fazer uma verificação da quantidade de caracteres (tem que ser 13 caracteres)
#o isbn vai ser do tipo str e para a verificação utilizar o isalpha para conferir se tem letra
#ano_expiração = o ano que o livro foi criado, expiração = a expiração do livro (validade)
#a expiração do livro é o ano da expiração + 4
#Verificar se tem o ano de Publicação