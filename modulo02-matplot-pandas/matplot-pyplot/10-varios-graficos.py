import matplotlib.pyplot as plt

# mosaico permite maior flexibilidado no uso de vários subgráficos em uma mesma figura
# layout constrained permite ajuste automático de espaçamento
# right significa que o gráfico da direita ocupa toda a segunda coluna
fig, ax = plt.subplot_mosaic([['upleft', 'right'],
                               ['lowleft', 'right']], layout='constrained')

# dando títulos aos subgráficos
ax['upleft'].set_title('upleft')
ax['lowleft'].set_title('lowleft')
ax['right'].set_title('right')

plt.show()