# Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno
# e presentar:
# A - A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
# B - A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
# C - A mensagem "Aprovado com Distinção", se a média for igual a 10.

n1 = float(input('Informe a primeira nota: '))
if n1 >= 0 and n1 <= 10:
    n2 = float(input('Informe a segunda nota: '))
    if n2 >= 0 and n2 <= 10:
        n3 = float(input('Informe a terceura nota: '))
        if n3 >= 0 and n3 <= 10:
            media = (n1 + n2 + n3) / 3
            if media == 10:
                print(f'Aprovado com Distinção, média {media:.2f}')
            elif media >= 7:
                print(f'Aprovado, média {media:.2f}')
            else:
                print(f'Reprovado {media:.2f}')
        else:
            print(' Terceira nota Incorreta')

    else:
        print('segunda nota incorreta')
else:
    print('Primeira nota incorreta')

