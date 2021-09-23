aluno = dict()
aluno['nome'] = str(input('Nome do aluno: '))
aluno['média'] = float(input('Média do aluno: '))
if aluno['média'] >= 5:
    aluno['situação'] = 'APROVADO'
else:
    aluno['situação'] = 'REPROVADO'
print('=-' *30)
print(f'O aluno {aluno["nome"]} obteve a média de {aluno["média"]}.\n'
    f'E está {aluno["situação"]}.')
