'''
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
Imprima os dados do programa com as mensagens adequadas.

'''
def calculo_do_regulamento_de_pesca(quilo:float):
    if quilo < 50: #Verificar se é menor que o limite de peso do regulamento
        print(f'Sua mercadoria está dentro do regulamento, são {quilo:0.2f} quilos')
    
    elif quilo > 50: #Verifica se ultrapassa o limite de peso do regulamento
        excesso = quilo - 50 
        multa = excesso * 4.00
        print(f'Sua mercadoria ultrapassou {excesso:0.2f} quilos e a multa é de R$ {multa:0.2f}.')


if __name__ == "__main__":
    mercadoria = float(input('Quantos quilos tem sua mercadoria ?\n'))
    calculo_do_regulamento_de_pesca(mercadoria)
