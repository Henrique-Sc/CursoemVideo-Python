def notas(*n, sit=False):
    """
    -> Analise notas de diversos alunos
    :param n: nota do aluno (uma ou mais notas)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """

    dic = {
        'Total de notas': len(n),
        'Maior nota': max(n),
        'Menor nota': min(n),
        'Média': sum(n) / len(n)
    }
    if sit:
        media = dic['Média']
        if media < 5:
            s = 'RUIM'
        elif 5 <= media < 7:
            s = 'RAZOÁVEL'
        else:
            s = 'BOA'
        dic['Situação'] = s
    return dic


# Programa principal
resultado = notas(8, 7, 5, 9.85)
for i, d in enumerate(resultado.items()):
    if i >= 1 and d[0] != 'Situação':
        print(f'{d[0]}: {d[1]:.2f}')
    else:
        print(f'{d[0]}: {d[1]:}')
