"""""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';

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
                    'S - solteiro,\n'
                    'C - casado,\n'
                    'V - viúvo,\n'
                    'D - divorciado\n').upper()
while (estadoCivil != 'S') and (estadoCivil != 'C') and (estadoCivil != 'V') and (estadoCivil != 'D'):
    estadoCivil = input("Estado civil inválido, digite novamente: ")

print(f'Nome: {nome}\n'
      f'Idade: {idade}\n'
      f'Salário: {salario}\n'
      f'Sexo: {sexo}\n'
      f'Estado Civil: {estadoCivil}')
