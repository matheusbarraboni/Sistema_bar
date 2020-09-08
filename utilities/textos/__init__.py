def mensagem_erro(mensagem):
    print(f'\033[31mERRO!{mensagem}\033[m')


def moeda(valor, cambio='R$'):
    return f'{cambio}{valor:.2f}'.replace('.',',')