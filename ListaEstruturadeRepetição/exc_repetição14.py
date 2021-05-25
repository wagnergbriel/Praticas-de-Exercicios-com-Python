'''
Faça um programa que peça 10 números inteiros,
calcule e mostre a quantidade de números pares e a quantidade de números impares.
'''
lista_de_numero = []
LIMITE = 1
ID = 0
while LIMITE <= 10:
    numero = int(input(f'{LIMITE}:Digite um numero:\n'))
    lista_de_numero.append(numero)
    LIMITE += 1
while range(ID, len(lista_de_numero)):
    paridade_do_numero = lista_de_numero[ID]
    if paridade_do_numero % 2 == 0:
        print(f'O número {paridade_do_numero} é par|', end='')
    else:
        print(f'O número {paridade_do_numero} é impar|', end='')
    ID += 1
