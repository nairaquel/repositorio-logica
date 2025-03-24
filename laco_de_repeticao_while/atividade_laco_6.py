import os 
os.system("clear||cls")

login = "naira"
senha = 246180

while True:
    login_1 = (input("Digite login: "))
    senha_1 = int(input("Digite sua senha: "))

    if login_1 ==  login and senha_1 == senha:
        print("Acesso permitido!")
    else:
        print("Acesso negado!")

    print()
    print("Fim")
     
         
         
