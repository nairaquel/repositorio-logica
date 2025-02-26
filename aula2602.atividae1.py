import os
os.system("clear")

# exemplo de estrutura condicimnal aninhada
# match-case substitui o uso do if-elif-else

dia = input("Digite dia da semana :")

match dia:
    case "segunda" :
        print("Hoje é segunda-feira.")

    case "terça" :
        print("Hoje é terça-feira.")
  

    case "quarta" :
        print("Hoje é quarta-feira.")

    case "quinta" :
        print("Hoje é quinta-feira.")
 
    case "sexta" :
        print("Hoje é sexta-feira.")

    case "sabado" | "domingo" :
        print("Hoje é final de semana.")

    case _:
        print("Dia inválido.")


print("===FIM===")