# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
# 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

largura = float(input('Informe a largura: '))
comprimento = float(input('informe o comprimento: '))
area = largura*comprimento
tinta = area/3
lata =int(tinta/18)
if (tinta%18>0):
      latamais = lata + 1
      valor = latamais*80
      print('A área total de pintura é {area}, é preciso {latamais} de latas de tinta, o valor total é de R${valor}'
            .format(area=area, latamais=latamais, valor=valor))
else:
      valor = lata*80
      print('A área total de pintura é {area}, é preciso {lata} de latas de tinta, o valor total é de R${valor}'
            .format(area=area, lata=lata, valor=valor))
