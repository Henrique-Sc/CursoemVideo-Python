n1 = int(input('Digite um número: '))
n2 = int(input('Digite um segundo número: '))
n3 = int(input('Digite um terceiro número: '))
if n1 > n2:
    if n1 > n3:
        if n2 > n3:
            print(f'O maior número é o {n1} e o menor número é o {n3}')
        else:
            print(f'O maior número é o {n1} e o menor número é o {n2}')
if n2 > n1:
    if n2 > n3:
        if n1 > n3:
            print(f'O maior número é o {n2} e o menor número é o {n3}')
        else:
            print(f'O maior número é o {n2} e o menor número é o {n1}')
if n3 > n1:
    if n3 > n2:
        if n1 > n2:
            print(f'O maior número é o {n3} e o menor número é o {n2}')
        else:
            print(f'O maior número é o {n3} e o menor número é o {n1}')
