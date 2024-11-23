class Product:
    def __init__(self, connection):
        self.connection = connection
    
    def adicionar_produto(self, nome, descricao, preco_custo, preco_venda, fornecedor_id, categoria):
        cursor = self.connection.cursor()
        sql = """
        INSERT INTO produtos (nome, descricao, preco_custo, preco_venda, fornecedor_id, categoria)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (nome, descricao, preco_custo, preco_venda, fornecedor_id, categoria))
        self.connection.commit()
    
    def editar_produto(self, produto_id, nome, descricao, preco_custo, preco_venda, fornecedor_id, categoria):
        cursor = self.connection.cursor()
        sql = """
        UPDATE produtos 
        SET nome = %s, descricao = %s, preco_custo = %s, preco_venda = %s, fornecedor_id = %s, categoria = %s 
        WHERE id_produto = %s
        """
        cursor.execute(sql, (nome, descricao, preco_custo, preco_venda, fornecedor_id, categoria, produto_id))
        self.connection.commit()
    
    def remover_produto(self, produto_id):
        cursor = self.connection.cursor()
        sql = "DELETE FROM produtos WHERE id_produto = %s"
        cursor.execute(sql, (produto_id,))
        self.connection.commit()

    def consultar_produtos(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM produtos")
        return cursor.fetchall()

    def registrar_venda(self, produto_id, quantidade_vendida):
        cursor = self.connection.cursor()
        cursor.execute("SELECT quantidade, preco_venda FROM produtos WHERE id_produto = %s", (produto_id,))
        produto = cursor.fetchone()

        if produto:
            quantidade_em_estoque = produto[0]
            preco_unitario = produto[1]
            
            if quantidade_vendida <= quantidade_em_estoque:
                nova_quantidade = quantidade_em_estoque - quantidade_vendida
                cursor.execute("UPDATE produtos SET quantidade = %s WHERE id_produto = %s", (nova_quantidade, produto_id))
                self.connection.commit()
                return quantidade_vendida * preco_unitario
            else:
                return None
        else:
            return None
