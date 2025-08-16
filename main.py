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

def recuperar_conta_usuario(contas, numero_conta):
    """Busca uma conta na lista pelo número da conta."""
    for conta in contas:
        if conta['numero_conta'] == numero_conta:
            return conta
    return None

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
        "usuario": usuario,
        "saldo": 0,
        "extrato": [],
        "numero_saques": 0
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
    """
    Realiza a operação de depósito.
    Argumentos: saldo, valor, extrato (posicionais).
    Retorna: saldo e extrato atualizados.
    """
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito:\t\tR$ {valor:.2f}")
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
    return saldo, extrato

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Realiza a operação de saque.
    Argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques (nomeados).
    Retorna: saldo e extrato atualizados.
    """
    saldo_insuficiente = valor > saldo
    limite_saque_excedido = valor > limite
    limite_saques_excedido = numero_saques >= limite_saques

    if saldo_insuficiente:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    elif limite_saque_excedido:
        print(f"\n@@@ Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}. @@@")
    elif limite_saques_excedido:
        print("\n@@@ Operação falhou! Número máximo de saques diários excedido. @@@")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque:\t\t\tR$ {valor:.2f}")
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    
    return saldo, extrato, numero_saques

def extrato(saldo, /, *, extrato):
    """
    Exibe o extrato da conta.
    Argumentos: saldo (posicional) e extrato (nomeado).
    Não há retorno.
    """
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in extrato:
            print(transacao)

    print(f"\nSaldo:\t\t\tR$ {saldo:.2f}")
    print("==========================================")

# ====================================================================
# FUNÇÃO PRINCIPAL E MENU
# ====================================================================

def main():
    """Função principal que gerencia o fluxo do caixa eletrônico."""
    LIMITE_SAQUES = 3
    LIMITE_VALOR_SAQUE = 500

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
            try:
                numero_conta = int(input("Informe o número da conta: "))
            except ValueError:
                print("\n@@@ Número de conta inválido. Informe um número. @@@")
                continue

            conta = recuperar_conta_usuario(contas, numero_conta)
            
            if not conta:
                print("\n@@@ Conta não encontrada! @@@")
                continue

            try:
                valor = float(input("Informe o valor do depósito: R$ "))
            except ValueError:
                print("\n@@@ Valor inválido. Informe um número. @@@")
                continue

            conta['saldo'], conta['extrato'] = deposito(conta['saldo'], valor, conta['extrato'])

        elif opcao == "s":
            try:
                numero_conta = int(input("Informe o número da conta: "))
            except ValueError:
                print("\n@@@ Número de conta inválido. Informe um número. @@@")
                continue

            conta = recuperar_conta_usuario(contas, numero_conta)

            if not conta:
                print("\n@@@ Conta não encontrada! @@@")
                continue

            try:
                valor = float(input("Informe o valor do saque: R$ "))
            except ValueError:
                print("\n@@@ Valor inválido. Informe um número. @@@")
                continue

            conta['saldo'], conta['extrato'], conta['numero_saques'] = saque(
                saldo=conta['saldo'],
                valor=valor,
                extrato=conta['extrato'],
                limite=LIMITE_VALOR_SAQUE,
                numero_saques=conta['numero_saques'],
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            try:
                numero_conta = int(input("Informe o número da conta: "))
            except ValueError:
                print("\n@@@ Número de conta inválido. Informe um número. @@@")
                continue
            
            conta = recuperar_conta_usuario(contas, numero_conta)

            if not conta:
                print("\n@@@ Conta não encontrada! @@@")
                continue

            extrato(conta['saldo'], extrato=conta['extrato'])
        
        elif opcao == "nu":
            criar_usuario()
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(AGENCIA, numero_conta, usuarios)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("\n@@@ Operação inválida, por favor selecione novamente. @@@")

if __name__ == "__main__":
    main()