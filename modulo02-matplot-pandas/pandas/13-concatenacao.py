import pandas as pd

df1 = pd.DataFrame({'coluna1': [1, 2, 3]})
df2 = pd.DataFrame({'coluna1': [4, 5, 6]})

# Concatenação vertical
result_vert = pd.concat([df1, df2])
print(result_vert)

# Concatenação horizontal
result_hor = pd.concat([df1, df2], axis=1)
print(result_hor)