import os
import time
os.system("cls || clear")

lista_nomes = []

#Função que verifica se a lista está vazia
def verificar_lista_vazia (lista_nomes):
    if not lista_nomes:
        return True
    return False

#Função para adicionar
def adicionar_nome(lista_nomes):
    nome = input ("Digite seu nome: ")
    lista_nomes.append(nome)
    print (f"\n{nome} adicionado com sucesso.")

#Funcao para mostrar todos os nomes da lista.

def listar_nomes(lista_nomes):
    if verificar_lista_vazia(lista_nomes):
        print ("\nA lista está vazia.")
        return
    print("\nLista de nomes:")
    for nome in lista_nomes:
        print (f"- {nome}")

def excluir_nome(lista_nomes):
    if verificar_lista_vazia(lista_nomes):
        print ("\nA lista está vazia.")
        return
    listar_nomes(lista_nomes)
    nome_remover = input("\nDigite o nome que deseja remover: ")
    if nome_remover in lista_nomes:
        lista_nomes.remove(nome_remover)
        print (f"\n{nome_remover} removido com sucesso.")
    else:
        print (f"\n{nome_remover} não encontrado na lista.")

def atualizar_nome (lista_nomes):
    nome_antigo = input("Digite o nome que deseja atualizar: ")
    if nome_antigo in lista_nomes:
        novo_nome = input("Digite o novo nome: ")
        indice = lista_nomes.index(nome_antigo)
        lista_nomes[indice] = novo_nome
        print (f"\n{nome_antigo} atualizado para {novo_nome}.")
    else:
        print (f"\n{nome_antigo} não encontrado na lista.")
    
#Mostrando menu
while True:
    print ("""
Gerenciador de nomes -
1 - Adicionar
2 - Listar todos os nomes
3 - Atualizar nomes
4 - Remover nomes
5 - Sair
Escolha uma opção: """)
    opcao = int (input("Digite a opção desejada: "))
    
    match opcao:
        case 1:
            adicionar_nome(lista_nomes)
        case 2:
            listar_nomes(lista_nomes)
        case 3:
            atualizar_nome(lista_nomes)
        case 4:
            excluir_nome(lista_nomes)
        case 5:
            print("Saindo do programa...")
            time.sleep(2)
            os.system("cls || clear")
            break
        case _:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)
            os.system("cls || clear")
    os.system("cls || clear")
    time.sleep(2)
    os.system("cls || clear")

