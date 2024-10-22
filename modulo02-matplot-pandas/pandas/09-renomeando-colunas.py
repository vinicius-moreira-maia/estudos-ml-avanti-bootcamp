import pandas as pd
import sys

df = pd.DataFrame({"nome": ["Waldir", "Kaio", "Diego"], "salario": [12000, 9000, 55000]})

print(df)

# Renomeando várias colunas
df.rename(columns = {'nome': 'nome_do_caba',         
                     'salario': 'salario_do_caba'},     
          inplace = True)

print()
print(df)