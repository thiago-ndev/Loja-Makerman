from model.produto import Produto
from model.produto import ClientesProdutosComprados
from model.pessoas import ClienteJuridico, ClienteFisico
from model.estoque import Estoque
from model.endereco import Endereco


if __name__ == '__main__':

    CF = ClienteFisico()
    PJ = ClienteJuridico()

    produto = Produto(1, 'chocolate', 20.0)
    estoque = Estoque()
    endereco = Endereco(1, 'rio', 'cascadura', 'ferraz', 14)

    CF.id = 1
    CF.nome = 'thiago'
    CF.email = "TESTE@GMAIL.com"
    CF.cpf = '12345789'
    CF.endereco = endereco
    CF.data_nasc = '30/05/2000'


    compra = ClientesProdutosComprados(CF, produto, 25)

    print(compra)
