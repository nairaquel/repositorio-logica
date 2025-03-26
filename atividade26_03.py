import os
os.system("clear||cls")

contador = 0


while True:
    print("____________________________")
    opcao = int(input("""
CÓDIGO | DESCRIÇÃO
    1  | ADCIONAR PESSOA ))
    2  | EXIBIR RESULTADOS
    3  | SAIR
DIGITE A OPÇÃO DESEJADA:"""))
    print("____________________________")
    contador +=1
    match opcao:
        case 1:
            os.system("clear||cls")
            print("ADCIONANDO NOVA PESSOA")
            nome = input("Digite um nome: ")
            fixar_nome = nome
            genero =input("""Digite um gênero
F FEMININO
M MASCULINO 
Digite a opcão desejada: """).upper()
            fixar_genero = genero
            idade =int(input("Digite uma idade: "))
            fixar_idade = idade
            salario =int(input("Digite um salário: "))
            fixar_salario = salario
        case 2: 
            print("EXIBINDO RESULTADOS!")
            print(f"NOME: {nome}")
            print(f"GENERO: {genero}")
            print(f"IDADE: {idade}")
            print(f"SALÁRIO: {salario}")
        case 3:
            break
        case _:
            print("OPÇÃO INVÁLIDA!")

        
