'''Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
Dica: utilize o operador módulo (resto da divisão).'''

def verificar_paridade(numero:int):
    if numero % 2 == 0: 
        numero_par = numero
        return f'{numero_par} é par.' 
    else: 
        numero_impar = numero
        return f'{numero_impar} é impar.'

if __name__ == '__main__':
    print(verificar_paridade(101))
