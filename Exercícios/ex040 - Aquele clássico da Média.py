from color import red, blue, yellow, black

print(f'{red("-=")}' * 12)
print(f'\033[33m{"VERIFICADOR DE MÉDIA":^24}')
print(f'{red("-=")}' * 12)

nome = str(input('\n\033[30mQual é o seu nome? ')).strip().title()

a = float(input(f'\nDigite a sua primeira nota: '))
b = float(input('Digite a sua segunda nota: '))
media = (a + b) / 2

print(f'\n\033[30m{nome}, com as notas {a} e {b}, você teve uma média de \033[4m{media}!\033[m')

if media < 5:
    print(f'{red("REPROVADO!")}')

elif media == 5 or 5 < media < 7:
    print(f'{yellow("RECUPERAÇÃO!")}')

elif media == 7 or media > 7:
    print(f'{blue("APROVADO!")}')
