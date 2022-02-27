print('--- Digite uma expressão matemática ---')

print('\nExemplo: (a + b) * c')
exp = list(input('Digite aqui: ').strip())
parenteses1 = int()
parenteses2 = int()
for c in exp:
    if c == '(':
        parenteses1 += 1
    elif c == ')':
        parenteses2 += 1
if parenteses1 == parenteses2:
    print('\nExpressão válida!')
else:
    print('\nExpressão inválida!')
