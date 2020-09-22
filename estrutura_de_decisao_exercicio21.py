# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
# quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor
# mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes
# na máquina.
# A - Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5
# e uma nota de 1;
# B - Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro
# notas de 10, uma nota de 5 e quatro notas de 1.

valor = int(input('Qual o valor do saque: '))
if valor >= 10 and valor <= 600:
    n100 = valor // 100
    resto = valor - n100*100
    n50 = resto // 50
    resto = resto - n50*50
    n10 = resto // 10
    resto = resto - n10*10
    n5 = resto // 5
    resto = resto - n5 * 5
    n1 = resto // 1
    print(f'Nota de 100: {n100}\nNota de 50: {n50}\nNota de 10: {n10}\nNota de 5: {n5}\nNota de 1: {n1}')
else:
    print('Valor minimo é R$ 10.00 e maximo 600.00')
