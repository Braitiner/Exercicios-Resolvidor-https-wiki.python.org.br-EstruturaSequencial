# Faça um programa que leia 5 números e informe o maior número.

maior = 0
for c in range(0,5):
    n = float(input('Digite um número: '))
    if n > maior:
        maior = n
print(maior)




