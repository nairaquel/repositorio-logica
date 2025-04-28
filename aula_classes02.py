import os
os.system("cls||clear")

from dataclasses import dataclass

@dataclass
class pessoa:
    nome : str
    idade :int
    peso : float
    altura: float


    nome = input("DIGITE SEU NOME: ")
    idade = int(input("DIGITE SUA IDADE: "))
    peso = float(input("DIGITE SEU PESO: "))
    altura = float(input("DIGITE SUA ALTURA: "))

print(f"Nome: {pessoa.nome} , Idade: {pessoa.idade}, Peso: {pessoa.peso}, Altura: {pessoa.altura} ")