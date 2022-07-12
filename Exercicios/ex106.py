from time import sleep

cores = ('\033[m',          # 0 - sem cor
         '\033[38;5;9m',    # 1 - vermelho
         '\033[38;5;10m',   # 2 - verde
         '\033[38;5;11m',   # 3 - amarelo
         '\033[38;5;12m',   # 4 - azul
         '\033[38;5;13m',   # 5 - magenta
         '\033[38;5;14m')   # 6 - ciano


def title(txt, cor=0):
    tmn = len(txt) + 4
    print(cores[cor], end='')
    print('-' * tmn)
    print(f'  {txt}')
    print('-' * tmn)
    print(cores[0])


def ajuda(comando):
    help(comando)


while True:
    title('SISTEMA DE AJUDA PyHelp', cor=4)
    sleep(1)

    print(f'\033[3m~Digite fim para parar \033[m')
    func = str(input(f'{cores[1]}Função ou biblioteca > {cores[0]}')).lower()

    print()  # Print vazio para quebrar linha

    if func == 'fim':
        break
    else:
        title(f'Carregando manual do comando "{func}"', cor=4)
        sleep(1)
        ajuda(func)
        sleep(1)

title('ATÉ LOGO!', cor=6)
