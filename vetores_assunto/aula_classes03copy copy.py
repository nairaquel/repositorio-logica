import os
os.system("cls||clear")

from dataclasses import dataclass

@dataclass
class pessoa:
    nome : str
    email:str
    telefone: int
    endereço: str
    def exibindo_dados(self):
        print("\nEXIBINDO DADOS: ")
        print(f"Nome: {self.nome} , Idade: {self.idade}, Peso: {self.peso}, Altura: {self.altura} ")
       

    nome = input("DIGITE SEU NOME: ")
    email = input("DIGITE SEU EMAIL: ")
    telefone = int(input("DIGITE SEU NÚMERO DE TELEFONE: "))
    endereço = input("DIGITE SEU ENDEREÇO: ")
