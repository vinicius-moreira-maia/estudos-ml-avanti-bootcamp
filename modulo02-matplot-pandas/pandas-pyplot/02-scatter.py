import pandas as pd
from matplotlib import pyplot as plt

data = {    
    'ano': [1984, 1990, 1998, 2027],    
    'valor': [10, 17, 15, 19]
}

df = pd.DataFrame(data)

# eixo x e y
plt.scatter(df['ano'], df['valor'], marker = 'o')

plt.xlabel('Ano')

plt.ylabel('Valor')

plt.title('Gráfico de Dispersão')

plt.show()