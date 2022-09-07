"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto
de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças
adquiridas e escreva o valor a ser pago pelo cliente.
"""


kgMorangos = float(input('Quantidade de morangos em kg: '))
kgMacas = float(input('Quantidade de maçãs em kg: '))

if kgMorangos <= 5:
    precoMorango = kgMorangos * 2.50
else:
    precoMorango = kgMorangos * 2.20

if kgMacas <= 5:
    precoMaca = kgMacas * 1.80
else:
    precoMaca = kgMacas * 1.50

precoTotal = precoMorango + precoMaca
kgTotal = kgMorangos + kgMacas
desconto = precoTotal * 0.10
precoDesconto = precoTotal - desconto


print('Preço morangos: R$%.2f \n'
      'Preço maçãs: R$%.2f \n'
      'Quantidade total em kg: %.1f \n'
      'Preço total: R$%.2f \n' % (precoMorango, precoMaca, kgTotal, precoTotal))

if kgTotal > 8 or precoTotal > 25:
    print('Desconto de 10% concedido!')
    print('Preço com desconto: R$%.2f' % precoDesconto)









