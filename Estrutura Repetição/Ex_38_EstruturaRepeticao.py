"""
Um funcionário de uma empresa recebe aumento salarial anualmente:
Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário.
"""

ano_inicial = 1996
aumento = 15
salarioInicial = 1000

while True:
    ano_atual = int(input('Digite o ano que deseja saber o salário: '))

    if ano_atual > ano_inicial:
        aumento_atual = (ano_atual - ano_inicial) * aumento * 2
        salarioAtual = salarioInicial + aumento_atual
        print(f'No ano de {ano_atual} o aumento é de R$%.2f\n'
              f'O salário atual é de R$%.2f' % (aumento_atual, salarioAtual))

    elif ano_atual == ano_inicial:
        print(f'No ano de {ano_inicial}, o aumento é de R$%.2f\n'
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

















