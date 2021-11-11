"""Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
Ex.: 5!=5.4.3.2.1=120"""
fatorial = 5
resultado = 1
contagem = 1

while contagem <= fatorial:
    resultado *= contagem
    contagem += 1
    print("----", resultado)
