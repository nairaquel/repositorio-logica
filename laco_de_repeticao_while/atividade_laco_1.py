import os
os.system("clear||cls")

contador = 0
continua = 's'

while continua == 's':
#comandos a serem repetidos
    print("Repetindo...")

    contador +=1

    continua = input("Tecle 's' se desejar continuar.").strip().lower()
    #.strip() - para tirar o espaço

if contador == 0:
    print("O bloco NÃO foi repetido.")
else:
    print(f"O bloco foi repetido {contador} vezes.")

# outra forma de fazer:#

#contador = 0
#continua = 's'

#while True:
#comandos a serem repetidos#
#    print("Repetindo...")

#    continua = input("Tecle 's' se desejar continuar.").strip().lower()
#    contador +=1
#    if continua != 's':
        #break

# != - diferente#

#if contador == 0:
#    print("O bloco NÃO foi repetido.")
#else:
#    print(f"O bloco foi repetido {contador} vezes.")

#"True- comando tem q começar com a letra maiuscula#
#

