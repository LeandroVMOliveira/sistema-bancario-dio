
LIMITE_SAQUES = 3
def main():
    

    saldo = 0
    limite = 500
    extrato = ""
    
    saques = 0

    while(True):
    
        opcao = menu()

        if opcao == "d":
            extrato, saldo = deposito(extrato, saldo)
            continue
        elif opcao == "s":
            data = saque(
                limite = limite,
                saldo = saldo,
                maxi = LIMITE_SAQUES,
                saques = saques,
                extrato = extrato
            )
            if data != 1:
                saques += 1
                extrato = data[0]
                saldo = data[1]
            
            continue
                
        elif opcao == "e":
            historico(saldo, extrato = extrato)
        
        
        elif opcao == "q":
            break


        else:
            print("Operação invalida, por favor selecione novamente o operação desejada")

def menu():
    print ("""
=============MENU=============       
[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova conta
[lc] Listar contas
[nu] Novo usuário
[q] Sair      
==============================
     """)
    return input("==>  ")

def digitcheck(tipo: str):
    while(True):
        try:
            digit = int(input(f"Digite o valor para {tipo}: "))
            if digit > 0:
                return digit
            print("Coloque apenas numeros inteiros positivos")
        except(ValueError):
            print("Coloque apenas numeros inteiros positivos")

def deposito(extrato, saldo , /):
    "Efetua o processo de depósito"

    valor = digitcheck("deposito")

    extrato += (f"Deposito: + R${valor}\n")
    saldo += valor

    print("Depósito efetuado com sucesso!")
    
    return extrato, saldo

def saque(*, limite, saldo, maxi, saques, extrato):
    "Se cumprir com todos os requerimentos, permite ao usuário sacar seu dinheiro da conta"

    valor = digitcheck("saque")
    
    if valor > limite:
            print(f"Valor não deve ultrapassar o limite de R${limite:.02f}")
            return 1
    if valor > saldo:
            print(f"Saldo insuficiente. Saldo: R${saldo:.02f}")
            return 1
    if saques >= maxi:
        print(f"Limite de {limite} saques atingido, tente navamente amanhã")
        return 1
    
    
    extrato += (f"Saque:    - R${valor:.02f}\n")
    saldo -= valor
    

    print("Saque efetuado com sucesso!")

    return extrato, saldo

def historico(saldo, /, *, extrato):
    "Mostra todas as transações efeituadas pelo usuário"

    print(extrato)
    print(f"Saldo atual: R${saldo:.02f}")

    return

main()
