def leiaInt(txt=''):
    a = input(txt)
    if a.strip().isnumeric():
        return int(a)


n = leiaInt('Digite um número: ')
print(type(n))
