"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
a) Para homens: (72.7*h) - 58
b) Para mulheres: (62.1*h) - 44.7
"""

h = float(input('Digite sua altura: '))
pesoIdealH = (72.7 * h) - 58
pesoIdealM = (62.1 * h) - 44.7

print('Peso ideal homens: %.1f \n'
      'Peso ideal mulheres: %.1f' % (pesoIdealH, pesoIdealM))

