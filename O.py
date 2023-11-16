class Circo1:

    def apresentar(self, tipo):
        if tipo == 1:
            self.apresentar_malabarista()
        if tipo == 2:
            self.apresentar_palhaco()

    def apresentar_malabarista(self):
        print('Olá eu sou o malabarista')

    def apresentar_palhaco(self):
        print('Olá eu sou o manoel')


class Circo2:

    def apresentar_show(self, apresentador: any):
        apresentador.apresentar_Show()


class Malabarista(Circo2):

    def apresentar_Show(self):
        print('Malabarista na area')


class Palhaco(Circo2):

    def apresentar_Show(self):
        print('Manoel na area')


class Domador(Circo2):

    def apresentar_Show(self):
        print('Domador na Area')


if __name__ == '__main__':
    circle = Circo1()
    circle.apresentar_malabarista()
    circle.apresentar_palhaco()
    circle.apresentar(3)  # Não apresentaria nada pois a classe está fechada para extenções

    circo = Circo2()

    malabarista = Malabarista()
    manoel = Palhaco()
    domador = Domador()

    malabarista.apresentar_Show()
    manoel.apresentar_Show()
    domador.apresentar_Show()
