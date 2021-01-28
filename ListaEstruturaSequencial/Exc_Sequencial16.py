'''
Faça um programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

'''
import math

def calcular_medida_de_tinta(tamanho:int):
  litros = tamanho / 3

  if litros <= 18:
     print(f'Com {tamanho} m² será necessário uma lata de tinta, custa R$ 80.00')
  
  else:
     latasdetinta = math.ceil(litros/18) #Essa função arrendonda o número para cima, o número mais próximo
     preco = latasdetinta * 80
     print(f'Com {tamanho} m² será necessário {latasdetinta} latas de tinta, custa R$ {preco:0.2f}')

if __name__ == "__main__":
    metroquadrado = int(input('Quantos m² você vai pintar ?\n'))
    calcular_medida_de_tinta(metroquadrado)