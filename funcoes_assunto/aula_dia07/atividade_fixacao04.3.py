import os 
os.system("clear||cls")

def numero(parametro):
    if(parametro) % 2 == 0:
        print("\nNÚMERO PAR!")
   
    if(parametro) % 2 == 1:
        print("\nNÚMERO IMPAR!")

solicitando = int(input("DIGITE UM NÚMERO: "))
numero(solicitando)
print("\n= = = FIM = = =")