# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao
# aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a
# nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro
# aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
# a. Maior e Menor Acerto;
# b. Total de Alunos que utilizaram o sistema;
# c. A Média das Notas da Turma



print('Informe o gabarito da prova:')
p1 = str(input('01: ')).strip().upper()[0]
p2 = str(input('02: ')).strip().upper()[0]
p3 = str(input('03: ')).strip().upper()[0]
p4 = str(input('04: ')).strip().upper()[0]
p5 = str(input('05: ')).strip().upper()[0]
p6 = str(input('06: ')).strip().upper()[0]
p7 = str(input('07: ')).strip().upper()[0]
p8 = str(input('08: ')).strip().upper()[0]
p9 = str(input('09: ')).strip().upper()[0]
p10 = str(input('10: ')).strip().upper()[0]
cont = soma = maior = 0
menor = 11
while True:
    r1 = r2 = r3 = r4 = r5 = r6 = r7 = r8 = r9 = r10 = ''
    for c in range(1, 11):
        print(f'Questão {c}')
        alternativa = str(input('Alternativa:\n[A]\n[B]\n[C]\n[D]\n[E]\n>> ')).strip().upper()[0]
        while alternativa not in 'ABCDE':
            print('AVISO - alternativa invalida.')
            alternativa = str(input('Alternativa:\n[A]\n[B]\n[C]\n[D]\n[E]\n>> ')).strip().upper()[0]
        if c == 1:
            r1 = alternativa
        if c == 2:
            r2 = alternativa
        if c == 3:
            r3 = alternativa
        if c == 4:
            r4 = alternativa
        if c == 5:
            r5 = alternativa
        if c == 6:
            r6 = alternativa
        if c == 7:
            r7 = alternativa
        if c == 8:
            r8 = alternativa
        if c == 9:
            r9 = alternativa
        if c == 10:
            r10 = alternativa
    acertos = 0
    if r1 == p1:
        acertos += 1
    if r2 == p2:
        acertos += 1
    if r3 == p3:
        acertos += 1
    if r4 == p4:
        acertos += 1
    if r5 == p5:
        acertos += 1
    if r6 == p6:
        acertos += 1
    if r7 == p7:
        acertos += 1
    if r8 == p8:
        acertos += 1
    if r9 == p9:
        acertos += 1
    if r10 == p10:
        acertos += 1
    print(acertos)
    cont += 1
    soma += acertos
    sair = str(input('Deseja realizar um novo lançamento: [S/N]')).strip().upper()[0]
    while sair not in 'SN':
        print('AVISO - Escolha S para sim e N para não.')
        sair = str(input('Deseja realizar um novo lançamento: [S/N]')).strip().upper()[0]
    if sair == 'N':
        break
if maior < acertos:
    maior = acertos
if menor > acertos:
    menor = acertos
print(f'Total de avaliações {cont}\nMaior nota {maior}\nMenor nota {menor}\nNota média {soma/cont:.2f}')
