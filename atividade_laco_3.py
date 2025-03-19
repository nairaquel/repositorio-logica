import os
os.system("clear||cls")

idade = int(input("Digite sua idade: "))

while True:
    idade = int(input("Digite sua idade: "))

    if idade < 18:
        print("Somente maiores de 18 anos\n")
    else: 
        break

print("FIM")