def leiaInt(txt=''):
    while True:
        num = input(txt)
        if num.strip().isnumeric():
            return int(num)
        else:
            print('\033[31mValor incorreto! Digite um número inteiro.\033[m')


# Programa principal
n = leiaInt('Digite um número: ')
print(f'O número digitado foi {n}')

