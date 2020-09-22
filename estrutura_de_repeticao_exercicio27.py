# Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade
# de alunos para cada turma. As turmas não podem ter mais de 40 alunos.

turmas = int(input('Informe a quantidade de turmas: '))
soma = media = 0
for c in range(1, turmas+1):
    alunos = int(input(f'Informe a quantidade de alunos da turma {c}: '))
    while alunos < 0 or alunos > 40:
        alunos = int(input(f'AVISO quantidade deve ser enre 0 e 40. Informe a quantidade de alunos da turma {c}'))
    soma += alunos
media = soma/turmas
print(f'A média de alunos por turma é de {media:.2f}')
