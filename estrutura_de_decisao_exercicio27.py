# Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                       Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um
# desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
# (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

morango = float(input('Informe a quantidade de morango: '))
maca = float(input('Informe a quantidade de maça: '))
p1 = 2.5
p2 = 1.8
peso = morango + maca
if morango >= 5:
    p1 = 2.2
    morango = morango * p1
    print(morango)
else:
    morango = morango * p1
    print(morango)
if maca >= 5:
    p2 = 1.5
    print(maca)
    maca = maca * p2
else:
    maca = maca * p2
    print(maca)
valor = morango + maca
print(valor)
if peso >= 8 or valor >= 25:
    valor = valor * 0.9
    print(f'O valor da compra é R${valor:.2f}')
else:
    print(f'O valor da compra é R${valor:.2f}')

