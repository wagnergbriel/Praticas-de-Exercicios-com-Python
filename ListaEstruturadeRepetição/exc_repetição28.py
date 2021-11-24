""" Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
O usuário deverá informar a quantidade de CDs e o valor para em cada um."""
quantidade_de_cds = int(input("Informe a quantidade de cds:\n"))
soma_do_preco_do_cds = 0

for cds in range(1, quantidade_de_cds + 1):
    preco_dos_cds = float(input(f"Qual é o preço do {cds}° cd?\n"))
    soma_do_preco_do_cds += preco_dos_cds

media_dos_preco_dos_cds = soma_do_preco_do_cds / quantidade_de_cds
print(f"A média dos preços do cds é de R$ {media_dos_preco_dos_cds:0.2f}")
