import os 
os.system("cls || clear")

# crinando listas.
lista_notas  = []

# adicionando 3 notas em uma lista.
for i in range(3):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)
    
# exibindo todos os valores em uma lista. 
print()
for nota in lista_notas: # foreach
    print(nota)
# soma
soma = sum(lista_notas)