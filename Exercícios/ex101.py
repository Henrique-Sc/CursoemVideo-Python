from datetime import datetime

anoAtual = datetime.now().year


def voto(nascimento):
    idade = anoAtual - nascimento
    print(idade)


print('-' * 30)
nasc = int(input(f'Ano de nascimento (aaaa): '))
