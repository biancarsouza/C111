op = int(input("Digite 1 se quiser adicionar uma pessoa a lista ou 0 se quiser mostrar os dados finais: "))

while op != 0 and op != 1:
    op = int(input("Digite 1 se quiser adicionar uma pessoa a lista ou 0 se quiser mostrar os dados finais: "))

dados = {}
conjunto = []

while op == 1:
    dados['nome'] = input('Entre com o nome da pessoa: ')
    dados['idade'] = int(input('Entre com a idade da pessoa: '))
    dados['sexo'] = input('Entre com o sexo da pessoa (F para mulher e M para homem): ')

    while dados['sexo'] != 'F' and dados['sexo'] != 'M':
        dados['sexo'] = input('Entre com o sexo da pessoa (F para mulher e M para homem): ')

    conjunto.append(dados.copy())

    op = int(input("\nDigite 1 se quiser adicionar uma pessoa a lista ou 0 se quiser mostrar os dados finais: "))

    while op != 0 and op != 1:
        op = int(input("\nDigite 1 se quiser adicionar uma pessoa a lista ou 0 se quiser mostrar os dados finais: "))

print("Média de idade:", sum([pessoa['idade'] for pessoa in conjunto]) / len(conjunto))
print("Mulheres com menos de 20 anos:", len([pessoa for pessoa in conjunto if pessoa['sexo'] == 'F' and pessoa['idade'] < 20]))