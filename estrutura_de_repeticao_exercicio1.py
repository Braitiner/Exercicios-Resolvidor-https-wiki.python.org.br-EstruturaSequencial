# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue
# pedindo até que o usuário informe um valor válido.

n = int(input('Informe uma nota entre 0 e 10: '))
while n < 0 or n > 10:
    n = int(input('Valor incorreto, informe uma nota entre 0 e 10: '))
print(f'A nota informada foi {n}')
