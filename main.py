# ====================================================================
# SCRIPT PRINCIPAL DO SISTEMA BANCÁRIO - V2
# ====================================================================

# Variáveis globais para armazenar os dados do sistema.
AGENCIA = "0001"
usuarios = []
contas = []

# ====================================================================
# FUNÇÕES DE OPERAÇÃO (modularizadas)
# ====================================================================

def deposito(saldo, valor, extrato, /):
    # Lógica de depósito - (positional only)
    pass

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    # Lógica de saque - (keyword only)
    pass

def extrato(saldo, /, *, extrato):
    # Lógica de extrato - (positional and keyword only)
    pass

# ====================================================================
# NOVAS FUNÇÕES DO SISTEMA
# ====================================================================

def criar_usuario():
    # Lógica para cadastrar novo usuário
    pass

def criar_conta(agencia, numero_conta, usuarios):
    # Lógica para criar conta e vincular a um usuário
    pass

def listar_contas(contas):
    # Lógica para listar todas as contas
    pass


# ====================================================================
# FUNÇÃO PRINCIPAL E MENU
# ====================================================================

def main():
    """Função principal que gerencia o fluxo do caixa eletrônico."""

    # Variáveis de controle para a conta atual
    saldo = 0
    saques_realizados = 0
    historico = []

    menu = """\n
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo usuário
    [nc] Nova conta
    [lc] Listar contas
    [q] Sair
    
    => """

    while True:
        opcao = input(menu).lower()

        if opcao == "d":
            # Chama a função de depósito
            pass
        elif opcao == "s":
            # Chama a função de saque
            pass
        elif opcao == "e":
            # Chama a função de extrato
            pass
        elif opcao == "nu":
            criar_usuario()
        elif opcao == "nc":
            # Chama a função de criar conta
            pass
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("\n@@@ Operação inválida, por favor selecione novamente. @@@")

if __name__ == "__main__":
    main()