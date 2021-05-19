'''
Faça um programa que leia 5 números e informe o maior número
'''
BOOL = True
while BOOL:
    primeiro_numero = int(input('Digite o 1 número:\n'))
    segundo_numero = int(input('Digite o 2 número:\n'))
    terceiro_numero = int(input('Digite o 3 número:\n'))
    quarto_numero = int(input('Digite o 4 número:\n'))
    quinto_numero = int(input('Digite o 5 número:\n'))
    lista_de_numeros = [
        primeiro_numero,
        segundo_numero,
        terceiro_numero,
        quarto_numero,
        quinto_numero
    ]
    print(f'O maior número é {max(lista_de_numeros)}\n')
    BOOL = False
