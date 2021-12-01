""" Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
Um número primo é aquele que é divisível apenas por um e por ele mesmo.
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo."""
while True:
    numero_primo = int(
        input("Digite o número para ver se é primo:(Digite zero para parar o loop)\n")
    )
    if numero_primo % 2 == 1 and numero_primo != 2:
        print(f"{numero_primo} é um número primo")
    elif numero_primo == 0:
        break
    else:
        print(f"{numero_primo} não é um número primo")
