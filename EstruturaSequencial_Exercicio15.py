# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
# total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
# para o sindicato, faça um programa que nos dê:
# a. salário bruto.
# b. quanto pagou ao INSS.
# c. quanto pagou ao sindicato.
# d. o salário líquido.
# e. calcule os descontos e o salário líquido, conforme a tabela abaixo:

# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

vlhora = float(input('Informe o valor da sua hora de trabalho: '))
horas = float(input('Informe o total de horas trabalhadas no mês: '))
salario = vlhora*horas
ir = salario*0.11
inss = salario*0.08
sind = salario*0.05
liq = salario-(ir+inss+sind)

print('+ Salário Bruto: R$ {salario}'
      '\n- IR (11%): R${ir}'
      '\n- INSS (8%): R${inss}'
      '\n- Sindicato (5%): R${sind}'
      '\nSalário Liquido: R${liq}'.format(salario=salario,ir=ir,inss=inss,sind=sind,liq=liq))
