# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool: até 20 litros, desconto de 3% por litro, acima de 20 litros, desconto de 5% por litro
# Gasolina: até 20 litros, desconto de 4% por litro, acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
# (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se
# que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

litro = float(input('Quantos litros foram abastecidos: '))
combus = input('Qual combustivel?\nA - àlcool\nG - gasolina\n- ')
if combus == 'G':
    if litro <= 20:
        preco = litro * 2.5
        desc = preco * 0.03
        print(f'{litro} de gasoline, valor a pagar {preco - desc:.2f}')
    else:
        preco = litro * 2.5
        desc = preco * 0.05
        print(f'{litro} de gasoline, valor a pagar {preco - desc:.2f}')
elif combus == 'A':
    if litro <= 20:
        preco = litro * 1.9
        desc = preco * 0.03
        print(f'{litro} de Alcool, valor a pagar {preco - desc:.2f}')
    else:
        preco = litro * 1.9
        desc = preco * 0.05
        print(f'{litro} de Alcool, valor a pagar {preco - desc:.2f}')
else:
    print('Incorreto; informar A para Álcool ou G para gasolina')
