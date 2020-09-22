# O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de
# quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado
# o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar
# na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os
# preços de 1 até 50 produtos, conforme o exemplo abaixo:
# EX: Lojas Quase Dois - Tabela de Preços
# 1 - R$ 1.99
# 2 - R$ 3.98
# ...
# 50 - R$ 99.50
print('Lojas Quase Dois\n', '-='*10, '\nTabela de Preços')
for c in range(1, 51):
    print(f'{c:>3} - R${c * 1.99:>6.2f}')
