"""
Faça um Programa que peça dois números e imprima o maior deles.
"""

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print('Maior número:', n1)
elif n2 > n1:
    print('Maior número:', n2)
else:
    if n1 == n2:
        print('Números iguais')