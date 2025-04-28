import os
os.sytem("cls||clear")
#chamando/importando classes
from dataclasses import dataclass
#identificação da classe
@dataclass
class pessoa:
    nome : str
    idade :int

#identificação da classe
@dataclass
class pet:
    nome : str
    idade : int
    raca : str
#definindo os dados
pessoa1 = pessoa("Marta ", 30)
pessoa2 = pessoa("josé" , 40)

#definindo os dados
pet1 = pet("Totó", 2, "pastor-alemão")
pet2 = pet("Hulk", 3, "pitbull")

#escrevendo/printando os dados da primeira classe
print(f"Nome: {pessoa1.nome} ,Idade: {pessoa1.idade}")
print(f"Nome: {pessoa2.nome} ,Idade: {pessoa2.idade}")

#escrevendo/printando os dados da primeira classe
print(f"Nome: {pet1.nome} ,Idade: {pet1.idade}, raça: {pet1.raca}")
print(f"Nome: {pet2.nome} ,Idade: {pet2.idade}, raça: {pet2.raca}")