import os 
os.system ("clear")

#OPÇÃO 1

idade = int(input("Digite sua idade: "))

#if idade < 18 or idade > 65:
#   print("VOTO NÃO OBRIGATORIO!")
#else:
#   print("VOTO OBRIGATORIO!")

#OPÇÃO 2

if idade < 18 and idade > 65:
    print("VOTO NÃO OBRIGATORIO!")
else:
    print("VOTO OBRIGATORIO!")

