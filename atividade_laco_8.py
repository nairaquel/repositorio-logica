import os 
os.system("clear||cls")

login_cadastrado = "naira"
senha_cadastrado = "246180"


for i in range(3):
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    if login_cadastrado == login  and senha_cadastrado == senha:
        print("Acesso permitido!")
        break
    else:
        print("acesso negado. \n")
        if i == 2:
            print("Número de tentativas acima do permitido!")
        

         
         
