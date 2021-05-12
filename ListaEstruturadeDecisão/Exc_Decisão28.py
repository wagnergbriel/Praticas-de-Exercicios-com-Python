'''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
porém não há limites para a quantidade de carne por cliente. 
Se compra for feita no cartão Tabajara o cliente receberá ainda um DESCONTO de 5% sobre o total da compra.
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal,
contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento,
VALOR do DESCONTO e VALOR a pagar.
'''
print(
    'O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:\n\
                      Até 5 Kg           Acima de 5 Kg\n\
    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg\n\
    Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg\n\
    Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg\n\
    -------------------------------------------------------\n'
)

opcao = input('Digite o tipo de carne que deseja comprar:\n\
        Digite File Duplo/Alcantra/Picanha.\n'
)

quilos = int(input('Quantos quilos dejesa comprar ?\n'))

pagamento = input('Deseja pagar com o cartão Tabajara ?\n\
    Digite S para sim ou N para não\n'
)

#preço das carnes
FILEDUPLOATE5KL = 4.90
ALCATRAATE5KL = 5.90
PICANHAATE5KL = 6.90

FILEDUPLOMAISDE5KL = 5.80
ALCATRAMAISDE5KL = 6.80
PICANHAMAISDE5KL = 7.80

VALOR = 0
DESCONTO = 0

if opcao == "File Duplo" and quilos <= 5:
    VALOR = quilos * FILEDUPLOATE5KL
       
elif opcao == "Alcatra" and quilos <= 5:
    VALOR = quilos * ALCATRAATE5KL
    
elif opcao == "Picanha" and quilos <= 5:
    VALOR = quilos * PICANHAATE5KL

#Carne acima de 5kl
elif opcao == "File Duplo" and quilos > 5:
    VALOR = quilos * FILEDUPLOMAISDE5KL

elif opcao == "Alcatra" and quilos > 5:
    VALOR = quilos * ALCATRAMAISDE5KL

elif opcao == "Picanha" and quilos > 5:
    VALOR = quilos * PICANHAMAISDE5KL


#Calculo de DESCONTO da promoção
if pagamento == 's'.upper():
    DESCONTO = VALOR - (VALOR * 0.05)
    print(f'------------------------------------\n\
        {opcao}:\n\
        Pagamento no cartão: {pagamento}\n\
        VALOR Total:\t{VALOR:0.2f}\n\
        VALOR da promoção:\t{DESCONTO:0.2f}'
    )
else:
    print(f'------------------------------------\n\
        {opcao}:\n\
        Pagamento no cartão: {pagamento}\n\
        VALOR Total:\t{VALOR:0.2f}\n'
    )