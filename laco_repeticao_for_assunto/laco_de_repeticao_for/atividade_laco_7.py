import os
os.system("clear||cls")

pares = 0
impares = 0

print("SOLICITANDO NOTAS")
for i in range (5):
    numero = int(input(f"Digite o valor {i+1}: "))

    if numero %2 == 0:
        pares +=1
    else:
        impares += 1
       
print()       
print(f"Números pares:{pares}")   
print(f"Números ímpares:{impares}")

print(f"\nFIM DO PROGRAMA")