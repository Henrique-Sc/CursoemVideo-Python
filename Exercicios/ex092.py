# Import
from datetime import datetime
from time import sleep as s

# Pegando dados iniciais
user = dict()
user['Nome'] = str(input('Nome: ')).strip().upper()
nasc = int(input('Ano de nascimento: ').strip())
user['Idade']= datetime.now().year - nasc
user['Ctps'] = int(input('Número da Cateira de Trabalho (Se não tiver, digite 0): '))

# Se tiver carteira de trabalho, terá que inserir mais dados
if user['Ctps'] != 0:
    user['Ano de contratação'] = int(input('Ano de contratação: ').strip())
    user['Salário'] = f'{int(input("Salário: R$")):.2f}'
    user['Idade da aposentadoria'] = (user['Ano de contratação'] + 35) - nasc

# Mostrando os dados
s(0.5)
print('\n=-=-=-=-=-=-=-=-=-=-=-=-=\n')
for k, v in user.items():
    s(0.5)
    print(f'{k}: {v}')
s(0.5)
print('\n=-=-=-=-=-=-=-=-=-=-=-=-=')
s(0.6)
