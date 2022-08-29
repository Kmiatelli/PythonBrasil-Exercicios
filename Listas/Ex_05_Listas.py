"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
"""

num = []
par = []
impar = []


for i in range(1, 21):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        i += 1
        par.append(n)
        num.append(n)
    else:
        impar.append(n)
        num.append(n)
print(f'Números recebidos: {num}\n'
      f'Números pares: {par}\n'
      f'Números ímpares: {impar}')



