"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

while True:
    letra = input('Digite uma letra ou um número para sair: ').lower()
    if letra.isnumeric():
        print('Encerrando programa...')
        break
    elif letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        print('A letra digitada é uma vogal')
    elif letra != 'a' or letra != 'e' or letra != 'i' or letra != 'o' or letra != 'u':
        print('A letra digitada é uma consoante')
