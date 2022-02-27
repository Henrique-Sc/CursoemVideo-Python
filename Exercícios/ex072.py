numtxt = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
          'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

cores = dict(reset='\033[m',
             red='\033[31m',
             blue='\033[34m',
             negrito='\033[1m',
             neg_ita='\033[1;3m'
             )

while True:
    num = int(input('Digite um número entre 0 e 20: ').strip())
    while True:
        if 0 <= num <= 20:
            break
        num = int(input('Valor inválido! Digite um número entre 0 e 20: '))

    print(f'\n{cores["negrito"]}O número {num} por extenso é {cores["neg_ita"]}{numtxt[num]}{cores["reset"]}.')

    esc = input('\nQuer continuar? (Sim / Não) ').strip().upper()[0]

    while True:
        if esc not in 'SN':
            print('')
            esc = input(f'{cores["red"]}Valores incorretos! Digite novamente (Sim / Não): {cores["reset"]}').strip().upper()[0]
        else:
            break
    print('')

    if esc == 'N':
        break

print('--- Fim da execução ---')
