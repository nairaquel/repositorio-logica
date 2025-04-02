import os
os.system("clear||cls")

def logo_senai():
    os.system("clear||cls")
    print("=== SENAI DENDEZEIROS ===")

def calculo (nota_1 , nota_2):
    numeros = nota_1 + nota_2
    soma = numeros /2
    return soma

logo_senai()
primeiro_numero = int(input("DIGITE O PRIMEIRO NÚMERO: "))
logo_senai()
segundo_numero = int(input("DIGITE O SEGUNDO NÚMERO: "))

soma = primeiro_numero , segundo_numero
numeros = primeiro_numero + segundo_numero

print(f"NÚMEROS: {soma}")
print(f"SOMA: {numeros}")
