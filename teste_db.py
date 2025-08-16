# Arquivo: teste_db.py

import sqlite3

def criar_banco_simples():
    print("Tentando criar o arquivo do banco de dados...")
    try:
        conn = sqlite3.connect('teste_simples.db')
        conn.close()
        print("Arquivo 'teste_simples.db' criado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == '__main__':
    criar_banco_simples()