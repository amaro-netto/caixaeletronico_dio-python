import sqlite3
import datetime

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

def inserir_cliente(nome, data_nascimento, cpf, endereco):
    """Insere um novo cliente na tabela 'clientes'."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO clientes (nome, data_nascimento, cpf, endereco)
        VALUES (?, ?, ?, ?);
    """, (nome, data_nascimento, cpf, endereco))
    
    conn.commit()
    conn.close()
    print(f"Cliente {nome} inserido com sucesso!")

def inserir_conta(agencia, numero, saldo, numero_saques, cliente_id):
    """Insere uma nova conta na tabela 'contas'."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO contas (agencia, numero, saldo, numero_saques, cliente_id)
        VALUES (?, ?, ?, ?, ?);
    """, (agencia, numero, saldo, numero_saques, cliente_id))
    
    conn.commit()
    conn.close()
    print(f"Conta {numero} criada com sucesso para o cliente {cliente_id}!")

def inserir_transacao(tipo, valor, conta_id):
    """Insere uma nova transação na tabela 'transacoes'."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute("""
        INSERT INTO transacoes (tipo, valor, data, conta_id)
        VALUES (?, ?, ?, ?);
    """, (tipo, valor, data_hora, conta_id))
    
    conn.commit()
    conn.close()

def buscar_cliente_por_cpf(cpf):
    """Busca um cliente na tabela 'clientes' pelo CPF."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM clientes WHERE cpf = ?;", (cpf,))
    cliente = cursor.fetchone()
    
    conn.close()
    return cliente

def buscar_conta_por_numero(numero):
    """Busca uma conta na tabela 'contas' pelo número da conta."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM contas WHERE numero = ?;", (numero,))
    conta = cursor.fetchone()
    
    conn.close()
    return conta

def atualizar_saldo_conta(numero_conta, novo_saldo):
    """Atualiza o saldo de uma conta na tabela 'contas'."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        UPDATE contas
        SET saldo = ?
        WHERE numero = ?;
    """, (novo_saldo, numero_conta))
    
    conn.commit()
    conn.close()
    print(f"Saldo da conta {numero_conta} atualizado para R$ {novo_saldo:.2f}.")

def atualizar_numero_saques(numero_conta, novo_numero_saques):
    """Atualiza o contador de saques de uma conta na tabela 'contas'."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
        UPDATE contas
        SET numero_saques = ?
        WHERE numero = ?;
    """, (novo_numero_saques, numero_conta))
    
    conn.commit()
    conn.close()
    print(f"Contador de saques da conta {numero_conta} atualizado para {novo_numero_saques}.")

if __name__ == '__main__':
    # Este bloco é executado apenas se o script for rodado diretamente
    criar_tabelas()