'''
Altere o programa anterior para mostrar no final a soma dos números.
'''
primeiro_numero = int(input('Digite o 1 numero:\n'))
segundo_numero = int(input('Digite o 2 numero:\n'))
aux = primeiro_numero
limite = segundo_numero - 1
SOMA = 0
if primeiro_numero < segundo_numero:
    print(f'Os números entre {primeiro_numero} e {segundo_numero}:', end=" ")
    while aux < limite:
        aux += 1
        SOMA += aux
        print(f'{aux}', end=" ")
    print(f'\nA soma dos numeros é {SOMA}\n')
