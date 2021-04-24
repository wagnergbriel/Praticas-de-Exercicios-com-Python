''' Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.'''

def desconto_de_frutas():
    print('                 Até 5 Kg           Acima de 5 \n\
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg\n\
    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg')

    opcao = input('Digite o tipo de fruta que deseja comprar:\n\
        \tDigite Morango ou Maça.')
    
    quilos = int(input('Quantos quilos dejesa comprar ?'))

    #preço até 5 kg
    morango5kg = 2.50
    maça5kg = 1.80

    #preço acima de 5 kg
    morangomais5kg = 2.20
    maçamais5kg = 1.50

    if opcao == "Morango" and quilos <= 5:
        valor = quilos * morango5kg
        return f'------------------------------------\n\
            Morango:\n\
            Valor Total:\t{valor:0.2f}\n'

            if quilos > 8 or valor > 25:
                valor = quilos * morangomais5kg
                desconto = valor - (valor * 0.10)
                return f'------------------------------------\n\
                    Morango:\n\
                    Valor Total:\t{valor:0.2f}\n\
                    Valor da promoção:\t{desconto:0.2f}'







print(desconto_de_frutas())