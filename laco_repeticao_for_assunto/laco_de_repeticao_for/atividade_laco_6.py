import os
os.system ("cls || clear")

soma = 0
for i in range(1, 6):
    numero = [int(input("Insira um numero: "))]
    
    soma += numero

print(f"Seu total é {soma}")