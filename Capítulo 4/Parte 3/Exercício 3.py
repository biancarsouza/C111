import numpy as np

dataset = np.loadtxt('./Capítulo 4/space.csv', delimiter = ';', dtype = str, encoding = 'utf-8')

location = dataset[1:, 2]

localizadoNosEUA = np.char.find(location, 'USA') > 0
soma = localizadoNosEUA[localizadoNosEUA == True].sum()

print('Missões espaciais realizadas pelos Estados Unidos:', soma)