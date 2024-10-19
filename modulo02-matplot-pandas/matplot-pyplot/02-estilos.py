import matplotlib.pyplot as plt
import numpy as np

data1, data2, data3, data4 = np.random.randn(4, 100) 

# por padrão, só retorna um subgráfico
fig, ax = plt.subplots(figsize=(5, 2.7))

# aqui vai grar um array de 0 a 100
x = np.arange(len(data1))

# cumsum retorna um novo array com a soma cumulativa de cada elemento do array original
# x é o array de 0 a 100, y é o da soma cumulativa
# o resto são configurações de estilo
#ax.plot(x, np.cumsum(data1), color='blue', linewidth=3, linestyle='--')

estilo = {'color':'blue', 
          'linewidth':3, 
          'linestyle':'--'}

# plot retorna uma Line2D, então posso ter 2 em um só eixo (subgráfico), conforme abaixo
ax.plot(x, np.cumsum(data1), **estilo)
l, = ax.plot(x, np.cumsum(data2), color='orange', linewidth=2)

# como o retorno é uma Line2D, eu posso estilizá-la ainda mais
l.set_linestyle(':')

plt.show()