class Endereco:
    def __init__(self, bairro: str, rua: str, numero_casa: str, cidade: str, estado: str, cep: str, complemento: str):
        self.bairro = bairro
        self.rua = rua
        self.numero_casa = numero_casa
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.complemento = complemento

    def retornar_endereco_resumido(self):
        return f"Endereço: {self.rua}, {self.numero_casa}, {self.bairro}"
    








