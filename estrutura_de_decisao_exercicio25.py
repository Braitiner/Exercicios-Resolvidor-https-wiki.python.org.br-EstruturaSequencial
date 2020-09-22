# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder
# positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como  "Cúmplice" e 5 como
# "Assassino". Caso contrário, ele será classificado como "Inocente".

print('Telefonou para a vítima?')
p1 = int(input('Digite 1 para sim.\nDigite 2 para não.\n'))
if p1 >=1 and p1 <= 2:
    print('Esteve no local do crime?')
    p2 = int(input('Digite 1 para sim.\nDigite 2 para não.\n'))
    if p2 >=1 and p2 <= 2:
        print('Mora perto da vítima?')
        p3 = int(input('Digite 1 para sim.\nDigite 2 para não.\n'))
        if p3 >= 1 and p3 <= 2:
            print('Devia para a vítima?')
            p4 = int(input('Digite 1 para sim.\nDigite 2 para não.\n'))
            if p4 >= 1 and p4 <= 2:
                print('Já trabalhou com a vítima?')
                p5 = int(input('Digite 1 para sim.\nDigite 2 para não.\n'))
                if p5 >= 1 and p5 <= 2:
                    sim = 0
                    if p1 == 1:
                        sim = sim + 1
                    if p2 == 1:
                        sim = sim + 1
                    if p3 == 1:
                        sim = sim + 1
                    if p4 == 1:
                        sim = sim + 1
                    if p5 == 1:
                        sim = sim + 1
                    if sim == 5:
                        print('Assassino')
                    elif sim >= 3:
                        print('Cumplice')
                    elif sim >= 2:
                        print('Suspeito')
                    else:
                        print('Inocente')
                else:
                    print('Favor informar 1 para sim ou 2 para não')
            else:
                print('Favor informar 1 para sim ou 2 para não')
        else:
            print('Favor informar 1 para sim ou 2 para não')
    else:
        print('Favor informar 1 para sim ou 2 para não')
else:
    print('Favor informar 1 para sim ou 2 para não')







