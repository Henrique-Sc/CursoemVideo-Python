from datetime import date
ano = date.today().year
ano_nascimento = int(input('Digite o ano em que você nasceu: ').strip())
idade = ano - ano_nascimento
if idade < 18:
    print(f'Você tem {idade} anos, e deve fazer o seu alistamento daqui a {18 - idade} anos!')
elif idade == 18:
    print(f'Você já tem {idade} anos, e deve fazer o seu alistamento!')
elif idade > 18:
    if idade - 18 == 1:
        print(f'\nVocê tem {idade} anos, e já passou do tempo de você fazer o seu alistamento!')
        print(f'Já atrasou {idade - 18} ano!')
    else:
        print(f'\nVocê tem {idade} anos, e já passou do tempo de você fazer o seu alistamento!')
        print(f'Já atrasou {idade - 18} anos!')
