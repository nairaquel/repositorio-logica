import os 
os.system("cls||clear")

comida = ""
valor = 0


while True:
    pedido = print("""
    CÓDIGO \t | PRATO          | VALOR
____________________________________________    
    1      \t | PICANHA        |  R$25,00 
    2      \t | LASANHA        |  R$20,00 
    3      \t | STROGONOFF     |  R$18,00 
    4      \t | BIFE ACEBOLADO |  R$15,00
    5      \t | PÃO COM OVO    |  R$05,00 
_____________________________________________""")
    opcao = int(input("DIGITE O CÓDIGO DESEJADO: "))

    match pedido:
        case 1:
            comida += "PICANHA"
            valor += 25
        case 2:
            comida += "LASANHA"
            valor += 20
          
            #pedido += comida
        case 3:
            comida += "STROGONOFF"
            valor += 18
        case 4:
            comida += "BIFE ACEBOLADO"
            valor += 15
            
            #pedido += comida
        case 5:
            comida +="PÃO COM OVO"
            valor += 5
           
            #pedido += comida
        case _:
            print("OPÇÃO ÍNVALIDA")
            valor = " "
            calculo = 0
    pergunta = input("DESEJA PEDIR MAIS ALGUMA COISA? RESPONDA S para SIM e N para NÃO: ").oppper()
    if pergunta == "N":
        break

print("==== EXIBINDO VALOR ====")
print(f"PEDIDO(S):{comida} ")
print(f"VALOR:{valor} ")
if pergunta == "sim" or pergunta == "Sim":