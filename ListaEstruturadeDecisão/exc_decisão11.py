'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    
    * salários até R$ 280,00 (incluindo) : aumento de 20%
    * salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    * salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    * salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    * o salário antes do reajuste;
    * o percentual de aumento aplicado;
    * o valor do aumento;
    * o novo salário, após o aumento.
'''
def reajuste_de_salario(salario:float): 
    if salario <= 280.00: #salários até R$ 280,00 (incluindo) : aumento de 20%
        reajuste = salario + (salario * 0.2)
        print(f'Seu salário atual é de R${salario:0.2f}, com reajuste de 20% passou a ser R${reajuste:0.2f}.')
    
    elif salario > 280.00 and salario <= 700.00: #salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
        reajuste = salario + (salario * 0.15)
        print(f'Seu salário atual é de R${salario:0.2f}, com reajuste de 15% passou a ser R${reajuste:0.2f}.')
    
    elif salario > 700.00 and salario <= 1500.00: #salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
        reajuste = salario + (salario * 0.1)
        print(f'Seu salário atual é de R${salario:0.2f}, com reajuste de 10% passou a ser R${reajuste:0.2f}.')
    
    elif salario > 1500.00: #salários de R$ 1500,00 em diante : aumento de 5%
        reajuste = salario + (salario * 0.05)
        print(f'Seu salário atual é de R${salario:0.2f}, com reajuste de 5% passou a ser R${reajuste:0.2f}.')
        


if __name__ == "__main__":
    salario = float(input('Digite seu salário: \n'))
    reajuste_de_salario(salario)