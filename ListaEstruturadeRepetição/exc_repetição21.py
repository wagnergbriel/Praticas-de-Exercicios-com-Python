""" Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1."""
numeroprimo = int(input("Digite o número para verificar se é primo ou não:\n"))
divisor = 0

for i in range(1, numeroprimo + 1):
    if numeroprimo % i == 0:
        divisor += 1

if divisor == 2:
    print(f"{numeroprimo} é um número primo")
else:
    print(f"{numeroprimo} não é um número primo")
