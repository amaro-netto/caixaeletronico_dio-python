# ====================================================================
# SCRIPT PRINCIPAL DO SISTEMA BANCÁRIO - V2
# ====================================================================

# Variáveis globais para armazenar os dados do sistema.
AGENCIA = "0001"
usuarios = []
contas = []

# ====================================================================
# FUNÇÕES AUXILIARES E NOVAS FUNÇÕES DO SISTEMA
# ====================================================================

def filtrar_usuario_por_cpf(cpf, usuarios):
    """Filtra a lista de usuários e retorna o usuário com o CPF informado."""
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

def criar_usuario():
    """Permite o cadastro de um novo usuário (cliente)."""
    global usuarios

    cpf = input("Informe o CPF (somente números): ")
    usuario_existente = filtrar_usuario_por_cpf(cpf, usuarios)

    if usuario_existente:
        print("\n@@@ Já existe usuário com este CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    
    logradouro = input("Informe o logradouro (ex: Rua, Av, etc.): ")
    nro = input("Informe o número: ")
    bairro = input("Informe o bairro: ")
    cidade = input("Informe a cidade: ")
    estado = input("Informe a sigla do estado: ")
    
    endereco = f"{logradouro}, {nro} - {bairro} - {cidade}/{estado}"

    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    
    usuarios.append(novo_usuario)
    print("\n=== Usuário criado com sucesso! ===")

def criar_conta(agencia, numero_conta, usuarios):
    # Lógica para criar conta e vincular a um usuário
    pass

def listar_contas(contas):
    # Lógica para listar todas as contas
    pass

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
# FUNÇÃO PRINCIPAL E MENU
# ====================================================================

def main():
    """Função principal que gerencia o fluxo do caixa eletrônico."""
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
            pass
        elif opcao == "s":
            pass
        elif opcao == "e":
            pass
        elif opcao == "nu":
            criar_usuario()
        elif opcao == "nc":
            pass
        elif opcao == "lc":
            pass
        elif opcao == "q":
            break
        else:
            print("\n@@@ Operação inválida, por favor selecione novamente. @@@")

if __name__ == "__main__":
    main()