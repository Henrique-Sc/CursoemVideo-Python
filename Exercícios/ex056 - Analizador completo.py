from color import blue, red

media = 0
nome_hmv = str
mulheres_m20 = 0
idade_hmv = 0

for c in range(1, 5):
    # encontrando os dados dos indivíduos

    print('-=' * 6, f'{red(f"{c}ª PESSOA")}', '-=' * 6)

    nome = str(input('\nDigite o seu nome: ')).strip().title()
    idade = int(input('Sua idade: ').strip())
    sexo = str(input('Digite o seu sexo (F / M): ')).strip().upper()
    print('')

    # analizando os dados
    # nome do homem mais velho

    if sexo == 'M' and c == 1:
        idade_hmv = idade
        nome_hmv = nome
    elif sexo == 'M':
        if idade > idade_hmv:
            nome_hmv = nome
            idade_hmv = idade

    # média de idade do grupo
    media += idade / 4

    # quantidades de mulheres que tem menos de 20 anos
    if sexo == 'F' and idade < 20:
        mulheres_m20 = mulheres_m20 + 1
if nome_hmv == '':
    nome_hmv = 'Não tem'

# resultado
print(f'''{blue(f'{" ANÁLISE DOS DADOS ":-^34}')}
Média de idade do grupo: {media:.1f} anos

Nome do homem mais velho e a sua idade: {nome_hmv}, {idade_hmv} anos

Quantidades de mulheres com menos de vinte anos: {mulheres_m20}
{blue('-=') * 17}''')
