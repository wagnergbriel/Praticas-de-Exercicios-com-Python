'''
Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''

def verificar_genero(sexo):
    if sexo in('F', 'f'):
        print('Sexo Feminino')
    elif sexo in ('M','m'):
        print('sexo masculino')
    else:
        print('Sexo invalido')

if __name__ == "__main__":
    sexo = input('Digite a letra que indica o seu sexo:\n')
    verificar_genero(sexo)