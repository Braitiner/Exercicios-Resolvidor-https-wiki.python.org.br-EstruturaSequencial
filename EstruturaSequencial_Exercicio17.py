# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de
# 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o preço seja o menor.
# Acrescente 10% de folga e sempre arredonde os valores para
# cima, isto é, considere latas cheias.

area1 = float(input('Informe o tamanho da área a ser pintada: '))
area = area1+area1*0.1
litro = (area/6)
lata = int(litro/18)
lataresto = (litro%18)
sogalao = int(litro/3.6)
sogalaoresto = (litro%3.6)
galao = 0
galaoresto = 0
# Menor preço (galão e lata)
if (lataresto<=10.8):
    galao = int(lataresto / 3.6)
    # print('galao',galao)
    galaoresto = lataresto-(galao*3.6)
    # print('galaoresto',galaoresto)
    if(galaoresto != 0):
            galao += 1
            print('O menor preço para pintar a área de {area}M² já considerando a perda de 10% é R${:.2f}, você vai levar {lata} lata(s), e {galao} galão(s).'
                  .format((lata*80+galao*25),lata=lata, galao=galao,area=area1))
else:
    lata += 1
    print('O menor preço para pintar a área de {area}M² já considerando a perda de 10% é R${:.2f} você vai levar {lata} lata(s).'.format((lata*80),area=area1,lata=lata))

# Somente latas
if (lataresto>0):
    lata += 1
    print('Comprando apenas lata para pintar a área de {area}M² já considerando a perda de 10% o valor é R${:.2f} e você vai levar {lata} lata(s).'
          .format((lata*80),area=area1, lata=lata))
else:
    print('Comprando apenas lata para pintar a área de {area}M² já considerando a perda de 10% o valor é R${:.2f} e você vai levar {lata} lata(s).'
        .format((lata * 80), area=area1, lata=lata))
# Somente galão
if  (sogalaoresto>0):
    sogalao +=1
    print('Comprando apenas Galão para pintar a área de {area}M² já considerando a perda de 10% o valor é R${:.2f} e você vai levar {galao} galão(s).'
        .format((sogalao * 25), area=area1, galao=sogalao))
else:
    print('Comprando apenas Galão para pintar a área de {area}M² já considerando a perda de 10% o valor é R${:.2f} e você vai levar {galao} galão(s).'
        .format((sogalao * 25), area=area1, galao=sogalao))


