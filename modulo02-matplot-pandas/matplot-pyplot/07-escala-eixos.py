import matplotlib.pyplot as plt
import numpy as np

data1, data2, data3, data4 = np.random.randn(4, 100) 

# 1 linha, 2 colunas (2 subgráficos)
fig, axs = plt.subplots(1, 2, figsize=(5, 2.7))

# Define o layout restrito
fig.set_constrained_layout(True) 

# arrays para os dados dos eixos x e y
xdata = np.arange(len(data1)) 
data = 10**data1

# gráfico 1
axs[0].plot(xdata, data)

# gráfico 2 (alterando de escala linear, default, para escala logarítmica)
axs[1].set_yscale('log')
axs[1].plot(xdata, data)

plt.show()