import tkinter as tk
from tkinter import ttk, messagebox
import database as db

def criar_janela_principal():
    janela = tk.Tk()
    janela.title("Sistema Bancário V4")
    janela.geometry("400x300")
    
    ttk.Button(janela, text="Novo Cliente", command=abrir_janela_novo_cliente).pack(pady=10)
    ttk.Button(janela, text="Nova Conta", command=abrir_janela_nova_conta).pack(pady=10)
    ttk.Button(janela, text="Operações Bancárias", command=lambda: messagebox.showinfo("Em desenvolvimento", "Funcionalidade em breve...")).pack(pady=10)
    
    janela.mainloop()

def abrir_janela_novo_cliente():
    janela_cliente = tk.Toplevel()
    janela_cliente.title("Novo Cliente")
    janela_cliente.geometry("300x250")
    
    ttk.Label(janela_cliente, text="Nome:").pack(pady=5)
    entry_nome = ttk.Entry(janela_cliente)
    entry_nome.pack()
    
    ttk.Label(janela_cliente, text="CPF:").pack(pady=5)
    entry_cpf = ttk.Entry(janela_cliente)
    entry_cpf.pack()
    
    ttk.Label(janela_cliente, text="Data de Nascimento (dd-mm-aaaa):").pack(pady=5)
    entry_data_nascimento = ttk.Entry(janela_cliente)
    entry_data_nascimento.pack()
    
    ttk.Label(janela_cliente, text="Endereço:").pack(pady=5)
    entry_endereco = ttk.Entry(janela_cliente)
    entry_endereco.pack()
    
    ttk.Button(janela_cliente, text="Salvar", command=lambda: salvar_cliente(
        entry_nome.get(),
        entry_data_nascimento.get(),
        entry_cpf.get(),
        entry_endereco.get(),
        janela_cliente
    )).pack(pady=10)

def salvar_cliente(nome, data_nascimento, cpf, endereco, janela):
    if not nome or not cpf or not data_nascimento or not endereco:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
        return
    
    if db.buscar_cliente_por_cpf(cpf):
        messagebox.showerror("Erro", "CPF já cadastrado.")
    else:
        db.inserir_cliente(nome, data_nascimento, cpf, endereco)
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        janela.destroy()

def abrir_janela_nova_conta():
    janela_conta = tk.Toplevel()
    janela_conta.title("Nova Conta")
    janela_conta.geometry("250x150")
    
    ttk.Label(janela_conta, text="CPF do Cliente:").pack(pady=5)
    entry_cpf = ttk.Entry(janela_conta)
    entry_cpf.pack()
    
    ttk.Button(janela_conta, text="Criar Conta", command=lambda: criar_nova_conta(
        entry_cpf.get(),
        janela_conta
    )).pack(pady=10)

def criar_nova_conta(cpf, janela):
    if not cpf:
        messagebox.showerror("Erro", "O CPF é obrigatório.")
        return
        
    cliente = db.buscar_cliente_por_cpf(cpf)
    
    if not cliente:
        messagebox.showerror("Erro", "Cliente não encontrado.")
        return
    
    # O numero da conta será o próximo ID do banco de dados (que é sequencial)
    # Por simplicidade, podemos contar o número de contas existentes no banco e adicionar 1
    # Vamos criar uma nova função de busca para isso
    
    # Vamos adicionar uma nova função ao database.py
    # db.get_proximo_numero_conta()
    # e usar essa função aqui. Mas por enquanto, vamos usar um número fixo para não travar
    # Por exemplo, numero = 1, e depois incrementamos
    
    # Supondo que você adicionou uma função ao database.py para pegar o próximo número da conta
    # numero_conta = db.get_proximo_numero_conta()
    # Por enquanto, vamos usar uma lógica mais simples para não precisar alterar o database.py agora
    # Podemos buscar todas as contas e pegar o numero da última, ou simplesmente contar
    
    # Lógica provisória para o número da conta
    proximo_numero = db.get_proximo_numero_conta() # Vamos supor que esta função exista
    
    db.inserir_conta("0001", proximo_numero, 0.0, 0, cliente[0]) # cliente[0] é o id do cliente
    messagebox.showinfo("Sucesso", f"Conta {proximo_numero} criada com sucesso para {cliente[1]}!")
    janela.destroy()

# A funçao get_proximo_numero_conta() precisa ser criada no arquivo database.py
# Vamos adicionar ela lá para não dar erro
def get_proximo_numero_conta():
    conn = db.sqlite3.connect(db.DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(numero) FROM contas;")
    max_numero = cursor.fetchone()[0]
    conn.close()
    if max_numero is None:
        return 1
    return max_numero + 1

# O main.py nao muda, ele continua chamando a janela principal