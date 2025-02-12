dados = {}

dados['nome'] = input("Digite o nome do aluno: ")
dados['media'] = float(input("Digite a média do aluno: "))

if dados['media'] >= 50:
    dados['situacao'] = 'AP'
else:
    dados['situacao'] = 'RP'

print("\nNome:", dados['nome'])
print("Média:", dados['media'])
print("Situação:", dados['situacao'])

print("\n", dados)