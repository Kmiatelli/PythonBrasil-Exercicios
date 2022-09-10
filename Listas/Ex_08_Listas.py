"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida.
"""

idade = []
altura = []

for i in range(1, 6):
    print('%dº Pessoa' % i)
    num = int(input('Informe sua idade: '))
    idade.append(num)
    alt = float(input('Informe sua altura: '))
    altura.append(alt)
print('Ordem lida -> ' 'Idade:', idade, 'Altura:', altura)
print('Ordem inversa -> ' 'Idade:', idade[::-1], 'Altura:', altura[::-1])
