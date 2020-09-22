# Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da
# operação deve ser acompanhado de uma frase que diga se o número é:
# A - par ou ímpar;
# B - positivo ou negativo;
# C - inteiro ou decimal.

n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
operacao = int(input('Informe qual operação deseja realizar entre os números informados:\n1 - Soma\n2 - Subtração'
                     '\n3 - Multiplicação\n4 - Divisão\n '))
if operacao == 1:
    operacao = n1 + n2
    if operacao % 2 > 1:
        parouimpar = 'Impar'
    else:
        parouimpar = 'Par'
    if operacao < 0:
        positivonegativo = 'Negativo'
    else:
        positivonegativo = 'Positivo'
    if operacao == round(operacao):
        int_dec = 'Inteiro'
    else:
        int_dec = 'Decimal'
elif operacao == 2:
    operacao = n1 - n2
    if operacao % 2 > 1:
        parouimpar = 'Impar'
    else:
        parouimpar = 'Par'
    if operacao < 0:
        positivonegativo = 'Negativo'
    else:
        positivonegativo = 'Positivo'
    if operacao == round(operacao):
        int_dec = 'Inteiro'
    else:
        int_dec = 'Decimal'
elif operacao == 3:
    operacao = n1 * n2
    if operacao % 2 > 1:
        parouimpar = 'Impar'
    else:
        parouimpar = 'Par'
    if operacao < 0:
        positivonegativo = 'Negativo'
    else:
        positivonegativo = 'Positivo'
    if operacao == round(operacao):
        int_dec = 'Inteiro'
    else:
        int_dec = 'Decimal'
elif operacao == 4:
    operacao = n1 / n2
    if operacao % 2 > 1:
        parouimpar = 'Impar'
    else:
        parouimpar = 'Par'
    if operacao < 0:
        positivonegativo = 'Negativo'
    else:
        positivonegativo = 'Positivo'
    if operacao == round(operacao):
        int_dec = 'Inteiro'
    else:
        int_dec = 'Decimal'
else:
    print('Operação invalida.')
print(f'O resultado é {operacao} um número {parouimpar}, {positivonegativo} e {int_dec}')