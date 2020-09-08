import os
from utilities import textos

arq_cardapio = open('cardapio', 'r')
cardapio = []
for i in arq_cardapio:
    i = i.split(';')
    cardapio.append(i[0:3])
arq_cardapio.close()


def soma(val):
    total = sum(map(int, val))
    return total


# remove a file from the current directory
def remover_arquivo(nome):
    os.unlink(nome)


def mostrar_conta(mesa=-999):
    if mesa == -999:
        mesa = numero_mesa()
    a = open(str(mesa), 'r')
    itens = []
    soma = 0
    for i in a:
        itens.append(i)
    a.close()
    print(60 * '-')
    print(f'{"Conta mesa ":>35}{mesa}')
    print(60 * '-')
    print(f'{"Quant":6}|{"Produto":^29}|{" Val unit "}|{"Val total":^11}|')
    for i in itens:
        i = i.split(';')
        val_total = float(i[2]) * int(i[3])
        soma += val_total
        print(f'{i[3]:<4} x  {i[1]:<30}  {textos.moeda(float(i[2]))} {textos.moeda(val_total):>10}')
    print(60*'-')
    print(f'{"Valor total":>47} = {textos.moeda(soma)}')


def deletar_mesa(mesa=-999):
    if mesa == -999:
        mesa = numero_mesa()
    remover_arquivo(str(mesa))
    a = open('mesas_abertas', 'r')
    linhas = a.readline().split(';')
    a.close()
    b = open('mesas_abertas', 'w')
    cont = False
    for i in linhas:
        if i != str(mesa):
            b.write(f'{i};')
        else:
            cont = True
    b.close()
    if cont:
        print(f'Mesa {mesa} exlcuida!')
    else:
        print(f'Mesa {mesa} não está aberta!')


def numero_mesa():
    while True:
        try:
            mesa = int(input('Digite o número da mesa: '))
        except:
            textos.mensagem_erro('Número inválido!')
        else:
            break
    return mesa


def abrir_mesa(mesa=-999):
    if mesa == -999:
        mesa = numero_mesa()
    if existe_arquivo(str(mesa)) is False:
        a = open('mesas_abertas', 'a')
        a.write(f'{mesa};')
        a.close()
        b = open(str(mesa), 'a')
        b.write('estou aberto')
        b.close()
        print(f'Mesa {mesa} aberta com sucesso!')
    else:
        print('Mesa já aberta!')


def add_item_mesa():
    n_mesa = numero_mesa()
    if existe_arquivo(str(n_mesa)) is False:
        abrir_mesa(mesa=n_mesa)
    while True:
        try:
            cod = int(input('código do produto:'))
        except:
            textos.mensagem_erro('Digite um código válido!')
        else:
            existe = False
            for i in cardapio:
                if cod == int(i[0]):
                    existe = True
                    break
            if existe:
                break
            else:
                textos.mensagem_erro('Produto não encontrado')

    while True:
        try:
            quant = int(input('Quantidade:'))
        except:
            textos.mensagem_erro('Digite um número válido!')
        else:
            break

    for i in cardapio:
        if cod == int(i[0]):
            a = open(str(n_mesa), 'a')
            a.write(f'{i[0]};{i[1]};{i[2]};{quant};\n')
            a.close()
            print(f'Produto adicionado com sucesso na mesa {n_mesa}')


def mostrar_mesas():
    mesas_a = open('mesas_abertas', 'r')
    print('\033[34mMesas abertas:\033[m')
    print('\033[32m', end='')
    for i in mesas_a:
        cont = 0
        i = i.split(';')
        del (i[-1])
        i = list(map(int, i))
        i.sort()
        for j in i:
            print(f'{j}', end='    ')
            cont += 1
            if cont >= 10:
                print('')
                print('')
                cont = 0
    mesas_a.close()
    print('\033[m')


def cardapio_add():
    # defining a list to keep the data before add to the archive
    lista = [0, 0, 0]

    # the three while loops below get the info's needed to register the product
    while True:
        try:
            lista[0] = int(input('Codigo do produto:'))
        except:
            textos.mensagem_erro('Digite um código válido!')
        else:
            sair = True
            a = open('cardapio', 'r')
            for i in a:
                i = i.split(';')
                if int(i[0]) == lista[0]:
                    textos.mensagem_erro('Produto já cadastrado!')
                    sair = False
            a.close()
            if sair:
                break
    while True:
        try:
            lista[1] = str(input('Nome:')).capitalize()
        except KeyboardInterrupt:
            textos.mensagem_erro('Dígite um nome válido!')
        else:
            if ';' in lista[1]:
                textos.mensagem_erro('Caractere ";" inválido!')
            break
    while True:
        try:
            lista[2] = float((input('Preço:')).replace(',', '.'))
        except:
            textos.mensagem_erro('Digite um preço válido')
        else:
            break
    # opening a file to keep the data
    a = open('cardapio', 'a')
    a.write(f'{lista[0]};{lista[1]};{lista[2]};\n')  # data are added with a ';' to separate
    a.close()
    print('Produto cadastrado com sucesso!')


def cardapio_del():
    if existe_arquivo('cardapio'):
        while True:
            try:
                # cod will receive the value of the code to be deleted
                cod = int(input('Digite o código do produto a ser excluido:(-1 para sair) '))
            except:
                textos.mensagem_erro('Digite um código válido!')
            else:
                if cod != -1:
                    # a while loop to get the line of the txt that have the product
                    while True:
                        a = open('cardapio', 'r')
                        linhas = a.readlines()  # receive all the file's lines
                        a.close()
                        b = open('cardapio', 'w')
                        existe = False    # determine if there is a product with the code typed
                        for i in linhas:
                            i = i.split(';')    # transform a String in a list
                            if i[0] == str(cod):
                                existe = True
                            else:
                                b.write(f'{i[0]};{i[1]};{i[2]};{i[3]}')
                        b.close()
                        break
                    if existe is False:
                        print('\033[31mProduto não encontrado!\033[m')
                    else:
                        print('Produto excluido com sucesso!')
                        break
                else:
                    break
    else:
        print('\033[31mNão há produtos cadastrados!\033[m')


def existe_arquivo(nome):
    try:
        a = open(nome, 'r')
        a.close()
    except:
        return False
    else:
        return True
