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


def valor_conta(mesa=-999):
    if mesa == -999:
        mesa = numero_mesa()
    a = open(str(mesa), 'r')
    soma = desconto = 0
    for i in a:
        i = i.split(';')
        if i[0].isnumeric():
            val_total = float(i[2]) * int(i[3])
            soma += val_total
        else:
            desconto += float(i[1])
    return soma - desconto


def mostrar_conta(mesa=-999):
    if mesa == -999:
        mesa = numero_mesa()
    a = open(str(mesa), 'r')
    itens = []
    soma = desconto = 0
    for i in a:
        itens.append(i)
    a.close()
    print(60 * '-')
    print(f'{"Conta mesa ":>35}{mesa}')
    print(60 * '-')
    print(f'{"Quant":6}|{"Produto":^29}|{" Val unit "}|{"Val total":^11}|')
    for i in itens:
        i = i.split(';')
        if i[0].isnumeric():
            val_total = float(i[2]) * int(i[3])
            soma += val_total
            print(f'{i[3]:<4} x  {i[1]:<30}  {textos.moeda(float(i[2]))} {textos.moeda(val_total):>10}')
        else:
            desconto += float(i[1])
    print(60*'-')
    print(f'{"Valor total":>47}:  {textos.moeda(soma)}')
    if desconto != 0:
        print(f'{"Desconto":>47}: -{textos.moeda(desconto)}')
        print(60 * '-')
        print(f'{"Novo total":>47}:  {textos.moeda(soma - desconto)}')


def fechar_conta(mesa=-999):
    if mesa == -999:
        mesa = numero_mesa()
    while True:
        if existe_arquivo(str(mesa)):
            mostrar_conta(mesa)
            val_conta = valor_conta(mesa)
            while True:
                try:
                    val_pago = float(input('Valor a ser pago  [0: valor total]\n'
                                                            f'{"[-1: sair]":>28}    :R$'))
                except:
                    textos.mensagem_erro('Dígite um valor válido')
                else:
                    if val_pago > val_conta:
                        textos.mensagem_erro('Valor digitado maior que o valor da conta!')
                    elif val_pago == val_conta or val_pago == 0:
                        pagamento(val_conta)
                        deletar_fechar_mesa(mesa)
                        print('Pagamento realizado com sucesso!')
                        sair = True
                        break
                    elif val_pago > 0 and val_pago < val_conta:
                        pagamento(val_pago)
                        a = open(str(mesa), 'a')
                        a.write(f'{"desconto"};{val_pago};\n')
                        a.close()
                        print('Pagamento realizado com sucesso!')
                        resp = ''
                        while True:
                            resp = input('Adicionar mais um pagamento a mesa? (S/N):').lower()
                            sair = False
                            if resp == 'n':
                                sair = True
                                break
                            elif resp == 's':
                                break
                            else:
                                textos.mensagem_erro(' Valor inválido!')
                        break
            if sair:
                break
        else:
            textos.mensagem_erro(' Mesa fechada!')
            mesa = numero_mesa()


def pagamento(valor):
    while True:
        try:
            forma = int(input(f'Digite a forma de pagamento: [1 para dinheiro]\n'
                              f'{"[2 para crédito]":>45}\n'
                              f'{"[3 para débito]":>44}: '))
        except:
            textos.mensagem_erro('Valor inválido!')
        else:
            lista = [1,2,3]
            if forma in lista:
                a = open('faturamento', 'a')
                a.write(f'{forma};{valor};\n')
                a.close()
                break
            else:
                textos.mensagem_erro('Opção inválida!')


def mostrar_faturamento():
    if existe_arquivo('faturamento'):
        print(60 * '-')
        print(f'{"Faturamento":^60}')
        print(60 * '-')
        a = open('faturamento', 'r')
        credito = s_credito = debito = s_debito = dinheiro = s_dinheiro = 0
        for i in a:
            i = i.split(';')
            if i[0] == '1':
                dinheiro += 1
                s_dinheiro += float(i[1])
            elif i[0] == '2':
                credito += 1
                s_credito += float(i[1])
            elif i[0] == '3':
                debito += 1
                s_debito += float(i[1])
        print(f'{dinheiro} pedidos pagos em dinheiro')
        print(f'totalizando {textos.moeda(s_dinheiro)}')
        print()
        print(f'{credito} pedidos pagos no crédito')
        print(f'totalizando {textos.moeda(s_credito)}')
        print()
        print(f'{debito} pedidos pagos no débito')
        print(f'totalizando {textos.moeda(s_debito)}')
        print(60 * '-')
        print(f'Valor total faturado: {textos.moeda(s_credito + s_debito + s_dinheiro)}')


    else:
        print('Não há registros de faturamento.')


def deletar_mesa(mesa=-999):
    if mesa == -999:
        mesa = numero_mesa()
    try:
        os.unlink(str(mesa))
    except:
        textos.mensagem_erro(f' Mesa {mesa} não está aberta!')
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


def deletar_fechar_mesa(mesa=-999):
    if mesa == -999:
        mesa = numero_mesa()
    try:
        os.unlink(str(mesa))
    except:
        textos.mensagem_erro(f' Mesa {mesa} não está aberta!')
    else:
        a = open('mesas_abertas', 'r')
        linhas = a.readline().split(';')
        a.close()
        b = open('mesas_abertas', 'w')
        for i in linhas:
            if i != str(mesa) and i != '':
                b.write(f'{i};')
        b.close()


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
            print(f'Produto adicionado com sucesso na mesa {n_mesa}.')


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
