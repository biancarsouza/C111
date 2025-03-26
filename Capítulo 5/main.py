import pandas as pd
import numpy as np

# Parte 1

# 1 - Criar séries
labels1 = ['Java', 'C', 'Python']
dados1 = [16.21, 16.04, 9.85]

seriesAno1 = pd.Series(index = labels1, data = dados1)

labels2 = ['C', 'Python', 'Java']
dados2 = [16.21, 12.12, 11.68]

seriesAno2 = pd.Series(index = labels2, data = dados2)

print(seriesAno1)
print(seriesAno2)

# 2 - Porcentagem total que as linguagens representam juntas no mercado em cada um dos anos
print("\nPorcentagem total do ano 1:", seriesAno1.sum())
print("Porcentagem total do ano 2:", seriesAno2.sum())

# 3 - Crescimento/declínio de cada linguagem do primeiro ano para o segundo ano
labels3 = ['Java', 'C', 'Python']
dados3 = [seriesAno2['Java'] - seriesAno1['Java'], seriesAno2['C'] - seriesAno1['C'], seriesAno2['Python'] - seriesAno1['Python']]

seriesCreDec = pd.Series(index = labels3, data = dados3)

print("\nCrescimento/declínio de Java:", round(seriesCreDec['Java'], 3))
print("Crescimento/declínio de C:", round(seriesCreDec['C'], 3))
print("Crescimento/declínio de Python:", round(seriesCreDec['Python'], 3))

# 4 - Mostrar apenas os dados das linguagens que tiveram crescimento
print("\nDados das linguagens que tiveram crescimento (nome e quanto de crescimento):")
print(seriesCreDec[seriesCreDec > 0])

# 5 - Qual seria a linguagem mais popular caso as porcentagens de crescimento/declínio se mantivessem nos próximos dois anos
labels4 = ['Java', 'C', 'Python']
dados4 = [seriesAno2['Java'] + 2 * seriesCreDec['Java'], seriesAno2['C'] + 2 * seriesCreDec['C'], seriesAno2['Python'] + 2 * seriesCreDec['Python']]

seriesCreDecEmDoisAnos = pd.Series(index = labels4, data = dados4)

print("\nLinguagem mais popular nos próximos dois anos:")
print(seriesCreDecEmDoisAnos.nlargest(1))

# Parte 2

# 6 - Usando o dataframe abaixo, mostrar a média dos elementos da coluna X que são menores que 30
df = pd.DataFrame(
    index = ['A', 'B', 'C', 'D', 'E'],
    columns = ['W', 'X', 'Y', 'Z'],
    data = np.random.randint(1, 50 , [5, 4])
)

print("\nDataframe a ser utilizado nas próximas questões:")
print(df)

print("\nMédia dos elementos da coluna X que são menores que 30:", round(df[df['X'] < 30]['X'].mean(), 3))

# 7 - Média dos elementos do dataframe da linha D usando loc() e a soma dos elementos da linha E usando iloc()
print("\nMédia dos elementos da linha D:", round(df.loc['D'].mean(), 3))
print("Soma dos elementos da linha E:", df.iloc[4].sum())

# 8 - Slicing para mostrar apenas as linhas A, C e E e as colunas X e Y, depois mostrar a soma de cada linha e de cada coluna
dfSliced = df.loc[['A', 'C', 'E'], ['X', 'Y']]

print("\nDataframe pós slicing (linhas A, C e E e colunas X e Y):")
print(dfSliced)

print("\nSoma de cada linha:")
print(dfSliced.sum(axis = 1))

print("\nSoma de cada coluna:")
print(dfSliced.sum(axis = 0))