'''Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.'''
import math

raio = int(input('Digite o raio do círculo: \n'))
areadocirculo = math.pi * pow(raio,2)
print(f'A área do círculo é {areadocirculo:0.2f}')
