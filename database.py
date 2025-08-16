import sqlite3

# Define o nome do arquivo do banco de dados
DB_NAME = 'banco.db'

def criar_tabelas():
    """Cria a conexão com o banco de dados e as tabelas do sistema, se não existirem."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Cria a tabela de clientes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            data_nascimento TEXT,
            cpf TEXT UNIQUE NOT NULL,
            endereco TEXT NOT NULL
        );
    """)

    # Cria a tabela de contas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            agencia TEXT NOT NULL,
            numero INTEGER UNIQUE NOT NULL,
            saldo REAL NOT NULL,
            numero_saques INTEGER NOT NULL,
            cliente_id INTEGER NOT NULL,
            FOREIGN KEY (cliente_id) REFERENCES clientes (id)
        );
    """)

    # Cria a tabela de transações
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,
            valor REAL NOT NULL,
            data TEXT NOT NULL,
            conta_id INTEGER NOT NULL,
            FOREIGN KEY (conta_id) REFERENCES contas (id)
        );
    """)

    conn.commit()
    conn.close()
    
    print("Banco de dados e tabelas criadas com sucesso!")

if __name__ == '__main__':
    # Este bloco é executado apenas se o script for rodado diretamente
    criar_tabelas()