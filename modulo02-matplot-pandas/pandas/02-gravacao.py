import pandas as pd

df = pd.DataFrame({"time": ["ceará", "fortaleza"],
                   "jogador": ["Sérgio Alves", "Clodoaldo"],
                   "estádio": ["Castelão", "PV"],
                   "idade" : [59, 63]})

print(df)

# index = False é para não gravar a coluna que enumera a linha
df.to_csv("exemplo_gravacao.csv", index = False)