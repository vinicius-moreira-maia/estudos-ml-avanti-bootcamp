import pandas as pd
from sklearn.model_selection import train_test_split

# pip install scikit-learn

'''
 - Scikit-learn é uma lib para Machine Learning.
 
 - Contém vários algoritmos supervisionados e não-supervisionados.
 
 - Também contém funções de pré-processamento e de avaliação de modelos.
'''


data = {    
'features': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],    
'target': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

# Divisão dos dados em conjuntos de treinamento e teste

# features são as características do conjunto de dados
# variáveis preditoras e independentes
# x são características
X = df['features'] # colunas

# target são os rótulos, é o que está tentando ser previsto
# variáveis dependentes
# target é a variável alvo!
y = df['target'] # dados

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2, # 20 % do total serão os dados de teste, 80% serão o conjunto de treinamento
    random_state=42 # definindo uma semente para aleatoriedade desta divisão de conjuntos
)

# na esquerda é a posição no data frame
# na direita é ou o dado (Y / target)
# ou a coluna (x / features)
print("Conjunto de treinamento (X):\n", X_train)
print("Conjunto de teste (X):\n", X_test)
print("Conjunto de treinamento (y):\n", y_train)
print("Conjunto de teste (y):\n", y_test)