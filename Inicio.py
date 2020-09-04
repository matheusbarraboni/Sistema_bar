from utilities import func
from utilities import textos

print(60*'=')
print(f'{"Sistema bar":^60}')
print(60*'=')
arq_cardapio = open('cardapio', 'r')
cardapio = []
for i in arq_cardapio:
    i = i.split(';')
    cardapio.append(i[0:3])
arq_cardapio.close()
#  func.mostrar_mesas()

