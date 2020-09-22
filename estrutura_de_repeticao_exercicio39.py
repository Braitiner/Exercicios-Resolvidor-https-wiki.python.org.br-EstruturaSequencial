# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
# representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais
# alto e o número do aluno mais baixo, junto com suas alturas.

cod_aluno = int(input('Informe o código do aluno: '))
alt_aluno = int(input('Informe a altura do aluno em centimetros: '))
alto = baixo = alt_aluno
cod_alto = cod_baixo = cod_aluno
for c in range(1, 10):
    cod_aluno = int(input('Informe o código do aluno: '))
    alt_aluno = int(input('Informe a altura do aluno em centimetros: '))
    if alto < alt_aluno:
        alto = alt_aluno
        cod_alto = cod_aluno
    if baixo > alt_aluno:
        baixo = alt_aluno
        cod_baixo = cod_aluno
print(f'''O aluno mais altoe é {cod_alto} e tem {alto} cm
O aluno mais baixo é {cod_baixo} e tem {baixo} cm.''')
