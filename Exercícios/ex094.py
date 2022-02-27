from time import sleep as s

r = '\033[m'
IR = '\033[38;5;9m'
IB = '\033[38;5;12m'

# Declarando as variáveis
pessoas = []
c = 0

# Laço para a inserção dos dados
while True:
    pessoas.append(
        {'nome': str(input('Seu nome: ')).strip().title(),
         'idade': int(input('Sua idade: ').strip()),
         'sexo': str(input(f'Sexo: [{IR}M{r}aculino / {IR}F{r}eminino / {IR}O{r}utros] ')).strip().upper()[0]}
    )

    while pessoas[c]['sexo'] not in 'MFO':
        pessoas[c]['sexo'] = str(input(f'Sexo: [{IR}M{r}aculino / {IR}F{r}eminino / {IR}O{r}utros] ')).strip().upper()[0]

    c += 1

    esc = str(input(f'\nDeseja continuar? [{IB}S{r}im / {IR}N{r}ão] ')).strip().upper()[0]
    if esc not in 'NS':
        print()
        while esc not in 'NS':
            esc = str(input(f'{IR}Valor incorreto!{r} Deseja continuar? [{IB}S{r}im / {IR}N{r}ão] ')).strip().upper()[0]
    print()
    if esc == 'N':
        break

# Declarando as variáveis
quant_pessoas = len(pessoas)
tot_idade = 0
mulheres = []

# Laços para análise dos dados
for p in pessoas:
    tot_idade += p['idade']
    if p['sexo'] == 'F':
        mulheres.append(p['nome'])
media_idade = tot_idade / quant_pessoas

# Exibição dos dados
s(0.5), print('==' * 20, '\n'), s(0.5)

print(f'- Número de pessoas cadastradas: {len(pessoas)}'), s(0.5)
print(f'- Média de idade do grupo: {media_idade:.2f}'), s(0.5)
print(f'- Nome das mulheres cadastradas: {mulheres}'), s(0.5)
print(f'- Pessoas com idade maior que a média do grupo: '), s(0.5)
for p in pessoas:
    if p['idade'] > media_idade:
        print(f'\t-> Nome: {p["nome"]}; idade: {p["idade"]}; sexo: {"sexo"} '), s(0.5)
print()
print('==' * 20), s(0.5)
