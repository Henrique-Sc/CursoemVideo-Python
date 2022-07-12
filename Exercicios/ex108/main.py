# Importar o módulo moeda.py
import moeda

# Usar as funções aumentar, diminuir, dobro e metade
p = float(input('Digite o preço: R$'))

print()
print('-' * 30)
print()

print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando em 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo em 13, temos {moeda.moeda(moeda.diminuir(p, 13))}')
