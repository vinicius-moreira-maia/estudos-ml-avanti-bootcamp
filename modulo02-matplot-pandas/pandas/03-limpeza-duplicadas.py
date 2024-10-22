import pandas as pd

# limpeza e pré-processamento

df = pd.DataFrame({"time": ["ceará", "fortalEza"],
                   "jogador": ["Sérgio Alves", "clodoaldo"],
                   "estádio": ["Castelão", "P.V"],
                   "idade" : [59, 63],
                   "tecnico" : ["Felipão", "Felipão"]})

# verificando duplicação de linhas em todo o DF
# retorna uma série booleana
#print(df.duplicated())

# verificando duplicadas em uma coluna
#print(df["tecnico"].duplicated())

# limpeza e pré-processamento
df = pd.DataFrame({"time": ["ceará", "fortaleza", "flamengo", "ceará", "mirassol","ceará","bahia" ,"ceará" "fortaleza", "flamengo", "real madrid"]})

print(df)
print()
print(df.duplicated())

# removendo duplicadas

# mantendo a 1ª ocorrência
print()
df2 = df.drop_duplicates()
#print()
#print(df2)

# mantendo a última ocorrência
print()
df3 = df.drop_duplicates(keep='last')
print(df3)

