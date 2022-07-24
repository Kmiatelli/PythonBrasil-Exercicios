# Identificador

while True:
    registro = int(input('Digite o registro da lanchonete: '))
    if registro != 3553052:
        continue
    else:
        print('Bem vindo(a) a lanchonete elaborada pela Karina Miatelli Calaça Vieira')
        break

# Início do código
# Descrição do cardápio com os códigos para o cliente #
print('-' * 16, 'Cardápio', '-' * 16)
print('|Código|        Descrição        | Valor |')
print('|100|        Cachorro Quente     |  9,00 |')
print('|101|    Cachorro Quente Duplo   | 11,00 |')
print('|102|            X-Egg           | 12,00 |')
print('|103|           X-Salada         | 12,00 |')
print('|104|           X-Bacon          | 14,00 |')
print('|105|            X-Tudo          | 17,00 |')
print('|200|        Refrigerante Lata   |  5,00 |')
print('|201|          Chá Gelado        |  4,00 |')

total = 0  # Variável acumuladora

while True:  # Enquanto tudo o que estiver dentro do laço for verdadeiro o programa continua seguindo os passos #
    codigo = int(input('Entre com o código do produto desejado: '))  # Cliente entra com o código #
    if codigo == 100:
        valor = 9.00
        print('Você pediu um Cachorro Quente no valor de R$ 9,00')
    elif codigo == 101:
        valor = 11.00
        print('Você pediu um Cachorro Quente Duplo no valor de R$ 11,00')
    elif codigo == 102:
        valor = 12.00
        print('Você pediu um X-Egg no valor de R$ 12,00')
    elif codigo == 103:
        valor = 12.00
        print('Você pediu um X-Salada no valor de R$ 12,00')
    elif codigo == 104:
        valor = 14.00
        print('Você pediu um X-Bacon no valor de R$ 14,00')
    elif codigo == 105:
        valor = 17.00
        print('Você pediu um X-Tudo no valor de R$ 17,00')
    elif codigo == 200:
        valor = 5.00
        print('Você pediu um Refrigerante Lata no valor de R$ 5,00')
    elif codigo == 201:
        valor = 4.00
        print('Você pediu um Chá Gelado no valor de R$ 4,00')
    else:
        print('Você digitou uma opção inválida')
        continue  # Loop/ retorna ao início para que o cliente digite uma opção válida
    print('Deseja pedir mais alguma coisa? ')
    pedido = int(input('1' '-' 'Sim ' '\n'  # Espaço entre linhas
                       '2' '-' 'Não ''\n'))
    if pedido == 1:
        total += valor  # Acumula os valores ao longo das escolhas
        continue  # Loop/ retorna ao início para que o cliente faça mais escolhas
    else:
        print('Finalizando pedidos...')
        print('O total a ser pago é de: R$ %.2f' % (total + valor))
        break  # Para o loop e encerra o programa
