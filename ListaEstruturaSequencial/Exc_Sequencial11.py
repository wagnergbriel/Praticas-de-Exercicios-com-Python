'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a - o produto do dobro do primeiro com metade do segundo .
b - a soma do triplo do primeiro com o terceiro.
c - o terceiro elevado ao cubo.
'''

def calculo_de_tres_variaveis(numero1:int, numero2:int, numero3:float):
    a = (numero1 * 2)*(numero2/2)
    print(f'O produto do primeiro com metade do segundo: {a}\n')
    
    b = (numero3 * 3)+ numero3
    print(f'A soma do triplo do primeiro com o terceiro: {b}\n')
    
    c = pow(numero3,3)
    print(f'O terceiro elevado ao cubo: {c}\n')

if __name__ == "__main__":
    calculo_de_tres_variaveis(10,20,4.5)