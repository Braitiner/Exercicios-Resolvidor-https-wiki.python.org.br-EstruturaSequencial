# O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto
# indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das
# temperaturas.

temp = float(input('Informe a temperatura: '))
menor = maior = temp
soma = cont = 0
while True:
    soma += temp
    cont += 1
    sair = str(input('Deseja lançar uma nova temperatura? [S/N]')).upper().strip()[0]
    while sair not in 'SN':
        sair = str(input('AVISO - Informe S para sim e N para não. Deseja lançar uma nova temperatura? [S/N]')).upper().strip()[0]
    if sair == 'N':
        break
    temp = float(input('Informe a temperatura: '))
    if menor > temp:
        menor = temp
    elif maior < temp:
        maior = temp
print(f'Menor temperatura {menor}\nMaior temperatura {maior}\nTemperatura média {soma/cont:.2f}')

