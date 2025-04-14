import os
os.system("cls||clear")



def calculo (peso , altura):

    return peso / (altura * altura) 

def situação (imc):
    os.system("cls||clear")
    if imc >= 40:
        situacao =  "OBESIDADE GRAU III!"
        recomendacao = "Busque assistência médica imediatamente !"
    elif imc >= 35:
        situacao =  "OBESIDADE GRAU II !"
        recomendacao = "Consulte um médico para avaliaçaõ e  orientação."
    elif imc >= 30:
        situacao =  "SOBREPESO !"
        recomendacao = "Procure a orientação de um profissional sa saúde. "
    elif imc >= 25:
        situacao =  "SOBREPESO !"
        recomendacao = "Considere uma dieta balanceada e atividade física"
    elif imc >= 18.5 :
        situacao =  "PESO NORMAL !"
        recomendacao = "Mantenha hábitos saudáveis"
    else :
        situacao =  "ABAIXO DO PESO !"
        return situacao , recomendacao
       
peso = float(input("DIGITE SEU PESO:"))
altura = float(input("DIGITE SUA ALTURA:"))

calculo1 = calculo (peso , altura)
situação1 = situação (calculo1)
print("=== EXIBINDO RESULTADOS ===")
print("")


