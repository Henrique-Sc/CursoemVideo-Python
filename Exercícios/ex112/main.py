# Importar o módulo moeda e dado
from utilidadesCeV import moeda
from utilidadesCeV import dado


# Usar as funções aumentar, diminuir, dobro e metade
preco = dado.leiaDinheiro('Digite o preço do produto: R$')
moeda.resumo(preco, 80, 35)
