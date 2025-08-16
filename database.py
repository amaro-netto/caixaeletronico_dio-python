import sqlite3
import datetime

DB_NAME = 'banco.db'

def criar_tabelas():
    # ... (código existente) ...
    pass

def inserir_cliente(nome, data_nascimento, cpf, endereco):
    # ... (código existente) ...
    pass

def inserir_conta(agencia, numero, saldo, numero_saques, cliente_id):
    # ... (código existente) ...
    pass

def inserir_transacao(tipo, valor, conta_id):
    # ... (código existente) ...
    pass

def buscar_cliente_por_cpf(cpf):
    # ... (código existente) ...
    pass

def buscar_conta_por_numero(numero):
    # ... (código existente) ...
    pass

def buscar_transacoes_por_conta_id(conta_id):
    # ... (código existente) ...
    pass

def atualizar_saldo_conta(numero_conta, novo_saldo):
    # ... (código existente) ...
    pass

def atualizar_numero_saques(numero_conta, novo_numero_saques):
    # ... (código existente) ...
    pass

def get_proximo_numero_conta():
    """Retorna o próximo número de conta disponível (sequencial)."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT MAX(numero) FROM contas;")
    max_numero = cursor.fetchone()[0]
    
    conn.close()
    
    if max_numero is None:
        return 1
    return max_numero + 1

if __name__ == '__main__':
    criar_tabelas()