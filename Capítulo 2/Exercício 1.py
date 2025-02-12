nome = input("Entre com o seu nome completo: ")

print("Nome apenas em letras maiúsculas:", nome.upper())
print("Nome apenas em letras minúsculas:", nome.lower())
print("Quantidade de letras:", len(nome) - nome.count(' '))

nome = nome.split()
nome[-1] = "do Inatel"
nome = " ".join(nome)

print("Nome alterado:", nome)