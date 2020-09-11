from utilities import func
from utilities import textos
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
                  opcao = int(input('Sua opção:'))
            except:
                  textos.mensagem_erro(' Digite um número válido!')
            else:
                  if opcao == 1:
                        func.abrir_mesa()
                        break
                  elif opcao == 2:
                        func.add_item_mesa()
                        break
                  elif opcao == 3:
                        print('1 - Ver Conta\n'
                              '2 - Adicionar pagamento')
                        while True:
                              try:
                                    opcao = int(input('Sua opção:'))
                              except:
                                    textos.mensagem_erro(' Digite um número válido!')
                              else:
                                    if opcao == 1:
                                          func.mostrar_conta()
                                          break
                                    elif opcao == 2:
                                          func.fechar_conta()
                                          break
                                    else:
                                          textos.mensagem_erro(' Opção inválida!')
                        break
                  elif opcao == 4:
                        func.deletar_mesa()
                        break
                  elif opcao == 5:
                        print('1 - Adicionar item\n'
                              '2 - Excluir item\n'
                              '3 - Mostrar cardápio completo')
                        while True:
                              try:
                                    opcao = int(input('Sua opção:'))
                              except:
                                    textos.mensagem_erro(' Digite um número válido!')
                              else:
                                    if opcao == 1:
                                          func.cardapio_add()
                                          break
                                    elif opcao == 2:
                                          func.cardapio_del()
                                          break
                                    else:
                                          textos.mensagem_erro(' Digite uma opção válida!')
                        break