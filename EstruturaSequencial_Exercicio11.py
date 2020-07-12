# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.

n1 = int(input('Informe um número inteiro: '))
n2 = int(input('Informe um número inteiro: '))
n3 = float(input('Informe um número real: '))
equac1 = (n1**2) + (n2/2)
equac2 = (n1*3)+n3
equac3 = n3**3

print('O produto do dobro do primeiro número com metade do segundo número ={equac1}'
      '\nA soma do triplo do primeiro número com o terceiro número ={equac2}'
      '\nO terceiro número elevado ao cubo ={equac3}.'.format(equac1=equac1,equac2=equac2,equac3=equac3))



