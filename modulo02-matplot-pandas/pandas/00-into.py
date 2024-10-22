import pandas as pd

'''
NumPy é escrito diretamente em C, e não a partir das estruturas do Python (como listas, tuplas, etc.). Portanto a maioria das operações
matemáticas são processadas em C.
Em C, arrays são blocos contínuos de memória, com acesso imediato (O(1)).
Portanto as operações no NumPy são todas vetorizadas, ou seja, executadas na estrutura como um todo de uma só vez.
Listas, ao contrário, são objetos que apontam
para outros objetos em lugares diferentes na memória, portanto necessariamente são estruturas iterativas.
'''

'''
pandas é construído em cima do numpy, portanto facilmente integrável com ele e bastante performático

2 estruturas:
dataframe = estrutura de dados tabular, semelhante a uma tabela de BD
series = estrutura unidimensional, semelhante a uma coluna de dataframe ou a um array
'''

df = pd.DataFrame({"Name": [ "Braund, Mr. Owen Harris",
                             "Allen, Mr. William Henry",
                             "Bonnell, Miss. Elizabeth"],
                   "Age": [22, 35, 58],
                   "Sex": ["male", "male", "female"]})

print(df)

print()

print(df["Age"])
print(type(df["Age"])) # selecionar uma coluna é selecionar uma Series

print()

print(f"idade máxima: {df['Age'].max()}")

print()

# estatísticas básicas
print(df.describe())