import pandas as pd

# limpeza e pré-processamento

# limpeza e pré-processamento
df = pd.DataFrame({"time": ["ceará", "fortaleza", "flamengo", "ceará", "mirassol","ceará","bahia" ,"ceará" , "fortaleza", "flamengo", "real madrid"]})

arr = []
for i,time in enumerate(df["time"]):
    arr.append(f"Neymar")

# adicionando nova coluna
df["jogador"] = arr

print(df)
print()

# OBS: esses métodos geram novos data frames, para alterar o df original é necessário fornecer o parâmetro 'inplace = True'

# remove os dados duplicados sem deixar nenhum
print(df.drop_duplicates(keep=False))

print()

# removendo duplicados com base em colunas
print(df.drop_duplicates(subset=['time']))

print()
# todos os jogadores são iguais, portanto ele deixa apenas uma linha aqui
print(df.drop_duplicates(subset=['jogador']))