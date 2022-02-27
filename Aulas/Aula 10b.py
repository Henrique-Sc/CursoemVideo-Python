#nome = str(input('Qual o seu nome? ')).title()
#if nome.split()[0] == 'Henrique':
    #print('\nQue nome lindo você tem! :3')
#else:
    #print('\nQue nome mais normal...')
#print(f'\nBom dia {nome.split()[0]}!')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print(f'A sua média foi {m:.1f}')
print('SUA NOTA FOI BOA! PARABÉNS!' if m >= 6.0 else 'ESTUDE MAIS!!')
