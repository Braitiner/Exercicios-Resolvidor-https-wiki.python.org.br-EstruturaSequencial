# Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0
for x in range(0, 5):
    n = float(input('Informe um número: '))
    soma += n
print(f'A soma dos números são {soma} e a média é {soma / 5:.2f}')
