print('\033[31m-=\033[m' * 5, '\033[37mProgressão aritimética\033[m', '\033[31m=-\033[m' * 5)
pt = int(input('\nPrimeiro termo da PA: '))
razao = int(input('Razão: '))
print('')
c = 0
while c != 10:
    print(pt + (razao * c), end=' → ')
    c += 1
print('...')
