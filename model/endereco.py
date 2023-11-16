class Endereco:
    def __init__(self, id: int = None, cidade: str = None, bairro: str = None, rua: str = None,
                 numero: int = None) -> None:
        self.id = id
        self.cidade = cidade
        self.bairro = bairro
        self.rua = rua
        self.numero = numero

    def __str__(self):
        return f'{self.id}, {self.cidade}, {self.bairro}, {self.rua}, {self.numero}'

    def __repr__(self):
        return f'{self.id}, {self.cidade}, {self.bairro} , {self.rua}, {self.numero}'
