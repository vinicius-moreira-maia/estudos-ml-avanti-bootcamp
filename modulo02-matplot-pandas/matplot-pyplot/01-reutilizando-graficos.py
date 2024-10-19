import matplotlib.pyplot as plt
import numpy as np

def my_plotter(ax, data1, data2, param_dict):  
    '''
    Recebe o objeto do tipo Axis (que guarda o objeto que representa o subgráfico), os dados do eixo x e do eixo y e uma lista de parâmetros opcionais, usados para formatações adicionais do gráfico (**kwargs - keyword arguments).
    '''
    
    # o retorno é da classe Line2D, esse objeto pode ser usado para alterações adicionais na linha do gráfico (estilo, etc)
    out = ax.plot(data1, data2, **param_dict)   
    
    return out

# gerando um array 2d com quatro linhas, de 100 elementos cada
# rands retorna números entre 0 e 1
# usando as 4 variáveis cada uma recebe um array
data1, data2, data3, data4 = np.random.randn(4, 100) 

# subplots gra uma grade de subgráficos
# 1 e 2 são número de linhas e número de colunas (isso diz rspeito à quantidade de subgráficos)
# ax1 e ax2 são os eixos de cada subgráfico, a partir deles é só enviar os dados para cada um, para ocorrer a plotagem
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))

# o x e a o aqui são marcadores nos vértices das linhas dos gráficos
my_plotter(ax1, data1, data2, {'marker': 'x'})
my_plotter(ax2, data3, data4, {'marker': 'o'})

plt.show()