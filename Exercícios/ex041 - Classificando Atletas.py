from datetime import date
nascimento = int(input('Em que ano você nasceu? '))
ano_atual = date.today().year
idade = ano_atual - nascimento

if idade < 10:
    print(f'Como você tem \033[33m{idade} anos\033[m, a sua categoria na nataçaõ é: \033[34mMIRIM\033[m')
elif idade < 15:
    print(f'Como você tem \033[33m{idade} anos\033[m, a sua categoria na nataçaõ é: \033[34mINFANTIL\033[m')
elif idade < 20:
    print(f'Como você tem \033[33m{idade} anos\033[m, a sua categoria na natação é: \033[34mJUNIOR\033[m')
elif idade < 21:
    print(f'Como você tem \033[33m{idade} anos\033[m, a sua categoria na natação é: \033[34mSÊNIOR\033[m')
else:
    print(f'Como você tem \033[33m{idade} anos\033[m, a sua categoria na natação é: \033[34mMASTER\033[m')
