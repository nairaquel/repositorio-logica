import os
os.system("clear")

# entrada
opcao = int(input("""
codigo \t Prato  \t\t valor
 1 \t Picanha \t\t R$ 25,00
 2 \t lasanha \t\t R$ 20,00
 3 \t strogonoff \t\t R$ 18,00
 4 \t Bife acebolado\t\t R$ 15,00
5 \t Pão com ovo \t\t R$ 5,00 
                                 
Digite a opção desejada:"""))

# processamento

match opcao:
    case 1:
        print("Picanha R$ 25,00")
    case 2:
        print("asanha  R$ 20,00")
    case 3:
        print("strogonoff  R$ 18,00")
    case 4:
        print("Bife acebolado R$ 15,00")
    case 5:
        print("Pão com ovo R$ 5,00 ")
    case _: 
        print("OPÇÃO INVÁLIDA!")

# saída

print("\n")
print(f"Pedido finalizado!")