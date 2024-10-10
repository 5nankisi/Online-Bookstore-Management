from classes import *
from datetime import datetime
import pickle
import os

listaCliente = ListaCliente()
listaLivro = ListaLivro()


def tela(sect):
    print("*******************************************************************************************")
    print("                                Livraria Camões")
    print("*******************************************************************************************\n\n")
    print(f"================== {sect} ==================")


def gravarLista(lista, nome):
    arq = open(nome + ".pkl", "wb")
    pickle.dump(lista, arq)
    arq.close()


def lerLista(nome):
    arq = open(nome + ".pkl", "rb")
    lista = pickle.load(arq)
    arq.close()
    return lista


def criarConta():
    while True:
        listaCliente = ListaCliente()
        os.system("cls") or None
        tela("Criar Conta")

        nome = input("Nome: ")
        nacionalidade = input("Nacionalidade: ")
        bi = input("Nº B.I.: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        profissao = input("Profissão: ")
        morada = input("Morada: ")
        numCartCred = input("Nº de Cartão de Crédito: ")

        password = input("Palavra-passe: ")

        while password != input("Digite a Palavra-passe novamente: "):
            print("\033[0;31mPalavra-passe incorreta!!!\033[m")
            password = input("Palavra-passe: ")

        dec = (input("Deseja salvar esses dados? [S/N]: ")).upper()

        while dec not in "SN":
            print("\033[0;31mComando Invalido!!!\033[m")
            dec = (input("Deseja salvar esses dados? [S/N]: ")).upper()

        if dec == "S":
            cliente = Cliente(nome, nacionalidade, email, password, numCartCred, profissao, bi, morada, telefone)

            try:
                listaCliente = lerLista("ListaCliente")
            except:
                gravarLista(listaCliente, "ListaCliente")

            listaCliente.append(cliente)

            gravarLista(listaCliente, "ListaCliente")
            return
        else:
            continue


def login():
    os.system("cls") or None

    listaCliente = ListaCliente()

    try:
        listaCliente = lerLista("ListaCliente")
    except:
        gravarLista(listaCliente, "ListaCliente")

    if listaCliente.head is None:
        print("\033[0;33mAinda não existem clientes cadastrados.\033[m")
        return

    acesso = False

    while True:
        cliente = None

        tela("login")

        nome = input("Digite o Nome: ")
        password = input("Digite a Palavra-passe: ")

        for i in range(0, len(listaCliente)):
            if nome == listaCliente[i].nome and password == listaCliente[i].password:
                acesso = True
                cliente = listaCliente[i]
                break

        if acesso:
            os.system("cls") or None
            homeClientes(cliente)
            break
        else:
            print(f"\033[0;31m!!!!!!!!!!!!!!!!! Senha Incorreta !!!!!!!!!!!!!!!!!\033[m")


def homeClientes(cliente):

    tela("Home")
    print("\n================== Escolha uma Opção ==================")
    print("1 - Pesquisar Por Livros")
    print("2 - Listar Todos os Livros da Livraria")
    print("0 - Sair")
    print("=====\n")
    op = int(input("Opção: "))
    os.system("cls") or None

    match op:
        case 1:
            pesquisarLivros(cliente)
        case 2:
            listarTodosLivros(cliente)
        case 0:
            return
        case _:
            print("\033[0;31mOpção invalida!!!\033[m")


def pesquisarLivros(cliente):
    os.system("cls") or None

    listaLivro = ListaLivro()

    try:
        listaLivro = lerLista("ListaLivro")
    except:
        gravarLista(listaLivro, "ListaLivro")

    if listaLivro.head is None:
        print("\033[0;33mAinda não existem livros em nossa livraria.\033[m")
        homeClientes(cliente)
        return

    tela("Pesquisar Livro")

    op = input("Digite o Título/ISBN/Nome do Autor do Livro: ")

    existe = False

    for i in range(0, len(listaLivro)):
        if op.upper() in (str(listaLivro[i].titulo)).upper() or op.upper() in (str(listaLivro[i].autor)).upper() or op.upper() in (str(listaLivro[i].isbn)).upper() or op.upper() in (str(listaLivro[i].editora)).upper():
            existe = True
            break

    if not existe:
        print("\033[0;33mNão existe nenhum livro com essas referências!!!\033[m")
        homeClientes(cliente)
    else:
        print("=================================\nResultado da Pesquisa\n")

        print("=====================================================================================================================================================================================================")
        for j in range(0, len(listaLivro)):
            if op.upper() in (str(listaLivro[j].titulo)).upper() or op.upper() in (str(listaLivro[j].autor)).upper() or op.upper() in (str(listaLivro[j].isbn)).upper() or op.upper() in (str(listaLivro[j].editora)).upper():
                print(f"""Título: {listaLivro[j].titulo}          ISBN: {listaLivro[j].isbn}          Author: {listaLivro[j].autor}           Editora: {listaLivro[j].editora}            Ano de Publicação: {listaLivro[j].anoDePubli}           Preço: {listaLivro[j].preco} Kzs
=====================================================================================================================================================================================================""")

        print("\n\n\n")
        homeClientes(cliente)


def listarTodosLivros(cliente):
    carrinho = Carrinho()
    listaLivro = ListaLivro()

    try:
        listaLivro = lerLista("ListaLivro")
    except:
        gravarLista(listaLivro, "ListaLivro")

    while True:
        os.system("cls") or None

        if listaLivro.head is None:
            print("\033[0;33mAinda não existem livros em nossa livraria.\033[m")
            homeClientes(cliente)
            return

        tela("Lista de Todos os Livros Disponíveis para Compra e Aluguel")

        print(f"\n\n\033[0;35mCarrinho: {len(carrinho)}\033[m\n\n")

        print("=====================================================================================================================================================================================================")
        for j in range(0, len(listaLivro)):
                print(f"""Título: {listaLivro[j].titulo}          ISBN: {listaLivro[j].isbn}          Autor: {listaLivro[j].autor}            Editora: {listaLivro[j].editora}            Ano de Publicação: {listaLivro[j].anoDePubli}           Preço: {listaLivro[j].preco} Kzs
=====================================================================================================================================================================================================""")

        existe = False

        while True:
            isbn = input("Digite o I.S.B.N. do Livro: ")

            for k in range(0, len(listaLivro)):
                if listaLivro[k].isbn == isbn:
                    existe = True
                    break

            if existe:
                break
            else:
                print("\033[0;31mI.S.B.N. Inexistente!!!\033[m")
                #homeClientes(cliente)
                #return
                break

        print("*** Pretende: ")
        print("1 - Adicionar ao Carrinho")
        print("2 - Ver Carrinho")
        print("0 - Sair")
        print("=====")
        op = int(input("Opção: "))
        os.system("cls") or None

        match op:
            case 1:
                for l in range(0, len(listaLivro)):
                    if listaLivro[l].isbn == isbn:
                        carrinho.append(listaLivro[l])
                        listaLivro.remove(listaLivro[l])
                        print("\033[0;32mLivro Adicionado ao Carrinho!!!\033[m")
                        feito = input("Pressione qualquer tecla para continuar: ")
                        if len(listaLivro) == 0:
                            functionCarrinho(cliente, carrinho, listaLivro)
                        break

                continue

            case 2:
                functionCarrinho(cliente, carrinho, listaLivro)
            case 0:
                homeClientes(cliente)
                return
            case _:
                print("\033[0;31mOpção invalida!!!\033[m")
                continue


def funcionario():
    os.system("cls") or None

    tela("Home para Funcionários")
    print("\n================== Escolha uma Opção ==================")
    print("1 - Adicionar Livros")
    print("2 - Remover Livros")
    print("3 - Ver Todos Livros")
    print("0 - Sair")
    print("=====\n")
    op = input("Opção: ")
    os.system("cls") or None

    match op:
        case "1":
            adicionarLivro()
        case "2":
            removerLivro()
        case "3":
            verTodosLivros()
        case "0":
            return
        case _:
            print("\033[0;31mOpção invalida!!!\033[m")


def adicionarLivro():
    listaLivro = ListaLivro()

    os.system("cls") or None

    tela("Adicionar Livros")

    titulo = input("Título: ")
    isbn = input("I.S.B.N.: ")
    autor = input("Autor: ")
    editora = input("Editora: ")
    anoDePubli = input("Ano de Publicação: ")
    preco = input("Preço: ")

    livro = Livro(titulo, isbn, autor, editora, anoDePubli, preco)

    try:
        listaLivro = lerLista("ListaLivro")
    except:
        gravarLista(listaLivro, "ListaLivro")

    listaLivro.append(livro)

    gravarLista(listaLivro, "ListaLivro")

    print(f"\033[0;32mLivro Adicionado com Sucesso!!!\033[m")
    add = input("Pressione qualquer tecla para continuar: ")
    funcionario()


def functionCarrinho(cliente, carrinho, listaLivro):
    while True:
        os.system("cls") or None

        tela("Carrinho")

        print(f"\n\033[0;35mCarrinho: {len(carrinho)}\033[m\n")

        if len(carrinho) == 0:
            print(f"\033[0;31mCarrinho Vazio\033[m")
            vazio = input("Pressione qualquer tecla para continuar: ")
            break

        for o in range(0, len(carrinho)):
            print(f"""=====================================================================================================================================================================================================

Título: {carrinho[o].titulo}            ISBN: {carrinho[o].isbn}            Autor: {carrinho[o].autor}          Editora: {carrinho[o].editora}          Ano de Publicação: {carrinho[o].anoDePubli}         Preço: {carrinho[o].preco} Kzs
=====================================================================================================================================================================================================""")

        existe = False

        title = ""
        author = ""
        editor = ""
        price = ""

        isbn = input("Digite o I.S.B.N. do Livro: ")

        for m in range(0, len(carrinho)):
            if carrinho[m].isbn == isbn:
                title = carrinho[m].titulo
                author = carrinho[m].autor
                editor = carrinho[m].editora
                price = carrinho[m].preco
                existe = True
                break

        print("*** Pretende: ")
        print("1 - Remover do Carrinho")
        print("2 - Comprar Livro")
        print("3 - Reservar Livro")
        print("0 - Sair")
        print("=====")

        op = input("Opção: ")

        if op == "1":
            if existe:
                for n in range(0, len(carrinho)):
                    if carrinho[n].isbn == isbn:
                        listaLivro.append(carrinho[n])
                        carrinho.remove(carrinho[n])
                        print("\033[0;32mLivro Removido do Carrinho!!!\033[m")
                        feito = input("Pressione qualquer tecla para continuar: ")
                        break
            else:
                print("\033[0;31mI.S.B.N. Inexistente no Carrinho!!!\033[m")

            continue
        elif op == "2" or op == "3":
            if op == "2":
                option = "Compra"
            else:
                option = "Reserva"

            arq = open(f"Recibo{isbn + cliente.nome + option}.txt", "w")
            relatorio = f"""
                                                {option} de Livro

                        ********************************************************************************
                        Título: {title}         I.S.B.N.: {isbn}            Autor: {author}

                        Editora: {editor}       Preço: {price}

                        ********************************************************************************
                                                Dados do Cliente

                        ********************************************************************************                        
                        Nome: {cliente.nome}    E-mail: {cliente.email}     B.I.: {cliente.bi}

                        Morada: {cliente.morada}                            Telefone: {cliente.telefone}

                        Nº de Cartão de Crédito: {cliente.numCartCred}      Data: {datetime.now()}
                        """

            arq.write(relatorio)
            arq.close()

            if op == "2":
                option = "Comprado"
            else:
                option = "Reservado"

            print(f"\033[0;32mLivro {option} com Sucesso!!!\033[m")
            feito = input("Pressione qualquer tecla para continuar: ")

            for p in range(0, len(carrinho)):
                if carrinho[p].isbn == isbn:
                    carrinho.remove(carrinho[p])
                    break

            if carrinho.head is None:
                break

            continue
        elif op == "0":
            break
        else:
            print("\033[0;31mOpção invalida!!!\033[m")
            continue


def removerLivro():
    listaLivro = ListaLivro()

    os.system("cls") or None

    tela("Remover Livros")

    try:
        listaLivro = lerLista("ListaLivro")
    except:
        gravarLista(listaLivro, "ListaLivro")

    isbn = input("Digite o I.S.B.N. do Livro: ")

    for k in range(0, len(listaLivro)):
        if listaLivro[k].isbn == isbn:
            listaLivro.remove(listaLivro[k])
            gravarLista(listaLivro, "ListaLivro")
            print(f"\033[0;32mLivro Removido com Sucesso!!!\033[m")
            remove = input("Pressione qualquer tecla para continuar: ")
            funcionario()

    print("\033[0;31mI.S.B.N. Inexistente!!!\033[m")
    noExist = input("Pressione qualquer tecla para continuar: ")
    funcionario()


def verTodosLivros():
    listaLivro = ListaLivro()

    try:
        listaLivro = lerLista("ListaLivro")
    except:
        gravarLista(listaLivro, "ListaLivro")

    os.system("cls") or None

    if listaLivro.head is None:
        print("\033[0;33mAinda não existem livros em nossa livraria.\033[m")
        funcionario()
        return

    tela("\033[0;32mLista de Todos os Livros\033[m")
    print("\n")

    print("=====================================================================================================================================================================================================")
    for j in range(0, len(listaLivro)):
        print(f"""Título: {listaLivro[j].titulo}          ISBN: {listaLivro[j].isbn}          Autor: {listaLivro[j].autor}            Editora: {listaLivro[j].editora}            Ano de Publicação: {listaLivro[j].anoDePubli}           Preço: {listaLivro[j].preco} Kzs
=====================================================================================================================================================================================================""")

    fim = input("Pressione qualquer tecla para continuar: ")
    funcionario()
