import os
os.system("clear||cls")


nota = 0

print("SOLICITANDO NOTAS")
for i in range (1,4):

    nota = int(input(f"Digite a nota {i}: "))
    soma = nota + nota
media = soma /i
if media < 4:
    print("ALUNO REPROVADO!")
else :
    print("ALUNO APROVADO!")

print()
print(f"media:{media}")

