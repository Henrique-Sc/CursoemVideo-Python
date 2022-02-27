brasil = list()
estado = dict()

for c in range(3):
    estado['uf'] = input('Unidade Federativa: ').strip().title()
    estado['sigla'] = input('Sigla do Estado: ').upper()
    brasil.append(estado.copy())
    print()

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
