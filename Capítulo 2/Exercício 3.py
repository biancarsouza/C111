letra = input("Digite uma de acordo com o seu sexo (M para homem e F para mulher): ")

while letra != "M" and letra != "F":
    letra = input("Caractere inválido. Digite M para homem e F para mulher: ")

if letra == "M":
    print("Você é um homem.")
else:
    print("Você é uma mulher.")