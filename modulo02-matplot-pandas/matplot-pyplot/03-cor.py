import matplotlib.pyplot as plt
import numpy as np

data1, data2, data3, data4 = np.random.randn(4, 100) 

fig, ax = plt.subplots(figsize=(5, 2.7))

# facecolor é o fill
# edgecolor é o stroke
# s é o tamanho da bolinha do gráfico de dispersão
# k e C0 são códios de cor do próprio matplot
ax.scatter(data1, data2, s=50, facecolor='C0', edgecolor='k')

plt.show()

# parei no slide 11