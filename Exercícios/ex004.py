print('===================================')
a = input('Digite algo para analisar: ')
print(' ')
print('Classe primitiva', type(a))
print('É um número?', a.isnumeric())
print('É um decimal?', a.isnumeric())
print('É alfabética', a.isalpha())
print('É um alfanumérico?', a.isalnum())
print('É maiúsculo?', a.isupper())
print('É minúsculo?', a.islower())
print('A primeira letra está em maiúsculo?', a.istitle())
print('Só contém espaço?', a.isspace())
print(' ')
print('========Análise concluída!========')
