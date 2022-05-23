def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de diversos alunos.
    :param n: nota do alunos (uma ou mais notas)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: Retorna u  dicionário com a análise das notas do aluno e a situação (se sit for True)
    """

    dic = {
        'Total de notas': len(n),
        'Maior nota': max(n),
        'Menor nota': min(n),
        'Média': sum(n) / len(n)
    }

    # Se o parâmetro sit for True, o dicionário receberá a situação.
    if sit:
        if dic['Média'] >= 7:
            dic['Situação'] = 'BOA'
        elif dic['Média'] >= 5:
            dic['Situação'] = 'RAZOÁVEL'
        else:
            dic['Situação'] = 'RUIM'

    return dic


# Programa principal
resultado = notas(10, 4.58, 5, 8.5, sit=True)
print(resultado)
