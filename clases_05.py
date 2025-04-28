import os
os.system("cls||clear")
from dataclasses import dataclass

@dataclass 
class endereco:
    logradouro: str
    numero: int

@dataclass
class pessoa: 
    nome: str
    idade: int
    endereco: endereco
    def exibirdados(self):
        print(f"nome:{self.nome}, idade:{self.idade}, endereço:{self.endereco.logradouro}, numero:{self.endereco.numero}")

endereco1 = endereco("rua A", "33")
pessoa1 = pessoa("Marta", 22, "endereco1")

print("DADOS DA PESSOA: ")
pessoa1.exibirdados()