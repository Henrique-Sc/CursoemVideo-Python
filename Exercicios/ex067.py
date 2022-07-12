reset = '\033[m'
IYellow = '\033[38;5;11m'
IBlue = '\033[38;5;12m'
while True:
    n = int(input('Digite um número para ver a sua tabuada: ').strip())
    if n <= 0:
        break
    print('')
    print('-=' * 8)
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('-=' * 8)
    print('')
print(f'\nPrograma fechado com êxito! (ﾉ◕ヮ◕)ﾉ{IYellow}*:･ﾟ✧ {IBlue}Volte sempre {IYellow}✧ﾟ･: *{reset}ヽ(◕ヮ◕ヽ)')
