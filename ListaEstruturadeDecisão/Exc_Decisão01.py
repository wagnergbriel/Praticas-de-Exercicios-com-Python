#Faça um Programa que peça dois números e imprima o maior deles.

def maior_numero(primeironumero:int, segundonumero:int):
    if primeironumero > segundonumero:
        print(f'{primeironumero} é maior que {segundonumero}')
    else:
        print(f'{segundonumero} é maior que {primeironumero}')

if __name__== "__main__":
    maior_numero(20,5)
