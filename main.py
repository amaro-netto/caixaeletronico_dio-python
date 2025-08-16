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
    """Cria uma nova conta corrente e a vincula a um usuário existente."""
    global contas

    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario_por_cpf(cpf, usuarios)

    if not usuario:
        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
        return None

    nova_conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario
    }
    contas.append(nova_conta)
    
    print(f"\n=== Conta {numero_conta} criada com sucesso para o usuário {usuario['nome']}! ===")
    
    return nova_conta

def listar_contas(contas):
    """Exibe todas as contas cadastradas no sistema."""
    if not contas:
        print("\n@@@ Não há contas cadastradas. @@@")
        return

    print("\n=== Lista de Contas ===")
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("-" * 20)
        print(linha)
    print("=======================")

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
    # Variáveis de controle de conta (Temporário, será alterado depois)
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
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("\n@@@ Operação inválida, por favor selecione novamente. @@@")

if __name__ == "__main__":
    main()