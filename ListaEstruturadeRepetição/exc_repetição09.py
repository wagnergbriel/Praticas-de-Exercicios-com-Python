'''
Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
'''
NUMERO_IMPAR = 0
while NUMERO_IMPAR < 50:
    NUMERO_IMPAR += 1
    if NUMERO_IMPAR % 2 != 0:
        print(NUMERO_IMPAR)
