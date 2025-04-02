import numpy as np
import pandas as pd

dfPaises = pd.read_csv('./Capítulo 5/paises.csv', delimiter = ';')

# 1 - Mostrar quais e quantos países são da Oceania usando o str.contains
oceania = dfPaises[dfPaises['Region'].str.contains('Oceania')]
print("Países da Oceania:")
print(oceania)
print("Quantidade de países da Oceania:", oceania.shape[0])

# 2 - Mostrar o nome e região do país com a maior população
maiorPopulacao = dfPaises[dfPaises['Population'] == dfPaises['Population'].max()]
print("\nNome do país mais populoso e qual a sua região:")
print(maiorPopulacao[['Country', 'Region']])

# 3 - Agrupar os países por região e mostrar a média de literacy de cada
mediaLiteracy = dfPaises.groupby('Region')['Literacy'].mean()
print("\nMédia de literacy por região:")
print(mediaLiteracy)

# 4 - Mostrar o nome dos países que não possuem coastline e guardar em um arquivo noCoast.csv
noCoast = dfPaises[dfPaises['Coastline'] == 0]
print("\nPaíses sem litoral:")
print(noCoast[['Country']])
noCoast[['Country']].to_csv('./Capítulo 5/noCoast.csv', index = False)

# 5 - Se a deathrate for menor do que 9 retornar 'Balanced' e 'Urgent' caso contrário. Criar um campo 'Humanitarian help' que receba estes valores para cada país. Depois mostrar o dataset para verificar a inserção da coluna.
dfPaises['Humanitarian help'] = np.where(dfPaises['Deathrate'] < 9, 'Balanced', 'Urgent')
print("\nDataset com a coluna 'Humanitarian help':")
print(dfPaises[['Country', 'Deathrate', 'Humanitarian help']])