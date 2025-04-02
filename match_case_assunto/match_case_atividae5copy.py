import os 
os. system ('clear')

# escreva um programa ultilizando o comando match-case que mostre um mês do ano de acordo com o número digitado pelo ususario. 
#ex:
# 1 = janeiro
# 2 = fevereiro
# ...
# 12 = dezembro


mes = int(input("""
MêS \t\t\t Número
janeiro \t\t  1
fevereiro \t\t  2
março  \t\t\t  3
abril  \t\t\t  4
maio   \t\t\t  5
junho \t\t\t  6
julho \t\t\t  7
agosto \t\t\t  8
setembro \t\t  9
outubro \t\t 10
novembro \t\t 11
dezembro \t\t 12
DIGITE O NÚMERO CORRESPONDENTE AO MÊS DO ANO:"""))

match mes:
    case 1:
        print("Mês do ano: janeiro!") 
    case 2:
        print("Mês do ano: fevereiro!") 
    case 3:
        print("Mês do ano: março!") 
    case 4:
        print("Mês do ano: abril!") 
    case 5:
        print("Mês do ano: maio!") 
    case 6:
        print("Mês do ano: junho!") 
    case 7:
        print("Mês do ano: julho!") 
    case 8:
        print("Mês do ano: agosto!") 
    case 9:
        print("Mês do ano: sentembro!") 
    case 10:
        print("Mês do ano: outrubro!") 
    case 11:
        print("Mês do ano: novembro!") 
    case 12:
        print("Mês do ano: dezembro!") 
    case _: 
        print("Opção inválida")

print(f"Mês do ano: {mes}")
print("===FIM===")
        