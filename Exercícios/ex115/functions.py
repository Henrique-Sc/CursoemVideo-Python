cores = [
    '\033[m',    # 0 - Sem cor
    '\033[31m',  # 1 - Vermelho
    '\033[32m',  # 2 - Verde
    '\033[33m',  # 3 - Amarelo
    '\033[34m',  # 4 - Azul
    '\033[35m',  # 5 - Lilás
    '\033[36m',  # 6 - Ciano
    '\033[37m',  # 7 - Cinza
]


def title(txt, simb='=', corTitle=0, corSimb=0):
    simb = simb[0]
    tmn = len(txt) + 4

    print(f'{cores[corSimb]}{simb}{cores[0]}' * tmn)
    print(f'  {cores[corTitle]}{txt}{cores[0]}')
    print(f'{cores[corSimb]}{simb}{cores[0]}' * tmn)


def menu():
    while True:
        try:
            esc = int(input('''
OPÇÕES:
    1 - cadastrar
    2 - Lista dos cadastros
    
O que deseja fazer? '''))

        except:
            print()
            title('Erro! Digite as opções corretamente.', corSimb=1, corTitle=1)
            # print(f'\n{cores[1]}Erro! Digite as opções corretamente.{cores[0]}')

        else:
            if str(esc) not in '12':
                print()
                title('Erro! Digite as opções corretamente.', corSimb=1, corTitle=1)
