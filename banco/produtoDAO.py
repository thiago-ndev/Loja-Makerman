from model.produto import Produto
from model.estoque import Estoque

from conexao import Conexao

class ProdutoDao(Conexao):
    ##Produto -> lista de valores que serão armazenados

    def cadastrar(self, produto):
        try:
            self.abrir_conexao()
            cursor = self.conn.cursor()
            cursor.execute('INSERT INTO PRODUTO(nome, preco, quantidade) VALUES(%s, %s, %s)',
                           (produto.nome, produto.preco, produto.quantidade))
            self.conn.commit()

        except Exception as ex:
            raise Exception('CreateError, erro ao criar o produto. [%s]' % ex.args)
        finally:
            self.fechar_conexao()

    def lista(self):
        try:
            self.abrir_conexao()
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM PRODUTO ORDER BY ID')
            # pegar os registros no banco
            registros = cursor.fetchall()
            produtos = []
            # registro -> id, nome, preco, quantidade
            for registro in registros:
                produto = Produto(registro[0], registro[1], registro[2], registro[3])
                produtos.append(produto)
            return produtos
        except Exception as ex:
            raise Exception('ReadError. erro ao listar os produtos. [%s]' % ex.args)
        finally:
            self.fechar_conexao()

    def busca(self, id):
        try:
            self.abrir_conexao()
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM PRODUTO WHERE id = %s ',
                           (id,))
            registro = cursor.fetchone()
            if registro is not None:
                produto = Produto(registro[0], registro[1], registro[2], registro[3])
                return produto
            raise Exception('id não encontrado')

        except Exception as ex:
            raise Exception('ReadOneError, erro ao efetuar a busca. [%s]' % ex.args)
        finally:
            self.fechar_conexao()

    def delete(self, id):
        try:
            self.abrir_conexao()
            cursor = self.conn.cursor()
            cursor.execute('DELETE FROM PRODUTO WHERE id = %s',
                           (id,))
            self.conn.commit()
        except Exception as ex:
            raise Exception('DeleteError, erro ao deletar registro. [%s]' % ex.args)
        finally:
            self.fechar_conexao()

    def update(self, produto):
        try:
            self.abrir_conexao()
            cursor = self.conn.cursor()
            cursor.execute('UPDATE PRODUTO set nome = %s,  preco = %s, quantidade = %s WHERE id = %s',
                           (produto.nome, produto.preco, produto.quantidade, produto.id))

            self.conn.commit()
        except Exception as ex:
            raise Exception('UpdateError, erro ao atualizar o produto. [%s]' % ex.args)
        finally:
            self.fechar_conexao()


produtoDAO = ProdutoDao()

produto = Produto(25, 'nome', 15)
