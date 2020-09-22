# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
# Não utilize a função de potência da linguagem

print('Exponenciação')
base = int(input('Informe a base: '))
exp = int(input('Informe o expoente: '))
cont = 1
calc = 1 #calc recebe 1 para não zerar a multiplicação.
while cont <= exp:
    if cont == exp:
        print(f'{base}', end=' ')
        calc *= base
        cont += 1
    else:
        print(f'{base} x', end=' ')
        calc *= base
        cont += 1
print(f'= {calc}')


