"""Faça um Programa que leia três números e mostre o maior deles."""
primeironumero = int(input("Digite o primeiro número:\n"))
segundonumero = int(input("Digite o segundo número:\n"))
terceironumero = int(input("Digite o terceiro número:\n"))

if primeironumero > segundonumero and primeironumero > terceironumero:
    print(
        f"Entre {primeironumero}, {segundonumero}, {terceironumero}\
        o maior deles é {primeironumero}"
    )
elif segundonumero > primeironumero and segundonumero > terceironumero:
    print(
        f"Entre {primeironumero},{segundonumero},{terceironumero}\
        o maior deles é {segundonumero}"
    )
elif terceironumero > primeironumero and terceironumero > segundonumero:
    print(
        f"Entre {primeironumero}, {segundonumero}, {terceironumero}\
        o maior deles é {terceironumero}"
    )
