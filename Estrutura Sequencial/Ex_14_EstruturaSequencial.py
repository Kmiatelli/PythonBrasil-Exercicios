"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca
do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e
na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
"""

pesoPeixes = float(input('Digite o peso dos peixes: '))

if pesoPeixes > 50:
    excesso = pesoPeixes - 50
    multa = excesso * 4.00

    print('Peso excedente: %.1fkg. \n'
          'Valor da multa a ser paga: %.1f reais.' % (excesso, multa))

else:
    print('Você não excedeu o limite de peso estabelecido.')
