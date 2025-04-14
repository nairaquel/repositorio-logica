import os 
os.system("clear||cls")

def calcular_media1(n1 , n2) :
    somar = n1 + n2
    return somar

def calcular_media2(n1 , n2) :
    subtrair = n1 - n2
    return subtrair

def calcular_media3(n1 , n2) :
    multiplicar = n1 * n2
    return multiplicar

def calcular_media4(n1 , n2) :
    dividir = n1 / n2
    return dividir


n1 = float(input(f"Digite o número: "))
n2 = float(input(f"Digite o número: "))

print("===EXIBINDO RESULTADOS===")
print()
print(f"Sua SOMA : {calcular_media1(n1, n2)}")
print(f"Sua SUBTRAÇÃO: {calcular_media2(n1, n2)}")
print(f"Sua MULTIPLICAR: {calcular_media3(n1, n2)}")
print(f"Sua DIVISÃO: {calcular_media4(n1, n2)}")




 
