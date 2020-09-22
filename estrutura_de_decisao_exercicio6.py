# Faça um Programa que leia três números e mostre o maior deles.

n1 = float(input('Informe o primeoro número: '))
n2 = float(input('Informe o segundo númeor: '))
n3 = float(input('Infome o teceiro número: '))
if n1 > n2 and n1 > n3:
    print(f'o maior número é {n1}')
elif n2 > n1 and n2 > n3:
    print(f'O maior número é {n2}')
else:
    print(f'O maior número é {n3}')

