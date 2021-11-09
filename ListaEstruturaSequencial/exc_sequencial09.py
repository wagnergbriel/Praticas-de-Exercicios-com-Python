'''
    Faça um Programa que peça a temperatura em graus Fahrenheit, 
    transforme e mostre a temperatura em graus Celsius.
    C = 5 * ((F-32) / 9).
'''

fahrenheit = int(input('Digite a temperatura em Fahrenheit:\n'))
celsius = 5 *  ((fahrenheit-32) / 9)
print(f'Em Fahrenheit {fahrenheit}°F; em Celsius é {celsius:0.1f}°C')