nome = input('Digite seu nome completo: ')
print(f"""\nSeu nome com todas as letras maiúsculas:
{nome.upper()}""")

print(f"""\nSeu nome com todas as letras minúsculas:
{nome.lower()}""")

print(f"\nTotal de letras do seu nome: {len(''.join(nome.split()))}""")

print(f"\nTotal de letras do seu primeiro nome: {len(nome.split()[0])}")
