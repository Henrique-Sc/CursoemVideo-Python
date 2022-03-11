def escreva(txt):
    tam_txt = len(txt) + 4
    print('-' * tam_txt)
    print(f'{txt:^{tam_txt}}')
    print('-' * tam_txt)


escreva('Olá mundo')
print('')
escreva('Henrique da SIlva Costa')
print('')
escreva('python')