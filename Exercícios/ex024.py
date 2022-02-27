cidade = input('Digite o nome de uma cidade: ')
dividido = cidade.split()
formatado = dividido[0].title()
print(f"Essa cidade começa com o nome 'SANTO'? {'Santo' in formatado}")
