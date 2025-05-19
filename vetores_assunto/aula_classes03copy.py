import os
os.system("cls||clear")

from dataclasses import dataclass

@dataclass
class pessoa:
    nome : str
    email:str
    telefone: int
    endereço: str


    nome = input("DIGITE SEU NOME: ")
    email = input("DIGITE SEU EMAIL: ")
    telefone = int(input("DIGITE SEU NÚMERO DE TELEFONE: "))
    endereço = input("DIGITE SEU ENDEREÇO: ")

print("\nEXIBINDO DADOS")
print(f"NOME: {pessoa.nome}")
print(f"EMAIL: {pessoa.email}")
print(f"TELEFONE: {pessoa.telefone}")
print(f"ENDEREÇO: {pessoa.endereço}")