zimport os 
#outro comando
import time

os.system("clear||cls")


numero = int(input("Digite um numero: "))
segundos = float(input("Digite os segundos: "))
print(f"\n")
for i in range (numero,0,-1):
    print(f"valor da variável i: {i}\n")
#11 once começa, 0 onde termina , -1 para ser decrescente
    time.sleep(segundos)

print("FIM DO PROGRAMA")
