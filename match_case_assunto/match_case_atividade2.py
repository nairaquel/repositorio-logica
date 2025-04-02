import os 
os.system("clear")

# entrada(pedir pra fazer algo)
primeiro_numero = int(input("Digite o primeiro número: "))
operador = input("Digite a operação desejada(+ - * /):")
segundo_numero = int(input("Digite o segundo número: "))

# processamento

match operador: 
    case "+":
        RESULTADO = primeiro_numero + segundo_numero
    case "-":
        RESULTADO = primeiro_numero - segundo_numero
    case "*":
        RESULTADO = primeiro_numero * segundo_numero
    case "/":
        RESULTADO = primeiro_numero / segundo_numero
    case _:
        RESULTADO = "OPÇÃO INVÁLIDA!"
# saída
print(f"\nprimeiro número:{primeiro_numero}")
print(f"operação: {operador}")
print(f"segundo número: {segundo_numero}")
print(f"Resultado: {RESULTADO}")

print("===FIM===")