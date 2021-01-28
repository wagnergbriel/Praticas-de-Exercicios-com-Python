'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
utilizando as seguintes fórmulas:

Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''

def peso_ideal(altura:float, genero:str):
    
    if (genero == 'M'): #Se o genero for masculino, será executado este bloco
        peso =  (72.7*altura) - 58
        print(f'Seu peso ideal é {peso:0.1f}')
    
    elif (genero == 'F'): #Se o genero for Feminino, será executado este bloco
        peso = (62.1*altura) - 44.7
        print(f'Seu peso ideal é {peso:0.1f}')
    
    elif (genero != 'M' or 'F'): #Se o genero informado não estiver nas opções, será executado este bloco
            raise ValueError('Não faz parte das opções.')

if __name__ == "__main__":
    altura = float(input('Qual é a sua altura? \n'))
    genero = str(input('Qual é o seu sexo?-----Se for Homem digite M, se for mulher digite F----\n'))
    peso_ideal(altura, genero)