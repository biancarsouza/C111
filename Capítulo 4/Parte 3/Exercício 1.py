import numpy as np

dataset = np.loadtxt('./Capítulo 4/space.csv', delimiter = ';', dtype = str, encoding = 'utf-8')

statusMission = dataset[1:, 7]

sucesso = np.char.startswith(statusMission, 'Success') > 0
soma = sucesso[sucesso == True].sum()
porcentagem = (soma * 100) / statusMission.size

print('Porcentagem de missões que deram certo:', round(porcentagem, 2))