b = 'DESAFIO 007'
print(f'{b:=^31}')
print('')
nome = str(input('Digite seu nome: '))
print('')
n1 = float(input('Nota da primeira prova: '))
n2 = float(input('Nota da segunda prova: '))
print(f'\n{nome}, a sua média foi {(n1 + n2)/2}')
