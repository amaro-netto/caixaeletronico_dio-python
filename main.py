# ====================================================================
# SCRIPT PRINCIPAL DO SISTEMA BANCÁRIO - V3 (POO)
# ====================================================================

# Funções auxiliares (manteremos por enquanto)
# ...

class PessoaFisica:
    # ... (código da classe PessoaFisica) ...
    def __init__(self, nome, data_nascimento, cpf):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Cliente(PessoaFisica):
    # ... (código da classe Cliente) ...
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(nome, data_nascimento, cpf)
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao):
        pass

    def adicionar_conta(self, conta):
        self.contas.append(conta)


# ====================================================================
# NOVAS CLASSES DE CONTA E HISTÓRICO
# ====================================================================

class Historico:
    """
    Classe para armazenar o histórico de transações de uma conta.
    """
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(transacao)

class Conta:
    """
    Classe base para contas bancárias.
    Possui saldo, número, agência, cliente e histórico.
    """
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
    """
    Representa uma Conta Corrente, que herda de Conta.
    Possui atributos específicos de limite e limite de saques.
    """
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
        
        # Chama o método sacar da classe-mãe (Conta)
        return super().sacar(valor)


# ====================================================================
# FUNÇÃO PRINCIPAL E MENU (a ser refatorada)
# ====================================================================

# ... (código da função main) ...