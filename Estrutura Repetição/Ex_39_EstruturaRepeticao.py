"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo
representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo.
Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
"""

maior_altura = 0
menor_altura = 2.00
numero_aluno_alto = 0
numero_aluno_baixo = 0

for i in range(1, 11):
    altura = float(input(f'Aluno {i}, informe sua altura: '))

    if altura > maior_altura:
        numero_aluno_alto = i
        maior_altura = altura

    if altura < menor_altura:
        numero_aluno_baixo = i
        menor_altura = altura

print(f'O aluno mais alto é o número {numero_aluno_alto} com {maior_altura}\n'
      f'O aluno mais baixo é o número {numero_aluno_baixo} com {menor_altura}')
















