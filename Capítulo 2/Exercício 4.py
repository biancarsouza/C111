kms = float(input("Digite a quantidade de quilômetros: "))

if kms <= 200:
    preco = 0.5 * kms
else:
    preco = 0.45 * kms

print("Preço da passagem: R$", preco)