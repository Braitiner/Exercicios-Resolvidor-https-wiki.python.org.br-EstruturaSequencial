# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
# formula para calcular o circulo é PI*R²
#Limitar a quantidade de casas decimais no print usei o comando :.2F


raio =float(input('Informe o raio do circulo: '))
pi = 3.14159265359
print('A área do círculo é {:.2f}.'.format(pi*raio**2))


