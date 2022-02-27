from color import blue, red, yellow, magenta, black

print('\033[30mOBS: para valores numéricos com vírgula, troca-se a "," pelo "."\033[m\n')

valor_produto = float(input('Qual o valor do produto? R$'))
metodo_pagamento = int(input(f'''\n{black('Qual será o método de pagamento?')}

{black('1 - para')} {yellow('pagamentos à vista')} {black("""no dinheiro (10% de desconto)
2 - para""")} {blue('pagamentos à vista')} {black("""no cartão (5% de desconto)
3 - para""")} {magenta('pagamentos em até 2x')} {black("""no cartão (sem juros)
4 - para""")} {red('pagamentos em 3x ou mais')} {black('no cartão (20% de juros)')}

Digite a forma de \033[1;4mpagamento escolhida\033[m: '''))

if metodo_pagamento == 1:
    novo_produto = valor_produto - (valor_produto * 0.1)
    print(f'\nO produto no valor de {red(f"R${valor_produto:.2f}")}, com {yellow("10%")} de desconto fica no total de {blue(f"R${novo_produto:.2f}")}')

elif metodo_pagamento == 2:
    novo_produto = valor_produto - (valor_produto * 0.05)
    print(f'\nO produto no valor de {magenta(f"R${valor_produto:.2f}")}, com {yellow("5%")} de desconto fica no total de {blue(f"R${novo_produto:.2f}")}')

elif metodo_pagamento == 3:
    parcelas = valor_produto / 2
    print(f'\nO produto no valor de {blue(f"R${valor_produto:.2f}")}, divido em \033[4m2x no cartão\033[m sem juros, vai ter cada parcela no valor de {red(f"R${parcelas:.2f}")}')

elif metodo_pagamento == 4:
    total_parcelas = int(input('\nE em quantas vezes você gostaria de parcelar no cartão? '))
    parcelas = (valor_produto + valor_produto * 0.2) / total_parcelas
    print(f'\nO produto no valor de {red(f"R${valor_produto:.2f}")}, divido em \033[4m{total_parcelas}x no cartão\033[m com 20% de juros, vai ter cada parcela no valor de {blue(f"R${parcelas:.2f}")}')

else:
    print(red('\nOPÇÃO INVÁLIDA! Escolha uma opção entre 1 e 3'))
