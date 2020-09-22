# A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que
# o valor seja maior que 500.

termo = 1
f1= f2 = 0
while termo <= 610: # O laço está até 610 porque é o proximo número depois de 500 na sequencia de Fibonacci.
    if termo == 610:
        print(termo,end='')
        f2 = f1
        f1 = termo
        termo = f1 + f2
    else:
        print(termo, end=' ↠ ')
        f2 = f1
        f1 = termo
        termo = f1 + f2
