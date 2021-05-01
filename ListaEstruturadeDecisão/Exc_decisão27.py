''' Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.'''

def desconto_de_frutas():
    print('                 Até 5 Kg           Acima de 5 \n\
    Morango         R$ 2,50 por Kg          R$ 2,20 por Kg\n\
    Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg\n\
    -------------------------------------------------------\n')

    opcao = input('Digite o tipo de fruta que deseja comprar:\n\
        Digite Morango ou Maça.\n')
    
    quilos = int(input('Quantos quilos dejesa comprar ?\n'))
    
    #Preços das frutas

    MORANGOATE5KL = 2.50
    MAÇAATE5KL = 1.80

    MORANGOMAISDE5KL = 2.20
    MAÇAMAISDE5KL = 1.50

    valor = 0
    desconto = 0


    if opcao == "Morango" and quilos <= 5:
            valor = quilos * MORANGOATE5KL
       
    elif opcao == "Morango" and quilos > 5:
            valor = quilos * MORANGOMAISDE5KL
    
    elif opcao == "Maça" and quilos <= 5:
            valor = quilos * MAÇAATE5KL

    elif opcao == "Maça" and quilos > 5:
            valor = quilos * MAÇAMAISDE5KL

    elif opcao != "Morango" and  opcao != "Maça":
            return 'Não foi selecionado a opção correta. Digite Morango ou Maça !'
           
    #Calculo de Desconto da promoção
    if quilos > 8 or valor > 25:
        desconto = valor - (valor * 0.10)
        return f'------------------------------------\n\
            {opcao}:\n\
            Valor Total:\t{valor:0.2f}\n\
            Valor da promoção:\t{desconto:0.2f}'
    else:
        return f'------------------------------------\n\
            {opcao}:\n\
            Valor Total:\t{valor:0.2f}\n'





print(desconto_de_frutas())