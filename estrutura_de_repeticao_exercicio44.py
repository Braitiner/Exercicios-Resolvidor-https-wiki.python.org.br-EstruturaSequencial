# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos
# utilizados são:
# > 1 , 2, 3, 4  - Votos para os respectivos candidatos
# > (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# > 5 - Voto Nulo
# > 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# a. O total de votos para cada candidato;
# b. O total de votos nulos;
# c. O total de votos em branco;
# d. A percentagem de votos nulos sobre o total de votos;
# e .A percentagem de votos em branco sobre o total de votos.
# f. Para finalizar o conjunto de votos tem-se o valor zero.
l_1 = l_2 = l_3 = l_4 = l_5 = l_6 = p_n = p_b = cont = 0
while True:
    cadidatos = int(input('Escolha uma opção\n[1] - Bolsonario\n[2] - Lula\n[3] - Aécio Neves\n[4] - Jose Serra\n[5] '
                          '- Nulo\n[6] - Voto em Branco\n[0] - Sair\n >> '))
    while cadidatos not in (0, 1, 2, 3, 4, 5, 6):
        print('AVISO - Opção invalida')
        cadidatos = int(input(
            'Escolha uma opção\n[1] - Bolsonario\n[2] - Lula\n[3] - Aécio Neves\n[4] - Jose Serra\n[5] - Nulo\n[6] - '
            'Voto em Branco\n[0] - Sair\n>> '))
    if cadidatos == 0:
        break
    if cadidatos == 1:
        l_1 += 1
    if cadidatos == 2:
        l_2 += 1
    if cadidatos == 3:
        l_3 += 1
    if cadidatos == 4:
        l_4 += 1
    if cadidatos == 5:
        l_5 += 1
    if cadidatos == 6:
        l_6 += 1
    cont += 1
p_n = l_5/cont
p_b = l_6/cont
print(f'Resultados:\n[1] - Bolsonario - {l_1} votos\n[2] - Lula - {l_2} votos\n[3] - Aécio Neves - {l_3} votos\n'
      f'[4] - Jose Serra -{l_4} votos\n[5] - Nulo - {l_5} votos\n[6] - Voto em Branco - {l_6} votos'
      f'\nPercentual de votos Nulos {p_n*100:.2f}%\nPercentual de votos Brancos - {p_b*100:.2f}%')
