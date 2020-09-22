# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor
# votar e ao final mostrar o número de votos de cada candidato.

eleitores = int(input('Informe o total de eleitores: '))
c_1 = c_2 = c_3 = 0

for c in range(0, eleitores):
    cand = str(input('[A] - Jurema\n[B] - Gutemberg\n[C] - Bartolomeu\n>> ')).strip().upper()[0]
    while cand not in 'ABC':
        cand = str(input('AVISO escolha uma das opções: A, B ou C\n[A] - Jurema\n[B] - Gutemberg\n[C] - Bartolomeu\n >>')).strip().upper()[0]
    if cand == 'A':
        c_1 += 1
    elif cand == 'B':
        c_2 += 1
    elif cand == 'C':
        c_3 += 1
print(f'Jurema {c_1} Votos\nGutemberg {c_2} votos\nBartolomeu {c_3} votos.')



