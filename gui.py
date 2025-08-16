import tkinter as tk
from tkinter import ttk, messagebox
import database as db  # Importa o nosso arquivo de banco de dados

# Cria a janela principal do aplicativo
def criar_janela_principal():
    janela = tk.Tk()
    janela.title("Sistema Bancário V4")
    janela.geometry("400x300")
    
    # Cria os botões para cada funcionalidade
    ttk.Button(janela, text="Novo Cliente", command=abrir_janela_novo_cliente).pack(pady=10)
    ttk.Button(janela, text="Nova Conta", command=lambda: messagebox.showinfo("Em desenvolvimento", "Funcionalidade em breve...")).pack(pady=10)
    ttk.Button(janela, text="Operações Bancárias", command=lambda: messagebox.showinfo("Em desenvolvimento", "Funcionalidade em breve...")).pack(pady=10)
    
    janela.mainloop()

# Cria a janela para cadastro de novo cliente
def abrir_janela_novo_cliente():
    janela_cliente = tk.Toplevel()
    janela_cliente.title("Novo Cliente")
    janela_cliente.geometry("300x250")
    
    # Rótulos e campos de entrada
    ttk.Label(janela_cliente, text="Nome:").pack(pady=5)
    entry_nome = ttk.Entry(janela_cliente)
    entry_nome.pack()
    
    ttk.Label(janela_cliente, text="CPF:").pack(pady=5)
    entry_cpf = ttk.Entry(janela_cliente)
    entry_cpf.pack()
    
    # Um botão que chama a função para salvar
    ttk.Button(janela_cliente, text="Salvar", command=lambda: salvar_cliente(
        entry_nome.get(),
        entry_cpf.get(),
        janela_cliente
    )).pack(pady=10)

# Função para salvar o cliente no banco de dados
def salvar_cliente(nome, cpf, janela):
    if not nome or not cpf:
        messagebox.showerror("Erro", "Nome e CPF são obrigatórios.")
        return
    
    # Validações e inserção no banco de dados (usaremos nosso módulo database)
    if db.buscar_cliente_por_cpf(cpf):
        messagebox.showerror("Erro", "CPF já cadastrado.")
    else:
        # A data de nascimento e endereço serão simplificados por enquanto
        db.inserir_cliente(nome, "", cpf, "")
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
        janela.destroy() # Fecha a janela após o sucesso

# Inicia a aplicação
if __name__ == "__main__":
    criar_janela_principal()