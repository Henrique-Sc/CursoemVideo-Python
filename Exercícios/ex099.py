from time import sleep


def maior(*numeros):
    print('-=' * 17 + '-')
    print('Analisando', end='')
    for c in '...':
        sleep(0.3)
        print(c, end='')
    print(c for '...')

maior(1)
