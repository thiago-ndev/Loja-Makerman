import psycopg2

class Conexao:

    conn = None

    _user = 'postgres'
    _database = 'loja'
    _password = 'negan'
    _host = 'localhost'
    _port = '5433'

    def abrir_conexao(self):
        try:

            self.conn = psycopg2.connect(user = self._user, dbname=self._database,
                                         password= self._password, host=self._host, port=self._port)
            print('conexão aberta')
        except Exception as ex:
            raise Exception('AbrirConexaoError, erro ao abrir conexao [%s]' % ex.args)

    def fechar_conexao(self):
        try:

            if self.conn:
                self.conn.close()
                print('conexão fechada')

            else:
                raise Exception('FecharConexaoError, a conexao nunca foi aberta.')

        except Exception as ex:
            raise Exception('FecharConexaoError, erro ao fechar conexao [%s]' % ex.args)