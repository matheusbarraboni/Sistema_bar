def mensagem_erro(mensagem):
    print(f'\033[31mERRO!{mensagem}\033[m')


def titulo(nome, linha='-'):
    print(60 * f'{linha}')
    print(f'{nome:^60}')
    print(60 * f'{linha}')


def moeda(valor, cambio='R$'):
    return f'{cambio}{valor:.2f}'.replace('.',',')