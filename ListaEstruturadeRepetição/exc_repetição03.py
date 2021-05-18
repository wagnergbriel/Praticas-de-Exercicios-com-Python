'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''
BOOL = True
while BOOL:
    nome = input('Qual é o seu nome ?\n')
    idade = int(input('Qual a sua idade ?\n'))
    salario = float(input('Qual é o seu salário ?\n'))
    sexo = input('Qual é o seu sexo ?\n')
    estado_civil = input('Qual é o seu estado civil ?\n')
    opcao_sexo = ['F', 'M', 'f', 'm']
    opcao_estado_civil = ['s', 'c', 'v', 'd', 'S', 'C', 'V', 'D']
    limite_idade = lambda i: idade > 0 and idade <= 150
    if len(nome) > 3 and\
        limite_idade(idade) and\
        sexo in opcao_sexo and\
        estado_civil in opcao_estado_civil:
        print('As informações são validas !')
        BOOL = False
    else:
        print('As informações não são validas !\n')
        BOOL = True
