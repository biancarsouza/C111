import numpy as np

dataset = np.loadtxt('./Capítulo 4/space.csv', delimiter = ';', dtype = str, encoding = 'utf-8')

companyName = dataset[1:, 1]
detail = dataset[1:, 4]
cost = dataset[1:, 6].astype(float)

spacex = detail[companyName == "SpaceX"]
custo = cost[companyName == "SpaceX"]
max = np.argmax(custo)

print('Missão mais cara realizada pelas empresas "SpaceX":', spacex[max])