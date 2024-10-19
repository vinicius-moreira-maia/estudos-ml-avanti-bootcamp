import matplotlib.pyplot as plt
import numpy as np

data1, data2, data3, data4 = np.random.randn(4, 100) 
xdata = np.arange(len(data1)) 

# 2 linhas, 1 coluna
fig, axs = plt.subplots(2, 1, layout='constrained')

axs[0].plot(xdata, data1)
axs[0].set_title('Ticks automáticos')



axs[1].plot(xdata, data1)
axs[1].set_title('Ticks manuais')

# ticks são os nomes de valores dos eixos
# array com números de 0 a 100, passo 30 (0, 30, 60 e 90)
# a lista são os nomes de cada 'tick'
axs[1].set_xticks(np.arange(0, 100, 30), ['zero', '30', 'sixty', '90'])

# apenas 3 ticks, os nomes serão os próprios valores
axs[1].set_yticks([-1.5, 0, 1.5]) 

plt.show()
