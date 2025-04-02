import os
os.system ("clear")

altura = float(input("Digite sua altura: "))
genero = input("""
M \t Mulher
H \t Homem
                            
Digite o genêro correspondente: """)


match genero: 
    case "M" | "m":
        calculo_1 = ( 62.1 * altura) - 44.7

        print(f"Genêro: {genero}")
        print(f"Altura: {altura}")
        print(f"Peso ideal: { calculo_1}")

    case "H" | "h": 
        calculo_2 = (72.7 * altura) - 58

        print(f"Genêro: {genero}")
        print(f"Altura: {altura}")
        print(f"Peso ideal: { calculo_2}")

    case _:
        print(f"Opção invalida!")
