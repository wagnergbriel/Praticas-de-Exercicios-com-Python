""" Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados."""
numero_primo = int(input("Digite o número para verificar se é primo ou não:\n"))

for i in range(1, numero_primo):
    if i % 2 == 1 and i != 2:
        print(f"{i} é um número primo", end=" | ")
