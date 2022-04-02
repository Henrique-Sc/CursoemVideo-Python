def notas(*n, sit=False):
    dic = {
        'Total de notas': len(n),
        'Maior nota': max(n),
        'Menor nota': min(n),
        'Média': sum(n) / len(n)
    }
    return dic


# Programa principal
resultado = notas(9.51, 10, 5.50, 4)
for k, v in resultado.items():
    if type(v) == float:
        print(f'{k}: {v:.2f}')
    else:
        print(f'{k}: {v}')
