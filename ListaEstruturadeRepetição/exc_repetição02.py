'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual
ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''
BOOL = True
while BOOL:
    usuario = input('Digite o nome de usuário:\n')
    senha = input('Digite sua senha:\n')
    if usuario == senha:
        print('Dados incorretos, digite - os novamente !\n')
    else:
        print('Registrado com Sucesso !')
        BOOL = False
