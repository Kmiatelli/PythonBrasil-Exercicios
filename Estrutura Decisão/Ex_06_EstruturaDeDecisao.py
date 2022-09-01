"""
Faça um Programa que leia três números e mostre o maior deles.
"""

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

maior = n1

if n2 > maior and n2 > n3:
    maior = n2
elif n3 > maior and n3 > n1:
    maior = n3

print(f'Maior número: {maior}')
