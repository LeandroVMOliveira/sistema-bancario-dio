

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
            deposito(extrato, saldo) 
            continue
        elif opcao == "s":
            saque(limite, saldo, LIMITE_SAQUES, saques, extrato)
            continue
                
        elif opcao == "e":
            historico(extrato, saldo)
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

def deposito(extrato, saldo):
    valor = digitcheck("deposito")
    extrato += (f"Deposito: + R${valor}\n")
    saldo += valor
    print("Depósito efetuado com sucesso!")

def saque(limite, saldo, max, saques, extrato):
    valor = digitcheck("saque")
    if valor > limite:
            print(f"Valor não deve ultrapassar o limite de R${limite:.02f}")
            return
    if valor > saldo:
            print(f"Saldo insuficiente. Saldo: R${saldo:.02f}")
            return
    if saques >= limite:
        print(f"Limite de {limite} saques atingido, tente navamente amanhã")
        return
    saques += 1
    extrato += (f"Saque:    - R${valor:.02f}\n")
    saldo -= valor
    print("Saque efetuado com sucesso!")

def historico(extrato, saldo):
    print(extrato)
    print(f"Saldo atual: R${saldo:.02f}")
main()
