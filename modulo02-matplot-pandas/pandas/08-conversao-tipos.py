import pandas as pd
import sys

df = pd.DataFrame({"nome": ["Waldir", "Kaio", "Diego"], "salario": [12000, 9000, 55000]})

# info são os metadados
df.info()
print()

# conversão
df["salario"] = df["salario"].astype(float)
df.info()

# describe é um resumo estatístico
# print(df.describe())
# print()