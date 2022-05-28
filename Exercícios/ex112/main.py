# Importar o módulo moeda
from utilidadesCeV import moeda
from utilidadesCeV import dado


# Usar as funções aumentar, diminuir, dobro e metade
p = dado.leiaDinheiro('Digite o preço do produto: R$')
moeda.resumo(p, 80, 35)
