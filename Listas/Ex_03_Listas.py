"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""

notas = []
n = 0
soma = 0

for i in range(1, 5):
    n = float(input('Nota: '))
    i += 1
    notas.append(n)
for elemento in notas:
    soma += elemento
    media = soma / 4
print(f'Notas: {notas}\n'
      f'Média: {media}')
