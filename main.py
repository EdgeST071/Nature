import curses
from database import Database
from product import Product
from sale import Sale
from terminal import TerminalInterface

def main(stdscr):
    # Inicializa a conexão com o banco de dados
    db = Database()
    connection = db.conectar()

    if connection:
        # Inicia a interface de terminal
        terminal = TerminalInterface(stdscr, connection)
        terminal.exibir_menu()

        # Fecha a conexão com o banco de dados
        db.fechar_conexao()
    else:
        print("Não foi possível conectar ao banco de dados.")

if __name__ == "__main__":
    # Usando curses para rodar o terminal de interface
    curses.wrapper(main)
