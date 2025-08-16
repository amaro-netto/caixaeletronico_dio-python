# ====================================================================
# SCRIPT PRINCIPAL DO SISTEMA BANCÁRIO - V3 (POO)
# ====================================================================

# Vamos definir as classes de acordo com o diagrama UML.

class PessoaFisica:
    """
    Classe base que representa uma Pessoa Física.
    Possui atributos como nome, data de nascimento e CPF.
    """
    def __init__(self, nome, data_nascimento, cpf):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Cliente(PessoaFisica):
    """
    Representa um Cliente do banco, que é uma Pessoa Física.
    Possui uma lista de contas e um endereço.
    """
    def __init__(self, nome, data_nascimento, cpf, endereco):
        # Chama o construtor da classe-mãe (PessoaFisica)
        super().__init__(nome, data_nascimento, cpf)
        self.endereco = endereco
        self.contas = []  # Lista para armazenar as contas do cliente
    
    def realizar_transacao(self, conta, transacao):
        """Método para o cliente realizar uma transação em uma conta específica."""
        # A lógica para isso será implementada mais tarde
        pass

    def adicionar_conta(self, conta):
        """Adiciona uma nova conta à lista de contas do cliente."""
        self.contas.append(conta)


# ====================================================================
# OUTRAS CLASSES SERÃO DEFINIDAS A SEGUIR
# ====================================================================


# ====================================================================
# FUNÇÃO PRINCIPAL E MENU (ainda a ser refatorada para usar as classes)
# ====================================================================

def main():
    # O loop principal e as funcionalidades serão reescritos
    # para interagir com objetos, não mais com dicionários.
    pass

if __name__ == "__main__":
    main()