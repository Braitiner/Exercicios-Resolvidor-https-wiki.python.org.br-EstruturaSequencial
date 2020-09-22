# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão
# é sempre pelo mais barato.

p1 = float(input('Informe o valor do primeiro produto: R$ '))
p2 = float(input('Informe o valor do segundo produto: R$ '))
p3 = float(input('Informe o valor do segundo produto: R$ '))
if p1 <= p2 and p1 <= p3:
    print(f'O menor valor é o primeiro produto R$ {p1:.2f}.')
elif p2 <= p1 and p2 <= p3:
    print(f'O menor valor é o segundo produto R$ {p2:.2f}.')
elif p3 <= p1 and p3 <= p2:
    print(f'O menor valor é o terceiro produto R$ {p3:.2f}.')


