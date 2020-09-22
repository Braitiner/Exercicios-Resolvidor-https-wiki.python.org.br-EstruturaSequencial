# Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o
# fatorial a números inteiros positivos e menores que 16.
sair = ''
while True:
    n = int(input('Escolha um número de 0 a 16 para fatorar? '))
    while n < 0 or n > 16:
        n = int(input('AVISO - O número deve ser de 0 a 16: '))
    c = n
    calc = c
    print(f'{n}! = ', end='')
    while c >= 1:
        if c == 1:
            print(c, end='= ')
            c -= 1
        else:
            print(c, end='.')
            calc = calc * (c - 1)
            c -= 1
    print(calc)
    sair = str(input('Deseja fatorar um novo número entre 0 e 16: [S/N] ')).upper().strip()[0]
    while sair not in 'SN':
        sair = str(input('AVISO - Escolha S para sim e N para não: ')).upper().strip()[0]
    if sair == 'N':
        break
