import os
os.system("clear||cls")

pares = 0
impares = 0
positivo = 0
negativo = 0
soma = 0

print("Ideia de Marcelooooooooo\n")
for i in range (5):
    numero = int(input(f"Digite um número {i+1}: "))
    if numero %2 == 0:
        pares +=1
    else:
        impares += 1

    if numero < 0:
        negativo += 1
    else:   
        positivo += 1
        soma += numero
        

media = soma / positivo

print()
print(f"PARES: {pares}")
print(f"IMPARES: {impares}")
print(f"POSITIVOS: {positivo}")
print(f"NEGATIVOS: {negativo}")
print(f"MÉDIA: {media}")
print()
print("PRONTO MARCELOOOOOO")