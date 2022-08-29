"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""

vetor = []

for count in range(1, 11):
    char = input('Digite um caracteres: ').upper()
    if char != 'A' and char != 'E' and char != 'I' and char != 'O' and char != 'U':
        vetor.append(char)
print(f'Quantidade de consoantes: {len(vetor)}\n'
      f'Consoantes: {vetor}')
