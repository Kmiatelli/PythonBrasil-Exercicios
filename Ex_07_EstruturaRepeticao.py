"""
Faça um programa que leia 5 números e informe o maior número.
"""


num = []

for i in range(0, 5):
    n = int(input(f'Digite um número: '))
    num.append(n)
    print(max(num))




