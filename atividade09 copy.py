import os
os.system("cls||clear")

lista = []
repitcao = 6
positivos = 0
negativos = 0
contador = 0
contador2 = 0

def calcular_pos(v1 , v2):
    soma_positivos = v1 + v2
    return soma_positivos

def calcular_neg(n1 , n2):
    soma_negativos = n1 + n2
    return soma_negativos

numero_pos1 = float(input("digite um número positivo"))
numero_pos2 = float(input("digite um número positivo"))
numero_neg1 = float(input("digite um número negativo"))
numero_neg2 = float(input("digite um número negativo"))

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