valor_casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual é o valor do seu salário? R$'))
anos = float(input('Em quantos anos aproximadamente, você pretende terminar de pagar essa casa? '))
meses = anos * 12
mensalidade = valor_casa / meses

if mensalidade <= (salario * 0.3):
    print('\n\033[34mO empréstimo foi aprovado!\033[m')
    print(f'Você terá que pagar \033[4;31m{meses:.0f} parcelas\033[m, sendo elas no valor de \033[33mR${mensalidade:.2f}\033[m')
else:
    print('\n\033[31mO empréstimo não foi aprovado!\033[m')
    print(f'As parcelas excedeu \033[4;1m30%\033[m do seu salário (R${salario * 0.3:.2f}), sendo cada parcela no valor de \033[31mR${mensalidade:.2f}\033[m')
    print(f'Sendo elas, {meses:.0f} parcelas ao todo.')
