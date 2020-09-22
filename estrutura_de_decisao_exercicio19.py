# Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
# mesmo
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

n = float(input('Informe um número entre 0 e 1000: '))
if n >= 0 and n <= 1000:
    centena = n // 100
    dezena = (n-centena*100)//10
    unidade = n-(centena*100)-(dezena*10)//1
    if centena >= 2 and dezena >= 2 and unidade >= 2:
        print(f'{n:.0f} = {centena:.0f} centenas, {dezena:.0f} dezenas e {unidade:.0f} unidades')
    elif centena == 1 and dezena >= 2 and unidade >=2:
        print(f'{n:.0f} = {centena:.0f} centena, {dezena:.0f} dezenas e {unidade:.0f} unidades')
    elif centena == 1 and dezena == 1 and unidade >=2:
        print(f'{n:.0f} = {centena:.0f} centena, {dezena:.0f} dezena e {unidade:.0f} unidades')
    elif centena == 1 and dezena == 1 and unidade == 1:
        print(f'{n:.0f} = {centena:.0f} centena, {dezena:.0f} dezena e {unidade:.0f} unidade')
    elif centena >= 2 and dezena == 0 and unidade == 0:
        print(f'{n:.0f} = {centena:.0f} centenas')
    elif centena >= 1 and dezena == 0 and unidade == 0:
        print(f'{n:.0f} = {centena:.0f} centena')
    elif centena >= 2 and dezena >= 2 and unidade == 0:
        print(f'{n:.0f} = {centena:.0f} centenas, {dezena:.0f} dezenas')
    elif centena >= 2 and dezena == 1 and unidade == 0:
        print(f'{n:.0f} = {centena:.0f} centenas, {dezena:.0f} dezena')
    elif centena == 0 and dezena >= 2 and unidade >=2:
        print(f'{n:.0f} = {dezena:.0f} dezenas e {unidade:.0f} unidades')
    elif centena == 0 and dezena == 1 and unidade >=2:
        print(f'{n:.0f} = {dezena:.0f} dezena e {unidade:.0f} unidades')
    elif centena == 0 and dezena == 1 and unidade == 1:
        print(f'{n:.0f} = {dezena:.0f} dezena e {unidade:.0f} unidade')
    elif centena == 0 and dezena == 0 and unidade >= 2:
        print(f'{n:.0f} = {unidade:.0f} unidades')
    elif centena == 0 and dezena == 0 and unidade == 1:
        print(f'{n:.0f} = {unidade:.0f} unidade')
    elif centena >= 2 and dezena == 0 and unidade >= 2:
        print(f'{n:.0f} = {centena:.0f} centenas e {unidade:.0f} unidades')
    elif centena >= 2 and dezena == 0 and unidade == 1:
        print(f'{n:.0f} = {centena:.0f} centenas e {unidade:.0f} unidade')
    elif centena == 1 and dezena == 0 and unidade == 1:
        print(f'{n:.0f} = {centena:.0f} centena e {unidade:.0f} unidade')
    elif centena >= 2 and dezena == 1 and unidade == 1:
        print(f'{n:.0f} = {centena:.0f} centenas, {dezena:.0f} dezena e {unidade:.0f} unidade')
    elif centena == 0 and dezena >= 2 and unidade == 0:
        print(f'{n:.0f} = {dezena:.0f} dezenas')
    elif centena == 0 and dezena == 1 and unidade == 0:
        print(f'{n:.0f} = {dezena:.0f} dezena')
    elif centena == 0 and dezena >= 2 and unidade == 1:
        print(f'{n:.0f} = {dezena:.0f} dezenas e {unidade:.0f} unidade')
else:
    print('O número de ser entre 0 a 1000 ')