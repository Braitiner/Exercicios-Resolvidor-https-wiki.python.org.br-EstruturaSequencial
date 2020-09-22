# Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes
# intervalos: [0-25], [26-50], [51-75] e [76-100] a entrada de dados deverá terminar quando for lido um número negativo.

c_1 = c_2 = c_3 = c_4 = 0
while True:
    n = int(input('Informe um número: '))
    if n < 0:
        break
    elif n <= 25:
        c_1 += 1
    elif n <= 50:
        c_2 += 1
    elif n <= 75:
        c_3 += 1
    elif n <= 100:
        c_4 += 1
print(f'Números entre [0-25] - {c_1}\nNúmeros entre [26-50] - {c_2}\nNúmeros entre [51-75] - {c_3}'
      f'\nNúmeros entre [76-100] - {c_4}')


