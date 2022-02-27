print('\033[37m-=\033[m' * 5, '\033[31mProgressão aritimética\033[m', '\033[37m=-\033[m' * 5)

pt = int(input('\nPrimeiro termo da PA: '))
razao = int(input('Razão: '))
print('')

c = 0
total = 10
mais = 1
while mais != 0:
    while c != total:
        print(pt + (c * razao), end=' → ')
        c += 1
    print('...')
    mais = int(input('\nQuantos termos você quer ver a mais? '))
    total += mais
print(f'''\n\033[31m{'-==-' * 9}\033[m

Fim do programa!
Foram analizados {c} termos no total''')