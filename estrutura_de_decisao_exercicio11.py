# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para
# desenvolver o programa que calculará os reajustes.

# Faça o programa que recebe o salário do colaborador e o reajuste segundo o seguinte critério baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5%
# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = float(input('Informe o salário atual: '))
percentagem = 0
aumento = 0
if salario > 1500:
    percentagem = 0.05
    aumento = salario * percentagem
elif salario > 700 and salario <= 1500:
    percentagem = 0.1
    aumento = salario * percentagem
elif salario > 280 and salario <= 700:
    percentagem = 0.15
    aumento = salario * percentagem
elif salario <= 280:
    percentagem = 0.2
    aumento = salario * percentagem
print(f'Seu salário atual é R$ {salario:.2f}.\nO percentual de aumento aplicado será de {percentagem*100:.0f} %.'
      f'\nO valor do aumento é R$ {aumento:.2f}\nO novo sário será R$ {salario+aumento:.2f}')
