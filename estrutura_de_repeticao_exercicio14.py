# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de
# números Ímpares.
par = impar = soma = 0
for c in range(0, 10):
    n = int(input('Informe um número inteiro: '))
    soma += n
    if n % 2 == 1:
        impar += 1
    else:
        par += 1
print(f'O somatorio é {soma}, foi informado {par} números pares e {impar} números impares.')
