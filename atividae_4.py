import os
os.system("clear")

matricula = int(input("Digite sua matricula:"))
nascimento = int(input("Digite o ano do seu nascimento:"))
tempo = int(input("Digite seu tempo trabalho:" ))

idade = (2025- nascimento)

if idade < 65:
    print("Não requerer aposentadoria!")

else idade >= 65 or tempo >= 30:
    print("Requerer aposentadoria!")

