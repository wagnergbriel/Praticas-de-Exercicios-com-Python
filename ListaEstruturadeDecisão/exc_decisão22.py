"""Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
Dica: utilize o operador módulo (resto da divisão)."""
numero = 101

if numero % 2 == 0:
    numero_par = numero
    print(f"{numero_par} é par.")
else:
    numero_impar = numero
    print(f"{numero_impar} é impar.")
