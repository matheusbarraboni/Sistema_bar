from time import sleep

def mensagem_erro(mensagem):
    print(f'\033[31mERRO!{mensagem}\033[m')
    sleep(2)


def titulo(nome, linha='-'):
    print(60 * f'{linha}')
    print(f'{nome:^60}')
    print(60 * f'{linha}')


def colorido(texto, cor='branco', fundo=None, estilo='none'):
    lista_cor = {'branco':30, 'vermelho':31, 'verde':32, 'amarelo':33,
                 'azul':34, 'roxo': 35, 'ciano':36, 'cinza':37}
    lista_fundo = {'branco':40, 'vermelho':41, 'verde':42, 'amarelo':43,
                 'azul':44, 'roxo': 45, 'ciano':46, 'cinza':47}
    lista_estilo = {'none':0, 'bold':1, 'underline':4, 'negative':7}

    cor = lista_cor[cor]
    estilo = lista_estilo[estilo]

    if fundo == None:
       return f'\033[{estilo};{cor}m{texto}\033[m'
    else:
        fundo = lista_fundo[fundo]
        return f'\033[{estilo};{fundo};{cor}m{texto}\033[m'

def moeda(valor, cambio='R$'):
    return f'{cambio}{valor:.2f}'.replace('.',',')