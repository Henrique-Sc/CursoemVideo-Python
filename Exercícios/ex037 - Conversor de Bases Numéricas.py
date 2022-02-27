num = int(input('Digite um número qualquer: '))
conversor = int(input(f"""\nAgora escolha o método de conversão:
\033[33m1 - para binário\033[m
\033[34m2 - para octal\033[m
\033[31m3 - para hexadecimal\033[m

Digite aqui o método escolhido: """))

if conversor == 1:
    print(f'\nO valor {num}, convertido para binário é {bin(num)[2:]}')
elif conversor == 2:
    print(f'\nO valor {num}, convertido para octal é {oct(num)[2:]}')
elif conversor == 3:
    print(f'\nO valor {num}, convertido para hexadecimal é {hex(num)[2:]}')
else:
    print(('\n\033[31mERRO! Opção inválida'))
    print('Tente novamente.')
