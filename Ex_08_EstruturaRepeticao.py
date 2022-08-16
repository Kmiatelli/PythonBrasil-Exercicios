"""
Faça um programa que leia 5 números e informe a soma e a média dos números.
"""

num = []
soma = 0
media = 0

for i in range(0, 5):
    n = int(input('Digite um número: '))
    num.append(n)
    soma = sum(num)
    media = soma/5

print(f'Números digitados: {num} \n'
      f'Soma dos números: {soma} \n'
      f'Média: {media}')
