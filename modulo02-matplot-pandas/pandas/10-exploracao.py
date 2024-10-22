import pandas as pd

df = pd.DataFrame({"nome": ["Waldir", "Kaio", "Diego", "Biu", "Biu", "Diquinho"], "salario": [12000, 9000, 5000, 3200, 1250, 700]})

# média
print(df["salario"].mean())

# mediana
print(df["salario"].median())

# desvio padrão
# desvio padrão avalia a dispersão dos dados em relação à média
# quanto mais alto mais dispersos
print(df["salario"].std())

print(df["salario"].min())
print(df["salario"].max())

print()

# contagem de valores únicos
print(df["nome"].value_counts())

# valores únicos
print(df["nome"].unique())

# filtragem com base em condição
linha_maior_sal = df[df['salario'] == df['salario'].max()]
print(f"Quem tem o maior slário? {linha_maior_sal['nome'][0]}")
