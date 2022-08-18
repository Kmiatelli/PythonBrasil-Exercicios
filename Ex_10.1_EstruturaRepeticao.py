"""
Altere o programa anterior para mostrar no final a soma dos números.
"""

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

intervalo = []

for i in range(n1 + 1, n2):
    intervalo.append(i)
    print(i)
soma = sum(intervalo)

for r in range(n2 + 1, n1):
    intervalo.append(r)
    print(r)
soma = sum(intervalo)

print(f'Soma intervalo: {soma}')
