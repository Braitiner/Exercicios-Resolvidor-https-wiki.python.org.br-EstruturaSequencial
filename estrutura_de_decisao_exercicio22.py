# Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
# Dica: utilize o operador módulo (resto da divisão).
numero = int(input('Informe um número: '))
if numero % 2 > 0:
    print(f'{numero} é número impar')
else:
    print(f'{numero} é um número par')
