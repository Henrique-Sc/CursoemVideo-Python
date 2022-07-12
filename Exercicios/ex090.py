aluno = dict()
aluno['nome'] = str(input('Nome do aluno: ')).strip().title()
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['média'] < 5:
    aluno['situação'] = 'Reprovado'
elif aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Recuperação'

print()
print('=-=-=-=-=-=-=-=-=-=-=-=')
print()

for k, v in aluno.items():
    if type(v) == float:
        print(f'{k.title()}: {v:.2f}')
    else:
        print(f'{k.title()}: {v}')