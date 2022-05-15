def voto(nascimento):
    from datetime import datetime

    anoAtual = datetime.now().year
    idade = anoAtual - nascimento

    if idade < 16:
        result = 'VOTO NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        result = 'VOTO OPCIONAL'
    else:
        result = 'VOTO OBRIGATÓRIO'

    return f'Com {idade} anos: {result}'


print('-' * 30)
nasc = int(input(f'Ano de nascimento (aaaa): '))
print(voto(nasc))
