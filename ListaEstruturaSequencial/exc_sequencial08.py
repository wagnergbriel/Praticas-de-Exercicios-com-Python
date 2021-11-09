'''
    Faça um Programa que pergunte quanto você ganha por hora e o 
    número de horas trabalhadas no mês. 
    Calcule e mostre o total do seu salário no referido mês.
'''

ganhoporhora = int(input('Quanto você ganha por hora ?\n'))
qtdhorastrabalhadasmes = int(input('Quantas horas trabalhou no mês ?\n'))
salariototal = salarioporhora * horastrabalhadasmes
print(f'Seu salário total no mês é {salariototal}')

