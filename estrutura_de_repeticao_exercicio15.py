# A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até
# o n−ésimo termo.

print('Serie de Fibonacci')
n = int(input('Informe quantos termos deseja visualizar: '))
termo = 1
f1 = 0
f2 = 0
for c in range(n):
    if c == n-1:
        print(termo, end='')
        f2 = f1
        f1 = termo
        termo = f1 + f2
    else:
        print(termo, end=' ⇒ ')
        f2 = f1
        f1 = termo
        termo = f1 + f2


