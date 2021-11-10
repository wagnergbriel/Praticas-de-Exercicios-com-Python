"""Faça um Programa que leia três números e mostre-os em ordem decrescente."""
primeironumero = int(input("Digite o primeiro número:\n"))
segundonumero = int(input("Digite o segundo número:\n"))
terceironumero = int(input("Digite o terceiro número:\n"))

if terceironumero > segundonumero:
    aux = terceironumero
    terceironumero = segundonumero
    segundonumero = aux

if segundonumero > primeironumero:
    aux = segundonumero
    segundonumero = primeironumero
    primeironumero = aux

if terceironumero > segundonumero:
    aux = terceironumero
    terceironumero = segundonumero
    segundonumero = aux

print("\nNúmeros de forma decrescente:")
print(f"{primeironumero}, {segundonumero}, {terceironumero}")
