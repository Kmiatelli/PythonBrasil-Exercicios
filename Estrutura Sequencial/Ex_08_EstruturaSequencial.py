"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""

ganho = float(input('Digite quanto ganha por hora: '))
nHoras = float(input('Digite as horas trabalhadas no mês: '))

salario = ganho * nHoras

print(f'Seu salário nesse mês é de: {salario}')
