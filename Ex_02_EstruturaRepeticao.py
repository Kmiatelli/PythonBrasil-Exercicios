"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
"""

nome_user = input('Digite um nome de usuário: ')
senha = input('Digite uma senha: ')
while senha == nome_user:
    print('A senha não pode ser igual ao nome de usuário, por favor escolha outra: ')
    senha = input('Digite uma senha: ')
else:
    print('Acesso concedido!')
