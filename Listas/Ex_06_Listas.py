"""
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0.
"""

listaMedia = []

for aluno in range(1, 4):
    soma = 0

    print('Aluno: ', aluno)
    for n in range(1, 5):
        soma += float(input('Digite sua nota: '))

    media = soma / 4
    print('Média aluno: %.1f' % media)
    print('\n')

    if media >= 7:
        listaMedia.append(media)
print(f'Quantidade de alunos com nota acima da média: {len(listaMedia)}')


