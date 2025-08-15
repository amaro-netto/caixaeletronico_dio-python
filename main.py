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
                    
                    historico_transacoes.append(f"Depósito: R$ {valor_deposito:.2f}")
                    
                    print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso!")
                else:
                    print("Operação falhou! O valor informado deve ser positivo.")
            
            except ValueError:
                print("Operação falhou! O valor informado não é um número válido.")

        elif opcao == "s":
            print("\n--- Operação de Saque ---")
            
            try:
                valor_saque = float(input("Informe o valor do saque: R$ "))

                if valor_saque <= 0:
                    print("Operação falhou! O valor informado deve ser positivo.")
                    continue

                if valor_saque > saldo:
                    print("Operação falhou! Você não tem saldo suficiente.")
                    continue

                if valor_saque > limite_valor_saque:
                    print(f"Operação falhou! O valor máximo por saque é de R$ {limite_valor_saque:.2f}.")
                    continue

                if saques_realizados_hoje >= LIMITE_SAQUES:
                    print("Operação falhou! Limite de saques diários atingido.")
                    continue

                saldo -= valor_saque
                saques_realizados_hoje += 1
                
                historico_transacoes.append(f"Saque: R$ {valor_saque:.2f}")

                print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")

            except ValueError:
                print("Operação falhou! O valor informado não é um número válido.")
        
        elif opcao == "e":
            print("\n--- Extrato ---")
            
            if not historico_transacoes:
                print("Não foram realizadas movimentações.")
            else:
                for transacao in historico_transacoes:
                    print(transacao)
            
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("-----------------")

        elif opcao == "q":
            print("\nObrigado por usar nosso sistema. Volte sempre!")
            break

        else:
            print("\nOperação inválida, por favor selecione novamente a operação desejada.")

# Executa a função principal quando o script é iniciado.
if __name__ == "__main__":
    main()