# Faça um Programa que leia três números e mostre o maior e o menor deles.

print('Informe três numeros diferentes:')
n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo númeor: '))
n3 = float(input('Teceiro número: '))
# Utilizei o >= e <= porque se o usuário informar numeros iguais ele tambem identifica.
if n1 >= n2 and n1 >= n3:
    print(f'O maior número é: {n1}')
elif n2 >= n1 and n2 >= n3:
    print(f'O maior número é: {n2}')
elif n3 >= n1 and n3 >= n2:
    print(f'O maior número é: {n3}')

if n1 <= n2 and n1 <= n3:
    print(f'O menor número é: {n1}')
elif n2 <= n1 and n2 <= n3:
    print(f'O menor número é: {n2}')
elif n3 <= n1 and n3 <= n2:
    print(f'O menor número é: {n3}')



