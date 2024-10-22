import pandas as pd
import sys

df1 = pd.DataFrame({
    "nome":  ["Waldir", "Kaio", 
              "Diego", "Biu", 
              "Biu", "Diquinho"], 
    "salario": [12000, 9000, 
                5000, 3200, 
                1250, 700], 
    "idade": [44, 60, 
              50, 32, 
              12, 77]})

df2 = pd.DataFrame({
    "nome":  ["Brioco", "Buiú", 
              "Diego", "Biu", 
              "Zé", "Diquinho"], 
    "time": ["Santos", "Palmeiras", 
             "Ceará", "Vasco", 
             "Porto", "Messejana"]})

# o join combina os data-frames usando índices, no lugar de colunas-chave
df1=df1.set_index("nome")
df2=df2.set_index("nome")

# os sufixos são usados para o caso de colunas com o mesmo nome
# how é o tipo do join (padrão é left)
resultado_join = df1.join(df2, lsuffix='_left', rsuffix='_right', how="inner")

print(resultado_join)