import os
os.system ("cls || clear")


positivos = 0
contador = 0

while True:
    numero = float(input("digite um valor: "))
    contador +=1
    if numero > 0:
        positivos += numero
        soma = positivos / contador
    if numero < 0:
        break
print(f"media: {soma}")

    