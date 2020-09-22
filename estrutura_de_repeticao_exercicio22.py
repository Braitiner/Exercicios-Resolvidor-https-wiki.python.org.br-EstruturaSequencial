# Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é
# divisível.

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
    for c2 in range(1, n+1):
        resto = n % c2
        if resto == 0:
            print(f'O número {n} é multiplo de {c2}')
