distancia = float(input('Digite a distância da sua viajem: '))
if distancia <= 200:
    print('\nComo a distância é menor ou igual que 200, sendo cobrado R$0,50 por Km')
    print(f'O valor da passagem é R${0.50 * distancia}')
else:
    print('\nComo a distância é maior que 200, sendo cobrado R$0,45 por Km')
    print(f'O valor da passagem é R${0.45 * distancia}')
