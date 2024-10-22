import pandas as pd
from matplotlib import pyplot as plt

data = {    
    'categoria': ['A', 'B', 'C', 'D'],    
    'valor': [10, 25, 15, 30]
}

df = pd.DataFrame(data)

# eixo x e y
plt.bar(df['categoria'], df['valor'])

plt.xlabel('Categoria')

plt.ylabel('Valor')

plt.title('Gráfico de Barras')

plt.show()