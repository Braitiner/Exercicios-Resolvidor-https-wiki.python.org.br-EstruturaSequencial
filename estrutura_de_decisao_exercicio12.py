# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 11% INSS e que o FGTS corresponde a 8% do Salário
# Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos
# os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20%
# Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00

salario = float(input('Qual o valor da hora trabalhada: '))
hora = float(input('Quantas horas trabalhadas: '))
bruto = salario * hora
inss = 0.11
fgts = 0.08
ir = 0
if bruto > 2500:
    ir = 0.2
elif bruto > 1500:
    ir = 0.1
elif bruto > 900:
    ir = 0.05
elif bruto <= 900:
    ir = 0

print(f' Holerite'
      f'\nSalário Bruto: ({salario} * {hora})    : R$ {bruto:>6.2f}'
      f'\n(-) IR ({ir*100:.0f}%)                      : R$ {ir*bruto:>6.2f}'
      f'\n(-) INSS ({inss*100:.0f}%)                   : R$ {inss*bruto:>6.2f}'
      f'\nFGTS ({fgts*100}%)                      : R$ {fgts*bruto:6.2f}'
      f'\nTotal de descontos               : R$ {(ir*bruto)+(inss*bruto):6.2f}'
      f'\nSalário liquido                  : R$ {bruto - (ir*bruto+inss*bruto):6.2f}')

