import os
os.system("clear||cls")


contador = 1
valor_nota = 0

while True:
    contador +=1
    nota = int(input("Digite sua nota:"))
    valor_nota += nota
    
    nova_nota= int(input("""
Adicionar nova nota?
SIM   1
NÃO   2
escolha opção desejada: """))                  

    print()
    media = valor_nota / contador

    if nova_nota == 2:
        break
print(f"MEDIA:{media:.2f}")
print(contador)




  

      



