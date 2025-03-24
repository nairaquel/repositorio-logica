import os 
os.system("clear||cls")

calculo_nota = 0

for i in range(3):
    nota = float(input("Digite a sua nota: "))
    calculo_nota += nota

    while nota > 10 or nota < 0:    
        print("Nota inválida!")
        nota = float(input("Digite a sua nota: "))
        calculo_nota += nota
media = calculo_nota /3

if media >=7:
    print("ALUNO APROVADO!")
elif media <= 6.9:
    print("ALUNO RECUPERAÇÃO!")
else:
    print("ALUNO REPROVADO!")

    
        
        


