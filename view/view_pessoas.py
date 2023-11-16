from model.pessoas import ClienteJuridico, ClienteFisico, Funcionario, Gerente, Cargo
from model.endereco import Endereco
from model.produto import Produto
from model.estoque import Estoque


if __name__ == '__main__':
    produto = Produto(1, 'chocolate', 20.0)
    estoque = Estoque()
    endereco = Endereco(1, 'rio', 'cascadura', 'ferraz', 14)
    funcionario = Funcionario()


    estoque.id = 1
    estoque.produto = 'chocolate'
    estoque.qty = 20

    funcionario.id = 1
    funcionario.nome = 'thiago'
    funcionario.endereco = endereco

    cargo = Cargo('desenvolvedor', 3000)

    funcionario.cargo = cargo

    print(funcionario)

    # pj = ClienteJuridico()
    # pj.id = 1
    # pj.nome = 'th'
    # pj.endereco = endereco
    # pj.ramo = 'desenvolvimento'
    # pj.email = '@algumacoisa'
    # pj.cnpj = '132435718'
    # print(pj)