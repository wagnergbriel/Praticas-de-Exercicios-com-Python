#Faça um Programa que leia três números e mostre o maior deles.

def maior_numero(primeironumero:int, segundonumero:int, terceironumero:int):
    if primeironumero > segundonumero and primeironumero > terceironumero:
        print(f'Entre {primeironumero}, {segundonumero}, {terceironumero} o maior deles é {primeironumero}')
    
    elif segundonumero > primeironumero and segundonumero > terceironumero:
        print(f'Entre {primeironumero}, {segundonumero}, {terceironumero} o maior deles é {segundonumero}')
    
    elif terceironumero > primeironumero and terceironumero > segundonumero:
        print(f'Entre {primeironumero}, {segundonumero}, {terceironumero} o maior deles é {terceironumero}')

if __name__ == "__main__":
    primeironumero = int(input('Digite o primeiro número:\n'))
    segundonumero = int(input('Digite o segundo número:\n'))
    terceironumero = int(input('Digite o terceiro número:\n'))
    maior_numero(primeironumero, segundonumero, terceironumero)