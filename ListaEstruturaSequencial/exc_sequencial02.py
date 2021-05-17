#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

def imprimir_numero(num):
    print(f'O número informado foi {num}')

if __name__ == "__main__":
    numero = int(input('Digite um número: \n'))
    imprimir_numero(numero)