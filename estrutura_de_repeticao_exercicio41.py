# Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
# Os juros e a quantidade de parcelas seguem a tabela abaixo:
# Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
# 1       0%
# 3       10%
# 6       15%
# 9       20%
# 12      25%
# Exemplo de saída do programa:
# Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
# R$ 1.000,00     0               1                       R$  1.000,00
# R$ 1.100,00     100             3                       R$    366,00
# R$ 1.150,00     150             6                       R$    191,67

divida = float(input('Informe o valor da dívida: R$ '))
taxa = 5
parcela = 1
juro = divida*(taxa/100)
vlr_parc = juro + divida/parcela
vlr_div = 0
print('Valor da Dívida      Valor dos Juros     Quantidade de Parcelas      Valor da Parcela')
for c in range(0, 13, 3):
    if c == 0:
        taxa = 0
        parcela = 1
        juro = divida * (taxa / 100)
        vlr_div = divida + juro
        vlr_parc = vlr_div / parcela
        print(f'{vlr_div:<6.2f}                 {juro:<6.2f}                 {parcela}                           {vlr_parc:<6.2f}')
    else:
        taxa += 5
        parcela = c
        juro = divida * (taxa / 100)
        vlr_div = divida + juro
        vlr_parc = vlr_div / parcela
        print(f'{vlr_div:<6.2f}                 {juro:<6.2f}                 {parcela}                           {vlr_parc:>6.2f}')
        taxa +=5






