class Sale:
    def __init__(self, connection):
        self.connection = connection
        self.product = Product(connection)
    
    def realizar_venda(self, produto_id, quantidade_vendida):
        total_venda = self.product.registrar_venda(produto_id, quantidade_vendida)
        if total_venda:
            return total_venda
        else:
            return None
