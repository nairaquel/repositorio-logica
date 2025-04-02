import os 
os.system("clear||cls")

contador = 0
pares = 0
impares = 0
soma_pares = 0
total = 0

while True:
    numero = int(input("Digite um número: "))
    contador += 1
    total += numero
    if numero == 0:
        break
    if numero %2 == 0:
        pares +=1
        soma_pares += numero
    else:
        impares += 1
        soma += numero
    media2 = soma_pares / pares
    media = total / contador
print(f"PARES: {pares}")
print(f"IMPARES: {impares}")
print(f"MÉDIA: {media:.2f}")
print(f"MEDIA TOTAL: {media2}")
