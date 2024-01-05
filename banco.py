def main():
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
    saques = 0
    while(True):
        opcao = input(menu)

        if opcao == "d":
            valor = digitcheck("deposito")
            extrato += (f"Deposito: + R${valor}\n")
            saldo += valor
            print("Depósito efetuado com sucesso!")
            continue
        elif opcao == "s":
            valor = digitcheck("saque")
            if valor > limite:
                print(f"Valor não deve ultrapassar o limite de R${limite:.02f}")
                continue
            if valor > saldo:
                print(f"Saldo insuficiente. Saldo: R${saldo:.02f}")
                continue
            if saques >= LIMITE_SAQUES:
                print(f"Limite de {LIMITE_SAQUES} saques atingido, tente navamente amanhã")
                continue
            saques += 1
            extrato += (f"Saque:    - R${valor:.02f}\n")
            saldo -= valor
            print("Saque efetuado com sucesso!")
            continue
                
        elif opcao == "e":
            print(extrato)
            print(f"Saldo atual: R${saldo:.02f}")
        elif opcao == "q":
            break


        else:
            print("Operação invalida, por favor selecione novamente o operação desejada")

def digitcheck(tipo: str):
    while(True):
        try:
            digit = int(input(f"Digite o valor para {tipo}: "))
            if digit > 0:
                return digit
            print("Coloque apenas numeros inteiros positivos")
        except(ValueError):
            print("Coloque apenas numeros inteiros positivos")

main()
