'''
Faça um programa que receba dois números inteiros e
gere os números inteiros que estão no intervalo compreendido por eles.
'''
primeiro_numero = int(input('Digite o 1 numero:\n'))
segundo_numero = int(input('Digite o 2 numero:\n'))
aux = primeiro_numero
if primeiro_numero < segundo_numero:
    print(f'Os números entre {primeiro_numero} e {segundo_numero}:', end=" ")
    while aux < segundo_numero:
        aux += 1
        print(f'{aux}', end=" ")
