pessoas = []

for pessoa in range(3):
    dados = {}
    dados['nome'] = input('Entre com o nome da pessoa: ')
    dados['peso'] = float(input('Entre com o peso da pessoa: '))

    pessoas.append(dados)

print("Nome da pessoa mais pesada:", max(pessoas, key=lambda x: x['peso'])['nome'])
print("Nome da pessoa mais leve:", min(pessoas, key=lambda x: x['peso'])['nome'])
