# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
n = int(input('Qual número deseja fatorar? '))
c = n
calc = c
print(f'{n}! = ',end='')
while c >= 1:
    if c == 1:
        print(c,end='= ')
        c -= 1
    else:
        print(c, end='.')
        calc = calc * (c - 1)
        c -= 1
print(calc)
