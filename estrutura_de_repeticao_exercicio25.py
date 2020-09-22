# Faça um programa que calcule e mostre a média aritmética de N notas.
soma = cont = media = 0
while True:
    n = float(input('Informe um número ou -1 para sair: '))
    if n == -1:
        break
    soma += n
    cont += 1
    media = soma / cont

print(f'A média dos números registrados é {media}.')





