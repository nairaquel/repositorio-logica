import os
os.system("cls||clear")

from dataclasses import dataclass

@dataclass
class pessoa:
    nome : str
    idade :int
    peso : float
    altura: float

@dataclass
class pet:
    nome1 : str
    idade1 :int

print(" = = = = DADOS DO RESPONSÁVEL = = = =")
nome = input("DIGITE SEU NOME: ")
idade = int(input("DIGITE SUA IDADE: "))
peso = float(input("DIGITE SEU PESO: "))
altura = float(input("DIGITE SUA ALTURA: "))

print(" \n= = = = DADOS DO PET = = = =")
nome = input("DIGITE O NOME DO PET: ")
idade = int(input("DIGITE A IDADE DO PET: "))
  

print("\n = = = = DADOS DO RESPONSÁVEL = = = =")
print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}, Peso: {pessoa.peso}, Altura: {pessoa.altura} ")
print("\n = = = = DADOS DO RESPONSÁVEL = = = =")
print(f"Nome: {pet.nome1} , Idade: {pet.idade1}")