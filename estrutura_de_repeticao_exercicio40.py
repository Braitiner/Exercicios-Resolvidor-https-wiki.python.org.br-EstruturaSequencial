# Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos
# os seguintes dados:
# a. Código da cidade;
# b. Número de veículos de passeio (em 2001);
# c. Número de acidentes de trânsito com vítimas (em 2001). Deseja-se saber:
# d .Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# e .Qual a média de veículos nas cinco cidades juntas;
# f. Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

cod_cidade = int(input('Código da cidade: '))
veiculos = int(input('Números de veículos: '))
acidentes = int(input('Acidentes com vitimas: '))
indice = acidentes / veiculos
maior_ind = menor_ind = indice
cod_maior = cod_menor = cod_cidade
soma = soma_acid = cont =0
for c in range(1, 5):
    soma += veiculos
    cod_cidade = int(input('Código da cidade: '))
    veiculos = int(input('Números de veículos: '))
    acidentes = int(input('Acidentes com vitimas: '))
    indice = acidentes / veiculos
    if maior_ind < indice:
        maior_ind = indice
        cod_maior = cod_cidade
    if menor_ind > indice:
        menor_ind = indice
        cod_menor = cod_cidade
    if veiculos < 2000:
        soma_acid += acidentes
        cont +=1
print(f'''Cidade {cod_maior}, com maior indece de acidentes{maior_ind:.2f}
Cidade {cod_menor} com menor indide de acidentes {menor_ind:.2f}
A média de veiculos das 5 cidades é de {soma/5:.2f}
A média de acidentes nas cidades com menos de 2000 veículos é {soma_acid/cont:.2f}''')




