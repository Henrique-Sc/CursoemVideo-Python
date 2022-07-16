from time import sleep

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


def linha(tmh=30, simb='=', colorSimb=0):
    print(f'{cores[colorSimb]}{simb}{cores[0]}' * tmh)


def title(txt, simb='=', colorTitle=0, colorSimb=0, tmn=30, line=True):
    simb = simb[0]

    if line:
        linha(tmn, simb, colorSimb)
    print(f'{cores[colorTitle]}{txt:^30}{cores[0]}')
    if line:
        linha(tmn, simb, colorSimb)


def erroMenu():
    print()
    title('Erro! Digite as opções corretamente.', colorSimb=1, colorTitle=1, line=False)
    print()
    sleep(1)


def menu():
    while True:
        title('CADASTRO DE USUÁRIO', colorSimb=3)

        print(f' {cores[4]}1{cores[0]} - Cadastrar')
        print(f' {cores[4]}2{cores[0]} - Lista dos cadastros')
        print(f' {cores[4]}3{cores[0]} - Sair do programa')
        linha(colorSimb=3)
        sleep(1)

        # Tentar converter para inteiro
        try:
            esc = int(input('O que deseja fazer? '))

        except:
            erroMenu()

        else:
            if str(esc) not in '123':
                erroMenu()
            else:
                sleep(1)
                return esc


def opcoes(esc):
    # Verificar se o arquivo .txt está criado
    try:
        with open('cadastros.txt', 'r') as arquivo:
            arquivo.read()

    except FileNotFoundError:
        with open('cadastros.txt', 'w+') as arquivo:
            pass

    finally:
        # Cadastrar
        if esc == 1:
            cadastrar()
        # Listar
        elif esc == 2:
            listar()
        # Sair
        elif esc == 3:
            sair()
        sleep(1)


def leiaNome(txt):
    while True:
        nome = str(input(txt)).strip().title()[:18].rstrip()
        if nome == '' or len(nome) < 3:
            print()
            title('Erro! Digite o seu nome corretamente.', colorSimb=1, colorTitle=1, line=False)
            print()
            sleep(1)
        else:
            break
    return nome


def erroIdade():
    print()
    title('Erro! Digite a sua idade corretamente.', colorSimb=1, colorTitle=1, line=False)
    print()
    sleep(1)


def leiaIdade(txt):
    while True:
        try:
            idade = int(input(txt).strip()[:3])
        except:
            erroIdade()
        else:
            if idade < 0:
                erroIdade()
            else:
                return idade


def cadastrar():
    linha(colorSimb=3)
    nome = leiaNome('Digite o seu nome: ')
    idade = leiaIdade('Digite a sua idade: ')
    with open('cadastros.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{nome};{idade}\n')
    sleep(1)
    print(f'\nCadastro de {nome} realizado com sucesso!')
    sleep(1)


def listar():
    title('PESSOAS CADASTRADAS', colorSimb=3)

    with open('cadastros.txt', 'r', encoding='utf-8') as arquivo:
        cadastros = arquivo.readlines()

    if len(cadastros) == 0:
        print(f'{cores[1]}{"Nenhum cadastro encontrado!":^30}{cores[0]}')
    else:
        for cadastro in cadastros:
            cadastro = cadastro.replace('\n', '').split(';')
            print(f' {cadastro[0]:<19} {cadastro[1]}', 'ano' if int(cadastro[1]) <= 1 else 'anos')

    sleep(1)


def sair():
    title('Saindo do programa...', colorSimb=3)
    sleep(1)
    print(f'{cores[4]}{"-> Volte sempre! <-":^30}{cores[0]}')
