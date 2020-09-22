# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

n = int(input('Informe um número: '))
menor = n
maior = n
sair = ''
soma = 0
while True:
    if maior < n:
        maior = n
    if menor > n:
        menor = n
    soma += n
    sair = str(input('Deseja incluir mais um número? [S/N]')).upper().strip()[0]
    while sair not in 'SN':
        sair = str(input('Opção incorreta, informe S para sim e N para não: ')).upper().strip()[0]
    if sair == 'N':
        break
    if sair == 'S':
        n = int(input('Infome um número: '))
print(f'O maior número informado é {maior}, o menor {menor} a soma de todos os valores lançados foi {soma}')
