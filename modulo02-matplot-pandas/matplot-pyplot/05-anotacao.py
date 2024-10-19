import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(5, 2.7))

# criação dos arrays de dados (mesma quantidade de elementos nos 2)
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2 * np.pi * t)

# lw = line width
line, = ax.plot(t, s, lw=2)

# local max é o nome da anotação
# xy são as coordenadas da seta
# xytext são as coordenadas da anotação
# arrowprops são propriedades de estilo da seta
# shrink aqui diz que a seta irá ligar os pontos, mas terá 5% de espaço entre eles
ax.annotate(   
     'local max', xy=(2, 1), xytext=(3, 1.5),
      arrowprops=dict(facecolor='red', shrink=0.05)
)

# definindo até qual valor o eixo y suportará
ax.set_ylim(-2, 2)

plt.show()