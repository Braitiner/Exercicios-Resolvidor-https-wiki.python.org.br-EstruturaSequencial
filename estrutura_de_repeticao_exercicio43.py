# O cardápio de uma lanchonete é o seguinte:
# Especificação   Código  Preço
# Cachorro Quente 100     R$ 8,20
# Bauru Simples   101     R$ 8,30
# Bauru com ovo   102     R$ 9,50
# Hambúrguer      103     R$ 12,20
# Cheeseburguer   104     R$ 15,30
# Refrigerante    105     R$ 5,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago
# por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve
# ser encerrado.
p1 = p2 = p3 = p4 = p5 = p6 = q1 = q2 = q3 = q4 = q5 = q6 = valor_tot = 0
while True:
    codigo = int(input('''Especificação     Código     Preço
Cachorro Quente   100        R$  8,20
Bauru Simples     101        R$  8,30
Bauru com ovo     102        R$  9,50
Hamburguer        103        R$ 12,20
Cheeseburguer     104        R$ 15,30
Refrigerante      105        R$  5,00
Codigo ou 0 para sair>> '''))
    while codigo not in(0,100,101,102,103,104,105):
        print('AVISO, código incorreto')
        codigo = int(input('''Especificação     Código     Preço
        Cachorro Quente   100        R$  8,20
        Bauru Simples     101        R$  8,30
        Bauru com ovo     102        R$  9,50
        Hamburguer        103        R$ 12,20
        Cheeseburguer     104        R$ 15,30
        Refrigerante      105        R$  5,00
        Codigo ou 0 para sair>> '''))
    if codigo == 0:
        break
    quantidade = int(input('Quantidade: '))
    if codigo == 100:
        p1 = quantidade * 8.2
        q1 += quantidade
    if codigo == 101:
        p2 = quantidade * 8.3
        q2 = quantidade
    if codigo == 102:
        p3 = quantidade * 9.5
        q3 = quantidade
    if codigo == 103:
        p4 = quantidade * 12.90
        q4 = quantidade
    if codigo == 104:
        p5 = quantidade * 15.30
        q5 = quantidade
    if codigo == 105:
        p6 = quantidade * 5
        q6 = quantidade

    valor_tot += p1
if p1 > 0:
    print(f'{q1} Cachorro Quente - R$ {p1:.2f}')
if p2 > 0:
    print(f'{q2} Bauru Simples - R$ {p2:.2f}')
if p3 > 0:
    print(f'{q3} Bauru Simples - R$ {p3:.2f}')
if p4 > 0:
    print(f'{q4} Bauru Simples - R$ {p4:.2f}')
if p5 > 0:
    print(f'{q5} Bauru Simples - R$ {p5:.2f}')
if p6 > 0:
    print(f'{q6} Bauru Simples - R$ {p6:.2f}')
print(f'Valor total: {valor_tot:.2f}')










