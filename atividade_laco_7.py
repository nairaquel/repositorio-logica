import os 
os.system("clear||cls")

login_cadastrado = "naira"
senha_cadastrado = 246180
contador = 0

while True:
    login = ("Digite seu login: ")
    senha = ("Digite sua senha: ")
    if login_cadastrado == login  and senha_cadastrado == senha:
        print("Acesso permitido!")
        break
    else:
        print("acesso negado. \n")
        contador += 1
    if contador == 3:
        print("Número de tentativas acima do permitido!")
        break

         
         
