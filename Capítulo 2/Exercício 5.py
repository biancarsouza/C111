numero = int(input("Entre com um número inteiro entre 1000 e 9999: "))

while numero < 1000 or numero > 9999:
    numero = int(input("Número inválido. Entre com um número inteiro entre 1000 e 9999: "))

numero = str(numero)

print(numero[3])
print(numero[2])
print(numero[1])
print(numero[0])