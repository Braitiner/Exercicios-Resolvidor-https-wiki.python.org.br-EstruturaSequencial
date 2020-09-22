# Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
n3 = float(input('Terceiro número: '))

# maior número
if n1 >= n2 and n1 >= n3:
    maior = n1
elif n2 >= n1 and n2 >= n3:
    maior = n2
elif n3 >= n1 and n3 >= n2:
    maior = n3
# menor número
if n1 <= n2 and n1 <= n3:
    menor = n1
elif n2 <= n1 and n2 <= n3:
    menor = n2
elif n3 <= n1 and n3 <= n1:
    menor = n3

# Número médio
if n1 != maior and n1 != menor:
    medio = n1
elif n2 != maior and n2 != menor:
    medio = n2
elif n3 != maior and n3 != menor:
    medio = n3

# Impressão na tela:
print(f'{maior}\n{medio}\n{menor}')

# Para resolver o exercício identifiquei primeiro o maior e o menor número, depois identifiquei qual o numéro é
# diferente de maior e menor este é o número do meio.
