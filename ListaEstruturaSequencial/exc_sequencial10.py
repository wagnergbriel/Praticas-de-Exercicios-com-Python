'''
    Faça um Programa que peça a temperatura em graus Celsius, 
    transforme e mostre em graus Fahrenheit.
'''

celsius = int(input('Digite a temperatura em Celsius:\n'))
fahrenheit = 32 + ((celsius*9) / 5)
print(f'Em Fahrenheit {fahrenheit}°F; em Celsius é {celsius:0.1f}°C')
