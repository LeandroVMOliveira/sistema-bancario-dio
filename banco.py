menu = """
 
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


==> """

saldo = 0
limite = 500
extrato = ""
LIMITE_SAQUES = 3

while(True):
    opcao = input(menu)

    if opcao == "d":
        #deposito()
        ...
    elif opcao == "s":
        #saque()
        ...
    elif opcao == "e":
        #extrato()
        ...
    elif opcao == "q":
        break


    else:
        print("Operação invalida, por favor selecione novamente o operação desejada")