import pandas as pd

# leitura
df = pd.read_csv("titanic.csv")
print(df.head(3))

# tipos de todas as colunas
print(df.dtypes)

# coleção com todas as colunas
print(df.columns)

# selecionando colunas
print(df[["Name", "Survived"]].head())

# filtrando linhas específicas
print()
print(df["Age"] > 35)