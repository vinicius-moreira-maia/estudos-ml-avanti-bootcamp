import matplotlib.pyplot as plt
import numpy as np

data1, data2, data3, data4 = np.random.randn(4, 100) 

fig, ax = plt.subplots(figsize=(5, 5))

fig.set_constrained_layout(True)

ax.plot(np.arange(len(data1)), data1, label='linha 1')
ax.plot(np.arange(len(data2)), data2, label='linha 2')

# aqui será exibido como um scatter, pois eu forneci estilo de marcador
ax.plot(np.arange(len(data3)), data3, 'd', label='linha 3')

# mostrando a legenda
ax.legend()

plt.show()