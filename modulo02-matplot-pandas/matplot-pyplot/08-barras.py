import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(5, 2.7))

# Define o layout restrito
fig.set_constrained_layout(True)

# cada catehoria é uma barra
categories = ['turnips', 'rutabaga', 'cucumber', 'pumpkins']

# bar() é o gráfico de barras, obviamente
# as categorias serão o eixo x
# o array possui 4 números (len(categories)) aleatórios entre 0 e 1
ax.bar(categories, np.random.rand(len(categories)))

plt.show()