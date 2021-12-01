""" Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120."""
import math

numero = int(input("Digite o número para obter fatorial:\n"))
contagem = numero + 1
fatorial = math.factorial(numero)
print(f"{numero}!:")
for i in range(1, numero + 1):
    contagem -= 1
    print(contagem, end="*")
print(f" = {fatorial}")
