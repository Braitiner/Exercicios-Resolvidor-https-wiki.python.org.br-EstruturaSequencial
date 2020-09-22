# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por
# eles.

n_1 = int(input('Informe o primeiro número: '))
n_2 = int(input('Informe o segundo número: '))
if n_1 >= n_2:
    cont = n_2 + 1
    print(f'Os números inteiros entre o intervalo de {n_2} a {n_1} são: ')
    while cont < n_1:
        print(cont, end=', ')
        cont += 1
else:
    cont = n_1 + 1
    print(f'Os números inteiros entre o intervalo de {n_1} a {n_2} são: ')
    while cont < n_2:
        print(cont, end=', ')
        cont += 1
