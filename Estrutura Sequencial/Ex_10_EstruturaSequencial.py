"""
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""

celsius = float(input('Informe a temperatura atual em graus Celsius: '))
temp = celsius * 1.8 + 32
print('%.2fº Celsius equivale a %.2fº Fahrenheit.' % (celsius, temp))


