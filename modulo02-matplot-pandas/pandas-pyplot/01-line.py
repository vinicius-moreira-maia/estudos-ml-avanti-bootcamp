import pandas as pd
from matplotlib import pyplot as plt

data = {    
    'ano': [1984, 1990, 1998, 2027],    
    'valor': [10, 25, 15, 30]
}

df = pd.DataFrame(data)

# eixo x e y
plt.plot(df['ano'], df['valor'], marker = 'o')

plt.xlabel('Ano')

plt.ylabel('Valor')

plt.title('Gráfico de Linhas')

plt.show()