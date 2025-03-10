import numpy as np

dataset = np.loadtxt('./Capítulo 4/space.csv', delimiter = ';', dtype = str, encoding = 'utf-8')

companyName = dataset[1:, 1]

nomeDasEmpresas, qtdDeMissoes = np.unique(companyName, return_counts = True)

i = 0

for each in nomeDasEmpresas:
    print('Nome da empresa:', nomeDasEmpresas[i])
    print('Total de missões:', qtdDeMissoes[i], "\n")

    i += 1