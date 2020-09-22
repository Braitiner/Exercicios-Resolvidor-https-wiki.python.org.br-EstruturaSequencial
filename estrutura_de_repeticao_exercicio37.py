# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais
# magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e
# seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o
# programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais
# magro, além da média das alturas e dos pesos dos clientes.

cod = int(input('Código cliente: '))
altura = float(input('Informe a altura: '))
peso = float(input('Informe o peso: '))
alt_maior = alt_menor = altura
cod_alt_maior = cod_alt_menor = cod_peso_maior = cod_peso_menor = cod
peso_maior = peso_menor = peso
soma_alt = soma_peso = cont = 0
while True:
    soma_alt += altura
    soma_peso += peso
    cont += 1
    if alt_maior < altura:
        alt_maior = altura
        cod_alt_maior = cod
    if alt_menor > altura:
        alt_menor = altura
        cod_alt_menor = cod
    if peso_maior < peso:
        peso_maior = peso
        cod_peso_maior = cod
    if peso_menor > peso:
        peso_menor = peso
        cod_peso_menor = cod
    cod = int(input('Código cliente ou 0 para sair: '))
    if cod == 0:
        break
    altura = float(input('Informe a altura: '))
    peso = float(input('Informe o peso: '))
print(f'''O cliete mais alto é {cod_alt_maior} e tem {alt_maior} de altura.
O cliente mais baixo é {cod_alt_menor} e tem {alt_menor} de altura
O cliente mais pesado é {cod_peso_maior} com {peso_maior} kilos
o cliente mais magro é {cod_peso_menor} com {peso_menor} kilos
A altura média é de {soma_alt/cont:.2f} e o peso médio é {soma_peso/cont:.2f}''')

