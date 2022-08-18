"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""

temp = float(input('Informe a temperatura atual em Fahrenheit: '))
c = 5 * ((temp-32)/9)
print('%.2fº Fahrenheit equivale a %.2fº Celsius.' % (temp, c))
