import os
os.system("clear||cls")

contador = 0
idade_min = 999
idade_max = 0
salario_max = 0
salario_max = 999999999
media_salarial = 0

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
            idade = int(input("Digite uma idade: "))
            fixar_idade = idade
            if idade < idade_max:
                idade_min = idade
            if idade > idade_min:
                idade_max = idade
            salario = int(input("Digite um salário: "))
            media_salarial = salario / contador
            fixar_salario = salario
            if salario <= salario_max:
                salario_min = salario
                genero =input("""Digite um gênero
F FEMININO
M MASCULINO 
Digite a opcão desejada: """).upper()
                match genero:
                  case "F":
                    contador +=1
                    if salario < salario_min:
                        salario_min = salario
                    if salario > salario_min:
                        salario_max = salario
                  case "M":
                    print()
                
        case 2: 
            print("EXIBINDO RESULTADOS!")
            print(f"NOME: {nome}")
            print(f"GENERO: {genero}")
            print(f"IDADE: {idade}")
            print(f"SALÁRIO: {salario}")
            print(f"MEDIA SALÁRIAL: {media_salarial}")
            print(f"MENOR SALARIO : {salario_min}")
            print(f"MAIOR SALARIO : {salario_max}")
          
        case 3:
            break
        case _:
            print("OPÇÃO INVÁLIDA!")
