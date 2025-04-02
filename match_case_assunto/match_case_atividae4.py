import os 
os. system ('clear')

dia_da_semana = int(input("""
DIA  \t\t\t Número
segunda-feira\t\t 2 
terça-feira \t\t 3 
quarta-feira \t\t 4 
quinta-feira \t\t 5
sexta-feira  \t\t 6
sábado  \t\t 7
domingo \t\t 1
DIGITE O NÚMERO CORRESPONDENTE AO DIA DA SEMANA:"""))

match dia_da_semana:
    case 2: 
        print("Segunda-feira!")
        print("Dia últil!")
    
    case 3: 
        print("Terça-feira!")
        print("Dia últil!")
    
    case 4: 
        print("Quarta-feira!")
        print("Dia últil!")
    
    case 5: 
        print("Quinta-feira!")
        print("Dia últil!")
    
    case 6: 
        print("sexta-feira!")
        print("Dia últil!")
    
    case 7: 
        print("Segunda-feira!")
        print("Final de semana!")
    
    case 1: 
        print("Segunda-feira!")
        print("final de semana!")
    
    case _: 
        print("Opção inválida")

print(f"Dia da semana: {dia_da_semana}")
        