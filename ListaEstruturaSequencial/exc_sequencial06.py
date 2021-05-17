#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

def calcular_area_circulo(raio):
    areadocirculo = math.pi * pow(raio,2)
    print(f'A área do círculo é {areadocirculo:0.2f}')

if __name__ == "__main__":
    raio = int(input('Digite o raio do círculo: \n'))
    calcular_area_circulo(raio)