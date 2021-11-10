""" Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
Dica: utilize uma função de arredondamento."""
numero = 1.56

if isinstance(numero, int):
    print(f"{numero} é inteiro.")

elif isinstance(numero, float):
    print(f"{numero} é decimal.")

if not type(numero) is int or float:
    raise TypeError("A variável inserida não é int ou float.")
