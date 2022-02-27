from time import sleep

print('\033[37m=-\033[m' * 6, '\033[31mAnálise de dados\033[m', '\033[37m-=\033[m' * 6)

num = [float(input('\nDigite um valor: '))]

escolha = str()
while escolha != 'N':
    num.append(float(input('Digite outro valor: ')))
    escolha = input('\nDeseja continuar? [\033[34mS\033[m/\033[31mN\033[m] ').strip().upper()
    while escolha not in 'SN':
        escolha = input('\033[31mValor incorreto! Digite um valor válido:\033[m [\033[34mS\033[m/\033[31mN\033[m] \033[m').strip().upper()

sleep(0.5)
print('\n\033[33mAnalizando os dados...\033[m')
sleep(1)

print(f'\nQuantidade de números digitados: {len(num)}')
print(f'Maior número: {max(num)}')
print(f'Menor número: {min(num)}')
print(f'\n\033[34mMédia dos valores: {sum(num) / len(num):.2f}\033[m')
