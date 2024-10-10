from functions import *


while True:
    tela("Escolha uma Opção")

    print("1 - Fazer Login")
    print("2 - Criar uma Conta Cliente")
    print("3 - Para Funcionários da Livraria")
    print("0 - Sair")
    print("======\n")
    op = input("Opção: ")
    os.system("cls") or None

    match op:
        case "1":
            login()
        case "2":
            criarConta()
        case "3":
            os.system("cls") or None

            tela("Login")

            nome = input("Digite o Nome: ")
            password = input("Digite a Palavra-passe: ")

            funcionario()
        case "0":
            break
        case _:
            print("\033[0;31mOpção invalida!!!\033[m")
