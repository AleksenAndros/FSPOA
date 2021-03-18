'''Construir um algoritmo que contenha 3 listas:
•   Nomes de produtos
•   Preços de cada produto
•   Quantidades de cada produto
Construir uma função para imprimir um dos produtos da lista e uma função para retirar um dos produtos das listas'''

from time import sleep

lst_nomes = ["COCA-COLA", "FRUKI", "PEPSI", "SPRITE"]
lst_precos = [8.0, 5.0, 7.5, 6.0]
lst_qtd = [100, 40, 80, 60]

# --- função 1 ---

def adicionar():
    def nome_ok():
        while True:
            nome = input("\nDigite o nome do produto: ").upper()
            if nome not in lst_nomes:
                return nome
            else:
                print("\nProduto já cadastrado.")
                sleep(0.75)
    def preco_ok():    
        while True:
            try:
                preco = float(input("\nDigite o preço: "))
                if preco > 0:
                    return preco
                else:
                    raise ValueError
            except ValueError:
                print("\nDigite somente números positivos.")
                sleep(0.75)
    def qtd_ok():    
        while True:
            try:
                qtd = int(input("\nDigite a quantidade: "))
                if qtd > 0:
                    return qtd
                else:
                    raise ValueError
            except ValueError:
                print("\nDigite somente números positivos.")
                sleep(0.75)
    print("\nCadastro de novo produto")
    sleep(1.5)
    lst_nomes.append(nome_ok())
    lst_precos.append(preco_ok())
    lst_qtd.append(qtd_ok())
    print("\nProduto cadastrado com sucesso.")
    sleep(0.75)

# --- função 2

def imprimir():
    print("\nProdutos:\n")
    sleep(0.75)
    for x in lst_nomes:
        print(x)
    while True:
        x = input("\nDigite o nome do produto: ").upper()
        if x in lst_nomes:
            x = lst_nomes.index(x)
            print("\nNome: {} | Preço: R${} | Quantidade: {}".format(lst_nomes[x], lst_precos[x], lst_qtd[x]))
            sleep(0.75)
            break
        else:
            print("\nProduto não consta no sistema")
            sleep(0.75)

# --- função 3 ---

def retirar():
    def remove_prod(lst, i):
        for x in lst:
            x.pop(i)
    print("Produtos:\n")
    sleep(0.75)
    for x in lst_nomes:
        print(x)
    while True:
        remove_x = input("\nDigite o nome do produto a ser removido: ").upper()
        if remove_x in lst_nomes:
            remove_x = lst_nomes.index(remove_x)
            remove_prod([lst_nomes, lst_precos, lst_qtd], remove_x)
            print("\nProduto removido com sucesso.")
            sleep(0.75)
            break
        else:
            print("\nProduto não consta no sistema.")
            sleep(0.75)

# --- menu de escolha ---

while True:
    try:
        menu = int(input('''
    MENU
    1- Cadastrar produto
    2- Detalhes do produto
    3- Remover produto
    0- Encerrar programa
    Escolha: '''))
        if menu == 0:
            print("\nFinalizando...")
            sleep(1.5)
            break
        elif menu == 1:
            adicionar()
            input("\nPressione Enter para prosseguir")
        elif menu == 2:
            imprimir()
            input("\nPressione Enter para prosseguir")
        elif menu == 3:
            retirar()
            input("\nPressione Enter para prosseguir")
        else:
            raise ValueError
    except ValueError:
        print("\nOpção inválida.")
        sleep(1)