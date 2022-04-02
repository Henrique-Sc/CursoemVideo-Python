from datetime import datetime

anoAtual = datetime.now().year


def voto(nascimento):
    idade = anoAtual - nascimento

    if idade < 16 or idade > 60:
        result = 'VOTO NEGADO'
    elif 16 <= idade < 18:
        result = 'VOTO OPCIONAL'
    else:
        result = 'VOTO OBRIGATÓRIO'

    return f'Com {idade} anos: {result}'


print('-' * 30)
nasc = int(input(f'Ano de nascimento (aaaa): '))
print(voto(nasc))
