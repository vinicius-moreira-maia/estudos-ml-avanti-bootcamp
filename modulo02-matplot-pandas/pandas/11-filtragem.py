import pandas as pd
import sys

df = pd.DataFrame({"nome": ["Waldir", "Kaio", "Diego", "Biu", "Biu", "Diquinho"], "salario": [12000, 9000, 5000, 3200, 1250, 700], "idade": [44, 60, 50, 32, 12, 77]})

# query
# seleciona toda a linha
print(df.query('salario < 1500'))

print()

# loc
# seleciona apenas o nome de quem ganha mais que 3500
print(df.loc[df['salario'] > 3500, ['nome']])

# & (and) - | (or)
# seleciona linhas
print()
filtro = (df['idade'] > 40) & (df['salario'] % 2 == 0)
print(df[filtro])