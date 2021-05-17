''' Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool: até 20 litros, desconto de 3% por litro;
acima de 20 litros, desconto de 5% por litro.

Gasolina:até 20 litros, desconto de 4% por litro; 
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.'''

def desconto_de_combustivel():
    print('O preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.\n')
    combustivel = input('Qual combustível você quer para abastecer seu carro ?\n\
                Digitel A para Alcool\n\
                Digite G para Gasolina.\n')
    
    litroscomustivel = float(input('Quantos litros deseja colocar ?\n'))
    gasolina = 2.50
    alcool = 1.90

    if combustivel.upper() == "A" and litroscomustivel <= 20:
        valordocombustivel = litroscomustivel * alcool
        desconto = valordocombustivel - (valordocombustivel * 0.3)
    
        return f'----------------------------------------\n\
        Abestecimento com Alcool:\n\
            Valor Total:\t{valordocombustivel:0.2f}\n\
            Valor da promoção:\t{desconto:0.2f}'
    
    elif combustivel.upper() == "A" and litroscomustivel > 20:
        valordocombustivel = litroscomustivel * alcool
        desconto = valordocombustivel - (valordocombustivel * 0.5)

        return f'----------------------------------------\n\
        Abestecimento com Alcool:\n\
            Valor Total:\t{valordocombustivel:0.2f}\n\
            Valor da promoção:\t{desconto:0.2f}'

    elif combustivel.upper() == "G" and litroscomustivel <= 20:
        valordocombustivel = litroscomustivel * gasolina
        desconto = valordocombustivel - (valordocombustivel * 0.4)

        return f'----------------------------------------\n\
        Abestecimento com Gasolina:\n\
            Valor Total:\t{valordocombustivel:0.2f}\n\
            Valor da promoção:\t{desconto:0.2f}'

    elif combustivel.upper() == "G" and litroscomustivel > 20:
        valordocombustivel = litroscomustivel * gasolina
        desconto = valordocombustivel - (valordocombustivel * 0.6)

        return f'----------------------------------------\n\
        Abestecimento com Gasolina:\n\
            Valor Total:\t{valordocombustivel:0.2f}\n\
            Valor da promoção:\t{desconto:0.2f}'



print(desconto_de_combustivel())