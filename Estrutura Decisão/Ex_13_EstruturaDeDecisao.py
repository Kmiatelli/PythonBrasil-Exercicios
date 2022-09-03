"""
Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""

while True:
    try:
        dia = int(input('Digite um número entre 1 e 6 ou 0 para sair: '))
    except ValueError:
        print('Letras não são aceitas.')
        continue
    if dia == 1:
        print('Hoje é Domingo')
    elif dia == 2:
        print('Hoje é Segunda-feira')
    elif dia == 3:
        print('Hoje é Terça-feira')
    elif dia == 4:
        print('Hoje é Quarta-feira')
    elif dia == 5:
        print('Hoje é Quinta-feira')
    elif dia == 6:
        print('Hoje é Sexta-feira')
    elif dia == 0:
        print('Encerrando o programa...')
        break
    else:
        print('Valor inválido!')
        continue

# Utilizei tratativa de exceções e laço while para treino, entretanto para a atividade proposta não há necessidade.
