import os
os.system("clear||cls")


nota_1 = int(input("Digite sua nota: "))
nota_2 = int(input("Digite sua nota: "))


soma = (nota_1 + nota_2 ) /2

while True:
    if soma < 0 or soma > 10:
        nota = int(input("Digite sua nota: "))
    else:
        break

print(f"Média: {soma}\n")
print("FIM")

#jeito certo==================================================

#QUANTIDADE_DE_NOTAS = 2
#soma = 0

#for i in range(QUANTIDADE_DE_NOTAS):
#    while True:
#       nota = int(input("Digite sua nota: "))

#        if nota < 0 or nota > 10:
#            print("A nota deve ser entre 0 e 10.\n"
#        else:
#        soma += nota
#        break
        
#media = soma / QUANTIDADE_DE_NOTAS

#print(f"Média : {media}")

