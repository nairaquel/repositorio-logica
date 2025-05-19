import os 
os.system("cls||clear")

lista = []

for i in range(5):
    numero = int (input(f"DIGITE O {i + 1}º NÚMERO: "))
    lista.append(numero)


#verificando número maior e menor na lista
    numero1 = min(lista)
    numero2 = max(lista)

#inicia contadem com a variavel i , começando pelo numero 1
for i, numero in  enumerate(lista , start=1):
    print(f"{i}º numero: {numero}")

print(f"\nMENOR NÚMERO: numero1")
print(F"MAIOR NÚMERO: numero2")