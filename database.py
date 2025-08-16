import sqlite3
import datetime

DB_NAME = 'banco.db'

def criar_tabelas():
    # ... (código da função anterior, que já temos) ...
    pass

def inserir_cliente(nome, data_nascimento, cpf, endereco):
    """Insere um novo cliente na tabela 'clientes'."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # O comando INSERT INTO é usado para adicionar novas linhas
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