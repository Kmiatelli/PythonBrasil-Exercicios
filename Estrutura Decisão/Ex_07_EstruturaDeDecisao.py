"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
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

menor = n1

if n2 < menor and n2 < n3:
    menor = n2
elif n3 < menor and n3 < n1:
    menor = n3

print(f'Menor número: {menor}')

# Outra maneira mais fácil de se encontrar números maiores e menores utilizando a função max e min:

num = []

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

num.append(n1)
num.append(n2)
num.append(n3)

print('Maior número:', max(num))
print('Menor número:', min(num))
