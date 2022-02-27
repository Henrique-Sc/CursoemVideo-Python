salario = float(input('Qual o valor do seu salário? R$'))
if salario >= 1250:
    print(f'Seu novo salário com um aumento de 10% fica R${salario * 10 / 100 + salario:.2f}')
else:
    print(f'Seu novo salário com um aumento de 15% fica R${salario * 15 / 100 + salario:.2f}')
