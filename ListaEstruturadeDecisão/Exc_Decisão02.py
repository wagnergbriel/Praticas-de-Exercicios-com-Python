#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

def verificar_do_numero(numero:int):
    if numero > 0:
        print(f'{numero} é positivo.')
    else:
        print(f'{numero} é negativo.')

if __name__ == "__main__":
    numero = int(input('Digite um número:\n'))
    verificar_do_numero(numero)