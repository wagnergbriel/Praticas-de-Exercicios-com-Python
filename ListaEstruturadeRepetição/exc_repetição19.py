'''Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.'''
inicio = int(input('Digite o número que a contagem deve iniciar:\n'))
fim = int(input('Digite o número que a contagem deve terminar:\n'))
soma_dos_numeros = 0
for numero in range(inicio, fim):
    soma_dos_numeros += numero
print(f'Menor numero: {inicio}; Maior numero: {fim}; Soma dos numeros: {soma_dos_numeros}') 