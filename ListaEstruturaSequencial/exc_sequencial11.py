'''
    Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    a - o produto do dobro do primeiro com metade do segundo .
    b - a soma do triplo do primeiro com o terceiro.
    c - o terceiro elevado ao cubo.
'''
numero1 = int(input("Digite o primeiro numero:\n"))
numero2 = int(input("Digite o segundo numero:\n"))
numero3 = float(input("Digite o terceiro numero:\n"))
a = (numero1 * 2)*(numero2/2)
print(f'O produto do primeiro com metade do segundo: {a}\n')
    
b = (numero3 * 3)+ numero3
print(f'A soma do triplo do primeiro com o terceiro: {b}\n')
    
c = pow(numero3,3)
print(f'O terceiro elevado ao cubo: {c:.1f}\n')
