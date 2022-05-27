# Importar o módulo moeda.py
import moedas

# Usar as funções aumentar, diminuir, dobro e metade
p = float(input('Digite o preço: R$'))

print()
print('-' * 30)
print()

print(f'A metade de {moedas.moeda(p)} é {moedas.moeda(moedas.metade(p))}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.moeda(moedas.dobro(p))}')
print(f'Aumentando em 10%, temos {moedas.moeda(moedas.aumentar(p, 10))}')
print(f'Diminuindo em 13, temos {moedas.moeda(moedas.diminuir(p, 13))}')
