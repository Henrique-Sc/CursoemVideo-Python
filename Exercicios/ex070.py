reset = '\033[m'
red = '\033[31m'
IBlue = '\033[34;1m'
blue = '\033[34m'

cont = 1
valor_total = prod_mais_mil = valor_prod_barato = 0
nome_prod_barato = str

print(f'{IBlue}=-=' * 5 + '-' + f'=-=' * 4)
print(f'=-{reset}  Cadastro de produtos  {IBlue}-={reset}')
print(f'{IBlue}=-=' * 5 + '-' + f'=-=' * 4)

print('')
while True:
    print(f'{red}-={reset}' * 4, f'{cont}º Produto', f'{red}=-{reset}' * 4)

    nome_produto = str(input('\nNome do produto: ')).strip()
    valor_produto = float(input('preço do produto: R$').strip())
    if valor_produto > 1000:
        prod_mais_mil += 1
    if cont == 1 or valor_produto < valor_prod_barato:
        nome_prod_barato = nome_produto
        valor_prod_barato = valor_produto
    cont += 1
    valor_total += valor_produto

    escolha = str(input('\nQuer continuar? [S/N] ')).strip().upper()[0]
    while escolha not in 'SN':
        escolha = str(input(f'{red}Valor inválido! Digite novamente: [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
    print('')
print('')
print(f'{IBlue}=-=' * 5 + '-' + f'{IBlue}=-={reset}' * 4)
print('')
print(f'''Valor total dos produtos: R${valor_total:5.2f}
Temos {prod_mais_mil} produtos custando mais de R$1000
O produto mais barato é o(a) {nome_prod_barato} e custa R${valor_prod_barato:.2f}''')
