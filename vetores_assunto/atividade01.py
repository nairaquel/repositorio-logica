import os 
os.system("cls||clear")

lista_notas = []

for i in range(3):
    notas = float(input("DIGITE UMA NOTA: "))
    lista_notas.append(notas)

soma = sum(lista_notas)
media = soma / notas

for notas in lista_notas:
 
    print(notas)
print(soma)
print(media)