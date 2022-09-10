"""
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""

vetor = []
soma = 0
mult = 1

for i in range(5):
    n = int(input('Digite um número inteiro: '))
    vetor.append(n)

for elementos in vetor:
    soma += elementos
    mult *= elementos

print(f'Números: {vetor}\n'
      f'Soma: {soma}\n'
      f'Multiplicação: {mult}')




