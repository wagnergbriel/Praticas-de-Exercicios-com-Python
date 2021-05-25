'''
Faça um programa que peça dois números, base e expoente, calcule e mostre o
primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
'''
while True:
    primeiro_numero = int(input('Digite a base da potencia:\n'))
    segundo_numero = int(input('Digite o expoente da potencia:\n'))
    potencia = primeiro_numero ** segundo_numero
    print(f'O resultado da potencia é {potencia}')
