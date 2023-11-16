from model.pessoas import Cliente, Funcionario

class Produto:
    def __init__(self, id: int = None, nome: str = None, preco: float = None) -> None:
        self.id = id
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f'{self.id}, {self.nome}, {self.preco}'

    def __repr__(self):
        return f'{self.id}, {self.nome}, {self.preco}'

class ClientesProdutosComprados:

    def __init__(self, cliente: Cliente, produto:Produto, qty: int = None, atendente:Funcionario = None):
        self.cliente = cliente
        self.produto = produto
        self.atendente = atendente
        self.qty = qty

    def __str__(self):
        return f'{self.cliente},\n {self.produto},\n {self.qty}'

    def __repr__(self):
        return f'{self.cliente}, {self.produto}, {self.qty}'
