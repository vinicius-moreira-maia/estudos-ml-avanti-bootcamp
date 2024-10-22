import pandas as pd
import matplotlib.pyplot as plt

# (max - min) / nº de bins
# (75 - 25) / 5 = 10
# 5 intervalos de 10 em 10
# os valores serão distribuídos nas barras em que couberem
'''
20 a 30 - 25 e 30 (2)
30 a 40 - 35 e 40 (2)
40 a 50 - 45 e 50 (2)
50 a 60 - 55 e 60 (2)
60 a 70 - 65, 70 e 75 (3)
'''

data = {
    'idade': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
}

df = pd.DataFrame(data)

# Histograma usando Matplotlib
# bins é o número de barras
# 'k' é preto na notação do matplot
plt.hist(df['idade'], bins=5, edgecolor='k')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.title('Histograma')
plt.show()