'''
Faça um programa para uma loja de tintas. 
O programa deverá pedir o metroquadrado em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

'''
import math

metroquadrado = int(input('Quantos m² você vai pintar ?\n'))
litros = metroquadrado / 3

if litros <= 18:
   print(f'Com {metroquadrado} m² será necessário uma lata de tinta, custa R$ 80.00')
  
else:
   latasdetinta = math.ceil(litros/18) #Essa função arrendonda o número para cima, o número mais próximo
   preco = latasdetinta * 80
   print(f'Com {metroquadrado} m² será necessário {latasdetinta} latas de tinta, custa R$ {preco:0.2f}')
