"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""

s = 1
n = 0

total_s = 0


print('Faremos algumas perguntas. Responda 1 para SIM ou 0 para NÃO.')

telefonou = int(input('Telefonou para vítima?\n'
                      '-> '))
if telefonou == 1:
    total_s += 1

local = int(input('Esteve no local do crime?\n'
                  '-> '))
if local == 1:
    total_s += 1

moradia = int(input('Mora perto da vítima?\n'
                    '-> '))
if moradia == 1:
    total_s += 1

devendo = int(input('Devia para a vítima?\n'
                    '-> '))
if devendo == 1:
    total_s += 1

trabalho = int(input('Já trabalhou com a vítima?\n'
                     '-> '))
if trabalho == 1:
    total_s += 1

if total_s == 2:
    print('Classificação: Suspeita!')
elif 3 <= total_s <= 4:
    print('Classificação: Cúmplice!')
elif total_s == 5:
    print('Classificação: Assassino!')
else:
    print('Classificação: Inocente!')
