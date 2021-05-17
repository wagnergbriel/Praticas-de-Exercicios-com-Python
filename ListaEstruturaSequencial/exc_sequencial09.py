'''Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).'''

def convercao_de_temperatura(tempfahrenheit):
    celsius = 5 *  ((tempfahrenheit-32) / 9)
    print(f'Em Fahrenheit {tempfahrenheit}°F; em Celsius é {celsius:0.1f}°C')

if __name__ == "__main__":
    fahrenheit = int(input('Digite a temperatura em Fahrenheit:\n'))
    convercao_de_temperatura(fahrenheit)