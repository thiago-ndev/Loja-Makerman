from banco.conexao import Conexao


class ClienteDAO(Conexao):
    def cadastro(self, cliente):
        try:
            self.abrir_conexao()
            cursor = self.conn.cursor()
            if cliente:
                cliente.endereco.id += 1

            cursor.execute('insert into endereco(id, cidade, bairro, rua, numero) values(%s, %s, %s, %s, %s)',
                               (cliente.endereco.id, cliente.endereco.cidade, cliente.endereco.bairro,
                                cliente.endereco.rua, cliente.endereco.numero))

            if cliente.type == 'fisico':

                cursor.execute('insert into cliente_fisico(nome, email, senha, cpf, data_nasc)'
                               ' values(%s, %s, %s, %s, %s)',
                               (cliente.nome, cliente.email,
                                cliente.senha, cliente.cpf, cliente.dataNasc))
                self.conn.commit()

            elif cliente.type == 'juridico':

                cursor.execute('insert into cliente_juridico(cnpj, ramo) values(%s, %s)',
                               (cliente.cnpj, cliente.ramo))
                self.conn.commit()

            else: raise Exception('Insira o tipo de cliente(fisico ou juridico)')

        except Exception as ex:
            raise Exception('CreateError, erro ao cadastrar o cliente. [%s]' % ex.args)
        finally:
            self.fechar_conexao()


    # def lista(self):
    #     try:
    #         self.abrir_conexao()
    #         cursor = self.conn.cursor()
    #         cursor.execute('SELECT * FROM PRODUTO ORDER BY ID')
    #         # pegar os registros no banco
    #         registros = cursor.fetchall()
    #         produtos = []
    #         # registro -> id, nome, preco, quantidade
    #         for registro in registros:
    #             produto = Produto(registro[0], registro[1], registro[2], registro[3])
    #             produtos.append(produto)
    #         return produtos
    #
    #     except Exception as ex:
    #         raise Exception('ReadError. erro ao listar os produtos. [%s]' % ex.args)
    #     finally:
    #         self.fechar_conexao()

    # def busca(self, id):
    #     try:
    #         self.abrir_conexao()
    #         cursor = self.conn.cursor()
    #         cursor.execute('SELECT * FROM PRODUTO WHERE id = %s ',
    #                        (id, ))
    #         registro = cursor.fetchone()
    #         if registro is not None:
    #             produto = Produto(registro[0], registro[1], registro[2], registro[3])
    #             return produto
    #         raise Exception('id não encontrado')
    #
    #     except Exception as ex:
    #         raise Exception('ReadOneError, erro ao efetuar a busca. [%s]' % ex.args)
    #     finally:
    #         self.fechar_conexao()
    #
    #
    # def delete(self, id):
    #     try:
    #         self.abrir_conexao()
    #         cursor = self.conn.cursor()
    #         cursor.execute('DELETE FROM PRODUTO WHERE id = %s',
    #                        (id, ))
    #         self.conn.commit()
    #     except Exception as ex:
    #         raise Exception('DeleteError, erro ao deletar registro. [%s]' % ex.args)
    #     finally:
    #         self.fechar_conexao()
    #
    #
    # def update(self, produto):
    #     try:
    #         self.abrir_conexao()
    #         cursor = self.conn.cursor()
    #         cursor.execute('UPDATE PRODUTO set nome = %s,  preco = %s, quantidade = %s WHERE id = %s',
    #                               (produto.nome, produto.preco, produto.quantidade, produto.id))
    #
    #         self.conn.commit()
    #     except Exception as ex:
    #         raise Exception('UpdateError, erro ao atualizar o produto. [%s]' % ex.args)
    #     finally:
    #         self.fechar_conexao()
