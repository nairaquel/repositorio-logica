import os 
os.system("cls||clear")

lista = []

for i in range(5):
    numero = int (input("DIGITE UM NÚMERO: "))
    lista.append(numero)

for numero in lista :
    print(numero)

    numero1 = min(lista)
    numero2 = max(lista)
print(f"\nMENOR NÚMERO: numero1")
print(F"MAIOR NÚMERO: numero2")