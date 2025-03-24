import os
os.system("clear||cls")

comanda = 0
while True:
    opcao = int(input("""
codigo \t Prato  \t\t valor
 1 \t Picanha \t\t R$ 25,00
 2 \t lasanha \t\t R$ 20,00
 3 \t strogonoff \t\t R$ 18,00
 4 \t Bife acebolado\t\t R$ 15,00
 5 \t Pão com ovo \t\t R$ 5,00 
                                 
Digite a opção desejada:"""))
    print()

    match opcao:
        case 1:
            print("Picanha R$ 25,00")
            prato = 25
        case 2:
            print("asanha  R$ 20,00")
            prato = 20
        case 3:
            print("strogonoff  R$ 18,00")
            prato = 18
        case 4:
            print("Bife acebolado R$ 15,00")
            prato = 15
        case 5:
            print("Pão com ovo R$ 5,00 ")
            prato = 5
        case _: 
            print("OPÇÃO INVÁLIDA!")
    print("-----------------------------------------")
    comanda+= prato
    decisao = int(input("""
SIM  1
NÃO  2                 
deseja escolher mais um prato?"""))
    print()
    print("-------------------------------------------")
    if decisao == 2:
        break
print()
print(f"VALOR TOTAL:{comanda}")



