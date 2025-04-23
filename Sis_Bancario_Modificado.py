# # INSERINDO LIMITE DIÁRIO DE TRANSAÇÃO E EXTRATO COM DATA E HORA # #

from datetime import datetime


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=>"""


saldo = 0
limite = 500
extrato = ""
LIMITE_SAQUE_DIARIO = 10
registro_saques = []  # registrando data/hora dos saques


# Operação de deposito

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor de depósito: "))
        
        if valor > 0:
            saldo += valor
            horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            extrato += f"[{horario}] Depósito: R$ {valor:.2f}\n"
            print("Depósito concluído com sucesso!")

        else:
            print("Operação falhou, o valor informado é inválido. Tente novamente!")
    

    # Operação saque

    elif opcao == "s":
        valor = float(input("Informe o valor que deseja sacar: "))
        agora = datetime.now()
        data_hoje = agora.date()

     # Conta quantos saques foram feitos hoje
        saques_hoje = [s for s in registro_saques if s.date() == data_hoje]


        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = len(saques_hoje) >= LIMITE_SAQUE_DIARIO

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente!")
        
        elif excedeu_limite:
            print("Operação falhou! O valor informado excede o limite para saque.")
        
        elif excedeu_saques:
            print("Operação falhou! Limite máximo de saques excedido!")
        
        elif valor > 0:
            saldo -= valor
            registro_saques.append(agora)  # salva data/hora do saque
            horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            extrato += f"[{horario}] Saque: R$ {valor:.2f}\n"
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
