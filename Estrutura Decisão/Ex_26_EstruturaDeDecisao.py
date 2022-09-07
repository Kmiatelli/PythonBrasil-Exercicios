"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
a) Álcool:
- até 20 litros, desconto de 3% por litro
- acima de 20 litros, desconto de 5% por litro
b) Gasolina:
- até 20 litros, desconto de 4% por litro
- acima de 20 litros, desconto de 6% por litro.
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
(codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente
sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

litros = float(input('Com quantos litros deseja abastecer?\n'
                     '-> '))
combustivel = input('Escolha o tipo de combustível:\n'
                    '"A" - Álcool\n'
                    '"G" - Gasolina\n'
                    '-> ').upper()

if combustivel == 'A':
    preco = litros * 1.90
    if litros <= 20:
        desconto = preco * 0.03
    else:
        desconto = preco * 0.05

if combustivel == 'G':
    preco = litros * 2.50
    if litros <= 20:
        desconto = preco * 0.04
    else:
        desconto = preco * 0.06

valor_desconto = preco - desconto  # Preço final após desconto concedido

print(f'Valor a pagar: R${valor_desconto}')
