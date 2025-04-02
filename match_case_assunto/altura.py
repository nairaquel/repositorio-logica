import os
os.system ("clear")

altura = int(input("Digite sua altura>: "))
genero = int(input("""
M \t Mulher
H \t Homem
                            
Digite o genêro correspondente: """))


match genero: 
    case "M":
        calculo_1 = ( 62.1 * altura) - 44.7

        print(f"Genêro: {genero}")
        print(f"Altura: {altura}")
        print(f"Peso ideal: { calculo_1}")

    case "H": 
        calculo_2 (72.7 * altura) - 58

        print(f"Genêro: {genero}")
        print(f"Altura: {altura}")
        print(f"Peso ideal: { calculo_1}")









    