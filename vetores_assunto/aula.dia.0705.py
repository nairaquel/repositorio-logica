import os 
os.system("clls||clear")

lista_funcionarios = []

from dataclasses import dataclass

@dataclass
class funcionarios:
    nome: str
    data_nascimento: str
    rg: str
    cpf: str

for i in range(2):
    print(" = = = = DADOS DOS FUNCIONÁRIOS = = = =")
nome = input("DIGITE SEU NOME: ")
data_nascimento = input("DIGITE A DATA DO SEU NASCIMENTO: ")
rg = input("DIGITE SEU RG (sem pontos ou vírgulas): ")
cpf = input("DIGITE SEU CPF (sem pontos ou vígulas): ")
dados = nome,data_nascimento, rg, cpf
lista_funcionarios.append(dados)

def funcionario(nome, data_nascimento, rg, cpf):
    nome1 = nome
    data_nascimento1 = data_nascimento
    rg1 = rg
    cpf1 = cpf
    return nome1, data_nascimento1, rg1, cpf1

nome1 = nome
data_nascimento1 = data_nascimento
rg1 = rg 
cpf1 = cpf

print(" = = = = EXIBINDOS DADOS DOS FUNCIONÁRIOS = = = =")
print(f'NOME: nome1')
print(f'DATA DE NASCIMENTO: data_nascimeto1')
print(f'RG: rg1')
print(f'CPF: cpf1')