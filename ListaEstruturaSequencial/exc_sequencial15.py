'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

a - salário bruto.
b - quanto pagou ao INSS.
c - quanto pagou ao sindicato.
d - o salário líquido.
e - calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

def total_salario_por_mes(salarioporhora, horastrabalhadasmes):
    salariototal = salarioporhora * horastrabalhadasmes
    print(f'\nSeu salário bruto no mês é R$ {salariototal:0.2f}\n')

    ir = salariototal * 0.11
    print(f'Seu imposto de renda no mês é R$ {ir:0.2f}\n')

    inss = salariototal * 0.08
    print(f'Seu INSS no mês é R$ {inss:0.2f}\n')

    sindicato = salariototal * 0.05
    print(f'Seu sindicato no mês é R$ {sindicato:0.2f}\n')
    
    salarioliquido = salariototal - (ir + inss + sindicato)
    print(f'Seu salário líquido no mês ficou R$ {salarioliquido:0.2f}\n')


if __name__ == "__main__":
    ganhoporhora = int(input('Quanto você ganha por hora ?\n'))
    qtdhorastrabalhadasmes = int(input('Quantas horas trabalhou no mês ?\n'))
    total_salario_por_mes(ganhoporhora, qtdhorastrabalhadasmes)