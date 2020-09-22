# Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de
# arredondamento.
numero = float(input('Informe um numro: '))
if numero == round(numero):
    print(f'{numero:.0f} - É um número interio.')
else:
    print(f'{numero} é um número decimal.')

