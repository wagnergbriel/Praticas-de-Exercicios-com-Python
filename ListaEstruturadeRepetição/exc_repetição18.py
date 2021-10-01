'''Faça um programa que, dado um conjunto de N números,
   determine o menor valor, o maior valor e a soma dos valores.'''
lista_de_numeros = [2, 4, 6, 9, 11]
soma_dos_numeros = 0
menor = min(lista_de_numeros)
maior = max(lista_de_numeros)
for numero in lista_de_numeros:
    soma_dos_numeros += numero
print(f'Menor numero: {menor}; Maior numero: {maior}; Soma dos numeros: {soma_dos_numeros}') 