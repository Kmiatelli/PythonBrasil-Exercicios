"""""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';

"""

"""

estadoCivil = input('Estado civil: \n'
                    's - solteiro,\n'
                    'c - casado,\n'
                    'v - viúvo,\n'
                    'd - divorciado\n')
"""


nome = input('Digite um nome: ').title()
while len(nome) <= 3:
    nome = input('Campo "nome" deve conter mais de 03 caracteres: ')

idade = int(input('Digite uma idade: '))
while idade < 0 or idade > 150:
    idade = int(input('Idade inválida! Digite novamente: '))

salario = float(input('Salário: '))
while salario <= 0:
    salario = float(input('Digite um salário válido:  '))

sexo = input('Sexo: F - Feminino\n'
             'M - Masculino\n').upper()
while sexo != 'F' and sexo != 'M':
    sexo = input('Digite um caractere válido: ').upper()

estadoCivil = input('Estado civil: \n'
                    's - solteiro,\n'
                    'c - casado,\n'
                    'v - viúvo,\n'
                    'd - divorciado\n')
while (estadoCivil != 's') and (estadoCivil != 'c') and (estadoCivil != 'v') and (estadoCivil != 'd'):
    estadoCivil = input("Estado civil inválido, digite novamente: ")
