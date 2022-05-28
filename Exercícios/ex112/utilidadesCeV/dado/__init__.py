def leiaDinheiro(txt):
    """
    -> Funcionamento parecido com um input, porém com tratamento de erros. Uso exclusivo para tratamento monetário.
    :param txt: Texto que vai ser visualizado pelo usuário, para que ele posssa digitar
    :return: retorna o valor que o usuário digitar
    """
    while True:
        # Receber uma string, excluindo os espaços, e se tiver vírgula, troca para pontos
        dinheiro = input(txt).strip().replace(',', '.')

        # Se a variável dinheiro, retirando os ponto for um decimal, converte o valor em Float
        if dinheiro.replace('.', '').isdecimal():
            dinheiro = float(dinheiro)
            break

        # Se não, retorna para o usuário que o valor inserido não é monetário
        else:
            print(f'\033[31mErro! "{dinheiro}" não é um valor monetário.\033[m')

    return float(dinheiro)
