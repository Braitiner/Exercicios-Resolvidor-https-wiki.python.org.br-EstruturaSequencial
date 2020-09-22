# Faça um programa que leia e valide as seguintes informações:
# a. Nome: maior que 3 caracteres;
# b. Idade: entre 0 e 150;
# c .Salário: maior que zero;
# d .Sexo: 'f' ou 'm';
# e .Estado Civil: 's', 'c', 'v', 'd';

print('='*10,'Faça seu Regitro','='*10)
nome = str(input('Nome: ')).strip()
while len(nome) < 3:
    nome = str(input('O nome deve ser maior que 3 caracteres.\nNome: ')).strip()
idade = int(input('Idade: '))
while idade < 0 or idade > 150:
    idade = int(input('A idade deve ser entre 0 e 150.\nIdade: '))
salario = float(input('Salário: R$ '))
while salario <= 0:
    salario = float(input('O salário deve ser maior que 0\nSalário: R$ '))
sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Opção invalida\nSexo: [M/F] ')).upper().strip()[0]
est_civ = str(input('Estado Civil\nSolterio......[S]\nCasado........[C]\nViúvo.........[V]\nDivorciado....[D]\n>> ')).upper().strip()[0]
while est_civ not in 'SCVD':
    est_civ = str(input('Opção invalida\nEstado Civil\nSolterio......[S]\nCasado........[C]\nViúvo.........['
                        'V]\nDivorciado....[D]\n>> ')).upper().strip()[0]




