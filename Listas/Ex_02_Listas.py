"""
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""

vetor = []

for i in range(0, 10):
    n = int(input('Digite um número: '))
    vetor.append(n)
vetor.reverse()
print(vetor)
#  print(vetor[::-1]) - outra opção de reversão

