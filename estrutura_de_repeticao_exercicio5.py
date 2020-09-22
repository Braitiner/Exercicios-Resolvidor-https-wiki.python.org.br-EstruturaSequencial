# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a
# entrada e permita repetir a operação.
repetir = 'S'
while repetir == 'S':
    print('Comparativo de Crescimento entre paises')
    pais_a = float(input('Infome a população do primeiro pais: '))
    while pais_a <= 0:
        pais_a = float(input('Aviso, a população deve ser maior que zero, infome a população do primeiro pais: '))
    taxa_a = float(input('Informe a taxa de crescimento do primeiro pais: '))/100
    pais_b = float(input('Informe a população do segundo pais: '))
    while pais_b < 0:
        pais_b = float(input('Aviso, a população deve ser maior que zero, infome a população do segundo pais: '))
    taxa_b = float(input('Informe a taxa de crescimento do segundo pais: '))/100
    ano_a = 0
    ano_b = 0
    if pais_a < pais_b:
        while pais_a <= pais_b:
            pais_a *= taxa_a+1
            pais_b *= taxa_b+1
            ano_a += 1
    else:
        while pais_b <= pais_a:
            pais_b *= taxa_b+1
            pais_a *= taxa_a+1
            ano_b += 1
    if ano_a > ano_b:
        print(f'O pais A vai demorar {ano_a} anos para igualar sua população com o pais B')
    else:
        print(f'O pais B vai demorar {ano_b} anos para igualar sua população com o pais A')
    repetir = str(input('Deseja fazer uma nova analise: [S/N]')).upper().strip()[0]
    while repetir not in 'SN':
        repetir = str(input('Aviso, escolha S para Sim e N para Não, deseja fazer uma nova analise: [S/N]')).upper().strip()[0]




