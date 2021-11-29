""" O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
Faça um programa que implemente uma caixa registradora rudimentar. 
O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. 
Um valor zero deve ser informado pelo operador para indicar o final da compra. 
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu,
para então calcular e mostrar o valor do troco. 
Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra."""
lista_de_preço = []
soma_dos_produtos = 0
contador = 0
valor_do_pagamento = 0

while True:
    contador += 1
    preço_do_produto = float(input("Digite o preço do produto:\n"))
    if preço_do_produto > 0:
        lista_de_preço.append(preço_do_produto)
    else:
        valor_do_pagamento = float(input("Qual valor do pagamento dos produtos:\n"))
        break


print("tabela de preço:\n")
for preço in lista_de_preço:
    soma_dos_produtos += preço
    print(f"Produto = R$ {preço}\n")

troco = valor_do_pagamento - soma_dos_produtos
print(f"Valor total: R$ {soma_dos_produtos}\n")

if troco > 0:
    print(f"Troco: R$ {troco}")
else:
    print(f"Falta R$ {troco * -1} para pagar")