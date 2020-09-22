# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a
# população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o
# número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as
# taxas de crescimento.

pais_a = 80000
pais_b = 200000
anos = 0
while pais_a <= pais_b:
    pais_a *= 1.03
    print(f'Pais a {pais_a:.0f}')
    pais_b *= 1.015
    print(f'Pais B {pais_b:.0f}')
    anos += 1
print(f'O pais A vai demorar {anos} para igualar sua população com o pais B')


