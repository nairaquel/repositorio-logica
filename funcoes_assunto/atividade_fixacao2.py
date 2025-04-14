import os

def logo_senai():
    os.system("clear||cls")
    print("===SENAI DENDEZEIROS===")

def somar(numero_1 , numero_2):
    return numero_1 + numero_2

def subtrair(numero_1 , numero_2):
    return numero_1 - numero_2

def multiplicar(numero_1 , numero_2):
    return numero_1 * numero_2

def dividir(numero_1 , numero_2):
    return numero_1 / numero_2

logo_senai()
numero_1 = int(input("DIGITE O PRIMEIRO NÚMERO: "))

logo_senai()
numero_2 = int(input("DIGITE O SEGUNDO NÚMERO: "))

soma = somar(numero_1 , numero_2)
subtracao = subtrair(numero_1 , numero_2)
multiplicacao = multiplicar(numero_1 , numero_2)
dividisao = dividir(numero_1 , numero_2)

logo_senai()
print(f"SOMA: {soma}")
print(f"SUBTRAÇÃO: {subtracao}")
print(f"MULTIPLICAÇÃO: {multiplicacao}")
print(f"DIVISÃO: {dividisao}")
