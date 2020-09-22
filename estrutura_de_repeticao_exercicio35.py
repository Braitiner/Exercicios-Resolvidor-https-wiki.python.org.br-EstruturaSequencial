# Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre
# 1 e um número inteiro informado pelo usuário.

n = int(input('Informe um número: '))
for c_1 in range(1, n + 1):
    resto = zero = 0
    for c in range(1, c_1+1):
        resto = c_1 % c
        if resto == 0:
            zero += 1
    if zero == 2 and c_1 >= n:
        print(f'{c_1} ', end='')
    elif zero == 2:
        print(f'{c_1} \033[2;32m↠\033[m ', end='')

