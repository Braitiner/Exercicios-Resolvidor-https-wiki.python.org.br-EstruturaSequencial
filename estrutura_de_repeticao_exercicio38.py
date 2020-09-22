# Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
# a. Esse funcionário foi contratado em 2015, com salário inicial de R$ 1.000,00;
# b. Em 2016 recebeu aumento de 1,5% sobre seu salário inicial;
# c. A partir de 2017 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
#    Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo
#    que o usuário digite o salário inicial do funcionário.

from datetime import date
salario = float(input('Informe o salário: R$ '))
taxa = 1.5
for c in range(2016, date.today().year+1):
    salario += salario * (taxa/100)
    taxa *= 2
print(f'Sálario atual R${salario:.2f}')
