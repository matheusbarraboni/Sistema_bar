from utilities import func
from utilities import textos
from time import sleep


def tela3():
    print('1 - Ver Conta\n'
          '2 - Adicionar pagamento')
    while True:
        try:
            opcoes_3[int(input('Sua opção:'))]()
        except KeyError:
            textos.mensagem_erro(' Digite uma opção válida!')
        except ValueError:
            textos.mensagem_erro(' Digite um número válido!')
        else:
            break


def tela5():
    print('1 - Adicionar item\n'
          '2 - Excluir item\n'
          '3 - Mostrar cardápio completo')
    while True:
        try:
            opcoes_5[int(input('Sua opção:'))]()
        except KeyError:
            textos.mensagem_erro(' Digite uma opção válida!')
        except ValueError:
            textos.mensagem_erro(' Digite um número válido!')
        else:
            break


opcoes_gerais = {
    1: func.abrir_mesa,
    2: func.add_item_mesa,
    3: tela3,
    4: func.deletar_mesa,
    5: tela5,
    6: func.mostrar_faturamento
}
opcoes_3 = {
    1: func.mostrar_conta,
    2: func.fechar_conta
}
opcoes_5 = {
    1: func.cardapio_add,
    2: func.cardapio_del,
    3: func.mostrar_cardapio
}

while True:
    textos.titulo('Sistema Bar', '=')
    func.mostrar_mesas()
    textos.titulo('Opções')
    print(f'{textos.colorido("1", "verde")} {textos.colorido("- Abrir Mesa")}\n'
          f'{textos.colorido("2", "verde")} {textos.colorido("- Adicionar produto a mesa")}\n'
          f'{textos.colorido("3", "verde")} {textos.colorido("- Conta da Mesa")}\n'
          f'{textos.colorido("4", "verde")} {textos.colorido("- Excluir mesa")}\n'
          f'{textos.colorido("5", "verde")} {textos.colorido("- Gerenciar cardápio")}\n'
          f'{textos.colorido("6", "verde")} {textos.colorido("- Ver faturamento")}')
    while True:
        try:
            opcoes_gerais[int(input('Sua opção:'))]()
        except ValueError:
            textos.mensagem_erro(' Digite um número válido!')
        except KeyError:
            textos.mensagem_erro(' Opção inválida!')
        else:
            sleep(2)
            break
