# Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da
# turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média
# calculada.

soma = cont = media = 0
while True:
    idade = int(input('Informe a idade ou -1 para sair:  '))
    soma += idade
    cont += 1
    media = soma / cont
    if idade == -1:
        break
if media < 26:
    print(f'A média de idade é {media:.2f}, a turma é jovem.')
elif media < 60:
    print(f'A m´dia de idade é {media:.2f}, a turma é adulta.')
else:
    print(f'A média de idade é {media:.2f}, a turma é idosa.')






