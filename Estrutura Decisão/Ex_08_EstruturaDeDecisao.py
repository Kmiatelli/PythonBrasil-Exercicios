"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é
sempre pelo mais barato.
"""

p1 = float(input('Digite o preço do primeiro produto: '))
p2 = float(input('Digite o preço do segundo produto: '))
p3 = float(input('Digite o preço do terceiro produto: '))

barato = p1

if p2 < barato and p2 < p3:
    barato = p2
elif p3 < barato and p3 < p1:
    barato = p3

print(f'Você deverá levar o produto no valor de: R${barato}')

