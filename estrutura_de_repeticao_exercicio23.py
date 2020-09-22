# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa
# deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o
# funcionamento, o estilo e o número de testes (divisões) executados.

n = int(input('Informe um número para saber se é primo e os primos antecessores a ele.: '))
divisao = 0
while True:
    zeros = 0
    resto = 0
    for c in range(1, n + 1):
        resto = n % c
        divisao += 1
        if resto == 0:
            zeros += 1
    if zeros == 2:
        print(f'O número {n} é primo.')
    n -= 1
    if n == 0:
        break
print(f'O sistema realizou {divisao} divisões para encontrar os números primos.')

