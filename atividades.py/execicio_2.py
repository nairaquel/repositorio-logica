import os 
os.system ("clear")

# eleabore um algoritimo usando operações lógivas para solicitar ao usuário 2 números e escrever.
# os números informados 
#o maior número 
# o menor número

#variaveis
primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

maior = max(primeiro_numero, segundo_numero)
menor = min(primeiro_numero, segundo_numero)


if primeiro_numero == segundo_numero:
    print("Os números são iguais")
else:
    print(f"maior número:  {segundo_numero}")
    print(f"menor número: {primeiro_numero}")