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
    lista_funcionarios.append(funcionarios(nome, data_nascimento, rg , cpf))


#def funcionario(nome, data_nascimento, rg, cpf):
    #funcionarios.txt = 
    #return funcionarios.txt


