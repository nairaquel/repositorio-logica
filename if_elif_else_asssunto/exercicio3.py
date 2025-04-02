import os
os.system ("clear")

# elabore um agoritimo para solicitar ao usuaria o login 



login_cadastrado =  "naira raquel"
senha_cadastrada = "2461"

login = input("Digite o login: ")
senha = input("Digite a senha: ")

if login == login_cadastrado and senha == senha_cadastrada:
    print("Bem vindo!")
else:
    print("Login ou Senha incorretos!")