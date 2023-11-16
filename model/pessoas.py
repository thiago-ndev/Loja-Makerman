from abc import ABC, abstractmethod
from model.endereco import Endereco

class Cliente(ABC):
    def __init__(self, id: int = None, nome: str = None, email: str = None) -> None:
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = None
        self.ativo = True
        self.endereco = Endereco

    def __str__(self):
        return f'{self.id}, {self.nome}, {self.email}, {self.endereco}'

    def __repr__(self):
        return f'{self.id}, {self.nome}, {self.email}, {self.endereco}'

    @abstractmethod
    def calcular_desconto(self, cliente_type) -> int:
        pass

    def comprar_produto(self):
        pass



class ClienteJuridico(Cliente):
    def __init__(self, id=None, nome=None, email=None,
                 cnpj: str = None, ramo: str = None) -> None:
        Cliente.__init__(self, id, nome, email)

        self.cnpj = cnpj
        self.ramo = ramo


    def calcular_desconto(self, cliente_type) -> int:
        raise NotImplementedError()
        pass

    def comprar_produto(self):
        pass

    def __str__(self):
        return f'{Cliente.__str__(self)}, {self.cnpj}, {self.ramo}'


    def __repr__(self):
        return f'{Cliente.__repr__(self)}, {self.cnpj}, {self.ramo}'

class ClienteFisico(Cliente):
    def __init__(self, id: int = None, nome: str = None, email: str = None,
                 cpf: str = None, dataNasc: str = None):

        Cliente.__init__(self, id, nome, email)

        self.cpf = cpf
        self.data_nasc = dataNasc

    def calcular_desconto(self, cliente_type) -> int:
        raise NotImplementedError()
        pass

    def comprar_produto(self):
        pass

    def __str__(self):
        return f'{Cliente.__str__(self)}, {self.cpf}, {self.data_nasc}'

    def __repr__(self):
        return  f'{Cliente.__repr__(self)}, {self.cpf}, {self.data_nasc}'

class Cargo:
    def __init__(self, cargo_name: str = None, salario: float = None):
        self.cargo_name = cargo_name
        self.__salario = salario


    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, value):
        self.__salario = value

    def __str__(self):
        return f'{self.cargo_name}, {self.__salario}'

    def __repr__(self):
        return f'{self.cargo_name}, {self.__salario}'

class Funcionario:

    def __init__(self, id :int = None, nome:str = None, email:str = None,cargo: Cargo = None):

        self.id = id
        self.nome = nome
        self.email = email
        self.cargo = cargo
        self.endereco = Endereco()


    def executar_tarefa(self, tarefa):
        tarefa.executar_tarefa()

    def __str__(self):
        return f'{self.id}, {self.nome}, {self.email}, {self.endereco}, {self.cargo}'

    def __repr__(self):
        return f'{self.id}, {self.nome}, {self.email}, {self.endereco}, {self.cargo}'

class Gerente:
    def __init__(self,id: int = None, nome: str = None) -> None:
        self.id = id
        self.nome = nome


    def __str__(self):
        return f'{self.id}, {self.nome}'

    def __repr__(self):
        return f'{self.id}, {self.nome}'