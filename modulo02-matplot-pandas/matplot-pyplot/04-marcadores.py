import matplotlib.pyplot as plt
import numpy as np
import sys

data1, data2, data3, data4 = np.random.randn(4, 100) 

fig, ax = plt.subplots(figsize=(5, 2.7))

# sem essa opção, poderia haver sobreposiçõs indesejáveis
fig.set_constrained_layout(True)

# o, d, v e s são apenas estilos gráficos de marcadores
# são usados, aqui, para diferenciar uma linha da outra
# dessa forma, os dados são o eixo y, pois é o default pra quando eu passo apenas 1 conjunto de dados
# como não defini o eixo x, fica parecendo um gráfico scatter, mas é um Line2D
ax.plot(data1, 'o', label='data1')
#ax.plot(data2, 'd', label='data2')

# usando '-', eu conecto os pontos dos marcadores
ax.plot(data3, '-v', label='data3')
#ax.plot(data4, 's', label='data4')

# legend é só para mostrar uma legenda no gráfico
ax.legend()

plt.show()