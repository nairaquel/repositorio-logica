import time
import os 
os.system("cls||clear")

lista = []
quantidade = 6 
pares = 0
impares = 0 

for i in range(quantidade):
    numeros = int(input(f"DIGITE O {i+1}º NÚMERO: "))
    lista.append(numeros)
    if numeros % 2 == 0:
        pares +=1
    else: 
        impares +=1 

print("= = = = EXIBINDO NÚMEROS = = = = ")
for numeros in lista:
    time.sleep(0.5)
    print(numeros)

print(f"\nnúmeros pares: {pares}")
print(f"números impares: {impares}")