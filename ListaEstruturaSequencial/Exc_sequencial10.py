# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

def convercao_de_temperatura(tempcelsius):
    fahrenheit = 32 + ((tempcelsius*9) / 5)
    print(f'Em Fahrenheit {fahrenheit}°F; em Celsius é {tempcelsius:0.1f}°C')

if __name__ == "__main__":
    Celsius = int(input('Digite a temperatura em Celsius:\n'))
    convercao_de_temperatura(Celsius)