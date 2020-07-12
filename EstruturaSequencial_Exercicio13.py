# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

h = float(input('Qual a sua altura: '))
man = (72.7*h)-58
woman = (62.1*h) - 44.7
print('O peso ideial se for mulher é {}, se for homem é {}.'.format(woman, man))
