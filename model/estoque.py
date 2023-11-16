from model.produto import Produto

class Estoque:
    def __init__(self, id: int = None, qty: int = None):
        self.id = id
        self.produto = Produto()
        self.qty = qty


    def __str__(self):
        return f'{self.id}, {self.produto}, {self.qty}'

    def __repr__(self):
        return f'{self.id}, {self.produto}, {self.qty}'



if __name__ == '__main__':


    estoque = Estoque()

    estoque.id = 1

    estoque.produto.nome = 'macarrao'
    estoque.produto.preco = 20

    estoque.qty = 15

    print(estoque)