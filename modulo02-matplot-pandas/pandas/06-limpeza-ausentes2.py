import pandas as pd

df = pd.DataFrame({"time": [None, "fortaleza", "flamengo", "ceará", None,"ceará","bahia" ,"ceará" , "fortaleza", None, "real madrid"]})

arr = []
for i,time in enumerate(df["time"]):
    if i in (5, 7):
        arr.append(None)
        continue
    arr.append(f"Neymar")

# adicionando nova coluna
df["jogador"] = arr

print(df)

# se a quantidade de elementos nulos for baixa, pode-se excluir as linhas, não impactará significativamente o resultado

# Remover linhas com valores ausentes em qualquer coluna (muta o df original)
df.dropna(inplace=True)

print()
print(df)

# Remover linhas com valores ausentes em colunas específicas
df.dropna(subset=['jogador'], inplace=True)

print(df)