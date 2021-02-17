'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
    que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
    mas não é descontado (é a empresa que deposita). 
O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
    Desconto do IR:
    * Salário Bruto até 900 (inclusive) - isento
    * Salário Bruto até 1500 (inclusive) - desconto de 5%
    * Salário Bruto até 2500 (inclusive) - desconto de 10%
    * Salário Bruto acima de 2500 - desconto de 20% 
    
    Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
    No exemplo o valor da hora é 5 e a quantidade de hora é 220.
'''
def calculo_do_salario_liquido(valorporhora:int, horastrabalhadas:int):
    salariobruto = valorporhora * horastrabalhadas
    
    if salariobruto <= 900.00: #Salário Bruto até 900 (inclusive) - isento
        print(f'Seu salario bruto é de R${salariobruto:0.2f}, você está isento dos descontos.')
    
    elif salariobruto > 900.00 and salariobruto <= 1500.00: #Salário Bruto até 1500 (inclusive) - desconto de 5%
        IR = salariobruto * 0.05
        INSS = salariobruto * 0.1
        FGTS = salariobruto * 0.11
        descontosalario = IR + INSS
        salarioliquido = (salariobruto - descontosalario) + FGTS
        print(f'\n                Salário Bruto: ({valorporhora}*{horastrabalhadas})  R${salariobruto:0.2f}\n\
                (-) IR (5%)  :      R${IR:0.2f}\n\
                (-) INSS (10%):     R${INSS:0.2f}\n\
                FGTS (11%)   :      R${FGTS:0.2f}\n\n\
                Total de Desconto:  R${descontosalario:0.2f}\n\
                Salário Liquido  :  R${salarioliquido:0.2f}')
    
    elif salariobruto > 1500.00 and salariobruto <= 2500.00: #Salário Bruto até 2500 (inclusive) - desconto de 10%
        IR = salariobruto * 0.1
        INSS = salariobruto * 0.1
        FGTS = salariobruto * 0.11
        descontosalario = IR + INSS
        salarioliquido = (salariobruto - descontosalario) + FGTS
        print(f'\n                Salário Bruto: ({valorporhora}*{horastrabalhadas})  R${salariobruto:0.2f}\n\
                (-) IR (10%)  :      R${IR:0.2f}\n\
                (-) INSS (10%):     R${INSS:0.2f}\n\
                FGTS (11%)   :      R${FGTS:0.2f}\n\n\
                Total de Desconto:  R${descontosalario:0.2f}\n\
                Salário Liquido  :  R${salarioliquido:0.2f}')
    
    elif salariobruto > 2500.00: #Salário Bruto acima de 2500 - desconto de 20% 
        IR = salariobruto * 0.2
        INSS = salariobruto * 0.1
        FGTS = salariobruto * 0.11
        descontosalario = IR + INSS
        salarioliquido = (salariobruto - descontosalario) + FGTS
        print(f'\n                Salário Bruto: ({valorporhora}*{horastrabalhadas})  R${salariobruto:0.2f}\n\
                (-) IR (20%)  :      R${IR:0.2f}\n\
                (-) INSS (10%):     R${INSS:0.2f}\n\
                FGTS (11%)   :      R${FGTS:0.2f}\n\n\
                Total de Desconto:  R${descontosalario:0.2f}\n\
                Salário Liquido  :  R${salarioliquido:0.2f}')
    
    


if __name__ == "__main__":
    valorporhora = int(input('Valor por hora de trabalho:\n'))
    horastrabalhadas = int(input('Horas trabalhadas:\n'))
    calculo_do_salario_liquido(valorporhora,horastrabalhadas)