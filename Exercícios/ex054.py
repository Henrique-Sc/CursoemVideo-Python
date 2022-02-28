from datetime import date
ano = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input(f'Insira o ano de nascimento da {c}ª pessoa: '))
    if ano - nasc >= 18:
        maior = maior + 1
    elif ano - nasc < 18:
        menor = menor + 1
print(f'\nQuantidades de pessoas que são maior de idade: {maior}')
print(f'E também, quantidades de pessoas que são menor de idade: {menor}')
