"""
Altere o programa anterior permitindo que o usuário digite o salário inicial do funcionário.
"""

ano_inicial = 1996
aumento = 15

while True:
    salarioInicial = float(input('Informe o salário inicial do funcionário: '))
    ano_atual = int(input('Digite o ano em que estamos: '))

    if ano_atual > ano_inicial:
        aumento_atual = (ano_atual - ano_inicial) * aumento * 2
        salarioAtual = salarioInicial + aumento_atual
        print(f'No ano de {ano_atual} o aumento será de R$%.2f\n'
              f'O salário atual é de R$%.2f' % (aumento_atual, salarioAtual))

    elif ano_atual == ano_inicial:
        print(f'No ano de {ano_inicial}, o aumento foi de R$%.2f\n'
              f'O salário atual é de R$%.2f' % (aumento, salarioInicial + aumento))
    else:
        if ano_atual < ano_inicial:
            print('Não há informações na base de dados para esse ano. Faça nova consulta.')
            continue

    consulta = input('Deseja fazer nova consulta? S - Sim/ N - Não.\n'
                     '-> ').upper()
    if consulta == 'S':
        continue
    else:
        print('Encerrando programa...')
        break

