# Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é
# aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é
# ou não um número primo.
n = int(input('Informe um número: '))
resto = zero = 0
for c in range(1, n+1):
    resto = n % c
    if resto == 0:
        zero += 1
if zero == 2:
    print(f'O número {n} é primo.')
else:
    print(f'O número {n} não é primo.')
