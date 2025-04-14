import os 
os.system("clear||cls")

def tabuada(parametro):
    for i in range(1,11):
        print(f"{i} x {parametro} = {parametro * i}")
    
print("===TABUADA===")
numeros = int(input("DIGITE UMNÚMERO: "))
tabuada(numeros)


