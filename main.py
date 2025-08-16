import database as db
import gui as gui

if __name__ == "__main__":
    # Removemos a chamada para db.criar_tabelas() daqui.
    # Ela só precisa ser executada uma vez para criar o banco de dados.
    gui.criar_janela_principal()