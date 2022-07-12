print('\033[4;31mEscreva a frase sem acento.\033[m\n')
frase = str(input('Digite uma frase qualquer: ')).capitalize()
txt_formatado = ''.join((frase.lower().strip()).split())
if txt_formatado == f'{txt_formatado[::-1]}':
    print(f'\nA frase "{frase}" é um \033[34;4mPALÍNDROMO!\033[m')
else:
    print(f'\nA frase "{frase}" NÃO É UM \033[31;4mPALÍNDROMO!\033[m')
