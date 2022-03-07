# Import
from datetime import datetime
from time import sleep as s

# Pegando dados iniciais
user = {
    'Nome': str(input('Nome: ')).strip().upper(),
    'Idade': datetime.now().year - int(input('Ano de nascimento: ').strip()),
    'Ctps': int(input('Número da Cateira de Trabalho (Se não tiver, digite 0): '))}

if user['Ctps'] != 0:
    user['Ano de contratação'] = int(input('Ano de contratação: ').strip())
    user['Salário'] = f'{int(input("Salário: R$")):.2f}'
    user['Data da aposentadoria'] = user['Ano de contratação'] + 35

s(0.5)
print('\n=-=-=-=-=-=-=-=-=-=-=-=-=\n')
for k, v in user.items():
    s(0.5)
    print(f'{k}: {v}')
s(0.5)
print('\n=-=-=-=-=-=-=-=-=-=-=-=-=')
s(0.6)
