#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.)
#   se digitar outro valor deve aparecer valor inválido.

def dias_da_semana(dia:int):
    if dia == 1:
        print('Hoje é Domingo.')
    
    elif dia == 2:
        print('Hoje é Segunda-Feira.')
    
    elif dia == 3:
        print('Hoje é Terça-Feira.')
    
    elif dia == 4:
        print('Hoje é Quarta-Feira.')
    
    elif dia == 5:
        print('Hoje é Quinta-Feira.')
    
    elif dia == 6:
        print('Hoje é Sexta-Feira.')
    
    elif dia == 7:
        print('Hoje é Sábado.')
    
    else:
        print('Valor Inválido.')

if __name__ == "__main__":
    dia = int(input('Digite o número que corresponde o dia da semana:\n'))
    dias_da_semana(dia)