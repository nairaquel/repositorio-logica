import os 
os.system("cls||clear")

lista = []
quantidade = 4 

for i in range(4):
    notas = int(input("DIGITE SUA NOTA: "))
    lista.append(notas)
    media = notas / quantidade # variavel q vai ser retornada
 
if media < 5:
        print("REPROVADO")
elif media >= 7:
        print ("APROVADO")
else:
        print(" RECUPERACAO")
    

print("\n==== RESULTADOS ====")
print(f"MEDIA: {media}")
#variavel| = retornada 


