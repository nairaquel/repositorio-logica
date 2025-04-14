import os 
os.system("clear||cls")

def calcular_media(n1 , n2) :
    soma = n1 + n2
    resultado = soma /2
    return resultado
def verificar_resultado(media):
    if media >= 7:
        print("APROVADO")
    else:
        print("REPROVADO")

print("=NOTAS=")
#for i in range(1,3):
#nota = float(input(f"DIGITE {I}°  nota"))
nota1 = ("DIGITE SUA PRIMEIRA NOTA: ")
nota2 = ("DIGITE SUA SEGUNDA NOTA: ")

media = calcular_media(n1 , n2)
verificar_resultado(media)