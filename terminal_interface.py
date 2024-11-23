import curses
from product import Product
from sale import Sale

class TerminalInterface:
    def __init__(self, stdscr, connection):
        self.stdscr = stdscr
        self.connection = connection
        self.product = Product(connection)
        self.sale = Sale(connection)

    def mostrar_menu(self):
        self.stdscr.clear()
        self.stdscr.addstr("Menu Principal:\n")
        self.stdscr.addstr("1. Adicionar Produto\n")
        self.stdscr.addstr("2. Editar Produto\n")
        self.stdscr.addstr("3. Remover Produto\n")
        self.stdscr.addstr("4. Consultar Estoque\n")
        self.stdscr.addstr("5. Registrar Venda\n")
        self.stdscr.addstr("6. Sair\n")
        self.stdscr.addstr("Escolha uma opção: ")
        escolha = self.stdscr.getstr().decode()
        return escolha

    def adicionar_produto(self):
        self.stdscr.clear()
        self.stdscr.addstr("Adicionar Produto\n")
        self.stdscr.addstr("Nome do produto: ")
        nome = self.stdscr.getstr().decode()
        self.stdscr.addstr("Descrição: ")
        descricao = self.stdscr.getstr().decode()
        self.stdscr.addstr("Preço de custo: ")
        preco_custo = float(self.stdscr.getstr().decode())
        self.stdscr.addstr("Preço de venda: ")
        preco_venda = float(self.stdscr.getstr().decode())
        self.stdscr.addstr("ID do fornecedor: ")
        fornecedor_id = int(self.stdscr.getstr().decode())
        self.stdscr.addstr("Categoria: ")
        categoria = self.stdscr.getstr().decode()

        self.product.adicionar_produto(nome, descricao, preco_custo, preco_venda, fornecedor_id, categoria)
        self.stdscr.addstr("Produto adicionado com sucesso!\n")
        self.stdscr.refresh()
        self.stdscr.getch()

    def exibir_menu(self):
        while True:
            escolha = self.mostrar_menu()
            if escolha == '1':
                self.adicionar_produto()
            elif escolha == '6':
                break
            else:
                self.stdscr.addstr("Opção inválida!\n")
                self.stdscr.refresh()
                self.stdscr.getch()
