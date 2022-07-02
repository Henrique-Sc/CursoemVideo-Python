IRed = '\033[38;5;9m'
reset = '\033[m'

txtKeyboardError = f'{IRed}Erro! Você preferiu não digitar esse número.{reset}'
txtError = f'{IRed}Erro! Digite um número inteiro válido.{reset}'


def leiaInt(txt):
    while True:
        try:
            a = int(input(txt))
        except KeyboardInterrupt:
            print(txtKeyboardError)
            a = 0
            return a
        except:
            print(txtError)
        else:
            return a


def leiaFloat(txt):
    while True:
        try:
            a = float(input(txt))
        except KeyboardInterrupt:
            print(txtKeyboardError)
            a = 0
            return a
        except:
            print(txtError)
        else:
            return a
