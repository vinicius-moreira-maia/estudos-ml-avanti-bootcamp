import numpy as np
import pandas as pd

'''
1- Use a lista de números: [12, 45, 67, 23, 89, 34, 22, 90, 56, 78].
2- Calcule a média dos números usando a biblioteca numpy.
3- Identifique os números que são maiores que a média.
4- Armazene os números maiores que a média em um DataFrame do pandas.
5- Salve o DataFrame em um arquivo CSV chamado "numeros_maiores_que_media.csv"
'''

# 1
lista = np.array([12, 45, 67, 23, 89, 34, 22, 90, 56, 78])
print(lista)

# 2
media = lista.mean()
print(media)

# 3
maiores_media = lista[lista > media]
print(maiores_media)

# 4
df = pd.DataFrame({"maiores_media" : maiores_media})
print(df)

# 5
df.to_csv("numeros_maiores_que_media.csv")