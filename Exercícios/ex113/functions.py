IRed = '\033[38;5;9m'
reset = '\033[m'


def leiaInt(txt):
    while True:
        try:
            a = int(input(txt))

        except KeyboardInterrupt:
            print(f'{IRed}Erro! Você interrompeu o programa.{reset}')

        except:
            print(f'{IRed}Erro! Digite um número inteiro válido.{reset}')

        else:
            return a
