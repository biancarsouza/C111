import numpy as np

dataset = np.loadtxt('./Capítulo 4/space.csv', delimiter = ';', dtype = str, encoding = 'utf-8')

cost = dataset[1:, 6].astype(float)
custos = cost[cost > 0]

print('Média de gastos de uma missão especial: US$', round(custos.sum() / custos.size, 2)) 