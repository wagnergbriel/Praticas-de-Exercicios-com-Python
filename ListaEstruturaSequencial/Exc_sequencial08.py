#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

def total_salario_por_mes(salarioporhora, horastrabalhadasmes):
    salariototal = salarioporhora * horastrabalhadasmes
    print(f'Seu salário total no mês é {salariototal}')

if __name__ == "__main__":
    ganhoporhora = int(input('Quanto você ganha por hora ?\n'))
    qtdhorastrabalhadasmes = int(input('Quantas horas trabalhou no mês ?\n'))
    total_salario_por_mes(ganhoporhora, qtdhorastrabalhadasmes)

