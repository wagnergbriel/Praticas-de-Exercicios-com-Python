#Faça um Programa que peça dois números e imprima a soma.

def soma(numero1, numero2):
    soma = int(numero1) + int(numero2)
    print(f'{numero1} + {numero2} = {soma}')

if __name__ == "__main__":
    numero1 = input('Digite o primeiro número: \n')
    numero2 = input('Digite o segundo número: \n')
    soma(numero1,numero2)