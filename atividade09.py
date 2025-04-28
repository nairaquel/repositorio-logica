import os
os.system("cls||clear")

lista = []
repitcao = 6
positivos = 0
negativos = 0
contador = 0
contador2 = 0


for i in range(repitcao):
    numero = float(input("Digite um número: "))
    lista.append(numero)
    if numero >= 0:
        contador += 1
        positivos += numero

    else:
        negativos += numero
        contador2 += 1
for numero in lista:
    print(lista)
print (f"positivos:{contador}")
print (f"Soma dos positivos:{positivos}")
print(f"negativos:{contador2}")
print (f"Soma dos negativos{negativos}")
print (f"Soma dos negativos{negativos}")