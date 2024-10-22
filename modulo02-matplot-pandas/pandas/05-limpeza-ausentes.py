import pandas as pd

df = pd.DataFrame({"time": [None, "fortaleza", "flamengo", "ceará", None,"ceará","bahia" ,"ceará" , "fortaleza", None, "real madrid"]})

arr = []
for i,time in enumerate(df["time"]):
    if i in (5, 7):
        arr.append("")
        continue
    arr.append(f"Neymar")

# adicionando nova coluna
df["jogador"] = arr

print(df)

# Se você deseja tratar strings vazias como nulas, precisará substituí-las explicitamente por valores nulos (np,nan ou None) 
# string vazia não é nulo, no pandas
df.replace("", None, inplace=True)

# True se for nulo, False se não for

# Verifica valores ausentes em todo o DataFrame
print()
#print(df.isna())

# Verifica valores ausentes em uma coluna específica
print(df['jogador'].isna())