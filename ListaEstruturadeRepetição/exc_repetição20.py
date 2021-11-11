"""  Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial 
várias vezes e limitando o fatorial a números inteiros positivos e menores que 16."""
fatorial = 15
resultado = 1
contagem = 1

while contagem <= fatorial:
    if fatorial > 0 and fatorial < 16:
        resultado *= contagem
        contagem += 1
        print(f"{contagem - 1}! = {resultado}")
    else:
        raise ValueError("Ultrapassou o limite da contagem.")
