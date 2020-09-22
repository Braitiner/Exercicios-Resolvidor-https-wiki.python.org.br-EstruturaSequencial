# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                       Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
# limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
# desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
# usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de
# pagamento, valor do desconto e valor a pagar.

corte = int(input('Informe o código do corte:\n1 - File duplo\n2 - Alcatra\n3 - Picanha\n- '))
if corte >= 1 and corte <= 3:
    if corte == 1:
        corte = 'File duplo'
        preco = 5.8
    elif corte == 2:
        corte = 'Alcatra'
        preco = 6.8
    else:
        corte = 'Picanha'
        preco = 7.8
    peso = float(input('Informe a quantidade desejada: '))
    if peso <= 5:
        preco = preco - 0.9
    else:
        preco = preco
    valor = preco * peso
    tabajara = int(input('Vai pagar com cartão tabajara:\n1 - Sim\n2 - Não\n- '))
    if tabajara >= 1 and tabajara <= 2:
        if tabajara == 1:
            desconto = valor * 0.05
            valorcomdesconto = valor - desconto
            fp = 'Cartão Tabajara'
        else:
            desconto = 0
            valorcomdesconto = valor
            fp = 'outra forma de pagamento'
        print(
            f'Cupom fiscal\n{corte}.....{peso}Kg.....Valor Unitario R$ {preco:.2f}\nValor total R$ {valor:.2f}.....Tipo de pagamento - '
            f'{fp}\nDesconto R$ -{desconto:.2f}\nValor a pagar{valorcomdesconto:.2f}')
    else:
        print('Forma de pagamento incorreta.')
else:
    print('Código incorreto')


