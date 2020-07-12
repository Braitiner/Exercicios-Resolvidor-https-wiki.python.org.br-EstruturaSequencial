# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
# variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite
# e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peixe =float(input('Qual o peso do peixe: '))
if (peixe>50):
    excesso = peixe - 50
    print('Você excedeu o limite estabelecido pelo regulamento em {}, o valor da múlta é de R${:.2f}.'.format(excesso, excesso*4))
else:
    print('O peso esta dentro do regulamento.')
