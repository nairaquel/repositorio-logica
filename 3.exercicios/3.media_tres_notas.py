import os
os.system("clear")

# elabore um algoritimo 

primeira_nota = float(input("Digite a primeira nota:" ))
segunda_nota = float(input("Digite a seguna nota:" ))
terceira_nota = float(input("Digite a terceira nota:" ))

soma = primeira_nota + segunda_nota + terceira_nota
media = soma / 3

print(f"Média: {media}")

if media < 7:
    print("REPROVADO!")
else:
    print("APROVADO!")