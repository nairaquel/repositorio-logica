import os 
os.system("clear||cls")

def metros(parametro) :

    calculo = parametro * 100

    return calculo

valor = float(input("DIGITE O VALOR EM METROS: "))

print(f"valor em centimetros: {metros(valor)}")