import os 

# Função sem retorno
def logo_senai():
    os.system("clear||cls")
    print("== SENAI ==")

logo_senai() #chamando a função
nome = input("Digite seu nome: ")

logo_senai() #chamando a função
idade = int(input("Digite sua idade: "))

logo_senai() #chamando a função
print(f"Nome: {nome}")
print(f"Idade: {idade}")