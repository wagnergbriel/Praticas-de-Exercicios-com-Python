""" O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99.
Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário"""
preço_do_pão = float(input(f"Digite o preço do pão:\n"))

print("\nTabela de preço\n")

for unidade_do_pão in range(1, 5 + 1):
    preço_na_tabela = preço_do_pão * unidade_do_pão
    print(f"{unidade_do_pão} - R$ {preço_na_tabela:0.2f}\n")
