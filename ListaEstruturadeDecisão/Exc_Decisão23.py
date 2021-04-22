''' Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
Dica: utilize uma função de arredondamento.'''

def verificar_conjunto_numerico(numero):
    if isinstance(numero, int):
        return f'{numero} é inteiro.'
    
    elif isinstance(numero, float):
        return f'{numero} é decimal.'
        
    if not type(numero) is int or float: 
        raise TypeError('A variável inserida não é int ou float.')

verificar_conjunto_numerico(1.56)
