import os
os.system("clear||cls")

contador = 0


while True:
    print("____________________________")
    print("""
CÓDIGO | DESCRIÇÃO
    1  | ADCIONAR PESSOA ))
    2  | EXIBIR RESULTADOS
    3  | SAIR
DIGITE A OPÇÃO DESEJADA:""")
    
    pergunta = int(input("DIGITE A OPÇÃO DESEJADA : ")).upper()

    match pergunta:
        case 1:
            print("ADICIONAR PESSOA1")
            nome = int(input("DIGITE SEU NOME : "))
            sexo = input("INFORSE SER SEXO - USE 'M' OU 'F' : ").upper()
            salario = float(input("DIGITE SEU SALARIO: "))
            contador += 1
            soma_salario += salario
            maior_idade = max (maior_idade , idade)
            menor_idade = min (menor_idade , idade)
            if sexo == "F" and salario >= 5000:
                mulheres5k += 1
            os.sytem("clear || cls")
        case 2:
            if contador > 0:
                media_salarial = soma_salario / contador
                print("Exibindo resultados")
                print(f"Média salarial do grupo: {media_salarial}")
                print(f"Maior idade do grupo: {maior_idade}")
                print(f"Menor idade do grupo: {menor_idade}")
                print(f"Quantidade de mulheres com salário a partir de 5k: {mulheres5k}")
                
