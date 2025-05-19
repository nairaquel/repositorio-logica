import os 
os.system("cls||clear")

lista = []
quantidade = 4 

for i in range(4):
    notas = int(input("DIDITE SUA NOTA: "))
    lista.append(notas)

#criar variavel para chamar essa função
def notas1 ():
    soma = sum(lista)
    media = soma / quantidade # variavel q vai ser retornada
    return media # retornar variavel

#criar variavel para chamar essa função
def mensagem(notas1): # variavel q vai ser retornada
    if notas < 5:
        print("REPROVADO")
    elif notas >= 7:
        print ("APROVADO")
    else:
        print(" RECUPERACAO")
        return mensagem
    
#variavel = retornada    
media = notas1()

print("\n==== RESULTADOS ====")
print(f"MEDIA: {media}")
#variavel| = retornada 
mensagem1 = mensagem(notas1)

