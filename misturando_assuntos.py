import os
os.system("cls||clear")
from dataclasses import dataclass

#CLASSES
#definindo a classes
@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

@dataclass
class filho:
    nome: str
    idade: int
    peso: float

dados_pessoa= Pessoa("Lucas", 25, 70.5, 1.75)
dados_filho= filho("Luca", 2)

print(dados_pessoa.nome)
print(dados_pessoa.idade)
print(dados_pessoa.peso)
print(dados_pessoa.altura)
print(dados_filho.nome)
print(dados_filho.idade) 
