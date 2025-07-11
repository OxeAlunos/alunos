from main.Endereco import Endereco

class Usuario:
    def __init__(self, nome, idade, cpf, email, telefone, endereco: Endereco):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

    def login(self):
        print('login')
    def logoff(self):
        print('logoff')
    

    
    
    
    
