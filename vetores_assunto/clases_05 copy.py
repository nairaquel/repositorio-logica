import os
os.system("cls||clear")
from dataclasses import dataclass

@dataclass 
class endereco:
    logradouro: str
    numero: int
    cidade: str

@dataclass
class pessoa: 
    nome: str
    email: str
    endereco: endereco
    def exibir_dados(self):
        print(f"nome:{self.nome}, email:{self.email}, logradoro:{self.endereco.logradouro}, numero:{self.endereco.numero}, cidade:{self.endereco.cidade}")

nome = input("digite seu nome:")
email = input("digite seu email:")
logradouro = input("dite seu endereço:")
numero = int(input("digite o nº:"))
cidade = input("digite sua ciadade:")

endereco1 = endereco(logradouro , numero, cidade)
pessoa1 = pessoa(nome, email, endereco1)

print("DADOS DA PESSOA: ")
pessoa1.exibir_dados()