import os 
#outro comando
import time

os.system("clear||cls")


numero = int (input("Digite um numero: "))
segundos =int (input("Digite os segundos: "))
for i in range (numero,0,-1):
    print(f"valor da variável i: {i}")
#11 once começa, 0 onde termina , -1 para ser decrescente
    time.sleep(segundos{i})

print("FIM DO PROGRAMA")
