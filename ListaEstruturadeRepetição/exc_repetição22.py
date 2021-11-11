''' Altere o programa de cálculo dos números primos, 
informando, caso o número não seja primo, por quais número ele é divisível.'''
numeroprimo = int(input("Digite o número para verificar se é primo ou não:\n"))
divisor = 0

for i in range(1, numeroprimo + 1):
    if numeroprimo % i == 0:
        divisor += 1

if divisor == 2:
    print(f"{numeroprimo} é um número primo")
else:
    print(f"{numeroprimo} não é um número primo, é divisível por {divisor} números")
