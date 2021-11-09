'''
Faça um Programa para uma loja de tintas. 
O programa deverá pedir o metroquadrado em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados 
    e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, 
    que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

a - comprar apenas latas de 18 litros;
b - comprar apenas galões de 3,6 litros;
c - misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga 
    e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''
import math

metroquadrado = int(input('Quantos m² você vai pintar ?\n'))
litroslata = metroquadrado / 6
litroslatoes = metroquadrado / 3.6

#Calculo da lata de 18 litros
if litroslata <= 18:
     print(f'Com {metroquadrado} m² será necessário uma lata de tinta de 18l, custa R$ 80.00')
  
else:
   latasdetinta = math.ceil(litroslata/18) #Essa função arrendonda o número para cima, o número mais próximo
   preco = latasdetinta * 80
   print(f'Com {metroquadrado} m² será necessário {latasdetinta} latas de tinta de 18l, custa R$ {preco:0.2f}')
  
#Calculo dos latões de 3,6 litros
if litroslatoes <= 3.6:
   print(f'Com {metroquadrado} m² será necessário uma lata de tinta de 3.6l, custa R$ 80.00')
  
else:
   latasdetinta = math.ceil(litroslatoes/3.6) #Essa função arrendonda o número para cima, o número mais próximo
   preco = latasdetinta * 25
   print(f'Com {metroquadrado} m² será necessário {latasdetinta} latas de tinta de 3.6l, custa R$ {preco:0.2f}')
