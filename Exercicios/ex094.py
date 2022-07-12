# Imports
from time import sleep

# Cores no terminal
r = '\033[m'
IR = '\033[38;5;9m'
IB = '\033[38;5;12m'

# Declarando as variáveis
pessoas = []
c = 0

# Laço para a inserção dos dados
while True:
    # Inserção dos dados
    nome = str(input('Seu nome: ')).strip().title()
    idade = int(input('Sua idade: ').strip())
    sexo = str(input(f'Sexo: [{IR}M{r}arculino / {IR}F{r}eminino / {IR}O{r}utros] ')).strip().upper()[0]
    
    # Tratamento de erro
    while sexo not in 'MFO':
        print(f'\n{IR}Valor incorreto!{r} Digite novamente.')
        sexo = str(input(f'Sexo: [{IR}M{r}asculino / {IR}F{r}eminino / {IR}O{r}utros] ')).strip().upper()[0]

    # Inserindo os dados em um dicionário, e depois colocando em uma lista
    dados = {'nome': nome, 'idade': idade, 'sexo': sexo}
    pessoas.append(dados)
    del nome, idade, sexo, dados
    
    c += 1

    esc = str(input(f'\nDeseja continuar? [{IB}S{r}im / {IR}N{r}ão] ')).strip().upper()[0]
    
    # Tratamento de erro
    if esc not in 'NS': print()
    while esc not in 'NS':
        esc = str(input(f'{IR}Valor incorreto!{r} Deseja continuar? [{IB}S{r}im / {IR}N{r}ão] ')).strip().upper()[0]
        
    print()
    
    if esc == 'N':
        break

# Declarando as variáveis
tot_pessoas = len(pessoas)
tot_idade = 0
tot_m = list()

# Laços para análise dos dados
for p in pessoas:
    tot_idade += p['idade']
    
    if p['sexo'] == 'F':
        tot_m.append(p['nome'])

if len(tot_m) == 0:
    tot_m = 'Nenhuma mulher foi cadastrada'
    
media_idade = tot_idade / tot_pessoas

# linha para design
sleep(0.5), print('==' * 20, '\n'), sleep(0.5)

# Exibição dos dados
print(f'- Número de pessoas cadastradas: {tot_pessoas}')
sleep(0.5)
print(f'- Média de idade do grupo: {media_idade:.1f}')
sleep(0.5)
print(f'- Nome das mulheres cadastradas: {tot_m}')
sleep(0.5)
print(f'- Pessoas com idade maior que a média do grupo: ')
sleep(0.5)

for i, p in enumerate(pessoas):
    if p['idade'] > media_idade:
        print('   -> ', end='')
        for k, v in p.items():
            print(f'{k.title()}: {v}; ', end='')
        
        print(), sleep(0.5)
        
if i == 0:
    print('   -- Nenhuma pessoa com a idade maior que a média')
sleep(0.5)


# Linha para design
print()
print('==' * 20), sleep(0.5)
