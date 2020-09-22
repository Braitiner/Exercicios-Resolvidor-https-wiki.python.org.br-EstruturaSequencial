# Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto
# em cada um deles. O usuário deverá informar a quantidade de CDs e o valor pago em cada um.

cd = int(input('Quantos CDs tem na coleção: '))
soma = media = 0
for c in range(1, cd + 1):
    valor = float(input(f'Qual valor pagou no CD {c}: R$ '))
    soma += valor
print(f'Sua coleção é composta por {cd} CDs, o preço médio do CD é R${soma/cd:.2f}, o valor total gasto em sua coleção '
      f'é R${soma:.2f}')
