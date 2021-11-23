""" Faça um programa que calcule o mostre a média aritmética de N notas."""
somadasnotas = 0
quantidadenotas = int(input("Digite a quantidade de notas a ser calculada:\n"))

for i in range(1, quantidadenotas + 1):
    notas = int(input(f"Digite a {i}° nota:\n"))
    somadasnotas += notas

mediaaritimetica = somadasnotas / quantidadenotas
print(f"\nA média aritmética é {mediaaritimetica:0.1f}")
