times = ['Real Madrid', 'São Paulo', 'Barcelona', 'Auckland City', 'Al Hilal']

print("Três primeiros colocados:")
print(times[:3])

print("\nÚltimos dois colocados:")
print(times[-2:])

print("\nLista em ordem alfabética:")
listaAlfabetica = sorted(times)
print(listaAlfabetica)

print("\nOnde se encontra o Barcelona na lista original:", times.index('Barcelona'))
print("Onde se encontra o Barcelona na lista em ordem alfabética:", listaAlfabetica.index('Barcelona'))