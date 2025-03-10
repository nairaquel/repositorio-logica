import os
os.system("clear")

nome = input("Digite seu nome: ")
nota_1 = int(input("Digite sua nota: "))
nota_2 = int(input("Digite sua nota: "))
media = (nota_1 + nota_2) /2 
 
if media >= 9:
    print("Conceito:A")
    print(f"Media:{media}")
    print("Aprovado!")

elif media >= 7.5:
    print("Conceito:B")
    print(f"Media:{media}")
    print("Aprovado!")
elif media >= 6:
    print("Conceito:C")
    print(f"Media:{media}")
    print("Aprovado!")
elif media >=4:
    print("Conceito:D")
    print(f"Media:{media}")
    print("Reprovado!")
else:
    print("Conceito:E")
    print(f"Media:{media}")
    print("Reprovado!")
