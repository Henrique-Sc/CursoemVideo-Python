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
resultado = notas(10, 4.58, 5, 8.5, sit=True)
print(resultado)
