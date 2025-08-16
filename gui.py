import tkinter as tk
from tkinter import ttk, messagebox
import database as db

# FUNÇÕES DA INTERFACE GRÁFICA

def criar_janela_principal():
    janela = tk.Tk()
    janela.title("Sistema Bancário V4")
    janela.geometry("400x300")
    
    ttk.Button(janela, text="Novo Cliente", command=abrir_janela_novo_cliente).pack(pady=10)
    ttk.Button(janela, text="Nova Conta", command=abrir_janela_nova_conta).pack(pady=10)
    ttk.Button(janela, text="Operações Bancárias", command=abrir_janela_operacoes_bancarias).pack(pady=10)
    
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
    
    proximo_numero = db.get_proximo_numero_conta()
    
    db.inserir_conta("0001", proximo_numero, 0.0, 0, cliente[0])
    messagebox.showinfo("Sucesso", f"Conta {proximo_numero} criada com sucesso para {cliente[1]}!")
    janela.destroy()

def abrir_janela_operacoes_bancarias():
    janela_operacoes = tk.Toplevel()
    janela_operacoes.title("Operações Bancárias")
    janela_operacoes.geometry("500x450")

    # Frame principal para organizar os widgets
    main_frame = ttk.Frame(janela_operacoes, padding="10")
    main_frame.pack(fill="both", expand=True)

    # Widgets para entrada de conta
    ttk.Label(main_frame, text="Número da Conta:").grid(row=0, column=0, pady=5, sticky="w")
    entry_conta = ttk.Entry(main_frame)
    entry_conta.grid(row=0, column=1, pady=5, sticky="ew")

    # Widgets para entrada de valor
    ttk.Label(main_frame, text="Valor (R$):").grid(row=1, column=0, pady=5, sticky="w")
    entry_valor = ttk.Entry(main_frame)
    entry_valor.grid(row=1, column=1, pady=5, sticky="ew")

    # Botões de operação
    ttk.Button(main_frame, text="Depósito", command=lambda: realizar_operacao(
        entry_conta.get(), entry_valor.get(), "deposito"
    )).grid(row=2, column=0, pady=10, sticky="ew")

    ttk.Button(main_frame, text="Saque", command=lambda: realizar_operacao(
        entry_conta.get(), entry_valor.get(), "saque"
    )).grid(row=2, column=1, pady=10, sticky="ew")

    # Widget para exibir o extrato
    ttk.Label(main_frame, text="Extrato:").grid(row=3, column=0, columnspan=2, pady=(20, 5), sticky="w")
    extrato_text = tk.Text(main_frame, height=10, width=50)
    extrato_text.grid(row=4, column=0, columnspan=2, sticky="nsew")
    extrato_text.config(state="disabled") # Deixa o campo não editável

    # Botão para visualizar extrato
    ttk.Button(main_frame, text="Visualizar Extrato", command=lambda: visualizar_extrato(
        entry_conta.get(), extrato_text
    )).grid(row=5, column=0, columnspan=2, pady=10, sticky="ew")

def realizar_operacao(numero_conta, valor, tipo_operacao):
    try:
        numero_conta = int(numero_conta)
        valor = float(valor)
    except ValueError:
        messagebox.showerror("Erro", "Número da conta e valor devem ser numéricos.")
        return

    conta = db.buscar_conta_por_numero(numero_conta)
    if not conta:
        messagebox.showerror("Erro", "Conta não encontrada.")
        return

    saldo_atual = conta[3]
    numero_saques = conta[4]
    
    if tipo_operacao == "deposito":
        if valor > 0:
            novo_saldo = saldo_atual + valor
            db.atualizar_saldo_conta(numero_conta, novo_saldo)
            db.inserir_transacao("Depósito", valor, conta[0])
            messagebox.showinfo("Sucesso", f"Depósito de R$ {valor:.2f} realizado.")
        else:
            messagebox.showerror("Erro", "O valor do depósito deve ser positivo.")
    
    elif tipo_operacao == "saque":
        limite_saque = 500
        limite_saques_diarios = 3
        
        if valor <= 0 or valor > limite_saque or valor > saldo_atual or numero_saques >= limite_saques_diarios:
            if valor <= 0:
                messagebox.showerror("Erro", "O valor do saque deve ser positivo.")
            elif valor > limite_saque:
                messagebox.showerror("Erro", f"O valor máximo por saque é de R$ {limite_saque:.2f}.")
            elif valor > saldo_atual:
                messagebox.showerror("Erro", "Saldo insuficiente.")
            elif numero_saques >= limite_saques_diarios:
                messagebox.showerror("Erro", f"Limite de saques diários ({limite_saques_diarios}) atingido.")
        else:
            novo_saldo = saldo_atual - valor
            db.atualizar_saldo_conta(numero_conta, novo_saldo)
            db.atualizar_numero_saques(numero_conta, numero_saques + 1)
            db.inserir_transacao("Saque", valor, conta[0])
            messagebox.showinfo("Sucesso", f"Saque de R$ {valor:.2f} realizado.")

def visualizar_extrato(numero_conta, extrato_widget):
    try:
        numero_conta = int(numero_conta)
    except ValueError:
        messagebox.showerror("Erro", "Número da conta deve ser numérico.")
        return
    
    conta = db.buscar_conta_por_numero(numero_conta)
    if not conta:
        messagebox.showerror("Erro", "Conta não encontrada.")
        return

    extrato_widget.config(state="normal")
    extrato_widget.delete("1.0", tk.END)
    
    transacoes = db.buscar_transacoes_por_conta_id(conta[0])
    
    if not transacoes:
        extrato_widget.insert(tk.END, "Não foram realizadas movimentações.\n")
    else:
        for transacao in transacoes:
            tipo, valor, data = transacao[1], transacao[2], transacao[3]
            extrato_widget.insert(tk.END, f"{data} - {tipo}: R$ {valor:.2f}\n")
    
    saldo_atual = conta[3]
    extrato_widget.insert(tk.END, f"\nSaldo Atual: R$ {saldo_atual:.2f}")
    extrato_widget.config(state="disabled")