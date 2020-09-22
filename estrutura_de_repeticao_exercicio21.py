# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que
# é divisível somente por ele mesmo e por 1.

n = int(input('Informe um número para saber se é ou não primo: '))
zeros = 0
resto = 0
for c in range(1, n+1):
    resto = n % c
    if resto == 0:
        zeros += 1
if zeros == 2:
    print(f'O número {n} é primo.')
else:
    print(f'O número {n} não é primo.')
