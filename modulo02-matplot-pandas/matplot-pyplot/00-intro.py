import matplotlib.pyplot as plt
import numpy as np

# pyplot é um submódulo do matplotlib que facilita a criação de gráficos
# pyplot é uma interface de mais alto nível que o matplot em si, portanto mais amigável
# é criado usando o matplotlib
# interface similar ao matlab

'''
partes de uma figura:
    título
    eixos
    textos
    escala

no matplot uma figura pode ter um ou mais eixos
'''

# o método subplots() é a maneira mais simples de criar gráficos com eixos
# o método retorna um objeto (classe Figure) que representa a figura e um objeto que representa os eixos (classe Axes)
# é no objeto Axes que se define os dados que serão utilizados na plotagem
#fig, ax = plt.subplots() 

# as duas listas são os dados dos eixos x e y
# plot é o método para exibir um gráfico de linhas
#ax.plot([1, 2, 3, 4], [1, 4, 2, 3]) 

# exibindo o gráfico
#plt.show()

#----------------------------------------------------------------

# seed é usado só para controlar a aleatoriedade dos númros aleatórios
np.random.seed(19680801)

# arange cria uma sequencia de numeros, em um array (0 a 49, no caso)
data = {    
 'a': np.arange(50),    
 'c': np.random.randint(0, 50, 50), # 50 números aleatórios de 0 a 50   
 'd': np.random.randn(50) # rand gera de 0 a 1 (floats)
}

data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

# figsize é o tamanho em polegadas
fig, ax = plt.subplots(figsize=(5, 2.7))

# aqui é só para alguns ajustes de exibição automáticos, para evitar sobreposições, etc
fig.set_constrained_layout(True) # Define o layout restrito

# scatter é o gráfico de "pontinhos"
# a e b são os eixos x e y
# c é cores dos pontos
# s é o tamanho dos pontos
# quando envio dados pelo data, posso referenciar as chaves do dicionário nos parâmetros (ou as colunas de um dataframe)
ax.scatter('a', 'b', c='c', s='d', data=data)

ax.set_xlabel('valores de a') # nome do eixo x
ax.set_ylabel('valores de b') # nome do eixo y

ax.set_title('Gráfico de Dispersão, papai')

plt.show()