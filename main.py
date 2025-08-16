# ====================================================================
# SCRIPT PRINCIPAL DO SISTEMA BANCÁRIO - V3 (POO)
# ====================================================================

# Variáveis globais para armazenar os objetos
clientes = []
contas = []

# ====================================================================
# CLASSES
# ====================================================================

class Historico:
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(transacao)


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor <= 0:
            print("\n@@@ Valor de saque inválido. @@@")
            return False
        
        if valor > self.saldo:
            print("\n@@@ Saldo insuficiente. @@@")
            return False

        self._saldo -= valor
        self.historico.adicionar_transacao(f"Saque de R$ {valor:.2f}")
        print("\n=== Saque realizado com sucesso! ===")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("\n@@@ Valor de depósito inválido. @@@")
            return False
        
        self._saldo += valor
        self.historico.adicionar_transacao(f"Depósito de R$ {valor:.2f}")
        print("\n=== Depósito realizado com sucesso! ===")
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([
            transacao for transacao in self.historico.transacoes 
            if "Saque" in transacao
        ])
        
        if valor > self.limite:
            print(f"\n@@@ O valor do saque excede o limite de R$ {self.limite:.2f}. @@@")
            return False
        
        if numero_saques >= self.limite_saques:
            print("\n@@@ Número máximo de saques diários atingido. @@@")
            return False
        
        return super().sacar(valor)


class PessoaFisica:
    def __init__(self, nome, data_nascimento, cpf):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Cliente(PessoaFisica):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(nome, data_nascimento, cpf)
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao):
        pass

    def adicionar_conta(self, conta):
        self.contas.append(conta)

# ====================================================================
# FUNÇÕES AUXILIARES
# ====================================================================

def recuperar_cliente(clientes, cpf):
    """Filtra a lista de clientes e retorna o cliente com o CPF informado."""
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None

def recuperar_conta(contas, numero_conta):
    """Busca uma conta na lista pelo número da conta."""
    for conta in contas:
        if conta.numero == numero_conta:
            return conta
    return None

def criar_usuario():
    """Permite o cadastro de um novo cliente."""
    cpf = input("Informe o CPF (somente números): ")
    cliente_existente = recuperar_cliente(clientes, cpf)

    if cliente_existente:
        print("\n@@@ Já existe usuário com este CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço completo (logradouro, nro - bairro - cidade/sigla estado): ")
    
    novo_cliente = Cliente(nome, data_nascimento, cpf, endereco)
    clientes.append(novo_cliente)
    print("\n=== Cliente criado com sucesso! ===")


def criar_conta():
    """Cria uma nova conta corrente e a vincula a um cliente existente."""
    global contas
    
    cpf = input("Informe o CPF do cliente: ")
    cliente = recuperar_cliente(clientes, cpf)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    numero_conta = len(contas) + 1
    nova_conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    
    contas.append(nova_conta)
    cliente.adicionar_conta(nova_conta)
    
    print(f"\n=== Conta {nova_conta.numero} criada com sucesso para o cliente {cliente.nome}! ===")


def listar_contas():
    """Exibe todas as contas cadastradas no sistema."""
    if not contas:
        print("\n@@@ Não há contas cadastradas. @@@")
        return

    print("\n=== Lista de Contas ===")
    for conta in contas:
        print("="*20)
        print(f"Agência:\t{conta.agencia}")
        print(f"C/C:\t\t{conta.numero}")
        print(f"Titular:\t{conta.cliente.nome}")


def realizar_deposito():
    """Gerencia a operação de depósito."""
    try:
        numero_conta = int(input("Informe o número da conta: "))
        conta = recuperar_conta(contas, numero_conta)
        if not conta:
            print("\n@@@ Conta não encontrada! @@@")
            return
        
        valor = float(input("Informe o valor do depósito: R$ "))
        conta.depositar(valor)
    except ValueError:
        print("\n@@@ Valor/número de conta inválido. @@@")


def realizar_saque():
    """Gerencia a operação de saque."""
    try:
        numero_conta = int(input("Informe o número da conta: "))
        conta = recuperar_conta(contas, numero_conta)
        if not conta:
            print("\n@@@ Conta não encontrada! @@@")
            return
        
        valor = float(input("Informe o valor do saque: R$ "))
        conta.sacar(valor)
    except ValueError:
        print("\n@@@ Valor/número de conta inválido. @@@")


def exibir_extrato():
    """Exibe o extrato de uma conta."""
    try:
        numero_conta = int(input("Informe o número da conta: "))
        conta = recuperar_conta(contas, numero_conta)
        if not conta:
            print("\n@@@ Conta não encontrada! @@@")
            return
            
        print("\n================ EXTRATO ================")
        if not conta.historico.transacoes:
            print("Não foram realizadas movimentações.")
        else:
            for transacao in conta.historico.transacoes:
                print(transacao)
        
        print(f"\nSaldo:\t\t\tR$ {conta.saldo:.2f}")
        print("==========================================")
    except ValueError:
        print("\n@@@ Número de conta inválido. @@@")


# ====================================================================
# FUNÇÃO PRINCIPAL E MENU
# ====================================================================

def main():
    menu = """\n
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Novo cliente
    [nc] Nova conta
    [lc] Listar contas
    [q] Sair
    
    => """

    while True:
        opcao = input(menu).lower()
        if opcao == "d":
            realizar_deposito()
        elif opcao == "s":
            realizar_saque()
        elif opcao == "e":
            exibir_extrato()
        elif opcao == "nu":
            criar_usuario()
        elif opcao == "nc":
            criar_conta()
        elif opcao == "lc":
            listar_contas()
        elif opcao == "q":
            break
        else:
            print("\n@@@ Operação inválida, por favor selecione novamente. @@@")

if __name__ == "__main__":
    main()