import pandas as pd
import sys


df = pd.DataFrame({"nome": ["Waldir", "Kaio", "Diego"], "salario": [12000, 9000, 55000]})

print(df)
print()

# outliers são valores extremos ou discrepantes

# Opção 1: Remoção de outliers
# filtragem de linhas
df_sem_outliers = df[df['salario'] < 15000]

print(df_sem_outliers)

def verifica_outlier(salario):
    if salario > 15000:
        return 15000
    return salario

# Opção 2: Transformação
# df['novo_salario'] = df['salario'].apply(verifica_outlier)

# print()
# print(df)
#print()

# Opção 3: Substituição
# mediana, se o conjunto de dados for ímpar, é o elemento central, se for par ´a média dos dois elementos centrais
mediana_salario = df['salario'].median()
df['salario_correto'] = df['salario'].apply(    
    lambda x: mediana_salario if x > 15000 else x
)

print()
print(df)