menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=>"""


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3


# Operação de deposito

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor de depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito concluído com sucesso!")

        else:
            print("Operação falhou, o valor informado é inválido. Tente novamente!")
    

    # Operação saque

    elif opcao == "s":
        valor = float(input("Informe o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente!")
        
        elif excedeu_limite:
            print("Operação falhou! O valor informado excede o limite para saque.")
        
        elif excedeu_saques:
            print("Operação falhou! Limite máximo de saques excedido!")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Operação concluída! Saque realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido")



    # Operação Extrato

    elif opcao == "e":
        print("============== EXTRATO ===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"saldo: R$ {saldo:.2f}\n")
        print("======================================")

    
    elif opcao == "q":
        print("Acesso encerrado!")
        break

    else:
        print("Operação falhou! O valor informado é inválido. Tente novamente.")
        