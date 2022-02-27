print('\033[31m-=\033[m' * 14)
print(f"\033[34m{'Progressão aritimética':^28}\033[m")
print('\033[31m-=\033[m\033[m' * 14)

print('\n-=-= Primeiros termos de uma PA -=-=\n')
pt = int(input('\nPrimeiro termo: '))
razao = int(input('Razão: '))
print('')
for c in range(0, 10):
    print(pt + (razao * c), end=' → ')
print('...')
