# Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

n = int(input('Informe um número entre 0 e 1000: '))
while n < 0 or n > 1000:
    n = int(input('\033[1;31mAviso:\033[m Informe um número entre 0 e 1000: '))
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
        n = int(input('Informe um número entre 0 e 1000: '))
        while n < 0 or n > 1000:
            n = int(input('\033[1;31mAviso:\033[m Informe um número entre 0 e 1000: '))
print(f'O maior número informado é {maior}, o menor {menor} a soma de todos os valores lançados foi {soma}')
