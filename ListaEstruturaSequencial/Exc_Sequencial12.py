'''
Tendo como dados de entrada a altura de uma pessoa, 
construa um algoritmo que calcule seu peso ideal, 
usando a seguinte fórmula: (72.7*altura) - 58
'''

def peso_ideal(altura:float):
    peso =  (72.7*altura) - 58
    print(f'Seu peso ideal é {peso:0.1f}')

if __name__ == "__main__":
    peso_ideal(1.60)