import os
os.system("clear")

nome = input(" Digite seu nome: ")
nota_1 = int(input(" Digite sua nota: "))


match nota: 
    case nota > | == 9:
    print(f"Nota conceito A")
    print(f"aprovado!")

    case nota > or == 7.5 and < 9:
        print(f"Nota conceito B")
        print(f"aprovado!")

    case nota > or == 6 and < 7.5:
        print(f"Nota conceito C")
        print(f"aprovado!")

    case nota > or == 4 and < 6:
        print(f"Nota conceito D")
        print(f"Reprovado!")

    case nota > 4:
        print(f"Nota conceito B")
        print(f"Reprovado!")

    case _:
        print("opção invalida")