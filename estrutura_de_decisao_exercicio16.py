# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir
# os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

# A - Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir
# os demais valores, sendo encerrado;

# B - Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;

# C - Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;

# D - Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

delta = 0

a = float(input('Informe o valor de A: '))
if  a != 0: # Se A for diferente de zero continua com o programa, se não for finaliza.
    b = float(input('Informe o valor de B: '))
    c = float(input('Informe o valor de C: '))
    delta = (b**2) - (4 * a) * c
    if delta >= 0: # condição verificar o calculo de delta se for negativo, finaliza informando que não possui raiz.
        if delta == 0:
            print('Possui apenas uma raiz')
        elif delta > 0:
            print('Possui duas raizes')

    else:
        print('Delta negativo Equação não possui raizes reais.')
else:
    print('Não é uma equação de segundo grau.')
