import os
os.system("clear")

nome = input(" Digite seu nome: ")
nota = int(input(" Digite sua nota: "))
                   
                   
if nota >= 9: 
    print(f"Nota conceito A")
    print(f"aprovado!")
elif nota >= 7.5:
    print(f"Nota conceito B")
    print(f"aprovado!")
elif nota >= 6:
    print(f"Nota conceito C")
    print(f"aprovado!")
elif nota <= 6:
    print(f"Nota conceito D")
    print(f"Reprovado!")
elif nota <= 4:
    print(f"Nota conceito B")
    print(f"Reprovado!")
else:
    print("opção invalida")