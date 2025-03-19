import numpy as np

dataset = np.loadtxt('./paises.csv', delimiter = ';', dtype = str, encoding = 'utf-8')

#Q1 - Slicing para mostrar apenas o país, região, população e área de cada país do dataset
sliced = dataset[1:, :4]
print(sliced)

#Q2 - Contar e mostrar quais as diferentes regiões do planeta segundo o dataset
regions = np.unique(dataset[1:, 1])
print("\nRegiões do mundo:\n", regions)
print("\nQuantidade de regiões:", len(regions))

#Q3 - Mostrar a taxa média de alfabetização do planeta
literacy = dataset[1:, 9].astype(float)
print("\nTaxa média mundial de alfabetização:", round(np.mean(literacy), 2))

#Q4 - Contar quantos países são da América do Norte
count_regions = sliced[1: , 1]
count_regions = count_regions[np.char.find(count_regions, "NORTHERN AMERICA")>=0]
print("\nQuantidade de países que são da América do Norte:", len(count_regions))

#Q5 - Mostrar qual país da América do Sul e Caribe possui a maior renda per capita
countries = sliced[:, 0]
regions = sliced[:, 1]
gdp = dataset[1:, 8].astype(float)
cond = np.char.find(regions, "LATIN AMER. & CARIB")>=0
best_country = np.argmax(gdp[cond])
countries = countries[cond]
print(f"\nPaís da América do Sul e Caribe com a maior renda per capita: {countries[best_country]}")