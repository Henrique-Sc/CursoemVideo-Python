IRed = '\033[38;5;9m'
reset = '\033[m'

txtKeyboardError = f'{IRed}Erro! Você preferiu não digitar esse número.{reset}'


def leiaInt(txt):
    while True:
        try:
            a = int(input(txt).strip())
        except KeyboardInterrupt:
            print(txtKeyboardError)
            a = 0
            return a
        except:
            print(f'{IRed}Erro! Digite um número inteiro válido.{reset}')
            continue
        else:
            return a


def leiaFloat(txt):
    while True:
        try:
            a = float(input(txt).strip())
        except KeyboardInterrupt:
            print(txtKeyboardError)
            a = 0
            return a
        except:
            print(f'{IRed}Erro! Digite um número decimal válido.{reset}')
            continue
        else:
            return a
