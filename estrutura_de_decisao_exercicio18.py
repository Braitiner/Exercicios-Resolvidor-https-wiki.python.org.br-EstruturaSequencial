# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

dia = int(input('Informe o dia: '))
if dia >= 1 and dia <= 31:
    mes = int(input('Informe o mês: '))
    if mes >=1 and mes <= 12:
        ano = int(input('Informe o ano: '))
        if ano >= 0:
            print(f'Formato correto - {dia:0>2}/{mes:0>2}/{ano:0>4}')
        else:
            print('Formato incorreto')
    else:
        print('Formato incorreto')
else:
    print('Formato incorreto')