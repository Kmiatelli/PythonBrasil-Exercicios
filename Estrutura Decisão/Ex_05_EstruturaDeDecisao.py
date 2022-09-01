"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno
e apresentar:
- A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
- A mensagem "Reprovado", se a média for menor do que sete;
- A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

n = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n + n2) / 2

if media == 10:
    print('Aprovado com Distinção!')
elif 7 <= media < 10:
    print('APROVADO')
elif media < 7:
    print('REPROVADO')
