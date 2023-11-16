
class validar_produto:
    pass


class ComprarProdutos:
    pass

# Entrada de dados

class EntradaProduto():

#Input
    def input_Nome(self):
        try:
            nome = str(input('Digite o nome do produto : '))
            return nome


        except Exception as ex:
            print(ex)

    def input_Id(self):
        try:
            id = int(input('Digite o id do produto : '))
            if id <=0:
                raise Exception('idError, o id não pode ser negativo ou zero')
            return id

        except ValueError as ex:
            print(ex)
            print('Digite um valor numérico valido.')
            return self.input_Id()


        except Exception as ex:
            print(ex)
            print('Erro ao digitar o id')
            return self.input_Id()


    def input_Preco(self):
        try:
            preco = float(input('Digite o Preço : '))
            if preco <= 0:
                raise Exception('PrecoError, o preço não pode ser negativo ou zero.')
            return preco


        except ValueError as ex:
            print(ex)
            print('Digite um valor numérico valido')
            return self.input_Preco()

        except Exception as ex:
            print(ex.args)
            print('Erro ao digitar o preço')
            return self.input_Preco()


    def input_Quantidade(self):
        try:
            quantidade = int(input('Digite a quantidade : '))
            if quantidade <=0:

                raise Exception('QuantidadeError, a quantidade não pode ser negativa ou zero.')

            return quantidade

        except ValueError as ex:
            print(ex)
            print('Digite um valor numérico valido')
            return self.input_Quantidade()

        except Exception as ex:
            print(ex)
            print('Erro ao digitar a quantidade')
            return self.input_Quantidade()