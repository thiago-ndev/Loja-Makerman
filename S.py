class SistemaDeRegistro:

    def cadastrar(self, name: str, cpf: int) -> None:
        if self.__validar_dados(name, cpf):
            self.__armazenar_usuario(name, cpf)
        else:
            self.__indicar_error()


    def __validar_dados(self, name, cpf) -> bool:
        if isinstance(name, str) and isinstance(cpf, int):
            return True
        else:
            return False


    def __armazenar_usuario(self, nome: str, cpf: int) -> None:
        print('acessa o banco de dados')
        print('Cadastrar o usuario {}, cpf {}'.format(nome, cpf))


    def __indicar_error(self) -> None:
        print('Dados invalidos')




if __name__ == '__main__':
    sistema = SistemaDeRegistro()

    sistema.cadastrar('String', 17652208742)
