"""Faça um programa que pergunte o preço de três produtos e informe qual produto 
    você deve comprar, sabendo que a decisão é sempre pelo mais barato."""
primeiropreco = float(input("Digite o primeiro preço:\n"))
segundopreco = float(input("Digite o segundo preço:\n"))
terceiropreco = float(input("Digite o terceiro preço:\n"))

if primeiropreco < segundopreco and primeiropreco < terceiropreco:
    print(
        f"Entre R$ {primeiropreco:0.2f}, R$ {segundopreco:0.2f}, R$ {terceiropreco:0.2f} o menor preço é R$ {primeiropreco:0.2f}"
    )

elif segundopreco < primeiropreco and segundopreco < terceiropreco:
    print(
        f"Entre R$ {primeiropreco:0.2f} R$ {segundopreco:0.2f} R$ {terceiropreco:0.2f} o menor preço é R$ {segundopreco:0.2f}"
    )

elif terceiropreco < primeiropreco and terceiropreco < segundopreco:
    print(
        f"Entre R$ {primeiropreco:0.2f}, R$ {segundopreco:0.2f}, R$ {terceiropreco:0.2f} o menor preço é R$ {terceiropreco:0.2f}"
    )
