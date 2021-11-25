""" Faça um programa que calcule o mostre a média aritmética de N notas."""
soma_das_notas = 0
quantidade_de_notas = int(input("Digite a quantidade de notas a ser calculada:\n"))

for i in range(1, quantidade_de_notas + 1):
    notas = int(input(f"Digite a {i}° nota:\n"))
    soma_das_notas += notas

media_aritimetica = soma_das_notas / quantidade_de_notas
print(f"\nA média aritmética é {media_aritimetica:0.1f}")
