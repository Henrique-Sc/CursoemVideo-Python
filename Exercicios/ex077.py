from time import sleep

lanches = ('coxinha', 'risole', 'esfirra de carne', 'esfirra de frango', 'esfirra de calabresa',
           'bolinho de queijo', 'pizza', 'hamburguer', 'lasanha', 'pastel')


print('-=' * 10 + '=-' * 10)
print('-=' * 5, 'Contagem de vogais', '=-' * 5)
print('-=' * 10 + '=-' * 10)
print('')
for comida in lanches:
    print(f'Na palvra "\033[4m{comida}\033[m" temos: ', end='')
    for letra in comida:
        if letra.lower() in 'aeiou':
            sleep(0.3)
            print(letra, end=' ', flush=True)
    sleep(0.5)
    print('\n')
print('', end='')
