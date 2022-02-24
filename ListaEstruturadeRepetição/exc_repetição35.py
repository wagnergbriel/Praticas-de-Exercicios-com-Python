""" Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário."""
lista_de_numeros_primos = []
numero_limite = int(
        input("Digite o número limite para ver quais são primos:\n")
    )
contagem = 0
while True:
    if contagem % 2 == 1 and contagem != 2:
        lista_de_numeros_primos.append(str(contagem))
    elif contagem == numero_limite:
        break
    contagem += 1
print(f"Os números primos de 1 até {numero_limite} são: {', '.join(lista_de_numeros_primos)}")
