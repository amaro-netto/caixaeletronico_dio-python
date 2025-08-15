# ====================================================================
# SCRIPT PRINCIPAL DO SISTEMA BANCÁRIO
# ====================================================================

# Variáveis globais para armazenar o estado do sistema.
saldo = 0.0
LIMITE_SAQUES = 3
saques_realizados_hoje = 0
historico_transacoes = []
limite_valor_saque = 500.00

# ====================================================================
# MENU PRINCIPAL
# ====================================================================

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# ====================================================================
# LOOP PRINCIPAL DO PROGRAMA
# ====================================================================

def main():
    """Função principal que gerencia o fluxo do caixa eletrônico."""
    global saldo, saques_realizados_hoje, historico_transacoes, limite_valor_saque

    while True:
        opcao = input(menu).lower()

        if opcao == "d":
            print("\n--- Operação de Depósito ---")
            
            try:
                valor_deposito = float(input("Informe o valor do depósito: R$ "))
                
                if valor_deposito > 0:
                    saldo += valor_deposito
                    
                    # Formata a string para o histórico
                    historico_transacoes.append(f"Depósito: R$ {valor_deposito:.2f}")
                    
                    print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
                else:
                    print("Operação falhou! O valor informado deve ser positivo.")
            
            except ValueError:
                print("Operação falhou! O valor informado não é um número válido.")

        elif opcao == "s":
            print("\n--- Operação de Saque ---")
            # Implementar a lógica de saque aqui
            pass

        elif opcao == "e":
            print("\n--- Operação de Extrato ---")
            # Implementar a lógica de extrato aqui
            pass

        elif opcao == "q":
            print("\nObrigado por usar nosso sistema. Volte sempre!")
            break

        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")

# Executa a função principal quando o script é iniciado.
if __name__ == "__main__":
    main()