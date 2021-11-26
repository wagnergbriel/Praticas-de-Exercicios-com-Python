""" O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto 
cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. 
Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. 
Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos"""
lista_de_preços = []
numero_da_tabela = 0

for i in range(1, 5 + 1):
    preço = float(input(f"Digite o {i}° preço da tabela:\n"))
    lista_de_preços.append(preço)

print("\nTabela de preço\n")

for preço_na_tabela in lista_de_preços:
    numero_da_tabela += 1
    print(f"{numero_da_tabela} - R$ {preço_na_tabela:0.2f}\n")
