''' Altere o programa de cálculo dos números primos, 
informando, caso o número não seja primo, por quais número ele é divisível.'''
numero_primo = int(input("Digite o número para verificar se é primo ou não:\n"))
divisor = 0

for i in range(1, numero_primo + 1):
    if numero_primo % i == 0:
        divisor += 1

if divisor == 2:
    print(f"{numero_primo} é um número primo")
else:
    print(f"{numero_primo} não é um número primo, é divisível por {divisor} números")
