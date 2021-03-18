'''Construir um algoritmo que contenha 3 listas:
•   Nomes de produtos
•   Preços de cada produto
•   Quantidades de cada produto
Construir uma função para imprimir um dos produtos da lista e uma função para retirar um dos produtos das listas'''


from time import sleep

lst_nomes = ["OI", "OIOI", "OIOIOI"]
lst_precos = [2, 4, 6]
lst_qtd = [20, 40, 60]

def adicionar():
    def nome_ok():
        while True:
            nome = input("Digite o nome do produto: ").upper()
            if nome not in lst_nomes:
                return nome
    def preco_ok():    
        while True:
            try:
                preco = int(input("Digite o preço: "))
                if preco > 0:
                    return preco
                else:
                    raise ValueError
            except ValueError:
                print("Digite somente números positivos.")
                sleep(1.5)
    def qtd_ok():    
        while True:
            try:
                qtd = int(input("Digite o preço: "))
                if qtd > 0 or qtd % 2 == 0:
                    return qtd
                else:
                    raise ValueError
            except ValueError:
                print("Digite somente números positivos.")
                sleep(1.5)
    print("\nCadastro de novo produto\n")
    sleep(1.5)
    lst_nomes.append(nome_ok())
    lst_precos.append(preco)
    lst_qtd.append(qtd)
    print("\nProduto cadastrado com sucesso.")
    sleep(0.75)

        else:
            print("Produto já cadastrado.")
            sleep(1.5)
        print(lst_nomes, lst_precos, lst_qtd)

def imprimir():
    x = input("Digite o nome do produto: ").upper()
    if x in lst_nomes:
        x = lst_nomes.index(x)
        print(lst_nomes[x], lst_precos[x], lst_qtd[x])

def remove_prod(lst, i):
    for x in lst:
        x.pop(i)

def retirar():
    remove_x = input("Digite o nome do produto: ").upper()
    if remove_x in lst_nomes:
        remove_x = lst_nomes.index(remove_x)
        remove_prod([lst_nomes, lst_precos, lst_qtd], remove_x)
        print(lst_nomes, lst_precos, lst_qtd)
    else:
        print("erro")

while True:
    print(lst_nomes, lst_precos, lst_qtd)
    try:
        menu = int(input("Escolha: "))
        if menu == 1:
            adicionar()
        elif menu == 2:
            imprimir()
        elif menu == 3:
            retirar()
    except ValueError:
        print("Opção inválida.")